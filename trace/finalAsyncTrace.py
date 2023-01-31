from __future__ import annotations
import tvm
import numpy as np
from tvm import te
import tvm.testing
import os


def print_mod(mod, name):
    if isinstance(mod, tvm.tir.Schedule):
        mod = mod.mod
    if not os.path.exists('bin'):
        os.system('mkdir bin')
    with open(f"bin/{name}.py", "w") as f:
        print("import tvm", file=f)
        print("from tvm import tir", file=f)
        print(mod.script(), file=f)
    with open(f"bin/{name}_lower.py", "w") as f:
        print("import tvm", file=f)
        print("from tvm import tir", file=f)
        print(tvm.lower(mod).script(), file=f)
    with open(f"bin/{name}_cuda_with_async.cu", "w") as f:
        with tvm.transform.PassContext(config={"tir.use_ptx_async_copy": 1}):
            rt_mod = tvm.build(sch.mod, target="cuda")
            print(rt_mod.imported_modules[0].get_source(), file=f)
    with open(f"bin/{name}_cuda_without_async.cu", "w") as f:
        with tvm.transform.PassContext(config={"tir.use_ptx_async_copy": 0}):
            rt_mod = tvm.build(sch.mod, target="cuda")
            print(rt_mod.imported_modules[0].get_source(), file=f)
    with open(f"bin/{name}_llvm.ll", "w") as f:
        rt_mod = tvm.build(sch.mod, target="cuda")
        print(rt_mod.get_source(), file=f)


def eval_mod(mod):
    if isinstance(mod, tvm.tir.Schedule):
        mod = mod.mod
    with tvm.transform.PassContext(config={"tir.use_ptx_async_copy": 1}):
        rt_mod = tvm.build(mod, target="cuda")
    dev = tvm.cuda(0)
    A_np = np.random.uniform(size=(1024, 1024)).astype("float32")
    B_np = np.random.uniform(size=(1024, 1024)).astype("float32")
    A_nd = tvm.nd.array(A_np, dev)
    B_nd = tvm.nd.array(B_np, dev)
    C_nd = tvm.nd.array(np.zeros((1024, 1024), dtype="float32"), dev)
    num_flop = 2 * 1024 * 1024 * 1024
    evaluator = rt_mod.time_evaluator("main", dev, number=10)
    print("GEMM speed: %f GFLOPS" % (num_flop / evaluator(A_nd, B_nd, C_nd).mean / 1e9))
    rt_mod(A_nd, B_nd, C_nd)
    tvm.testing.assert_allclose(C_nd.numpy(), np.dot(A_np.T, B_np), rtol=1e-5)


A = te.placeholder((1024, 1024), "float32", name="A")
B = te.placeholder((1024, 1024), "float32", name="B")
k = te.reduce_axis((0, 1024), name="k")
Y = te.compute((1024, 1024), lambda i, j: te.sum(A[k, i] * B[k, j], axis=k), name="Y")
GemmFunc = te.create_prim_func([A, B, Y]).with_attr({"global_symbol": "main"})
GemmModule = tvm.IRModule({"main": GemmFunc})
sch = tvm.tir.Schedule(GemmModule)

Y = sch.get_block(name="Y")
Y_local2gmem = sch.cache_write(block=Y, write_buffer_index=0, storage_scope="local")
A_gmem2smem = sch.cache_read(block=Y, read_buffer_index=0, storage_scope="shared.dyn")
A_smem2local = sch.cache_read(block=Y, read_buffer_index=0, storage_scope="local")
B_gmem2smem = sch.cache_read(block=Y, read_buffer_index=1, storage_scope="shared.dyn")
B_smem2local = sch.cache_read(block=Y, read_buffer_index=1, storage_scope="local")

I, J, K = sch.get_loops(block=Y)
temp_bx, temp_tx, warp_mma_m = sch.split(loop=I, factors=[8, 16, 8])
temp_by, temp_ty, warp_mma_n = sch.split(loop=J, factors=[8, 16, 8])
gemm_iteration_k, warp_mma_k = sch.split(loop=K, factors=[128, 8])
sch.reorder(temp_bx, temp_by, temp_tx, temp_ty, warp_mma_n, warp_mma_m)

bx = sch.fuse(temp_bx, temp_by)
sch.bind(loop=bx, thread_axis="blockIdx.x")

warp_idx_m, lane_offset_m_major, lane_offset_m_minor = sch.split(loop=temp_tx, factors=[4, 2, 2])
warp_idx_n, lane_offset_n = sch.split(loop=temp_ty, factors=[2, 8])
sch.reorder(bx, warp_idx_n, warp_idx_m, lane_offset_m_major, lane_offset_n, lane_offset_m_minor, gemm_iteration_k, warp_mma_k, warp_mma_n, warp_mma_m)
warp_idx = sch.fuse(warp_idx_n, warp_idx_m)
lane_idx = sch.fuse(lane_offset_m_major, lane_offset_n, lane_offset_m_minor)
tx = sch.fuse(warp_idx, lane_idx)
sch.bind(loop=tx, thread_axis="threadIdx.x")

sch.compute_at(block=A_smem2local, loop=warp_mma_k)
sch.compute_at(block=B_smem2local, loop=warp_mma_k)
sch.compute_at(block=A_gmem2smem, loop=gemm_iteration_k)
sch.compute_at(block=B_gmem2smem, loop=gemm_iteration_k)

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
ax0_0, ax0_1 = sch.split(loop=ax0, factors=[2, 4])
sch.vectorize(ax0_1)

ax0 = sch.get_loops(block=B_smem2local)[-1]
ax0_0, ax0_1 = sch.split(loop=ax0, factors=[2, 4])
sch.vectorize(ax0_1)

ax0A, ax1A = sch.get_loops(block=A_gmem2smem)[-2:]
ax01A = sch.fuse(ax0A, ax1A)
txA, jA = sch.split(loop=ax01A, factors=[256, 4])
sch.bind(loop=txA, thread_axis="threadIdx.x")
sch.vectorize(jA)

ax0B, ax1B = sch.get_loops(block=B_gmem2smem)[-2:]
ax01B = sch.fuse(ax0B, ax1B)
txB, jB = sch.split(loop=ax01B, factors=[256, 4])
sch.bind(loop=txB, thread_axis="threadIdx.x")

sch.reverse_compute_at(block=Y_local2gmem, loop=tx)

sch.unroll(warp_mma_k)
sch.unroll(warp_mma_n)
n, s = sch.split(loop=warp_mma_m, factors=[2, 4])
sch.unroll(n)
sch.vectorize(s)

Y_init = sch.decompose_reduction(block=Y, loop=gemm_iteration_k)
Y_init_m, Y_init_n = sch.get_loops(block=Y_init)[-2:]
sch.unroll(Y_init_m)
sch.unroll(Y_init_n)

Y_store2gmem_m, Y_store2gmem_n = sch.get_loops(Y_local2gmem)[-2:]
sch.unroll(Y_store2gmem_m)
n, s = sch.split(loop=Y_store2gmem_n, factors=[2, 4])
sch.vectorize(s)

# ref: https://github.com/apache/tvm-rfcs/blob/main/rfcs/0077-async-pipeline.md
sch.annotate(block_or_loop=warp_mma_k, ann_key="software_pipeline_stage", ann_val=[0, 0, 1])
sch.annotate(block_or_loop=warp_mma_k, ann_key="software_pipeline_order", ann_val=[0, 1, 2])
sch.annotate(block_or_loop=gemm_iteration_k, ann_key="software_pipeline_stage", ann_val=[0, 0, 2, 3, 3])
sch.annotate(block_or_loop=gemm_iteration_k, ann_key="software_pipeline_order", ann_val=[0, 1, 3, 2, 4])
sch.annotate(block_or_loop=gemm_iteration_k, ann_key="software_pipeline_async_stages", ann_val=[0, 1])

print_mod(sch, "tvm")
eval_mod(sch)
