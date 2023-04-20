# from tvm.script import ir as I
# from tvm.script import tir as T

@I.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer((512, 640), "float16"), B: T.Buffer((640, 256), "float16"), Y: T.Buffer((512, 256), "float16")):
        T.func_attr({"global_symbol": "main", "tir.noalias": T.bool(True)})
        blockIdx_x = T.launch_thread("blockIdx.x", 16)
        Y_reindex_m16n8k8_matrixC = T.allocate([16], "float16x2", "local")
        A_reindex_shared_dyn = T.allocate([15360], "float16", "shared.dyn")
        B_reindex_shared_dyn = T.allocate([7680], "float16", "shared.dyn")
        A_reindex_shared_dyn_m16n8k8_matrixA = T.allocate([16], "float16", "local")
        B_reindex_shared_dyn_m16n8k8_matrixB = T.allocate([16], "float16", "local")
        blockIdx_y = T.launch_thread("blockIdx.y", 4)
        threadIdx_y = T.launch_thread("threadIdx.y", 2)
        threadIdx_x = T.launch_thread("threadIdx.x", 32)
        Y_reindex_m16n8k8_matrixC_1 = T.decl_buffer((32,), "float16", scope="local")
        Y_reindex_m16n8k8_matrixC_2 = T.Buffer((16,), "float16x2", data=Y_reindex_m16n8k8_matrixC, scope="local")
        for ax0_0_3_init, ax1_0_3_init, ax1_0_4_init, b in T.grid(2, 2, 2, 2):
            Y_reindex_m16n8k8_matrixC_2[ax0_0_3_init * 8 + ax1_0_3_init * 4 + ax1_0_4_init * 2 + b] = T.Broadcast(T.float16(0), 2)
        with T.decl_buffer((15360,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn") as A_reindex_shared_dyn_1:
            B_reindex_shared_dyn_1 = T.decl_buffer((7680,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            A_reindex_shared_dyn_m16n8k8_matrixA_1 = T.decl_buffer((16,), "float16", data=A_reindex_shared_dyn_m16n8k8_matrixA, scope="local")
            B_reindex_shared_dyn_m16n8k8_matrixB_1 = T.decl_buffer((16,), "float16", data=B_reindex_shared_dyn_m16n8k8_matrixB, scope="local")
            A_reindex_shared_dyn_2 = T.Buffer((15360,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
            A_1 = T.Buffer((327680,), "float16", data=A.data)
            B_reindex_shared_dyn_2 = T.Buffer((7680,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            B_1 = T.Buffer((163840,), "float16", data=B.data)
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    for ax0_ax1_fused_0 in range(10):
                        A_reindex_shared_dyn_2[ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8:ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = A_1[blockIdx_x // 8 * 163840 + blockIdx_y * 40960 + (ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8) // 80 * 640 + (ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8) % 80:blockIdx_x // 8 * 163840 + blockIdx_y * 40960 + (ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8) // 80 * 640 + (ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8) % 80 + 8]
                T.attr(0, "async_scope", 1)
                for ax0_ax1_fused_0 in range(5):
                    B_reindex_shared_dyn_2[ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8:ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = B_1[ax0_ax1_fused_0 * 4096 + threadIdx_y * 2048 + threadIdx_x // 4 * 256 + blockIdx_x % 8 * 32 + threadIdx_x % 4 * 8:ax0_ax1_fused_0 * 4096 + threadIdx_y * 2048 + threadIdx_x // 4 * 256 + blockIdx_x % 8 * 32 + threadIdx_x % 4 * 8 + 8]
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    for ax0_ax1_fused_0 in range(10):
                        A_reindex_shared_dyn_2[ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 5120:ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 5120 + 8] = A_1[blockIdx_x // 8 * 163840 + blockIdx_y * 40960 + (ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8) // 80 * 640 + (ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8) % 80 + 80:blockIdx_x // 8 * 163840 + blockIdx_y * 40960 + (ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8) // 80 * 640 + (ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8) % 80 + 80 + 8]
                T.attr(0, "async_scope", 1)
                for ax0_ax1_fused_0 in range(5):
                    B_reindex_shared_dyn_2[ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 2560:ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 2560 + 8] = B_1[ax0_ax1_fused_0 * 4096 + threadIdx_y * 2048 + threadIdx_x // 4 * 256 + blockIdx_x % 8 * 32 + threadIdx_x % 4 * 8 + 20480:ax0_ax1_fused_0 * 4096 + threadIdx_y * 2048 + threadIdx_x // 4 * 256 + blockIdx_x % 8 * 32 + threadIdx_x % 4 * 8 + 20480 + 8]
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 1)
                T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, 0, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 2560, 2560, 1), threadIdx_x * 80)
                T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, 0, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, 0, 256, 1), threadIdx_x % 8 * 32 + threadIdx_x // 8 * 8)
            for ax2_0_0 in range(6):
                cse_var_1: T.int32 = (ax2_0_0 + 1) % 3
                with T.attr(0, "async_commit_queue_scope", 0):
                    with T.attr(0, "async_scope", 1):
                        for ax0_ax1_fused_0 in range(10):
                            cse_var_2: T.int32 = ax0_ax1_fused_0 * 512
                            A_reindex_shared_dyn_2[(ax2_0_0 + 2) % 3 * 5120 + cse_var_2 + threadIdx_y * 256 + threadIdx_x * 8:(ax2_0_0 + 2) % 3 * 5120 + cse_var_2 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = A_1[blockIdx_x // 8 * 163840 + blockIdx_y * 40960 + (cse_var_2 + threadIdx_y * 256 + threadIdx_x * 8) // 80 * 640 + ax2_0_0 * 80 + (cse_var_2 + threadIdx_y * 256 + threadIdx_x * 8) % 80 + 160:blockIdx_x // 8 * 163840 + blockIdx_y * 40960 + (cse_var_2 + threadIdx_y * 256 + threadIdx_x * 8) // 80 * 640 + ax2_0_0 * 80 + (cse_var_2 + threadIdx_y * 256 + threadIdx_x * 8) % 80 + 160 + 8]
                    T.attr(0, "async_scope", 1)
                    for ax0_ax1_fused_0 in range(5):
                        B_reindex_shared_dyn_2[(ax2_0_0 + 2) % 3 * 2560 + ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8:(ax2_0_0 + 2) % 3 * 2560 + ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = B_1[ax2_0_0 * 20480 + ax0_ax1_fused_0 * 4096 + threadIdx_y * 2048 + threadIdx_x // 4 * 256 + blockIdx_x % 8 * 32 + threadIdx_x % 4 * 8 + 40960:ax2_0_0 * 20480 + ax0_ax1_fused_0 * 4096 + threadIdx_y * 2048 + threadIdx_x // 4 * 256 + blockIdx_x % 8 * 32 + threadIdx_x % 4 * 8 + 40960 + 8]
                with T.attr(0, "async_wait_queue_scope", 0):
                    T.attr(0, "async_wait_inflight_count", 1)
                    for ax2_0_1 in range(9):
                        cse_var_4: T.int32 = ax2_0_0 % 3
                        cse_var_3: T.int32 = (ax2_0_1 + 1) % 2 * 8
                        T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, cse_var_3, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, cse_var_4 * 5120 + threadIdx_y * 2560 + ax2_0_1 * 8 + 8, 2560, 1), threadIdx_x * 80)
                        T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_3, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, cse_var_4 * 2560 + ax2_0_1 * 256 + 256, 256, 1), threadIdx_x % 8 * 32 + threadIdx_x // 8 * 8)
                        for ax0_0_3, ax1_0_3, ax1_0_4 in T.grid(2, 2, 2):
                            cse_var_7: T.int32 = ax1_0_3 * 4
                            cse_var_6: T.int32 = ax1_0_4 * 2
                            cse_var_5: T.int32 = ax2_0_1 % 2 * 8
                            T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, cse_var_5 + ax0_0_3 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_5 + cse_var_7 + cse_var_6, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 8 + cse_var_7 + cse_var_6, T.bool(False))
                T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, 0, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, cse_var_1 * 5120 + threadIdx_y * 2560, 2560, 1), threadIdx_x * 80)
                T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, 0, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, cse_var_1 * 2560, 256, 1), threadIdx_x % 8 * 32 + threadIdx_x // 8 * 8)
                for ax0_0_3, ax1_0_3, ax1_0_4 in T.grid(2, 2, 2):
                    cse_var_9: T.int32 = ax1_0_3 * 4
                    cse_var_8: T.int32 = ax1_0_4 * 2
                    T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 * 4 + 8, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_9 + cse_var_8 + 8, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 8 + cse_var_9 + cse_var_8, T.bool(False))
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 0)
                for ax2_0_1 in range(9):
                    cse_var_10: T.int32 = (ax2_0_1 + 1) % 2 * 8
                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, cse_var_10, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 2560 + ax2_0_1 * 8 + 8, 2560, 1), threadIdx_x * 80)
                    T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_10, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax2_0_1 * 256 + 256, 256, 1), threadIdx_x % 8 * 32 + threadIdx_x // 8 * 8)
                    for ax0_0_3, ax1_0_3, ax1_0_4 in T.grid(2, 2, 2):
                        cse_var_13: T.int32 = ax1_0_3 * 4
                        cse_var_12: T.int32 = ax1_0_4 * 2
                        cse_var_11: T.int32 = ax2_0_1 % 2 * 8
                        T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, cse_var_11 + ax0_0_3 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_11 + cse_var_13 + cse_var_12, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 8 + cse_var_13 + cse_var_12, T.bool(False))
            T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, 0, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 2560 + 5120, 2560, 1), threadIdx_x * 80)
            T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, 0, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, 2560, 256, 1), threadIdx_x % 8 * 32 + threadIdx_x // 8 * 8)
            for ax0_0_3, ax1_0_3, ax1_0_4 in T.grid(2, 2, 2):
                cse_var_15: T.int32 = ax1_0_3 * 4
                cse_var_14: T.int32 = ax1_0_4 * 2
                T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 * 4 + 8, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_15 + cse_var_14 + 8, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 8 + cse_var_15 + cse_var_14, T.bool(False))
            for ax2_0_1 in range(9):
                cse_var_16: T.int32 = (ax2_0_1 + 1) % 2 * 8
                T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, cse_var_16, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 2560 + ax2_0_1 * 8 + 5128, 2560, 1), threadIdx_x * 80)
                T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_16, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax2_0_1 * 256 + 2816, 256, 1), threadIdx_x % 8 * 32 + threadIdx_x // 8 * 8)
                for ax0_0_3, ax1_0_3, ax1_0_4 in T.grid(2, 2, 2):
                    cse_var_19: T.int32 = ax1_0_3 * 4
                    cse_var_18: T.int32 = ax1_0_4 * 2
                    cse_var_17: T.int32 = ax2_0_1 % 2 * 8
                    T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, cse_var_17 + ax0_0_3 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_17 + cse_var_19 + cse_var_18, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 8 + cse_var_19 + cse_var_18, T.bool(False))
            for ax0_0_3, ax1_0_3, ax1_0_4 in T.grid(2, 2, 2):
                cse_var_21: T.int32 = ax1_0_3 * 4
                cse_var_20: T.int32 = ax1_0_4 * 2
                T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 * 4 + 8, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_21 + cse_var_20 + 8, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 8 + cse_var_21 + cse_var_20, T.bool(False))
        Y_reindex_m16n8k8_matrixC_shared_dyn = T.decl_buffer((512,), "float16", scope="shared.dyn")
        for ax0_0 in range(4):
            B_reindex_shared_dyn_1 = T.Buffer((512,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            for ax1_0 in range(4):
                B_reindex_shared_dyn_1[threadIdx_y * 256 + ax1_0 * 64 + threadIdx_x * 2:threadIdx_y * 256 + ax1_0 * 64 + threadIdx_x * 2 + 2] = Y_reindex_m16n8k8_matrixC_2[ax0_0 // 2 * 8 + ax1_0 * 2 + ax0_0 % 2]
            for ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 in range(8):
                Y_1 = T.Buffer((131072,), "float16", data=Y.data)
                Y_1[blockIdx_x // 8 * 65536 + blockIdx_y * 16384 + ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 // 4 * 8192 + ax0_0 * 2048 + threadIdx_y * 1024 + threadIdx_x // 8 * 256 + blockIdx_x % 8 * 32 + ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 % 4 * 8 + threadIdx_x % 8] = B_reindex_shared_dyn_1[ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 * 64 + threadIdx_y * 32 + threadIdx_x]
