# from tvm.script import ir as I
# from tvm.script import tir as T

@I.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer((4096, 4096), "float16"), B: T.Buffer((4096, 4096), "float16"), Y: T.Buffer((4096, 4096), "float16")):
        T.func_attr({"global_symbol": "main", "tir.noalias": T.bool(True)})
        blockIdx_x = T.launch_thread("blockIdx.x", 4)
        Y_reindex_m16n8k8_matrixC = T.allocate([128], "float16x2", "local")
        A_reindex_shared_dyn = T.allocate([6144], "float16", "shared.dyn")
        B_reindex_shared_dyn = T.allocate([6144], "float16", "shared.dyn")
        A_reindex_shared_dyn_m16n8k8_matrixA = T.allocate([64], "float16", "local")
        B_reindex_shared_dyn_m16n8k8_matrixB = T.allocate([32], "float16", "local")
        blockIdx_y = T.launch_thread("blockIdx.y", 256)
        threadIdx_y = T.launch_thread("threadIdx.y", 2)
        threadIdx_x = T.launch_thread("threadIdx.x", 32)
        Y_reindex_m16n8k8_matrixC_1 = T.decl_buffer((256,), "float16", scope="local")
        Y_reindex_m16n8k8_matrixC_2 = T.Buffer((128,), "float16x2", data=Y_reindex_m16n8k8_matrixC, scope="local")
        for ax1_0_3_init, ax0_0_4_init, b in T.grid(8, 8, 2):
            Y_reindex_m16n8k8_matrixC_2[ax0_0_4_init * 16 + ax1_0_3_init * 2 + b] = T.Broadcast(T.float16(0), 2)
        with T.decl_buffer((6144,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn") as A_reindex_shared_dyn_1:
            B_reindex_shared_dyn_1 = T.decl_buffer((6144,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            A_reindex_shared_dyn_m16n8k8_matrixA_1 = T.decl_buffer((64,), "float16", data=A_reindex_shared_dyn_m16n8k8_matrixA, scope="local")
            B_reindex_shared_dyn_m16n8k8_matrixB_1 = T.decl_buffer((32,), "float16", data=B_reindex_shared_dyn_m16n8k8_matrixB, scope="local")
            A_reindex_shared_dyn_2 = T.Buffer((6144,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
            A_1 = T.Buffer((16777216,), "float16", data=A.data)
            B_reindex_shared_dyn_2 = T.Buffer((6144,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
            B_1 = T.Buffer((16777216,), "float16", data=B.data)
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    for ax0_ax1_fused_0 in range(4):
                        A_reindex_shared_dyn_2[ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8:ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = A_1[blockIdx_x // 2 * 8388608 + blockIdx_y // 16 * 524288 + ax0_ax1_fused_0 * 131072 + threadIdx_y * 65536 + threadIdx_x // 2 * 4096 + threadIdx_x % 2 * 8:blockIdx_x // 2 * 8388608 + blockIdx_y // 16 * 524288 + ax0_ax1_fused_0 * 131072 + threadIdx_y * 65536 + threadIdx_x // 2 * 4096 + threadIdx_x % 2 * 8 + 8]
                T.attr(0, "async_scope", 1)
                for ax0_ax1_fused_0 in range(4):
                    B_reindex_shared_dyn_2[ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8:ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = B_1[ax0_ax1_fused_0 * 16384 + threadIdx_y * 8192 + threadIdx_x // 16 * 4096 + blockIdx_x % 2 * 2048 + blockIdx_y % 16 * 128 + threadIdx_x % 16 * 8:ax0_ax1_fused_0 * 16384 + threadIdx_y * 8192 + threadIdx_x // 16 * 4096 + blockIdx_x % 2 * 2048 + blockIdx_y % 16 * 128 + threadIdx_x % 16 * 8 + 8]
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    for ax0_ax1_fused_0 in range(4):
                        A_reindex_shared_dyn_2[ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 2048:ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 2048 + 8] = A_1[blockIdx_x // 2 * 8388608 + blockIdx_y // 16 * 524288 + ax0_ax1_fused_0 * 131072 + threadIdx_y * 65536 + threadIdx_x // 2 * 4096 + threadIdx_x % 2 * 8 + 16:blockIdx_x // 2 * 8388608 + blockIdx_y // 16 * 524288 + ax0_ax1_fused_0 * 131072 + threadIdx_y * 65536 + threadIdx_x // 2 * 4096 + threadIdx_x % 2 * 8 + 16 + 8]
                T.attr(0, "async_scope", 1)
                for ax0_ax1_fused_0 in range(4):
                    B_reindex_shared_dyn_2[ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 2048:ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 2048 + 8] = B_1[ax0_ax1_fused_0 * 16384 + threadIdx_y * 8192 + threadIdx_x // 16 * 4096 + blockIdx_x % 2 * 2048 + blockIdx_y % 16 * 128 + threadIdx_x % 16 * 8 + 65536:ax0_ax1_fused_0 * 16384 + threadIdx_y * 8192 + threadIdx_x // 16 * 4096 + blockIdx_x % 2 * 2048 + blockIdx_y % 16 * 128 + threadIdx_x % 16 * 8 + 65536 + 8]
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 1)
                for ax0_0 in range(4):
                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax0_0 * 512, 512, 1), threadIdx_x * 16)
                for ax1_0 in range(2):
                    T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax1_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, threadIdx_y * 64 + ax1_0 * 32, 1024, 1), threadIdx_x % 8 * 128 + threadIdx_x // 8 * 8)
            for ax2_0_0 in range(254):
                with T.attr(0, "async_commit_queue_scope", 0):
                    with T.attr(0, "async_scope", 1):
                        for ax0_ax1_fused_0 in range(4):
                            A_reindex_shared_dyn_2[(ax2_0_0 + 2) % 3 * 2048 + ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8:(ax2_0_0 + 2) % 3 * 2048 + ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = A_1[blockIdx_x // 2 * 8388608 + blockIdx_y // 16 * 524288 + ax0_ax1_fused_0 * 131072 + threadIdx_y * 65536 + threadIdx_x // 2 * 4096 + ax2_0_0 * 16 + threadIdx_x % 2 * 8 + 32:blockIdx_x // 2 * 8388608 + blockIdx_y // 16 * 524288 + ax0_ax1_fused_0 * 131072 + threadIdx_y * 65536 + threadIdx_x // 2 * 4096 + ax2_0_0 * 16 + threadIdx_x % 2 * 8 + 32 + 8]
                    T.attr(0, "async_scope", 1)
                    for ax0_ax1_fused_0 in range(4):
                        B_reindex_shared_dyn_2[(ax2_0_0 + 2) % 3 * 2048 + ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8:(ax2_0_0 + 2) % 3 * 2048 + ax0_ax1_fused_0 * 512 + threadIdx_y * 256 + threadIdx_x * 8 + 8] = B_1[ax2_0_0 * 65536 + ax0_ax1_fused_0 * 16384 + threadIdx_y * 8192 + threadIdx_x // 16 * 4096 + blockIdx_x % 2 * 2048 + blockIdx_y % 16 * 128 + threadIdx_x % 16 * 8 + 131072:ax2_0_0 * 65536 + ax0_ax1_fused_0 * 16384 + threadIdx_y * 8192 + threadIdx_x // 16 * 4096 + blockIdx_x % 2 * 2048 + blockIdx_y % 16 * 128 + threadIdx_x % 16 * 8 + 131072 + 8]
                with T.attr(0, "async_wait_queue_scope", 0):
                    T.attr(0, "async_wait_inflight_count", 1)
                    for ax0_0 in range(4):
                        T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8 + 32, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax2_0_0 % 3 * 2048 + ax0_0 * 512 + 8, 512, 1), threadIdx_x * 16)
                    for ax1_0 in range(2):
                        T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax1_0 * 8 + 16, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax2_0_0 % 3 * 2048 + threadIdx_y * 64 + ax1_0 * 32 + 1024, 1024, 1), threadIdx_x % 8 * 128 + threadIdx_x // 8 * 8)
                    for ax1_0_3, ax0_0_4 in T.grid(8, 8):
                        cse_var_1: T.int32 = ax1_0_3 * 2
                        T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_4 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_1, Y_reindex_m16n8k8_matrixC, ax0_0_4 * 16 + cse_var_1, T.bool(False))
                for ax0_0 in range(4):
                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, (ax2_0_0 + 1) % 3 * 2048 + ax0_0 * 512, 512, 1), threadIdx_x * 16)
                for ax1_0 in range(2):
                    T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax1_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, (ax2_0_0 + 1) % 3 * 2048 + threadIdx_y * 64 + ax1_0 * 32, 1024, 1), threadIdx_x % 8 * 128 + threadIdx_x // 8 * 8)
                for ax1_0_3, ax0_0_4 in T.grid(8, 8):
                    cse_var_2: T.int32 = ax1_0_3 * 2
                    T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_4 * 4 + 32, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_2 + 16, Y_reindex_m16n8k8_matrixC, ax0_0_4 * 16 + cse_var_2, T.bool(False))
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 0)
                for ax0_0 in range(4):
                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8 + 32, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax0_0 * 512 + 4104, 512, 1), threadIdx_x * 16)
                for ax1_0 in range(2):
                    T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax1_0 * 8 + 16, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, threadIdx_y * 64 + ax1_0 * 32 + 5120, 1024, 1), threadIdx_x % 8 * 128 + threadIdx_x // 8 * 8)
                for ax1_0_3, ax0_0_4 in T.grid(8, 8):
                    cse_var_3: T.int32 = ax1_0_3 * 2
                    T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_4 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_3, Y_reindex_m16n8k8_matrixC, ax0_0_4 * 16 + cse_var_3, T.bool(False))
            for ax0_0 in range(4):
                T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax0_0 * 512, 512, 1), threadIdx_x * 16)
            for ax1_0 in range(2):
                T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax1_0 * 8, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, threadIdx_y * 64 + ax1_0 * 32, 1024, 1), threadIdx_x % 8 * 128 + threadIdx_x // 8 * 8)
            for ax1_0_3, ax0_0_4 in T.grid(8, 8):
                cse_var_4: T.int32 = ax1_0_3 * 2
                T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_4 * 4 + 32, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_4 + 16, Y_reindex_m16n8k8_matrixC, ax0_0_4 * 16 + cse_var_4, T.bool(False))
            for ax0_0 in range(4):
                T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0 * 8 + 32, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, ax0_0 * 512 + 8, 512, 1), threadIdx_x * 16)
            for ax1_0 in range(2):
                T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", B_reindex_shared_dyn_m16n8k8_matrixB, ax1_0 * 8 + 16, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, threadIdx_y * 64 + ax1_0 * 32 + 1024, 1024, 1), threadIdx_x % 8 * 128 + threadIdx_x // 8 * 8)
            for ax1_0_3, ax0_0_4 in T.grid(8, 8):
                cse_var_5: T.int32 = ax1_0_3 * 2
                T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_4 * 4, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_5, Y_reindex_m16n8k8_matrixC, ax0_0_4 * 16 + cse_var_5, T.bool(False))
            for ax1_0_3, ax0_0_4 in T.grid(8, 8):
                cse_var_6: T.int32 = ax1_0_3 * 2
                T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_reindex_shared_dyn_m16n8k8_matrixA, ax0_0_4 * 4 + 32, B_reindex_shared_dyn_m16n8k8_matrixB, cse_var_6 + 16, Y_reindex_m16n8k8_matrixC, ax0_0_4 * 16 + cse_var_6, T.bool(False))
        Y_reindex_m16n8k8_matrixC_shared_dyn = T.decl_buffer((1024,), "float16", scope="shared.dyn")
        for ax0_0 in range(16):
            A_reindex_shared_dyn_1 = T.Buffer((1024,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
            for ax1_0 in range(8):
                A_reindex_shared_dyn_1[threadIdx_y * 512 + ax1_0 * 64 + threadIdx_x * 2:threadIdx_y * 512 + ax1_0 * 64 + threadIdx_x * 2 + 2] = Y_reindex_m16n8k8_matrixC_2[ax0_0 // 2 * 16 + ax1_0 * 2 + ax0_0 % 2]
            for ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 in range(16):
                Y_1 = T.Buffer((16777216,), "float16", data=Y.data)
                Y_1[blockIdx_x // 2 * 8388608 + blockIdx_y // 16 * 524288 + ax0_0 * 32768 + threadIdx_y * 16384 + threadIdx_x // 8 * 4096 + blockIdx_x % 2 * 2048 + blockIdx_y % 16 * 128 + ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 * 8 + threadIdx_x % 8] = A_reindex_shared_dyn_1[ax0_0_2_ax1_0_2_fused_cache_ax1_0_cache_ax0_1_cache_ax1_1_cache_fused_0 * 64 + threadIdx_y * 32 + threadIdx_x]
