# from tvm.script import tir as T
@tvm.script.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer[(1536, 1536), "float32"], B: T.Buffer[(1536, 1536), "float32"], Y: T.Buffer[(1536, 1536), "float32"]):
        # function attr dict
        T.func_attr({"global_symbol": "main", "tir.noalias": True})
        # body
        # with T.block("root")
        Y_local = T.alloc_buffer([1536, 1536], dtype="float32", scope="local")
        A_shared_dyn = T.alloc_buffer([1536, 1536], dtype="float32", scope="shared.dyn")
        A_shared_dyn_local = T.alloc_buffer([1536, 1536], dtype="float32", scope="local")
        B_shared_dyn = T.alloc_buffer([1536, 1536], dtype="float32", scope="shared.dyn")
        B_shared_dyn_local = T.alloc_buffer([1536, 1536], dtype="float32", scope="local")
        for i_0_j_0_fused in T.thread_binding(64, thread="blockIdx.x"):
            for j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused in T.thread_binding(384, thread="threadIdx.x"):
                for j_2_init in T.unroll(8):
                    for i_2_0_init in T.unroll(3):
                        for i_2_1_init in T.unroll(4):
                            with T.block("Y_init"):
                                v_i = T.axis.spatial(1536, i_0_j_0_fused // 4 * 96 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused % 128 // 32 * 24 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused % 2 * 12 + i_2_0_init * 4 + i_2_1_init)
                                v_j = T.axis.spatial(1536, i_0_j_0_fused % 4 * 384 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused // 128 * 128 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused % 32 // 2 * 8 + j_2_init)
                                T.reads()
                                T.writes(Y_local[v_i, v_j])
                                Y_local[v_i, v_j] = T.float32(0)
                for k_0 in T.serial(384, annotations={"software_pipeline_async_stages":[0, 1], "software_pipeline_order":[0, 1, 3, 2, 4], "software_pipeline_stage":[0, 0, 3, 4, 4]}):
                    for ax0_ax1_fused_0_ax0_ax1_fused_1_fused in T.thread_binding(384, thread="threadIdx.x"):
                        for ax0_ax1_fused_2 in T.vectorized(1):
                            with T.block("A_shared.dyn"):
                                v0 = T.axis.spatial(1536, i_0_j_0_fused // 4 * 96 + (ax0_ax1_fused_0_ax0_ax1_fused_1_fused // 48 * 48 + ax0_ax1_fused_0_ax0_ax1_fused_1_fused % 48 + ax0_ax1_fused_2) // 4)
                                v1 = T.axis.spatial(1536, k_0 * 4 + (ax0_ax1_fused_0_ax0_ax1_fused_1_fused // 48 * 48 + ax0_ax1_fused_0_ax0_ax1_fused_1_fused % 48 + ax0_ax1_fused_2) % 4)
                                T.reads(A[v0, v1])
                                T.writes(A_shared_dyn[v0, v1 // 32 * 32 + v1 % 8 // 4 * 16 + v1 % 32 // 8 * 4 + v1 % 4])
                                A_shared_dyn[v0, v1 // 32 * 32 + v1 % 8 // 4 * 16 + v1 % 32 // 8 * 4 + v1 % 4] = A[v0, v1]
                    for ax0_ax1_fused_0_ax0_ax1_fused_1_fused in T.thread_binding(384, thread="threadIdx.x"):
                        for ax0_ax1_fused_2 in T.vectorized(4):
                            with T.block("B_shared.dyn"):
                                v0 = T.axis.spatial(1536, k_0 * 4 + (ax0_ax1_fused_0_ax0_ax1_fused_1_fused // 48 * 192 + ax0_ax1_fused_0_ax0_ax1_fused_1_fused % 48 * 4 + ax0_ax1_fused_2) // 384)
                                v1 = T.axis.spatial(1536, i_0_j_0_fused % 4 * 384 + (ax0_ax1_fused_0_ax0_ax1_fused_1_fused // 48 * 192 + ax0_ax1_fused_0_ax0_ax1_fused_1_fused % 48 * 4 + ax0_ax1_fused_2) % 384)
                                T.reads(B[v0, v1])
                                T.writes(B_shared_dyn[v0, v1 // 64 * 64 + v1 % 8 // 4 * 32 + v1 % 64 // 8 * 4 + v1 % 4])
                                B_shared_dyn[v0, v1 // 64 * 64 + v1 % 8 // 4 * 32 + v1 % 64 // 8 * 4 + v1 % 4] = B[v0, v1]
                    for k_1 in T.unroll(4, annotations={"software_pipeline_order":[0, 1, 2], "software_pipeline_stage":[0, 0, 1]}):
                        for ax0_0 in T.serial(3):
                            for ax0_1 in T.vectorized(4):
                                for ax1 in T.serial(1):
                                    with T.block("A_shared.dyn_local"):
                                        v0 = T.axis.spatial(1536, i_0_j_0_fused // 4 * 96 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused % 128 // 32 * 24 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused % 2 * 12 + ax0_0 * 4 + ax0_1)
                                        v1 = T.axis.spatial(1536, ax1 + k_0 * 4 + k_1)
                                        T.reads(A_shared_dyn[v0, v1 // 32 * 32 + v1 % 8 // 4 * 16 + v1 % 32 // 8 * 4 + v1 % 4])
                                        T.writes(A_shared_dyn_local[v0, v1])
                                        A_shared_dyn_local[v0, v1] = A_shared_dyn[v0, v1 // 32 * 32 + v1 % 8 // 4 * 16 + v1 % 32 // 8 * 4 + v1 % 4]
                        for ax0, ax1_0 in T.grid(1, 2):
                            for ax1_1 in T.vectorized(4):
                                with T.block("B_shared.dyn_local"):
                                    v0 = T.axis.spatial(1536, ax0 + k_0 * 4 + k_1)
                                    v1 = T.axis.spatial(1536, i_0_j_0_fused % 4 * 384 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused // 128 * 128 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused % 32 // 2 * 8 + ax1_0 * 4 + ax1_1)
                                    T.reads(B_shared_dyn[v0, v1 // 64 * 64 + v1 % 8 // 4 * 32 + v1 % 64 // 8 * 4 + v1 % 4])
                                    T.writes(B_shared_dyn_local[v0, v1])
                                    B_shared_dyn_local[v0, v1] = B_shared_dyn[v0, v1 // 64 * 64 + v1 % 8 // 4 * 32 + v1 % 64 // 8 * 4 + v1 % 4]
                        for j_2 in T.unroll(8):
                            for i_2_0 in T.unroll(3):
                                for i_2_1 in T.vectorized(4):
                                    with T.block("Y_update"):
                                        v_i = T.axis.spatial(1536, i_0_j_0_fused // 4 * 96 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused % 128 // 32 * 24 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused % 2 * 12 + i_2_0 * 4 + i_2_1)
                                        v_j = T.axis.spatial(1536, i_0_j_0_fused % 4 * 384 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused // 128 * 128 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused % 32 // 2 * 8 + j_2)
                                        v_k = T.axis.reduce(1536, k_0 * 4 + k_1)
                                        T.reads(Y_local[v_i, v_j], A_shared_dyn_local[v_i, v_k], B_shared_dyn_local[v_k, v_j])
                                        T.writes(Y_local[v_i, v_j])
                                        Y_local[v_i, v_j] = Y_local[v_i, v_j] + A_shared_dyn_local[v_i, v_k] * B_shared_dyn_local[v_k, v_j]
                for ax0 in T.unroll(12):
                    for ax1_0 in T.serial(2):
                        for ax1_1 in T.vectorized(4):
                            with T.block("Y_local"):
                                v0 = T.axis.spatial(1536, i_0_j_0_fused // 4 * 96 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused % 128 // 32 * 24 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused % 2 * 12 + ax0)
                                v1 = T.axis.spatial(1536, i_0_j_0_fused % 4 * 384 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused // 128 * 128 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused % 32 // 2 * 8 + ax1_0 * 4 + ax1_1)
                                T.reads(Y_local[v0, v1])
                                T.writes(Y[v0, v1])
                                Y[v0, v1] = Y_local[v0, v1]
    

