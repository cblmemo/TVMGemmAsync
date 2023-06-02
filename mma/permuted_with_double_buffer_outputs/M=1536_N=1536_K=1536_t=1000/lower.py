# from tvm.script import ir as I
# from tvm.script import tir as T

@I.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer((1536, 1536), "float16"), B: T.Buffer((1536, 1536), "float16"), Y: T.Buffer((1536, 1536), "float16")):
        T.func_attr({"global_symbol": "main", "tir.noalias": T.bool(True)})
        blockIdx_x = T.launch_thread("blockIdx.x", 24)
        Y_reindex_m16n8k8_matrixC = T.allocate([96], "float16x2", "local")
        A_reindex_shared_dyn_local = T.allocate([15], "float16x8", "local")
        B_reindex_shared_dyn_local = T.allocate([34], "float16x8", "local")
        A_reindex_shared_dyn = T.allocate([6144], "float16", "shared.dyn")
        B_reindex_shared_dyn = T.allocate([4096], "float16", "shared.dyn")
        A_reindex_shared_dyn_m16n8k8_matrixA = T.allocate([48], "float16", "local")
        B_reindex_shared_dyn_m16n8k8_matrixB = T.allocate([32], "float16", "local")
        blockIdx_y = T.launch_thread("blockIdx.y", 4)
        threadIdx_y = T.launch_thread("threadIdx.y", 4)
        threadIdx_x = T.launch_thread("threadIdx.x", 32)
        Y_reindex_m16n8k8_matrixC_1 = T.decl_buffer((192,), "float16", scope="local")
        Y_reindex_m16n8k8_matrixC_2 = T.Buffer((96,), "float16x2", data=Y_reindex_m16n8k8_matrixC, scope="local")
        for ax0_0_3_init, ax1_0_3_init, ax1_0_4_init, b in T.grid(6, 4, 2, 2):
            Y_reindex_m16n8k8_matrixC_2[ax0_0_3_init * 16 + ax1_0_3_init * 4 + ax1_0_4_init * 2 + b] = T.Broadcast(T.float16(0), 2)
        with T.decl_buffer((6144,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn") as A_reindex_shared_dyn_1:
            B_reindex_shared_dyn_1 = T.decl_buffer((4096,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            A_reindex_shared_dyn_local_1 = T.decl_buffer((120,), "float16", scope="local")
            B_reindex_shared_dyn_local_1 = T.decl_buffer((272,), "float16", scope="local")
            A_reindex_shared_dyn_m16n8k8_matrixA_1 = T.decl_buffer((48,), "float16", data=A_reindex_shared_dyn_m16n8k8_matrixA, scope="local")
            B_reindex_shared_dyn_m16n8k8_matrixB_1 = T.decl_buffer((32,), "float16", data=B_reindex_shared_dyn_m16n8k8_matrixB, scope="local")
            A_reindex_shared_dyn_local_2 = T.Buffer((15,), "float16x8", data=A_reindex_shared_dyn_local, scope="local")
            A_1 = T.Buffer((2359296,), "float16", data=A.data)
            for ax0_ax1_fused_0_cache in range(3):
                A_reindex_shared_dyn_local_2[ax0_ax1_fused_0_cache * 5] = A_1[blockIdx_x // 12 * 1179648 + blockIdx_y * 294912 + ax0_ax1_fused_0_cache * 98304 + threadIdx_y * 24576 + threadIdx_x // 2 * 1536 + threadIdx_x % 2 * 8:blockIdx_x // 12 * 1179648 + blockIdx_y * 294912 + ax0_ax1_fused_0_cache * 98304 + threadIdx_y * 24576 + threadIdx_x // 2 * 1536 + threadIdx_x % 2 * 8 + 8]
            B_reindex_shared_dyn_local_2 = T.Buffer((34,), "float16x8", data=B_reindex_shared_dyn_local, scope="local")
            B_1 = T.Buffer((2359296,), "float16", data=B.data)
            for ax0_ax1_fused_0_cache in range(2):
                B_reindex_shared_dyn_local_2[ax0_ax1_fused_0_cache * 17] = B_1[ax0_ax1_fused_0_cache * 12288 + threadIdx_y * 3072 + threadIdx_x // 16 * 1536 + blockIdx_x % 12 * 128 + threadIdx_x % 16 * 8:ax0_ax1_fused_0_cache * 12288 + threadIdx_y * 3072 + threadIdx_x // 16 * 1536 + blockIdx_x % 12 * 128 + threadIdx_x % 16 * 8 + 8]
            A_reindex_shared_dyn_2 = T.Buffer((6144,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
            for ax0_ax1_fused_0 in range(3):
                A_reindex_shared_dyn_2[ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x * 8:ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = A_reindex_shared_dyn_local_2[ax0_ax1_fused_0 * 5]
            B_reindex_shared_dyn_2 = T.Buffer((4096,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            for ax0_ax1_fused_0 in range(2):
                B_reindex_shared_dyn_2[ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x // 8 * 64 + T.bitwise_xor(threadIdx_x % 8, threadIdx_y * 2 + threadIdx_x // 16) * 8:ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x // 8 * 64 + T.bitwise_xor(threadIdx_x % 8, threadIdx_y * 2 + threadIdx_x // 16) * 8 + 8] = B_reindex_shared_dyn_local_2[ax0_ax1_fused_0 * 17]
            for ax0_0 in range(3):
                T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y // 2 * 1536 + ax0_0 * 512, 512, 1), threadIdx_x * 16)
            for ax1_0 in range(2):
                T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax1_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, 0, 1024, 1), threadIdx_x % 8 * 128 + threadIdx_y % 2 * 64 + T.bitwise_xor(ax1_0 * 4 + threadIdx_x // 8, threadIdx_x % 8) * 8)
            for ax2_0_0 in range(95):
                for ax0_ax1_fused_0_cache in range(3):
                    A_reindex_shared_dyn_local_2[ax0_ax1_fused_0_cache * 5] = A_1[blockIdx_x // 12 * 1179648 + blockIdx_y * 294912 + ax0_ax1_fused_0_cache * 98304 + threadIdx_y * 24576 + threadIdx_x // 2 * 1536 + ax2_0_0 * 16 + threadIdx_x % 2 * 8 + 16:blockIdx_x // 12 * 1179648 + blockIdx_y * 294912 + ax0_ax1_fused_0_cache * 98304 + threadIdx_y * 24576 + threadIdx_x // 2 * 1536 + ax2_0_0 * 16 + threadIdx_x % 2 * 8 + 16 + 8]
                for ax0_ax1_fused_0_cache in range(2):
                    B_reindex_shared_dyn_local_2[ax0_ax1_fused_0_cache * 17] = B_1[ax2_0_0 * 24576 + ax0_ax1_fused_0_cache * 12288 + threadIdx_y * 3072 + threadIdx_x // 16 * 1536 + blockIdx_x % 12 * 128 + threadIdx_x % 16 * 8 + 24576:ax2_0_0 * 24576 + ax0_ax1_fused_0_cache * 12288 + threadIdx_y * 3072 + threadIdx_x // 16 * 1536 + blockIdx_x % 12 * 128 + threadIdx_x % 16 * 8 + 24576 + 8]
                for ax0_0 in range(3):
                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8 + 24, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax2_0_0 % 2 * 3072 + threadIdx_y // 2 * 1536 + ax0_0 * 512 + 8, 512, 1), threadIdx_x * 16)
                for ax1_0 in range(2):
                    T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax1_0 * 8 + 16, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax2_0_0 % 2 * 2048, 1024, 1), threadIdx_x % 8 * 128 + threadIdx_y % 2 * 64 + T.bitwise_xor(ax1_0 * 4 + threadIdx_x // 8, threadIdx_x % 8) * 8 + 1024)
                for ax0_0_3, ax1_0_3, ax1_0_4 in T.grid(6, 4, 2):
                    cse_var_2: T.int32 = ax1_0_3 * 4
                    cse_var_1: T.int32 = ax1_0_4 * 2
                    T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_2 + cse_var_1, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 16 + cse_var_2 + cse_var_1, T.bool(False))
                for ax0_ax1_fused_0 in range(3):
                    A_reindex_shared_dyn_2[(ax2_0_0 + 1) % 2 * 3072 + ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x * 8:(ax2_0_0 + 1) % 2 * 3072 + ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = A_reindex_shared_dyn_local_2[ax0_ax1_fused_0 * 5]
                for ax0_ax1_fused_0 in range(2):
                    B_reindex_shared_dyn_2[(ax2_0_0 + 1) % 2 * 2048 + ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x // 8 * 64 + T.bitwise_xor(threadIdx_x % 8, threadIdx_y * 2 + threadIdx_x // 16) * 8:(ax2_0_0 + 1) % 2 * 2048 + ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x // 8 * 64 + T.bitwise_xor(threadIdx_x % 8, threadIdx_y * 2 + threadIdx_x // 16) * 8 + 8] = B_reindex_shared_dyn_local_2[ax0_ax1_fused_0 * 17]
                for ax0_0 in range(3):
                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, (ax2_0_0 + 1) % 2 * 3072 + threadIdx_y // 2 * 1536 + ax0_0 * 512, 512, 1), threadIdx_x * 16)
                for ax1_0 in range(2):
                    T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax1_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, (ax2_0_0 + 1) % 2 * 2048, 1024, 1), threadIdx_x % 8 * 128 + threadIdx_y % 2 * 64 + T.bitwise_xor(ax1_0 * 4 + threadIdx_x // 8, threadIdx_x % 8) * 8)
                for ax0_0_3, ax1_0_3, ax1_0_4 in T.grid(6, 4, 2):
                    cse_var_4: T.int32 = ax1_0_3 * 4
                    cse_var_3: T.int32 = ax1_0_4 * 2
                    T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 * 4 + 24, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_4 + cse_var_3 + 16, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 16 + cse_var_4 + cse_var_3, T.bool(False))
            for ax0_0 in range(3):
                T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8 + 24, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y // 2 * 1536 + ax0_0 * 512 + 3080, 512, 1), threadIdx_x * 16)
            for ax1_0 in range(2):
                T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax1_0 * 8 + 16, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, 2048, 1024, 1), threadIdx_x % 8 * 128 + threadIdx_y % 2 * 64 + T.bitwise_xor(ax1_0 * 4 + threadIdx_x // 8, threadIdx_x % 8) * 8 + 1024)
            for ax0_0_3, ax1_0_3, ax1_0_4 in T.grid(6, 4, 2):
                cse_var_6: T.int32 = ax1_0_3 * 4
                cse_var_5: T.int32 = ax1_0_4 * 2
                T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_6 + cse_var_5, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 16 + cse_var_6 + cse_var_5, T.bool(False))
            for ax0_0_3, ax1_0_3, ax1_0_4 in T.grid(6, 4, 2):
                cse_var_8: T.int32 = ax1_0_3 * 4
                cse_var_7: T.int32 = ax1_0_4 * 2
                T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 * 4 + 24, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_8 + cse_var_7 + 16, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 16 + cse_var_8 + cse_var_7, T.bool(False))
        Y_reindex_m16n8k8_matrixC_shared_dyn = T.decl_buffer((2048,), "float16", scope="shared.dyn")
        for ax0_0 in range(12):
            B_reindex_shared_dyn_1 = T.Buffer((2048,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            for ax1_0 in range(8):
                B_reindex_shared_dyn_1[threadIdx_y * 512 + ax1_0 * 64 + threadIdx_x * 2:threadIdx_y * 512 + ax1_0 * 64 + threadIdx_x * 2 + 2] = Y_reindex_m16n8k8_matrixC_2[ax0_0 // 2 * 16 + ax1_0 * 2 + ax0_0 % 2]
            for ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 in range(16):
                Y_1 = T.Buffer((2359296,), "float16", data=Y.data)
                Y_1[blockIdx_x // 12 * 1179648 + blockIdx_y * 294912 + ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 // 8 * 147456 + ax0_0 * 12288 + threadIdx_y % 2 * 6144 + threadIdx_x // 8 * 1536 + blockIdx_x % 12 * 128 + ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 % 8 * 16 + threadIdx_y // 2 * 8 + threadIdx_x % 8] = B_reindex_shared_dyn_1[ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 * 128 + threadIdx_y * 32 + threadIdx_x]
