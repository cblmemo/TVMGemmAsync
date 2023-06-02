# from tvm.script import ir as I
# from tvm.script import tir as T

@I.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer((512, 768), "float16"), B: T.Buffer((768, 3072), "float16"), Y: T.Buffer((512, 3072), "float16")):
        T.func_attr({"global_symbol": "main", "tir.noalias": T.bool(True)})
        blockIdx_x = T.launch_thread("blockIdx.x", 8)
        Y_reindex_m16n8k8_matrixC = T.allocate([32], "float16x2", "local")
        A_reindex_shared_dyn_local = T.allocate([20], "float16x8", "local")
        B_reindex_shared_dyn_local = T.allocate([18], "float16x8", "local")
        A_reindex_shared_dyn = T.allocate([8192], "float16", "shared.dyn")
        B_reindex_shared_dyn = T.allocate([4096], "float16", "shared.dyn")
        A_reindex_shared_dyn_m16n8k8_matrixA = T.allocate([32], "float16", "local")
        B_reindex_shared_dyn_m16n8k8_matrixB = T.allocate([64], "float16", "local")
        blockIdx_y = T.launch_thread("blockIdx.y", 24)
        threadIdx_y = T.launch_thread("threadIdx.y", 4)
        threadIdx_x = T.launch_thread("threadIdx.x", 32)
        Y_reindex_m16n8k8_matrixC_1 = T.decl_buffer((64,), "float16", scope="local")
        Y_reindex_m16n8k8_matrixC_2 = T.Buffer((32,), "float16x2", data=Y_reindex_m16n8k8_matrixC, scope="local")
        for ax0_0_4_init, ax1_0_4_init, b in T.grid(2, 8, 2):
            Y_reindex_m16n8k8_matrixC_2[ax0_0_4_init * 16 + ax1_0_4_init * 2 + b] = T.Broadcast(T.float16(0), 2)
        with T.decl_buffer((8192,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn") as A_reindex_shared_dyn_1:
            B_reindex_shared_dyn_1 = T.decl_buffer((4096,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            A_reindex_shared_dyn_local_1 = T.decl_buffer((160,), "float16", scope="local")
            B_reindex_shared_dyn_local_1 = T.decl_buffer((144,), "float16", scope="local")
            A_reindex_shared_dyn_m16n8k8_matrixA_1 = T.decl_buffer((32,), "float16", data=A_reindex_shared_dyn_m16n8k8_matrixA, scope="local")
            B_reindex_shared_dyn_m16n8k8_matrixB_1 = T.decl_buffer((64,), "float16", data=B_reindex_shared_dyn_m16n8k8_matrixB, scope="local")
            A_reindex_shared_dyn_local_2 = T.Buffer((20,), "float16x8", data=A_reindex_shared_dyn_local, scope="local")
            A_1 = T.Buffer((393216,), "float16", data=A.data)
            for ax0_ax1_fused_0_cache in range(4):
                A_reindex_shared_dyn_local_2[ax0_ax1_fused_0_cache * 5] = A_1[blockIdx_x // 2 * 98304 + ax0_ax1_fused_0_cache * 24576 + threadIdx_y * 6144 + threadIdx_x // 4 * 768 + threadIdx_x % 4 * 8:blockIdx_x // 2 * 98304 + ax0_ax1_fused_0_cache * 24576 + threadIdx_y * 6144 + threadIdx_x // 4 * 768 + threadIdx_x % 4 * 8 + 8]
            B_reindex_shared_dyn_local_2 = T.Buffer((18,), "float16x8", data=B_reindex_shared_dyn_local, scope="local")
            B_1 = T.Buffer((2359296,), "float16", data=B.data)
            for ax0_ax1_fused_0_cache in range(2):
                B_reindex_shared_dyn_local_2[ax0_ax1_fused_0_cache * 9] = B_1[ax0_ax1_fused_0_cache * 49152 + threadIdx_y * 12288 + threadIdx_x // 8 * 3072 + blockIdx_x % 2 * 1536 + blockIdx_y * 64 + threadIdx_x % 8 * 8:ax0_ax1_fused_0_cache * 49152 + threadIdx_y * 12288 + threadIdx_x // 8 * 3072 + blockIdx_x % 2 * 1536 + blockIdx_y * 64 + threadIdx_x % 8 * 8 + 8]
            A_reindex_shared_dyn_2 = T.Buffer((8192,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
            for ax0_ax1_fused_0 in range(4):
                A_reindex_shared_dyn_2[ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x // 4 * 32 + T.bitwise_xor(threadIdx_x % 4, threadIdx_x // 8) * 8:ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x // 4 * 32 + T.bitwise_xor(threadIdx_x % 4, threadIdx_x // 8) * 8 + 8] = A_reindex_shared_dyn_local_2[ax0_ax1_fused_0 * 5]
            B_reindex_shared_dyn_2 = T.Buffer((4096,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            for ax0_ax1_fused_0 in range(2):
                B_reindex_shared_dyn_2[ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x // 8 * 64 + T.bitwise_xor(threadIdx_x % 8, threadIdx_y % 2 * 4 + threadIdx_x // 8) * 8:ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x // 8 * 64 + T.bitwise_xor(threadIdx_x % 8, threadIdx_y % 2 * 4 + threadIdx_x // 8) * 8 + 8] = B_reindex_shared_dyn_local_2[ax0_ax1_fused_0 * 9]
            for ax1_0 in range(2):
                T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax1_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, 0, 1024, 1), threadIdx_y * 1024 + threadIdx_x * 32 + T.bitwise_xor(ax1_0, threadIdx_x % 8 // 2) * 8)
            for ax0_0, ax1_0 in T.grid(2, 2):
                T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax0_0 * 16 + ax1_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, 0, 512, 1), ax0_0 * 512 + threadIdx_x % 8 * 64 + T.bitwise_xor(ax1_0 * 4 + threadIdx_x // 8, threadIdx_x % 8) * 8)
            for ax2_0_0 in range(23):
                for ax0_ax1_fused_0_cache in range(4):
                    A_reindex_shared_dyn_local_2[ax0_ax1_fused_0_cache * 5] = A_1[blockIdx_x // 2 * 98304 + ax0_ax1_fused_0_cache * 24576 + threadIdx_y * 6144 + threadIdx_x // 4 * 768 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 32:blockIdx_x // 2 * 98304 + ax0_ax1_fused_0_cache * 24576 + threadIdx_y * 6144 + threadIdx_x // 4 * 768 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 32 + 8]
                for ax0_ax1_fused_0_cache in range(2):
                    B_reindex_shared_dyn_local_2[ax0_ax1_fused_0_cache * 9] = B_1[ax2_0_0 * 98304 + ax0_ax1_fused_0_cache * 49152 + threadIdx_y * 12288 + threadIdx_x // 8 * 3072 + blockIdx_x % 2 * 1536 + blockIdx_y * 64 + threadIdx_x % 8 * 8 + 98304:ax2_0_0 * 98304 + ax0_ax1_fused_0_cache * 49152 + threadIdx_y * 12288 + threadIdx_x // 8 * 3072 + blockIdx_x % 2 * 1536 + blockIdx_y * 64 + threadIdx_x % 8 * 8 + 98304 + 8]
                for ax1_0 in range(2):
                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax1_0 * 8 + 16, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax2_0_0 % 2 * 4096, 1024, 1), threadIdx_y * 1024 + threadIdx_x * 32 + T.bitwise_xor(ax1_0 + 2, threadIdx_x % 8 // 2) * 8)
                for ax0_0, ax1_0 in T.grid(2, 2):
                    T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax0_0 * 16 + ax1_0 * 8 + 32, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax2_0_0 % 2 * 2048, 512, 1), ax0_0 * 512 + threadIdx_x % 8 * 64 + T.bitwise_xor(ax1_0 * 4 + threadIdx_x // 8, threadIdx_x % 8) * 8 + 1024)
                for ax2_0_2, ax0_0_4, ax1_0_4 in T.grid(2, 2, 8):
                    cse_var_1: T.int32 = ax1_0_4 * 2
                    T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax2_0_2 * 8 + ax0_0_4 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, ax2_0_2 * 16 + cse_var_1, Y_reindex_m16n8k8_matrixC, ax0_0_4 * 16 + cse_var_1, T.bool(False))
                for ax0_ax1_fused_0 in range(4):
                    A_reindex_shared_dyn_2[(ax2_0_0 + 1) % 2 * 4096 + ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x // 4 * 32 + T.bitwise_xor(threadIdx_x % 4, threadIdx_x // 8) * 8:(ax2_0_0 + 1) % 2 * 4096 + ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x // 4 * 32 + T.bitwise_xor(threadIdx_x % 4, threadIdx_x // 8) * 8 + 8] = A_reindex_shared_dyn_local_2[ax0_ax1_fused_0 * 5]
                for ax0_ax1_fused_0 in range(2):
                    B_reindex_shared_dyn_2[(ax2_0_0 + 1) % 2 * 2048 + ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x // 8 * 64 + T.bitwise_xor(threadIdx_x % 8, threadIdx_y % 2 * 4 + threadIdx_x // 8) * 8:(ax2_0_0 + 1) % 2 * 2048 + ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x // 8 * 64 + T.bitwise_xor(threadIdx_x % 8, threadIdx_y % 2 * 4 + threadIdx_x // 8) * 8 + 8] = B_reindex_shared_dyn_local_2[ax0_ax1_fused_0 * 9]
                for ax1_0 in range(2):
                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax1_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, (ax2_0_0 + 1) % 2 * 4096, 1024, 1), threadIdx_y * 1024 + threadIdx_x * 32 + T.bitwise_xor(ax1_0, threadIdx_x % 8 // 2) * 8)
                for ax0_0, ax1_0 in T.grid(2, 2):
                    T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax0_0 * 16 + ax1_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, (ax2_0_0 + 1) % 2 * 2048, 512, 1), ax0_0 * 512 + threadIdx_x % 8 * 64 + T.bitwise_xor(ax1_0 * 4 + threadIdx_x // 8, threadIdx_x % 8) * 8)
                for ax2_0_2, ax0_0_4, ax1_0_4 in T.grid(2, 2, 8):
                    cse_var_2: T.int32 = ax1_0_4 * 2
                    T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax2_0_2 * 8 + ax0_0_4 * 4 + 16, B_reindex_shared_dyn_m16n8k8_matrixB, ax2_0_2 * 16 + cse_var_2 + 32, Y_reindex_m16n8k8_matrixC, ax0_0_4 * 16 + cse_var_2, T.bool(False))
            for ax1_0 in range(2):
                T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax1_0 * 8 + 16, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, 4096, 1024, 1), threadIdx_y * 1024 + threadIdx_x * 32 + T.bitwise_xor(ax1_0 + 2, threadIdx_x % 8 // 2) * 8)
            for ax0_0, ax1_0 in T.grid(2, 2):
                T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax0_0 * 16 + ax1_0 * 8 + 32, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, 2048, 512, 1), ax0_0 * 512 + threadIdx_x % 8 * 64 + T.bitwise_xor(ax1_0 * 4 + threadIdx_x // 8, threadIdx_x % 8) * 8 + 1024)
            for ax2_0_2, ax0_0_4, ax1_0_4 in T.grid(2, 2, 8):
                cse_var_3: T.int32 = ax1_0_4 * 2
                T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax2_0_2 * 8 + ax0_0_4 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, ax2_0_2 * 16 + cse_var_3, Y_reindex_m16n8k8_matrixC, ax0_0_4 * 16 + cse_var_3, T.bool(False))
            for ax2_0_2, ax0_0_4, ax1_0_4 in T.grid(2, 2, 8):
                cse_var_4: T.int32 = ax1_0_4 * 2
                T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax2_0_2 * 8 + ax0_0_4 * 4 + 16, B_reindex_shared_dyn_m16n8k8_matrixB, ax2_0_2 * 16 + cse_var_4 + 32, Y_reindex_m16n8k8_matrixC, ax0_0_4 * 16 + cse_var_4, T.bool(False))
        Y_reindex_m16n8k8_matrixC_shared_dyn = T.decl_buffer((2048,), "float16", scope="shared.dyn")
        for ax0_0 in range(4):
            B_reindex_shared_dyn_1 = T.Buffer((2048,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            for ax1_0 in range(8):
                B_reindex_shared_dyn_1[threadIdx_y * 512 + ax1_0 * 64 + threadIdx_x * 2:threadIdx_y * 512 + ax1_0 * 64 + threadIdx_x * 2 + 2] = Y_reindex_m16n8k8_matrixC_2[ax0_0 // 2 * 16 + ax1_0 * 2 + ax0_0 % 2]
            for ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 in range(16):
                Y_1 = T.Buffer((1572864,), "float16", data=Y.data)
                Y_1[blockIdx_x // 2 * 393216 + ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 // 4 * 98304 + ax0_0 * 24576 + threadIdx_y % 2 * 12288 + threadIdx_x // 8 * 3072 + blockIdx_x % 2 * 1536 + blockIdx_y * 64 + ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 % 4 * 16 + threadIdx_y // 2 * 8 + threadIdx_x % 8] = B_reindex_shared_dyn_1[ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 * 128 + threadIdx_y * 32 + threadIdx_x]
