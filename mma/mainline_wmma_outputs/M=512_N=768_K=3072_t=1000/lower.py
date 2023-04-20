# from tvm.script import ir as I
# from tvm.script import tir as T

@I.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer((512, 3072), "float16"), B: T.Buffer((3072, 768), "float16"), Y: T.Buffer((512, 768), "float16")):
        T.func_attr({"global_symbol": "main", "tir.noalias": T.bool(True)})
        blockIdx_y = T.launch_thread("blockIdx.y", 12)
        Y_reindex_shared_dyn_wmma_accumulator = T.allocate([512], "float16", "wmma.accumulator")
        A_reindex_shared_dyn = T.allocate([4608], "float16", "shared.dyn")
        B_reindex_shared_dyn = T.allocate([4608], "float16", "shared.dyn")
        A_reindex_shared_dyn_wmma_matrix_a = T.allocate([2048], "float16", "wmma.matrix_a")
        B_reindex_shared_dyn_wmma_matrix_b = T.allocate([1024], "float16", "wmma.matrix_b")
        blockIdx_x = T.launch_thread("blockIdx.x", 8)
        threadIdx_y = T.launch_thread("threadIdx.y", 8)
        threadIdx_x = T.launch_thread("threadIdx.x", 32)
        for ax0_0_4_init in range(2):
            T.tvm_fill_fragment(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, ax0_0_4_init, T.float32(0))
        for ax2_0_0 in range(48):
            A_reindex_shared_dyn_1 = T.decl_buffer((64, 64), "float16", data=A_reindex_shared_dyn, strides=(72, 1), scope="shared.dyn")
            B_reindex_shared_dyn_1 = T.decl_buffer((64, 64), "float16", data=B_reindex_shared_dyn, strides=(72, 1), scope="shared.dyn")
            for ax0_ax1_fused_0 in range(4):
                A_reindex_shared_dyn_2 = T.Buffer((4608,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
                A_1 = T.Buffer((1572864,), "float16", data=A.data)
                A_reindex_shared_dyn_2[ax0_ax1_fused_0 * 1152 + threadIdx_y * 144 + threadIdx_x // 16 * 72 + threadIdx_x % 16 * 4:ax0_ax1_fused_0 * 1152 + threadIdx_y * 144 + threadIdx_x // 16 * 72 + threadIdx_x % 16 * 4 + 4] = A_1[blockIdx_y // 6 * 786432 + blockIdx_x // 2 * 196608 + ax0_ax1_fused_0 * 49152 + threadIdx_y * 6144 + threadIdx_x // 16 * 3072 + ax2_0_0 * 64 + threadIdx_x % 16 * 4:blockIdx_y // 6 * 786432 + blockIdx_x // 2 * 196608 + ax0_ax1_fused_0 * 49152 + threadIdx_y * 6144 + threadIdx_x // 16 * 3072 + ax2_0_0 * 64 + threadIdx_x % 16 * 4 + 4]
            for ax0_ax1_fused_0 in range(4):
                B_reindex_shared_dyn_2 = T.Buffer((4608,), "float16", data=B_reindex_shared_dyn, scope="shared.dyn")
                B_1 = T.Buffer((2359296,), "float16", data=B.data)
                B_reindex_shared_dyn_2[ax0_ax1_fused_0 * 1152 + threadIdx_y * 144 + threadIdx_x // 16 * 72 + threadIdx_x % 16 * 4:ax0_ax1_fused_0 * 1152 + threadIdx_y * 144 + threadIdx_x // 16 * 72 + threadIdx_x % 16 * 4 + 4] = B_1[ax2_0_0 * 49152 + ax0_ax1_fused_0 * 12288 + threadIdx_y * 1536 + threadIdx_x // 16 * 768 + blockIdx_y % 6 * 128 + blockIdx_x % 2 * 64 + threadIdx_x % 16 * 4:ax2_0_0 * 49152 + ax0_ax1_fused_0 * 12288 + threadIdx_y * 1536 + threadIdx_x // 16 * 768 + blockIdx_y % 6 * 128 + blockIdx_x % 2 * 64 + threadIdx_x % 16 * 4 + 4]
            for ax0_0, ax1_0 in T.grid(2, 4):
                T.tvm_load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a, 16, 16, 16, ax0_0 * 4 + ax1_0, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y // 4 * 2304 + ax0_0 * 1152 + ax1_0 * 16, 1152, 1), 72, "row_major")
            for ax0_0 in range(4):
                T.tvm_load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b, 16, 16, 16, ax0_0, T.tvm_access_ptr(T.type_annotation("float16"), B_reindex_shared_dyn, ax0_0 * 1152 + threadIdx_y % 4 * 16, 1152, 1), 72, "row_major")
            for ax2_0_2, ax0_0_4 in T.grid(4, 2):
                T.tvm_mma_sync(Y_reindex_shared_dyn_wmma_accumulator, ax0_0_4, A_reindex_shared_dyn_wmma_matrix_a, ax0_0_4 * 4 + ax2_0_2, B_reindex_shared_dyn_wmma_matrix_b, ax2_0_2, Y_reindex_shared_dyn_wmma_accumulator, ax0_0_4)
        for ax2 in range(2):
            T.tvm_store_matrix_sync(Y_reindex_shared_dyn_wmma_accumulator, 16, 16, 16, ax2, T.tvm_access_ptr(T.type_annotation("float16"), A_reindex_shared_dyn, threadIdx_y * 256, 256, 2), 16, "row_major")
            for ax0_ax1_ax3_ax4_ax5_fused_0 in range(2):
                Y_1 = T.Buffer((393216,), "float16", data=Y.data)
                A_reindex_shared_dyn_1 = T.Buffer((2048,), "float16", data=A_reindex_shared_dyn, scope="shared.dyn")
                Y_1[blockIdx_y // 6 * 196608 + blockIdx_x // 2 * 49152 + ax0_ax1_ax3_ax4_ax5_fused_0 * 24576 + ax2 * 12288 + threadIdx_y % 2 * 6144 + threadIdx_x // 4 * 768 + blockIdx_y % 6 * 128 + blockIdx_x % 2 * 64 + threadIdx_y // 2 * 16 + threadIdx_x % 4 * 4:blockIdx_y // 6 * 196608 + blockIdx_x // 2 * 49152 + ax0_ax1_ax3_ax4_ax5_fused_0 * 24576 + ax2 * 12288 + threadIdx_y % 2 * 6144 + threadIdx_x // 4 * 768 + blockIdx_y % 6 * 128 + blockIdx_x % 2 * 64 + threadIdx_y // 2 * 16 + threadIdx_x % 4 * 4 + 4] = A_reindex_shared_dyn_1[ax0_ax1_ax3_ax4_ax5_fused_0 * 1024 + threadIdx_y * 128 + threadIdx_x * 4:ax0_ax1_ax3_ax4_ax5_fused_0 * 1024 + threadIdx_y * 128 + threadIdx_x * 4 + 4]
