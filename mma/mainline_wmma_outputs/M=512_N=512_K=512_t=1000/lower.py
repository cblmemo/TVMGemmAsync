# from tvm.script import ir as I
# from tvm.script import tir as T

@I.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer((512, 512), "float16"), B: T.Buffer((512, 512), "float16"), Y: T.Buffer((512, 512), "float16")):
        T.func_attr({"global_symbol": "main", "tir.noalias": T.bool(True)})
        blockIdx_y = T.launch_thread("blockIdx.y", 8)
        Y_reindex_shared_dyn_wmma_accumulator = T.allocate([512], "float16", "wmma.accumulator")
        A_reindex_shared_dyn = T.allocate([4608], "float16", "shared.dyn")
        B_reindex_shared_dyn = T.allocate([4608], "float16", "shared.dyn")
        A_reindex_shared_dyn_wmma_matrix_a = T.allocate([256], "float16", "wmma.matrix_a")
        B_reindex_shared_dyn_wmma_matrix_b = T.allocate([512], "float16", "wmma.matrix_b")
        blockIdx_x = T.launch_thread("blockIdx.x", 8)
        threadIdx_y = T.launch_thread("threadIdx.y", 8)
        threadIdx_x = T.launch_thread("threadIdx.x", 32)
        T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 0, T.float32(0))
        T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 1, T.float32(0))
        for ax2_0_0 in range(8):
            A_reindex_shared_dyn_1 = T.decl_buffer((64, 64), "float16", data=A_reindex_shared_dyn, strides=(72, 1), scope="shared.dyn")
            B_reindex_shared_dyn_1 = T.decl_buffer((64, 64), "float16", data=B_reindex_shared_dyn, strides=(72, 1), scope="shared.dyn")
            A_reindex_shared_dyn_2 = T.Buffer((4608,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
            A_1 = T.Buffer((262144,), "float16", data=A.data)
            A_reindex_shared_dyn_2[threadIdx_y * 288 + threadIdx_x // 8 * 72 + threadIdx_x % 8 * 8:threadIdx_y * 288 + threadIdx_x // 8 * 72 + threadIdx_x % 8 * 8 + 8] = A_1[blockIdx_y * 32768 + threadIdx_y * 2048 + threadIdx_x // 8 * 512 + ax2_0_0 * 64 + threadIdx_x % 8 * 8:blockIdx_y * 32768 + threadIdx_y * 2048 + threadIdx_x // 8 * 512 + ax2_0_0 * 64 + threadIdx_x % 8 * 8 + 8]
            A_reindex_shared_dyn_2[threadIdx_y * 288 + threadIdx_x // 8 * 72 + threadIdx_x % 8 * 8 + 2304:threadIdx_y * 288 + threadIdx_x // 8 * 72 + threadIdx_x % 8 * 8 + 2304 + 8] = A_1[blockIdx_y * 32768 + threadIdx_y * 2048 + threadIdx_x // 8 * 512 + ax2_0_0 * 64 + threadIdx_x % 8 * 8 + 16384:blockIdx_y * 32768 + threadIdx_y * 2048 + threadIdx_x // 8 * 512 + ax2_0_0 * 64 + threadIdx_x % 8 * 8 + 16384 + 8]
            B_reindex_shared_dyn_2 = T.Buffer((4608,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            B_1 = T.Buffer((262144,), "float16", data=B.data)
            B_reindex_shared_dyn_2[threadIdx_y * 288 + threadIdx_x // 8 * 72 + threadIdx_x % 8 * 8:threadIdx_y * 288 + threadIdx_x // 8 * 72 + threadIdx_x % 8 * 8 + 8] = B_1[ax2_0_0 * 32768 + threadIdx_y * 2048 + threadIdx_x // 8 * 512 + blockIdx_x * 64 + threadIdx_x % 8 * 8:ax2_0_0 * 32768 + threadIdx_y * 2048 + threadIdx_x // 8 * 512 + blockIdx_x * 64 + threadIdx_x % 8 * 8 + 8]
            B_reindex_shared_dyn_2[threadIdx_y * 288 + threadIdx_x // 8 * 72 + threadIdx_x % 8 * 8 + 2304:threadIdx_y * 288 + threadIdx_x // 8 * 72 + threadIdx_x % 8 * 8 + 2304 + 8] = B_1[ax2_0_0 * 32768 + threadIdx_y * 2048 + threadIdx_x // 8 * 512 + blockIdx_x * 64 + threadIdx_x % 8 * 8 + 16384:ax2_0_0 * 32768 + threadIdx_y * 2048 + threadIdx_x // 8 * 512 + blockIdx_x * 64 + threadIdx_x % 8 * 8 + 16384 + 8]
            T.tvm_load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a, 16, 16, 16, 0, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y // 2 * 1152, 1152, 1), 72, "row_major")
            T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 0, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, threadIdx_y % 2 * 32, 1152, 1), 72, "row_major")
            T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 1, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, threadIdx_y % 2 * 32 + 16, 1152, 1), 72, "row_major")
            T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 0, A_reindex_shared_dyn_wmma_matrix_a, 0, B_reindex_shared_dyn_wmma_matrix_b, 0, Y_reindex_shared_dyn_wmma_accumulator, 0)
            T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 1, A_reindex_shared_dyn_wmma_matrix_a, 0, B_reindex_shared_dyn_wmma_matrix_b, 1, Y_reindex_shared_dyn_wmma_accumulator, 1)
            T.tvm_load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a, 16, 16, 16, 0, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y // 2 * 1152 + 16, 1152, 1), 72, "row_major")
            T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 0, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, threadIdx_y % 2 * 32 + 1152, 1152, 1), 72, "row_major")
            T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 1, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, threadIdx_y % 2 * 32 + 1168, 1152, 1), 72, "row_major")
            T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 0, A_reindex_shared_dyn_wmma_matrix_a, 0, B_reindex_shared_dyn_wmma_matrix_b, 0, Y_reindex_shared_dyn_wmma_accumulator, 0)
            T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 1, A_reindex_shared_dyn_wmma_matrix_a, 0, B_reindex_shared_dyn_wmma_matrix_b, 1, Y_reindex_shared_dyn_wmma_accumulator, 1)
            T.tvm_load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a, 16, 16, 16, 0, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y // 2 * 1152 + 32, 1152, 1), 72, "row_major")
            T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 0, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, threadIdx_y % 2 * 32 + 2304, 1152, 1), 72, "row_major")
            T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 1, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, threadIdx_y % 2 * 32 + 2320, 1152, 1), 72, "row_major")
            T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 0, A_reindex_shared_dyn_wmma_matrix_a, 0, B_reindex_shared_dyn_wmma_matrix_b, 0, Y_reindex_shared_dyn_wmma_accumulator, 0)
            T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 1, A_reindex_shared_dyn_wmma_matrix_a, 0, B_reindex_shared_dyn_wmma_matrix_b, 1, Y_reindex_shared_dyn_wmma_accumulator, 1)
            T.tvm_load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a, 16, 16, 16, 0, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y // 2 * 1152 + 48, 1152, 1), 72, "row_major")
            T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 0, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, threadIdx_y % 2 * 32 + 3456, 1152, 1), 72, "row_major")
            T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 1, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, threadIdx_y % 2 * 32 + 3472, 1152, 1), 72, "row_major")
            T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 0, A_reindex_shared_dyn_wmma_matrix_a, 0, B_reindex_shared_dyn_wmma_matrix_b, 0, Y_reindex_shared_dyn_wmma_accumulator, 0)
            T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 1, A_reindex_shared_dyn_wmma_matrix_a, 0, B_reindex_shared_dyn_wmma_matrix_b, 1, Y_reindex_shared_dyn_wmma_accumulator, 1)
        T.tvm_store_matrix_sync(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 0, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 512, 256, 2), 16, "row_major")
        T.tvm_store_matrix_sync(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 1, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 512 + 256, 256, 2), 16, "row_major")
        Y_1 = T.Buffer((262144,), "float16", data=Y.data)
        A_reindex_shared_dyn_1 = T.Buffer((4096,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
        Y_1[blockIdx_y * 32768 + threadIdx_y // 4 * 8192 + threadIdx_x // 2 * 512 + blockIdx_x * 64 + threadIdx_y % 4 * 16 + threadIdx_x % 2 * 8:blockIdx_y * 32768 + threadIdx_y // 4 * 8192 + threadIdx_x // 2 * 512 + blockIdx_x * 64 + threadIdx_y % 4 * 16 + threadIdx_x % 2 * 8 + 8] = A_reindex_shared_dyn_1[threadIdx_y * 256 + threadIdx_x * 8:threadIdx_y * 256 + threadIdx_x * 8 + 8]
        Y_1[blockIdx_y * 32768 + threadIdx_y // 4 * 8192 + threadIdx_x // 2 * 512 + blockIdx_x * 64 + threadIdx_y % 4 * 16 + threadIdx_x % 2 * 8 + 16384:blockIdx_y * 32768 + threadIdx_y // 4 * 8192 + threadIdx_x // 2 * 512 + blockIdx_x * 64 + threadIdx_y % 4 * 16 + threadIdx_x % 2 * 8 + 16384 + 8] = A_reindex_shared_dyn_1[threadIdx_y * 256 + threadIdx_x * 8 + 2048:threadIdx_y * 256 + threadIdx_x * 8 + 2048 + 8]
