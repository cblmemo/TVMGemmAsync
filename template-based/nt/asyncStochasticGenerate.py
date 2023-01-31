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

def stochastic_schedule_regular(sch: tvm.tir.Schedule):
    Y = sch.get_block(name="Y")
    Y_local2gmem = sch.cache_write(block=Y, write_buffer_index=0, storage_scope="local")
    A_gmem2smem = sch.cache_read(block=Y, read_buffer_index=0, storage_scope="shared.dyn")
    A_smem2local = sch.cache_read(block=Y, read_buffer_index=0, storage_scope="local")
    B_gmem2smem = sch.cache_read(block=Y, read_buffer_index=1, storage_scope="shared.dyn")
    B_smem2local = sch.cache_read(block=Y, read_buffer_index=1, storage_scope="local")

    I, J, K = sch.get_loops(block=Y)
    vtemp_bx, vtemp_tx, vwarp_mma_m = sch.sample_perfect_tile(loop=I, n=3, max_innermost_factor=16)
    vtemp_by, vtemp_ty, vwarp_mma_n = sch.sample_perfect_tile(loop=J, n=3, max_innermost_factor=16)
    vgemm_iteration_k, vwarp_mma_k = sch.sample_perfect_tile(loop=K, n=2, max_innermost_factor=8)
    temp_bx, temp_tx, warp_mma_m = sch.split(loop=I, factors=[vtemp_bx, vtemp_tx, vwarp_mma_m])
    temp_by, temp_ty, warp_mma_n = sch.split(loop=J, factors=[vtemp_by, vtemp_ty, vwarp_mma_n])
    gemm_iteration_k, warp_mma_k = sch.split(loop=K, factors=[vgemm_iteration_k, vwarp_mma_k])
    sch.reorder(temp_bx, temp_by, temp_tx, temp_ty, warp_mma_n, warp_mma_m)

    bx = sch.fuse(temp_bx, temp_by)
    sch.bind(loop=bx, thread_axis="blockIdx.x")

    vwarp_idx_m, vlane_offset_m_major, vlane_offset_m_minor = sch.sample_perfect_tile(loop=temp_tx, n=3)
    vwarp_idx_n, vlane_offset_n = sch.sample_perfect_tile(loop=temp_ty, n=2)
    warp_idx_m, lane_offset_m_major, lane_offset_m_minor = sch.split(loop=temp_tx, factors=[vwarp_idx_m, vlane_offset_m_major, vlane_offset_m_minor])
    warp_idx_n, lane_offset_n = sch.split(loop=temp_ty, factors=[vwarp_idx_n, vlane_offset_n])
    sch.reorder(bx, warp_idx_n, warp_idx_m, lane_offset_m_major, lane_offset_n, lane_offset_m_minor, gemm_iteration_k, warp_mma_k, warp_mma_n, warp_mma_m)
    warp_idx = sch.fuse(warp_idx_n, warp_idx_m)
    lane_idx = sch.fuse(lane_offset_m_major, lane_offset_n, lane_offset_m_minor)
    tx = sch.fuse(warp_idx, lane_idx)
    sch.bind(loop=tx, thread_axis="threadIdx.x")

    sch.compute_at(block=A_smem2local, loop=warp_mma_k, preserve_unit_loops=True)
    sch.compute_at(block=B_smem2local, loop=warp_mma_k, preserve_unit_loops=True)
    sch.compute_at(block=A_gmem2smem, loop=gemm_iteration_k, preserve_unit_loops=True)
    sch.compute_at(block=B_gmem2smem, loop=gemm_iteration_k, preserve_unit_loops=True)

    sch.transform_layout(block=A_smem2local, buffer=("read", 0), index_map=lambda i, j: (i, 
        (j // 128) * 128 + # threadblock_offset
        ((j % 128) // 32) * 32 +  # warp_idx % 4
        ((j % 32) // 16) * 8 + # lane_idx // 16
        ((j % 16) // 8) * 4 + # lane_idx % 2
        ((j % 8) // 4) * 16 + (j % 8) % 4 # warp_mma_m
    ))
    sch.transform_layout(block=B_smem2local, buffer=("read", 0), index_map=lambda i, j: (i, 
        (j // 128) * 128 + # threadblock_offset
        ((j % 128) // 64) * 64 + # warp_idx // 4
        ((j % 64) // 8) * 4 + # (lane_idx % 16) // 2
        ((j % 8) // 4) * 32 + ((j % 8) % 4) # temp_warp_mma_n
    ))

    ax0 = sch.get_loops(block=A_smem2local)[-1]
    ax0_0, ax0_1 = sch.split(loop=ax0, factors=[None, 4])
    sch.vectorize(ax0_1)

    ax0 = sch.get_loops(block=B_smem2local)[-1]
    ax0_0, ax0_1 = sch.split(loop=ax0, factors=[None, 4])
    sch.vectorize(ax0_1)

    ax0A, ax1A = sch.get_loops(block=A_gmem2smem)[-2:]
    ax01A = sch.fuse(ax0A, ax1A)
    temp_txA, temp_tyA, jA = sch.split(loop=ax01A, factors=[vtemp_tx, vtemp_ty, None])
    txA = sch.fuse(temp_txA, temp_tyA)
    sch.bind(loop=txA, thread_axis="threadIdx.x")
    sch.vectorize(jA)

    ax0B, ax1B = sch.get_loops(block=B_gmem2smem)[-2:]
    ax01B = sch.fuse(ax0B, ax1B)
    temp_txB, temp_tyB, jB = sch.split(loop=ax01B, factors=[vtemp_tx, vtemp_ty, None])
    txB = sch.fuse(temp_txB, temp_tyB)
    sch.bind(loop=txB, thread_axis="threadIdx.x")

    sch.reverse_compute_at(block=Y_local2gmem, loop=tx, preserve_unit_loops=True)

    sch.unroll(warp_mma_k)
    sch.unroll(warp_mma_n)
    n, s = sch.split(loop=warp_mma_m, factors=[None, 4])
    sch.unroll(n)
    sch.vectorize(s)

    Y_init = sch.decompose_reduction(block=Y, loop=gemm_iteration_k)
    Y_init_m, Y_init_n = sch.get_loops(block=Y_init)[-2:]
    sch.unroll(Y_init_m)
    sch.unroll(Y_init_n)

    Y_store2gmem_m, Y_store2gmem_n = sch.get_loops(Y_local2gmem)[-2:]
    sch.unroll(Y_store2gmem_m)
    n, s = sch.split(loop=Y_store2gmem_n, factors=[None, 4])
    sch.vectorize(s)

    stage = 4

    sch.annotate(block_or_loop=warp_mma_k, ann_key="software_pipeline_stage", ann_val=[0, 0, 1])
    sch.annotate(block_or_loop=warp_mma_k, ann_key="software_pipeline_order", ann_val=[0, 1, 2])
    sch.annotate(block_or_loop=gemm_iteration_k, ann_key="software_pipeline_stage", ann_val=[0, 0, stage - 2, stage - 1, stage - 1])
    sch.annotate(block_or_loop=gemm_iteration_k, ann_key="software_pipeline_order", ann_val=[0, 1, 3, 2, 4])
    sch.annotate(block_or_loop=gemm_iteration_k, ann_key="software_pipeline_async_stages", ann_val=[0, 1])

    return sch

def initializer():
    @register_func("meta_schedule.builder.async_build")
    def async_build(mod: IRModule, target: Target, _params: Optional[Dict[str, NDArray]]) -> Module:
        from tvm.driver import build as tvm_build
        from tvm.tir.transform import RemoveWeightLayoutRewriteBlock

        mod = RemoveWeightLayoutRewriteBlock(skip_ndarray_rewrite=True)(mod)
        with tvm.transform.PassContext(config={"tir.use_async_copy": 1 if use_async else 0}):
            rt_mod = tvm_build(mod, target=target)
        return rt_mod

def stochastic_schedule_irregular_8_multiple(sch: tvm.tir.Schedule):
    Y = sch.get_block(name="Y")
    Y_local2gmem = sch.cache_write(block=Y, write_buffer_index=0, storage_scope="local")
    A_gmem2smem = sch.cache_read(block=Y, read_buffer_index=0, storage_scope="shared.dyn")
    A_smem2local = sch.cache_read(block=Y, read_buffer_index=0, storage_scope="local")
    B_gmem2smem = sch.cache_read(block=Y, read_buffer_index=1, storage_scope="shared.dyn")
    B_smem2local = sch.cache_read(block=Y, read_buffer_index=1, storage_scope="local")

    I, J, K = sch.get_loops(block=Y)
    vtemp_bx, vtemp_tx, vwarp_mma_m = sch.sample_perfect_tile(loop=I, n=3, max_innermost_factor=16)
    vtemp_by, vtemp_ty, vwarp_mma_n = sch.sample_perfect_tile(loop=J, n=3, max_innermost_factor=16)
    vgemm_iteration_k, vwarp_mma_k = sch.sample_perfect_tile(loop=K, n=2, max_innermost_factor=8)
    temp_bx, temp_tx, warp_mma_m = sch.split(loop=I, factors=[vtemp_bx, vtemp_tx, vwarp_mma_m])
    temp_by, temp_ty, warp_mma_n = sch.split(loop=J, factors=[vtemp_by, vtemp_ty, vwarp_mma_n])
    gemm_iteration_k, warp_mma_k = sch.split(loop=K, factors=[vgemm_iteration_k, vwarp_mma_k])
    sch.reorder(temp_bx, temp_by, temp_tx, temp_ty, warp_mma_n, warp_mma_m)

    bx = sch.fuse(temp_bx, temp_by)
    sch.bind(loop=bx, thread_axis="blockIdx.x")

    vwarp_idx_m, vlane_offset_m_major, vlane_offset_m_minor = sch.sample_perfect_tile(loop=temp_tx, n=3)
    vwarp_idx_n, vlane_offset_n = sch.sample_perfect_tile(loop=temp_ty, n=2)
    warp_idx_m, lane_offset_m_major, lane_offset_m_minor = sch.split(loop=temp_tx, factors=[vwarp_idx_m, vlane_offset_m_major, vlane_offset_m_minor])
    warp_idx_n, lane_offset_n = sch.split(loop=temp_ty, factors=[vwarp_idx_n, vlane_offset_n])
    sch.reorder(bx, warp_idx_n, warp_idx_m, lane_offset_m_major, lane_offset_n, lane_offset_m_minor, gemm_iteration_k, warp_mma_k, warp_mma_n, warp_mma_m)
    warp_idx = sch.fuse(warp_idx_n, warp_idx_m)
    lane_idx = sch.fuse(lane_offset_m_major, lane_offset_n, lane_offset_m_minor)
    tx = sch.fuse(warp_idx, lane_idx)
    sch.bind(loop=tx, thread_axis="threadIdx.x")

    sch.compute_at(block=A_smem2local, loop=warp_mma_k, preserve_unit_loops=True)
    sch.compute_at(block=B_smem2local, loop=warp_mma_k, preserve_unit_loops=True)
    sch.compute_at(block=A_gmem2smem, loop=gemm_iteration_k, preserve_unit_loops=True)
    sch.compute_at(block=B_gmem2smem, loop=gemm_iteration_k, preserve_unit_loops=True)

    # sch.transform_layout(block=A_smem2local, buffer=("read", 0), index_map=lambda i, j: (i, 
    #     (j // 128) * 128 + # threadblock_offset
    #     ((j % 128) // 32) * 32 +  # warp_idx % 4
    #     ((j % 32) // 16) * 8 + # lane_idx // 16
    #     ((j % 16) // 8) * 4 + # lane_idx % 2
    #     ((j % 8) // 4) * 16 + (j % 8) % 4 # warp_mma_m
    # ))
    # sch.transform_layout(block=B_smem2local, buffer=("read", 0), index_map=lambda i, j: (i, 
    #     (j // 128) * 128 + # threadblock_offset
    #     ((j % 128) // 64) * 64 + # warp_idx // 4
    #     ((j % 64) // 8) * 4 + # (lane_idx % 16) // 2
    #     ((j % 8) // 4) * 32 + ((j % 8) % 4) # temp_warp_mma_n
    # ))

    ax0 = sch.get_loops(block=A_smem2local)[-1]
    vaxA0, vaxA1 = sch.sample_perfect_tile(loop=ax0, n=2)
    ax0_0, ax0_1 = sch.split(loop=ax0, factors=[vaxA0, vaxA1])
    sch.vectorize(ax0_1)

    ax0 = sch.get_loops(block=B_smem2local)[-1]
    vaxB0, vaxB1 = sch.sample_perfect_tile(loop=ax0, n=2)
    ax0_0, ax0_1 = sch.split(loop=ax0, factors=[vaxB0, vaxB1])
    sch.vectorize(ax0_1)

    ax0A, ax1A = sch.get_loops(block=A_gmem2smem)[-2:]
    ax01A = sch.fuse(ax0A, ax1A)
    temp_txA, temp_tyA, jA = sch.split(loop=ax01A, factors=[vtemp_tx, vtemp_ty, None])
    txA = sch.fuse(temp_txA, temp_tyA)
    sch.bind(loop=txA, thread_axis="threadIdx.x")
    # sch.vectorize(jA)

    ax0B, ax1B = sch.get_loops(block=B_gmem2smem)[-2:]
    ax01B = sch.fuse(ax0B, ax1B)
    temp_txB, temp_tyB, jB = sch.split(loop=ax01B, factors=[vtemp_tx, vtemp_ty, None])
    txB = sch.fuse(temp_txB, temp_tyB)
    sch.bind(loop=txB, thread_axis="threadIdx.x")

    sch.reverse_compute_at(block=Y_local2gmem, loop=tx, preserve_unit_loops=True)

    sch.unroll(warp_mma_k)
    sch.unroll(warp_mma_n)
    # n, s = sch.split(loop=warp_mma_m, factors=[None, 4])
    # sch.unroll(n)
    # sch.vectorize(s)
    sch.unroll(warp_mma_m)

    Y_init = sch.decompose_reduction(block=Y, loop=gemm_iteration_k)
    Y_init_m, Y_init_n = sch.get_loops(block=Y_init)[-2:]
    sch.unroll(Y_init_m)
    sch.unroll(Y_init_n)

    Y_store2gmem_m, Y_store2gmem_n = sch.get_loops(Y_local2gmem)[-2:]
    sch.unroll(Y_store2gmem_m)
    vaxY0, vaxY1 = sch.sample_perfect_tile(loop=Y_store2gmem_n, n=2)
    n, s = sch.split(loop=Y_store2gmem_n, factors=[vaxY0, vaxY1])
    sch.vectorize(s)

    sch.annotate(block_or_loop=warp_mma_k, ann_key="software_pipeline_stage", ann_val=[0, 0, 1])
    sch.annotate(block_or_loop=warp_mma_k, ann_key="software_pipeline_order", ann_val=[0, 1, 2])
    sch.annotate(block_or_loop=gemm_iteration_k, ann_key="software_pipeline_stage", ann_val=[0, 0, 2, 3, 3])
    sch.annotate(block_or_loop=gemm_iteration_k, ann_key="software_pipeline_order", ann_val=[0, 1, 3, 2, 4])
    sch.annotate(block_or_loop=gemm_iteration_k, ann_key="software_pipeline_async_stages", ann_val=[0, 1])

    return sch

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

def get_schedule_function():
    if M % 128 == 0 and N % 128 == 0 and K % 128 == 0:
        return stochastic_schedule_regular
    if M % 8 == 0 and N % 8 == 0 and K % 8 == 0:
        return stochastic_schedule_irregular_8_multiple
    raise

db = ms.tir_integration.tune_tir(
    mod=GemmModule,
    target="nvidia/geforce-rtx-3080",
    work_dir=f"./db/M={M}_N={N}_K={K}",
    space=ms.space_generator.ScheduleFn(
        get_schedule_function(),
        sch_rules=[],
        postprocs=[],
        mutator_probs={},
    ),
    max_trials_global=t,
    builder=LocalBuilder(
        f_build="meta_schedule.builder.async_build",
        initializer=initializer
    ),
    runner=ms.runner.RPCRunner(
        rpc_config=ms.runner.RPCConfig(
            tracker_host="172.16.2.241",
            tracker_port=4445,
            tracker_key="rtx-3080",
            session_timeout_sec=600,
        ),\
        alloc_repeat=1,
    ),
)
sch = db.query_schedule(GemmModule, target=Target("nvidia/geforce-rtx-3080"), workload_name="main")

with open(f"outputs/M={M}_N={N}_K={K}/script.py", "w") as f:
    print(sch.mod.script(), file=f)
with open(f"outputs/M={M}_N={N}_K={K}/lower.py", "w") as f:
    print(tvm.lower(sch.mod).script(), file=f)
with open(f"outputs/M={M}_N={N}_K={K}/trace.py", "w") as f:
    print(sch.trace, file=f)
with tvm.transform.PassContext(config={"tir.use_async_copy": 1 if use_async else 0}):
    rt_mod = tvm.build(sch.mod, target="cuda")
with open(f"outputs/M={M}_N={N}_K={K}/cuda.cu", "w") as f:
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

flop = 2 * (M * N * K + M * N)
print("GFLOPS: %.2f" % (flop / time / 1e9))

with open('finished_task.txt', 'a') as f:
    f.write(f'\n[FINISH | stochastic] M={M} N={N} K={K} t={t}')
