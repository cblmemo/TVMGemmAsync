# from tvm.script import tir as T
@tvm.script.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer[(256, 512), "float32"], B: T.Buffer[(256, 384), "float32"], Y: T.Buffer[(512, 384), "float32"]):
        # function attr dict
        T.func_attr({"global_symbol": "main", "tir.noalias": True})
        # var definition
        threadIdx_x = T.env_thread("threadIdx.x")
        blockIdx_x = T.env_thread("blockIdx.x")
        # buffer definition
        A_1 = T.buffer_decl([131072], dtype="float32", data=A.data)
        B_1 = T.buffer_decl([98304], dtype="float32", data=B.data)
        Y_1 = T.buffer_decl([196608], dtype="float32", data=Y.data)
        # body
        T.launch_thread(blockIdx_x, 64)
        Y_local = T.allocate([24], "float32", "local")
        Y_local_1 = T.buffer_decl([24], dtype="float32", data=Y_local, scope="local")
        A_shared_dyn = T.allocate([2048], "float32", "shared.dyn")
        A_shared_dyn_1 = T.buffer_decl([2048], dtype="float32", data=A_shared_dyn, scope="shared.dyn")
        B_shared_dyn = T.allocate([4096], "float32", "shared.dyn")
        B_shared_dyn_1 = T.buffer_decl([4096], dtype="float32", data=B_shared_dyn, scope="shared.dyn")
        A_shared_dyn_local = T.allocate([4], "float32", "local")
        A_shared_dyn_local_1 = T.buffer_decl([4], dtype="float32", data=A_shared_dyn_local, scope="local")
        B_shared_dyn_local = T.allocate([24], "float32", "local")
        B_shared_dyn_local_1 = T.buffer_decl([24], dtype="float32", data=B_shared_dyn_local, scope="local")
        T.launch_thread(threadIdx_x, 128)
        Y_local_1[0] = T.float32(0)
        Y_local_1[12] = T.float32(0)
        Y_local_1[1] = T.float32(0)
        Y_local_1[13] = T.float32(0)
        Y_local_1[2] = T.float32(0)
        Y_local_1[14] = T.float32(0)
        Y_local_1[3] = T.float32(0)
        Y_local_1[15] = T.float32(0)
        Y_local_1[4] = T.float32(0)
        Y_local_1[16] = T.float32(0)
        Y_local_1[5] = T.float32(0)
        Y_local_1[17] = T.float32(0)
        Y_local_1[6] = T.float32(0)
        Y_local_1[18] = T.float32(0)
        Y_local_1[7] = T.float32(0)
        Y_local_1[19] = T.float32(0)
        Y_local_1[8] = T.float32(0)
        Y_local_1[20] = T.float32(0)
        Y_local_1[9] = T.float32(0)
        Y_local_1[21] = T.float32(0)
        Y_local_1[10] = T.float32(0)
        Y_local_1[22] = T.float32(0)
        Y_local_1[11] = T.float32(0)
        Y_local_1[23] = T.float32(0)
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x // 8 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 8 // 2 * 4:threadIdx_x // 8 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 8 // 2 * 4 + 4] = A_1[threadIdx_x // 16 * 512 + blockIdx_x // 8 * 64 + threadIdx_x % 16 * 4:threadIdx_x // 16 * 512 + blockIdx_x // 8 * 64 + threadIdx_x % 16 * 4 + 4]
            T.attr(0, "async_scope", 1)
            for ax0_ax1_fused_2 in T.serial(3):
                B_shared_dyn_1[threadIdx_x // 16 * 128 + (blockIdx_x % 8 * 3 + (threadIdx_x % 16 * 3 + ax0_ax1_fused_2) // 16) // 4 * 64 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 8 // 4 * 32 + (blockIdx_x % 8 * 6 + (threadIdx_x % 16 * 3 + ax0_ax1_fused_2) // 8) % 8 * 4 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 4 - blockIdx_x % 8 * 48 // 64 * 64] = B_1[threadIdx_x // 16 * 384 + blockIdx_x % 8 * 48 + threadIdx_x % 16 * 3 + ax0_ax1_fused_2]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x // 8 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 8 // 2 * 4 + 512:threadIdx_x // 8 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 8 // 2 * 4 + 512 + 4] = A_1[threadIdx_x // 16 * 512 + blockIdx_x // 8 * 64 + threadIdx_x % 16 * 4 + 4096:threadIdx_x // 16 * 512 + blockIdx_x // 8 * 64 + threadIdx_x % 16 * 4 + 4096 + 4]
            T.attr(0, "async_scope", 1)
            for ax0_ax1_fused_2 in T.serial(3):
                B_shared_dyn_1[threadIdx_x // 16 * 128 + (blockIdx_x % 8 * 3 + (threadIdx_x % 16 * 3 + ax0_ax1_fused_2) // 16) // 4 * 64 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 8 // 4 * 32 + (blockIdx_x % 8 * 6 + (threadIdx_x % 16 * 3 + ax0_ax1_fused_2) // 8) % 8 * 4 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 4 + 1024 - blockIdx_x % 8 * 48 // 64 * 64] = B_1[threadIdx_x // 16 * 384 + blockIdx_x % 8 * 48 + threadIdx_x % 16 * 3 + ax0_ax1_fused_2 + 3072]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x // 8 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 8 // 2 * 4 + 1024:threadIdx_x // 8 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 8 // 2 * 4 + 1024 + 4] = A_1[threadIdx_x // 16 * 512 + blockIdx_x // 8 * 64 + threadIdx_x % 16 * 4 + 8192:threadIdx_x // 16 * 512 + blockIdx_x // 8 * 64 + threadIdx_x % 16 * 4 + 8192 + 4]
            T.attr(0, "async_scope", 1)
            for ax0_ax1_fused_2 in T.serial(3):
                B_shared_dyn_1[threadIdx_x // 16 * 128 + (blockIdx_x % 8 * 3 + (threadIdx_x % 16 * 3 + ax0_ax1_fused_2) // 16) // 4 * 64 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 8 // 4 * 32 + (blockIdx_x % 8 * 6 + (threadIdx_x % 16 * 3 + ax0_ax1_fused_2) // 8) % 8 * 4 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 4 + 2048 - blockIdx_x % 8 * 48 // 64 * 64] = B_1[threadIdx_x // 16 * 384 + blockIdx_x % 8 * 48 + threadIdx_x % 16 * 3 + ax0_ax1_fused_2 + 6144]
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 2)
            for ax1_1_s in T.serial(4):
                if ax1_1_s < 2:
                    A_shared_dyn_local_1[ax1_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s]
            for ax1_0 in T.serial(3):
                cse_var_1: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_1:cse_var_1 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_1) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_1) // 8) % 8 * 4 - blockIdx_x % 8 * 48 // 64 * 64:(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_1) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_1) // 8) % 8 * 4 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
        for k_0 in T.serial(29):
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    A_shared_dyn_1[(k_0 + 3) % 4 * 512 + threadIdx_x // 8 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 8 // 2 * 4:(k_0 + 3) % 4 * 512 + threadIdx_x // 8 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 8 // 2 * 4 + 4] = A_1[k_0 * 4096 + threadIdx_x // 16 * 512 + blockIdx_x // 8 * 64 + threadIdx_x % 16 * 4 + 12288:k_0 * 4096 + threadIdx_x // 16 * 512 + blockIdx_x // 8 * 64 + threadIdx_x % 16 * 4 + 12288 + 4]
                T.attr(0, "async_scope", 1)
                for ax0_ax1_fused_2 in T.serial(3):
                    B_shared_dyn_1[(k_0 + 3) % 4 * 1024 + threadIdx_x // 16 * 128 + (blockIdx_x % 8 * 3 + (threadIdx_x % 16 * 3 + ax0_ax1_fused_2) // 16) // 4 * 64 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 8 // 4 * 32 + (blockIdx_x % 8 * 6 + (threadIdx_x % 16 * 3 + ax0_ax1_fused_2) // 8) % 8 * 4 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 4 - blockIdx_x % 8 * 48 // 64 * 64] = B_1[k_0 * 3072 + threadIdx_x // 16 * 384 + blockIdx_x % 8 * 48 + threadIdx_x % 16 * 3 + ax0_ax1_fused_2 + 9216]
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 2)
                for ax1_1_s in T.serial(4):
                    if ax1_1_s < 2:
                        A_shared_dyn_local_1[ax1_1_s + 2] = A_shared_dyn_1[k_0 % 4 * 512 + threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 64]
                for ax1_0 in T.serial(3):
                    cse_var_2: T.int32 = ax1_0 * 4
                    B_shared_dyn_local_1[cse_var_2 + 12:cse_var_2 + 12 + 4] = B_shared_dyn_1[k_0 % 4 * 1024 + (blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_2) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_2) // 8) % 8 * 4 + 128 - blockIdx_x % 8 * 48 // 64 * 64:k_0 % 4 * 1024 + (blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_2) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_2) // 8) % 8 * 4 + 128 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_3: T.int32 = i_2_1_s * 12
                        Y_local_1[cse_var_3] = Y_local_1[cse_var_3] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_4: T.int32 = i_2_1_s * 12 + 1
                        Y_local_1[cse_var_4] = Y_local_1[cse_var_4] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_5: T.int32 = i_2_1_s * 12 + 2
                        Y_local_1[cse_var_5] = Y_local_1[cse_var_5] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_6: T.int32 = i_2_1_s * 12 + 3
                        Y_local_1[cse_var_6] = Y_local_1[cse_var_6] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_7: T.int32 = i_2_1_s * 12 + 4
                        Y_local_1[cse_var_7] = Y_local_1[cse_var_7] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_8: T.int32 = i_2_1_s * 12 + 5
                        Y_local_1[cse_var_8] = Y_local_1[cse_var_8] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_9: T.int32 = i_2_1_s * 12 + 6
                        Y_local_1[cse_var_9] = Y_local_1[cse_var_9] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_10: T.int32 = i_2_1_s * 12 + 7
                        Y_local_1[cse_var_10] = Y_local_1[cse_var_10] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_11: T.int32 = i_2_1_s * 12 + 8
                        Y_local_1[cse_var_11] = Y_local_1[cse_var_11] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[8]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_12: T.int32 = i_2_1_s * 12 + 9
                        Y_local_1[cse_var_12] = Y_local_1[cse_var_12] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[9]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_13: T.int32 = i_2_1_s * 12 + 10
                        Y_local_1[cse_var_13] = Y_local_1[cse_var_13] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[10]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_14: T.int32 = i_2_1_s * 12 + 11
                        Y_local_1[cse_var_14] = Y_local_1[cse_var_14] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[11]
                for ax1_1_s in T.serial(4):
                    if ax1_1_s < 2:
                        A_shared_dyn_local_1[ax1_1_s] = A_shared_dyn_1[k_0 % 4 * 512 + threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 128]
                for ax1_0 in T.serial(3):
                    cse_var_15: T.int32 = ax1_0 * 4
                    B_shared_dyn_local_1[cse_var_15:cse_var_15 + 4] = B_shared_dyn_1[k_0 % 4 * 1024 + (blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_15) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_15) // 8) % 8 * 4 + 256 - blockIdx_x % 8 * 48 // 64 * 64:k_0 % 4 * 1024 + (blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_15) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_15) // 8) % 8 * 4 + 256 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_16: T.int32 = i_2_1_s * 12
                        Y_local_1[cse_var_16] = Y_local_1[cse_var_16] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_17: T.int32 = i_2_1_s * 12 + 1
                        Y_local_1[cse_var_17] = Y_local_1[cse_var_17] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_18: T.int32 = i_2_1_s * 12 + 2
                        Y_local_1[cse_var_18] = Y_local_1[cse_var_18] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_19: T.int32 = i_2_1_s * 12 + 3
                        Y_local_1[cse_var_19] = Y_local_1[cse_var_19] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_20: T.int32 = i_2_1_s * 12 + 4
                        Y_local_1[cse_var_20] = Y_local_1[cse_var_20] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[16]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_21: T.int32 = i_2_1_s * 12 + 5
                        Y_local_1[cse_var_21] = Y_local_1[cse_var_21] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[17]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_22: T.int32 = i_2_1_s * 12 + 6
                        Y_local_1[cse_var_22] = Y_local_1[cse_var_22] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[18]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_23: T.int32 = i_2_1_s * 12 + 7
                        Y_local_1[cse_var_23] = Y_local_1[cse_var_23] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[19]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_24: T.int32 = i_2_1_s * 12 + 8
                        Y_local_1[cse_var_24] = Y_local_1[cse_var_24] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[20]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_25: T.int32 = i_2_1_s * 12 + 9
                        Y_local_1[cse_var_25] = Y_local_1[cse_var_25] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[21]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_26: T.int32 = i_2_1_s * 12 + 10
                        Y_local_1[cse_var_26] = Y_local_1[cse_var_26] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[22]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_27: T.int32 = i_2_1_s * 12 + 11
                        Y_local_1[cse_var_27] = Y_local_1[cse_var_27] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[23]
                for ax1_1_s in T.serial(4):
                    if ax1_1_s < 2:
                        A_shared_dyn_local_1[ax1_1_s + 2] = A_shared_dyn_1[k_0 % 4 * 512 + threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 192]
                for ax1_0 in T.serial(3):
                    cse_var_28: T.int32 = ax1_0 * 4
                    B_shared_dyn_local_1[cse_var_28 + 12:cse_var_28 + 12 + 4] = B_shared_dyn_1[k_0 % 4 * 1024 + (blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_28) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_28) // 8) % 8 * 4 + 384 - blockIdx_x % 8 * 48 // 64 * 64:k_0 % 4 * 1024 + (blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_28) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_28) // 8) % 8 * 4 + 384 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_29: T.int32 = i_2_1_s * 12
                        Y_local_1[cse_var_29] = Y_local_1[cse_var_29] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_30: T.int32 = i_2_1_s * 12 + 1
                        Y_local_1[cse_var_30] = Y_local_1[cse_var_30] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_31: T.int32 = i_2_1_s * 12 + 2
                        Y_local_1[cse_var_31] = Y_local_1[cse_var_31] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_32: T.int32 = i_2_1_s * 12 + 3
                        Y_local_1[cse_var_32] = Y_local_1[cse_var_32] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_33: T.int32 = i_2_1_s * 12 + 4
                        Y_local_1[cse_var_33] = Y_local_1[cse_var_33] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_34: T.int32 = i_2_1_s * 12 + 5
                        Y_local_1[cse_var_34] = Y_local_1[cse_var_34] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_35: T.int32 = i_2_1_s * 12 + 6
                        Y_local_1[cse_var_35] = Y_local_1[cse_var_35] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_36: T.int32 = i_2_1_s * 12 + 7
                        Y_local_1[cse_var_36] = Y_local_1[cse_var_36] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_37: T.int32 = i_2_1_s * 12 + 8
                        Y_local_1[cse_var_37] = Y_local_1[cse_var_37] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[8]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_38: T.int32 = i_2_1_s * 12 + 9
                        Y_local_1[cse_var_38] = Y_local_1[cse_var_38] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[9]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_39: T.int32 = i_2_1_s * 12 + 10
                        Y_local_1[cse_var_39] = Y_local_1[cse_var_39] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[10]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_40: T.int32 = i_2_1_s * 12 + 11
                        Y_local_1[cse_var_40] = Y_local_1[cse_var_40] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[11]
                for ax1_1_s in T.serial(4):
                    if ax1_1_s < 2:
                        A_shared_dyn_local_1[ax1_1_s] = A_shared_dyn_1[k_0 % 4 * 512 + threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 256]
                for ax1_0 in T.serial(3):
                    cse_var_41: T.int32 = ax1_0 * 4
                    B_shared_dyn_local_1[cse_var_41:cse_var_41 + 4] = B_shared_dyn_1[k_0 % 4 * 1024 + (blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_41) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_41) // 8) % 8 * 4 + 512 - blockIdx_x % 8 * 48 // 64 * 64:k_0 % 4 * 1024 + (blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_41) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_41) // 8) % 8 * 4 + 512 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_42: T.int32 = i_2_1_s * 12
                        Y_local_1[cse_var_42] = Y_local_1[cse_var_42] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_43: T.int32 = i_2_1_s * 12 + 1
                        Y_local_1[cse_var_43] = Y_local_1[cse_var_43] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_44: T.int32 = i_2_1_s * 12 + 2
                        Y_local_1[cse_var_44] = Y_local_1[cse_var_44] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_45: T.int32 = i_2_1_s * 12 + 3
                        Y_local_1[cse_var_45] = Y_local_1[cse_var_45] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_46: T.int32 = i_2_1_s * 12 + 4
                        Y_local_1[cse_var_46] = Y_local_1[cse_var_46] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[16]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_47: T.int32 = i_2_1_s * 12 + 5
                        Y_local_1[cse_var_47] = Y_local_1[cse_var_47] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[17]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_48: T.int32 = i_2_1_s * 12 + 6
                        Y_local_1[cse_var_48] = Y_local_1[cse_var_48] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[18]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_49: T.int32 = i_2_1_s * 12 + 7
                        Y_local_1[cse_var_49] = Y_local_1[cse_var_49] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[19]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_50: T.int32 = i_2_1_s * 12 + 8
                        Y_local_1[cse_var_50] = Y_local_1[cse_var_50] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[20]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_51: T.int32 = i_2_1_s * 12 + 9
                        Y_local_1[cse_var_51] = Y_local_1[cse_var_51] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[21]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_52: T.int32 = i_2_1_s * 12 + 10
                        Y_local_1[cse_var_52] = Y_local_1[cse_var_52] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[22]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_53: T.int32 = i_2_1_s * 12 + 11
                        Y_local_1[cse_var_53] = Y_local_1[cse_var_53] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[23]
                for ax1_1_s in T.serial(4):
                    if ax1_1_s < 2:
                        A_shared_dyn_local_1[ax1_1_s + 2] = A_shared_dyn_1[k_0 % 4 * 512 + threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 320]
                for ax1_0 in T.serial(3):
                    cse_var_54: T.int32 = ax1_0 * 4
                    B_shared_dyn_local_1[cse_var_54 + 12:cse_var_54 + 12 + 4] = B_shared_dyn_1[k_0 % 4 * 1024 + (blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_54) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_54) // 8) % 8 * 4 + 640 - blockIdx_x % 8 * 48 // 64 * 64:k_0 % 4 * 1024 + (blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_54) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_54) // 8) % 8 * 4 + 640 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_55: T.int32 = i_2_1_s * 12
                        Y_local_1[cse_var_55] = Y_local_1[cse_var_55] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_56: T.int32 = i_2_1_s * 12 + 1
                        Y_local_1[cse_var_56] = Y_local_1[cse_var_56] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_57: T.int32 = i_2_1_s * 12 + 2
                        Y_local_1[cse_var_57] = Y_local_1[cse_var_57] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_58: T.int32 = i_2_1_s * 12 + 3
                        Y_local_1[cse_var_58] = Y_local_1[cse_var_58] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_59: T.int32 = i_2_1_s * 12 + 4
                        Y_local_1[cse_var_59] = Y_local_1[cse_var_59] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_60: T.int32 = i_2_1_s * 12 + 5
                        Y_local_1[cse_var_60] = Y_local_1[cse_var_60] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_61: T.int32 = i_2_1_s * 12 + 6
                        Y_local_1[cse_var_61] = Y_local_1[cse_var_61] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_62: T.int32 = i_2_1_s * 12 + 7
                        Y_local_1[cse_var_62] = Y_local_1[cse_var_62] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_63: T.int32 = i_2_1_s * 12 + 8
                        Y_local_1[cse_var_63] = Y_local_1[cse_var_63] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[8]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_64: T.int32 = i_2_1_s * 12 + 9
                        Y_local_1[cse_var_64] = Y_local_1[cse_var_64] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[9]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_65: T.int32 = i_2_1_s * 12 + 10
                        Y_local_1[cse_var_65] = Y_local_1[cse_var_65] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[10]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_66: T.int32 = i_2_1_s * 12 + 11
                        Y_local_1[cse_var_66] = Y_local_1[cse_var_66] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[11]
                for ax1_1_s in T.serial(4):
                    if ax1_1_s < 2:
                        A_shared_dyn_local_1[ax1_1_s] = A_shared_dyn_1[k_0 % 4 * 512 + threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 384]
                for ax1_0 in T.serial(3):
                    cse_var_67: T.int32 = ax1_0 * 4
                    B_shared_dyn_local_1[cse_var_67:cse_var_67 + 4] = B_shared_dyn_1[k_0 % 4 * 1024 + (blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_67) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_67) // 8) % 8 * 4 + 768 - blockIdx_x % 8 * 48 // 64 * 64:k_0 % 4 * 1024 + (blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_67) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_67) // 8) % 8 * 4 + 768 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_68: T.int32 = i_2_1_s * 12
                        Y_local_1[cse_var_68] = Y_local_1[cse_var_68] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_69: T.int32 = i_2_1_s * 12 + 1
                        Y_local_1[cse_var_69] = Y_local_1[cse_var_69] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_70: T.int32 = i_2_1_s * 12 + 2
                        Y_local_1[cse_var_70] = Y_local_1[cse_var_70] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_71: T.int32 = i_2_1_s * 12 + 3
                        Y_local_1[cse_var_71] = Y_local_1[cse_var_71] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_72: T.int32 = i_2_1_s * 12 + 4
                        Y_local_1[cse_var_72] = Y_local_1[cse_var_72] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[16]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_73: T.int32 = i_2_1_s * 12 + 5
                        Y_local_1[cse_var_73] = Y_local_1[cse_var_73] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[17]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_74: T.int32 = i_2_1_s * 12 + 6
                        Y_local_1[cse_var_74] = Y_local_1[cse_var_74] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[18]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_75: T.int32 = i_2_1_s * 12 + 7
                        Y_local_1[cse_var_75] = Y_local_1[cse_var_75] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[19]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_76: T.int32 = i_2_1_s * 12 + 8
                        Y_local_1[cse_var_76] = Y_local_1[cse_var_76] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[20]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_77: T.int32 = i_2_1_s * 12 + 9
                        Y_local_1[cse_var_77] = Y_local_1[cse_var_77] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[21]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_78: T.int32 = i_2_1_s * 12 + 10
                        Y_local_1[cse_var_78] = Y_local_1[cse_var_78] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[22]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_79: T.int32 = i_2_1_s * 12 + 11
                        Y_local_1[cse_var_79] = Y_local_1[cse_var_79] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[23]
                for ax1_1_s in T.serial(4):
                    if ax1_1_s < 2:
                        A_shared_dyn_local_1[ax1_1_s + 2] = A_shared_dyn_1[k_0 % 4 * 512 + threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 448]
                for ax1_0 in T.serial(3):
                    cse_var_80: T.int32 = ax1_0 * 4
                    B_shared_dyn_local_1[cse_var_80 + 12:cse_var_80 + 12 + 4] = B_shared_dyn_1[k_0 % 4 * 1024 + (blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_80) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_80) // 8) % 8 * 4 + 896 - blockIdx_x % 8 * 48 // 64 * 64:k_0 % 4 * 1024 + (blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_80) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_80) // 8) % 8 * 4 + 896 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_81: T.int32 = i_2_1_s * 12
                        Y_local_1[cse_var_81] = Y_local_1[cse_var_81] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_82: T.int32 = i_2_1_s * 12 + 1
                        Y_local_1[cse_var_82] = Y_local_1[cse_var_82] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_83: T.int32 = i_2_1_s * 12 + 2
                        Y_local_1[cse_var_83] = Y_local_1[cse_var_83] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_84: T.int32 = i_2_1_s * 12 + 3
                        Y_local_1[cse_var_84] = Y_local_1[cse_var_84] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_85: T.int32 = i_2_1_s * 12 + 4
                        Y_local_1[cse_var_85] = Y_local_1[cse_var_85] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_86: T.int32 = i_2_1_s * 12 + 5
                        Y_local_1[cse_var_86] = Y_local_1[cse_var_86] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_87: T.int32 = i_2_1_s * 12 + 6
                        Y_local_1[cse_var_87] = Y_local_1[cse_var_87] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_88: T.int32 = i_2_1_s * 12 + 7
                        Y_local_1[cse_var_88] = Y_local_1[cse_var_88] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_89: T.int32 = i_2_1_s * 12 + 8
                        Y_local_1[cse_var_89] = Y_local_1[cse_var_89] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[8]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_90: T.int32 = i_2_1_s * 12 + 9
                        Y_local_1[cse_var_90] = Y_local_1[cse_var_90] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[9]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_91: T.int32 = i_2_1_s * 12 + 10
                        Y_local_1[cse_var_91] = Y_local_1[cse_var_91] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[10]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_92: T.int32 = i_2_1_s * 12 + 11
                        Y_local_1[cse_var_92] = Y_local_1[cse_var_92] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[11]
            for ax1_1_s in T.serial(4):
                if ax1_1_s < 2:
                    A_shared_dyn_local_1[ax1_1_s] = A_shared_dyn_1[(k_0 + 1) % 4 * 512 + threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s]
            for ax1_0 in T.serial(3):
                cse_var_93: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_93:cse_var_93 + 4] = B_shared_dyn_1[(k_0 + 1) % 4 * 1024 + (blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_93) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_93) // 8) % 8 * 4 - blockIdx_x % 8 * 48 // 64 * 64:(k_0 + 1) % 4 * 1024 + (blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_93) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_93) // 8) % 8 * 4 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_94: T.int32 = i_2_1_s * 12
                    Y_local_1[cse_var_94] = Y_local_1[cse_var_94] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_95: T.int32 = i_2_1_s * 12 + 1
                    Y_local_1[cse_var_95] = Y_local_1[cse_var_95] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_96: T.int32 = i_2_1_s * 12 + 2
                    Y_local_1[cse_var_96] = Y_local_1[cse_var_96] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_97: T.int32 = i_2_1_s * 12 + 3
                    Y_local_1[cse_var_97] = Y_local_1[cse_var_97] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_98: T.int32 = i_2_1_s * 12 + 4
                    Y_local_1[cse_var_98] = Y_local_1[cse_var_98] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[16]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_99: T.int32 = i_2_1_s * 12 + 5
                    Y_local_1[cse_var_99] = Y_local_1[cse_var_99] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[17]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_100: T.int32 = i_2_1_s * 12 + 6
                    Y_local_1[cse_var_100] = Y_local_1[cse_var_100] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[18]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_101: T.int32 = i_2_1_s * 12 + 7
                    Y_local_1[cse_var_101] = Y_local_1[cse_var_101] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[19]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_102: T.int32 = i_2_1_s * 12 + 8
                    Y_local_1[cse_var_102] = Y_local_1[cse_var_102] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[20]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_103: T.int32 = i_2_1_s * 12 + 9
                    Y_local_1[cse_var_103] = Y_local_1[cse_var_103] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[21]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_104: T.int32 = i_2_1_s * 12 + 10
                    Y_local_1[cse_var_104] = Y_local_1[cse_var_104] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[22]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_105: T.int32 = i_2_1_s * 12 + 11
                    Y_local_1[cse_var_105] = Y_local_1[cse_var_105] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[23]
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 1)
            for ax1_1_s in T.serial(4):
                if ax1_1_s < 2:
                    A_shared_dyn_local_1[ax1_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 576]
            for ax1_0 in T.serial(3):
                cse_var_106: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_106 + 12:cse_var_106 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_106) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_106) // 8) % 8 * 4 + 1152 - blockIdx_x % 8 * 48 // 64 * 64:(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_106) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_106) // 8) % 8 * 4 + 1152 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_107: T.int32 = i_2_1_s * 12
                    Y_local_1[cse_var_107] = Y_local_1[cse_var_107] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_108: T.int32 = i_2_1_s * 12 + 1
                    Y_local_1[cse_var_108] = Y_local_1[cse_var_108] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_109: T.int32 = i_2_1_s * 12 + 2
                    Y_local_1[cse_var_109] = Y_local_1[cse_var_109] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_110: T.int32 = i_2_1_s * 12 + 3
                    Y_local_1[cse_var_110] = Y_local_1[cse_var_110] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_111: T.int32 = i_2_1_s * 12 + 4
                    Y_local_1[cse_var_111] = Y_local_1[cse_var_111] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_112: T.int32 = i_2_1_s * 12 + 5
                    Y_local_1[cse_var_112] = Y_local_1[cse_var_112] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_113: T.int32 = i_2_1_s * 12 + 6
                    Y_local_1[cse_var_113] = Y_local_1[cse_var_113] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_114: T.int32 = i_2_1_s * 12 + 7
                    Y_local_1[cse_var_114] = Y_local_1[cse_var_114] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_115: T.int32 = i_2_1_s * 12 + 8
                    Y_local_1[cse_var_115] = Y_local_1[cse_var_115] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_116: T.int32 = i_2_1_s * 12 + 9
                    Y_local_1[cse_var_116] = Y_local_1[cse_var_116] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_117: T.int32 = i_2_1_s * 12 + 10
                    Y_local_1[cse_var_117] = Y_local_1[cse_var_117] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_118: T.int32 = i_2_1_s * 12 + 11
                    Y_local_1[cse_var_118] = Y_local_1[cse_var_118] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[11]
            for ax1_1_s in T.serial(4):
                if ax1_1_s < 2:
                    A_shared_dyn_local_1[ax1_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 640]
            for ax1_0 in T.serial(3):
                cse_var_119: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_119:cse_var_119 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_119) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_119) // 8) % 8 * 4 + 1280 - blockIdx_x % 8 * 48 // 64 * 64:(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_119) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_119) // 8) % 8 * 4 + 1280 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_120: T.int32 = i_2_1_s * 12
                    Y_local_1[cse_var_120] = Y_local_1[cse_var_120] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_121: T.int32 = i_2_1_s * 12 + 1
                    Y_local_1[cse_var_121] = Y_local_1[cse_var_121] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_122: T.int32 = i_2_1_s * 12 + 2
                    Y_local_1[cse_var_122] = Y_local_1[cse_var_122] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_123: T.int32 = i_2_1_s * 12 + 3
                    Y_local_1[cse_var_123] = Y_local_1[cse_var_123] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_124: T.int32 = i_2_1_s * 12 + 4
                    Y_local_1[cse_var_124] = Y_local_1[cse_var_124] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[16]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_125: T.int32 = i_2_1_s * 12 + 5
                    Y_local_1[cse_var_125] = Y_local_1[cse_var_125] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[17]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_126: T.int32 = i_2_1_s * 12 + 6
                    Y_local_1[cse_var_126] = Y_local_1[cse_var_126] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[18]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_127: T.int32 = i_2_1_s * 12 + 7
                    Y_local_1[cse_var_127] = Y_local_1[cse_var_127] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[19]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_128: T.int32 = i_2_1_s * 12 + 8
                    Y_local_1[cse_var_128] = Y_local_1[cse_var_128] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[20]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_129: T.int32 = i_2_1_s * 12 + 9
                    Y_local_1[cse_var_129] = Y_local_1[cse_var_129] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[21]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_130: T.int32 = i_2_1_s * 12 + 10
                    Y_local_1[cse_var_130] = Y_local_1[cse_var_130] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[22]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_131: T.int32 = i_2_1_s * 12 + 11
                    Y_local_1[cse_var_131] = Y_local_1[cse_var_131] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[23]
            for ax1_1_s in T.serial(4):
                if ax1_1_s < 2:
                    A_shared_dyn_local_1[ax1_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 704]
            for ax1_0 in T.serial(3):
                cse_var_132: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_132 + 12:cse_var_132 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_132) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_132) // 8) % 8 * 4 + 1408 - blockIdx_x % 8 * 48 // 64 * 64:(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_132) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_132) // 8) % 8 * 4 + 1408 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_133: T.int32 = i_2_1_s * 12
                    Y_local_1[cse_var_133] = Y_local_1[cse_var_133] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_134: T.int32 = i_2_1_s * 12 + 1
                    Y_local_1[cse_var_134] = Y_local_1[cse_var_134] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_135: T.int32 = i_2_1_s * 12 + 2
                    Y_local_1[cse_var_135] = Y_local_1[cse_var_135] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_136: T.int32 = i_2_1_s * 12 + 3
                    Y_local_1[cse_var_136] = Y_local_1[cse_var_136] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_137: T.int32 = i_2_1_s * 12 + 4
                    Y_local_1[cse_var_137] = Y_local_1[cse_var_137] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_138: T.int32 = i_2_1_s * 12 + 5
                    Y_local_1[cse_var_138] = Y_local_1[cse_var_138] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_139: T.int32 = i_2_1_s * 12 + 6
                    Y_local_1[cse_var_139] = Y_local_1[cse_var_139] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_140: T.int32 = i_2_1_s * 12 + 7
                    Y_local_1[cse_var_140] = Y_local_1[cse_var_140] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_141: T.int32 = i_2_1_s * 12 + 8
                    Y_local_1[cse_var_141] = Y_local_1[cse_var_141] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_142: T.int32 = i_2_1_s * 12 + 9
                    Y_local_1[cse_var_142] = Y_local_1[cse_var_142] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_143: T.int32 = i_2_1_s * 12 + 10
                    Y_local_1[cse_var_143] = Y_local_1[cse_var_143] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_144: T.int32 = i_2_1_s * 12 + 11
                    Y_local_1[cse_var_144] = Y_local_1[cse_var_144] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[11]
            for ax1_1_s in T.serial(4):
                if ax1_1_s < 2:
                    A_shared_dyn_local_1[ax1_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 768]
            for ax1_0 in T.serial(3):
                cse_var_145: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_145:cse_var_145 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_145) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_145) // 8) % 8 * 4 + 1536 - blockIdx_x % 8 * 48 // 64 * 64:(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_145) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_145) // 8) % 8 * 4 + 1536 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_146: T.int32 = i_2_1_s * 12
                    Y_local_1[cse_var_146] = Y_local_1[cse_var_146] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_147: T.int32 = i_2_1_s * 12 + 1
                    Y_local_1[cse_var_147] = Y_local_1[cse_var_147] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_148: T.int32 = i_2_1_s * 12 + 2
                    Y_local_1[cse_var_148] = Y_local_1[cse_var_148] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_149: T.int32 = i_2_1_s * 12 + 3
                    Y_local_1[cse_var_149] = Y_local_1[cse_var_149] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_150: T.int32 = i_2_1_s * 12 + 4
                    Y_local_1[cse_var_150] = Y_local_1[cse_var_150] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[16]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_151: T.int32 = i_2_1_s * 12 + 5
                    Y_local_1[cse_var_151] = Y_local_1[cse_var_151] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[17]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_152: T.int32 = i_2_1_s * 12 + 6
                    Y_local_1[cse_var_152] = Y_local_1[cse_var_152] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[18]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_153: T.int32 = i_2_1_s * 12 + 7
                    Y_local_1[cse_var_153] = Y_local_1[cse_var_153] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[19]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_154: T.int32 = i_2_1_s * 12 + 8
                    Y_local_1[cse_var_154] = Y_local_1[cse_var_154] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[20]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_155: T.int32 = i_2_1_s * 12 + 9
                    Y_local_1[cse_var_155] = Y_local_1[cse_var_155] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[21]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_156: T.int32 = i_2_1_s * 12 + 10
                    Y_local_1[cse_var_156] = Y_local_1[cse_var_156] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[22]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_157: T.int32 = i_2_1_s * 12 + 11
                    Y_local_1[cse_var_157] = Y_local_1[cse_var_157] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[23]
            for ax1_1_s in T.serial(4):
                if ax1_1_s < 2:
                    A_shared_dyn_local_1[ax1_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 832]
            for ax1_0 in T.serial(3):
                cse_var_158: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_158 + 12:cse_var_158 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_158) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_158) // 8) % 8 * 4 + 1664 - blockIdx_x % 8 * 48 // 64 * 64:(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_158) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_158) // 8) % 8 * 4 + 1664 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_159: T.int32 = i_2_1_s * 12
                    Y_local_1[cse_var_159] = Y_local_1[cse_var_159] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_160: T.int32 = i_2_1_s * 12 + 1
                    Y_local_1[cse_var_160] = Y_local_1[cse_var_160] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_161: T.int32 = i_2_1_s * 12 + 2
                    Y_local_1[cse_var_161] = Y_local_1[cse_var_161] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_162: T.int32 = i_2_1_s * 12 + 3
                    Y_local_1[cse_var_162] = Y_local_1[cse_var_162] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_163: T.int32 = i_2_1_s * 12 + 4
                    Y_local_1[cse_var_163] = Y_local_1[cse_var_163] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_164: T.int32 = i_2_1_s * 12 + 5
                    Y_local_1[cse_var_164] = Y_local_1[cse_var_164] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_165: T.int32 = i_2_1_s * 12 + 6
                    Y_local_1[cse_var_165] = Y_local_1[cse_var_165] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_166: T.int32 = i_2_1_s * 12 + 7
                    Y_local_1[cse_var_166] = Y_local_1[cse_var_166] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_167: T.int32 = i_2_1_s * 12 + 8
                    Y_local_1[cse_var_167] = Y_local_1[cse_var_167] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_168: T.int32 = i_2_1_s * 12 + 9
                    Y_local_1[cse_var_168] = Y_local_1[cse_var_168] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_169: T.int32 = i_2_1_s * 12 + 10
                    Y_local_1[cse_var_169] = Y_local_1[cse_var_169] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_170: T.int32 = i_2_1_s * 12 + 11
                    Y_local_1[cse_var_170] = Y_local_1[cse_var_170] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[11]
            for ax1_1_s in T.serial(4):
                if ax1_1_s < 2:
                    A_shared_dyn_local_1[ax1_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 896]
            for ax1_0 in T.serial(3):
                cse_var_171: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_171:cse_var_171 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_171) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_171) // 8) % 8 * 4 + 1792 - blockIdx_x % 8 * 48 // 64 * 64:(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_171) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_171) // 8) % 8 * 4 + 1792 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_172: T.int32 = i_2_1_s * 12
                    Y_local_1[cse_var_172] = Y_local_1[cse_var_172] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_173: T.int32 = i_2_1_s * 12 + 1
                    Y_local_1[cse_var_173] = Y_local_1[cse_var_173] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_174: T.int32 = i_2_1_s * 12 + 2
                    Y_local_1[cse_var_174] = Y_local_1[cse_var_174] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_175: T.int32 = i_2_1_s * 12 + 3
                    Y_local_1[cse_var_175] = Y_local_1[cse_var_175] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_176: T.int32 = i_2_1_s * 12 + 4
                    Y_local_1[cse_var_176] = Y_local_1[cse_var_176] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[16]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_177: T.int32 = i_2_1_s * 12 + 5
                    Y_local_1[cse_var_177] = Y_local_1[cse_var_177] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[17]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_178: T.int32 = i_2_1_s * 12 + 6
                    Y_local_1[cse_var_178] = Y_local_1[cse_var_178] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[18]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_179: T.int32 = i_2_1_s * 12 + 7
                    Y_local_1[cse_var_179] = Y_local_1[cse_var_179] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[19]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_180: T.int32 = i_2_1_s * 12 + 8
                    Y_local_1[cse_var_180] = Y_local_1[cse_var_180] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[20]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_181: T.int32 = i_2_1_s * 12 + 9
                    Y_local_1[cse_var_181] = Y_local_1[cse_var_181] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[21]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_182: T.int32 = i_2_1_s * 12 + 10
                    Y_local_1[cse_var_182] = Y_local_1[cse_var_182] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[22]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_183: T.int32 = i_2_1_s * 12 + 11
                    Y_local_1[cse_var_183] = Y_local_1[cse_var_183] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[23]
            for ax1_1_s in T.serial(4):
                if ax1_1_s < 2:
                    A_shared_dyn_local_1[ax1_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 960]
            for ax1_0 in T.serial(3):
                cse_var_184: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_184 + 12:cse_var_184 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_184) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_184) // 8) % 8 * 4 + 1920 - blockIdx_x % 8 * 48 // 64 * 64:(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_184) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_184) // 8) % 8 * 4 + 1920 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_185: T.int32 = i_2_1_s * 12
                    Y_local_1[cse_var_185] = Y_local_1[cse_var_185] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_186: T.int32 = i_2_1_s * 12 + 1
                    Y_local_1[cse_var_186] = Y_local_1[cse_var_186] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_187: T.int32 = i_2_1_s * 12 + 2
                    Y_local_1[cse_var_187] = Y_local_1[cse_var_187] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_188: T.int32 = i_2_1_s * 12 + 3
                    Y_local_1[cse_var_188] = Y_local_1[cse_var_188] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_189: T.int32 = i_2_1_s * 12 + 4
                    Y_local_1[cse_var_189] = Y_local_1[cse_var_189] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_190: T.int32 = i_2_1_s * 12 + 5
                    Y_local_1[cse_var_190] = Y_local_1[cse_var_190] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_191: T.int32 = i_2_1_s * 12 + 6
                    Y_local_1[cse_var_191] = Y_local_1[cse_var_191] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_192: T.int32 = i_2_1_s * 12 + 7
                    Y_local_1[cse_var_192] = Y_local_1[cse_var_192] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_193: T.int32 = i_2_1_s * 12 + 8
                    Y_local_1[cse_var_193] = Y_local_1[cse_var_193] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_194: T.int32 = i_2_1_s * 12 + 9
                    Y_local_1[cse_var_194] = Y_local_1[cse_var_194] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_195: T.int32 = i_2_1_s * 12 + 10
                    Y_local_1[cse_var_195] = Y_local_1[cse_var_195] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_196: T.int32 = i_2_1_s * 12 + 11
                    Y_local_1[cse_var_196] = Y_local_1[cse_var_196] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[11]
        for ax1_1_s in T.serial(4):
            if ax1_1_s < 2:
                A_shared_dyn_local_1[ax1_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 1024]
        for ax1_0 in T.serial(3):
            cse_var_197: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_197:cse_var_197 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_197) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_197) // 8) % 8 * 4 + 2048 - blockIdx_x % 8 * 48 // 64 * 64:(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_197) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_197) // 8) % 8 * 4 + 2048 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_198: T.int32 = i_2_1_s * 12
                Y_local_1[cse_var_198] = Y_local_1[cse_var_198] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_199: T.int32 = i_2_1_s * 12 + 1
                Y_local_1[cse_var_199] = Y_local_1[cse_var_199] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_200: T.int32 = i_2_1_s * 12 + 2
                Y_local_1[cse_var_200] = Y_local_1[cse_var_200] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_201: T.int32 = i_2_1_s * 12 + 3
                Y_local_1[cse_var_201] = Y_local_1[cse_var_201] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_202: T.int32 = i_2_1_s * 12 + 4
                Y_local_1[cse_var_202] = Y_local_1[cse_var_202] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[16]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_203: T.int32 = i_2_1_s * 12 + 5
                Y_local_1[cse_var_203] = Y_local_1[cse_var_203] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[17]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_204: T.int32 = i_2_1_s * 12 + 6
                Y_local_1[cse_var_204] = Y_local_1[cse_var_204] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[18]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_205: T.int32 = i_2_1_s * 12 + 7
                Y_local_1[cse_var_205] = Y_local_1[cse_var_205] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[19]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_206: T.int32 = i_2_1_s * 12 + 8
                Y_local_1[cse_var_206] = Y_local_1[cse_var_206] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[20]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_207: T.int32 = i_2_1_s * 12 + 9
                Y_local_1[cse_var_207] = Y_local_1[cse_var_207] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[21]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_208: T.int32 = i_2_1_s * 12 + 10
                Y_local_1[cse_var_208] = Y_local_1[cse_var_208] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[22]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_209: T.int32 = i_2_1_s * 12 + 11
                Y_local_1[cse_var_209] = Y_local_1[cse_var_209] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[23]
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 0)
            for ax1_1_s in T.serial(4):
                if ax1_1_s < 2:
                    A_shared_dyn_local_1[ax1_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 1088]
            for ax1_0 in T.serial(3):
                cse_var_210: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_210 + 12:cse_var_210 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_210) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_210) // 8) % 8 * 4 + 2176 - blockIdx_x % 8 * 48 // 64 * 64:(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_210) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_210) // 8) % 8 * 4 + 2176 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_211: T.int32 = i_2_1_s * 12
                    Y_local_1[cse_var_211] = Y_local_1[cse_var_211] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_212: T.int32 = i_2_1_s * 12 + 1
                    Y_local_1[cse_var_212] = Y_local_1[cse_var_212] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_213: T.int32 = i_2_1_s * 12 + 2
                    Y_local_1[cse_var_213] = Y_local_1[cse_var_213] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_214: T.int32 = i_2_1_s * 12 + 3
                    Y_local_1[cse_var_214] = Y_local_1[cse_var_214] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_215: T.int32 = i_2_1_s * 12 + 4
                    Y_local_1[cse_var_215] = Y_local_1[cse_var_215] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_216: T.int32 = i_2_1_s * 12 + 5
                    Y_local_1[cse_var_216] = Y_local_1[cse_var_216] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_217: T.int32 = i_2_1_s * 12 + 6
                    Y_local_1[cse_var_217] = Y_local_1[cse_var_217] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_218: T.int32 = i_2_1_s * 12 + 7
                    Y_local_1[cse_var_218] = Y_local_1[cse_var_218] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_219: T.int32 = i_2_1_s * 12 + 8
                    Y_local_1[cse_var_219] = Y_local_1[cse_var_219] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_220: T.int32 = i_2_1_s * 12 + 9
                    Y_local_1[cse_var_220] = Y_local_1[cse_var_220] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_221: T.int32 = i_2_1_s * 12 + 10
                    Y_local_1[cse_var_221] = Y_local_1[cse_var_221] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_222: T.int32 = i_2_1_s * 12 + 11
                    Y_local_1[cse_var_222] = Y_local_1[cse_var_222] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[11]
            for ax1_1_s in T.serial(4):
                if ax1_1_s < 2:
                    A_shared_dyn_local_1[ax1_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 1152]
            for ax1_0 in T.serial(3):
                cse_var_223: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_223:cse_var_223 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_223) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_223) // 8) % 8 * 4 + 2304 - blockIdx_x % 8 * 48 // 64 * 64:(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_223) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_223) // 8) % 8 * 4 + 2304 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_224: T.int32 = i_2_1_s * 12
                    Y_local_1[cse_var_224] = Y_local_1[cse_var_224] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_225: T.int32 = i_2_1_s * 12 + 1
                    Y_local_1[cse_var_225] = Y_local_1[cse_var_225] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_226: T.int32 = i_2_1_s * 12 + 2
                    Y_local_1[cse_var_226] = Y_local_1[cse_var_226] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_227: T.int32 = i_2_1_s * 12 + 3
                    Y_local_1[cse_var_227] = Y_local_1[cse_var_227] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_228: T.int32 = i_2_1_s * 12 + 4
                    Y_local_1[cse_var_228] = Y_local_1[cse_var_228] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[16]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_229: T.int32 = i_2_1_s * 12 + 5
                    Y_local_1[cse_var_229] = Y_local_1[cse_var_229] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[17]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_230: T.int32 = i_2_1_s * 12 + 6
                    Y_local_1[cse_var_230] = Y_local_1[cse_var_230] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[18]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_231: T.int32 = i_2_1_s * 12 + 7
                    Y_local_1[cse_var_231] = Y_local_1[cse_var_231] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[19]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_232: T.int32 = i_2_1_s * 12 + 8
                    Y_local_1[cse_var_232] = Y_local_1[cse_var_232] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[20]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_233: T.int32 = i_2_1_s * 12 + 9
                    Y_local_1[cse_var_233] = Y_local_1[cse_var_233] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[21]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_234: T.int32 = i_2_1_s * 12 + 10
                    Y_local_1[cse_var_234] = Y_local_1[cse_var_234] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[22]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_235: T.int32 = i_2_1_s * 12 + 11
                    Y_local_1[cse_var_235] = Y_local_1[cse_var_235] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[23]
            for ax1_1_s in T.serial(4):
                if ax1_1_s < 2:
                    A_shared_dyn_local_1[ax1_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 1216]
            for ax1_0 in T.serial(3):
                cse_var_236: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_236 + 12:cse_var_236 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_236) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_236) // 8) % 8 * 4 + 2432 - blockIdx_x % 8 * 48 // 64 * 64:(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_236) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_236) // 8) % 8 * 4 + 2432 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_237: T.int32 = i_2_1_s * 12
                    Y_local_1[cse_var_237] = Y_local_1[cse_var_237] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_238: T.int32 = i_2_1_s * 12 + 1
                    Y_local_1[cse_var_238] = Y_local_1[cse_var_238] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_239: T.int32 = i_2_1_s * 12 + 2
                    Y_local_1[cse_var_239] = Y_local_1[cse_var_239] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_240: T.int32 = i_2_1_s * 12 + 3
                    Y_local_1[cse_var_240] = Y_local_1[cse_var_240] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_241: T.int32 = i_2_1_s * 12 + 4
                    Y_local_1[cse_var_241] = Y_local_1[cse_var_241] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_242: T.int32 = i_2_1_s * 12 + 5
                    Y_local_1[cse_var_242] = Y_local_1[cse_var_242] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_243: T.int32 = i_2_1_s * 12 + 6
                    Y_local_1[cse_var_243] = Y_local_1[cse_var_243] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_244: T.int32 = i_2_1_s * 12 + 7
                    Y_local_1[cse_var_244] = Y_local_1[cse_var_244] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_245: T.int32 = i_2_1_s * 12 + 8
                    Y_local_1[cse_var_245] = Y_local_1[cse_var_245] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_246: T.int32 = i_2_1_s * 12 + 9
                    Y_local_1[cse_var_246] = Y_local_1[cse_var_246] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_247: T.int32 = i_2_1_s * 12 + 10
                    Y_local_1[cse_var_247] = Y_local_1[cse_var_247] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_248: T.int32 = i_2_1_s * 12 + 11
                    Y_local_1[cse_var_248] = Y_local_1[cse_var_248] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[11]
            for ax1_1_s in T.serial(4):
                if ax1_1_s < 2:
                    A_shared_dyn_local_1[ax1_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 1280]
            for ax1_0 in T.serial(3):
                cse_var_249: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_249:cse_var_249 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_249) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_249) // 8) % 8 * 4 + 2560 - blockIdx_x % 8 * 48 // 64 * 64:(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_249) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_249) // 8) % 8 * 4 + 2560 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_250: T.int32 = i_2_1_s * 12
                    Y_local_1[cse_var_250] = Y_local_1[cse_var_250] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_251: T.int32 = i_2_1_s * 12 + 1
                    Y_local_1[cse_var_251] = Y_local_1[cse_var_251] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_252: T.int32 = i_2_1_s * 12 + 2
                    Y_local_1[cse_var_252] = Y_local_1[cse_var_252] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_253: T.int32 = i_2_1_s * 12 + 3
                    Y_local_1[cse_var_253] = Y_local_1[cse_var_253] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_254: T.int32 = i_2_1_s * 12 + 4
                    Y_local_1[cse_var_254] = Y_local_1[cse_var_254] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[16]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_255: T.int32 = i_2_1_s * 12 + 5
                    Y_local_1[cse_var_255] = Y_local_1[cse_var_255] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[17]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_256: T.int32 = i_2_1_s * 12 + 6
                    Y_local_1[cse_var_256] = Y_local_1[cse_var_256] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[18]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_257: T.int32 = i_2_1_s * 12 + 7
                    Y_local_1[cse_var_257] = Y_local_1[cse_var_257] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[19]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_258: T.int32 = i_2_1_s * 12 + 8
                    Y_local_1[cse_var_258] = Y_local_1[cse_var_258] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[20]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_259: T.int32 = i_2_1_s * 12 + 9
                    Y_local_1[cse_var_259] = Y_local_1[cse_var_259] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[21]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_260: T.int32 = i_2_1_s * 12 + 10
                    Y_local_1[cse_var_260] = Y_local_1[cse_var_260] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[22]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_261: T.int32 = i_2_1_s * 12 + 11
                    Y_local_1[cse_var_261] = Y_local_1[cse_var_261] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[23]
            for ax1_1_s in T.serial(4):
                if ax1_1_s < 2:
                    A_shared_dyn_local_1[ax1_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 1344]
            for ax1_0 in T.serial(3):
                cse_var_262: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_262 + 12:cse_var_262 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_262) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_262) // 8) % 8 * 4 + 2688 - blockIdx_x % 8 * 48 // 64 * 64:(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_262) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_262) // 8) % 8 * 4 + 2688 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_263: T.int32 = i_2_1_s * 12
                    Y_local_1[cse_var_263] = Y_local_1[cse_var_263] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_264: T.int32 = i_2_1_s * 12 + 1
                    Y_local_1[cse_var_264] = Y_local_1[cse_var_264] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_265: T.int32 = i_2_1_s * 12 + 2
                    Y_local_1[cse_var_265] = Y_local_1[cse_var_265] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_266: T.int32 = i_2_1_s * 12 + 3
                    Y_local_1[cse_var_266] = Y_local_1[cse_var_266] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_267: T.int32 = i_2_1_s * 12 + 4
                    Y_local_1[cse_var_267] = Y_local_1[cse_var_267] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_268: T.int32 = i_2_1_s * 12 + 5
                    Y_local_1[cse_var_268] = Y_local_1[cse_var_268] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_269: T.int32 = i_2_1_s * 12 + 6
                    Y_local_1[cse_var_269] = Y_local_1[cse_var_269] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_270: T.int32 = i_2_1_s * 12 + 7
                    Y_local_1[cse_var_270] = Y_local_1[cse_var_270] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_271: T.int32 = i_2_1_s * 12 + 8
                    Y_local_1[cse_var_271] = Y_local_1[cse_var_271] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_272: T.int32 = i_2_1_s * 12 + 9
                    Y_local_1[cse_var_272] = Y_local_1[cse_var_272] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_273: T.int32 = i_2_1_s * 12 + 10
                    Y_local_1[cse_var_273] = Y_local_1[cse_var_273] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_274: T.int32 = i_2_1_s * 12 + 11
                    Y_local_1[cse_var_274] = Y_local_1[cse_var_274] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[11]
            for ax1_1_s in T.serial(4):
                if ax1_1_s < 2:
                    A_shared_dyn_local_1[ax1_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 1408]
            for ax1_0 in T.serial(3):
                cse_var_275: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_275:cse_var_275 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_275) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_275) // 8) % 8 * 4 + 2816 - blockIdx_x % 8 * 48 // 64 * 64:(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_275) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_275) // 8) % 8 * 4 + 2816 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_276: T.int32 = i_2_1_s * 12
                    Y_local_1[cse_var_276] = Y_local_1[cse_var_276] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_277: T.int32 = i_2_1_s * 12 + 1
                    Y_local_1[cse_var_277] = Y_local_1[cse_var_277] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_278: T.int32 = i_2_1_s * 12 + 2
                    Y_local_1[cse_var_278] = Y_local_1[cse_var_278] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_279: T.int32 = i_2_1_s * 12 + 3
                    Y_local_1[cse_var_279] = Y_local_1[cse_var_279] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_280: T.int32 = i_2_1_s * 12 + 4
                    Y_local_1[cse_var_280] = Y_local_1[cse_var_280] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[16]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_281: T.int32 = i_2_1_s * 12 + 5
                    Y_local_1[cse_var_281] = Y_local_1[cse_var_281] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[17]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_282: T.int32 = i_2_1_s * 12 + 6
                    Y_local_1[cse_var_282] = Y_local_1[cse_var_282] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[18]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_283: T.int32 = i_2_1_s * 12 + 7
                    Y_local_1[cse_var_283] = Y_local_1[cse_var_283] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[19]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_284: T.int32 = i_2_1_s * 12 + 8
                    Y_local_1[cse_var_284] = Y_local_1[cse_var_284] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[20]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_285: T.int32 = i_2_1_s * 12 + 9
                    Y_local_1[cse_var_285] = Y_local_1[cse_var_285] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[21]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_286: T.int32 = i_2_1_s * 12 + 10
                    Y_local_1[cse_var_286] = Y_local_1[cse_var_286] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[22]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_287: T.int32 = i_2_1_s * 12 + 11
                    Y_local_1[cse_var_287] = Y_local_1[cse_var_287] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[23]
            for ax1_1_s in T.serial(4):
                if ax1_1_s < 2:
                    A_shared_dyn_local_1[ax1_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 1472]
            for ax1_0 in T.serial(3):
                cse_var_288: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_288 + 12:cse_var_288 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_288) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_288) // 8) % 8 * 4 + 2944 - blockIdx_x % 8 * 48 // 64 * 64:(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_288) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_288) // 8) % 8 * 4 + 2944 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_289: T.int32 = i_2_1_s * 12
                    Y_local_1[cse_var_289] = Y_local_1[cse_var_289] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_290: T.int32 = i_2_1_s * 12 + 1
                    Y_local_1[cse_var_290] = Y_local_1[cse_var_290] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_291: T.int32 = i_2_1_s * 12 + 2
                    Y_local_1[cse_var_291] = Y_local_1[cse_var_291] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_292: T.int32 = i_2_1_s * 12 + 3
                    Y_local_1[cse_var_292] = Y_local_1[cse_var_292] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_293: T.int32 = i_2_1_s * 12 + 4
                    Y_local_1[cse_var_293] = Y_local_1[cse_var_293] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_294: T.int32 = i_2_1_s * 12 + 5
                    Y_local_1[cse_var_294] = Y_local_1[cse_var_294] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_295: T.int32 = i_2_1_s * 12 + 6
                    Y_local_1[cse_var_295] = Y_local_1[cse_var_295] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_296: T.int32 = i_2_1_s * 12 + 7
                    Y_local_1[cse_var_296] = Y_local_1[cse_var_296] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_297: T.int32 = i_2_1_s * 12 + 8
                    Y_local_1[cse_var_297] = Y_local_1[cse_var_297] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_298: T.int32 = i_2_1_s * 12 + 9
                    Y_local_1[cse_var_298] = Y_local_1[cse_var_298] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_299: T.int32 = i_2_1_s * 12 + 10
                    Y_local_1[cse_var_299] = Y_local_1[cse_var_299] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_300: T.int32 = i_2_1_s * 12 + 11
                    Y_local_1[cse_var_300] = Y_local_1[cse_var_300] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[11]
        for ax1_1_s in T.serial(4):
            if ax1_1_s < 2:
                A_shared_dyn_local_1[ax1_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 1536]
        for ax1_0 in T.serial(3):
            cse_var_301: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_301:cse_var_301 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_301) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_301) // 8) % 8 * 4 + 3072 - blockIdx_x % 8 * 48 // 64 * 64:(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_301) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_301) // 8) % 8 * 4 + 3072 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_302: T.int32 = i_2_1_s * 12
                Y_local_1[cse_var_302] = Y_local_1[cse_var_302] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_303: T.int32 = i_2_1_s * 12 + 1
                Y_local_1[cse_var_303] = Y_local_1[cse_var_303] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_304: T.int32 = i_2_1_s * 12 + 2
                Y_local_1[cse_var_304] = Y_local_1[cse_var_304] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_305: T.int32 = i_2_1_s * 12 + 3
                Y_local_1[cse_var_305] = Y_local_1[cse_var_305] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_306: T.int32 = i_2_1_s * 12 + 4
                Y_local_1[cse_var_306] = Y_local_1[cse_var_306] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[16]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_307: T.int32 = i_2_1_s * 12 + 5
                Y_local_1[cse_var_307] = Y_local_1[cse_var_307] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[17]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_308: T.int32 = i_2_1_s * 12 + 6
                Y_local_1[cse_var_308] = Y_local_1[cse_var_308] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[18]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_309: T.int32 = i_2_1_s * 12 + 7
                Y_local_1[cse_var_309] = Y_local_1[cse_var_309] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[19]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_310: T.int32 = i_2_1_s * 12 + 8
                Y_local_1[cse_var_310] = Y_local_1[cse_var_310] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[20]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_311: T.int32 = i_2_1_s * 12 + 9
                Y_local_1[cse_var_311] = Y_local_1[cse_var_311] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[21]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_312: T.int32 = i_2_1_s * 12 + 10
                Y_local_1[cse_var_312] = Y_local_1[cse_var_312] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[22]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_313: T.int32 = i_2_1_s * 12 + 11
                Y_local_1[cse_var_313] = Y_local_1[cse_var_313] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[23]
        for ax1_1_s in T.serial(4):
            if ax1_1_s < 2:
                A_shared_dyn_local_1[ax1_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 1600]
        for ax1_0 in T.serial(3):
            cse_var_314: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_314 + 12:cse_var_314 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_314) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_314) // 8) % 8 * 4 + 3200 - blockIdx_x % 8 * 48 // 64 * 64:(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_314) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_314) // 8) % 8 * 4 + 3200 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_315: T.int32 = i_2_1_s * 12
                Y_local_1[cse_var_315] = Y_local_1[cse_var_315] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_316: T.int32 = i_2_1_s * 12 + 1
                Y_local_1[cse_var_316] = Y_local_1[cse_var_316] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_317: T.int32 = i_2_1_s * 12 + 2
                Y_local_1[cse_var_317] = Y_local_1[cse_var_317] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_318: T.int32 = i_2_1_s * 12 + 3
                Y_local_1[cse_var_318] = Y_local_1[cse_var_318] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_319: T.int32 = i_2_1_s * 12 + 4
                Y_local_1[cse_var_319] = Y_local_1[cse_var_319] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_320: T.int32 = i_2_1_s * 12 + 5
                Y_local_1[cse_var_320] = Y_local_1[cse_var_320] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_321: T.int32 = i_2_1_s * 12 + 6
                Y_local_1[cse_var_321] = Y_local_1[cse_var_321] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_322: T.int32 = i_2_1_s * 12 + 7
                Y_local_1[cse_var_322] = Y_local_1[cse_var_322] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_323: T.int32 = i_2_1_s * 12 + 8
                Y_local_1[cse_var_323] = Y_local_1[cse_var_323] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[8]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_324: T.int32 = i_2_1_s * 12 + 9
                Y_local_1[cse_var_324] = Y_local_1[cse_var_324] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[9]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_325: T.int32 = i_2_1_s * 12 + 10
                Y_local_1[cse_var_325] = Y_local_1[cse_var_325] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[10]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_326: T.int32 = i_2_1_s * 12 + 11
                Y_local_1[cse_var_326] = Y_local_1[cse_var_326] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[11]
        for ax1_1_s in T.serial(4):
            if ax1_1_s < 2:
                A_shared_dyn_local_1[ax1_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 1664]
        for ax1_0 in T.serial(3):
            cse_var_327: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_327:cse_var_327 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_327) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_327) // 8) % 8 * 4 + 3328 - blockIdx_x % 8 * 48 // 64 * 64:(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_327) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_327) // 8) % 8 * 4 + 3328 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_328: T.int32 = i_2_1_s * 12
                Y_local_1[cse_var_328] = Y_local_1[cse_var_328] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_329: T.int32 = i_2_1_s * 12 + 1
                Y_local_1[cse_var_329] = Y_local_1[cse_var_329] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_330: T.int32 = i_2_1_s * 12 + 2
                Y_local_1[cse_var_330] = Y_local_1[cse_var_330] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_331: T.int32 = i_2_1_s * 12 + 3
                Y_local_1[cse_var_331] = Y_local_1[cse_var_331] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_332: T.int32 = i_2_1_s * 12 + 4
                Y_local_1[cse_var_332] = Y_local_1[cse_var_332] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[16]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_333: T.int32 = i_2_1_s * 12 + 5
                Y_local_1[cse_var_333] = Y_local_1[cse_var_333] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[17]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_334: T.int32 = i_2_1_s * 12 + 6
                Y_local_1[cse_var_334] = Y_local_1[cse_var_334] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[18]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_335: T.int32 = i_2_1_s * 12 + 7
                Y_local_1[cse_var_335] = Y_local_1[cse_var_335] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[19]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_336: T.int32 = i_2_1_s * 12 + 8
                Y_local_1[cse_var_336] = Y_local_1[cse_var_336] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[20]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_337: T.int32 = i_2_1_s * 12 + 9
                Y_local_1[cse_var_337] = Y_local_1[cse_var_337] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[21]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_338: T.int32 = i_2_1_s * 12 + 10
                Y_local_1[cse_var_338] = Y_local_1[cse_var_338] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[22]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_339: T.int32 = i_2_1_s * 12 + 11
                Y_local_1[cse_var_339] = Y_local_1[cse_var_339] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[23]
        for ax1_1_s in T.serial(4):
            if ax1_1_s < 2:
                A_shared_dyn_local_1[ax1_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 1728]
        for ax1_0 in T.serial(3):
            cse_var_340: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_340 + 12:cse_var_340 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_340) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_340) // 8) % 8 * 4 + 3456 - blockIdx_x % 8 * 48 // 64 * 64:(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_340) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_340) // 8) % 8 * 4 + 3456 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_341: T.int32 = i_2_1_s * 12
                Y_local_1[cse_var_341] = Y_local_1[cse_var_341] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_342: T.int32 = i_2_1_s * 12 + 1
                Y_local_1[cse_var_342] = Y_local_1[cse_var_342] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_343: T.int32 = i_2_1_s * 12 + 2
                Y_local_1[cse_var_343] = Y_local_1[cse_var_343] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_344: T.int32 = i_2_1_s * 12 + 3
                Y_local_1[cse_var_344] = Y_local_1[cse_var_344] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_345: T.int32 = i_2_1_s * 12 + 4
                Y_local_1[cse_var_345] = Y_local_1[cse_var_345] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_346: T.int32 = i_2_1_s * 12 + 5
                Y_local_1[cse_var_346] = Y_local_1[cse_var_346] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_347: T.int32 = i_2_1_s * 12 + 6
                Y_local_1[cse_var_347] = Y_local_1[cse_var_347] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_348: T.int32 = i_2_1_s * 12 + 7
                Y_local_1[cse_var_348] = Y_local_1[cse_var_348] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_349: T.int32 = i_2_1_s * 12 + 8
                Y_local_1[cse_var_349] = Y_local_1[cse_var_349] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[8]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_350: T.int32 = i_2_1_s * 12 + 9
                Y_local_1[cse_var_350] = Y_local_1[cse_var_350] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[9]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_351: T.int32 = i_2_1_s * 12 + 10
                Y_local_1[cse_var_351] = Y_local_1[cse_var_351] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[10]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_352: T.int32 = i_2_1_s * 12 + 11
                Y_local_1[cse_var_352] = Y_local_1[cse_var_352] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[11]
        for ax1_1_s in T.serial(4):
            if ax1_1_s < 2:
                A_shared_dyn_local_1[ax1_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 1792]
        for ax1_0 in T.serial(3):
            cse_var_353: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_353:cse_var_353 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_353) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_353) // 8) % 8 * 4 + 3584 - blockIdx_x % 8 * 48 // 64 * 64:(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_353) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_353) // 8) % 8 * 4 + 3584 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_354: T.int32 = i_2_1_s * 12
                Y_local_1[cse_var_354] = Y_local_1[cse_var_354] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_355: T.int32 = i_2_1_s * 12 + 1
                Y_local_1[cse_var_355] = Y_local_1[cse_var_355] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_356: T.int32 = i_2_1_s * 12 + 2
                Y_local_1[cse_var_356] = Y_local_1[cse_var_356] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_357: T.int32 = i_2_1_s * 12 + 3
                Y_local_1[cse_var_357] = Y_local_1[cse_var_357] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_358: T.int32 = i_2_1_s * 12 + 4
                Y_local_1[cse_var_358] = Y_local_1[cse_var_358] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[16]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_359: T.int32 = i_2_1_s * 12 + 5
                Y_local_1[cse_var_359] = Y_local_1[cse_var_359] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[17]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_360: T.int32 = i_2_1_s * 12 + 6
                Y_local_1[cse_var_360] = Y_local_1[cse_var_360] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[18]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_361: T.int32 = i_2_1_s * 12 + 7
                Y_local_1[cse_var_361] = Y_local_1[cse_var_361] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[19]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_362: T.int32 = i_2_1_s * 12 + 8
                Y_local_1[cse_var_362] = Y_local_1[cse_var_362] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[20]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_363: T.int32 = i_2_1_s * 12 + 9
                Y_local_1[cse_var_363] = Y_local_1[cse_var_363] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[21]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_364: T.int32 = i_2_1_s * 12 + 10
                Y_local_1[cse_var_364] = Y_local_1[cse_var_364] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[22]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_365: T.int32 = i_2_1_s * 12 + 11
                Y_local_1[cse_var_365] = Y_local_1[cse_var_365] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[23]
        for ax1_1_s in T.serial(4):
            if ax1_1_s < 2:
                A_shared_dyn_local_1[ax1_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 1856]
        for ax1_0 in T.serial(3):
            cse_var_366: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_366 + 12:cse_var_366 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_366) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_366) // 8) % 8 * 4 + 3712 - blockIdx_x % 8 * 48 // 64 * 64:(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_366) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_366) // 8) % 8 * 4 + 3712 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_367: T.int32 = i_2_1_s * 12
                Y_local_1[cse_var_367] = Y_local_1[cse_var_367] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_368: T.int32 = i_2_1_s * 12 + 1
                Y_local_1[cse_var_368] = Y_local_1[cse_var_368] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_369: T.int32 = i_2_1_s * 12 + 2
                Y_local_1[cse_var_369] = Y_local_1[cse_var_369] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_370: T.int32 = i_2_1_s * 12 + 3
                Y_local_1[cse_var_370] = Y_local_1[cse_var_370] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_371: T.int32 = i_2_1_s * 12 + 4
                Y_local_1[cse_var_371] = Y_local_1[cse_var_371] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_372: T.int32 = i_2_1_s * 12 + 5
                Y_local_1[cse_var_372] = Y_local_1[cse_var_372] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_373: T.int32 = i_2_1_s * 12 + 6
                Y_local_1[cse_var_373] = Y_local_1[cse_var_373] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_374: T.int32 = i_2_1_s * 12 + 7
                Y_local_1[cse_var_374] = Y_local_1[cse_var_374] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_375: T.int32 = i_2_1_s * 12 + 8
                Y_local_1[cse_var_375] = Y_local_1[cse_var_375] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[8]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_376: T.int32 = i_2_1_s * 12 + 9
                Y_local_1[cse_var_376] = Y_local_1[cse_var_376] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[9]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_377: T.int32 = i_2_1_s * 12 + 10
                Y_local_1[cse_var_377] = Y_local_1[cse_var_377] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[10]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_378: T.int32 = i_2_1_s * 12 + 11
                Y_local_1[cse_var_378] = Y_local_1[cse_var_378] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[11]
        for ax1_1_s in T.serial(4):
            if ax1_1_s < 2:
                A_shared_dyn_local_1[ax1_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 1920]
        for ax1_0 in T.serial(3):
            cse_var_379: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_379:cse_var_379 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_379) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_379) // 8) % 8 * 4 + 3840 - blockIdx_x % 8 * 48 // 64 * 64:(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_379) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_379) // 8) % 8 * 4 + 3840 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_380: T.int32 = i_2_1_s * 12
                Y_local_1[cse_var_380] = Y_local_1[cse_var_380] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_381: T.int32 = i_2_1_s * 12 + 1
                Y_local_1[cse_var_381] = Y_local_1[cse_var_381] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_382: T.int32 = i_2_1_s * 12 + 2
                Y_local_1[cse_var_382] = Y_local_1[cse_var_382] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_383: T.int32 = i_2_1_s * 12 + 3
                Y_local_1[cse_var_383] = Y_local_1[cse_var_383] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_384: T.int32 = i_2_1_s * 12 + 4
                Y_local_1[cse_var_384] = Y_local_1[cse_var_384] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[16]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_385: T.int32 = i_2_1_s * 12 + 5
                Y_local_1[cse_var_385] = Y_local_1[cse_var_385] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[17]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_386: T.int32 = i_2_1_s * 12 + 6
                Y_local_1[cse_var_386] = Y_local_1[cse_var_386] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[18]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_387: T.int32 = i_2_1_s * 12 + 7
                Y_local_1[cse_var_387] = Y_local_1[cse_var_387] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[19]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_388: T.int32 = i_2_1_s * 12 + 8
                Y_local_1[cse_var_388] = Y_local_1[cse_var_388] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[20]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_389: T.int32 = i_2_1_s * 12 + 9
                Y_local_1[cse_var_389] = Y_local_1[cse_var_389] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[21]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_390: T.int32 = i_2_1_s * 12 + 10
                Y_local_1[cse_var_390] = Y_local_1[cse_var_390] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[22]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_391: T.int32 = i_2_1_s * 12 + 11
                Y_local_1[cse_var_391] = Y_local_1[cse_var_391] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[23]
        for ax1_1_s in T.serial(4):
            if ax1_1_s < 2:
                A_shared_dyn_local_1[ax1_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 32 * 32 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 32 // 8 * 4 + threadIdx_x % 4 // 2 * 2 + ax1_1_s + 1984]
        for ax1_0 in T.serial(3):
            cse_var_392: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_392 + 12:cse_var_392 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_392) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_392) // 8) % 8 * 4 + 3968 - blockIdx_x % 8 * 48 // 64 * 64:(blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_392) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 6 + threadIdx_x // 64 * 3 + (threadIdx_x % 2 * 12 + cse_var_392) // 8) % 8 * 4 + 3968 - blockIdx_x % 8 * 48 // 64 * 64 + 4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_393: T.int32 = i_2_1_s * 12
                Y_local_1[cse_var_393] = Y_local_1[cse_var_393] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_394: T.int32 = i_2_1_s * 12 + 1
                Y_local_1[cse_var_394] = Y_local_1[cse_var_394] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_395: T.int32 = i_2_1_s * 12 + 2
                Y_local_1[cse_var_395] = Y_local_1[cse_var_395] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_396: T.int32 = i_2_1_s * 12 + 3
                Y_local_1[cse_var_396] = Y_local_1[cse_var_396] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_397: T.int32 = i_2_1_s * 12 + 4
                Y_local_1[cse_var_397] = Y_local_1[cse_var_397] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_398: T.int32 = i_2_1_s * 12 + 5
                Y_local_1[cse_var_398] = Y_local_1[cse_var_398] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_399: T.int32 = i_2_1_s * 12 + 6
                Y_local_1[cse_var_399] = Y_local_1[cse_var_399] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_400: T.int32 = i_2_1_s * 12 + 7
                Y_local_1[cse_var_400] = Y_local_1[cse_var_400] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_401: T.int32 = i_2_1_s * 12 + 8
                Y_local_1[cse_var_401] = Y_local_1[cse_var_401] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[8]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_402: T.int32 = i_2_1_s * 12 + 9
                Y_local_1[cse_var_402] = Y_local_1[cse_var_402] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[9]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_403: T.int32 = i_2_1_s * 12 + 10
                Y_local_1[cse_var_403] = Y_local_1[cse_var_403] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[10]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_404: T.int32 = i_2_1_s * 12 + 11
                Y_local_1[cse_var_404] = Y_local_1[cse_var_404] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[11]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_405: T.int32 = i_2_1_s * 12
                Y_local_1[cse_var_405] = Y_local_1[cse_var_405] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_406: T.int32 = i_2_1_s * 12 + 1
                Y_local_1[cse_var_406] = Y_local_1[cse_var_406] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_407: T.int32 = i_2_1_s * 12 + 2
                Y_local_1[cse_var_407] = Y_local_1[cse_var_407] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_408: T.int32 = i_2_1_s * 12 + 3
                Y_local_1[cse_var_408] = Y_local_1[cse_var_408] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_409: T.int32 = i_2_1_s * 12 + 4
                Y_local_1[cse_var_409] = Y_local_1[cse_var_409] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[16]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_410: T.int32 = i_2_1_s * 12 + 5
                Y_local_1[cse_var_410] = Y_local_1[cse_var_410] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[17]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_411: T.int32 = i_2_1_s * 12 + 6
                Y_local_1[cse_var_411] = Y_local_1[cse_var_411] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[18]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_412: T.int32 = i_2_1_s * 12 + 7
                Y_local_1[cse_var_412] = Y_local_1[cse_var_412] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[19]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_413: T.int32 = i_2_1_s * 12 + 8
                Y_local_1[cse_var_413] = Y_local_1[cse_var_413] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[20]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_414: T.int32 = i_2_1_s * 12 + 9
                Y_local_1[cse_var_414] = Y_local_1[cse_var_414] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[21]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_415: T.int32 = i_2_1_s * 12 + 10
                Y_local_1[cse_var_415] = Y_local_1[cse_var_415] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[22]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_416: T.int32 = i_2_1_s * 12 + 11
                Y_local_1[cse_var_416] = Y_local_1[cse_var_416] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[23]
        for ax1_0 in T.serial(3):
            cse_var_417: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 8 * 24576 + threadIdx_x % 64 // 2 * 768 + blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_417:blockIdx_x // 8 * 24576 + threadIdx_x % 64 // 2 * 768 + blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_417 + 4] = Y_local_1[cse_var_417:cse_var_417 + 4]
        for ax1_0 in T.serial(3):
            cse_var_418: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 8 * 24576 + threadIdx_x % 64 // 2 * 768 + blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_418 + 384:blockIdx_x // 8 * 24576 + threadIdx_x % 64 // 2 * 768 + blockIdx_x % 8 * 48 + threadIdx_x // 64 * 24 + threadIdx_x % 2 * 12 + cse_var_418 + 384 + 4] = Y_local_1[cse_var_418 + 12:cse_var_418 + 12 + 4]
    

