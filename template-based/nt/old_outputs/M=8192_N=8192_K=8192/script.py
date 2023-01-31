# from tvm.script import tir as T
@tvm.script.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer[(8192, 8192), "float32"], B: T.Buffer[(8192, 8192), "float32"], Y: T.Buffer[(8192, 8192), "float32"]):
        # function attr dict
        T.func_attr({"global_symbol": "main", "tir.noalias": True})
        # body
        # with T.block("root")
        Y_local = T.alloc_buffer([8192, 8192], dtype="float32", scope="local")
        A_shared = T.alloc_buffer([8192, 8192], dtype="float32", scope="shared")
        B_shared = T.alloc_buffer([8192, 8192], dtype="float32", scope="shared")
        for i_0_j_0_fused in T.thread_binding(4096, thread="blockIdx.x", annotations={"pragma_auto_unroll_max_step":512, "pragma_unroll_explicit":1}):
            for i_1_j_1_fused in T.thread_binding(4, thread="vthread.x"):
                for i_2_j_2_fused in T.thread_binding(256, thread="threadIdx.x"):
                    for i_3_init, j_3_init, i_4_init, j_4_init in T.grid(1, 2, 2, 4):
                        with T.block("Y_init"):
                            v_i = T.axis.spatial(8192, i_0_j_0_fused // 128 * 256 + i_2_j_2_fused // 2 * 2 + i_3_init * 2 + i_4_init)
                            v_j = T.axis.spatial(8192, i_0_j_0_fused % 128 * 64 + i_1_j_1_fused * 16 + i_2_j_2_fused % 2 * 8 + j_3_init * 4 + j_4_init)
                            T.reads()
                            T.writes(Y_local[v_i, v_j])
                            T.block_attr({"meta_schedule.thread_extent_high_inclusive":1024, "meta_schedule.thread_extent_low_inclusive":32, "meta_schedule.tiling_structure":"SSSRRSRS"})
                            Y_local[v_i, v_j] = T.float32(0)
                    for k_0 in T.serial(256):
                        for ax0_ax1_fused_0 in T.serial(16):
                            for ax0_ax1_fused_1 in T.thread_binding(256, thread="threadIdx.x"):
                                for ax0_ax1_fused_2 in T.vectorized(2):
                                    with T.block("A_shared"):
                                        v0 = T.axis.spatial(8192, k_0 * 32 + (ax0_ax1_fused_0 * 512 + ax0_ax1_fused_1 * 2 + ax0_ax1_fused_2) // 256)
                                        v1 = T.axis.spatial(8192, i_0_j_0_fused // 128 * 256 + (ax0_ax1_fused_0 * 512 + ax0_ax1_fused_1 * 2 + ax0_ax1_fused_2) % 256)
                                        T.reads(A[v0, v1])
                                        T.writes(A_shared[v0, v1])
                                        A_shared[v0, v1] = A[v0, v1]
                        for ax0_ax1_fused_0 in T.serial(2):
                            for ax0_ax1_fused_1 in T.thread_binding(256, thread="threadIdx.x"):
                                for ax0_ax1_fused_2 in T.vectorized(4):
                                    with T.block("B_shared"):
                                        v0 = T.axis.spatial(8192, k_0 * 32 + (ax0_ax1_fused_0 * 1024 + ax0_ax1_fused_1 * 4 + ax0_ax1_fused_2) // 64)
                                        v1 = T.axis.spatial(8192, i_0_j_0_fused % 128 * 64 + (ax0_ax1_fused_0 * 1024 + ax0_ax1_fused_1 * 4 + ax0_ax1_fused_2) % 64)
                                        T.reads(B[v0, v1])
                                        T.writes(B_shared[v0, v1])
                                        B_shared[v0, v1] = B[v0, v1]
                        for k_1, i_3, j_3, k_2, i_4, j_4 in T.grid(8, 1, 2, 4, 2, 4):
                            with T.block("Y_update"):
                                v_i = T.axis.spatial(8192, i_0_j_0_fused // 128 * 256 + i_2_j_2_fused // 2 * 2 + i_3 * 2 + i_4)
                                v_j = T.axis.spatial(8192, i_0_j_0_fused % 128 * 64 + i_1_j_1_fused * 16 + i_2_j_2_fused % 2 * 8 + j_3 * 4 + j_4)
                                v_k = T.axis.reduce(8192, k_0 * 32 + k_1 * 4 + k_2)
                                T.reads(Y_local[v_i, v_j], A_shared[v_k, v_i], B_shared[v_k, v_j])
                                T.writes(Y_local[v_i, v_j])
                                T.block_attr({"meta_schedule.thread_extent_high_inclusive":1024, "meta_schedule.thread_extent_low_inclusive":32, "meta_schedule.tiling_structure":"SSSRRSRS"})
                                Y_local[v_i, v_j] = Y_local[v_i, v_j] + A_shared[v_k, v_i] * B_shared[v_k, v_j]
                    for ax0, ax1 in T.grid(2, 8):
                        with T.block("Y_local"):
                            v0 = T.axis.spatial(8192, i_0_j_0_fused // 128 * 256 + i_2_j_2_fused // 2 * 2 + ax0)
                            v1 = T.axis.spatial(8192, i_0_j_0_fused % 128 * 64 + i_1_j_1_fused * 16 + i_2_j_2_fused % 2 * 8 + ax1)
                            T.reads(Y_local[v0, v1])
                            T.writes(Y[v0, v1])
                            Y[v0, v1] = Y_local[v0, v1]
    

