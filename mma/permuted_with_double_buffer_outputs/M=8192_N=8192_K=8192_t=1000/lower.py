# from tvm.script import ir as I
# from tvm.script import tir as T

@I.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer((8192, 8192), "float16"), B: T.Buffer((8192, 8192), "float16"), Y: T.Buffer((8192, 8192), "float16")):
        T.func_attr({"global_symbol": "main", "tir.noalias": T.bool(True)})
        blockIdx_x = T.launch_thread("blockIdx.x", 64)
        Y_reindex_m16n8k8_matrixC = T.allocate([128], "float16x2", "local")
        A_reindex_shared_dyn_local = T.allocate([5], "float16x8", "local")
        B_reindex_shared_dyn_local = T.allocate([260], "float16x8", "local")
        A_reindex_shared_dyn = T.allocate([4096], "float16", "shared.dyn")
        B_reindex_shared_dyn = T.allocate([16384], "float16", "shared.dyn")
        A_reindex_shared_dyn_m16n8k8_matrixA = T.allocate([32], "float16", "local")
        B_reindex_shared_dyn_m16n8k8_matrixB = T.allocate([64], "float16", "local")
        blockIdx_y = T.launch_thread("blockIdx.y", 16)
        threadIdx_y = T.launch_thread("threadIdx.y", 8)
        threadIdx_x = T.launch_thread("threadIdx.x", 32)
        Y_reindex_m16n8k8_matrixC_1 = T.decl_buffer((256,), "float16", scope="local")
        Y_reindex_m16n8k8_matrixC_2 = T.Buffer((128,), "float16x2", data=Y_reindex_m16n8k8_matrixC, scope="local")
        for ax0_0_4_init, ax1_0_4_init, b in T.grid(4, 16, 2):
            Y_reindex_m16n8k8_matrixC_2[ax0_0_4_init * 32 + ax1_0_4_init * 2 + b] = T.Broadcast(T.float16(0), 2)
        with T.decl_buffer((4096,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn") as A_reindex_shared_dyn_1:
            B_reindex_shared_dyn_1 = T.decl_buffer((16384,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            A_reindex_shared_dyn_local_1 = T.decl_buffer((40,), "float16", scope="local")
            B_reindex_shared_dyn_local_1 = T.decl_buffer((2080,), "float16", scope="local")
            A_reindex_shared_dyn_m16n8k8_matrixA_1 = T.decl_buffer((32,), "float16", data=A_reindex_shared_dyn_m16n8k8_matrixA, scope="local")
            B_reindex_shared_dyn_m16n8k8_matrixB_1 = T.decl_buffer((64,), "float16", data=B_reindex_shared_dyn_m16n8k8_matrixB, scope="local")
            A_reindex_shared_dyn_local_2 = T.Buffer((5,), "float16x8", data=A_reindex_shared_dyn_local, scope="local")
            A_1 = T.Buffer((67108864,), "float16", data=A.data)
            A_reindex_shared_dyn_local_2[0] = A_1[blockIdx_x // 4 * 4194304 + blockIdx_y // 4 * 1048576 + threadIdx_y * 131072 + threadIdx_x // 2 * 8192 + threadIdx_x % 2 * 8:blockIdx_x // 4 * 4194304 + blockIdx_y // 4 * 1048576 + threadIdx_y * 131072 + threadIdx_x // 2 * 8192 + threadIdx_x % 2 * 8 + 8]
            B_reindex_shared_dyn_local_2 = T.Buffer((260,), "float16x8", data=B_reindex_shared_dyn_local, scope="local")
            B_1 = T.Buffer((67108864,), "float16", data=B.data)
            for ax0_ax1_fused_0_cache in range(4):
                B_reindex_shared_dyn_local_2[ax0_ax1_fused_0_cache * 65] = B_1[ax0_ax1_fused_0_cache * 32768 + threadIdx_y // 2 * 8192 + blockIdx_x % 4 * 2048 + blockIdx_y % 4 * 512 + threadIdx_y % 2 * 256 + threadIdx_x * 8:ax0_ax1_fused_0_cache * 32768 + threadIdx_y // 2 * 8192 + blockIdx_x % 4 * 2048 + blockIdx_y % 4 * 512 + threadIdx_y % 2 * 256 + threadIdx_x * 8 + 8]
            A_reindex_shared_dyn_2 = T.Buffer((4096,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
            A_reindex_shared_dyn_2[threadIdx_y * 256 + threadIdx_x * 8:threadIdx_y * 256 + threadIdx_x * 8 + 8] = A_reindex_shared_dyn_local_2[0]
            B_reindex_shared_dyn_2 = T.Buffer((16384,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            for ax0_ax1_fused_0 in range(4):
                B_reindex_shared_dyn_2[ax0_ax1_fused_0 * 2048 + threadIdx_y * 256 + threadIdx_x // 8 * 64 + T.bitwise_xor(threadIdx_x % 8, ax0_ax1_fused_0 % 2 * 4 + threadIdx_y // 2) * 8:ax0_ax1_fused_0 * 2048 + threadIdx_y * 256 + threadIdx_x // 8 * 64 + T.bitwise_xor(threadIdx_x % 8, ax0_ax1_fused_0 % 2 * 4 + threadIdx_y // 2) * 8 + 8] = B_reindex_shared_dyn_local_2[ax0_ax1_fused_0 * 65]
            for ax0_0 in range(2):
                T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y // 4 * 1024 + ax0_0 * 512, 512, 1), threadIdx_x * 16)
            for ax1_0 in range(4):
                T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax1_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, 0, 4096, 1), threadIdx_x % 8 * 512 + threadIdx_y % 4 * 128 + ax1_0 // 2 * 64 + T.bitwise_xor(ax1_0 % 2 * 4 + threadIdx_x // 8, threadIdx_x % 8) * 8)
            for ax2_0_0 in range(511):
                A_reindex_shared_dyn_local_2[0] = A_1[blockIdx_x // 4 * 4194304 + blockIdx_y // 4 * 1048576 + threadIdx_y * 131072 + threadIdx_x // 2 * 8192 + ax2_0_0 * 16 + threadIdx_x % 2 * 8 + 16:blockIdx_x // 4 * 4194304 + blockIdx_y // 4 * 1048576 + threadIdx_y * 131072 + threadIdx_x // 2 * 8192 + ax2_0_0 * 16 + threadIdx_x % 2 * 8 + 16 + 8]
                for ax0_ax1_fused_0_cache in range(4):
                    B_reindex_shared_dyn_local_2[ax0_ax1_fused_0_cache * 65] = B_1[ax2_0_0 * 131072 + ax0_ax1_fused_0_cache * 32768 + threadIdx_y // 2 * 8192 + blockIdx_x % 4 * 2048 + blockIdx_y % 4 * 512 + threadIdx_y % 2 * 256 + threadIdx_x * 8 + 131072:ax2_0_0 * 131072 + ax0_ax1_fused_0_cache * 32768 + threadIdx_y // 2 * 8192 + blockIdx_x % 4 * 2048 + blockIdx_y % 4 * 512 + threadIdx_y % 2 * 256 + threadIdx_x * 8 + 131072 + 8]
                for ax0_0 in range(2):
                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8 + 16, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax2_0_0 % 2 * 2048 + threadIdx_y // 4 * 1024 + ax0_0 * 512 + 8, 512, 1), threadIdx_x * 16)
                for ax1_0 in range(4):
                    T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax1_0 * 8 + 32, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax2_0_0 % 2 * 8192, 4096, 1), threadIdx_x % 8 * 512 + threadIdx_y % 4 * 128 + ax1_0 // 2 * 64 + T.bitwise_xor(ax1_0 % 2 * 4 + threadIdx_x // 8, threadIdx_x % 8) * 8 + 4096)
                for ax0_0_4, ax1_0_4 in T.grid(4, 16):
                    cse_var_1: T.int32 = ax1_0_4 * 2
                    T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_4 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_1, Y_reindex_m16n8k8_matrixC, ax0_0_4 * 32 + cse_var_1, T.bool(False))
                A_reindex_shared_dyn_2[(ax2_0_0 + 1) % 2 * 2048 + threadIdx_y * 256 + threadIdx_x * 8:(ax2_0_0 + 1) % 2 * 2048 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = A_reindex_shared_dyn_local_2[0]
                for ax0_ax1_fused_0 in range(4):
                    B_reindex_shared_dyn_2[(ax2_0_0 + 1) % 2 * 8192 + ax0_ax1_fused_0 * 2048 + threadIdx_y * 256 + threadIdx_x // 8 * 64 + T.bitwise_xor(threadIdx_x % 8, ax0_ax1_fused_0 % 2 * 4 + threadIdx_y // 2) * 8:(ax2_0_0 + 1) % 2 * 8192 + ax0_ax1_fused_0 * 2048 + threadIdx_y * 256 + threadIdx_x // 8 * 64 + T.bitwise_xor(threadIdx_x % 8, ax0_ax1_fused_0 % 2 * 4 + threadIdx_y // 2) * 8 + 8] = B_reindex_shared_dyn_local_2[ax0_ax1_fused_0 * 65]
                for ax0_0 in range(2):
                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, (ax2_0_0 + 1) % 2 * 2048 + threadIdx_y // 4 * 1024 + ax0_0 * 512, 512, 1), threadIdx_x * 16)
                for ax1_0 in range(4):
                    T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax1_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, (ax2_0_0 + 1) % 2 * 8192, 4096, 1), threadIdx_x % 8 * 512 + threadIdx_y % 4 * 128 + ax1_0 // 2 * 64 + T.bitwise_xor(ax1_0 % 2 * 4 + threadIdx_x // 8, threadIdx_x % 8) * 8)
                for ax0_0_4, ax1_0_4 in T.grid(4, 16):
                    cse_var_2: T.int32 = ax1_0_4 * 2
                    T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_4 * 4 + 16, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_2 + 32, Y_reindex_m16n8k8_matrixC, ax0_0_4 * 32 + cse_var_2, T.bool(False))
            for ax0_0 in range(2):
                T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8 + 16, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y // 4 * 1024 + ax0_0 * 512 + 2056, 512, 1), threadIdx_x * 16)
            for ax1_0 in range(4):
                T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax1_0 * 8 + 32, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, 8192, 4096, 1), threadIdx_x % 8 * 512 + threadIdx_y % 4 * 128 + ax1_0 // 2 * 64 + T.bitwise_xor(ax1_0 % 2 * 4 + threadIdx_x // 8, threadIdx_x % 8) * 8 + 4096)
            for ax0_0_4, ax1_0_4 in T.grid(4, 16):
                cse_var_3: T.int32 = ax1_0_4 * 2
                T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_4 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_3, Y_reindex_m16n8k8_matrixC, ax0_0_4 * 32 + cse_var_3, T.bool(False))
            for ax0_0_4, ax1_0_4 in T.grid(4, 16):
                cse_var_4: T.int32 = ax1_0_4 * 2
                T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_4 * 4 + 16, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_4 + 32, Y_reindex_m16n8k8_matrixC, ax0_0_4 * 32 + cse_var_4, T.bool(False))
        Y_reindex_m16n8k8_matrixC_shared_dyn = T.decl_buffer((8192,), "float16", scope="shared.dyn")
        for ax0_0 in range(8):
            B_reindex_shared_dyn_1 = T.Buffer((8192,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            for ax1_0 in range(16):
                B_reindex_shared_dyn_1[threadIdx_y * 1024 + ax1_0 * 64 + threadIdx_x * 2:threadIdx_y * 1024 + ax1_0 * 64 + threadIdx_x * 2 + 2] = Y_reindex_m16n8k8_matrixC_2[ax0_0 // 2 * 32 + ax1_0 * 2 + ax0_0 % 2]
            for ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 in range(32):
                Y_1 = T.Buffer((67108864,), "float16", data=Y.data)
                Y_1[blockIdx_x // 4 * 4194304 + blockIdx_y // 4 * 1048576 + ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 // 16 * 524288 + ax0_0 * 65536 + threadIdx_y % 2 * 32768 + threadIdx_x // 8 * 8192 + blockIdx_x % 4 * 2048 + blockIdx_y % 4 * 512 + ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 % 16 * 32 + threadIdx_y // 2 * 8 + threadIdx_x % 8] = B_reindex_shared_dyn_1[ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 * 256 + threadIdx_y * 32 + threadIdx_x]
