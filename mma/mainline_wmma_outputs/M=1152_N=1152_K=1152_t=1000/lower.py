# from tvm.script import ir as I
# from tvm.script import tir as T

@I.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer((1152, 1152), "float16"), B: T.Buffer((1152, 1152), "float16"), Y: T.Buffer((1152, 1152), "float16")):
        T.func_attr({"global_symbol": "main", "tir.noalias": T.bool(True)})
        blockIdx_y = T.launch_thread("blockIdx.y", 27)
        Y_reindex_shared_dyn_wmma_accumulator = T.allocate([3072], "float16", "wmma.accumulator")
        A_reindex_shared_dyn = T.allocate([2560], "float16", "shared.dyn")
        B_reindex_shared_dyn = T.allocate([6400], "float16", "shared.dyn")
        A_reindex_shared_dyn_wmma_matrix_a = T.allocate([1024], "float16", "wmma.matrix_a")
        B_reindex_shared_dyn_wmma_matrix_b = T.allocate([768], "float16", "wmma.matrix_b")
        blockIdx_x = T.launch_thread("blockIdx.x", 4)
        threadIdx_y = T.launch_thread("threadIdx.y", 4)
        threadIdx_x = T.launch_thread("threadIdx.x", 32)
        for ax1_0_3_init, ax0_0_4_init in T.grid(3, 4):
            T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, ax0_0_4_init * 3 + ax1_0_3_init, T.float32(0))
        for ax2_0_0 in range(36):
            A_reindex_shared_dyn_1 = T.decl_buffer((64, 32), "float16", data=A_reindex_shared_dyn, strides=(40, 1), scope="shared.dyn")
            B_reindex_shared_dyn_1 = T.decl_buffer((32, 192), "float16", data=B_reindex_shared_dyn, strides=(200, 1), scope="shared.dyn")
            for ax0_ax1_fused_0 in range(2):
                A_reindex_shared_dyn_2 = T.Buffer((2560,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
                A_1 = T.Buffer((1327104,), "float16", data=A.data)
                A_reindex_shared_dyn_2[ax0_ax1_fused_0 * 1280 + threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8:ax0_ax1_fused_0 * 1280 + threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8 + 8] = A_1[blockIdx_y // 3 * 147456 + blockIdx_x // 2 * 73728 + ax0_ax1_fused_0 * 36864 + threadIdx_y * 9216 + threadIdx_x // 4 * 1152 + ax2_0_0 * 32 + threadIdx_x % 4 * 8:blockIdx_y // 3 * 147456 + blockIdx_x // 2 * 73728 + ax0_ax1_fused_0 * 36864 + threadIdx_y * 9216 + threadIdx_x // 4 * 1152 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 8]
            for ax0_ax1_fused_0 in range(6):
                B_reindex_shared_dyn_2 = T.Buffer((6400,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
                B_1 = T.Buffer((1327104,), "float16", data=B.data)
                B_reindex_shared_dyn_2[(ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x * 8) // 192 * 200 + (ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x * 8) % 192:(ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x * 8) // 192 * 200 + (ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x * 8) % 192 + 8] = B_1[ax2_0_0 * 36864 + (ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x * 8) // 192 * 1152 + blockIdx_y % 3 * 384 + blockIdx_x % 2 * 192 + (ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x * 8) % 192:ax2_0_0 * 36864 + (ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x * 8) // 192 * 1152 + blockIdx_y % 3 * 384 + blockIdx_x % 2 * 192 + (ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x * 8) % 192 + 8]
            for ax2_0_1 in range(2):
                for ax0_0 in range(4):
                    T.tvm_load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a, 16, 16, 16, ax0_0, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax0_0 * 640 + ax2_0_1 * 16, 640, 1), 40, "row_major")
                for ax1_0 in range(3):
                    T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, ax1_0, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax2_0_1 * 3200 + threadIdx_y * 48 + ax1_0 * 16, 3200, 1), 200, "row_major")
                for ax1_0_3, ax0_0_4 in T.grid(3, 4):
                    cse_var_1: T.int32 = ax0_0_4 * 3 + ax1_0_3
                    T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, cse_var_1, A_reindex_shared_dyn_wmma_matrix_a, ax0_0_4, B_reindex_shared_dyn_wmma_matrix_b, ax1_0_3, Y_reindex_shared_dyn_wmma_accumulator, cse_var_1)
        for ax2 in range(4):
            for ax3 in range(3):
                T.tvm_store_matrix_sync(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, ax2 * 3 + ax3, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, threadIdx_y * 768 + ax3 * 256, 256, 2), 16, "row_major")
            for ax0_ax1_ax3_ax4_ax5_fused_0 in range(12):
                Y_1 = T.Buffer((1327104,), "float16", data=Y.data)
                B_reindex_shared_dyn_1 = T.Buffer((3072,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
                Y_1[blockIdx_y // 3 * 147456 + blockIdx_x // 2 * 73728 + ax2 * 18432 + threadIdx_y * 4608 + threadIdx_x // 8 * 1152 + blockIdx_y % 3 * 384 + blockIdx_x % 2 * 192 + ax0_ax1_ax3_ax4_ax5_fused_0 * 16 + threadIdx_x % 8 * 2:blockIdx_y // 3 * 147456 + blockIdx_x // 2 * 73728 + ax2 * 18432 + threadIdx_y * 4608 + threadIdx_x // 8 * 1152 + blockIdx_y % 3 * 384 + blockIdx_x % 2 * 192 + ax0_ax1_ax3_ax4_ax5_fused_0 * 16 + threadIdx_x % 8 * 2 + 2] = B_reindex_shared_dyn_1[ax0_ax1_ax3_ax4_ax5_fused_0 * 256 + threadIdx_y * 64 + threadIdx_x * 2:ax0_ax1_ax3_ax4_ax5_fused_0 * 256 + threadIdx_y * 64 + threadIdx_x * 2 + 2]
