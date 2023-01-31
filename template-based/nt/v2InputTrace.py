from __future__ import annotations
import tvm
import numpy as np
from tvm import te
import tvm.testing
import os
import sys

class Shape:
    def __init__(self, m, n, k):
        self.mm = m
        self.nn = n
        self.kk = k
    def m(self):
        return self.mm
    def n(self):
        return self.nn
    def k(self):
        return self.kk
    def string(self):
        return str(self.mm) + ',' + str(self.nn) + ',' + str(self.kk)

# M, N, K = 1024, 1024, 1024
# M, N, K = 2048, 2048, 2048
M, N, K = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
# ThreadblockShape = Shape(128, 128, 8)
# WarpShape = Shape(32, 64, 8)
# ThreadblockShape = Shape(128, 256, 8)
# WarpShape = Shape(64, 64, 8)
ThreadblockShape = Shape(int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))
WarpShape = Shape(int(sys.argv[7]), int(sys.argv[8]), int(sys.argv[9]))
Stage = int(sys.argv[10])

WarpSize = 32
WarpNumThreadsM = 8 if WarpShape.m() > WarpShape.n() else 4
WarpNumThreads = Shape(WarpNumThreadsM, WarpSize // WarpNumThreadsM, -1)
ThreadTile = Shape(WarpShape.m() // WarpNumThreads.m(), WarpShape.n() // WarpNumThreads.n(), -1)
LaneLayout = 2 if (WarpShape.m() // WarpNumThreads.m() > 4 and WarpShape.n() // WarpNumThreads.n() > 4) else 1
LaneMmaShape = Shape(min(ThreadTile.m(), 4), min(ThreadTile.n(), 4), -1)
ThreadNumShape = Shape(ThreadblockShape.m() // WarpShape.m() * WarpNumThreads.m(), ThreadblockShape.n() // WarpShape.n() * WarpNumThreads.n(), -1)


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
    with open(f"bin/{name}_cuda.cu", "w") as f:
        with tvm.transform.PassContext(config={"tir.use_async_copy": 1}):
            rt_mod = tvm.build(sch.mod, target="cuda")
            print(rt_mod.imported_modules[0].get_source(), file=f)
    # with open(f"bin/{name}_cuda_without_async.cu", "w") as f:
    #     with tvm.transform.PassContext(config={"tir.use_async_copy": 0}):
    #         rt_mod = tvm.build(sch.mod, target="cuda")
    #         print(rt_mod.imported_modules[0].get_source(), file=f)
    # with open(f"bin/{name}_llvm.ll", "w") as f:
    #     rt_mod = tvm.build(sch.mod, target="cuda")
    #     print(rt_mod.get_source(), file=f)


def eval_mod(mod, use_async = True):
    if isinstance(mod, tvm.tir.Schedule):
        mod = mod.mod
    with tvm.transform.PassContext(config={"tir.use_async_copy": 1 if use_async else 0}):
        rt_mod = tvm.build(mod, target="cuda")
    dev = tvm.cuda(0)
    A_np = np.random.uniform(size=(K, M)).astype("float32")
    B_np = np.random.uniform(size=(K, N)).astype("float32")
    A_nd = tvm.nd.array(A_np, dev)
    B_nd = tvm.nd.array(B_np, dev)
    C_nd = tvm.nd.array(np.zeros((M, N), dtype="float32"), dev)
    num_flop = 2 * (M * N * K + M * N)
    evaluator = rt_mod.time_evaluator("main", dev, number=10)
    print("GEMM speed %s async copy: %f GFLOPS" % ("with" if use_async else "without", num_flop / evaluator(A_nd, B_nd, C_nd).mean / 1e9))
    rt_mod(A_nd, B_nd, C_nd)
    tvm.testing.assert_allclose(C_nd.numpy(), np.dot(A_np.T, B_np), rtol=1e-5)


def eval_myself(mod):
    def get_first_digit(s):
        st, ed = -1, -1
        for i, ch in enumerate(s):
            if ch.isdigit():
                st = i
                break
        for i in range(st, len(s)):
            if not s[i].isdigit():
                ed = i
                break
        return int(s[st:ed])
    if isinstance(mod, tvm.tir.Schedule):
        mod = mod.mod
    lower_script = tvm.lower(mod).script()
    # print('cp1')
    with tvm.transform.PassContext(config={"tir.use_async_copy": 1}):
        cuda_script = tvm.build(mod, target="cuda").imported_modules[0].get_source()
    # print('cp2')
    szA, szB, nb, nt = -1, -1, -1, -1
    for l in lower_script.split('\n'):
        raw = l.strip()
        if raw.startswith('A_shared_dyn = T.allocate'):
            szA = get_first_digit(raw)
        if raw.startswith('B_shared_dyn = T.allocate'):
            szB = get_first_digit(raw)
        if raw.startswith('T.launch_thread(blockIdx_x'):
            nb = get_first_digit(raw)
        if raw.startswith('T.launch_thread(threadIdx_x'):
            nt = get_first_digit(raw)
    assert szA != -1, 'A_shared size not found'
    assert szB != -1, 'B_shared size not found'
    assert nb != -1, 'block num not found'
    assert nt != -1, 'thread num not found'
    shared_size = (szA + szB) * 4
    with open('include/myself.cu', 'w') as f:
        f.write(cuda_script)
    with open('include/inc.h', 'w') as f:
        f.write('#include "myself.cu"\n')
        f.write(f'\n#define M {M}\n#define N {N}\n#define K {K}\n')
        f.write(f'\n#define SHARED_SIZE {shared_size}\n#define BLOCK_NUM {nb}\n#define THREAD_NUM {nt}\n')
    # print('cp3')
    os.system('nvcc speedTest.cu -o bin/cutlassMultiStage -I ../async_nt_cutlass/include -gencode=arch=compute_86,code=sm_86')
    # print('cp4')
    os.system('bin/cutlassMultiStage')

A = te.placeholder((K, M), "float32", name="A")
B = te.placeholder((K, N), "float32", name="B")
k = te.reduce_axis((0, K), name="k")
Y = te.compute((M, N), lambda i, j: te.sum(A[k, i] * B[k, j], axis=k), name="Y")
GemmFunc = te.create_prim_func([A, B, Y]).with_attr({"global_symbol": "main"})
GemmModule = tvm.IRModule({"main": GemmFunc})
sch = tvm.tir.Schedule(GemmModule)

Y = sch.get_block(name="Y")
Y_local2gmem = sch.cache_write(block=Y, write_buffer_index=0, storage_scope="local")
A_gmem2smem = sch.cache_read(block=Y, read_buffer_index=0, storage_scope="shared.dyn")
A_smem2local = sch.cache_read(block=Y, read_buffer_index=0, storage_scope="local")
B_gmem2smem = sch.cache_read(block=Y, read_buffer_index=1, storage_scope="shared.dyn")
B_smem2local = sch.cache_read(block=Y, read_buffer_index=1, storage_scope="local")

loopI, loopJ, loopK = sch.get_loops(block=Y)
temp_bx, temp_tx, warp_mma_m = sch.split(loop=loopI, factors=[
    (M + ThreadblockShape.m() - 1) // ThreadblockShape.m(),
    ThreadNumShape.m(),
    WarpShape.m() // WarpNumThreads.m()
])
temp_by, temp_ty, warp_mma_n = sch.split(loop=loopJ, factors=[
    (N + ThreadblockShape.n() - 1) // ThreadblockShape.n(),
    ThreadNumShape.n(),
    WarpShape.n() // WarpNumThreads.n()
])
gemm_iteration_k, warp_mma_k = sch.split(loop=loopK, factors=[
    (K + ThreadblockShape.k() - 1) // ThreadblockShape.k(),
    ThreadblockShape.k()
])
sch.reorder(temp_bx, temp_by, temp_tx, temp_ty, warp_mma_n, warp_mma_m)

bx = sch.fuse(temp_bx, temp_by)
sch.bind(loop=bx, thread_axis="blockIdx.x")

warp_idx_m, lane_offset_m = sch.split(loop=temp_tx, factors=[ThreadblockShape.m() // WarpShape.m(), WarpNumThreads.m()])
lane_offset_m_major, lane_offset_m_minor = sch.split(loop=lane_offset_m, factors=[WarpNumThreads.m() // LaneLayout, LaneLayout])
warp_idx_n, lane_offset_n = sch.split(loop=temp_ty, factors=[ThreadblockShape.n() // WarpShape.n(), WarpNumThreads.n()])
sch.reorder(bx, warp_idx_n, warp_idx_m, lane_offset_m_major, lane_offset_n, lane_offset_m_minor, gemm_iteration_k, warp_mma_k, warp_mma_n, warp_mma_m)
warp_idx = sch.fuse(warp_idx_n, warp_idx_m)
lane_idx = sch.fuse(lane_offset_m_major, lane_offset_n, lane_offset_m_minor)
tx = sch.fuse(warp_idx, lane_idx)
sch.bind(loop=tx, thread_axis="threadIdx.x")

sch.compute_at(block=A_smem2local, loop=warp_mma_k, preserve_unit_loops=True)
sch.compute_at(block=B_smem2local, loop=warp_mma_k, preserve_unit_loops=True)
sch.compute_at(block=A_gmem2smem, loop=gemm_iteration_k, preserve_unit_loops=True)
sch.compute_at(block=B_gmem2smem, loop=gemm_iteration_k, preserve_unit_loops=True)

# print(f"""sch.transform_layout(block=A_smem2local, buffer=("read", 0), index_map=lambda i, j: (i, 
#     (j // {ThreadblockShape.m()}) * {ThreadblockShape.m()} + # threadblock_offset
#     ((j % {ThreadblockShape.m()}) // {WarpShape.m()}) * {WarpShape.m()} +  # warp_idx % 4
#     ((j % {WarpShape.m()}) // {(WarpShape.m() // (WarpNumThreads.m() // LaneLayout))}) * {(LaneMmaShape.m() * LaneLayout)} + # lane_idx // 16
#     ((j % {(WarpShape.m() // (WarpNumThreads.m() // LaneLayout))}) // {(WarpShape.m() // (WarpNumThreads.m() // LaneLayout) // LaneLayout)}) * {LaneMmaShape.m()} + # lane_idx % 2
#     ((j % {(WarpShape.m() // (WarpNumThreads.m() // LaneLayout) // LaneLayout)}) // {LaneMmaShape.m()}) * {(WarpNumThreads.m() * LaneMmaShape.m())} + (j % {(WarpShape.m() // (WarpNumThreads.m() // LaneLayout) // LaneLayout)}) % {LaneMmaShape.m()} # warp_mma_m
# ))""")
sch.transform_layout(block=A_smem2local, buffer=("read", 0), index_map=lambda i, j: (i, 
    (j // ThreadblockShape.m()) * ThreadblockShape.m() + # threadblock_offset
    ((j % ThreadblockShape.m()) // WarpShape.m()) * WarpShape.m() +  # warp_idx % 4
    ((j % WarpShape.m()) // (WarpShape.m() // (WarpNumThreads.m() // LaneLayout))) * (LaneMmaShape.m() * LaneLayout) + # lane_idx // 16
    ((j % (WarpShape.m() // (WarpNumThreads.m() // LaneLayout))) // (WarpShape.m() // (WarpNumThreads.m() // LaneLayout) // LaneLayout)) * LaneMmaShape.m() + # lane_idx % 2
    ((j % (WarpShape.m() // (WarpNumThreads.m() // LaneLayout) // LaneLayout)) // LaneMmaShape.m()) * (WarpNumThreads.m() * LaneMmaShape.m()) + (j % (WarpShape.m() // (WarpNumThreads.m() // LaneLayout) // LaneLayout)) % LaneMmaShape.m() # warp_mma_m
))

# print(f"""sch.transform_layout(block=B_smem2local, buffer=("read", 0), index_map=lambda i, j: (i, 
#     (j // {ThreadblockShape.n()}) * {ThreadblockShape.n()} + # threadblock_offset
#     ((j % {ThreadblockShape.n()}) // {WarpShape.n()}) * {WarpShape.n()} + # warp_idx // 4
#     ((j % {WarpShape.n()}) // {(WarpShape.n() // WarpNumThreads.n())}) * {LaneMmaShape.n()} + # (lane_idx % 16) // 2
#     ((j % {(WarpShape.n() // WarpNumThreads.n())}) // {LaneMmaShape.n()}) * {(ThreadTile.n() * LaneMmaShape.n())} + ((j % {(WarpShape.n() // WarpNumThreads.n())}) % {LaneMmaShape.n()}) # temp_warp_mma_n
# ))""")
sch.transform_layout(block=B_smem2local, buffer=("read", 0), index_map=lambda i, j: (i, 
    (j // ThreadblockShape.n()) * ThreadblockShape.n() + # threadblock_offset
    ((j % ThreadblockShape.n()) // WarpShape.n()) * WarpShape.n() + # warp_idx // 4
    ((j % WarpShape.n()) // (WarpShape.n() // WarpNumThreads.n())) * LaneMmaShape.n() + # (lane_idx % 16) // 2
    ((j % (WarpShape.n() // WarpNumThreads.n())) // LaneMmaShape.n()) * (WarpNumThreads.n() * LaneMmaShape.n()) + ((j % (WarpShape.n() // WarpNumThreads.n())) % LaneMmaShape.n()) # temp_warp_mma_n
))

ax0 = sch.get_loops(block=A_smem2local)[-1]
ax0_0, ax0_1 = sch.split(loop=ax0, factors=[None, LaneMmaShape.m()])
sch.unroll(ax0_0)
sch.vectorize(ax0_1)

ax0 = sch.get_loops(block=B_smem2local)[-1]
ax0_0, ax0_1 = sch.split(loop=ax0, factors=[None, LaneMmaShape.n()])
sch.unroll(ax0_0)
sch.vectorize(ax0_1)

ax0A, ax1A = sch.get_loops(block=A_gmem2smem)[-2:]
ax01A = sch.fuse(ax0A, ax1A)
a, b, njA, jA = sch.split(loop=ax01A, factors=[ThreadNumShape.m(), ThreadNumShape.n(), None, 4])
sch.unroll(njA)
txA = sch.fuse(a, b)
sch.bind(loop=txA, thread_axis="threadIdx.x")
sch.vectorize(jA)
# sch.unroll(jA)

ax0B, ax1B = sch.get_loops(block=B_gmem2smem)[-2:]
ax01B = sch.fuse(ax0B, ax1B)
a, b, njB, jB = sch.split(loop=ax01B, factors=[ThreadNumShape.m(), ThreadNumShape.n(), None, 4])
sch.unroll(njB)
txB = sch.fuse(a, b)
sch.bind(loop=txB, thread_axis="threadIdx.x")
# sch.vectorize(jB)
sch.unroll(jB)

sch.reverse_compute_at(block=Y_local2gmem, loop=tx, preserve_unit_loops=True)

sch.unroll(warp_mma_k)
sch.unroll(warp_mma_n)
n, s = sch.split(loop=warp_mma_m, factors=[None, 4])
sch.unroll(n)
sch.vectorize(s)
# sch.unroll(warp_mma_m)

Y_init = sch.decompose_reduction(block=Y, loop=gemm_iteration_k)
Y_init_m, Y_init_n = sch.get_loops(block=Y_init)[-2:]
sch.unroll(Y_init_m)
sch.unroll(Y_init_n)

Y_store2gmem_m, Y_store2gmem_n = sch.get_loops(Y_local2gmem)[-2:]
sch.unroll(Y_store2gmem_m)
n, s = sch.split(loop=Y_store2gmem_n, factors=[None, 4])
sch.unroll(n)
sch.vectorize(s)

# ref: https://github.com/apache/tvm-rfcs/blob/main/rfcs/0077-async-pipeline.md
sch.annotate(block_or_loop=warp_mma_k, ann_key="software_pipeline_stage", ann_val=[0, 0, 1])
sch.annotate(block_or_loop=warp_mma_k, ann_key="software_pipeline_order", ann_val=[0, 1, 2])
sch.annotate(block_or_loop=gemm_iteration_k, ann_key="software_pipeline_stage", ann_val=[0, 0, Stage - 2, Stage - 1, Stage - 1])
sch.annotate(block_or_loop=gemm_iteration_k, ann_key="software_pipeline_order", ann_val=[0, 1, 3, 2, 4])
sch.annotate(block_or_loop=gemm_iteration_k, ann_key="software_pipeline_async_stages", ann_val=[0, 1])

print_mod(sch, f'M={M}_N={N}_K={K}_tbs=({ThreadblockShape.string()})_ws=({WarpShape.string()})_stage={Stage}')
# eval_mod(sch, use_async=True)
# print('start eval')
# print_mod(sch, 'unknown')
eval_myself(sch)
