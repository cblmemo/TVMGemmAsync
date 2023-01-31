# from tvm.script import tir as T
@tvm.script.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer[(800, 1472), "float32"], B: T.Buffer[(800, 1152), "float32"], Y: T.Buffer[(1472, 1152), "float32"]):
        # function attr dict
        T.func_attr({"global_symbol": "main", "tir.noalias": True})
        # body
        # with T.block("root")
        Y_local = T.alloc_buffer([1472, 1152], dtype="float32", scope="local")
        A_shared_dyn = T.alloc_buffer([800, 1472], dtype="float32", scope="shared.dyn")
        A_shared_dyn_local = T.alloc_buffer([800, 1472], dtype="float32", scope="local")
        B_shared_dyn = T.alloc_buffer([800, 1152], dtype="float32", scope="shared.dyn")
        B_shared_dyn_local = T.alloc_buffer([800, 1152], dtype="float32", scope="local")
        for i_0_j_0_fused in T.thread_binding(64, thread="blockIdx.x"):
            for j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused in T.thread_binding(276, thread="threadIdx.x"):
                for j_2_init in T.unroll(12):
                    for i_2_init in T.unroll(8):
                        with T.block("Y_init"):
                            v_i = T.axis.spatial(1472, i_0_j_0_fused // 8 * 184 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused % 92 // 4 * 8 + i_2_init)
                            v_j = T.axis.spatial(1152, i_0_j_0_fused % 8 * 144 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused // 92 * 48 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused % 4 * 12 + j_2_init)
                            T.reads()
                            T.writes(Y_local[v_i, v_j])
                            Y_local[v_i, v_j] = T.float32(0)
                for k_0 in T.serial(100, annotations={"software_pipeline_async_stages":[0, 1], "software_pipeline_order":[0, 1, 3, 2, 4], "software_pipeline_stage":[0, 0, 2, 3, 3]}):
                    for ax0_ax1_fused_0_ax0_ax1_fused_1_fused in T.thread_binding(276, thread="threadIdx.x"):
                        for ax0_ax1_fused_2 in T.serial(6):
                            with T.block("A_shared.dyn"):
                                T.where((ax0_ax1_fused_0_ax0_ax1_fused_1_fused // 12 * 12 + ax0_ax1_fused_0_ax0_ax1_fused_1_fused % 12) * 6 + ax0_ax1_fused_2 < 1472)
                                v0 = T.axis.spatial(800, k_0 * 8 + (ax0_ax1_fused_0_ax0_ax1_fused_1_fused // 12 * 72 + ax0_ax1_fused_0_ax0_ax1_fused_1_fused % 12 * 6 + ax0_ax1_fused_2) // 184)
                                v1 = T.axis.spatial(1472, i_0_j_0_fused // 8 * 184 + (ax0_ax1_fused_0_ax0_ax1_fused_1_fused // 12 * 72 + ax0_ax1_fused_0_ax0_ax1_fused_1_fused % 12 * 6 + ax0_ax1_fused_2) % 184)
                                T.reads(A[v0, v1])
                                T.writes(A_shared_dyn[v0, v1])
                                A_shared_dyn[v0, v1] = A[v0, v1]
                    for ax0_ax1_fused_0_ax0_ax1_fused_1_fused in T.thread_binding(276, thread="threadIdx.x"):
                        for ax0_ax1_fused_2 in T.serial(5):
                            with T.block("B_shared.dyn"):
                                T.where((ax0_ax1_fused_0_ax0_ax1_fused_1_fused // 12 * 12 + ax0_ax1_fused_0_ax0_ax1_fused_1_fused % 12) * 5 + ax0_ax1_fused_2 < 1152)
                                v0 = T.axis.spatial(800, k_0 * 8 + (ax0_ax1_fused_0_ax0_ax1_fused_1_fused // 12 * 60 + ax0_ax1_fused_0_ax0_ax1_fused_1_fused % 12 * 5 + ax0_ax1_fused_2) // 144)
                                v1 = T.axis.spatial(1152, i_0_j_0_fused % 8 * 144 + (ax0_ax1_fused_0_ax0_ax1_fused_1_fused // 12 * 60 + ax0_ax1_fused_0_ax0_ax1_fused_1_fused % 12 * 5 + ax0_ax1_fused_2) % 144)
                                T.reads(B[v0, v1])
                                T.writes(B_shared_dyn[v0, v1])
                                B_shared_dyn[v0, v1] = B[v0, v1]
                    for k_1 in T.unroll(8, annotations={"software_pipeline_order":[0, 1, 2], "software_pipeline_stage":[0, 0, 1]}):
                        for ax0, ax1_0 in T.grid(1, 1):
                            for ax1_1 in T.vectorized(8):
                                with T.block("A_shared.dyn_local"):
                                    v0 = T.axis.spatial(800, ax0 + k_0 * 8 + k_1)
                                    v1 = T.axis.spatial(1472, i_0_j_0_fused // 8 * 184 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused % 92 // 4 * 8 + ax1_0 * 8 + ax1_1)
                                    T.reads(A_shared_dyn[v0, v1])
                                    T.writes(A_shared_dyn_local[v0, v1])
                                    A_shared_dyn_local[v0, v1] = A_shared_dyn[v0, v1]
                        for ax0, ax1_0 in T.grid(1, 6):
                            for ax1_1 in T.vectorized(2):
                                with T.block("B_shared.dyn_local"):
                                    v0 = T.axis.spatial(800, ax0 + k_0 * 8 + k_1)
                                    v1 = T.axis.spatial(1152, i_0_j_0_fused % 8 * 144 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused // 92 * 48 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused % 4 * 12 + ax1_0 * 2 + ax1_1)
                                    T.reads(B_shared_dyn[v0, v1])
                                    T.writes(B_shared_dyn_local[v0, v1])
                                    B_shared_dyn_local[v0, v1] = B_shared_dyn[v0, v1]
                        for j_2 in T.unroll(12):
                            for i_2 in T.unroll(8):
                                with T.block("Y_update"):
                                    v_i = T.axis.spatial(1472, i_0_j_0_fused // 8 * 184 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused % 92 // 4 * 8 + i_2)
                                    v_j = T.axis.spatial(1152, i_0_j_0_fused % 8 * 144 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused // 92 * 48 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused % 4 * 12 + j_2)
                                    v_k = T.axis.reduce(800, k_0 * 8 + k_1)
                                    T.reads(Y_local[v_i, v_j], A_shared_dyn_local[v_k, v_i], B_shared_dyn_local[v_k, v_j])
                                    T.writes(Y_local[v_i, v_j])
                                    Y_local[v_i, v_j] = Y_local[v_i, v_j] + A_shared_dyn_local[v_k, v_i] * B_shared_dyn_local[v_k, v_j]
                for ax0 in T.unroll(8):
                    for ax1_0 in T.serial(3):
                        for ax1_1 in T.vectorized(4):
                            with T.block("Y_local"):
                                v0 = T.axis.spatial(1472, i_0_j_0_fused // 8 * 184 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused % 92 // 4 * 8 + ax0)
                                v1 = T.axis.spatial(1152, i_0_j_0_fused % 8 * 144 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused // 92 * 48 + j_1_0_i_1_0_fused_i_1_1_j_1_1_i_1_2_fused_fused % 4 * 12 + ax1_0 * 4 + ax1_1)
                                T.reads(Y_local[v0, v1])
                                T.writes(Y[v0, v1])
                                Y[v0, v1] = Y_local[v0, v1]
    

