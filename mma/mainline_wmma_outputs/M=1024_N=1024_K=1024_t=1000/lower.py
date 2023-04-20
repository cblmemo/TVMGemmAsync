# from tvm.script import ir as I
# from tvm.script import tir as T

@I.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer((1024, 1024), "float16"), B: T.Buffer((1024, 1024), "float16"), Y: T.Buffer((1024, 1024), "float16")):
        T.func_attr({"global_symbol": "main", "tir.noalias": T.bool(True)})
        blockIdx_y = T.launch_thread("blockIdx.y", 8)
        Y_reindex_shared_dyn_wmma_accumulator = T.allocate([1024], "float16", "wmma.accumulator")
        A_reindex_shared_dyn = T.allocate([2560], "float16", "shared.dyn")
        B_reindex_shared_dyn = T.allocate([4352], "float16", "shared.dyn")
        A_reindex_shared_dyn_wmma_matrix_a = T.allocate([2048], "float16", "wmma.matrix_a")
        B_reindex_shared_dyn_wmma_matrix_b = T.allocate([512], "float16", "wmma.matrix_b")
        blockIdx_x = T.launch_thread("blockIdx.x", 16)
        threadIdx_y = T.launch_thread("threadIdx.y", 8)
        threadIdx_x = T.launch_thread("threadIdx.x", 32)
        for ax0_0_3_init in range(4):
            T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, ax0_0_3_init, T.float32(0))
        for ax2_0_0 in range(32):
            A_reindex_shared_dyn_1 = T.decl_buffer((64, 32), "float16", data=A_reindex_shared_dyn, strides=(40, 1), scope="shared.dyn")
            B_reindex_shared_dyn_1 = T.decl_buffer((32, 128), "float16", data=B_reindex_shared_dyn, strides=(136, 1), scope="shared.dyn")
            for ax0_ax1_fused_0 in range(2):
                A_reindex_shared_dyn_2 = T.Buffer((2560,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
                A_1 = T.Buffer((1048576,), "float16", data=A.data)
                A_reindex_shared_dyn_2[ax0_ax1_fused_0 * 1280 + threadIdx_y * 160 + threadIdx_x // 8 * 40 + threadIdx_x % 8 * 4:ax0_ax1_fused_0 * 1280 + threadIdx_y * 160 + threadIdx_x // 8 * 40 + threadIdx_x % 8 * 4 + 4] = A_1[blockIdx_y // 2 * 262144 + blockIdx_x // 4 * 65536 + ax0_ax1_fused_0 * 32768 + threadIdx_y * 4096 + threadIdx_x // 8 * 1024 + ax2_0_0 * 32 + threadIdx_x % 8 * 4:blockIdx_y // 2 * 262144 + blockIdx_x // 4 * 65536 + ax0_ax1_fused_0 * 32768 + threadIdx_y * 4096 + threadIdx_x // 8 * 1024 + ax2_0_0 * 32 + threadIdx_x % 8 * 4 + 4]
            for ax0_ax1_fused_0 in range(4):
                B_reindex_shared_dyn_2 = T.Buffer((4352,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
                B_1 = T.Buffer((1048576,), "float16", data=B.data)
                B_reindex_shared_dyn_2[ax0_ax1_fused_0 * 1088 + threadIdx_y * 136 + threadIdx_x * 4:ax0_ax1_fused_0 * 1088 + threadIdx_y * 136 + threadIdx_x * 4 + 4] = B_1[ax2_0_0 * 32768 + ax0_ax1_fused_0 * 8192 + threadIdx_y * 1024 + blockIdx_y % 2 * 512 + blockIdx_x % 4 * 128 + threadIdx_x * 4:ax2_0_0 * 32768 + ax0_ax1_fused_0 * 8192 + threadIdx_y * 1024 + blockIdx_y % 2 * 512 + blockIdx_x % 4 * 128 + threadIdx_x * 4 + 4]
            for ax0_0, ax1_0 in T.grid(4, 2):
                T.tvm_load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a, 16, 16, 16, ax0_0 * 2 + ax1_0, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax0_0 * 640 + ax1_0 * 16, 640, 1), 40, "row_major")
            for ax0_0 in range(2):
                T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, ax0_0, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax0_0 * 2176 + threadIdx_y * 16, 2176, 1), 136, "row_major")
            for ax0_0_3, ax2_0_2 in T.grid(4, 2):
                T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, ax0_0_3, A_reindex_shared_dyn_wmma_matrix_a, ax0_0_3 * 2 + ax2_0_2, B_reindex_shared_dyn_wmma_matrix_b, ax2_0_2, Y_reindex_shared_dyn_wmma_accumulator, ax0_0_3)
        for ax2 in range(4):
            T.tvm_store_matrix_sync(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, ax2, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 256, 256, 2), 16, "row_major")
            Y_1 = T.Buffer((1048576,), "float16", data=Y.data)
            A_reindex_shared_dyn_1 = T.Buffer((2048,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
            Y_1[blockIdx_y // 2 * 262144 + blockIdx_x // 4 * 65536 + ax2 * 16384 + threadIdx_x // 2 * 1024 + blockIdx_y % 2 * 512 + blockIdx_x % 4 * 128 + threadIdx_y * 16 + threadIdx_x % 2 * 8:blockIdx_y // 2 * 262144 + blockIdx_x // 4 * 65536 + ax2 * 16384 + threadIdx_x // 2 * 1024 + blockIdx_y % 2 * 512 + blockIdx_x % 4 * 128 + threadIdx_y * 16 + threadIdx_x % 2 * 8 + 8] = A_reindex_shared_dyn_1[threadIdx_y * 256 + threadIdx_x * 8:threadIdx_y * 256 + threadIdx_x * 8 + 8]
