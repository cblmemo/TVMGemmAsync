# from tvm.script import ir as I
# from tvm.script import tir as T

@I.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer((512, 3072), "float16"), B: T.Buffer((3072, 768), "float16"), Y: T.Buffer((512, 768), "float16")):
        T.func_attr({"global_symbol": "main", "tir.noalias": T.bool(True)})
        blockIdx_x = T.launch_thread("blockIdx.x", 32)
        Y_reindex_m16n8k8_matrixC = T.allocate([32], "float16x2", "local")
        A_reindex_shared_dyn = T.allocate([9216], "float16", "shared.dyn")
        B_reindex_shared_dyn = T.allocate([13824], "float16", "shared.dyn")
        A_reindex_shared_dyn_m16n8k8_matrixA = T.allocate([96], "float16", "local")
        B_reindex_shared_dyn_m16n8k8_matrixB = T.allocate([48], "float16", "local")
        blockIdx_y = T.launch_thread("blockIdx.y", 2)
        threadIdx_y = T.launch_thread("threadIdx.y", 3)
        threadIdx_x = T.launch_thread("threadIdx.x", 32)
        Y_reindex_m16n8k8_matrixC_1 = T.decl_buffer((64,), "float16", scope="local")
        Y_reindex_m16n8k8_matrixC_2 = T.Buffer((32,), "float16x2", data=Y_reindex_m16n8k8_matrixC, scope="local")
        for ax1_0_3_init, ax0_0_4_init, ax1_0_4_init, b in T.grid(2, 4, 2, 2):
            Y_reindex_m16n8k8_matrixC_2[ax0_0_4_init * 8 + ax1_0_3_init * 4 + ax1_0_4_init * 2 + b] = T.Broadcast(T.float16(0), 2)
        with T.decl_buffer((9216,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn") as A_reindex_shared_dyn_1:
            B_reindex_shared_dyn_1 = T.decl_buffer((13824,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            A_reindex_shared_dyn_m16n8k8_matrixA_1 = T.decl_buffer((96,), "float16", data=A_reindex_shared_dyn_m16n8k8_matrixA, scope="local")
            B_reindex_shared_dyn_m16n8k8_matrixB_1 = T.decl_buffer((48,), "float16", data=B_reindex_shared_dyn_m16n8k8_matrixB, scope="local")
            A_reindex_shared_dyn_2 = T.Buffer((9216,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
            A_1 = T.Buffer((1572864,), "float16", data=A.data)
            B_reindex_shared_dyn_2 = T.Buffer((13824,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            B_1 = T.Buffer((2359296,), "float16", data=B.data)
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    for ax0_ax1_fused_0 in range(4):
                        A_reindex_shared_dyn_2[ax0_ax1_fused_0 * 768 + threadIdx_y * 256 + threadIdx_x * 8:ax0_ax1_fused_0 * 768 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = A_1[blockIdx_x // 8 * 393216 + blockIdx_y * 196608 + ax0_ax1_fused_0 * 49152 + (threadIdx_y * 256 + threadIdx_x * 8) // 48 * 3072 + (threadIdx_y * 16 + threadIdx_x * 8) % 48:blockIdx_x // 8 * 393216 + blockIdx_y * 196608 + ax0_ax1_fused_0 * 49152 + (threadIdx_y * 256 + threadIdx_x * 8) // 48 * 3072 + (threadIdx_y * 16 + threadIdx_x * 8) % 48 + 8]
                T.attr(0, "async_scope", 1)
                for ax0_ax1_fused_0 in range(6):
                    B_reindex_shared_dyn_2[ax0_ax1_fused_0 * 768 + threadIdx_y * 256 + threadIdx_x * 8:ax0_ax1_fused_0 * 768 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = B_1[ax0_ax1_fused_0 * 6144 + (threadIdx_y * 256 + threadIdx_x * 8) // 96 * 768 + blockIdx_x % 8 * 96 + (threadIdx_y * 64 + threadIdx_x * 8) % 96:ax0_ax1_fused_0 * 6144 + (threadIdx_y * 256 + threadIdx_x * 8) // 96 * 768 + blockIdx_x % 8 * 96 + (threadIdx_y * 64 + threadIdx_x * 8) % 96 + 8]
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    for ax0_ax1_fused_0 in range(4):
                        A_reindex_shared_dyn_2[ax0_ax1_fused_0 * 768 + threadIdx_y * 256 + threadIdx_x * 8 + 3072:ax0_ax1_fused_0 * 768 + threadIdx_y * 256 + threadIdx_x * 8 + 3072 + 8] = A_1[blockIdx_x // 8 * 393216 + blockIdx_y * 196608 + ax0_ax1_fused_0 * 49152 + (threadIdx_y * 256 + threadIdx_x * 8) // 48 * 3072 + (threadIdx_y * 16 + threadIdx_x * 8) % 48 + 48:blockIdx_x // 8 * 393216 + blockIdx_y * 196608 + ax0_ax1_fused_0 * 49152 + (threadIdx_y * 256 + threadIdx_x * 8) // 48 * 3072 + (threadIdx_y * 16 + threadIdx_x * 8) % 48 + 48 + 8]
                T.attr(0, "async_scope", 1)
                for ax0_ax1_fused_0 in range(6):
                    B_reindex_shared_dyn_2[ax0_ax1_fused_0 * 768 + threadIdx_y * 256 + threadIdx_x * 8 + 4608:ax0_ax1_fused_0 * 768 + threadIdx_y * 256 + threadIdx_x * 8 + 4608 + 8] = B_1[ax0_ax1_fused_0 * 6144 + (threadIdx_y * 256 + threadIdx_x * 8) // 96 * 768 + blockIdx_x % 8 * 96 + (threadIdx_y * 64 + threadIdx_x * 8) % 96 + 36864:ax0_ax1_fused_0 * 6144 + (threadIdx_y * 256 + threadIdx_x * 8) // 96 * 768 + blockIdx_x % 8 * 96 + (threadIdx_y * 64 + threadIdx_x * 8) % 96 + 36864 + 8]
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 1)
                for ax0_0, ax1_0 in T.grid(2, 3):
                    cse_var_1: T.int32 = ax1_0 * 8
                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 24 + cse_var_1, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax0_0 * 1536 + cse_var_1, 1536, 1), threadIdx_x * 48)
                for ax0_0 in range(3):
                    T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax0_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax0_0 * 768 + threadIdx_y * 32, 768, 1), threadIdx_x % 8 * 96 + threadIdx_x // 8 * 8)
            for ax2_0_0 in range(62):
                with T.attr(0, "async_commit_queue_scope", 0):
                    with T.attr(0, "async_scope", 1):
                        for ax0_ax1_fused_0 in range(4):
                            A_reindex_shared_dyn_2[(ax2_0_0 + 2) % 3 * 3072 + ax0_ax1_fused_0 * 768 + threadIdx_y * 256 + threadIdx_x * 8:(ax2_0_0 + 2) % 3 * 3072 + ax0_ax1_fused_0 * 768 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = A_1[blockIdx_x // 8 * 393216 + blockIdx_y * 196608 + ax0_ax1_fused_0 * 49152 + (threadIdx_y * 256 + threadIdx_x * 8) // 48 * 3072 + ax2_0_0 * 48 + (threadIdx_y * 16 + threadIdx_x * 8) % 48 + 96:blockIdx_x // 8 * 393216 + blockIdx_y * 196608 + ax0_ax1_fused_0 * 49152 + (threadIdx_y * 256 + threadIdx_x * 8) // 48 * 3072 + ax2_0_0 * 48 + (threadIdx_y * 16 + threadIdx_x * 8) % 48 + 96 + 8]
                    T.attr(0, "async_scope", 1)
                    for ax0_ax1_fused_0 in range(6):
                        B_reindex_shared_dyn_2[(ax2_0_0 + 2) % 3 * 4608 + ax0_ax1_fused_0 * 768 + threadIdx_y * 256 + threadIdx_x * 8:(ax2_0_0 + 2) % 3 * 4608 + ax0_ax1_fused_0 * 768 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = B_1[ax2_0_0 * 36864 + ax0_ax1_fused_0 * 6144 + (threadIdx_y * 256 + threadIdx_x * 8) // 96 * 768 + blockIdx_x % 8 * 96 + (threadIdx_y * 64 + threadIdx_x * 8) % 96 + 73728:ax2_0_0 * 36864 + ax0_ax1_fused_0 * 6144 + (threadIdx_y * 256 + threadIdx_x * 8) // 96 * 768 + blockIdx_x % 8 * 96 + (threadIdx_y * 64 + threadIdx_x * 8) % 96 + 73728 + 8]
                with T.attr(0, "async_wait_queue_scope", 0):
                    T.attr(0, "async_wait_inflight_count", 1)
                    for ax0_0, ax1_0 in T.grid(2, 3):
                        cse_var_2: T.int32 = ax1_0 * 8
                        T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 24 + cse_var_2 + 48, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax2_0_0 % 3 * 3072 + ax0_0 * 1536 + cse_var_2 + 24, 1536, 1), threadIdx_x * 48)
                    for ax0_0 in range(3):
                        T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax0_0 * 8 + 24, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax2_0_0 % 3 * 4608 + ax0_0 * 768 + threadIdx_y * 32 + 2304, 768, 1), threadIdx_x % 8 * 96 + threadIdx_x // 8 * 8)
                    for ax1_0_3, ax2_0_2, ax0_0_4, ax1_0_4 in T.grid(2, 3, 4, 2):
                        cse_var_5: T.int32 = ax1_0_3 * 4
                        cse_var_4: T.int32 = ax2_0_2 * 8
                        cse_var_3: T.int32 = ax1_0_4 * 2
                        T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_4 // 2 * 24 + cse_var_4 + ax0_0_4 % 2 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_4 + cse_var_5 + cse_var_3, Y_reindex_m16n8k8_matrixC, ax0_0_4 * 8 + cse_var_5 + cse_var_3, T.bool(False))
                for ax0_0, ax1_0 in T.grid(2, 3):
                    cse_var_6: T.int32 = ax1_0 * 8
                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 24 + cse_var_6, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, (ax2_0_0 + 1) % 3 * 3072 + ax0_0 * 1536 + cse_var_6, 1536, 1), threadIdx_x * 48)
                for ax0_0 in range(3):
                    T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax0_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, (ax2_0_0 + 1) % 3 * 4608 + ax0_0 * 768 + threadIdx_y * 32, 768, 1), threadIdx_x % 8 * 96 + threadIdx_x // 8 * 8)
                for ax1_0_3, ax2_0_2, ax0_0_4, ax1_0_4 in T.grid(2, 3, 4, 2):
                    cse_var_9: T.int32 = ax1_0_3 * 4
                    cse_var_8: T.int32 = ax2_0_2 * 8
                    cse_var_7: T.int32 = ax1_0_4 * 2
                    T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_4 // 2 * 24 + cse_var_8 + ax0_0_4 % 2 * 4 + 48, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_8 + cse_var_9 + cse_var_7 + 24, Y_reindex_m16n8k8_matrixC, ax0_0_4 * 8 + cse_var_9 + cse_var_7, T.bool(False))
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 0)
                for ax0_0, ax1_0 in T.grid(2, 3):
                    cse_var_10: T.int32 = ax1_0 * 8
                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 24 + cse_var_10 + 48, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax0_0 * 1536 + cse_var_10 + 6168, 1536, 1), threadIdx_x * 48)
                for ax0_0 in range(3):
                    T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax0_0 * 8 + 24, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax0_0 * 768 + threadIdx_y * 32 + 11520, 768, 1), threadIdx_x % 8 * 96 + threadIdx_x // 8 * 8)
                for ax1_0_3, ax2_0_2, ax0_0_4, ax1_0_4 in T.grid(2, 3, 4, 2):
                    cse_var_13: T.int32 = ax1_0_3 * 4
                    cse_var_12: T.int32 = ax2_0_2 * 8
                    cse_var_11: T.int32 = ax1_0_4 * 2
                    T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_4 // 2 * 24 + cse_var_12 + ax0_0_4 % 2 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_12 + cse_var_13 + cse_var_11, Y_reindex_m16n8k8_matrixC, ax0_0_4 * 8 + cse_var_13 + cse_var_11, T.bool(False))
            for ax0_0, ax1_0 in T.grid(2, 3):
                cse_var_14: T.int32 = ax1_0 * 8
                T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 24 + cse_var_14, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax0_0 * 1536 + cse_var_14, 1536, 1), threadIdx_x * 48)
            for ax0_0 in range(3):
                T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax0_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax0_0 * 768 + threadIdx_y * 32, 768, 1), threadIdx_x % 8 * 96 + threadIdx_x // 8 * 8)
            for ax1_0_3, ax2_0_2, ax0_0_4, ax1_0_4 in T.grid(2, 3, 4, 2):
                cse_var_17: T.int32 = ax1_0_3 * 4
                cse_var_16: T.int32 = ax2_0_2 * 8
                cse_var_15: T.int32 = ax1_0_4 * 2
                T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_4 // 2 * 24 + cse_var_16 + ax0_0_4 % 2 * 4 + 48, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_16 + cse_var_17 + cse_var_15 + 24, Y_reindex_m16n8k8_matrixC, ax0_0_4 * 8 + cse_var_17 + cse_var_15, T.bool(False))
            for ax0_0, ax1_0 in T.grid(2, 3):
                cse_var_18: T.int32 = ax1_0 * 8
                T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 24 + cse_var_18 + 48, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax0_0 * 1536 + cse_var_18 + 24, 1536, 1), threadIdx_x * 48)
            for ax0_0 in range(3):
                T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax0_0 * 8 + 24, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax0_0 * 768 + threadIdx_y * 32 + 2304, 768, 1), threadIdx_x % 8 * 96 + threadIdx_x // 8 * 8)
            for ax1_0_3, ax2_0_2, ax0_0_4, ax1_0_4 in T.grid(2, 3, 4, 2):
                cse_var_21: T.int32 = ax1_0_3 * 4
                cse_var_20: T.int32 = ax2_0_2 * 8
                cse_var_19: T.int32 = ax1_0_4 * 2
                T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_4 // 2 * 24 + cse_var_20 + ax0_0_4 % 2 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_20 + cse_var_21 + cse_var_19, Y_reindex_m16n8k8_matrixC, ax0_0_4 * 8 + cse_var_21 + cse_var_19, T.bool(False))
            for ax1_0_3, ax2_0_2, ax0_0_4, ax1_0_4 in T.grid(2, 3, 4, 2):
                cse_var_24: T.int32 = ax1_0_3 * 4
                cse_var_23: T.int32 = ax2_0_2 * 8
                cse_var_22: T.int32 = ax1_0_4 * 2
                T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_4 // 2 * 24 + cse_var_23 + ax0_0_4 % 2 * 4 + 48, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_23 + cse_var_24 + cse_var_22 + 24, Y_reindex_m16n8k8_matrixC, ax0_0_4 * 8 + cse_var_24 + cse_var_22, T.bool(False))
        Y_reindex_m16n8k8_matrixC_shared_dyn = T.decl_buffer((768,), "float16", scope="shared.dyn")
        for ax0_0 in range(8):
            A_reindex_shared_dyn_1 = T.Buffer((768,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
            for ax1_0 in range(4):
                A_reindex_shared_dyn_1[threadIdx_y * 256 + ax1_0 * 64 + threadIdx_x * 2:threadIdx_y * 256 + ax1_0 * 64 + threadIdx_x * 2 + 2] = Y_reindex_m16n8k8_matrixC_2[ax0_0 // 2 * 8 + ax1_0 * 2 + ax0_0 % 2]
            for ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 in range(8):
                Y_1 = T.Buffer((393216,), "float16", data=Y.data)
                Y_1[blockIdx_x // 8 * 98304 + blockIdx_y * 49152 + ax0_0 * 6144 + (ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 * 12 + threadIdx_y * 4 + threadIdx_x // 8) % 8 * 768 + blockIdx_x % 8 * 96 + (ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 * 3 + threadIdx_y) // 2 * 8 + threadIdx_x % 8] = A_reindex_shared_dyn_1[ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 * 96 + threadIdx_y * 32 + threadIdx_x]
