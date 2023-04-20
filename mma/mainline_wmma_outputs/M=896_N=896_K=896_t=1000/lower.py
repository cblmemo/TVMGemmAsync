# from tvm.script import ir as I
# from tvm.script import tir as T

@I.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer((896, 896), "float16"), B: T.Buffer((896, 896), "float16"), Y: T.Buffer((896, 896), "float16")):
        T.func_attr({"global_symbol": "main", "tir.noalias": T.bool(True)})
        blockIdx_y = T.launch_thread("blockIdx.y", 28)
        Y_reindex_shared_dyn_wmma_accumulator = T.allocate([1024], "float16", "wmma.accumulator")
        A_reindex_shared_dyn = T.allocate([4096], "float16", "shared.dyn")
        B_reindex_shared_dyn = T.allocate([2304], "float16", "shared.dyn")
        A_reindex_shared_dyn_wmma_matrix_a = T.allocate([512], "float16", "wmma.matrix_a")
        B_reindex_shared_dyn_wmma_matrix_b = T.allocate([2048], "float16", "wmma.matrix_b")
        blockIdx_x = T.launch_thread("blockIdx.x", 7)
        threadIdx_y = T.launch_thread("threadIdx.y", 4)
        threadIdx_x = T.launch_thread("threadIdx.x", 32)
        T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 0, T.float32(0))
        T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 1, T.float32(0))
        T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 2, T.float32(0))
        T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 3, T.float32(0))
        for ax2_0_0 in range(28):
            A_reindex_shared_dyn_1 = T.decl_buffer((64, 32), "float16", data=A_reindex_shared_dyn, strides=(40, 1), scope="shared.dyn")
            B_reindex_shared_dyn_1 = T.decl_buffer((32, 64), "float16", data=B_reindex_shared_dyn, strides=(72, 1), scope="shared.dyn")
            A_reindex_shared_dyn_2 = T.Buffer((2560,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
            A_1 = T.Buffer((802816,), "float16", data=A.data)
            A_reindex_shared_dyn_2[threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8:threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8 + 8] = A_1[blockIdx_y // 2 * 57344 + threadIdx_y * 7168 + threadIdx_x // 4 * 896 + ax2_0_0 * 32 + threadIdx_x % 4 * 8:blockIdx_y // 2 * 57344 + threadIdx_y * 7168 + threadIdx_x // 4 * 896 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 8]
            A_reindex_shared_dyn_2[threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8 + 1280:threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8 + 1280 + 8] = A_1[blockIdx_y // 2 * 57344 + threadIdx_y * 7168 + threadIdx_x // 4 * 896 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 28672:blockIdx_y // 2 * 57344 + threadIdx_y * 7168 + threadIdx_x // 4 * 896 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 28672 + 8]
            B_reindex_shared_dyn_2 = T.Buffer((2304,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            B_1 = T.Buffer((802816,), "float16", data=B.data)
            B_reindex_shared_dyn_2[threadIdx_y * 288 + threadIdx_x // 8 * 72 + threadIdx_x % 8 * 8:threadIdx_y * 288 + threadIdx_x // 8 * 72 + threadIdx_x % 8 * 8 + 8] = B_1[ax2_0_0 * 28672 + threadIdx_y * 3584 + threadIdx_x // 8 * 896 + blockIdx_y % 2 * 448 + blockIdx_x * 64 + threadIdx_x % 8 * 8:ax2_0_0 * 28672 + threadIdx_y * 3584 + threadIdx_x // 8 * 896 + blockIdx_y % 2 * 448 + blockIdx_x * 64 + threadIdx_x % 8 * 8 + 8]
            B_reindex_shared_dyn_2[threadIdx_y * 288 + threadIdx_x // 8 * 72 + threadIdx_x % 8 * 8 + 1152:threadIdx_y * 288 + threadIdx_x // 8 * 72 + threadIdx_x % 8 * 8 + 1152 + 8] = B_1[ax2_0_0 * 28672 + threadIdx_y * 3584 + threadIdx_x // 8 * 896 + blockIdx_y % 2 * 448 + blockIdx_x * 64 + threadIdx_x % 8 * 8 + 14336:ax2_0_0 * 28672 + threadIdx_y * 3584 + threadIdx_x // 8 * 896 + blockIdx_y % 2 * 448 + blockIdx_x * 64 + threadIdx_x % 8 * 8 + 14336 + 8]
            T.tvm_load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a, 16, 16, 16, 0, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 640, 640, 1), 40, "row_major")
            T.tvm_load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a, 16, 16, 16, 1, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 640 + 16, 640, 1), 40, "row_major")
            T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 0, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, 0, 1152, 1), 72, "row_major")
            T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 1, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, 16, 1152, 1), 72, "row_major")
            T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 2, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, 32, 1152, 1), 72, "row_major")
            T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 3, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, 48, 1152, 1), 72, "row_major")
            T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 4, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, 1152, 1152, 1), 72, "row_major")
            T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 5, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, 1168, 1152, 1), 72, "row_major")
            T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 6, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, 1184, 1152, 1), 72, "row_major")
            T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 7, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, 1200, 1152, 1), 72, "row_major")
            T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 0, A_reindex_shared_dyn_wmma_matrix_a, 0, B_reindex_shared_dyn_wmma_matrix_b, 0, Y_reindex_shared_dyn_wmma_accumulator, 0)
            T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 0, A_reindex_shared_dyn_wmma_matrix_a, 1, B_reindex_shared_dyn_wmma_matrix_b, 4, Y_reindex_shared_dyn_wmma_accumulator, 0)
            T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 1, A_reindex_shared_dyn_wmma_matrix_a, 0, B_reindex_shared_dyn_wmma_matrix_b, 1, Y_reindex_shared_dyn_wmma_accumulator, 1)
            T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 1, A_reindex_shared_dyn_wmma_matrix_a, 1, B_reindex_shared_dyn_wmma_matrix_b, 5, Y_reindex_shared_dyn_wmma_accumulator, 1)
            T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 2, A_reindex_shared_dyn_wmma_matrix_a, 0, B_reindex_shared_dyn_wmma_matrix_b, 2, Y_reindex_shared_dyn_wmma_accumulator, 2)
            T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 2, A_reindex_shared_dyn_wmma_matrix_a, 1, B_reindex_shared_dyn_wmma_matrix_b, 6, Y_reindex_shared_dyn_wmma_accumulator, 2)
            T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 3, A_reindex_shared_dyn_wmma_matrix_a, 0, B_reindex_shared_dyn_wmma_matrix_b, 3, Y_reindex_shared_dyn_wmma_accumulator, 3)
            T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 3, A_reindex_shared_dyn_wmma_matrix_a, 1, B_reindex_shared_dyn_wmma_matrix_b, 7, Y_reindex_shared_dyn_wmma_accumulator, 3)
        T.tvm_store_matrix_sync(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 0, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 1024, 256, 2), 16, "row_major")
        T.tvm_store_matrix_sync(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 1, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 1024 + 256, 256, 2), 16, "row_major")
        T.tvm_store_matrix_sync(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 2, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 1024 + 512, 256, 2), 16, "row_major")
        T.tvm_store_matrix_sync(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 3, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 1024 + 768, 256, 2), 16, "row_major")
        for ax0_ax1_ax3_ax4_ax5_fused_0 in range(32):
            Y_1 = T.Buffer((802816,), "float16", data=Y.data)
            A_reindex_shared_dyn_1 = T.Buffer((4096,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
            Y_1[blockIdx_y // 2 * 57344 + ax0_ax1_ax3_ax4_ax5_fused_0 // 8 * 14336 + (ax0_ax1_ax3_ax4_ax5_fused_0 * 8 + threadIdx_y * 2 + threadIdx_x // 16) % 16 * 896 + blockIdx_y % 2 * 448 + blockIdx_x * 64 + ax0_ax1_ax3_ax4_ax5_fused_0 % 8 // 2 * 16 + threadIdx_x % 16] = A_reindex_shared_dyn_1[ax0_ax1_ax3_ax4_ax5_fused_0 * 128 + threadIdx_y * 32 + threadIdx_x]
