# from tvm.script import ir as I
# from tvm.script import tir as T

@I.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer((1536, 1536), "float16"), B: T.Buffer((1536, 1536), "float16"), Y: T.Buffer((1536, 1536), "float16")):
        T.func_attr({"global_symbol": "main", "tir.noalias": T.bool(True)})
        blockIdx_x = T.launch_thread("blockIdx.x", 16)
        Y_reindex_m16n8k8_matrixC = T.allocate([48], "float16x2", "local")
        A_reindex_shared_dyn = T.allocate([4608], "float16", "shared.dyn")
        B_reindex_shared_dyn = T.allocate([4608], "float16", "shared.dyn")
        A_reindex_shared_dyn_m16n8k8_matrixA = T.allocate([48], "float16", "local")
        B_reindex_shared_dyn_m16n8k8_matrixB = T.allocate([16], "float16", "local")
        blockIdx_y = T.launch_thread("blockIdx.y", 16)
        threadIdx_y = T.launch_thread("threadIdx.y", 3)
        threadIdx_x = T.launch_thread("threadIdx.x", 32)
        Y_reindex_m16n8k8_matrixC_1 = T.decl_buffer((96,), "float16", scope="local")
        Y_reindex_m16n8k8_matrixC_2 = T.Buffer((48,), "float16x2", data=Y_reindex_m16n8k8_matrixC, scope="local")
        for ax0_0_3_init, ax1_0_3_init, ax0_0_4_init, b in T.grid(2, 4, 3, 2):
            Y_reindex_m16n8k8_matrixC_2[ax0_0_3_init * 24 + ax0_0_4_init * 8 + ax1_0_3_init * 2 + b] = T.Broadcast(T.float16(0), 2)
        with T.decl_buffer((4608,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn") as A_reindex_shared_dyn_1:
            B_reindex_shared_dyn_1 = T.decl_buffer((4608,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            A_reindex_shared_dyn_m16n8k8_matrixA_1 = T.decl_buffer((48,), "float16", data=A_reindex_shared_dyn_m16n8k8_matrixA, scope="local")
            B_reindex_shared_dyn_m16n8k8_matrixB_1 = T.decl_buffer((16,), "float16", data=B_reindex_shared_dyn_m16n8k8_matrixB, scope="local")
            A_reindex_shared_dyn_2 = T.Buffer((4608,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
            A_1 = T.Buffer((2359296,), "float16", data=A.data)
            B_reindex_shared_dyn_2 = T.Buffer((4608,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            B_1 = T.Buffer((2359296,), "float16", data=B.data)
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    for ax0_ax1_fused_0 in range(2):
                        A_reindex_shared_dyn_2[ax0_ax1_fused_0 * 768 + threadIdx_y * 256 + threadIdx_x * 8:ax0_ax1_fused_0 * 768 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = A_1[blockIdx_x // 8 * 1179648 + blockIdx_y // 2 * 147456 + ax0_ax1_fused_0 * 73728 + threadIdx_y * 24576 + threadIdx_x // 2 * 1536 + threadIdx_x % 2 * 8:blockIdx_x // 8 * 1179648 + blockIdx_y // 2 * 147456 + ax0_ax1_fused_0 * 73728 + threadIdx_y * 24576 + threadIdx_x // 2 * 1536 + threadIdx_x % 2 * 8 + 8]
                T.attr(0, "async_scope", 1)
                for ax0_ax1_fused_0 in range(2):
                    B_reindex_shared_dyn_2[ax0_ax1_fused_0 * 768 + threadIdx_y * 256 + threadIdx_x * 8:ax0_ax1_fused_0 * 768 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = B_1[ax0_ax1_fused_0 * 12288 + (threadIdx_y * 256 + threadIdx_x * 8) // 96 * 1536 + blockIdx_x % 8 * 192 + blockIdx_y % 2 * 96 + (threadIdx_y * 64 + threadIdx_x * 8) % 96:ax0_ax1_fused_0 * 12288 + (threadIdx_y * 256 + threadIdx_x * 8) // 96 * 1536 + blockIdx_x % 8 * 192 + blockIdx_y % 2 * 96 + (threadIdx_y * 64 + threadIdx_x * 8) % 96 + 8]
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    for ax0_ax1_fused_0 in range(2):
                        A_reindex_shared_dyn_2[ax0_ax1_fused_0 * 768 + threadIdx_y * 256 + threadIdx_x * 8 + 1536:ax0_ax1_fused_0 * 768 + threadIdx_y * 256 + threadIdx_x * 8 + 1536 + 8] = A_1[blockIdx_x // 8 * 1179648 + blockIdx_y // 2 * 147456 + ax0_ax1_fused_0 * 73728 + threadIdx_y * 24576 + threadIdx_x // 2 * 1536 + threadIdx_x % 2 * 8 + 16:blockIdx_x // 8 * 1179648 + blockIdx_y // 2 * 147456 + ax0_ax1_fused_0 * 73728 + threadIdx_y * 24576 + threadIdx_x // 2 * 1536 + threadIdx_x % 2 * 8 + 16 + 8]
                T.attr(0, "async_scope", 1)
                for ax0_ax1_fused_0 in range(2):
                    B_reindex_shared_dyn_2[ax0_ax1_fused_0 * 768 + threadIdx_y * 256 + threadIdx_x * 8 + 1536:ax0_ax1_fused_0 * 768 + threadIdx_y * 256 + threadIdx_x * 8 + 1536 + 8] = B_1[ax0_ax1_fused_0 * 12288 + (threadIdx_y * 256 + threadIdx_x * 8) // 96 * 1536 + blockIdx_x % 8 * 192 + blockIdx_y % 2 * 96 + (threadIdx_y * 64 + threadIdx_x * 8) % 96 + 24576:ax0_ax1_fused_0 * 12288 + (threadIdx_y * 256 + threadIdx_x * 8) // 96 * 1536 + blockIdx_x % 8 * 192 + blockIdx_y % 2 * 96 + (threadIdx_y * 64 + threadIdx_x * 8) % 96 + 24576 + 8]
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 1)
                for ax0_0 in range(3):
                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax0_0 * 512, 512, 1), threadIdx_x * 16)
                T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, 0, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, threadIdx_y * 32, 768, 1), threadIdx_x % 8 * 96 + threadIdx_x // 8 * 8)
            for ax2_0_0 in range(94):
                with T.attr(0, "async_commit_queue_scope", 0):
                    with T.attr(0, "async_scope", 1):
                        for ax0_ax1_fused_0 in range(2):
                            A_reindex_shared_dyn_2[(ax2_0_0 + 2) % 3 * 1536 + ax0_ax1_fused_0 * 768 + threadIdx_y * 256 + threadIdx_x * 8:(ax2_0_0 + 2) % 3 * 1536 + ax0_ax1_fused_0 * 768 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = A_1[blockIdx_x // 8 * 1179648 + blockIdx_y // 2 * 147456 + ax0_ax1_fused_0 * 73728 + threadIdx_y * 24576 + threadIdx_x // 2 * 1536 + ax2_0_0 * 16 + threadIdx_x % 2 * 8 + 32:blockIdx_x // 8 * 1179648 + blockIdx_y // 2 * 147456 + ax0_ax1_fused_0 * 73728 + threadIdx_y * 24576 + threadIdx_x // 2 * 1536 + ax2_0_0 * 16 + threadIdx_x % 2 * 8 + 32 + 8]
                    T.attr(0, "async_scope", 1)
                    for ax0_ax1_fused_0 in range(2):
                        B_reindex_shared_dyn_2[(ax2_0_0 + 2) % 3 * 1536 + ax0_ax1_fused_0 * 768 + threadIdx_y * 256 + threadIdx_x * 8:(ax2_0_0 + 2) % 3 * 1536 + ax0_ax1_fused_0 * 768 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = B_1[ax2_0_0 * 24576 + ax0_ax1_fused_0 * 12288 + (threadIdx_y * 256 + threadIdx_x * 8) // 96 * 1536 + blockIdx_x % 8 * 192 + blockIdx_y % 2 * 96 + (threadIdx_y * 64 + threadIdx_x * 8) % 96 + 49152:ax2_0_0 * 24576 + ax0_ax1_fused_0 * 12288 + (threadIdx_y * 256 + threadIdx_x * 8) // 96 * 1536 + blockIdx_x % 8 * 192 + blockIdx_y % 2 * 96 + (threadIdx_y * 64 + threadIdx_x * 8) % 96 + 49152 + 8]
                with T.attr(0, "async_wait_queue_scope", 0):
                    T.attr(0, "async_wait_inflight_count", 1)
                    for ax0_0 in range(3):
                        T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8 + 24, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax2_0_0 % 3 * 1536 + ax0_0 * 512 + 8, 512, 1), threadIdx_x * 16)
                    T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax2_0_0 % 3 * 1536 + threadIdx_y * 32 + 768, 768, 1), threadIdx_x % 8 * 96 + threadIdx_x // 8 * 8)
                    for ax0_0_3, ax1_0_3, ax0_0_4 in T.grid(2, 4, 3):
                        cse_var_1: T.int32 = ax1_0_3 * 2
                        T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 * 12 + ax0_0_4 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_1, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 24 + ax0_0_4 * 8 + cse_var_1, T.bool(False))
                for ax0_0 in range(3):
                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, (ax2_0_0 + 1) % 3 * 1536 + ax0_0 * 512, 512, 1), threadIdx_x * 16)
                T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, 0, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, (ax2_0_0 + 1) % 3 * 1536 + threadIdx_y * 32, 768, 1), threadIdx_x % 8 * 96 + threadIdx_x // 8 * 8)
                for ax0_0_3, ax1_0_3, ax0_0_4 in T.grid(2, 4, 3):
                    cse_var_2: T.int32 = ax1_0_3 * 2
                    T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 * 12 + ax0_0_4 * 4 + 24, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_2 + 8, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 24 + ax0_0_4 * 8 + cse_var_2, T.bool(False))
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 0)
                for ax0_0 in range(3):
                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8 + 24, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax0_0 * 512 + 1544, 512, 1), threadIdx_x * 16)
                T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, threadIdx_y * 32 + 2304, 768, 1), threadIdx_x % 8 * 96 + threadIdx_x // 8 * 8)
                for ax0_0_3, ax1_0_3, ax0_0_4 in T.grid(2, 4, 3):
                    cse_var_3: T.int32 = ax1_0_3 * 2
                    T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 * 12 + ax0_0_4 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_3, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 24 + ax0_0_4 * 8 + cse_var_3, T.bool(False))
            for ax0_0 in range(3):
                T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax0_0 * 512 + 3072, 512, 1), threadIdx_x * 16)
            T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, 0, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, threadIdx_y * 32 + 3072, 768, 1), threadIdx_x % 8 * 96 + threadIdx_x // 8 * 8)
            for ax0_0_3, ax1_0_3, ax0_0_4 in T.grid(2, 4, 3):
                cse_var_4: T.int32 = ax1_0_3 * 2
                T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 * 12 + ax0_0_4 * 4 + 24, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_4 + 8, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 24 + ax0_0_4 * 8 + cse_var_4, T.bool(False))
            for ax0_0 in range(3):
                T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8 + 24, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax0_0 * 512 + 3080, 512, 1), threadIdx_x * 16)
            T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, threadIdx_y * 32 + 3840, 768, 1), threadIdx_x % 8 * 96 + threadIdx_x // 8 * 8)
            for ax0_0_3, ax1_0_3, ax0_0_4 in T.grid(2, 4, 3):
                cse_var_5: T.int32 = ax1_0_3 * 2
                T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 * 12 + ax0_0_4 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_5, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 24 + ax0_0_4 * 8 + cse_var_5, T.bool(False))
            for ax0_0_3, ax1_0_3, ax0_0_4 in T.grid(2, 4, 3):
                cse_var_6: T.int32 = ax1_0_3 * 2
                T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_3 * 12 + ax0_0_4 * 4 + 24, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_6 + 8, Y_reindex_m16n8k8_matrixC, ax0_0_3 * 24 + ax0_0_4 * 8 + cse_var_6, T.bool(False))
        Y_reindex_m16n8k8_matrixC_shared_dyn = T.decl_buffer((768,), "float16", scope="shared.dyn")
        for ax0_0 in range(12):
            A_reindex_shared_dyn_1 = T.Buffer((768,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
            for ax1_0 in range(4):
                A_reindex_shared_dyn_1[threadIdx_y * 256 + ax1_0 * 64 + threadIdx_x * 2:threadIdx_y * 256 + ax1_0 * 64 + threadIdx_x * 2 + 2] = Y_reindex_m16n8k8_matrixC_2[ax0_0 // 2 * 8 + ax1_0 * 2 + ax0_0 % 2]
            for ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 in range(8):
                Y_1 = T.Buffer((2359296,), "float16", data=Y.data)
                Y_1[blockIdx_x // 8 * 1179648 + blockIdx_y // 2 * 147456 + ax0_0 * 12288 + (ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 * 12 + threadIdx_y * 4 + threadIdx_x // 8) % 8 * 1536 + blockIdx_x % 8 * 192 + blockIdx_y % 2 * 96 + (ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 * 3 + threadIdx_y) // 2 * 8 + threadIdx_x % 8] = A_reindex_shared_dyn_1[ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 * 96 + threadIdx_y * 32 + threadIdx_x]
