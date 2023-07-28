import sys
import os
import numpy as np
import traceback

import tvm
import tvm.testing
from tvm import te
from tvm import meta_schedule as ms
from tvm.ir.module import IRModule
from tvm.target import Target

from typing import Callable, Dict, List, Optional, Union
from tvm.meta_schedule.builder import LocalBuilder
from tvm.runtime import NDArray, Module
from tvm._ffi import register_func
from tvm.tir.tensor_intrin import cuda  # get tensor intrin
from tvm.meta_schedule.testing.space_generation import (
    check_sketches,
    generate_design_space,
    print_sketches,
)

from util import get_mm_dirn, rdir, dbn


def multi_level_tiling_tensor_core(
    *,
    read_reuse_scope="shared.dyn",
    write_reuse_scope="shared",
    in_dtype="float16",
    out_dtype="float16",
    trans_b=False,
    use_software_pipeline=True,
) -> ms.schedule_rule.ScheduleRule:
    assert read_reuse_scope in ["shared", "shared.dyn"]
    assert write_reuse_scope in ["shared", "shared.dyn", "global"]
    if not isinstance(in_dtype, list):
        in_dtype = [in_dtype]
    if not isinstance(out_dtype, list):
        out_dtype = [out_dtype]
    if not isinstance(trans_b, list):
        trans_b = [trans_b]
    return ms.schedule_rule.MultiLevelTilingTensorCore(
        intrin_groups=[
            {
                "init": "mma_init_m16n8k8_f16",
                "load_a": "mma_load_m16n8k8_f16_A_shared_dyn",
                "load_b": "mma_load_m16n8k8_f16_B_shared_dyn",
                "compute": "mma_sync_m16n8k8_f16f16f16",
                "store": "mma_store_m16n8k8_f16_global",
            },
        ],
        structure="SSSRRSRS",
        tile_binds=["blockIdx.y", "blockIdx.x", "threadIdx.y"],
        max_innermost_factor=4,  # 64 // tensor intrin size
        vector_load_lens=[1, 2, 3, 4, 8, 16],
        reuse_read=ms.schedule_rule.ReuseType(
            req="must",
            levels=[4],
            scope=read_reuse_scope,
        ),
        reuse_write=ms.schedule_rule.ReuseType(
            # req="must" if write_reuse_scope.startswith("shared") else "no",
            req="no",
            levels=[2],
            scope=write_reuse_scope,
        ),
        use_software_pipeline=use_software_pipeline,
    )


M = int(sys.argv[1])
N = int(sys.argv[2])
K = int(sys.argv[3])
t = int(sys.argv[4])

original_block_name = "Y"

A = te.placeholder((M, K), "float16", name="A")
B = te.placeholder((K, N), "float16", name="B")
k = te.reduce_axis((0, K), name="k")
Y = te.compute((M, N), lambda i, j: te.sum(A[i, k] * B[k, j], axis=k), name=original_block_name)
GemmFunc = te.create_prim_func([A, B, Y]).with_attr({"global_symbol": "main"})
GemmModule = tvm.IRModule({"main": GemmFunc})


def initializer():

    @register_func("meta_schedule.builder.async_build")
    def async_build(mod: IRModule, target: Target, _params: Optional[Dict[str, NDArray]]) -> Module:
        """Async build function.

        Parameters
        ----------
        mod : IRModule
            The IRModule to be built.
        target : Target
            The target to be built.
        _params : Optional[Dict[str, NDArray]]
            The parameters to be used for the build. Must be None.

        Returns
        -------
        rt_mod : Module
            The built Module with async copy.
        """
        # pylint: disable=import-outside-toplevel
        from tvm.driver import build as tvm_build
        from tvm.tir.transform import RemoveWeightLayoutRewriteBlock
        # from tvm.tir.tensor_intrin import cuda  # re-import here for local builder


        # pylint: enable=import-outside-toplevel
        mod = RemoveWeightLayoutRewriteBlock(skip_ndarray_rewrite=True)(mod)
        with tvm.transform.PassContext(config={"tir.use_async_copy": 1}):
            rt_mod = tvm_build(mod, target=target)
        return rt_mod


db = ms.tir_integration.tune_tir(
    mod=GemmModule,
    target="nvidia/geforce-rtx-3080",
    work_dir=f"./{dbn}/{get_mm_dirn(M, N, K, t)}",
    max_trials_global=t,
    builder=LocalBuilder(f_build="meta_schedule.builder.async_build", initializer=initializer),
    space=ms.space_generator.PostOrderApply(
        sch_rules=[
            multi_level_tiling_tensor_core(out_dtype="float16")
        ],
    ),
)
sch = db.query_schedule(GemmModule, target=Target("nvidia/geforce-rtx-3080"), workload_name="main")

os.makedirs(f"{rdir}/{get_mm_dirn(M, N, K, t)}", exist_ok=True)

with open(f"{rdir}/{get_mm_dirn(M, N, K, t)}/script.py", "w") as f:
    print(sch.mod.script(), file=f)
with open(f"{rdir}/{get_mm_dirn(M, N, K, t)}/lower.py", "w") as f:
    print(tvm.lower(sch.mod).script(), file=f)
with open(f"{rdir}/{get_mm_dirn(M, N, K, t)}/trace.py", "w") as f:
    print(sch.trace, file=f)
with tvm.transform.PassContext(config={"tir.use_async_copy": 1}):
    rt_mod = tvm.build(sch.mod, target="cuda")
with open(f"{rdir}/{get_mm_dirn(M, N, K, t)}/cuda.cu", "w") as f:
    print(rt_mod.imported_modules[0].get_source(), file=f)
