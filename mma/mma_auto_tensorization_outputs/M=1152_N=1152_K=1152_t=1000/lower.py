# from tvm.script import ir as I
# from tvm.script import tir as T

@I.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer((1152, 1152), "float16"), B: T.Buffer((1152, 1152), "float16"), Y: T.Buffer((1152, 1152), "float16")):
        T.func_attr({"global_symbol": "main", "tir.noalias": T.bool(True)})
        blockIdx_x = T.launch_thread("blockIdx.x", 9)
        Y_reindex_m16n8k8_matrixC = T.allocate([96], "float16x2", "local")
        A_reindex_shared_dyn = T.allocate([12288], "float16", "shared.dyn")
        B_reindex_shared_dyn = T.allocate([9216], "float16", "shared.dyn")
        A_reindex_shared_dyn_m16n8k8_matrixA = T.allocate([32], "float16", "local")
        B_reindex_shared_dyn_m16n8k8_matrixB = T.allocate([48], "float16", "local")
        blockIdx_y = T.launch_thread("blockIdx.y", 12)
        threadIdx_y = T.launch_thread("threadIdx.y", 2)
        threadIdx_x = T.launch_thread("threadIdx.x", 32)
        Y_reindex_m16n8k8_matrixC_1 = T.decl_buffer((192,), "float16", scope="local")
        Y_reindex_m16n8k8_matrixC_2 = T.Buffer((96,), "float16x2", data=Y_reindex_m16n8k8_matrixC, scope="local")
        for ax0_0_3_init, ax1_0_3_init, ax1_0_4_init, b in T.grid(4, 4, 3, 2):
            Y_reindex_m16n8k8_matrixC_2[ax0_0_3_init * 24 + ax1_0_3_init * 6 + ax1_0_4_init * 2 + b] = T.Broadcast(T.float16(0), 2)
        with T.decl_buffer((12288,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn") as A_reindex_shared_dyn_1:
            B_reindex_shared_dyn_1 = T.decl_buffer((9216,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            A_reindex_shared_dyn_m16n8k8_matrixA_1 = T.decl_buffer((32,), "float16", data=A_reindex_shared_dyn_m16n8k8_matrixA, scope="local")
            B_reindex_shared_dyn_m16n8k8_matrixB_1 = T.decl_buffer((48,), "float16", data=B_reindex_shared_dyn_m16n8k8_matrixB, scope="local")
            A_reindex_shared_dyn_2 = T.Buffer((12288,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
            A_1 = T.Buffer((1327104,), "float16", data=A.data)
            B_reindex_shared_dyn_2 = T.Buffer((9216,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            B_1 = T.Buffer((1327104,), "float16", data=B.data)
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    for ax0_ax1_fused_0 in range(8):
                        A_reindex_shared_dyn_2[ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8:ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = A_1[blockIdx_x * 147456 + ax0_ax1_fused_0 * 18432 + threadIdx_y * 9216 + threadIdx_x // 4 * 1152 + threadIdx_x % 4 * 8:blockIdx_x * 147456 + ax0_ax1_fused_0 * 18432 + threadIdx_y * 9216 + threadIdx_x // 4 * 1152 + threadIdx_x % 4 * 8 + 8]
                T.attr(0, "async_scope", 1)
                for ax0_ax1_fused_0 in range(6):
                    B_reindex_shared_dyn_2[ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8:ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = B_1[(ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8) // 96 * 1152 + blockIdx_y * 96 + (ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8) % 96:(ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8) // 96 * 1152 + blockIdx_y * 96 + (ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8) % 96 + 8]
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    for ax0_ax1_fused_0 in range(8):
                        A_reindex_shared_dyn_2[ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 4096:ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 4096 + 8] = A_1[blockIdx_x * 147456 + ax0_ax1_fused_0 * 18432 + threadIdx_y * 9216 + threadIdx_x // 4 * 1152 + threadIdx_x % 4 * 8 + 32:blockIdx_x * 147456 + ax0_ax1_fused_0 * 18432 + threadIdx_y * 9216 + threadIdx_x // 4 * 1152 + threadIdx_x % 4 * 8 + 32 + 8]
                T.attr(0, "async_scope", 1)
                for ax0_ax1_fused_0 in range(6):
                    B_reindex_shared_dyn_2[ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 3072:ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 3072 + 8] = B_1[(ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8) // 96 * 1152 + blockIdx_y * 96 + (ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8) % 96 + 36864:(ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8) // 96 * 1152 + blockIdx_y * 96 + (ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8) % 96 + 36864 + 8]
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 1)
                for ax0_0 in range(2):
                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 2048 + ax0_0 * 1024, 1024, 1), threadIdx_x * 32)
                for ax1_0 in range(3):
                    T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax1_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax1_0 * 32, 768, 1), threadIdx_x % 8 * 96 + threadIdx_x // 8 * 8)
            for ax2_0_0 in range(34):
                with T.attr(0, "async_commit_queue_scope", 0):
                    with T.attr(0, "async_scope", 1):
                        for ax0_ax1_fused_0 in range(8):
                            A_reindex_shared_dyn_2[(ax2_0_0 + 2) % 3 * 4096 + ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8:(ax2_0_0 + 2) % 3 * 4096 + ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = A_1[blockIdx_x * 147456 + ax0_ax1_fused_0 * 18432 + threadIdx_y * 9216 + threadIdx_x // 4 * 1152 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 64:blockIdx_x * 147456 + ax0_ax1_fused_0 * 18432 + threadIdx_y * 9216 + threadIdx_x // 4 * 1152 + ax2_0_0 * 32 + threadIdx_x % 4 * 8 + 64 + 8]
                    T.attr(0, "async_scope", 1)
                    for ax0_ax1_fused_0 in range(6):
                        cse_var_1: T.int32 = ax0_ax1_fused_0 * 512
                        B_reindex_shared_dyn_2[(ax2_0_0 + 2) % 3 * 3072 + cse_var_1 + threadIdx_y * 256 + threadIdx_x * 8:(ax2_0_0 + 2) % 3 * 3072 + cse_var_1 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = B_1[ax2_0_0 * 36864 + (cse_var_1 + threadIdx_y * 256 + threadIdx_x * 8) // 96 * 1152 + blockIdx_y * 96 + (cse_var_1 + threadIdx_y * 256 + threadIdx_x * 8) % 96 + 73728:ax2_0_0 * 36864 + (cse_var_1 + threadIdx_y * 256 + threadIdx_x * 8) // 96 * 1152 + blockIdx_y * 96 + (cse_var_1 + threadIdx_y * 256 + threadIdx_x * 8) % 96 + 73728 + 8]
                with T.attr(0, "async_wait_queue_scope", 0):
                    T.attr(0, "async_wait_inflight_count", 1)
                    for ax2_0_1 in range(3):
                        for ax0_0 in range(2):
                            T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, (ax2_0_1 + 1) % 2 * 16 + ax0_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax2_0_0 % 3 * 4096 + threadIdx_y * 2048 + ax0_0 * 1024 + ax2_0_1 * 8 + 8, 1024, 1), threadIdx_x * 32)
                        for ax1_0 in range(3):
                            T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, (ax2_0_1 + 1) % 2 * 24 + ax1_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax2_0_0 % 3 * 3072 + ax2_0_1 * 768 + ax1_0 * 32 + 768, 768, 1), threadIdx_x % 8 * 96 + threadIdx_x // 8 * 8)
                        for ax0_0_3, ax1_0_3, ax1_0_4 in T.grid(4, 4, 3):
                            cse_var_4: T.int32 = ax2_0_1 % 2
                            cse_var_3: T.int32 = ax1_0_3 * 6
                            cse_var_2: T.int32 = ax1_0_4 * 2
                            T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, cse_var_4 * 16 + ax0_0_3 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_4 * 24 + cse_var_3 + cse_var_2, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 24 + cse_var_3 + cse_var_2, T.bool(False))
                for ax0_0 in range(2):
                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, (ax2_0_0 + 1) % 3 * 4096 + threadIdx_y * 2048 + ax0_0 * 1024, 1024, 1), threadIdx_x * 32)
                for ax1_0 in range(3):
                    T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax1_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, (ax2_0_0 + 1) % 3 * 3072 + ax1_0 * 32, 768, 1), threadIdx_x % 8 * 96 + threadIdx_x // 8 * 8)
                for ax0_0_3, ax1_0_3, ax1_0_4 in T.grid(4, 4, 3):
                    cse_var_6: T.int32 = ax1_0_3 * 6
                    cse_var_5: T.int32 = ax1_0_4 * 2
                    T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 * 4 + 16, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_6 + cse_var_5 + 24, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 24 + cse_var_6 + cse_var_5, T.bool(False))
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 0)
                for ax2_0_1 in range(3):
                    for ax0_0 in range(2):
                        T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, (ax2_0_1 + 1) % 2 * 16 + ax0_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 2048 + ax0_0 * 1024 + ax2_0_1 * 8 + 4104, 1024, 1), threadIdx_x * 32)
                    for ax1_0 in range(3):
                        T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, (ax2_0_1 + 1) % 2 * 24 + ax1_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax2_0_1 * 768 + ax1_0 * 32 + 3840, 768, 1), threadIdx_x % 8 * 96 + threadIdx_x // 8 * 8)
                    for ax0_0_3, ax1_0_3, ax1_0_4 in T.grid(4, 4, 3):
                        cse_var_9: T.int32 = ax2_0_1 % 2
                        cse_var_8: T.int32 = ax1_0_3 * 6
                        cse_var_7: T.int32 = ax1_0_4 * 2
                        T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, cse_var_9 * 16 + ax0_0_3 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_9 * 24 + cse_var_8 + cse_var_7, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 24 + cse_var_8 + cse_var_7, T.bool(False))
            for ax0_0 in range(2):
                T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 2048 + ax0_0 * 1024 + 8192, 1024, 1), threadIdx_x * 32)
            for ax1_0 in range(3):
                T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax1_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax1_0 * 32 + 6144, 768, 1), threadIdx_x % 8 * 96 + threadIdx_x // 8 * 8)
            for ax0_0_3, ax1_0_3, ax1_0_4 in T.grid(4, 4, 3):
                cse_var_11: T.int32 = ax1_0_3 * 6
                cse_var_10: T.int32 = ax1_0_4 * 2
                T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 * 4 + 16, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_11 + cse_var_10 + 24, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 24 + cse_var_11 + cse_var_10, T.bool(False))
            for ax2_0_1 in range(3):
                for ax0_0 in range(2):
                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, (ax2_0_1 + 1) % 2 * 16 + ax0_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 2048 + ax0_0 * 1024 + ax2_0_1 * 8 + 8200, 1024, 1), threadIdx_x * 32)
                for ax1_0 in range(3):
                    T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, (ax2_0_1 + 1) % 2 * 24 + ax1_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax2_0_1 * 768 + ax1_0 * 32 + 6912, 768, 1), threadIdx_x % 8 * 96 + threadIdx_x // 8 * 8)
                for ax0_0_3, ax1_0_3, ax1_0_4 in T.grid(4, 4, 3):
                    cse_var_14: T.int32 = ax2_0_1 % 2
                    cse_var_13: T.int32 = ax1_0_3 * 6
                    cse_var_12: T.int32 = ax1_0_4 * 2
                    T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, cse_var_14 * 16 + ax0_0_3 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_14 * 24 + cse_var_13 + cse_var_12, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 24 + cse_var_13 + cse_var_12, T.bool(False))
            for ax0_0_3, ax1_0_3, ax1_0_4 in T.grid(4, 4, 3):
                cse_var_16: T.int32 = ax1_0_3 * 6
                cse_var_15: T.int32 = ax1_0_4 * 2
                T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 * 4 + 16, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_16 + cse_var_15 + 24, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 24 + cse_var_16 + cse_var_15, T.bool(False))
        Y_reindex_m16n8k8_matrixC_shared_dyn = T.decl_buffer((1536,), "float16", scope="shared.dyn")
        for ax0_0 in range(8):
            B_reindex_shared_dyn_1 = T.Buffer((1536,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            for ax1_0 in range(12):
                B_reindex_shared_dyn_1[threadIdx_y * 768 + ax1_0 * 64 + threadIdx_x * 2:threadIdx_y * 768 + ax1_0 * 64 + threadIdx_x * 2 + 2] = Y_reindex_m16n8k8_matrixC_2[ax0_0 // 2 * 24 + ax1_0 * 2 + ax0_0 % 2]
            for ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 in range(24):
                Y_1 = T.Buffer((1327104,), "float16", data=Y.data)
                Y_1[blockIdx_x * 147456 + ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 // 12 * 73728 + ax0_0 * 9216 + threadIdx_y * 4608 + threadIdx_x // 8 * 1152 + blockIdx_y * 96 + ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 % 12 * 8 + threadIdx_x % 8] = B_reindex_shared_dyn_1[ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 * 64 + threadIdx_y * 32 + threadIdx_x]
