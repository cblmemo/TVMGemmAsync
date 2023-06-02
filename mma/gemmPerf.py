import sys
import os
import numpy as np
import traceback
import importlib

import tvm
import tvm.testing
from tvm import te
from tvm import meta_schedule as ms
from tvm.ir.module import IRModule
from tvm.target import Target
from tvm.tir import Schedule

from typing import Callable, Dict, List, Optional, Union
from tvm.meta_schedule.builder import LocalBuilder
from tvm.runtime import NDArray, Module
from tvm.contrib import cublas
from tvm._ffi import register_func

from util import get_mm_dirn, rdir

M = int(sys.argv[1])
N = int(sys.argv[2])
K = int(sys.argv[3])
t = int(sys.argv[4])

A = te.placeholder((M, K), "float16", name="A")
B = te.placeholder((K, N), "float16", name="B")
k = te.reduce_axis((0, K), name="k")
Y = te.compute((M, N), lambda i, j: te.sum(A[i, k] * B[k, j], axis=k), name="Y")
GemmFunc = te.create_prim_func([A, B, Y]).with_attr({"global_symbol": "main"})
GemmModule = tvm.IRModule({"main": GemmFunc})

sch = Schedule(GemmModule)

with open(f'{rdir}/{get_mm_dirn(M, N, K, t)}/trace.py', 'r+') as f:
    old = f.read()
    f.seek(0)
    f.write('from tvm import tir\nfrom tvm.tir import floordiv, floormod\n')
    f.write(old)

trace_module = importlib.import_module(f'{rdir}.{get_mm_dirn(M, N, K, t)}.trace')
method = getattr(trace_module, 'apply_trace')
method(sch)

with tvm.transform.PassContext(config={"tir.use_async_copy": 1}):
    rt_mod = tvm.build(sch.mod, target="cuda")

a_np = np.random.rand(M, K).astype(A.dtype)
b_np = np.random.rand(K, N).astype(B.dtype)
c_np = (a_np.astype("float32") @ b_np.astype("float32")).astype("float16")
a_tvm = tvm.nd.array(a_np, device=tvm.cuda(0))
b_tvm = tvm.nd.array(b_np, device=tvm.cuda(0))
c_tvm = tvm.nd.array(np.empty((M, N)).astype(Y.dtype), device=tvm.cuda(0))
rt_mod(a_tvm, b_tvm, c_tvm)
# assert np.allclose(c_tvm.numpy(), c_np, rtol=1e-2)

A_cublas = te.placeholder((M, K), name="A", dtype="float16")
B_cublas = te.placeholder((K, N), name="B", dtype="float16")
C_cublas = cublas.matmul(A_cublas, B_cublas, dtype="float16")
s = te.create_schedule(C_cublas.op)

dev = tvm.cuda(0)
f_cublas = tvm.build(s, [A_cublas, B_cublas, C_cublas], "cuda")
a_cublas = tvm.nd.array(a_np.astype("float16"), dev)
b_cublas = tvm.nd.array(b_np.astype("float16"), dev)
c_cublas = tvm.nd.array(np.zeros((M, N), dtype=C_cublas.dtype), dev)
f_cublas(a_cublas, b_cublas, c_cublas)

time_f = rt_mod.time_evaluator(rt_mod.entry_name, dev=tvm.cuda(0), number=10)
time = time_f(a_tvm, b_tvm, c_tvm).mean

flop = (M * N * K + M * N) * 2
print("%.2f" % (flop / time / 1e9))
print("%.9f" % time)

try:
    tvm.testing.assert_allclose(c_cublas.numpy(), c_tvm.numpy(), rtol=1e-2)
except:
    print("FAILED")
    print(traceback.format_exc())
