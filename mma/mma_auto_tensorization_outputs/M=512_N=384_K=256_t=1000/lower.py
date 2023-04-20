# from tvm.script import ir as I
# from tvm.script import tir as T

@I.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer((512, 256), "float16"), B: T.Buffer((256, 384), "float16"), Y: T.Buffer((512, 384), "float16")):
        T.func_attr({"global_symbol": "main", "tir.noalias": T.bool(True)})
        blockIdx_x = T.launch_thread("blockIdx.x", 8)
        Y_reindex_m16n8k8_matrixC = T.allocate([32], "float16x2", "local")
        A_reindex_shared_dyn = T.allocate([12288], "float16", "shared.dyn")
        B_reindex_shared_dyn = T.allocate([3072], "float16", "shared.dyn")
        A_reindex_shared_dyn_m16n8k8_matrixA = T.allocate([64], "float16", "local")
        B_reindex_shared_dyn_m16n8k8_matrixB = T.allocate([32], "float16", "local")
        blockIdx_y = T.launch_thread("blockIdx.y", 6)
        threadIdx_y = T.launch_thread("threadIdx.y", 2)
        threadIdx_x = T.launch_thread("threadIdx.x", 32)
        Y_reindex_m16n8k8_matrixC_1 = T.decl_buffer((64,), "float16", scope="local")
        Y_reindex_m16n8k8_matrixC_2 = T.Buffer((32,), "float16x2", data=Y_reindex_m16n8k8_matrixC, scope="local")
        for ax0_0_3_init, ax1_0_3_init, b in T.grid(4, 4, 2):
            Y_reindex_m16n8k8_matrixC_2[ax0_0_3_init * 8 + ax1_0_3_init * 2 + b] = T.Broadcast(T.float16(0), 2)
        with T.decl_buffer((12288,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn") as A_reindex_shared_dyn_1:
            B_reindex_shared_dyn_1 = T.decl_buffer((3072,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            A_reindex_shared_dyn_m16n8k8_matrixA_1 = T.decl_buffer((64,), "float16", data=A_reindex_shared_dyn_m16n8k8_matrixA, scope="local")
            B_reindex_shared_dyn_m16n8k8_matrixB_1 = T.decl_buffer((32,), "float16", data=B_reindex_shared_dyn_m16n8k8_matrixB, scope="local")
            A_reindex_shared_dyn_2 = T.Buffer((12288,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
            A_1 = T.Buffer((131072,), "float16", data=A.data)
            B_reindex_shared_dyn_2 = T.Buffer((3072,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            B_1 = T.Buffer((98304,), "float16", data=B.data)
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    for ax0_ax1_fused_0 in range(8):
                        A_reindex_shared_dyn_2[ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8:ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = A_1[blockIdx_x // 4 * 65536 + blockIdx_y // 3 * 32768 + ax0_ax1_fused_0 * 4096 + threadIdx_y * 2048 + threadIdx_x // 4 * 256 + threadIdx_x % 4 * 8:blockIdx_x // 4 * 65536 + blockIdx_y // 3 * 32768 + ax0_ax1_fused_0 * 4096 + threadIdx_y * 2048 + threadIdx_x // 4 * 256 + threadIdx_x % 4 * 8 + 8]
                T.attr(0, "async_scope", 1)
                for ax0_ax1_fused_0 in range(2):
                    B_reindex_shared_dyn_2[ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8:ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = B_1[ax0_ax1_fused_0 * 6144 + threadIdx_y * 3072 + threadIdx_x // 4 * 384 + blockIdx_x % 4 * 96 + blockIdx_y % 3 * 32 + threadIdx_x % 4 * 8:ax0_ax1_fused_0 * 6144 + threadIdx_y * 3072 + threadIdx_x // 4 * 384 + blockIdx_x % 4 * 96 + blockIdx_y % 3 * 32 + threadIdx_x % 4 * 8 + 8]
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    for ax0_ax1_fused_0 in range(8):
                        A_reindex_shared_dyn_2[ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 4096:ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 4096 + 8] = A_1[blockIdx_x // 4 * 65536 + blockIdx_y // 3 * 32768 + ax0_ax1_fused_0 * 4096 + threadIdx_y * 2048 + threadIdx_x // 4 * 256 + threadIdx_x % 4 * 8 + 32:blockIdx_x // 4 * 65536 + blockIdx_y // 3 * 32768 + ax0_ax1_fused_0 * 4096 + threadIdx_y * 2048 + threadIdx_x // 4 * 256 + threadIdx_x % 4 * 8 + 32 + 8]
                T.attr(0, "async_scope", 1)
                for ax0_ax1_fused_0 in range(2):
                    B_reindex_shared_dyn_2[ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 1024:ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 1024 + 8] = B_1[ax0_ax1_fused_0 * 6144 + threadIdx_y * 3072 + threadIdx_x // 4 * 384 + blockIdx_x % 4 * 96 + blockIdx_y % 3 * 32 + threadIdx_x % 4 * 8 + 12288:ax0_ax1_fused_0 * 6144 + threadIdx_y * 3072 + threadIdx_x // 4 * 384 + blockIdx_x % 4 * 96 + blockIdx_y % 3 * 32 + threadIdx_x % 4 * 8 + 12288 + 8]
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 1)
                for ax0_0, ax1_0 in T.grid(2, 2):
                    cse_var_1: T.int32 = ax1_0 * 8
                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 16 + cse_var_1, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 2048 + ax0_0 * 1024 + cse_var_1, 1024, 1), threadIdx_x * 32)
                for ax0_0 in range(2):
                    T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax0_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax0_0 * 256, 256, 1), threadIdx_x % 8 * 32 + threadIdx_x // 8 * 8)
            for ax2_0_0 in range(6):
                with T.attr(0, "async_commit_queue_scope", 0):
                    with T.attr(0, "async_scope", 1):
                        for ax0_ax1_fused_0 in range(8):
                            A_reindex_shared_dyn_2[(ax2_0_0 + 2) % 3 * 4096 + ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8:(ax2_0_0 + 2) % 3 * 4096 + ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = A_1[blockIdx_x // 4 * 65536 + blockIdx_y // 3 * 32768 + ax0_ax1_fused_0 * 4096 + threadIdx_y * 2048 + threadIdx_x // 4 * 256 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 64:blockIdx_x // 4 * 65536 + blockIdx_y // 3 * 32768 + ax0_ax1_fused_0 * 4096 + threadIdx_y * 2048 + threadIdx_x // 4 * 256 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 64 + 8]
                    T.attr(0, "async_scope", 1)
                    for ax0_ax1_fused_0 in range(2):
                        B_reindex_shared_dyn_2[(ax2_0_0 + 2) % 3 * 1024 + ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8:(ax2_0_0 + 2) % 3 * 1024 + ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = B_1[ax2_0_0 * 12288 + ax0_ax1_fused_0 * 6144 + threadIdx_y * 3072 + threadIdx_x // 4 * 384 + blockIdx_x % 4 * 96 + blockIdx_y % 3 * 32 + threadIdx_x % 4 * 8 + 24576:ax2_0_0 * 12288 + ax0_ax1_fused_0 * 6144 + threadIdx_y * 3072 + threadIdx_x // 4 * 384 + blockIdx_x % 4 * 96 + blockIdx_y % 3 * 32 + threadIdx_x % 4 * 8 + 24576 + 8]
                with T.attr(0, "async_wait_queue_scope", 0):
                    T.attr(0, "async_wait_inflight_count", 1)
                    for ax0_0, ax1_0 in T.grid(2, 2):
                        cse_var_2: T.int32 = ax1_0 * 8
                        T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 16 + cse_var_2 + 32, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax2_0_0 % 3 * 4096 + threadIdx_y * 2048 + ax0_0 * 1024 + cse_var_2 + 16, 1024, 1), threadIdx_x * 32)
                    for ax0_0 in range(2):
                        T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax0_0 * 8 + 16, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax2_0_0 % 3 * 1024 + ax0_0 * 256 + 512, 256, 1), threadIdx_x % 8 * 32 + threadIdx_x // 8 * 8)
                    for ax0_0_3, ax1_0_3, ax2_0_2 in T.grid(4, 4, 2):
                        cse_var_4: T.int32 = ax1_0_3 * 2
                        cse_var_3: T.int32 = ax2_0_2 * 8
                        T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 // 2 * 16 + cse_var_3 + ax0_0_3 % 2 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_3 + cse_var_4, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 8 + cse_var_4, T.bool(False))
                for ax0_0, ax1_0 in T.grid(2, 2):
                    cse_var_5: T.int32 = ax1_0 * 8
                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 16 + cse_var_5, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, (ax2_0_0 + 1) % 3 * 4096 + threadIdx_y * 2048 + ax0_0 * 1024 + cse_var_5, 1024, 1), threadIdx_x * 32)
                for ax0_0 in range(2):
                    T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax0_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, (ax2_0_0 + 1) % 3 * 1024 + ax0_0 * 256, 256, 1), threadIdx_x % 8 * 32 + threadIdx_x // 8 * 8)
                for ax0_0_3, ax1_0_3, ax2_0_2 in T.grid(4, 4, 2):
                    cse_var_7: T.int32 = ax1_0_3 * 2
                    cse_var_6: T.int32 = ax2_0_2 * 8
                    T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 // 2 * 16 + cse_var_6 + ax0_0_3 % 2 * 4 + 32, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_6 + cse_var_7 + 16, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 8 + cse_var_7, T.bool(False))
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 0)
                for ax0_0, ax1_0 in T.grid(2, 2):
                    cse_var_8: T.int32 = ax1_0 * 8
                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 16 + cse_var_8 + 32, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 2048 + ax0_0 * 1024 + cse_var_8 + 16, 1024, 1), threadIdx_x * 32)
                for ax0_0 in range(2):
                    T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax0_0 * 8 + 16, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax0_0 * 256 + 512, 256, 1), threadIdx_x % 8 * 32 + threadIdx_x // 8 * 8)
                for ax0_0_3, ax1_0_3, ax2_0_2 in T.grid(4, 4, 2):
                    cse_var_10: T.int32 = ax1_0_3 * 2
                    cse_var_9: T.int32 = ax2_0_2 * 8
                    T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 // 2 * 16 + cse_var_9 + ax0_0_3 % 2 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_9 + cse_var_10, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 8 + cse_var_10, T.bool(False))
            for ax0_0, ax1_0 in T.grid(2, 2):
                cse_var_11: T.int32 = ax1_0 * 8
                T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 16 + cse_var_11, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 2048 + ax0_0 * 1024 + cse_var_11 + 4096, 1024, 1), threadIdx_x * 32)
            for ax0_0 in range(2):
                T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax0_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax0_0 * 256 + 1024, 256, 1), threadIdx_x % 8 * 32 + threadIdx_x // 8 * 8)
            for ax0_0_3, ax1_0_3, ax2_0_2 in T.grid(4, 4, 2):
                cse_var_13: T.int32 = ax1_0_3 * 2
                cse_var_12: T.int32 = ax2_0_2 * 8
                T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 // 2 * 16 + cse_var_12 + ax0_0_3 % 2 * 4 + 32, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_12 + cse_var_13 + 16, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 8 + cse_var_13, T.bool(False))
            for ax0_0, ax1_0 in T.grid(2, 2):
                cse_var_14: T.int32 = ax1_0 * 8
                T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 16 + cse_var_14 + 32, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 2048 + ax0_0 * 1024 + cse_var_14 + 4112, 1024, 1), threadIdx_x * 32)
            for ax0_0 in range(2):
                T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax0_0 * 8 + 16, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax0_0 * 256 + 1536, 256, 1), threadIdx_x % 8 * 32 + threadIdx_x // 8 * 8)
            for ax0_0_3, ax1_0_3, ax2_0_2 in T.grid(4, 4, 2):
                cse_var_16: T.int32 = ax1_0_3 * 2
                cse_var_15: T.int32 = ax2_0_2 * 8
                T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 // 2 * 16 + cse_var_15 + ax0_0_3 % 2 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_15 + cse_var_16, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 8 + cse_var_16, T.bool(False))
            for ax0_0_3, ax1_0_3, ax2_0_2 in T.grid(4, 4, 2):
                cse_var_18: T.int32 = ax1_0_3 * 2
                cse_var_17: T.int32 = ax2_0_2 * 8
                T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 // 2 * 16 + cse_var_17 + ax0_0_3 % 2 * 4 + 32, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_17 + cse_var_18 + 16, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 8 + cse_var_18, T.bool(False))
        Y_reindex_m16n8k8_matrixC_shared_dyn = T.decl_buffer((512,), "float16", scope="shared.dyn")
        for ax0_0 in range(8):
            B_reindex_shared_dyn_1 = T.Buffer((512,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            for ax1_0 in range(4):
                B_reindex_shared_dyn_1[threadIdx_y * 256 + ax1_0 * 64 + threadIdx_x * 2:threadIdx_y * 256 + ax1_0 * 64 + threadIdx_x * 2 + 2] = Y_reindex_m16n8k8_matrixC_2[ax0_0 // 2 * 8 + ax1_0 * 2 + ax0_0 % 2]
            for ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 in range(8):
                Y_1 = T.Buffer((196608,), "float16", data=Y.data)
                Y_1[blockIdx_x // 4 * 98304 + blockIdx_y // 3 * 49152 + ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 // 4 * 24576 + ax0_0 * 3072 + threadIdx_y * 1536 + threadIdx_x // 8 * 384 + blockIdx_x % 4 * 96 + blockIdx_y % 3 * 32 + ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 % 4 * 8 + threadIdx_x % 8] = B_reindex_shared_dyn_1[ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 * 64 + threadIdx_y * 32 + threadIdx_x]
