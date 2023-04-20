# from tvm.script import ir as I
# from tvm.script import tir as T

@I.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer((512, 768), "float16"), B: T.Buffer((768, 3072), "float16"), Y: T.Buffer((512, 3072), "float16")):
        T.func_attr({"global_symbol": "main", "tir.noalias": T.bool(True)})
        blockIdx_y = T.launch_thread("blockIdx.y", 8)
        Y_reindex_shared_dyn_wmma_accumulator = T.allocate([4096], "float16", "wmma.accumulator")
        A_reindex_shared_dyn = T.allocate([5120], "float16", "shared.dyn")
        B_reindex_shared_dyn = T.allocate([4352], "float16", "shared.dyn")
        A_reindex_shared_dyn_wmma_matrix_a = T.allocate([1024], "float16", "wmma.matrix_a")
        B_reindex_shared_dyn_wmma_matrix_b = T.allocate([1024], "float16", "wmma.matrix_b")
        blockIdx_x = T.launch_thread("blockIdx.x", 12)
        threadIdx_y = T.launch_thread("threadIdx.y", 4)
        threadIdx_x = T.launch_thread("threadIdx.x", 32)
        T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 0, T.float32(0))
        T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 1, T.float32(0))
        T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 2, T.float32(0))
        T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 3, T.float32(0))
        T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 4, T.float32(0))
        T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 5, T.float32(0))
        T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 6, T.float32(0))
        T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 7, T.float32(0))
        T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 8, T.float32(0))
        T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 9, T.float32(0))
        T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 10, T.float32(0))
        T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 11, T.float32(0))
        T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 12, T.float32(0))
        T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 13, T.float32(0))
        T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 14, T.float32(0))
        T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, 15, T.float32(0))
        for ax2_0_0 in range(24):
            A_reindex_shared_dyn_1 = T.decl_buffer((128, 32), "float16", data=A_reindex_shared_dyn, strides=(40, 1), scope="shared.dyn")
            B_reindex_shared_dyn_1 = T.decl_buffer((32, 128), "float16", data=B_reindex_shared_dyn, strides=(136, 1), scope="shared.dyn")
            A_reindex_shared_dyn_2 = T.Buffer((5120,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
            A_1 = T.Buffer((393216,), "float16", data=A.data)
            A_reindex_shared_dyn_2[threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8:threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8 + 8] = A_1[blockIdx_y // 2 * 98304 + threadIdx_y * 6144 + threadIdx_x // 4 * 768 + ax2_0_0 * 32 + threadIdx_x % 4 * 8:blockIdx_y // 2 * 98304 + threadIdx_y * 6144 + threadIdx_x // 4 * 768 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 8]
            A_reindex_shared_dyn_2[threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8 + 1280:threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8 + 1280 + 8] = A_1[blockIdx_y // 2 * 98304 + threadIdx_y * 6144 + threadIdx_x // 4 * 768 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 24576:blockIdx_y // 2 * 98304 + threadIdx_y * 6144 + threadIdx_x // 4 * 768 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 24576 + 8]
            A_reindex_shared_dyn_2[threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8 + 2560:threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8 + 2560 + 8] = A_1[blockIdx_y // 2 * 98304 + threadIdx_y * 6144 + threadIdx_x // 4 * 768 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 49152:blockIdx_y // 2 * 98304 + threadIdx_y * 6144 + threadIdx_x // 4 * 768 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 49152 + 8]
            A_reindex_shared_dyn_2[threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8 + 3840:threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8 + 3840 + 8] = A_1[blockIdx_y // 2 * 98304 + threadIdx_y * 6144 + threadIdx_x // 4 * 768 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 73728:blockIdx_y // 2 * 98304 + threadIdx_y * 6144 + threadIdx_x // 4 * 768 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 73728 + 8]
            B_reindex_shared_dyn_2 = T.Buffer((4352,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            B_1 = T.Buffer((2359296,), "float16", data=B.data)
            B_reindex_shared_dyn_2[threadIdx_y * 272 + threadIdx_x // 16 * 136 + threadIdx_x % 16 * 8:threadIdx_y * 272 + threadIdx_x // 16 * 136 + threadIdx_x % 16 * 8 + 8] = B_1[ax2_0_0 * 98304 + threadIdx_y * 6144 + threadIdx_x // 16 * 3072 + blockIdx_y % 2 * 1536 + blockIdx_x * 128 + threadIdx_x % 16 * 8:ax2_0_0 * 98304 + threadIdx_y * 6144 + threadIdx_x // 16 * 3072 + blockIdx_y % 2 * 1536 + blockIdx_x * 128 + threadIdx_x % 16 * 8 + 8]
            B_reindex_shared_dyn_2[threadIdx_y * 272 + threadIdx_x // 16 * 136 + threadIdx_x % 16 * 8 + 1088:threadIdx_y * 272 + threadIdx_x // 16 * 136 + threadIdx_x % 16 * 8 + 1088 + 8] = B_1[ax2_0_0 * 98304 + threadIdx_y * 6144 + threadIdx_x // 16 * 3072 + blockIdx_y % 2 * 1536 + blockIdx_x * 128 + threadIdx_x % 16 * 8 + 24576:ax2_0_0 * 98304 + threadIdx_y * 6144 + threadIdx_x // 16 * 3072 + blockIdx_y % 2 * 1536 + blockIdx_x * 128 + threadIdx_x % 16 * 8 + 24576 + 8]
            B_reindex_shared_dyn_2[threadIdx_y * 272 + threadIdx_x // 16 * 136 + threadIdx_x % 16 * 8 + 2176:threadIdx_y * 272 + threadIdx_x // 16 * 136 + threadIdx_x % 16 * 8 + 2176 + 8] = B_1[ax2_0_0 * 98304 + threadIdx_y * 6144 + threadIdx_x // 16 * 3072 + blockIdx_y % 2 * 1536 + blockIdx_x * 128 + threadIdx_x % 16 * 8 + 49152:ax2_0_0 * 98304 + threadIdx_y * 6144 + threadIdx_x // 16 * 3072 + blockIdx_y % 2 * 1536 + blockIdx_x * 128 + threadIdx_x % 16 * 8 + 49152 + 8]
            B_reindex_shared_dyn_2[threadIdx_y * 272 + threadIdx_x // 16 * 136 + threadIdx_x % 16 * 8 + 3264:threadIdx_y * 272 + threadIdx_x // 16 * 136 + threadIdx_x % 16 * 8 + 3264 + 8] = B_1[ax2_0_0 * 98304 + threadIdx_y * 6144 + threadIdx_x // 16 * 3072 + blockIdx_y % 2 * 1536 + blockIdx_x * 128 + threadIdx_x % 16 * 8 + 73728:ax2_0_0 * 98304 + threadIdx_y * 6144 + threadIdx_x // 16 * 3072 + blockIdx_y % 2 * 1536 + blockIdx_x * 128 + threadIdx_x % 16 * 8 + 73728 + 8]
            for ax2_0_1 in range(2):
                T.tvm_load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a, 16, 16, 16, 0, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y // 2 * 2560 + ax2_0_1 * 16, 640, 1), 40, "row_major")
                T.tvm_load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a, 16, 16, 16, 1, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y // 2 * 2560 + ax2_0_1 * 16 + 640, 640, 1), 40, "row_major")
                T.tvm_load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a, 16, 16, 16, 2, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y // 2 * 2560 + ax2_0_1 * 16 + 1280, 640, 1), 40, "row_major")
                T.tvm_load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a, 16, 16, 16, 3, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y // 2 * 2560 + ax2_0_1 * 16 + 1920, 640, 1), 40, "row_major")
                T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 0, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax2_0_1 * 2176 + threadIdx_y % 2 * 64, 2176, 1), 136, "row_major")
                T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 1, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax2_0_1 * 2176 + threadIdx_y % 2 * 64 + 16, 2176, 1), 136, "row_major")
                T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 2, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax2_0_1 * 2176 + threadIdx_y % 2 * 64 + 32, 2176, 1), 136, "row_major")
                T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 3, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax2_0_1 * 2176 + threadIdx_y % 2 * 64 + 48, 2176, 1), 136, "row_major")
                T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 0, A_reindex_shared_dyn_wmma_matrix_a, 0, B_reindex_shared_dyn_wmma_matrix_b, 0, Y_reindex_shared_dyn_wmma_accumulator, 0)
                T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 1, A_reindex_shared_dyn_wmma_matrix_a, 0, B_reindex_shared_dyn_wmma_matrix_b, 1, Y_reindex_shared_dyn_wmma_accumulator, 1)
                T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 2, A_reindex_shared_dyn_wmma_matrix_a, 0, B_reindex_shared_dyn_wmma_matrix_b, 2, Y_reindex_shared_dyn_wmma_accumulator, 2)
                T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 3, A_reindex_shared_dyn_wmma_matrix_a, 0, B_reindex_shared_dyn_wmma_matrix_b, 3, Y_reindex_shared_dyn_wmma_accumulator, 3)
                T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 4, A_reindex_shared_dyn_wmma_matrix_a, 1, B_reindex_shared_dyn_wmma_matrix_b, 0, Y_reindex_shared_dyn_wmma_accumulator, 4)
                T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 5, A_reindex_shared_dyn_wmma_matrix_a, 1, B_reindex_shared_dyn_wmma_matrix_b, 1, Y_reindex_shared_dyn_wmma_accumulator, 5)
                T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 6, A_reindex_shared_dyn_wmma_matrix_a, 1, B_reindex_shared_dyn_wmma_matrix_b, 2, Y_reindex_shared_dyn_wmma_accumulator, 6)
                T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 7, A_reindex_shared_dyn_wmma_matrix_a, 1, B_reindex_shared_dyn_wmma_matrix_b, 3, Y_reindex_shared_dyn_wmma_accumulator, 7)
                T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 8, A_reindex_shared_dyn_wmma_matrix_a, 2, B_reindex_shared_dyn_wmma_matrix_b, 0, Y_reindex_shared_dyn_wmma_accumulator, 8)
                T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 9, A_reindex_shared_dyn_wmma_matrix_a, 2, B_reindex_shared_dyn_wmma_matrix_b, 1, Y_reindex_shared_dyn_wmma_accumulator, 9)
                T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 10, A_reindex_shared_dyn_wmma_matrix_a, 2, B_reindex_shared_dyn_wmma_matrix_b, 2, Y_reindex_shared_dyn_wmma_accumulator, 10)
                T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 11, A_reindex_shared_dyn_wmma_matrix_a, 2, B_reindex_shared_dyn_wmma_matrix_b, 3, Y_reindex_shared_dyn_wmma_accumulator, 11)
                T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 12, A_reindex_shared_dyn_wmma_matrix_a, 3, B_reindex_shared_dyn_wmma_matrix_b, 0, Y_reindex_shared_dyn_wmma_accumulator, 12)
                T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 13, A_reindex_shared_dyn_wmma_matrix_a, 3, B_reindex_shared_dyn_wmma_matrix_b, 1, Y_reindex_shared_dyn_wmma_accumulator, 13)
                T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 14, A_reindex_shared_dyn_wmma_matrix_a, 3, B_reindex_shared_dyn_wmma_matrix_b, 2, Y_reindex_shared_dyn_wmma_accumulator, 14)
                T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, 15, A_reindex_shared_dyn_wmma_matrix_a, 3, B_reindex_shared_dyn_wmma_matrix_b, 3, Y_reindex_shared_dyn_wmma_accumulator, 15)
        for ax2 in range(4):
            cse_var_2: T.int32 = ax2 * 49152
            cse_var_1: T.int32 = ax2 * 4
            T.tvm_store_matrix_sync(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, cse_var_1, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, threadIdx_y * 1024, 256, 2), 16, "row_major")
            T.tvm_store_matrix_sync(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, cse_var_1 + 1, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, threadIdx_y * 1024 + 256, 256, 2), 16, "row_major")
            T.tvm_store_matrix_sync(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, cse_var_1 + 2, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, threadIdx_y * 1024 + 512, 256, 2), 16, "row_major")
            T.tvm_store_matrix_sync(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, cse_var_1 + 3, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, threadIdx_y * 1024 + 768, 256, 2), 16, "row_major")
            Y_1 = T.Buffer((1572864,), "float16", data=Y.data)
            B_reindex_shared_dyn_1 = T.Buffer((4096,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            Y_1[blockIdx_y // 2 * 393216 + cse_var_2 + threadIdx_y % 2 * 24576 + threadIdx_x // 4 * 3072 + blockIdx_y % 2 * 1536 + blockIdx_x * 128 + threadIdx_y // 2 * 16 + threadIdx_x % 4 * 4:blockIdx_y // 2 * 393216 + cse_var_2 + threadIdx_y % 2 * 24576 + threadIdx_x // 4 * 3072 + blockIdx_y % 2 * 1536 + blockIdx_x * 128 + threadIdx_y // 2 * 16 + threadIdx_x % 4 * 4 + 4] = B_reindex_shared_dyn_1[threadIdx_y * 128 + threadIdx_x * 4:threadIdx_y * 128 + threadIdx_x * 4 + 4]
            Y_1[blockIdx_y // 2 * 393216 + cse_var_2 + threadIdx_y % 2 * 24576 + threadIdx_x // 4 * 3072 + blockIdx_y % 2 * 1536 + blockIdx_x * 128 + threadIdx_y // 2 * 16 + threadIdx_x % 4 * 4 + 32:blockIdx_y // 2 * 393216 + cse_var_2 + threadIdx_y % 2 * 24576 + threadIdx_x // 4 * 3072 + blockIdx_y % 2 * 1536 + blockIdx_x * 128 + threadIdx_y // 2 * 16 + threadIdx_x % 4 * 4 + 32 + 4] = B_reindex_shared_dyn_1[threadIdx_y * 128 + threadIdx_x * 4 + 512:threadIdx_y * 128 + threadIdx_x * 4 + 512 + 4]
            Y_1[blockIdx_y // 2 * 393216 + cse_var_2 + threadIdx_y % 2 * 24576 + threadIdx_x // 4 * 3072 + blockIdx_y % 2 * 1536 + blockIdx_x * 128 + threadIdx_y // 2 * 16 + threadIdx_x % 4 * 4 + 64:blockIdx_y // 2 * 393216 + cse_var_2 + threadIdx_y % 2 * 24576 + threadIdx_x // 4 * 3072 + blockIdx_y % 2 * 1536 + blockIdx_x * 128 + threadIdx_y // 2 * 16 + threadIdx_x % 4 * 4 + 64 + 4] = B_reindex_shared_dyn_1[threadIdx_y * 128 + threadIdx_x * 4 + 1024:threadIdx_y * 128 + threadIdx_x * 4 + 1024 + 4]
            Y_1[blockIdx_y // 2 * 393216 + cse_var_2 + threadIdx_y % 2 * 24576 + threadIdx_x // 4 * 3072 + blockIdx_y % 2 * 1536 + blockIdx_x * 128 + threadIdx_y // 2 * 16 + threadIdx_x % 4 * 4 + 96:blockIdx_y // 2 * 393216 + cse_var_2 + threadIdx_y % 2 * 24576 + threadIdx_x // 4 * 3072 + blockIdx_y % 2 * 1536 + blockIdx_x * 128 + threadIdx_y // 2 * 16 + threadIdx_x % 4 * 4 + 96 + 4] = B_reindex_shared_dyn_1[threadIdx_y * 128 + threadIdx_x * 4 + 1536:threadIdx_y * 128 + threadIdx_x * 4 + 1536 + 4]
            Y_1[blockIdx_y // 2 * 393216 + cse_var_2 + threadIdx_y % 2 * 24576 + threadIdx_x // 4 * 3072 + blockIdx_y % 2 * 1536 + blockIdx_x * 128 + threadIdx_y // 2 * 16 + threadIdx_x % 4 * 4 + 196608:blockIdx_y // 2 * 393216 + cse_var_2 + threadIdx_y % 2 * 24576 + threadIdx_x // 4 * 3072 + blockIdx_y % 2 * 1536 + blockIdx_x * 128 + threadIdx_y // 2 * 16 + threadIdx_x % 4 * 4 + 196608 + 4] = B_reindex_shared_dyn_1[threadIdx_y * 128 + threadIdx_x * 4 + 2048:threadIdx_y * 128 + threadIdx_x * 4 + 2048 + 4]
            Y_1[blockIdx_y // 2 * 393216 + (threadIdx_y * 128 + threadIdx_x * 4 + 2560) // 2048 * 196608 + cse_var_2 + threadIdx_y % 2 * 24576 + threadIdx_x // 4 * 3072 + blockIdx_y % 2 * 1536 + blockIdx_x * 128 + threadIdx_y // 2 * 16 + threadIdx_x % 4 * 4 + 32:blockIdx_y // 2 * 393216 + (threadIdx_y * 128 + threadIdx_x * 4 + 2560) // 2048 * 196608 + cse_var_2 + threadIdx_y % 2 * 24576 + threadIdx_x // 4 * 3072 + blockIdx_y % 2 * 1536 + blockIdx_x * 128 + threadIdx_y // 2 * 16 + threadIdx_x % 4 * 4 + 32 + 4] = B_reindex_shared_dyn_1[threadIdx_y * 128 + threadIdx_x * 4 + 2560:threadIdx_y * 128 + threadIdx_x * 4 + 2560 + 4]
            Y_1[blockIdx_y // 2 * 393216 + (threadIdx_y * 128 + threadIdx_x * 4 + 3072) // 2048 * 196608 + cse_var_2 + threadIdx_y % 2 * 24576 + threadIdx_x // 4 * 3072 + blockIdx_y % 2 * 1536 + blockIdx_x * 128 + threadIdx_y // 2 * 16 + threadIdx_x % 4 * 4 + 64:blockIdx_y // 2 * 393216 + (threadIdx_y * 128 + threadIdx_x * 4 + 3072) // 2048 * 196608 + cse_var_2 + threadIdx_y % 2 * 24576 + threadIdx_x // 4 * 3072 + blockIdx_y % 2 * 1536 + blockIdx_x * 128 + threadIdx_y // 2 * 16 + threadIdx_x % 4 * 4 + 64 + 4] = B_reindex_shared_dyn_1[threadIdx_y * 128 + threadIdx_x * 4 + 3072:threadIdx_y * 128 + threadIdx_x * 4 + 3072 + 4]
            Y_1[blockIdx_y // 2 * 393216 + (threadIdx_y * 128 + threadIdx_x * 4 + 3584) // 2048 * 196608 + cse_var_2 + threadIdx_y % 2 * 24576 + threadIdx_x // 4 * 3072 + blockIdx_y % 2 * 1536 + blockIdx_x * 128 + threadIdx_y // 2 * 16 + threadIdx_x % 4 * 4 + 96:blockIdx_y // 2 * 393216 + (threadIdx_y * 128 + threadIdx_x * 4 + 3584) // 2048 * 196608 + cse_var_2 + threadIdx_y % 2 * 24576 + threadIdx_x // 4 * 3072 + blockIdx_y % 2 * 1536 + blockIdx_x * 128 + threadIdx_y // 2 * 16 + threadIdx_x % 4 * 4 + 96 + 4] = B_reindex_shared_dyn_1[threadIdx_y * 128 + threadIdx_x * 4 + 3584:threadIdx_y * 128 + threadIdx_x * 4 + 3584 + 4]
