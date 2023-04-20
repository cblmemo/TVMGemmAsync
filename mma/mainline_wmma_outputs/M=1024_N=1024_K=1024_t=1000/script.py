# from tvm.script import ir as I
# from tvm.script import tir as T

@I.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer((1024, 1024), "float16"), B: T.Buffer((1024, 1024), "float16"), Y: T.Buffer((1024, 1024), "float16")):
        T.func_attr({"global_symbol": "main", "tir.noalias": T.bool(True)})
        # with T.block("root"):
        Y_reindex_shared_dyn = T.alloc_buffer((16, 64, 4, 1, 16, 16), "float16", scope="shared.dyn")
        Y_reindex_shared_dyn_wmma_accumulator = T.alloc_buffer((16, 64, 4, 1, 16, 16), "float16", scope="wmma.accumulator")
        A_reindex_shared_dyn = T.alloc_buffer((1024, 1024), "float16", scope="shared.dyn")
        B_reindex_shared_dyn = T.alloc_buffer((1024, 1024), "float16", scope="shared.dyn")
        A_reindex_shared_dyn_wmma_matrix_a = T.alloc_buffer((1024, 1024), "float16", scope="wmma.matrix_a")
        B_reindex_shared_dyn_wmma_matrix_b = T.alloc_buffer((1024, 1024), "float16", scope="wmma.matrix_b")
        for ax0_0_0_ax1_0_0_fused in T.thread_binding(8, thread="blockIdx.y"):
            for ax0_0_1_ax1_0_1_fused in T.thread_binding(16, thread="blockIdx.x"):
                for ax0_0_2_ax1_0_2_fused in T.thread_binding(8, thread="threadIdx.y"):
                    for ax0_0_3_init, ax1_0_3_init, ax0_0_4_init, ax1_0_4_init in T.grid(4, 1, 1, 1):
                        with T.block("Y_o_init"):
                            v0_o = T.axis.spatial(64, ax0_0_0_ax1_0_0_fused // 2 * 16 + ax0_0_1_ax1_0_1_fused // 4 * 4 + ax0_0_3_init + ax0_0_4_init)
                            v1_o = T.axis.spatial(64, ax0_0_0_ax1_0_0_fused % 2 * 32 + ax0_0_1_ax1_0_1_fused % 4 * 8 + ax0_0_2_ax1_0_2_fused + ax1_0_3_init + ax1_0_4_init)
                            T.reads()
                            T.writes(Y_reindex_shared_dyn_wmma_accumulator[v0_o // 4, v1_o, v0_o % 4, 0, 0:16, 0:16])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "warp_execution": 1})
                            C = T.match_buffer(Y_reindex_shared_dyn_wmma_accumulator[v0_o // 4, v1_o, v0_o % 4, 0, 0:16, 0:16], (16, 16), "float16", strides=("C_s0", "C_s1"), scope="wmma.accumulator", offset_factor=16)
                            T.tvm_fill_fragment(C.data, 16, 16, 16, C.elem_offset // C.strides[0] // 16 * (C.strides[0] // 16) + C.elem_offset % C.strides[0] // 16, T.float32(0))
                    for ax2_0_0 in range(32):
                        for ax0_ax1_fused_0 in range(2):
                            for ax0_ax1_fused_1 in T.thread_binding(8, thread="threadIdx.y"):
                                for ax0_ax1_fused_2 in T.thread_binding(32, thread="threadIdx.x"):
                                    for ax0_ax1_fused_3 in T.vectorized(4):
                                        with T.block("A_reindex_shared.dyn"):
                                            v0 = T.axis.spatial(1024, ax0_0_0_ax1_0_0_fused // 2 * 256 + ax0_0_1_ax1_0_1_fused // 4 * 64 + (ax0_ax1_fused_0 * 1024 + ax0_ax1_fused_1 * 128 + ax0_ax1_fused_2 * 4 + ax0_ax1_fused_3) // 32)
                                            v1 = T.axis.spatial(1024, ax2_0_0 * 32 + (ax0_ax1_fused_0 * 1024 + ax0_ax1_fused_1 * 128 + ax0_ax1_fused_2 * 4 + ax0_ax1_fused_3) % 32)
                                            T.reads(A[v0, v1])
                                            T.writes(A_reindex_shared_dyn[v0, v1])
                                            T.block_attr({"buffer_dim_align": [[0, 0, 32, 8]]})
                                            A_reindex_shared_dyn[v0, v1] = A[v0, v1]
                        for ax0_ax1_fused_0 in range(4):
                            for ax0_ax1_fused_1 in T.thread_binding(8, thread="threadIdx.y"):
                                for ax0_ax1_fused_2 in T.thread_binding(32, thread="threadIdx.x"):
                                    for ax0_ax1_fused_3 in T.vectorized(4):
                                        with T.block("B_reindex_shared.dyn"):
                                            v0 = T.axis.spatial(1024, ax2_0_0 * 32 + (ax0_ax1_fused_0 * 1024 + ax0_ax1_fused_1 * 128 + ax0_ax1_fused_2 * 4 + ax0_ax1_fused_3) // 128)
                                            v1 = T.axis.spatial(1024, ax0_0_0_ax1_0_0_fused % 2 * 512 + ax0_0_1_ax1_0_1_fused % 4 * 128 + (ax0_ax1_fused_0 * 1024 + ax0_ax1_fused_1 * 128 + ax0_ax1_fused_2 * 4 + ax0_ax1_fused_3) % 128)
                                            T.reads(B[v0, v1])
                                            T.writes(B_reindex_shared_dyn[v0, v1])
                                            T.block_attr({"buffer_dim_align": [[0, 0, 32, 8]]})
                                            B_reindex_shared_dyn[v0, v1] = B[v0, v1]
                        for ax2_0_1 in range(1):
                            for ax0_0, ax1_0 in T.grid(4, 2):
                                with T.block("A_reindex_shared.dyn_wmma.matrix_a_o"):
                                    v0_o = T.axis.spatial(64, ax0_0_0_ax1_0_0_fused // 2 * 16 + ax0_0_1_ax1_0_1_fused // 4 * 4 + ax0_0)
                                    v1_o = T.axis.spatial(64, ax2_0_0 * 2 + ax1_0)
                                    T.reads(A_reindex_shared_dyn[v0_o * 16:v0_o * 16 + 16, v1_o * 16:v1_o * 16 + 16])
                                    T.writes(A_reindex_shared_dyn_wmma_matrix_a[v0_o * 16:v0_o * 16 + 16, v1_o * 16:v1_o * 16 + 16])
                                    A_1 = T.match_buffer(A_reindex_shared_dyn[v0_o * 16:v0_o * 16 + 16, v1_o * 16:v1_o * 16 + 16], (16, 16), "float16", strides=("A_s0", "A_s1"), scope="shared.dyn", offset_factor=16)
                                    C = T.match_buffer(A_reindex_shared_dyn_wmma_matrix_a[v0_o * 16:v0_o * 16 + 16, v1_o * 16:v1_o * 16 + 16], (16, 16), "float16", strides=("C_s0", "C_s1"), scope="wmma.matrix_a", offset_factor=16)
                                    T.tvm_load_matrix_sync(C.data, 16, 16, 16, C.elem_offset // C.strides[0] // 16 * (C.strides[0] // 16) + C.elem_offset % C.strides[0] // 16, T.tvm_access_ptr(T.type_annotation("float16"), A_1.data, A_1.elem_offset, A_1.strides[0] * 16, 1), A_1.strides[0], "row_major")
                            for ax0_0, ax1_0 in T.grid(2, 1):
                                with T.block("B_reindex_shared.dyn_wmma.matrix_b_o"):
                                    v0_o = T.axis.spatial(64, ax2_0_0 * 2 + ax0_0)
                                    v1_o = T.axis.spatial(64, ax0_0_0_ax1_0_0_fused % 2 * 32 + ax0_0_1_ax1_0_1_fused % 4 * 8 + ax0_0_2_ax1_0_2_fused + ax1_0)
                                    T.reads(B_reindex_shared_dyn[v0_o * 16:v0_o * 16 + 16, v1_o * 16:v1_o * 16 + 16])
                                    T.writes(B_reindex_shared_dyn_wmma_matrix_b[v0_o * 16:v0_o * 16 + 16, v1_o * 16:v1_o * 16 + 16])
                                    A_1 = T.match_buffer(B_reindex_shared_dyn[v0_o * 16:v0_o * 16 + 16, v1_o * 16:v1_o * 16 + 16], (16, 16), "float16", strides=("A_s0", "A_s1"), scope="shared.dyn", offset_factor=16)
                                    C = T.match_buffer(B_reindex_shared_dyn_wmma_matrix_b[v0_o * 16:v0_o * 16 + 16, v1_o * 16:v1_o * 16 + 16], (16, 16), "float16", strides=("C_s0", "C_s1"), scope="wmma.matrix_b", offset_factor=16)
                                    T.tvm_load_matrix_sync(C.data, 16, 16, 16, C.elem_offset // C.strides[0] // 16 * (C.strides[0] // 16) + C.elem_offset % C.strides[0] // 16, T.tvm_access_ptr(T.type_annotation("float16"), A_1.data, A_1.elem_offset, A_1.strides[0] * 16, 1), A_1.strides[0], "row_major")
                            for ax0_0_3, ax1_0_3, ax2_0_2, ax0_0_4, ax1_0_4 in T.grid(4, 1, 2, 1, 1):
                                with T.block("Y_o_update"):
                                    v0_o = T.axis.spatial(64, ax0_0_0_ax1_0_0_fused // 2 * 16 + ax0_0_1_ax1_0_1_fused // 4 * 4 + ax0_0_3 + ax0_0_4)
                                    v1_o = T.axis.spatial(64, ax0_0_0_ax1_0_0_fused % 2 * 32 + ax0_0_1_ax1_0_1_fused % 4 * 8 + ax0_0_2_ax1_0_2_fused + ax1_0_3 + ax1_0_4)
                                    v2_o = T.axis.reduce(64, ax2_0_0 * 2 + ax2_0_1 * 2 + ax2_0_2)
                                    T.reads(Y_reindex_shared_dyn_wmma_accumulator[v0_o // 4, v1_o, v0_o % 4, 0, 0:16, 0:16], A_reindex_shared_dyn_wmma_matrix_a[v0_o * 16:v0_o * 16 + 16, v2_o * 16:v2_o * 16 + 16], B_reindex_shared_dyn_wmma_matrix_b[v2_o * 16:v2_o * 16 + 16, v1_o * 16:v1_o * 16 + 16])
                                    T.writes(Y_reindex_shared_dyn_wmma_accumulator[v0_o // 4, v1_o, v0_o % 4, 0, 0:16, 0:16])
                                    T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "warp_execution": 1})
                                    A_1 = T.match_buffer(A_reindex_shared_dyn_wmma_matrix_a[v0_o * 16:v0_o * 16 + 16, v2_o * 16:v2_o * 16 + 16], (16, 16), "float16", strides=("A_s0", "A_s1"), scope="wmma.matrix_a", offset_factor=16)
                                    B_1 = T.match_buffer(B_reindex_shared_dyn_wmma_matrix_b[v2_o * 16:v2_o * 16 + 16, v1_o * 16:v1_o * 16 + 16], (16, 16), "float16", strides=("B_s0", "B_s1"), scope="wmma.matrix_b", offset_factor=16)
                                    C = T.match_buffer(Y_reindex_shared_dyn_wmma_accumulator[v0_o // 4, v1_o, v0_o % 4, 0, 0:16, 0:16], (16, 16), "float16", strides=("C_s0", "C_s1"), scope="wmma.accumulator", offset_factor=16)
                                    T.tvm_mma_sync(C.data, C.elem_offset // C.strides[0] // 16 * (C.strides[0] // 16) + C.elem_offset % C.strides[0] // 16, A_1.data, A_1.elem_offset // A_1.strides[0] // 16 * (A_1.strides[0] // 16) + A_1.elem_offset % A_1.strides[0] // 16, B_1.data, B_1.elem_offset // B_1.strides[0] // 16 * (B_1.strides[0] // 16) + B_1.elem_offset % B_1.strides[0] // 16, C.data, C.elem_offset // C.strides[0] // 16 * (C.strides[0] // 16) + C.elem_offset % C.strides[0] // 16)
                for ax2 in range(4):
                    for ax0_ax1_fused in T.thread_binding(8, thread="threadIdx.y"):
                        for ax2_1, ax3 in T.grid(1, 1):
                            with T.block("Y_reindex_shared.dyn_wmma.accumulator_o"):
                                v0 = T.axis.spatial(16, ax0_0_0_ax1_0_0_fused // 2 * 4 + ax0_0_1_ax1_0_1_fused // 4)
                                v1 = T.axis.spatial(64, ax0_0_0_ax1_0_0_fused % 2 * 32 + ax0_0_1_ax1_0_1_fused % 4 * 8 + ax0_ax1_fused)
                                v2 = T.axis.spatial(4, ax2 + ax2_1)
                                v3 = T.axis.spatial(1, ax3)
                                v4_o = T.axis.spatial(1, 0)
                                v5_o = T.axis.spatial(1, 0)
                                T.reads(Y_reindex_shared_dyn_wmma_accumulator[v0, v1, v2, v3, 0:16, 0:16])
                                T.writes(Y_reindex_shared_dyn[v0, v1, v2, v3, 0:16, 0:16])
                                A_1 = T.match_buffer(Y_reindex_shared_dyn_wmma_accumulator[v0, v1, v2, v3, 0:16, 0:16], (16, 16), "float16", strides=("A_s0", "A_s1"), scope="wmma.accumulator", offset_factor=16)
                                C = T.match_buffer(Y_reindex_shared_dyn[v0, v1, v2, v3, 0:16, 0:16], (16, 16), "float16", strides=("C_s0", "C_s1"), scope="shared.dyn", offset_factor=16)
                                T.tvm_store_matrix_sync(A_1.data, 16, 16, 16, A_1.elem_offset // A_1.strides[0] // 16 * (A_1.strides[0] // 16) + A_1.elem_offset % A_1.strides[0] // 16, T.tvm_access_ptr(T.type_annotation("float16"), C.data, C.elem_offset, C.strides[0] * 16, 2), C.strides[0], "row_major")
                    for ax0_ax1_ax3_ax4_ax5_fused_0 in range(1):
                        for ax0_ax1_ax3_ax4_ax5_fused_1 in T.thread_binding(8, thread="threadIdx.y"):
                            for ax0_ax1_ax3_ax4_ax5_fused_2 in T.thread_binding(32, thread="threadIdx.x"):
                                for ax0_ax1_ax3_ax4_ax5_fused_3 in T.vectorized(8):
                                    with T.block("Y_reindex_shared.dyn"):
                                        v0 = T.axis.spatial(16, ax0_0_0_ax1_0_0_fused // 2 * 4 + ax0_0_1_ax1_0_1_fused // 4)
                                        v1 = T.axis.spatial(64, ax0_0_0_ax1_0_0_fused % 2 * 32 + ax0_0_1_ax1_0_1_fused % 4 * 8 + (ax0_ax1_ax3_ax4_ax5_fused_0 * 2048 + ax0_ax1_ax3_ax4_ax5_fused_1 * 256 + ax0_ax1_ax3_ax4_ax5_fused_2 * 8 + ax0_ax1_ax3_ax4_ax5_fused_3) // 256)
                                        v2 = T.axis.spatial(4, ax2)
                                        v3 = T.axis.spatial(1, 0)
                                        v4 = T.axis.spatial(16, (ax0_ax1_ax3_ax4_ax5_fused_0 * 2048 + ax0_ax1_ax3_ax4_ax5_fused_1 * 256 + ax0_ax1_ax3_ax4_ax5_fused_2 * 8 + ax0_ax1_ax3_ax4_ax5_fused_3) % 256 // 16)
                                        v5 = T.axis.spatial(16, (ax0_ax1_ax3_ax4_ax5_fused_0 * 2048 + ax0_ax1_ax3_ax4_ax5_fused_1 * 256 + ax0_ax1_ax3_ax4_ax5_fused_2 * 8 + ax0_ax1_ax3_ax4_ax5_fused_3) % 16)
                                        T.reads(Y_reindex_shared_dyn[v0, v1, v2, v3, v4, v5])
                                        T.writes(Y[v4 + v2 * 16 + v0 * 64, v5 + v1 * 16])
                                        Y[v4 + v2 * 16 + v0 * 64, v5 + v1 * 16] = Y_reindex_shared_dyn[v0, v1, v2, v3, v4, v5]
