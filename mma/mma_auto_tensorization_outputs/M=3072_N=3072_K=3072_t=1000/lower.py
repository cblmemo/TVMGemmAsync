# from tvm.script import ir as I
# from tvm.script import tir as T

@I.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer((3072, 3072), "float16"), B: T.Buffer((3072, 3072), "float16"), Y: T.Buffer((3072, 3072), "float16")):
        T.func_attr({"global_symbol": "main", "tir.noalias": T.bool(True)})
        blockIdx_x = T.launch_thread("blockIdx.x", 6)
        Y_reindex_m16n8k8_matrixC = T.allocate([96], "float16x2", "local")
        A_reindex_shared_dyn = T.allocate([9216], "float16", "shared.dyn")
        B_reindex_shared_dyn = T.allocate([6144], "float16", "shared.dyn")
        A_reindex_shared_dyn_m16n8k8_matrixA = T.allocate([96], "float16", "local")
        B_reindex_shared_dyn_m16n8k8_matrixB = T.allocate([16], "float16", "local")
        blockIdx_y = T.launch_thread("blockIdx.y", 64)
        threadIdx_y = T.launch_thread("threadIdx.y", 4)
        threadIdx_x = T.launch_thread("threadIdx.x", 32)
        Y_reindex_m16n8k8_matrixC_1 = T.decl_buffer((192,), "float16", scope="local")
        Y_reindex_m16n8k8_matrixC_2 = T.Buffer((96,), "float16x2", data=Y_reindex_m16n8k8_matrixC, scope="local")
        for ax0_0_3_init, ax1_0_3_init, b in T.grid(12, 4, 2):
            Y_reindex_m16n8k8_matrixC_2[ax0_0_3_init * 8 + ax1_0_3_init * 2 + b] = T.Broadcast(T.float16(0), 2)
        with T.decl_buffer((9216,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn") as A_reindex_shared_dyn_1:
            B_reindex_shared_dyn_1 = T.decl_buffer((6144,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            A_reindex_shared_dyn_m16n8k8_matrixA_1 = T.decl_buffer((96,), "float16", data=A_reindex_shared_dyn_m16n8k8_matrixA, scope="local")
            B_reindex_shared_dyn_m16n8k8_matrixB_1 = T.decl_buffer((16,), "float16", data=B_reindex_shared_dyn_m16n8k8_matrixB, scope="local")
            A_reindex_shared_dyn_2 = T.Buffer((9216,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
            A_1 = T.Buffer((9437184,), "float16", data=A.data)
            B_reindex_shared_dyn_2 = T.Buffer((6144,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            B_1 = T.Buffer((9437184,), "float16", data=B.data)
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    for ax0_ax1_fused_0 in range(3):
                        A_reindex_shared_dyn_2[ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x * 8:ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = A_1[blockIdx_y // 4 * 589824 + ax0_ax1_fused_0 * 196608 + threadIdx_y * 49152 + threadIdx_x // 2 * 3072 + threadIdx_x % 2 * 8:blockIdx_y // 4 * 589824 + ax0_ax1_fused_0 * 196608 + threadIdx_y * 49152 + threadIdx_x // 2 * 3072 + threadIdx_x % 2 * 8 + 8]
                T.attr(0, "async_scope", 1)
                for ax0_ax1_fused_0 in range(2):
                    B_reindex_shared_dyn_2[ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x * 8:ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = B_1[ax0_ax1_fused_0 * 24576 + threadIdx_y * 6144 + threadIdx_x // 16 * 3072 + blockIdx_x * 512 + blockIdx_y % 4 * 128 + threadIdx_x % 16 * 8:ax0_ax1_fused_0 * 24576 + threadIdx_y * 6144 + threadIdx_x // 16 * 3072 + blockIdx_x * 512 + blockIdx_y % 4 * 128 + threadIdx_x % 16 * 8 + 8]
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    for ax0_ax1_fused_0 in range(3):
                        A_reindex_shared_dyn_2[ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x * 8 + 3072:ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x * 8 + 3072 + 8] = A_1[blockIdx_y // 4 * 589824 + ax0_ax1_fused_0 * 196608 + threadIdx_y * 49152 + threadIdx_x // 2 * 3072 + threadIdx_x % 2 * 8 + 16:blockIdx_y // 4 * 589824 + ax0_ax1_fused_0 * 196608 + threadIdx_y * 49152 + threadIdx_x // 2 * 3072 + threadIdx_x % 2 * 8 + 16 + 8]
                T.attr(0, "async_scope", 1)
                for ax0_ax1_fused_0 in range(2):
                    B_reindex_shared_dyn_2[ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x * 8 + 2048:ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x * 8 + 2048 + 8] = B_1[ax0_ax1_fused_0 * 24576 + threadIdx_y * 6144 + threadIdx_x // 16 * 3072 + blockIdx_x * 512 + blockIdx_y % 4 * 128 + threadIdx_x % 16 * 8 + 49152:ax0_ax1_fused_0 * 24576 + threadIdx_y * 6144 + threadIdx_x // 16 * 3072 + blockIdx_x * 512 + blockIdx_y % 4 * 128 + threadIdx_x % 16 * 8 + 49152 + 8]
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 1)
                for ax0_0 in range(6):
                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax0_0 * 512, 512, 1), threadIdx_x * 16)
                T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, 0, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, threadIdx_y * 32, 1024, 1), threadIdx_x % 8 * 128 + threadIdx_x // 8 * 8)
            for ax2_0_0 in range(190):
                with T.attr(0, "async_commit_queue_scope", 0):
                    with T.attr(0, "async_scope", 1):
                        for ax0_ax1_fused_0 in range(3):
                            A_reindex_shared_dyn_2[(ax2_0_0 + 2) % 3 * 3072 + ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x * 8:(ax2_0_0 + 2) % 3 * 3072 + ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = A_1[blockIdx_y // 4 * 589824 + ax0_ax1_fused_0 * 196608 + threadIdx_y * 49152 + threadIdx_x // 2 * 3072 + ax2_0_0 * 16 + threadIdx_x % 2 * 8 + 32:blockIdx_y // 4 * 589824 + ax0_ax1_fused_0 * 196608 + threadIdx_y * 49152 + threadIdx_x // 2 * 3072 + ax2_0_0 * 16 + threadIdx_x % 2 * 8 + 32 + 8]
                    T.attr(0, "async_scope", 1)
                    for ax0_ax1_fused_0 in range(2):
                        B_reindex_shared_dyn_2[(ax2_0_0 + 2) % 3 * 2048 + ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x * 8:(ax2_0_0 + 2) % 3 * 2048 + ax0_ax1_fused_0 * 1024 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = B_1[ax2_0_0 * 49152 + ax0_ax1_fused_0 * 24576 + threadIdx_y * 6144 + threadIdx_x // 16 * 3072 + blockIdx_x * 512 + blockIdx_y % 4 * 128 + threadIdx_x % 16 * 8 + 98304:ax2_0_0 * 49152 + ax0_ax1_fused_0 * 24576 + threadIdx_y * 6144 + threadIdx_x // 16 * 3072 + blockIdx_x * 512 + blockIdx_y % 4 * 128 + threadIdx_x % 16 * 8 + 98304 + 8]
                with T.attr(0, "async_wait_queue_scope", 0):
                    T.attr(0, "async_wait_inflight_count", 1)
                    for ax0_0 in range(6):
                        T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8 + 48, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax2_0_0 % 3 * 3072 + ax0_0 * 512 + 8, 512, 1), threadIdx_x * 16)
                    T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax2_0_0 % 3 * 2048 + threadIdx_y * 32 + 1024, 1024, 1), threadIdx_x % 8 * 128 + threadIdx_x // 8 * 8)
                    for ax0_0_3, ax1_0_3 in T.grid(12, 4):
                        cse_var_1: T.int32 = ax1_0_3 * 2
                        T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_1, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 8 + cse_var_1, T.bool(False))
                for ax0_0 in range(6):
                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, (ax2_0_0 + 1) % 3 * 3072 + ax0_0 * 512, 512, 1), threadIdx_x * 16)
                T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, 0, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, (ax2_0_0 + 1) % 3 * 2048 + threadIdx_y * 32, 1024, 1), threadIdx_x % 8 * 128 + threadIdx_x // 8 * 8)
                for ax0_0_3, ax1_0_3 in T.grid(12, 4):
                    cse_var_2: T.int32 = ax1_0_3 * 2
                    T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 * 4 + 48, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_2 + 8, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 8 + cse_var_2, T.bool(False))
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 0)
                for ax0_0 in range(6):
                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8 + 48, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax0_0 * 512 + 3080, 512, 1), threadIdx_x * 16)
                T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, threadIdx_y * 32 + 3072, 1024, 1), threadIdx_x % 8 * 128 + threadIdx_x // 8 * 8)
                for ax0_0_3, ax1_0_3 in T.grid(12, 4):
                    cse_var_3: T.int32 = ax1_0_3 * 2
                    T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_3, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 8 + cse_var_3, T.bool(False))
            for ax0_0 in range(6):
                T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax0_0 * 512 + 6144, 512, 1), threadIdx_x * 16)
            T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, 0, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, threadIdx_y * 32 + 4096, 1024, 1), threadIdx_x % 8 * 128 + threadIdx_x // 8 * 8)
            for ax0_0_3, ax1_0_3 in T.grid(12, 4):
                cse_var_4: T.int32 = ax1_0_3 * 2
                T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 * 4 + 48, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_4 + 8, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 8 + cse_var_4, T.bool(False))
            for ax0_0 in range(6):
                T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8 + 48, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax0_0 * 512 + 6152, 512, 1), threadIdx_x * 16)
            T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, threadIdx_y * 32 + 5120, 1024, 1), threadIdx_x % 8 * 128 + threadIdx_x // 8 * 8)
            for ax0_0_3, ax1_0_3 in T.grid(12, 4):
                cse_var_5: T.int32 = ax1_0_3 * 2
                T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_5, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 8 + cse_var_5, T.bool(False))
            for ax0_0_3, ax1_0_3 in T.grid(12, 4):
                cse_var_6: T.int32 = ax1_0_3 * 2
                T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 * 4 + 48, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_6 + 8, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 8 + cse_var_6, T.bool(False))
        Y_reindex_m16n8k8_matrixC_shared_dyn = T.decl_buffer((1024,), "float16", scope="shared.dyn")
        for ax0_0 in range(24):
            B_reindex_shared_dyn_1 = T.Buffer((1024,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            for ax1_0 in range(4):
                B_reindex_shared_dyn_1[threadIdx_y * 256 + ax1_0 * 64 + threadIdx_x * 2:threadIdx_y * 256 + ax1_0 * 64 + threadIdx_x * 2 + 2] = Y_reindex_m16n8k8_matrixC_2[ax0_0 // 2 * 8 + ax1_0 * 2 + ax0_0 % 2]
            for ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 in range(8):
                Y_1 = T.Buffer((9437184,), "float16", data=Y.data)
                Y_1[blockIdx_y // 4 * 589824 + ax0_0 * 24576 + threadIdx_y % 2 * 12288 + threadIdx_x // 8 * 3072 + blockIdx_x * 512 + blockIdx_y % 4 * 128 + ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 * 16 + threadIdx_y // 2 * 8 + threadIdx_x % 8] = B_reindex_shared_dyn_1[ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 * 128 + threadIdx_y * 32 + threadIdx_x]
