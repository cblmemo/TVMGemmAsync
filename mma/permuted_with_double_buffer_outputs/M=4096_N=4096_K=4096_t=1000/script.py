# from tvm.script import ir as I
# from tvm.script import tir as T

@I.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer((4096, 4096), "float16"), B: T.Buffer((4096, 4096), "float16"), Y: T.Buffer((4096, 4096), "float16")):
        T.func_attr({"global_symbol": "main", "tir.noalias": T.bool(True)})
        # with T.block("root"):
        Y_reindex_m16n8k8_matrixC = T.alloc_buffer((4096, 4096), "float16", scope="m16n8k8.matrixC")
        A_reindex_shared_dyn = T.alloc_buffer((4096, 4096), "float16", scope="shared.dyn")
        B_reindex_shared_dyn = T.alloc_buffer((4096, 4096), "float16", scope="shared.dyn")
        A_reindex_shared_dyn_m16n8k8_matrixA = T.alloc_buffer((4096, 4096), "float16", scope="m16n8k8.matrixA")
        B_reindex_shared_dyn_m16n8k8_matrixB = T.alloc_buffer((4096, 4096), "float16", scope="m16n8k8.matrixB")
        for ax0_0_0_ax1_0_0_fused in T.thread_binding(4, thread="blockIdx.x"):
            for ax0_0_1_ax1_0_1_fused in T.thread_binding(64, thread="blockIdx.y"):
                for ax0_0_2_ax1_0_2_fused in T.thread_binding(8, thread="threadIdx.y"):
                    for ax0_0_3_init, ax1_0_3_init, ax0_0_4_init, ax1_0_4_init in T.grid(2, 2, 2, 8):
                        with T.block("Y_o_init"):
                            v0_o = T.axis.spatial(256, ax0_0_1_ax1_0_1_fused // 4 * 16 + ax0_0_2_ax1_0_2_fused // 2 * 4 + ax0_0_3_init * 2 + ax0_0_4_init)
                            v1_o = T.axis.spatial(512, ax0_0_0_ax1_0_0_fused * 128 + ax0_0_1_ax1_0_1_fused % 4 * 32 + ax0_0_2_ax1_0_2_fused % 2 * 16 + ax1_0_3_init * 8 + ax1_0_4_init)
                            T.reads()
                            T.writes(Y_reindex_m16n8k8_matrixC[v0_o * 16:v0_o * 16 + 16, v1_o * 8:v1_o * 8 + 8])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "warp_execution": 1})
                            dst = T.match_buffer(Y_reindex_m16n8k8_matrixC[v0_o * 16:v0_o * 16 + 16, v1_o * 8:v1_o * 8 + 8], (16, 8), "float16", scope="m16n8k8.matrixC", offset_factor=1)
                            tx = T.launch_thread("threadIdx.x", 32)
                            for b in range(2):
                                for i in T.vectorized(2):
                                    dst[b * 8 + tx // 4, tx % 4 * 2 + i] = T.float16(0)
                    for ax2_0_0 in T.serial(256, annotations={"software_pipeline_order": [0, 3, 1, 4, 5, 2, 6], "software_pipeline_stage": [0, 0, 0, 0, 0, 1, 1]}):
                        with T.block("A_reindex_shared.dyn"):
                            v0, v1 = T.axis.remap("SS", [ax0_0_1_ax1_0_1_fused, ax2_0_0])
                            T.reads(A[v0 // 4 * 256:v0 // 4 * 256 + 256, v1 * 16:v1 * 16 + 16])
                            T.writes(A_reindex_shared_dyn[v0 // 4 * 256:v0 // 4 * 256 + 256, v1 * 16:v1 * 16 + 16])
                            T.block_attr({"auto_copy": 1, "buffer_dim_align": [[0, 0, 32, 8]], "double_buffer_scope": 0, "local_stage": 1, "permuted_layout": "g2s_A", "vector_bytes": 16})
                            for ax0, ax1 in T.grid(256, 16):
                                A_reindex_shared_dyn[v0 // 4 * 256 + ax0, v1 * 16 + ax1] = A[v0 // 4 * 256 + ax0, v1 * 16 + ax1]
                        with T.block("B_reindex_shared.dyn"):
                            v0, v1, v2 = T.axis.remap("SSS", [ax2_0_0, ax0_0_0_ax1_0_0_fused, ax0_0_1_ax1_0_1_fused])
                            T.reads(B[v0 * 16:v0 * 16 + 16, v1 * 1024 + v2 % 4 * 256:v1 * 1024 + v2 % 4 * 256 + 256])
                            T.writes(B_reindex_shared_dyn[v0 * 16:v0 * 16 + 16, v1 * 1024 + v2 % 4 * 256:v1 * 1024 + v2 % 4 * 256 + 256])
                            T.block_attr({"auto_copy": 1, "buffer_dim_align": [[0, 0, 32, 8]], "double_buffer_scope": 0, "local_stage": 1, "permuted_layout": "g2s_B", "vector_bytes": 16})
                            for ax0, ax1 in T.grid(16, 256):
                                B_reindex_shared_dyn[v0 * 16 + ax0, v1 * 1024 + v2 % 4 * 256 + ax1] = B[v0 * 16 + ax0, v1 * 1024 + v2 % 4 * 256 + ax1]
                        for ax2_0_1 in T.serial(2, annotations={"software_pipeline_order": [0, 1, 2], "software_pipeline_stage": [0, 0, 1]}):
                            for ax0_0, ax1_0 in T.grid(2, 1):
                                with T.block("A_reindex_shared.dyn_m16n8k8.matrixA_o"):
                                    v0_o = T.axis.spatial(128, ax0_0_1_ax1_0_1_fused // 4 * 8 + ax0_0_2_ax1_0_2_fused // 2 * 2 + ax0_0)
                                    v1_o = T.axis.spatial(512, ax2_0_0 * 2 + ax2_0_1 + ax1_0)
                                    T.reads(A_reindex_shared_dyn[v0_o * 32:v0_o * 32 + 32, v1_o * 8:v1_o * 8 + 8])
                                    T.writes(A_reindex_shared_dyn_m16n8k8_matrixA[v0_o * 32:v0_o * 32 + 32, v1_o * 8:v1_o * 8 + 8])
                                    T.block_attr({"permuted_layout": "s2l_A"})
                                    src = T.match_buffer(A_reindex_shared_dyn[v0_o * 32:v0_o * 32 + 32, v1_o * 8:v1_o * 8 + 8], (32, 8), "float16", strides=("src_s0", "src_s1"), scope="shared.dyn", offset_factor=1)
                                    dst = T.match_buffer(A_reindex_shared_dyn_m16n8k8_matrixA[v0_o * 32:v0_o * 32 + 32, v1_o * 8:v1_o * 8 + 8], (32, 8), "float16", strides=("dst_s0", "dst_s1"), scope="m16n8k8.matrixA", offset_factor=1)
                                    tx = T.launch_thread("threadIdx.x", 32)
                                    T.ptx_ldmatrix("float16", T.bool(False), 4, ".b16", dst.data, (dst.elem_offset // dst.strides[0] // 32 * (dst.strides[0] // 8) + dst.elem_offset % dst.strides[0] // 8) * 8 + dst.elem_offset // dst.strides[0] % 32 // 16 * 4, T.tvm_access_ptr(T.type_annotation("float16"), src.data, src.elem_offset, src.strides[0] * 32, 1), tx * src.strides[0])
                            for ax0_0, ax1_0 in T.grid(1, 4):
                                with T.block("B_reindex_shared.dyn_m16n8k8.matrixB_o"):
                                    v0_o = T.axis.spatial(512, ax2_0_0 * 2 + ax2_0_1 + ax0_0)
                                    v1_o = T.axis.spatial(128, ax0_0_0_ax1_0_0_fused * 32 + ax0_0_1_ax1_0_1_fused % 4 * 8 + ax0_0_2_ax1_0_2_fused % 2 * 4 + ax1_0)
                                    T.reads(B_reindex_shared_dyn[v0_o * 8:v0_o * 8 + 8, v1_o * 32:v1_o * 32 + 32])
                                    T.writes(B_reindex_shared_dyn_m16n8k8_matrixB[v0_o * 8:v0_o * 8 + 8, v1_o * 32:v1_o * 32 + 32])
                                    T.block_attr({"permuted_layout": "s2l_B"})
                                    src = T.match_buffer(B_reindex_shared_dyn[v0_o * 8:v0_o * 8 + 8, v1_o * 32:v1_o * 32 + 32], (8, 32), "float16", strides=("src_s0", "src_s1"), scope="shared.dyn", offset_factor=1)
                                    dst = T.match_buffer(B_reindex_shared_dyn_m16n8k8_matrixB[v0_o * 8:v0_o * 8 + 8, v1_o * 32:v1_o * 32 + 32], (8, 32), "float16", strides=("dst_s0", "dst_s1"), scope="m16n8k8.matrixB", offset_factor=1)
                                    tx = T.launch_thread("threadIdx.x", 32)
                                    T.ptx_ldmatrix("float16", T.bool(True), 4, ".b16", dst.data, (dst.elem_offset // dst.strides[0] // 8 * (dst.strides[0] // 32) + dst.elem_offset % dst.strides[0] // 32) * 8 + dst.elem_offset % dst.strides[0] % 32 // 8 * 2, T.tvm_access_ptr(T.type_annotation("float16"), src.data, src.elem_offset, src.strides[0] * 8, 1), src.strides[0] * (tx % 8) + 8 * (tx // 8))
                            for ax0_0_3, ax1_0_3, ax2_0_2, ax0_0_4, ax1_0_4 in T.grid(2, 2, 1, 2, 8):
                                with T.block("Y_o_update"):
                                    v0_o = T.axis.spatial(256, ax0_0_1_ax1_0_1_fused // 4 * 16 + ax0_0_2_ax1_0_2_fused // 2 * 4 + ax0_0_3 * 2 + ax0_0_4)
                                    v1_o = T.axis.spatial(512, ax0_0_0_ax1_0_0_fused * 128 + ax0_0_1_ax1_0_1_fused % 4 * 32 + ax0_0_2_ax1_0_2_fused % 2 * 16 + ax1_0_3 * 8 + ax1_0_4)
                                    v2_o = T.axis.reduce(512, ax2_0_0 * 2 + ax2_0_1 + ax2_0_2)
                                    T.reads(Y_reindex_m16n8k8_matrixC[v0_o * 16:v0_o * 16 + 16, v1_o * 8:v1_o * 8 + 8], A_reindex_shared_dyn_m16n8k8_matrixA[v0_o * 16:v0_o * 16 + 16, v2_o * 8:v2_o * 8 + 8], B_reindex_shared_dyn_m16n8k8_matrixB[v2_o * 8:v2_o * 8 + 8, v1_o * 8:v1_o * 8 + 8])
                                    T.writes(Y_reindex_m16n8k8_matrixC[v0_o * 16:v0_o * 16 + 16, v1_o * 8:v1_o * 8 + 8])
                                    T.block_attr({"meta_schedule.thread_extent_high_inclusive": 1024, "meta_schedule.thread_extent_low_inclusive": 32, "warp_execution": 1})
                                    A_1 = T.match_buffer(A_reindex_shared_dyn_m16n8k8_matrixA[v0_o * 16:v0_o * 16 + 16, v2_o * 8:v2_o * 8 + 8], (16, 8), "float16", strides=("A_s0", "A_s1"), scope="m16n8k8.matrixA", offset_factor=1)
                                    B_1 = T.match_buffer(B_reindex_shared_dyn_m16n8k8_matrixB[v2_o * 8:v2_o * 8 + 8, v1_o * 8:v1_o * 8 + 8], (8, 8), "float16", strides=("B_s0", "B_s1"), scope="m16n8k8.matrixB", offset_factor=1)
                                    C = T.match_buffer(Y_reindex_m16n8k8_matrixC[v0_o * 16:v0_o * 16 + 16, v1_o * 8:v1_o * 8 + 8], (16, 8), "float16", strides=("C_s0", "C_s1"), scope="m16n8k8.matrixC", offset_factor=1)
                                    T.ptx_mma("float16", "m16n8k8", "row", "col", "fp16", "fp16", "fp16", A_1.data, (A_1.elem_offset // A_1.strides[0] // 32 * (A_1.strides[0] // 8) + A_1.elem_offset % A_1.strides[0] // 8) * 8 + A_1.elem_offset // A_1.strides[0] % 32 // 16 * 4, B_1.data, (B_1.elem_offset // B_1.strides[0] // 8 * (B_1.strides[0] // 32) + B_1.elem_offset % B_1.strides[0] // 32) * 8 + B_1.elem_offset % B_1.strides[0] % 32 // 8 * 2, C.data, C.elem_offset // C.strides[0] // 8 // 2 * 2 * (C.strides[0] // 8) + C.elem_offset // C.strides[0] // 8 % 2 + C.elem_offset % C.strides[0] // 8 * 2, T.bool(False))
                    with T.block("Y_reindex_m16n8k8.matrixC"):
                        v0, v1, v2 = T.axis.remap("SSS", [ax0_0_1_ax1_0_1_fused, ax0_0_2_ax1_0_2_fused, ax0_0_0_ax1_0_0_fused])
                        T.reads(Y_reindex_m16n8k8_matrixC[v0 // 4 * 256 + v1 // 2 * 64:v0 // 4 * 256 + v1 // 2 * 64 + 64, v2 * 1024 + v0 % 4 * 256 + v1 % 2 * 128:v2 * 1024 + v0 % 4 * 256 + v1 % 2 * 128 + 128])
                        T.writes(Y[v0 // 4 * 256 + v1 // 2 * 64:v0 // 4 * 256 + v1 // 2 * 64 + 64, v2 * 1024 + v0 % 4 * 256 + v1 % 2 * 128:v2 * 1024 + v0 % 4 * 256 + v1 % 2 * 128 + 128])
                        T.block_attr({"auto_copy": 1})
                        for ax0, ax1 in T.grid(64, 128):
                            Y[v0 // 4 * 256 + v1 // 2 * 64 + ax0, v2 * 1024 + v0 % 4 * 256 + v1 % 2 * 128 + ax1] = Y_reindex_m16n8k8_matrixC[v0 // 4 * 256 + v1 // 2 * 64 + ax0, v2 * 1024 + v0 % 4 * 256 + v1 % 2 * 128 + ax1]
