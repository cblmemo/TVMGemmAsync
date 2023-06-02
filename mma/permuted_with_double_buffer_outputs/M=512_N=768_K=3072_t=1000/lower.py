# from tvm.script import ir as I
# from tvm.script import tir as T

@I.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer((512, 3072), "float16"), B: T.Buffer((3072, 768), "float16"), Y: T.Buffer((512, 768), "float16")):
        T.func_attr({"global_symbol": "main", "tir.noalias": T.bool(True)})
        blockIdx_x = T.launch_thread("blockIdx.x", 24)
        Y_reindex_m16n8k8_matrixC = T.allocate([16], "float16x2", "local")
        A_reindex_shared_dyn_local = T.allocate([18], "float16x8", "local")
        B_reindex_shared_dyn_local = T.allocate([68], "float16x8", "local")
        A_reindex_shared_dyn = T.allocate([8192], "float16", "shared.dyn")
        B_reindex_shared_dyn = T.allocate([16384], "float16", "shared.dyn")
        A_reindex_shared_dyn_m16n8k8_matrixA = T.allocate([16], "float16", "local")
        B_reindex_shared_dyn_m16n8k8_matrixB = T.allocate([16], "float16", "local")
        blockIdx_y = T.launch_thread("blockIdx.y", 2)
        threadIdx_y = T.launch_thread("threadIdx.y", 8)
        threadIdx_x = T.launch_thread("threadIdx.x", 32)
        Y_reindex_m16n8k8_matrixC_1 = T.decl_buffer((32,), "float16", scope="local")
        Y_reindex_m16n8k8_matrixC_2 = T.Buffer((16,), "float16x2", data=Y_reindex_m16n8k8_matrixC, scope="local")
        for ax0_0_3_init, ax1_0_3_init, ax1_0_4_init, b in T.grid(2, 2, 2, 2):
            Y_reindex_m16n8k8_matrixC_2[ax0_0_3_init * 8 + ax1_0_3_init * 4 + ax1_0_4_init * 2 + b] = T.Broadcast(T.float16(0), 2)
        with T.decl_buffer((8192,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn") as A_reindex_shared_dyn_1:
            B_reindex_shared_dyn_1 = T.decl_buffer((16384,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            A_reindex_shared_dyn_local_1 = T.decl_buffer((144,), "float16", scope="local")
            B_reindex_shared_dyn_local_1 = T.decl_buffer((544,), "float16", scope="local")
            A_reindex_shared_dyn_m16n8k8_matrixA_1 = T.decl_buffer((16,), "float16", data=A_reindex_shared_dyn_m16n8k8_matrixA, scope="local")
            B_reindex_shared_dyn_m16n8k8_matrixB_1 = T.decl_buffer((16,), "float16", data=B_reindex_shared_dyn_m16n8k8_matrixB, scope="local")
            A_reindex_shared_dyn_local_2 = T.Buffer((18,), "float16x8", data=A_reindex_shared_dyn_local, scope="local")
            A_1 = T.Buffer((1572864,), "float16", data=A.data)
            for ax0_ax1_fused_0_cache in range(2):
                A_reindex_shared_dyn_local_2[ax0_ax1_fused_0_cache * 9] = A_1[blockIdx_x // 6 * 393216 + blockIdx_y * 196608 + ax0_ax1_fused_0_cache * 98304 + threadIdx_y * 12288 + threadIdx_x // 8 * 3072 + threadIdx_x % 8 * 8:blockIdx_x // 6 * 393216 + blockIdx_y * 196608 + ax0_ax1_fused_0_cache * 98304 + threadIdx_y * 12288 + threadIdx_x // 8 * 3072 + threadIdx_x % 8 * 8 + 8]
            B_reindex_shared_dyn_local_2 = T.Buffer((68,), "float16x8", data=B_reindex_shared_dyn_local, scope="local")
            B_1 = T.Buffer((2359296,), "float16", data=B.data)
            for ax0_ax1_fused_0_cache in range(4):
                B_reindex_shared_dyn_local_2[ax0_ax1_fused_0_cache * 17] = B_1[ax0_ax1_fused_0_cache * 12288 + threadIdx_y * 1536 + threadIdx_x // 16 * 768 + blockIdx_x % 6 * 128 + threadIdx_x % 16 * 8:ax0_ax1_fused_0_cache * 12288 + threadIdx_y * 1536 + threadIdx_x // 16 * 768 + blockIdx_x % 6 * 128 + threadIdx_x % 16 * 8 + 8]
            A_reindex_shared_dyn_2 = T.Buffer((8192,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
            for ax0_ax1_fused_0 in range(2):
                A_reindex_shared_dyn_2[ax0_ax1_fused_0 * 2048 + threadIdx_y * 256 + threadIdx_x // 8 * 64 + T.bitwise_xor(threadIdx_x % 8, threadIdx_y % 2 * 4 + threadIdx_x // 8) * 8:ax0_ax1_fused_0 * 2048 + threadIdx_y * 256 + threadIdx_x // 8 * 64 + T.bitwise_xor(threadIdx_x % 8, threadIdx_y % 2 * 4 + threadIdx_x // 8) * 8 + 8] = A_reindex_shared_dyn_local_2[ax0_ax1_fused_0 * 9]
            B_reindex_shared_dyn_2 = T.Buffer((16384,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            for ax0_ax1_fused_0 in range(4):
                B_reindex_shared_dyn_2[ax0_ax1_fused_0 * 2048 + threadIdx_y * 256 + threadIdx_x // 8 * 64 + T.bitwise_xor(threadIdx_x % 8, threadIdx_y % 4 * 2 + threadIdx_x // 16) * 8:ax0_ax1_fused_0 * 2048 + threadIdx_y * 256 + threadIdx_x // 8 * 64 + T.bitwise_xor(threadIdx_x % 8, threadIdx_y % 4 * 2 + threadIdx_x // 16) * 8 + 8] = B_reindex_shared_dyn_local_2[ax0_ax1_fused_0 * 17]
            T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, 0, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, 0, 2048, 1), threadIdx_y // 4 * 2048 + threadIdx_x * 64 + T.bitwise_xor(0, threadIdx_x % 8) * 8)
            T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, 0, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, 0, 1024, 1), threadIdx_x % 8 * 128 + threadIdx_y % 4 // 2 * 64 + T.bitwise_xor(threadIdx_y % 2 * 4 + threadIdx_x // 8, threadIdx_x % 8) * 8)
            for ax2_0_0 in range(47):
                cse_var_1: T.int32 = (ax2_0_0 + 1) % 2
                for ax0_ax1_fused_0_cache in range(2):
                    A_reindex_shared_dyn_local_2[ax0_ax1_fused_0_cache * 9] = A_1[blockIdx_x // 6 * 393216 + blockIdx_y * 196608 + ax0_ax1_fused_0_cache * 98304 + threadIdx_y * 12288 + threadIdx_x // 8 * 3072 + ax2_0_0 * 64 + threadIdx_x % 8 * 8 + 64:blockIdx_x // 6 * 393216 + blockIdx_y * 196608 + ax0_ax1_fused_0_cache * 98304 + threadIdx_y * 12288 + threadIdx_x // 8 * 3072 + ax2_0_0 * 64 + threadIdx_x % 8 * 8 + 64 + 8]
                for ax0_ax1_fused_0_cache in range(4):
                    B_reindex_shared_dyn_local_2[ax0_ax1_fused_0_cache * 17] = B_1[ax2_0_0 * 49152 + ax0_ax1_fused_0_cache * 12288 + threadIdx_y * 1536 + threadIdx_x // 16 * 768 + blockIdx_x % 6 * 128 + threadIdx_x % 16 * 8 + 49152:ax2_0_0 * 49152 + ax0_ax1_fused_0_cache * 12288 + threadIdx_y * 1536 + threadIdx_x // 16 * 768 + blockIdx_x % 6 * 128 + threadIdx_x % 16 * 8 + 49152 + 8]
                for ax2_0_1 in range(7):
                    cse_var_4: T.int32 = ax2_0_1 + 1
                    cse_var_3: T.int32 = ax2_0_0 % 2
                    cse_var_2: T.int32 = cse_var_4 % 2 * 8
                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, cse_var_2, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, cse_var_3 * 4096, 2048, 1), threadIdx_y // 4 * 2048 + threadIdx_x * 64 + T.bitwise_xor(cse_var_4, threadIdx_x % 8) * 8)
                    T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_2, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, cse_var_3 * 8192, 1024, 1), ax2_0_1 * 1024 + threadIdx_x % 8 * 128 + threadIdx_y % 4 // 2 * 64 + T.bitwise_xor(threadIdx_y % 2 * 4 + threadIdx_x // 8, threadIdx_x % 8) * 8 + 1024)
                    for ax0_0_3, ax1_0_3, ax1_0_4 in T.grid(2, 2, 2):
                        cse_var_7: T.int32 = ax1_0_3 * 4
                        cse_var_6: T.int32 = ax1_0_4 * 2
                        cse_var_5: T.int32 = ax2_0_1 % 2 * 8
                        T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, cse_var_5 + ax0_0_3 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_5 + cse_var_7 + cse_var_6, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 8 + cse_var_7 + cse_var_6, T.bool(False))
                for ax0_ax1_fused_0 in range(2):
                    A_reindex_shared_dyn_2[cse_var_1 * 4096 + ax0_ax1_fused_0 * 2048 + threadIdx_y * 256 + threadIdx_x // 8 * 64 + T.bitwise_xor(threadIdx_x % 8, threadIdx_y % 2 * 4 + threadIdx_x // 8) * 8:cse_var_1 * 4096 + ax0_ax1_fused_0 * 2048 + threadIdx_y * 256 + threadIdx_x // 8 * 64 + T.bitwise_xor(threadIdx_x % 8, threadIdx_y % 2 * 4 + threadIdx_x // 8) * 8 + 8] = A_reindex_shared_dyn_local_2[ax0_ax1_fused_0 * 9]
                for ax0_ax1_fused_0 in range(4):
                    B_reindex_shared_dyn_2[cse_var_1 * 8192 + ax0_ax1_fused_0 * 2048 + threadIdx_y * 256 + threadIdx_x // 8 * 64 + T.bitwise_xor(threadIdx_x % 8, threadIdx_y % 4 * 2 + threadIdx_x // 16) * 8:cse_var_1 * 8192 + ax0_ax1_fused_0 * 2048 + threadIdx_y * 256 + threadIdx_x // 8 * 64 + T.bitwise_xor(threadIdx_x % 8, threadIdx_y % 4 * 2 + threadIdx_x // 16) * 8 + 8] = B_reindex_shared_dyn_local_2[ax0_ax1_fused_0 * 17]
                T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, 0, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, cse_var_1 * 4096, 2048, 1), threadIdx_y // 4 * 2048 + threadIdx_x * 64 + T.bitwise_xor(0, threadIdx_x % 8) * 8)
                T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, 0, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, cse_var_1 * 8192, 1024, 1), threadIdx_x % 8 * 128 + threadIdx_y % 4 // 2 * 64 + T.bitwise_xor(threadIdx_y % 2 * 4 + threadIdx_x // 8, threadIdx_x % 8) * 8)
                for ax0_0_3, ax1_0_3, ax1_0_4 in T.grid(2, 2, 2):
                    cse_var_9: T.int32 = ax1_0_3 * 4
                    cse_var_8: T.int32 = ax1_0_4 * 2
                    T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 * 4 + 8, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_9 + cse_var_8 + 8, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 8 + cse_var_9 + cse_var_8, T.bool(False))
            for ax2_0_1 in range(7):
                cse_var_11: T.int32 = ax2_0_1 + 1
                cse_var_10: T.int32 = cse_var_11 % 2 * 8
                T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, cse_var_10, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, 4096, 2048, 1), threadIdx_y // 4 * 2048 + threadIdx_x * 64 + T.bitwise_xor(cse_var_11, threadIdx_x % 8) * 8)
                T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_10, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, 8192, 1024, 1), ax2_0_1 * 1024 + threadIdx_x % 8 * 128 + threadIdx_y % 4 // 2 * 64 + T.bitwise_xor(threadIdx_y % 2 * 4 + threadIdx_x // 8, threadIdx_x % 8) * 8 + 1024)
                for ax0_0_3, ax1_0_3, ax1_0_4 in T.grid(2, 2, 2):
                    cse_var_14: T.int32 = ax1_0_3 * 4
                    cse_var_13: T.int32 = ax1_0_4 * 2
                    cse_var_12: T.int32 = ax2_0_1 % 2 * 8
                    T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, cse_var_12 + ax0_0_3 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_12 + cse_var_14 + cse_var_13, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 8 + cse_var_14 + cse_var_13, T.bool(False))
            for ax0_0_3, ax1_0_3, ax1_0_4 in T.grid(2, 2, 2):
                cse_var_16: T.int32 = ax1_0_3 * 4
                cse_var_15: T.int32 = ax1_0_4 * 2
                T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 * 4 + 8, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_16 + cse_var_15 + 8, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 8 + cse_var_16 + cse_var_15, T.bool(False))
        Y_reindex_m16n8k8_matrixC_shared_dyn = T.decl_buffer((2048,), "float16", scope="shared.dyn")
        for ax0_0 in range(4):
            A_reindex_shared_dyn_1 = T.Buffer((2048,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
            for ax1_0 in range(4):
                A_reindex_shared_dyn_1[threadIdx_y * 256 + ax1_0 * 64 + threadIdx_x * 2:threadIdx_y * 256 + ax1_0 * 64 + threadIdx_x * 2 + 2] = Y_reindex_m16n8k8_matrixC_2[ax0_0 // 2 * 8 + ax1_0 * 2 + ax0_0 % 2]
            for ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 in range(8):
                Y_1 = T.Buffer((393216,), "float16", data=Y.data)
                Y_1[blockIdx_x // 6 * 98304 + blockIdx_y * 49152 + ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 // 4 * 24576 + ax0_0 * 6144 + threadIdx_y % 2 * 3072 + threadIdx_x // 8 * 768 + blockIdx_x % 6 * 128 + ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 % 4 * 32 + threadIdx_y // 2 * 8 + threadIdx_x % 8] = A_reindex_shared_dyn_1[ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 * 256 + threadIdx_y * 32 + threadIdx_x]
