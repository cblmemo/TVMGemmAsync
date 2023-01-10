import sys
import tvm
from tvm import meta_schedule as ms
from tvm.ir.module import IRModule
from tvm.script import tir as T
import numpy as np
from tvm import te
import os

from typing import Callable, Dict, List, Optional, Union
from tvm.target import Target
from tvm.meta_schedule.builder import LocalBuilder
from tvm.runtime import NDArray, Module
from tvm._ffi import register_func

use_async = True

M = int(sys.argv[1])
N = int(sys.argv[2])
K = int(sys.argv[3])
t = int(sys.argv[4])

A = te.placeholder((K, M), "float32", name="A")
B = te.placeholder((K, N), "float32", name="B")
k = te.reduce_axis((0, K), name="k")
Y = te.compute((M, N), lambda i, j: te.sum(A[k, i] * B[k, j], axis=k), name="Y")
GemmFunc = te.create_prim_func([A, B, Y]).with_attr({"global_symbol": "main"})
GemmModule = tvm.IRModule({"main": GemmFunc})

def initializer():
    @register_func("meta_schedule.builder.async_build")
    def async_build(mod: IRModule, target: Target, _params: Optional[Dict[str, NDArray]]) -> Module:
        from tvm.driver import build as tvm_build
        from tvm.tir.transform import RemoveWeightLayoutRewriteBlock

        mod = RemoveWeightLayoutRewriteBlock(skip_ndarray_rewrite=True)(mod)
        with tvm.transform.PassContext(config={"tir.use_async_copy": 1 if use_async else 0}):
            rt_mod = tvm_build(mod, target=target)
        return rt_mod

db = ms.tir_integration.tune_tir(
    mod=GemmModule,
    target="nvidia/geforce-rtx-3080",
    work_dir=f"./old_db/M={M}_N={N}_K={K}",
    max_trials_global=t,
    builder=LocalBuilder(
        f_build="meta_schedule.builder.async_build",
        initializer=initializer
    ),
    runner=ms.runner.RPCRunner(  # type: ignore
        rpc_config=ms.runner.RPCConfig(
            tracker_host="172.16.2.241",
            tracker_port=4445,
            tracker_key="rtx-3080",
            session_timeout_sec=600,
        ),
        alloc_repeat=1,
    ),
)
sch = db.query_schedule(GemmModule, target=Target("nvidia/geforce-rtx-3080"), workload_name="main")

with open(f"old_outputs/M={M}_N={N}_K={K}/script.py", "w") as f:
    print(sch.mod.script(), file=f)
with open(f"old_outputs/M={M}_N={N}_K={K}/lower.py", "w") as f:
    print(tvm.lower(sch.mod).script(), file=f)
with open(f"old_outputs/M={M}_N={N}_K={K}/trace.py", "w") as f:
    print(sch.trace, file=f)
with tvm.transform.PassContext(config={"tir.use_async_copy": 1 if use_async else 0}):
    rt_mod = tvm.build(sch.mod, target="cuda")
with open(f"old_outputs/M={M}_N={N}_K={K}/cuda.cu", "w") as f:
    print(rt_mod.imported_modules[0].get_source(), file=f)

a_np = np.random.rand(M, K).astype(A.dtype)
b_np = np.random.rand(K, N).astype(B.dtype)
c_np = a_np @ b_np
a_tvm = tvm.nd.array(a_np.T, device=tvm.cuda(0))
b_tvm = tvm.nd.array(b_np, device=tvm.cuda(0))
c_tvm = tvm.nd.array(np.empty((M, N)).astype(Y.dtype), device=tvm.cuda(0))
rt_mod(a_tvm, b_tvm, c_tvm)
assert np.allclose(c_tvm.numpy(), c_np)

time_f = rt_mod.time_evaluator(rt_mod.entry_name, dev=tvm.cuda(0), number=100)
time = time_f(a_tvm, b_tvm, c_tvm).mean

flop = M * N * K * 2
print("GFLOPS: %.2f" % (flop / time / 1e9))

with open('finished_task.txt', 'a') as f:
    f.write(f'\n[FINISH | old] M={M} N={N} K={K}')
