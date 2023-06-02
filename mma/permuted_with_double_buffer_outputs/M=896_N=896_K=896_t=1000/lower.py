# from tvm.script import ir as I
# from tvm.script import tir as T

@I.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer((896, 896), "float16"), B: T.Buffer((896, 896), "float16"), Y: T.Buffer((896, 896), "float16")):
        T.func_attr({"global_symbol": "main", "tir.noalias": T.bool(True)})
        blockIdx_x = T.launch_thread("blockIdx.x", 1)
        Y_reindex_m16n8k8_matrixC = T.allocate([64], "float16x2", "local")
        A_reindex_shared_dyn_local = T.allocate([20], "float16x8", "local")
        B_reindex_shared_dyn_local = T.allocate([68], "float16x8", "local")
        A_reindex_shared_dyn = T.allocate([8192], "float16", "shared.dyn")
        B_reindex_shared_dyn = T.allocate([8192], "float16", "shared.dyn")
        A_reindex_shared_dyn_m16n8k8_matrixA = T.allocate([16], "float16", "local")
        B_reindex_shared_dyn_m16n8k8_matrixB = T.allocate([64], "float16", "local")
        blockIdx_y = T.launch_thread("blockIdx.y", 49)
        threadIdx_y = T.launch_thread("threadIdx.y", 4)
        threadIdx_x = T.launch_thread("threadIdx.x", 32)
        Y_reindex_m16n8k8_matrixC_1 = T.decl_buffer((128,), "float16", scope="local")
        Y_reindex_m16n8k8_matrixC_2 = T.Buffer((64,), "float16x2", data=Y_reindex_m16n8k8_matrixC, scope="local")
        for ax1_0_3_init, ax0_0_4_init, ax1_0_4_init, b in T.grid(2, 2, 8, 2):
            Y_reindex_m16n8k8_matrixC_2[ax0_0_4_init * 32 + ax1_0_3_init * 16 + ax1_0_4_init * 2 + b] = T.Broadcast(T.float16(0), 2)
        with T.decl_buffer((8192,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn") as A_reindex_shared_dyn_1:
            B_reindex_shared_dyn_1 = T.decl_buffer((8192,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            A_reindex_shared_dyn_local_1 = T.decl_buffer((160,), "float16", scope="local")
            B_reindex_shared_dyn_local_1 = T.decl_buffer((544,), "float16", scope="local")
            A_reindex_shared_dyn_m16n8k8_matrixA_1 = T.decl_buffer((16,), "float16", data=A_reindex_shared_dyn_m16n8k8_matrixA, scope="local")
            B_reindex_shared_dyn_m16n8k8_matrixB_1 = T.decl_buffer((64,), "float16", data=B_reindex_shared_dyn_m16n8k8_matrixB, scope="local")
            A_reindex_shared_dyn_local_2 = T.Buffer((20,), "float16x8", data=A_reindex_shared_dyn_local, scope="local")
            A_1 = T.Buffer((802816,), "float16", data=A.data)
            for ax0_ax1_fused_0_cache in range(4):
                A_reindex_shared_dyn_local_2[ax0_ax1_fused_0_cache * 5] = A_1[blockIdx_y // 7 * 114688 + ax0_ax1_fused_0_cache * 28672 + threadIdx_y * 7168 + threadIdx_x // 4 * 896 + threadIdx_x % 4 * 8:blockIdx_y // 7 * 114688 + ax0_ax1_fused_0_cache * 28672 + threadIdx_y * 7168 + threadIdx_x // 4 * 896 + threadIdx_x % 4 * 8 + 8]
            B_reindex_shared_dyn_local_2 = T.Buffer((68,), "float16x8", data=B_reindex_shared_dyn_local, scope="local")
            B_1 = T.Buffer((802816,), "float16", data=B.data)
            for ax0_ax1_fused_0_cache in range(4):
                B_reindex_shared_dyn_local_2[ax0_ax1_fused_0_cache * 17] = B_1[ax0_ax1_fused_0_cache * 7168 + threadIdx_y * 1792 + threadIdx_x // 16 * 896 + blockIdx_y % 7 * 128 + threadIdx_x % 16 * 8:ax0_ax1_fused_0_cache * 7168 + threadIdx_y * 1792 + threadIdx_x // 16 * 896 + blockIdx_y % 7 * 128 + threadIdx_x % 16 * 8 + 8]
            A_reindex_shared_dyn_2 = T.Buffer((8192,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
            for ax0_ax1_fused_0 in range(4):
                A_reindex_shared_dyn_2[ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x // 4 * 32 + T.bitwise_xor(threadIdx_x % 4, threadIdx_x // 8) * 8:ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x // 4 * 32 + T.bitwise_xor(threadIdx_x % 4, threadIdx_x // 8) * 8 + 8] = A_reindex_shared_dyn_local_2[ax0_ax1_fused_0 * 5]
            B_reindex_shared_dyn_2 = T.Buffer((8192,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            for ax0_ax1_fused_0 in range(4):
                B_reindex_shared_dyn_2[ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x // 8 * 64 + T.bitwise_xor(threadIdx_x % 8, threadIdx_y * 2 + threadIdx_x // 16) * 8:ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x // 8 * 64 + T.bitwise_xor(threadIdx_x % 8, threadIdx_y * 2 + threadIdx_x // 16) * 8 + 8] = B_reindex_shared_dyn_local_2[ax0_ax1_fused_0 * 17]
            T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, 0, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, 0, 1024, 1), threadIdx_y * 1024 + threadIdx_x * 32 + T.bitwise_xor(0, threadIdx_x % 8 // 2) * 8)
            for ax1_0 in range(4):
                T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax1_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, 0, 1024, 1), threadIdx_x % 8 * 128 + ax1_0 // 2 * 64 + T.bitwise_xor(ax1_0 % 2 * 4 + threadIdx_x // 8, threadIdx_x % 8) * 8)
            for ax2_0_0 in range(27):
                for ax0_ax1_fused_0_cache in range(4):
                    A_reindex_shared_dyn_local_2[ax0_ax1_fused_0_cache * 5] = A_1[blockIdx_y // 7 * 114688 + ax0_ax1_fused_0_cache * 28672 + threadIdx_y * 7168 + threadIdx_x // 4 * 896 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 32:blockIdx_y // 7 * 114688 + ax0_ax1_fused_0_cache * 28672 + threadIdx_y * 7168 + threadIdx_x // 4 * 896 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 32 + 8]
                for ax0_ax1_fused_0_cache in range(4):
                    B_reindex_shared_dyn_local_2[ax0_ax1_fused_0_cache * 17] = B_1[ax2_0_0 * 28672 + ax0_ax1_fused_0_cache * 7168 + threadIdx_y * 1792 + threadIdx_x // 16 * 896 + blockIdx_y % 7 * 128 + threadIdx_x % 16 * 8 + 28672:ax2_0_0 * 28672 + ax0_ax1_fused_0_cache * 7168 + threadIdx_y * 1792 + threadIdx_x // 16 * 896 + blockIdx_y % 7 * 128 + threadIdx_x % 16 * 8 + 28672 + 8]
                for ax2_0_1 in range(3):
                    cse_var_1: T.int32 = ax2_0_1 + 1
                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, cse_var_1 % 2 * 8, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax2_0_0 % 2 * 4096, 1024, 1), threadIdx_y * 1024 + threadIdx_x * 32 + T.bitwise_xor(cse_var_1, threadIdx_x % 8 // 2) * 8)
                    for ax1_0 in range(4):
                        T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_1 % 2 * 32 + ax1_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax2_0_0 % 2 * 4096, 1024, 1), ax2_0_1 * 1024 + threadIdx_x % 8 * 128 + ax1_0 // 2 * 64 + T.bitwise_xor(ax1_0 % 2 * 4 + threadIdx_x // 8, threadIdx_x % 8) * 8 + 1024)
                    for ax1_0_3, ax0_0_4, ax1_0_4 in T.grid(2, 2, 8):
                        cse_var_4: T.int32 = ax2_0_1 % 2
                        cse_var_3: T.int32 = ax1_0_3 * 16
                        cse_var_2: T.int32 = ax1_0_4 * 2
                        T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, cse_var_4 * 8 + ax0_0_4 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_4 * 32 + cse_var_3 + cse_var_2, Y_reindex_m16n8k8_matrixC, ax0_0_4 * 32 + cse_var_3 + cse_var_2, T.bool(False))
                for ax0_ax1_fused_0 in range(4):
                    A_reindex_shared_dyn_2[(ax2_0_0 + 1) % 2 * 4096 + ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x // 4 * 32 + T.bitwise_xor(threadIdx_x % 4, threadIdx_x // 8) * 8:(ax2_0_0 + 1) % 2 * 4096 + ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x // 4 * 32 + T.bitwise_xor(threadIdx_x % 4, threadIdx_x // 8) * 8 + 8] = A_reindex_shared_dyn_local_2[ax0_ax1_fused_0 * 5]
                for ax0_ax1_fused_0 in range(4):
                    B_reindex_shared_dyn_2[(ax2_0_0 + 1) % 2 * 4096 + ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x // 8 * 64 + T.bitwise_xor(threadIdx_x % 8, threadIdx_y * 2 + threadIdx_x // 16) * 8:(ax2_0_0 + 1) % 2 * 4096 + ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x // 8 * 64 + T.bitwise_xor(threadIdx_x % 8, threadIdx_y * 2 + threadIdx_x // 16) * 8 + 8] = B_reindex_shared_dyn_local_2[ax0_ax1_fused_0 * 17]
                T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, 0, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, (ax2_0_0 + 1) % 2 * 4096, 1024, 1), threadIdx_y * 1024 + threadIdx_x * 32 + T.bitwise_xor(0, threadIdx_x % 8 // 2) * 8)
                for ax1_0 in range(4):
                    T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax1_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, (ax2_0_0 + 1) % 2 * 4096, 1024, 1), threadIdx_x % 8 * 128 + ax1_0 // 2 * 64 + T.bitwise_xor(ax1_0 % 2 * 4 + threadIdx_x // 8, threadIdx_x % 8) * 8)
                for ax1_0_3, ax0_0_4, ax1_0_4 in T.grid(2, 2, 8):
                    cse_var_6: T.int32 = ax1_0_3 * 16
                    cse_var_5: T.int32 = ax1_0_4 * 2
                    T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_4 * 4 + 8, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_6 + cse_var_5 + 32, Y_reindex_m16n8k8_matrixC, ax0_0_4 * 32 + cse_var_6 + cse_var_5, T.bool(False))
            for ax2_0_1 in range(3):
                cse_var_7: T.int32 = ax2_0_1 + 1
                T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, cse_var_7 % 2 * 8, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, 4096, 1024, 1), threadIdx_y * 1024 + threadIdx_x * 32 + T.bitwise_xor(cse_var_7, threadIdx_x % 8 // 2) * 8)
                for ax1_0 in range(4):
                    T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_7 % 2 * 32 + ax1_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, 4096, 1024, 1), ax2_0_1 * 1024 + threadIdx_x % 8 * 128 + ax1_0 // 2 * 64 + T.bitwise_xor(ax1_0 % 2 * 4 + threadIdx_x // 8, threadIdx_x % 8) * 8 + 1024)
                for ax1_0_3, ax0_0_4, ax1_0_4 in T.grid(2, 2, 8):
                    cse_var_10: T.int32 = ax2_0_1 % 2
                    cse_var_9: T.int32 = ax1_0_3 * 16
                    cse_var_8: T.int32 = ax1_0_4 * 2
                    T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, cse_var_10 * 8 + ax0_0_4 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_10 * 32 + cse_var_9 + cse_var_8, Y_reindex_m16n8k8_matrixC, ax0_0_4 * 32 + cse_var_9 + cse_var_8, T.bool(False))
            for ax1_0_3, ax0_0_4, ax1_0_4 in T.grid(2, 2, 8):
                cse_var_12: T.int32 = ax1_0_3 * 16
                cse_var_11: T.int32 = ax1_0_4 * 2
                T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_4 * 4 + 8, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_12 + cse_var_11 + 32, Y_reindex_m16n8k8_matrixC, ax0_0_4 * 32 + cse_var_12 + cse_var_11, T.bool(False))
        Y_reindex_m16n8k8_matrixC_shared_dyn = T.decl_buffer((4096,), "float16", scope="shared.dyn")
        for ax0_0 in range(4):
            A_reindex_shared_dyn_1 = T.Buffer((4096,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
            for ax1_0 in range(16):
                A_reindex_shared_dyn_1[threadIdx_y * 1024 + ax1_0 * 64 + threadIdx_x * 2:threadIdx_y * 1024 + ax1_0 * 64 + threadIdx_x * 2 + 2] = Y_reindex_m16n8k8_matrixC_2[ax0_0 // 2 * 32 + ax1_0 * 2 + ax0_0 % 2]
            for ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 in range(32):
                Y_1 = T.Buffer((802816,), "float16", data=Y.data)
                Y_1[blockIdx_y // 7 * 114688 + ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 // 8 * 28672 + ax0_0 * 7168 + threadIdx_y % 2 * 3584 + threadIdx_x // 8 * 896 + blockIdx_y % 7 * 128 + ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 % 8 * 16 + threadIdx_y // 2 * 8 + threadIdx_x % 8] = A_reindex_shared_dyn_1[ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 * 128 + threadIdx_y * 32 + threadIdx_x]
