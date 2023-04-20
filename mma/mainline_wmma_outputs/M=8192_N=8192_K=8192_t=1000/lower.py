# from tvm.script import ir as I
# from tvm.script import tir as T

@I.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer((8192, 8192), "float16"), B: T.Buffer((8192, 8192), "float16"), Y: T.Buffer((8192, 8192), "float16")):
        T.func_attr({"global_symbol": "main", "tir.noalias": T.bool(True)})
        blockIdx_y = T.launch_thread("blockIdx.y", 512)
        Y_reindex_shared_dyn_wmma_accumulator = T.allocate([8192], "float16", "wmma.accumulator")
        A_reindex_shared_dyn = T.allocate([10240], "float16", "shared.dyn")
        B_reindex_shared_dyn = T.allocate([4352], "float16", "shared.dyn")
        A_reindex_shared_dyn_wmma_matrix_a = T.allocate([1024], "float16", "wmma.matrix_a")
        B_reindex_shared_dyn_wmma_matrix_b = T.allocate([2048], "float16", "wmma.matrix_b")
        blockIdx_x = T.launch_thread("blockIdx.x", 4)
        threadIdx_y = T.launch_thread("threadIdx.y", 4)
        threadIdx_x = T.launch_thread("threadIdx.x", 32)
        for ax0_0_3_init in range(4):
            cse_var_1: T.int32 = ax0_0_3_init * 8
            T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, cse_var_1, T.float32(0))
            T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, cse_var_1 + 1, T.float32(0))
            T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, cse_var_1 + 2, T.float32(0))
            T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, cse_var_1 + 3, T.float32(0))
            T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, cse_var_1 + 4, T.float32(0))
            T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, cse_var_1 + 5, T.float32(0))
            T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, cse_var_1 + 6, T.float32(0))
            T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, cse_var_1 + 7, T.float32(0))
        for ax2_0_0 in range(256):
            A_reindex_shared_dyn_1 = T.decl_buffer((256, 32), "float16", data=A_reindex_shared_dyn, strides=(40, 1), scope="shared.dyn")
            B_reindex_shared_dyn_1 = T.decl_buffer((32, 128), "float16", data=B_reindex_shared_dyn, strides=(136, 1), scope="shared.dyn")
            A_reindex_shared_dyn_2 = T.Buffer((10240,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
            A_1 = T.Buffer((67108864,), "float16", data=A.data)
            A_reindex_shared_dyn_2[threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8:threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8 + 8] = A_1[blockIdx_y // 64 * 8388608 + blockIdx_x * 2097152 + threadIdx_y * 65536 + threadIdx_x // 4 * 8192 + ax2_0_0 * 32 + threadIdx_x % 4 * 8:blockIdx_y // 64 * 8388608 + blockIdx_x * 2097152 + threadIdx_y * 65536 + threadIdx_x // 4 * 8192 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 8]
            A_reindex_shared_dyn_2[threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8 + 1280:threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8 + 1280 + 8] = A_1[blockIdx_y // 64 * 8388608 + blockIdx_x * 2097152 + threadIdx_y * 65536 + threadIdx_x // 4 * 8192 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 262144:blockIdx_y // 64 * 8388608 + blockIdx_x * 2097152 + threadIdx_y * 65536 + threadIdx_x // 4 * 8192 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 262144 + 8]
            A_reindex_shared_dyn_2[threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8 + 2560:threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8 + 2560 + 8] = A_1[blockIdx_y // 64 * 8388608 + blockIdx_x * 2097152 + threadIdx_y * 65536 + threadIdx_x // 4 * 8192 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 524288:blockIdx_y // 64 * 8388608 + blockIdx_x * 2097152 + threadIdx_y * 65536 + threadIdx_x // 4 * 8192 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 524288 + 8]
            A_reindex_shared_dyn_2[threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8 + 3840:threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8 + 3840 + 8] = A_1[blockIdx_y // 64 * 8388608 + blockIdx_x * 2097152 + threadIdx_y * 65536 + threadIdx_x // 4 * 8192 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 786432:blockIdx_y // 64 * 8388608 + blockIdx_x * 2097152 + threadIdx_y * 65536 + threadIdx_x // 4 * 8192 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 786432 + 8]
            A_reindex_shared_dyn_2[threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8 + 5120:threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8 + 5120 + 8] = A_1[blockIdx_y // 64 * 8388608 + blockIdx_x * 2097152 + threadIdx_y * 65536 + threadIdx_x // 4 * 8192 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 1048576:blockIdx_y // 64 * 8388608 + blockIdx_x * 2097152 + threadIdx_y * 65536 + threadIdx_x // 4 * 8192 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 1048576 + 8]
            A_reindex_shared_dyn_2[threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8 + 6400:threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8 + 6400 + 8] = A_1[blockIdx_y // 64 * 8388608 + blockIdx_x * 2097152 + threadIdx_y * 65536 + threadIdx_x // 4 * 8192 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 1310720:blockIdx_y // 64 * 8388608 + blockIdx_x * 2097152 + threadIdx_y * 65536 + threadIdx_x // 4 * 8192 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 1310720 + 8]
            A_reindex_shared_dyn_2[threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8 + 7680:threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8 + 7680 + 8] = A_1[blockIdx_y // 64 * 8388608 + blockIdx_x * 2097152 + threadIdx_y * 65536 + threadIdx_x // 4 * 8192 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 1572864:blockIdx_y // 64 * 8388608 + blockIdx_x * 2097152 + threadIdx_y * 65536 + threadIdx_x // 4 * 8192 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 1572864 + 8]
            A_reindex_shared_dyn_2[threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8 + 8960:threadIdx_y * 320 + threadIdx_x // 4 * 40 + threadIdx_x % 4 * 8 + 8960 + 8] = A_1[blockIdx_y // 64 * 8388608 + blockIdx_x * 2097152 + threadIdx_y * 65536 + threadIdx_x // 4 * 8192 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 1835008:blockIdx_y // 64 * 8388608 + blockIdx_x * 2097152 + threadIdx_y * 65536 + threadIdx_x // 4 * 8192 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 1835008 + 8]
            B_reindex_shared_dyn_2 = T.Buffer((4352,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            B_1 = T.Buffer((67108864,), "float16", data=B.data)
            B_reindex_shared_dyn_2[threadIdx_y * 136 + threadIdx_x * 4:threadIdx_y * 136 + threadIdx_x * 4 + 4] = B_1[ax2_0_0 * 262144 + threadIdx_y * 8192 + blockIdx_y % 64 * 128 + threadIdx_x * 4:ax2_0_0 * 262144 + threadIdx_y * 8192 + blockIdx_y % 64 * 128 + threadIdx_x * 4 + 4]
            B_reindex_shared_dyn_2[threadIdx_y * 136 + threadIdx_x * 4 + 544:threadIdx_y * 136 + threadIdx_x * 4 + 544 + 4] = B_1[ax2_0_0 * 262144 + threadIdx_y * 8192 + blockIdx_y % 64 * 128 + threadIdx_x * 4 + 32768:ax2_0_0 * 262144 + threadIdx_y * 8192 + blockIdx_y % 64 * 128 + threadIdx_x * 4 + 32768 + 4]
            B_reindex_shared_dyn_2[threadIdx_y * 136 + threadIdx_x * 4 + 1088:threadIdx_y * 136 + threadIdx_x * 4 + 1088 + 4] = B_1[ax2_0_0 * 262144 + threadIdx_y * 8192 + blockIdx_y % 64 * 128 + threadIdx_x * 4 + 65536:ax2_0_0 * 262144 + threadIdx_y * 8192 + blockIdx_y % 64 * 128 + threadIdx_x * 4 + 65536 + 4]
            B_reindex_shared_dyn_2[threadIdx_y * 136 + threadIdx_x * 4 + 1632:threadIdx_y * 136 + threadIdx_x * 4 + 1632 + 4] = B_1[ax2_0_0 * 262144 + threadIdx_y * 8192 + blockIdx_y % 64 * 128 + threadIdx_x * 4 + 98304:ax2_0_0 * 262144 + threadIdx_y * 8192 + blockIdx_y % 64 * 128 + threadIdx_x * 4 + 98304 + 4]
            B_reindex_shared_dyn_2[threadIdx_y * 136 + threadIdx_x * 4 + 2176:threadIdx_y * 136 + threadIdx_x * 4 + 2176 + 4] = B_1[ax2_0_0 * 262144 + threadIdx_y * 8192 + blockIdx_y % 64 * 128 + threadIdx_x * 4 + 131072:ax2_0_0 * 262144 + threadIdx_y * 8192 + blockIdx_y % 64 * 128 + threadIdx_x * 4 + 131072 + 4]
            B_reindex_shared_dyn_2[threadIdx_y * 136 + threadIdx_x * 4 + 2720:threadIdx_y * 136 + threadIdx_x * 4 + 2720 + 4] = B_1[ax2_0_0 * 262144 + threadIdx_y * 8192 + blockIdx_y % 64 * 128 + threadIdx_x * 4 + 163840:ax2_0_0 * 262144 + threadIdx_y * 8192 + blockIdx_y % 64 * 128 + threadIdx_x * 4 + 163840 + 4]
            B_reindex_shared_dyn_2[threadIdx_y * 136 + threadIdx_x * 4 + 3264:threadIdx_y * 136 + threadIdx_x * 4 + 3264 + 4] = B_1[ax2_0_0 * 262144 + threadIdx_y * 8192 + blockIdx_y % 64 * 128 + threadIdx_x * 4 + 196608:ax2_0_0 * 262144 + threadIdx_y * 8192 + blockIdx_y % 64 * 128 + threadIdx_x * 4 + 196608 + 4]
            B_reindex_shared_dyn_2[threadIdx_y * 136 + threadIdx_x * 4 + 3808:threadIdx_y * 136 + threadIdx_x * 4 + 3808 + 4] = B_1[ax2_0_0 * 262144 + threadIdx_y * 8192 + blockIdx_y % 64 * 128 + threadIdx_x * 4 + 229376:ax2_0_0 * 262144 + threadIdx_y * 8192 + blockIdx_y % 64 * 128 + threadIdx_x * 4 + 229376 + 4]
            for ax2_0_1 in range(2):
                cse_var_2: T.int32 = ax2_0_1 * 2176
                T.tvm_load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a, 16, 16, 16, 0, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 2560 + ax2_0_1 * 16, 640, 1), 40, "row_major")
                T.tvm_load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a, 16, 16, 16, 1, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 2560 + ax2_0_1 * 16 + 640, 640, 1), 40, "row_major")
                T.tvm_load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a, 16, 16, 16, 2, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 2560 + ax2_0_1 * 16 + 1280, 640, 1), 40, "row_major")
                T.tvm_load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a, 16, 16, 16, 3, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 2560 + ax2_0_1 * 16 + 1920, 640, 1), 40, "row_major")
                T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 0, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, cse_var_2, 2176, 1), 136, "row_major")
                T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 1, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, cse_var_2 + 16, 2176, 1), 136, "row_major")
                T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 2, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, cse_var_2 + 32, 2176, 1), 136, "row_major")
                T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 3, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, cse_var_2 + 48, 2176, 1), 136, "row_major")
                T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 4, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, cse_var_2 + 64, 2176, 1), 136, "row_major")
                T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 5, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, cse_var_2 + 80, 2176, 1), 136, "row_major")
                T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 6, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, cse_var_2 + 96, 2176, 1), 136, "row_major")
                T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, 7, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, cse_var_2 + 112, 2176, 1), 136, "row_major")
                for ax0_0_3 in range(4):
                    cse_var_10: T.int32 = ax0_0_3 * 8
                    cse_var_9: T.int32 = cse_var_10 + 7
                    cse_var_8: T.int32 = cse_var_10 + 6
                    cse_var_7: T.int32 = cse_var_10 + 5
                    cse_var_6: T.int32 = cse_var_10 + 4
                    cse_var_5: T.int32 = cse_var_10 + 3
                    cse_var_4: T.int32 = cse_var_10 + 2
                    cse_var_3: T.int32 = cse_var_10 + 1
                    T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, cse_var_10, A_reindex_shared_dyn_wmma_matrix_a, ax0_0_3, B_reindex_shared_dyn_wmma_matrix_b, 0, Y_reindex_shared_dyn_wmma_accumulator, cse_var_10)
                    T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, cse_var_3, A_reindex_shared_dyn_wmma_matrix_a, ax0_0_3, B_reindex_shared_dyn_wmma_matrix_b, 1, Y_reindex_shared_dyn_wmma_accumulator, cse_var_3)
                    T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, cse_var_4, A_reindex_shared_dyn_wmma_matrix_a, ax0_0_3, B_reindex_shared_dyn_wmma_matrix_b, 2, Y_reindex_shared_dyn_wmma_accumulator, cse_var_4)
                    T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, cse_var_5, A_reindex_shared_dyn_wmma_matrix_a, ax0_0_3, B_reindex_shared_dyn_wmma_matrix_b, 3, Y_reindex_shared_dyn_wmma_accumulator, cse_var_5)
                    T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, cse_var_6, A_reindex_shared_dyn_wmma_matrix_a, ax0_0_3, B_reindex_shared_dyn_wmma_matrix_b, 4, Y_reindex_shared_dyn_wmma_accumulator, cse_var_6)
                    T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, cse_var_7, A_reindex_shared_dyn_wmma_matrix_a, ax0_0_3, B_reindex_shared_dyn_wmma_matrix_b, 5, Y_reindex_shared_dyn_wmma_accumulator, cse_var_7)
                    T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, cse_var_8, A_reindex_shared_dyn_wmma_matrix_a, ax0_0_3, B_reindex_shared_dyn_wmma_matrix_b, 6, Y_reindex_shared_dyn_wmma_accumulator, cse_var_8)
                    T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, cse_var_9, A_reindex_shared_dyn_wmma_matrix_a, ax0_0_3, B_reindex_shared_dyn_wmma_matrix_b, 7, Y_reindex_shared_dyn_wmma_accumulator, cse_var_9)
        for ax2 in range(4):
            cse_var_11: T.int32 = ax2 * 8
            T.tvm_store_matrix_sync(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, cse_var_11, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 2048, 256, 2), 16, "row_major")
            T.tvm_store_matrix_sync(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, cse_var_11 + 1, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 2048 + 256, 256, 2), 16, "row_major")
            T.tvm_store_matrix_sync(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, cse_var_11 + 2, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 2048 + 512, 256, 2), 16, "row_major")
            T.tvm_store_matrix_sync(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, cse_var_11 + 3, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 2048 + 768, 256, 2), 16, "row_major")
            T.tvm_store_matrix_sync(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, cse_var_11 + 4, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 2048 + 1024, 256, 2), 16, "row_major")
            T.tvm_store_matrix_sync(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, cse_var_11 + 5, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 2048 + 1280, 256, 2), 16, "row_major")
            T.tvm_store_matrix_sync(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, cse_var_11 + 6, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 2048 + 1536, 256, 2), 16, "row_major")
            T.tvm_store_matrix_sync(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, cse_var_11 + 7, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 2048 + 1792, 256, 2), 16, "row_major")
            for ax0_ax1_ax3_ax4_ax5_fused_0 in range(32):
                Y_1 = T.Buffer((67108864,), "float16", data=Y.data)
                A_reindex_shared_dyn_1 = T.Buffer((8192,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
                Y_1[blockIdx_y // 64 * 8388608 + blockIdx_x * 2097152 + ax0_ax1_ax3_ax4_ax5_fused_0 // 8 * 524288 + ax2 * 131072 + threadIdx_y * 32768 + threadIdx_x // 8 * 8192 + blockIdx_y % 64 * 128 + ax0_ax1_ax3_ax4_ax5_fused_0 % 8 * 16 + threadIdx_x % 8 * 2:blockIdx_y // 64 * 8388608 + blockIdx_x * 2097152 + ax0_ax1_ax3_ax4_ax5_fused_0 // 8 * 524288 + ax2 * 131072 + threadIdx_y * 32768 + threadIdx_x // 8 * 8192 + blockIdx_y % 64 * 128 + ax0_ax1_ax3_ax4_ax5_fused_0 % 8 * 16 + threadIdx_x % 8 * 2 + 2] = A_reindex_shared_dyn_1[ax0_ax1_ax3_ax4_ax5_fused_0 * 256 + threadIdx_y * 64 + threadIdx_x * 2:ax0_ax1_ax3_ax4_ax5_fused_0 * 256 + threadIdx_y * 64 + threadIdx_x * 2 + 2]
