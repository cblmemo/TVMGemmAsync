# from tvm.script import ir as I
# from tvm.script import tir as T

@I.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer((4096, 4096), "float16"), B: T.Buffer((4096, 4096), "float16"), Y: T.Buffer((4096, 4096), "float16")):
        T.func_attr({"global_symbol": "main", "tir.noalias": T.bool(True)})
        blockIdx_y = T.launch_thread("blockIdx.y", 16)
        Y_reindex_shared_dyn_wmma_accumulator = T.allocate([8192], "float16", "wmma.accumulator")
        A_reindex_shared_dyn = T.allocate([5120], "float16", "shared.dyn")
        B_reindex_shared_dyn = T.allocate([8448], "float16", "shared.dyn")
        A_reindex_shared_dyn_wmma_matrix_a = T.allocate([1024], "float16", "wmma.matrix_a")
        B_reindex_shared_dyn_wmma_matrix_b = T.allocate([2048], "float16", "wmma.matrix_b")
        blockIdx_x = T.launch_thread("blockIdx.x", 32)
        threadIdx_y = T.launch_thread("threadIdx.y", 4)
        threadIdx_x = T.launch_thread("threadIdx.x", 32)
        for ax0_0_3_init, ax1_0_3_init, ax0_0_4_init, ax1_0_4_init in T.grid(2, 2, 2, 4):
            T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, ax0_0_3_init * 16 + ax0_0_4_init * 8 + ax1_0_3_init * 4 + ax1_0_4_init, T.float32(0))
        for ax2_0_0 in range(128):
            A_reindex_shared_dyn_1 = T.decl_buffer((128, 32), "float16", data=A_reindex_shared_dyn, strides=(40, 1), scope="shared.dyn")
            B_reindex_shared_dyn_1 = T.decl_buffer((32, 256), "float16", data=B_reindex_shared_dyn, strides=(264, 1), scope="shared.dyn")
            for ax0_ax1_fused_0 in range(4):
                A_reindex_shared_dyn_2 = T.Buffer((5120,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
                A_1 = T.Buffer((16777216,), "float16", data=A.data)
                A_reindex_shared_dyn_2[ax0_ax1_fused_0 * 1280 + threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8:ax0_ax1_fused_0 * 1280 + threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8 + 8] = A_1[blockIdx_y // 4 * 4194304 + blockIdx_x // 4 * 524288 + ax0_ax1_fused_0 * 131072 + threadIdx_y * 32768 + threadIdx_x // 4 * 4096 + ax2_0_0 * 32 + threadIdx_x % 4 * 8:blockIdx_y // 4 * 4194304 + blockIdx_x // 4 * 524288 + ax0_ax1_fused_0 * 131072 + threadIdx_y * 32768 + threadIdx_x // 4 * 4096 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 8]
            for ax0_ax1_fused_0 in range(8):
                B_reindex_shared_dyn_2 = T.Buffer((8448,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
                B_1 = T.Buffer((16777216,), "float16", data=B.data)
                B_reindex_shared_dyn_2[ax0_ax1_fused_0 * 1056 + threadIdx_y * 264 + threadIdx_x * 8:ax0_ax1_fused_0 * 1056 + threadIdx_y * 264 + threadIdx_x * 8 + 8] = B_1[ax2_0_0 * 131072 + ax0_ax1_fused_0 * 16384 + threadIdx_y * 4096 + blockIdx_y % 4 * 1024 + blockIdx_x % 4 * 256 + threadIdx_x * 8:ax2_0_0 * 131072 + ax0_ax1_fused_0 * 16384 + threadIdx_y * 4096 + blockIdx_y % 4 * 1024 + blockIdx_x % 4 * 256 + threadIdx_x * 8 + 8]
            for ax2_0_1 in range(2):
                for ax0_0 in range(4):
                    T.tvm_load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a, 16, 16, 16, ax0_0, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y // 2 * 2560 + ax0_0 * 640 + ax2_0_1 * 16, 640, 1), 40, "row_major")
                for ax1_0 in range(8):
                    T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, ax1_0, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax2_0_1 * 4224 + threadIdx_y % 2 * 128 + ax1_0 * 16, 4224, 1), 264, "row_major")
                for ax0_0_3, ax1_0_3, ax0_0_4, ax1_0_4 in T.grid(2, 2, 2, 4):
                    cse_var_2: T.int32 = ax1_0_3 * 4
                    cse_var_1: T.int32 = ax0_0_3 * 16 + ax0_0_4 * 8 + cse_var_2 + ax1_0_4
                    T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, cse_var_1, A_reindex_shared_dyn_wmma_matrix_a, ax0_0_3 * 2 + ax0_0_4, B_reindex_shared_dyn_wmma_matrix_b, cse_var_2 + ax1_0_4, Y_reindex_shared_dyn_wmma_accumulator, cse_var_1)
        for ax2 in range(4):
            for ax3 in range(8):
                T.tvm_store_matrix_sync(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, ax2 * 8 + ax3, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, threadIdx_y * 2048 + ax3 * 256, 256, 2), 16, "row_major")
            for ax0_ax1_ax3_ax4_ax5_fused_0 in range(8):
                Y_1 = T.Buffer((16777216,), "float16", data=Y.data)
                B_reindex_shared_dyn_1 = T.Buffer((8192,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
                Y_1[blockIdx_y // 4 * 4194304 + blockIdx_x // 4 * 524288 + ax0_ax1_ax3_ax4_ax5_fused_0 // 4 * 262144 + ax2 * 65536 + threadIdx_x // 2 * 4096 + blockIdx_y % 4 * 1024 + blockIdx_x % 4 * 256 + ax0_ax1_ax3_ax4_ax5_fused_0 % 4 * 64 + threadIdx_y * 16 + threadIdx_x % 2 * 8:blockIdx_y // 4 * 4194304 + blockIdx_x // 4 * 524288 + ax0_ax1_ax3_ax4_ax5_fused_0 // 4 * 262144 + ax2 * 65536 + threadIdx_x // 2 * 4096 + blockIdx_y % 4 * 1024 + blockIdx_x % 4 * 256 + ax0_ax1_ax3_ax4_ax5_fused_0 % 4 * 64 + threadIdx_y * 16 + threadIdx_x % 2 * 8 + 8] = B_reindex_shared_dyn_1[ax0_ax1_ax3_ax4_ax5_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x * 8:ax0_ax1_ax3_ax4_ax5_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x * 8 + 8]
