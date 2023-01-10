# from tvm.script import tir as T
@tvm.script.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer[(1152, 1152), "float32"], B: T.Buffer[(1152, 1152), "float32"], Y: T.Buffer[(1152, 1152), "float32"]):
        # function attr dict
        T.func_attr({"global_symbol": "main", "tir.noalias": True})
        # var definition
        threadIdx_x = T.env_thread("threadIdx.x")
        blockIdx_x = T.env_thread("blockIdx.x")
        # buffer definition
        A_1 = T.buffer_decl([1327104], dtype="float32", data=A.data)
        B_1 = T.buffer_decl([1327104], dtype="float32", data=B.data)
        Y_1 = T.buffer_decl([1327104], dtype="float32", data=Y.data)
        # body
        T.launch_thread(blockIdx_x, 64)
        Y_local = T.allocate([96], "float32", "local")
        Y_local_1 = T.buffer_decl([96], dtype="float32", data=Y_local, scope="local")
        A_shared_dyn = T.allocate([2880], "float32", "shared.dyn")
        A_shared_dyn_1 = T.buffer_decl([2880], dtype="float32", data=A_shared_dyn, scope="shared.dyn")
        B_shared_dyn = T.allocate([3840], "float32", "shared.dyn")
        B_shared_dyn_1 = T.buffer_decl([3840], dtype="float32", data=B_shared_dyn, scope="shared.dyn")
        A_shared_dyn_local = T.allocate([12], "float32", "local")
        A_shared_dyn_local_1 = T.buffer_decl([12], dtype="float32", data=A_shared_dyn_local, scope="local")
        B_shared_dyn_local = T.allocate([32], "float32", "local")
        B_shared_dyn_local_1 = T.buffer_decl([32], dtype="float32", data=B_shared_dyn_local, scope="local")
        T.launch_thread(threadIdx_x, 216)
        Y_local_1[0] = T.float32(0)
        Y_local_1[16] = T.float32(0)
        Y_local_1[32] = T.float32(0)
        Y_local_1[48] = T.float32(0)
        Y_local_1[64] = T.float32(0)
        Y_local_1[80] = T.float32(0)
        Y_local_1[1] = T.float32(0)
        Y_local_1[17] = T.float32(0)
        Y_local_1[33] = T.float32(0)
        Y_local_1[49] = T.float32(0)
        Y_local_1[65] = T.float32(0)
        Y_local_1[81] = T.float32(0)
        Y_local_1[2] = T.float32(0)
        Y_local_1[18] = T.float32(0)
        Y_local_1[34] = T.float32(0)
        Y_local_1[50] = T.float32(0)
        Y_local_1[66] = T.float32(0)
        Y_local_1[82] = T.float32(0)
        Y_local_1[3] = T.float32(0)
        Y_local_1[19] = T.float32(0)
        Y_local_1[35] = T.float32(0)
        Y_local_1[51] = T.float32(0)
        Y_local_1[67] = T.float32(0)
        Y_local_1[83] = T.float32(0)
        Y_local_1[4] = T.float32(0)
        Y_local_1[20] = T.float32(0)
        Y_local_1[36] = T.float32(0)
        Y_local_1[52] = T.float32(0)
        Y_local_1[68] = T.float32(0)
        Y_local_1[84] = T.float32(0)
        Y_local_1[5] = T.float32(0)
        Y_local_1[21] = T.float32(0)
        Y_local_1[37] = T.float32(0)
        Y_local_1[53] = T.float32(0)
        Y_local_1[69] = T.float32(0)
        Y_local_1[85] = T.float32(0)
        Y_local_1[6] = T.float32(0)
        Y_local_1[22] = T.float32(0)
        Y_local_1[38] = T.float32(0)
        Y_local_1[54] = T.float32(0)
        Y_local_1[70] = T.float32(0)
        Y_local_1[86] = T.float32(0)
        Y_local_1[7] = T.float32(0)
        Y_local_1[23] = T.float32(0)
        Y_local_1[39] = T.float32(0)
        Y_local_1[55] = T.float32(0)
        Y_local_1[71] = T.float32(0)
        Y_local_1[87] = T.float32(0)
        Y_local_1[8] = T.float32(0)
        Y_local_1[24] = T.float32(0)
        Y_local_1[40] = T.float32(0)
        Y_local_1[56] = T.float32(0)
        Y_local_1[72] = T.float32(0)
        Y_local_1[88] = T.float32(0)
        Y_local_1[9] = T.float32(0)
        Y_local_1[25] = T.float32(0)
        Y_local_1[41] = T.float32(0)
        Y_local_1[57] = T.float32(0)
        Y_local_1[73] = T.float32(0)
        Y_local_1[89] = T.float32(0)
        Y_local_1[10] = T.float32(0)
        Y_local_1[26] = T.float32(0)
        Y_local_1[42] = T.float32(0)
        Y_local_1[58] = T.float32(0)
        Y_local_1[74] = T.float32(0)
        Y_local_1[90] = T.float32(0)
        Y_local_1[11] = T.float32(0)
        Y_local_1[27] = T.float32(0)
        Y_local_1[43] = T.float32(0)
        Y_local_1[59] = T.float32(0)
        Y_local_1[75] = T.float32(0)
        Y_local_1[91] = T.float32(0)
        Y_local_1[12] = T.float32(0)
        Y_local_1[28] = T.float32(0)
        Y_local_1[44] = T.float32(0)
        Y_local_1[60] = T.float32(0)
        Y_local_1[76] = T.float32(0)
        Y_local_1[92] = T.float32(0)
        Y_local_1[13] = T.float32(0)
        Y_local_1[29] = T.float32(0)
        Y_local_1[45] = T.float32(0)
        Y_local_1[61] = T.float32(0)
        Y_local_1[77] = T.float32(0)
        Y_local_1[93] = T.float32(0)
        Y_local_1[14] = T.float32(0)
        Y_local_1[30] = T.float32(0)
        Y_local_1[46] = T.float32(0)
        Y_local_1[62] = T.float32(0)
        Y_local_1[78] = T.float32(0)
        Y_local_1[94] = T.float32(0)
        Y_local_1[15] = T.float32(0)
        Y_local_1[31] = T.float32(0)
        Y_local_1[47] = T.float32(0)
        Y_local_1[63] = T.float32(0)
        Y_local_1[79] = T.float32(0)
        Y_local_1[95] = T.float32(0)
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                for ax0_ax1_fused_2_s in T.serial(3):
                    if threadIdx_x < 192:
                        A_shared_dyn_1[threadIdx_x * 3 + ax0_ax1_fused_2_s] = A_1[blockIdx_x // 8 * 165888 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) // 4 * 1152 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 4]
            T.attr(0, "async_scope", 1)
            for ax0_ax1_fused_2_s in T.serial(3):
                if threadIdx_x < 192:
                    B_shared_dyn_1[threadIdx_x // 48 * 192 + (blockIdx_x % 8 * 9 + (threadIdx_x % 48 * 3 + ax0_ax1_fused_2_s) // 16) // 4 * 64 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 8 // 4 * 32 + (blockIdx_x % 8 * 2 + (threadIdx_x % 48 * 3 + ax0_ax1_fused_2_s) // 8) % 8 * 4 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 4 - blockIdx_x % 8 * 144 // 64 * 64] = B_1[threadIdx_x // 48 * 1152 + blockIdx_x % 8 * 144 + threadIdx_x % 48 * 3 + ax0_ax1_fused_2_s]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                for ax0_ax1_fused_2_s in T.serial(3):
                    if threadIdx_x < 192:
                        A_shared_dyn_1[threadIdx_x * 3 + ax0_ax1_fused_2_s + 576] = A_1[blockIdx_x // 8 * 165888 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) // 4 * 1152 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 4 + 4]
            T.attr(0, "async_scope", 1)
            for ax0_ax1_fused_2_s in T.serial(3):
                if threadIdx_x < 192:
                    B_shared_dyn_1[threadIdx_x // 48 * 192 + (blockIdx_x % 8 * 9 + (threadIdx_x % 48 * 3 + ax0_ax1_fused_2_s) // 16) // 4 * 64 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 8 // 4 * 32 + (blockIdx_x % 8 * 2 + (threadIdx_x % 48 * 3 + ax0_ax1_fused_2_s) // 8) % 8 * 4 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 4 + 768 - blockIdx_x % 8 * 144 // 64 * 64] = B_1[threadIdx_x // 48 * 1152 + blockIdx_x % 8 * 144 + threadIdx_x % 48 * 3 + ax0_ax1_fused_2_s + 4608]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                for ax0_ax1_fused_2_s in T.serial(3):
                    if threadIdx_x < 192:
                        A_shared_dyn_1[threadIdx_x * 3 + ax0_ax1_fused_2_s + 1152] = A_1[blockIdx_x // 8 * 165888 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) // 4 * 1152 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 4 + 8]
            T.attr(0, "async_scope", 1)
            for ax0_ax1_fused_2_s in T.serial(3):
                if threadIdx_x < 192:
                    B_shared_dyn_1[threadIdx_x // 48 * 192 + (blockIdx_x % 8 * 9 + (threadIdx_x % 48 * 3 + ax0_ax1_fused_2_s) // 16) // 4 * 64 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 8 // 4 * 32 + (blockIdx_x % 8 * 2 + (threadIdx_x % 48 * 3 + ax0_ax1_fused_2_s) // 8) % 8 * 4 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 4 + 1536 - blockIdx_x % 8 * 144 // 64 * 64] = B_1[threadIdx_x // 48 * 1152 + blockIdx_x % 8 * 144 + threadIdx_x % 48 * 3 + ax0_ax1_fused_2_s + 9216]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                for ax0_ax1_fused_2_s in T.serial(3):
                    if threadIdx_x < 192:
                        A_shared_dyn_1[threadIdx_x * 3 + ax0_ax1_fused_2_s + 1728] = A_1[blockIdx_x // 8 * 165888 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) // 4 * 1152 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 4 + 12]
            T.attr(0, "async_scope", 1)
            for ax0_ax1_fused_2_s in T.serial(3):
                if threadIdx_x < 192:
                    B_shared_dyn_1[threadIdx_x // 48 * 192 + (blockIdx_x % 8 * 9 + (threadIdx_x % 48 * 3 + ax0_ax1_fused_2_s) // 16) // 4 * 64 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 8 // 4 * 32 + (blockIdx_x % 8 * 2 + (threadIdx_x % 48 * 3 + ax0_ax1_fused_2_s) // 8) % 8 * 4 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 4 + 2304 - blockIdx_x % 8 * 144 // 64 * 64] = B_1[threadIdx_x // 48 * 1152 + blockIdx_x % 8 * 144 + threadIdx_x % 48 * 3 + ax0_ax1_fused_2_s + 13824]
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 3)
            for ax0_0, ax0_1_s in T.grid(2, 4):
                if ax0_0 * 2 + ax0_1_s // 2 < 3:
                    A_shared_dyn_local_1[ax0_0 * 4 + ax0_1_s] = A_shared_dyn_1[threadIdx_x // 27 * 72 + threadIdx_x % 3 * 24 + ax0_0 * 16 + ax0_1_s * 4]
            for ax1_0 in T.serial(4):
                cse_var_1: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_1:cse_var_1 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_1) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_1) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
        for k_0 in T.serial(284):
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    for ax0_ax1_fused_2_s in T.serial(3):
                        if threadIdx_x < 192:
                            A_shared_dyn_1[(k_0 + 4) % 5 * 576 + threadIdx_x * 3 + ax0_ax1_fused_2_s] = A_1[blockIdx_x // 8 * 165888 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) // 4 * 1152 + k_0 * 4 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 4 + 16]
                T.attr(0, "async_scope", 1)
                for ax0_ax1_fused_2_s in T.serial(3):
                    if threadIdx_x < 192:
                        B_shared_dyn_1[(k_0 + 4) % 5 * 768 + threadIdx_x // 48 * 192 + (blockIdx_x % 8 * 9 + (threadIdx_x % 48 * 3 + ax0_ax1_fused_2_s) // 16) // 4 * 64 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 8 // 4 * 32 + (blockIdx_x % 8 * 2 + (threadIdx_x % 48 * 3 + ax0_ax1_fused_2_s) // 8) % 8 * 4 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 4 - blockIdx_x % 8 * 144 // 64 * 64] = B_1[k_0 * 4608 + threadIdx_x // 48 * 1152 + blockIdx_x % 8 * 144 + threadIdx_x % 48 * 3 + ax0_ax1_fused_2_s + 18432]
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 3)
                for ax0_0, ax0_1_s in T.grid(2, 4):
                    if ax0_0 * 2 + ax0_1_s // 2 < 3:
                        A_shared_dyn_local_1[ax0_0 * 4 + ax0_1_s + 6] = A_shared_dyn_1[k_0 % 5 * 576 + threadIdx_x // 27 * 72 + threadIdx_x % 3 * 24 + ax0_0 * 16 + ax0_1_s * 4 + 1]
                for ax1_0 in T.serial(4):
                    cse_var_2: T.int32 = ax1_0 * 4
                    B_shared_dyn_local_1[cse_var_2 + 16:cse_var_2 + 16 + 4] = B_shared_dyn_1[k_0 % 5 * 768 + (blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_2) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 192 - blockIdx_x % 8 * 144 // 64 * 64:k_0 % 5 * 768 + (blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_2) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 192 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
                for i_2_1_s in T.serial(4):
                    cse_var_3: T.int32 = i_2_1_s * 16
                    Y_local_1[cse_var_3] = Y_local_1[cse_var_3] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_4: T.int32 = i_2_1_s * 16 + 64
                        Y_local_1[cse_var_4] = Y_local_1[cse_var_4] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[0]
                for i_2_1_s in T.serial(4):
                    cse_var_5: T.int32 = i_2_1_s * 16 + 1
                    Y_local_1[cse_var_5] = Y_local_1[cse_var_5] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_6: T.int32 = i_2_1_s * 16 + 65
                        Y_local_1[cse_var_6] = Y_local_1[cse_var_6] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[1]
                for i_2_1_s in T.serial(4):
                    cse_var_7: T.int32 = i_2_1_s * 16 + 2
                    Y_local_1[cse_var_7] = Y_local_1[cse_var_7] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_8: T.int32 = i_2_1_s * 16 + 66
                        Y_local_1[cse_var_8] = Y_local_1[cse_var_8] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[2]
                for i_2_1_s in T.serial(4):
                    cse_var_9: T.int32 = i_2_1_s * 16 + 3
                    Y_local_1[cse_var_9] = Y_local_1[cse_var_9] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_10: T.int32 = i_2_1_s * 16 + 67
                        Y_local_1[cse_var_10] = Y_local_1[cse_var_10] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[3]
                for i_2_1_s in T.serial(4):
                    cse_var_11: T.int32 = i_2_1_s * 16 + 4
                    Y_local_1[cse_var_11] = Y_local_1[cse_var_11] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_12: T.int32 = i_2_1_s * 16 + 68
                        Y_local_1[cse_var_12] = Y_local_1[cse_var_12] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[4]
                for i_2_1_s in T.serial(4):
                    cse_var_13: T.int32 = i_2_1_s * 16 + 5
                    Y_local_1[cse_var_13] = Y_local_1[cse_var_13] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_14: T.int32 = i_2_1_s * 16 + 69
                        Y_local_1[cse_var_14] = Y_local_1[cse_var_14] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[5]
                for i_2_1_s in T.serial(4):
                    cse_var_15: T.int32 = i_2_1_s * 16 + 6
                    Y_local_1[cse_var_15] = Y_local_1[cse_var_15] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_16: T.int32 = i_2_1_s * 16 + 70
                        Y_local_1[cse_var_16] = Y_local_1[cse_var_16] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[6]
                for i_2_1_s in T.serial(4):
                    cse_var_17: T.int32 = i_2_1_s * 16 + 7
                    Y_local_1[cse_var_17] = Y_local_1[cse_var_17] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_18: T.int32 = i_2_1_s * 16 + 71
                        Y_local_1[cse_var_18] = Y_local_1[cse_var_18] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[7]
                for i_2_1_s in T.serial(4):
                    cse_var_19: T.int32 = i_2_1_s * 16 + 8
                    Y_local_1[cse_var_19] = Y_local_1[cse_var_19] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[8]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_20: T.int32 = i_2_1_s * 16 + 72
                        Y_local_1[cse_var_20] = Y_local_1[cse_var_20] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[8]
                for i_2_1_s in T.serial(4):
                    cse_var_21: T.int32 = i_2_1_s * 16 + 9
                    Y_local_1[cse_var_21] = Y_local_1[cse_var_21] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[9]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_22: T.int32 = i_2_1_s * 16 + 73
                        Y_local_1[cse_var_22] = Y_local_1[cse_var_22] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[9]
                for i_2_1_s in T.serial(4):
                    cse_var_23: T.int32 = i_2_1_s * 16 + 10
                    Y_local_1[cse_var_23] = Y_local_1[cse_var_23] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[10]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_24: T.int32 = i_2_1_s * 16 + 74
                        Y_local_1[cse_var_24] = Y_local_1[cse_var_24] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[10]
                for i_2_1_s in T.serial(4):
                    cse_var_25: T.int32 = i_2_1_s * 16 + 11
                    Y_local_1[cse_var_25] = Y_local_1[cse_var_25] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[11]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_26: T.int32 = i_2_1_s * 16 + 75
                        Y_local_1[cse_var_26] = Y_local_1[cse_var_26] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[11]
                for i_2_1_s in T.serial(4):
                    cse_var_27: T.int32 = i_2_1_s * 16 + 12
                    Y_local_1[cse_var_27] = Y_local_1[cse_var_27] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[12]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_28: T.int32 = i_2_1_s * 16 + 76
                        Y_local_1[cse_var_28] = Y_local_1[cse_var_28] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[12]
                for i_2_1_s in T.serial(4):
                    cse_var_29: T.int32 = i_2_1_s * 16 + 13
                    Y_local_1[cse_var_29] = Y_local_1[cse_var_29] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[13]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_30: T.int32 = i_2_1_s * 16 + 77
                        Y_local_1[cse_var_30] = Y_local_1[cse_var_30] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[13]
                for i_2_1_s in T.serial(4):
                    cse_var_31: T.int32 = i_2_1_s * 16 + 14
                    Y_local_1[cse_var_31] = Y_local_1[cse_var_31] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[14]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_32: T.int32 = i_2_1_s * 16 + 78
                        Y_local_1[cse_var_32] = Y_local_1[cse_var_32] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[14]
                for i_2_1_s in T.serial(4):
                    cse_var_33: T.int32 = i_2_1_s * 16 + 15
                    Y_local_1[cse_var_33] = Y_local_1[cse_var_33] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[15]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_34: T.int32 = i_2_1_s * 16 + 79
                        Y_local_1[cse_var_34] = Y_local_1[cse_var_34] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[15]
                for ax0_0, ax0_1_s in T.grid(2, 4):
                    if ax0_0 * 2 + ax0_1_s // 2 < 3:
                        A_shared_dyn_local_1[ax0_0 * 4 + ax0_1_s] = A_shared_dyn_1[k_0 % 5 * 576 + threadIdx_x // 27 * 72 + threadIdx_x % 3 * 24 + ax0_0 * 16 + ax0_1_s * 4 + 2]
                for ax1_0 in T.serial(4):
                    cse_var_35: T.int32 = ax1_0 * 4
                    B_shared_dyn_local_1[cse_var_35:cse_var_35 + 4] = B_shared_dyn_1[k_0 % 5 * 768 + (blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_35) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 384 - blockIdx_x % 8 * 144 // 64 * 64:k_0 % 5 * 768 + (blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_35) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 384 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
                for i_2_1_s in T.serial(4):
                    cse_var_36: T.int32 = i_2_1_s * 16
                    Y_local_1[cse_var_36] = Y_local_1[cse_var_36] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[16]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_37: T.int32 = i_2_1_s * 16 + 64
                        Y_local_1[cse_var_37] = Y_local_1[cse_var_37] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[16]
                for i_2_1_s in T.serial(4):
                    cse_var_38: T.int32 = i_2_1_s * 16 + 1
                    Y_local_1[cse_var_38] = Y_local_1[cse_var_38] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[17]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_39: T.int32 = i_2_1_s * 16 + 65
                        Y_local_1[cse_var_39] = Y_local_1[cse_var_39] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[17]
                for i_2_1_s in T.serial(4):
                    cse_var_40: T.int32 = i_2_1_s * 16 + 2
                    Y_local_1[cse_var_40] = Y_local_1[cse_var_40] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[18]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_41: T.int32 = i_2_1_s * 16 + 66
                        Y_local_1[cse_var_41] = Y_local_1[cse_var_41] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[18]
                for i_2_1_s in T.serial(4):
                    cse_var_42: T.int32 = i_2_1_s * 16 + 3
                    Y_local_1[cse_var_42] = Y_local_1[cse_var_42] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[19]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_43: T.int32 = i_2_1_s * 16 + 67
                        Y_local_1[cse_var_43] = Y_local_1[cse_var_43] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[19]
                for i_2_1_s in T.serial(4):
                    cse_var_44: T.int32 = i_2_1_s * 16 + 4
                    Y_local_1[cse_var_44] = Y_local_1[cse_var_44] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[20]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_45: T.int32 = i_2_1_s * 16 + 68
                        Y_local_1[cse_var_45] = Y_local_1[cse_var_45] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[20]
                for i_2_1_s in T.serial(4):
                    cse_var_46: T.int32 = i_2_1_s * 16 + 5
                    Y_local_1[cse_var_46] = Y_local_1[cse_var_46] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[21]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_47: T.int32 = i_2_1_s * 16 + 69
                        Y_local_1[cse_var_47] = Y_local_1[cse_var_47] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[21]
                for i_2_1_s in T.serial(4):
                    cse_var_48: T.int32 = i_2_1_s * 16 + 6
                    Y_local_1[cse_var_48] = Y_local_1[cse_var_48] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[22]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_49: T.int32 = i_2_1_s * 16 + 70
                        Y_local_1[cse_var_49] = Y_local_1[cse_var_49] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[22]
                for i_2_1_s in T.serial(4):
                    cse_var_50: T.int32 = i_2_1_s * 16 + 7
                    Y_local_1[cse_var_50] = Y_local_1[cse_var_50] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[23]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_51: T.int32 = i_2_1_s * 16 + 71
                        Y_local_1[cse_var_51] = Y_local_1[cse_var_51] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[23]
                for i_2_1_s in T.serial(4):
                    cse_var_52: T.int32 = i_2_1_s * 16 + 8
                    Y_local_1[cse_var_52] = Y_local_1[cse_var_52] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[24]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_53: T.int32 = i_2_1_s * 16 + 72
                        Y_local_1[cse_var_53] = Y_local_1[cse_var_53] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[24]
                for i_2_1_s in T.serial(4):
                    cse_var_54: T.int32 = i_2_1_s * 16 + 9
                    Y_local_1[cse_var_54] = Y_local_1[cse_var_54] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[25]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_55: T.int32 = i_2_1_s * 16 + 73
                        Y_local_1[cse_var_55] = Y_local_1[cse_var_55] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[25]
                for i_2_1_s in T.serial(4):
                    cse_var_56: T.int32 = i_2_1_s * 16 + 10
                    Y_local_1[cse_var_56] = Y_local_1[cse_var_56] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[26]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_57: T.int32 = i_2_1_s * 16 + 74
                        Y_local_1[cse_var_57] = Y_local_1[cse_var_57] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[26]
                for i_2_1_s in T.serial(4):
                    cse_var_58: T.int32 = i_2_1_s * 16 + 11
                    Y_local_1[cse_var_58] = Y_local_1[cse_var_58] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[27]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_59: T.int32 = i_2_1_s * 16 + 75
                        Y_local_1[cse_var_59] = Y_local_1[cse_var_59] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[27]
                for i_2_1_s in T.serial(4):
                    cse_var_60: T.int32 = i_2_1_s * 16 + 12
                    Y_local_1[cse_var_60] = Y_local_1[cse_var_60] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[28]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_61: T.int32 = i_2_1_s * 16 + 76
                        Y_local_1[cse_var_61] = Y_local_1[cse_var_61] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[28]
                for i_2_1_s in T.serial(4):
                    cse_var_62: T.int32 = i_2_1_s * 16 + 13
                    Y_local_1[cse_var_62] = Y_local_1[cse_var_62] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[29]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_63: T.int32 = i_2_1_s * 16 + 77
                        Y_local_1[cse_var_63] = Y_local_1[cse_var_63] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[29]
                for i_2_1_s in T.serial(4):
                    cse_var_64: T.int32 = i_2_1_s * 16 + 14
                    Y_local_1[cse_var_64] = Y_local_1[cse_var_64] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[30]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_65: T.int32 = i_2_1_s * 16 + 78
                        Y_local_1[cse_var_65] = Y_local_1[cse_var_65] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[30]
                for i_2_1_s in T.serial(4):
                    cse_var_66: T.int32 = i_2_1_s * 16 + 15
                    Y_local_1[cse_var_66] = Y_local_1[cse_var_66] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[31]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_67: T.int32 = i_2_1_s * 16 + 79
                        Y_local_1[cse_var_67] = Y_local_1[cse_var_67] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[31]
                for ax0_0, ax0_1_s in T.grid(2, 4):
                    if ax0_0 * 2 + ax0_1_s // 2 < 3:
                        A_shared_dyn_local_1[ax0_0 * 4 + ax0_1_s + 6] = A_shared_dyn_1[k_0 % 5 * 576 + threadIdx_x // 27 * 72 + threadIdx_x % 3 * 24 + ax0_0 * 16 + ax0_1_s * 4 + 3]
                for ax1_0 in T.serial(4):
                    cse_var_68: T.int32 = ax1_0 * 4
                    B_shared_dyn_local_1[cse_var_68 + 16:cse_var_68 + 16 + 4] = B_shared_dyn_1[k_0 % 5 * 768 + (blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_68) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 576 - blockIdx_x % 8 * 144 // 64 * 64:k_0 % 5 * 768 + (blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_68) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 576 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
                for i_2_1_s in T.serial(4):
                    cse_var_69: T.int32 = i_2_1_s * 16
                    Y_local_1[cse_var_69] = Y_local_1[cse_var_69] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_70: T.int32 = i_2_1_s * 16 + 64
                        Y_local_1[cse_var_70] = Y_local_1[cse_var_70] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[0]
                for i_2_1_s in T.serial(4):
                    cse_var_71: T.int32 = i_2_1_s * 16 + 1
                    Y_local_1[cse_var_71] = Y_local_1[cse_var_71] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_72: T.int32 = i_2_1_s * 16 + 65
                        Y_local_1[cse_var_72] = Y_local_1[cse_var_72] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[1]
                for i_2_1_s in T.serial(4):
                    cse_var_73: T.int32 = i_2_1_s * 16 + 2
                    Y_local_1[cse_var_73] = Y_local_1[cse_var_73] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_74: T.int32 = i_2_1_s * 16 + 66
                        Y_local_1[cse_var_74] = Y_local_1[cse_var_74] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[2]
                for i_2_1_s in T.serial(4):
                    cse_var_75: T.int32 = i_2_1_s * 16 + 3
                    Y_local_1[cse_var_75] = Y_local_1[cse_var_75] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_76: T.int32 = i_2_1_s * 16 + 67
                        Y_local_1[cse_var_76] = Y_local_1[cse_var_76] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[3]
                for i_2_1_s in T.serial(4):
                    cse_var_77: T.int32 = i_2_1_s * 16 + 4
                    Y_local_1[cse_var_77] = Y_local_1[cse_var_77] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_78: T.int32 = i_2_1_s * 16 + 68
                        Y_local_1[cse_var_78] = Y_local_1[cse_var_78] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[4]
                for i_2_1_s in T.serial(4):
                    cse_var_79: T.int32 = i_2_1_s * 16 + 5
                    Y_local_1[cse_var_79] = Y_local_1[cse_var_79] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_80: T.int32 = i_2_1_s * 16 + 69
                        Y_local_1[cse_var_80] = Y_local_1[cse_var_80] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[5]
                for i_2_1_s in T.serial(4):
                    cse_var_81: T.int32 = i_2_1_s * 16 + 6
                    Y_local_1[cse_var_81] = Y_local_1[cse_var_81] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_82: T.int32 = i_2_1_s * 16 + 70
                        Y_local_1[cse_var_82] = Y_local_1[cse_var_82] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[6]
                for i_2_1_s in T.serial(4):
                    cse_var_83: T.int32 = i_2_1_s * 16 + 7
                    Y_local_1[cse_var_83] = Y_local_1[cse_var_83] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_84: T.int32 = i_2_1_s * 16 + 71
                        Y_local_1[cse_var_84] = Y_local_1[cse_var_84] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[7]
                for i_2_1_s in T.serial(4):
                    cse_var_85: T.int32 = i_2_1_s * 16 + 8
                    Y_local_1[cse_var_85] = Y_local_1[cse_var_85] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[8]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_86: T.int32 = i_2_1_s * 16 + 72
                        Y_local_1[cse_var_86] = Y_local_1[cse_var_86] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[8]
                for i_2_1_s in T.serial(4):
                    cse_var_87: T.int32 = i_2_1_s * 16 + 9
                    Y_local_1[cse_var_87] = Y_local_1[cse_var_87] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[9]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_88: T.int32 = i_2_1_s * 16 + 73
                        Y_local_1[cse_var_88] = Y_local_1[cse_var_88] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[9]
                for i_2_1_s in T.serial(4):
                    cse_var_89: T.int32 = i_2_1_s * 16 + 10
                    Y_local_1[cse_var_89] = Y_local_1[cse_var_89] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[10]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_90: T.int32 = i_2_1_s * 16 + 74
                        Y_local_1[cse_var_90] = Y_local_1[cse_var_90] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[10]
                for i_2_1_s in T.serial(4):
                    cse_var_91: T.int32 = i_2_1_s * 16 + 11
                    Y_local_1[cse_var_91] = Y_local_1[cse_var_91] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[11]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_92: T.int32 = i_2_1_s * 16 + 75
                        Y_local_1[cse_var_92] = Y_local_1[cse_var_92] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[11]
                for i_2_1_s in T.serial(4):
                    cse_var_93: T.int32 = i_2_1_s * 16 + 12
                    Y_local_1[cse_var_93] = Y_local_1[cse_var_93] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[12]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_94: T.int32 = i_2_1_s * 16 + 76
                        Y_local_1[cse_var_94] = Y_local_1[cse_var_94] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[12]
                for i_2_1_s in T.serial(4):
                    cse_var_95: T.int32 = i_2_1_s * 16 + 13
                    Y_local_1[cse_var_95] = Y_local_1[cse_var_95] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[13]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_96: T.int32 = i_2_1_s * 16 + 77
                        Y_local_1[cse_var_96] = Y_local_1[cse_var_96] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[13]
                for i_2_1_s in T.serial(4):
                    cse_var_97: T.int32 = i_2_1_s * 16 + 14
                    Y_local_1[cse_var_97] = Y_local_1[cse_var_97] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[14]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_98: T.int32 = i_2_1_s * 16 + 78
                        Y_local_1[cse_var_98] = Y_local_1[cse_var_98] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[14]
                for i_2_1_s in T.serial(4):
                    cse_var_99: T.int32 = i_2_1_s * 16 + 15
                    Y_local_1[cse_var_99] = Y_local_1[cse_var_99] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[15]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_100: T.int32 = i_2_1_s * 16 + 79
                        Y_local_1[cse_var_100] = Y_local_1[cse_var_100] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[15]
            for ax0_0, ax0_1_s in T.grid(2, 4):
                if ax0_0 * 2 + ax0_1_s // 2 < 3:
                    A_shared_dyn_local_1[ax0_0 * 4 + ax0_1_s] = A_shared_dyn_1[(k_0 + 1) % 5 * 576 + threadIdx_x // 27 * 72 + threadIdx_x % 3 * 24 + ax0_0 * 16 + ax0_1_s * 4]
            for ax1_0 in T.serial(4):
                cse_var_101: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_101:cse_var_101 + 4] = B_shared_dyn_1[(k_0 + 1) % 5 * 768 + (blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_101) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 - blockIdx_x % 8 * 144 // 64 * 64:(k_0 + 1) % 5 * 768 + (blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_101) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
            for i_2_1_s in T.serial(4):
                cse_var_102: T.int32 = i_2_1_s * 16
                Y_local_1[cse_var_102] = Y_local_1[cse_var_102] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[16]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_103: T.int32 = i_2_1_s * 16 + 64
                    Y_local_1[cse_var_103] = Y_local_1[cse_var_103] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[16]
            for i_2_1_s in T.serial(4):
                cse_var_104: T.int32 = i_2_1_s * 16 + 1
                Y_local_1[cse_var_104] = Y_local_1[cse_var_104] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[17]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_105: T.int32 = i_2_1_s * 16 + 65
                    Y_local_1[cse_var_105] = Y_local_1[cse_var_105] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[17]
            for i_2_1_s in T.serial(4):
                cse_var_106: T.int32 = i_2_1_s * 16 + 2
                Y_local_1[cse_var_106] = Y_local_1[cse_var_106] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[18]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_107: T.int32 = i_2_1_s * 16 + 66
                    Y_local_1[cse_var_107] = Y_local_1[cse_var_107] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[18]
            for i_2_1_s in T.serial(4):
                cse_var_108: T.int32 = i_2_1_s * 16 + 3
                Y_local_1[cse_var_108] = Y_local_1[cse_var_108] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[19]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_109: T.int32 = i_2_1_s * 16 + 67
                    Y_local_1[cse_var_109] = Y_local_1[cse_var_109] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[19]
            for i_2_1_s in T.serial(4):
                cse_var_110: T.int32 = i_2_1_s * 16 + 4
                Y_local_1[cse_var_110] = Y_local_1[cse_var_110] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[20]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_111: T.int32 = i_2_1_s * 16 + 68
                    Y_local_1[cse_var_111] = Y_local_1[cse_var_111] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[20]
            for i_2_1_s in T.serial(4):
                cse_var_112: T.int32 = i_2_1_s * 16 + 5
                Y_local_1[cse_var_112] = Y_local_1[cse_var_112] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[21]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_113: T.int32 = i_2_1_s * 16 + 69
                    Y_local_1[cse_var_113] = Y_local_1[cse_var_113] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[21]
            for i_2_1_s in T.serial(4):
                cse_var_114: T.int32 = i_2_1_s * 16 + 6
                Y_local_1[cse_var_114] = Y_local_1[cse_var_114] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[22]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_115: T.int32 = i_2_1_s * 16 + 70
                    Y_local_1[cse_var_115] = Y_local_1[cse_var_115] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[22]
            for i_2_1_s in T.serial(4):
                cse_var_116: T.int32 = i_2_1_s * 16 + 7
                Y_local_1[cse_var_116] = Y_local_1[cse_var_116] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[23]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_117: T.int32 = i_2_1_s * 16 + 71
                    Y_local_1[cse_var_117] = Y_local_1[cse_var_117] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[23]
            for i_2_1_s in T.serial(4):
                cse_var_118: T.int32 = i_2_1_s * 16 + 8
                Y_local_1[cse_var_118] = Y_local_1[cse_var_118] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[24]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_119: T.int32 = i_2_1_s * 16 + 72
                    Y_local_1[cse_var_119] = Y_local_1[cse_var_119] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[24]
            for i_2_1_s in T.serial(4):
                cse_var_120: T.int32 = i_2_1_s * 16 + 9
                Y_local_1[cse_var_120] = Y_local_1[cse_var_120] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[25]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_121: T.int32 = i_2_1_s * 16 + 73
                    Y_local_1[cse_var_121] = Y_local_1[cse_var_121] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[25]
            for i_2_1_s in T.serial(4):
                cse_var_122: T.int32 = i_2_1_s * 16 + 10
                Y_local_1[cse_var_122] = Y_local_1[cse_var_122] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[26]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_123: T.int32 = i_2_1_s * 16 + 74
                    Y_local_1[cse_var_123] = Y_local_1[cse_var_123] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[26]
            for i_2_1_s in T.serial(4):
                cse_var_124: T.int32 = i_2_1_s * 16 + 11
                Y_local_1[cse_var_124] = Y_local_1[cse_var_124] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[27]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_125: T.int32 = i_2_1_s * 16 + 75
                    Y_local_1[cse_var_125] = Y_local_1[cse_var_125] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[27]
            for i_2_1_s in T.serial(4):
                cse_var_126: T.int32 = i_2_1_s * 16 + 12
                Y_local_1[cse_var_126] = Y_local_1[cse_var_126] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[28]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_127: T.int32 = i_2_1_s * 16 + 76
                    Y_local_1[cse_var_127] = Y_local_1[cse_var_127] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[28]
            for i_2_1_s in T.serial(4):
                cse_var_128: T.int32 = i_2_1_s * 16 + 13
                Y_local_1[cse_var_128] = Y_local_1[cse_var_128] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[29]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_129: T.int32 = i_2_1_s * 16 + 77
                    Y_local_1[cse_var_129] = Y_local_1[cse_var_129] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[29]
            for i_2_1_s in T.serial(4):
                cse_var_130: T.int32 = i_2_1_s * 16 + 14
                Y_local_1[cse_var_130] = Y_local_1[cse_var_130] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[30]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_131: T.int32 = i_2_1_s * 16 + 78
                    Y_local_1[cse_var_131] = Y_local_1[cse_var_131] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[30]
            for i_2_1_s in T.serial(4):
                cse_var_132: T.int32 = i_2_1_s * 16 + 15
                Y_local_1[cse_var_132] = Y_local_1[cse_var_132] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[31]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_133: T.int32 = i_2_1_s * 16 + 79
                    Y_local_1[cse_var_133] = Y_local_1[cse_var_133] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[31]
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 2)
            for ax0_0, ax0_1_s in T.grid(2, 4):
                if ax0_0 * 2 + ax0_1_s // 2 < 3:
                    A_shared_dyn_local_1[ax0_0 * 4 + ax0_1_s + 6] = A_shared_dyn_1[threadIdx_x // 27 * 72 + threadIdx_x % 3 * 24 + ax0_0 * 16 + ax0_1_s * 4 + 2305]
            for ax1_0 in T.serial(4):
                cse_var_134: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_134 + 16:cse_var_134 + 16 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_134) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 3264 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_134) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 3264 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
            for i_2_1_s in T.serial(4):
                cse_var_135: T.int32 = i_2_1_s * 16
                Y_local_1[cse_var_135] = Y_local_1[cse_var_135] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_136: T.int32 = i_2_1_s * 16 + 64
                    Y_local_1[cse_var_136] = Y_local_1[cse_var_136] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                cse_var_137: T.int32 = i_2_1_s * 16 + 1
                Y_local_1[cse_var_137] = Y_local_1[cse_var_137] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_138: T.int32 = i_2_1_s * 16 + 65
                    Y_local_1[cse_var_138] = Y_local_1[cse_var_138] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                cse_var_139: T.int32 = i_2_1_s * 16 + 2
                Y_local_1[cse_var_139] = Y_local_1[cse_var_139] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_140: T.int32 = i_2_1_s * 16 + 66
                    Y_local_1[cse_var_140] = Y_local_1[cse_var_140] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                cse_var_141: T.int32 = i_2_1_s * 16 + 3
                Y_local_1[cse_var_141] = Y_local_1[cse_var_141] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_142: T.int32 = i_2_1_s * 16 + 67
                    Y_local_1[cse_var_142] = Y_local_1[cse_var_142] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                cse_var_143: T.int32 = i_2_1_s * 16 + 4
                Y_local_1[cse_var_143] = Y_local_1[cse_var_143] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_144: T.int32 = i_2_1_s * 16 + 68
                    Y_local_1[cse_var_144] = Y_local_1[cse_var_144] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                cse_var_145: T.int32 = i_2_1_s * 16 + 5
                Y_local_1[cse_var_145] = Y_local_1[cse_var_145] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_146: T.int32 = i_2_1_s * 16 + 69
                    Y_local_1[cse_var_146] = Y_local_1[cse_var_146] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                cse_var_147: T.int32 = i_2_1_s * 16 + 6
                Y_local_1[cse_var_147] = Y_local_1[cse_var_147] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_148: T.int32 = i_2_1_s * 16 + 70
                    Y_local_1[cse_var_148] = Y_local_1[cse_var_148] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                cse_var_149: T.int32 = i_2_1_s * 16 + 7
                Y_local_1[cse_var_149] = Y_local_1[cse_var_149] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_150: T.int32 = i_2_1_s * 16 + 71
                    Y_local_1[cse_var_150] = Y_local_1[cse_var_150] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[7]
            for i_2_1_s in T.serial(4):
                cse_var_151: T.int32 = i_2_1_s * 16 + 8
                Y_local_1[cse_var_151] = Y_local_1[cse_var_151] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_152: T.int32 = i_2_1_s * 16 + 72
                    Y_local_1[cse_var_152] = Y_local_1[cse_var_152] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                cse_var_153: T.int32 = i_2_1_s * 16 + 9
                Y_local_1[cse_var_153] = Y_local_1[cse_var_153] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_154: T.int32 = i_2_1_s * 16 + 73
                    Y_local_1[cse_var_154] = Y_local_1[cse_var_154] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                cse_var_155: T.int32 = i_2_1_s * 16 + 10
                Y_local_1[cse_var_155] = Y_local_1[cse_var_155] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_156: T.int32 = i_2_1_s * 16 + 74
                    Y_local_1[cse_var_156] = Y_local_1[cse_var_156] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                cse_var_157: T.int32 = i_2_1_s * 16 + 11
                Y_local_1[cse_var_157] = Y_local_1[cse_var_157] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[11]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_158: T.int32 = i_2_1_s * 16 + 75
                    Y_local_1[cse_var_158] = Y_local_1[cse_var_158] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[11]
            for i_2_1_s in T.serial(4):
                cse_var_159: T.int32 = i_2_1_s * 16 + 12
                Y_local_1[cse_var_159] = Y_local_1[cse_var_159] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_160: T.int32 = i_2_1_s * 16 + 76
                    Y_local_1[cse_var_160] = Y_local_1[cse_var_160] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                cse_var_161: T.int32 = i_2_1_s * 16 + 13
                Y_local_1[cse_var_161] = Y_local_1[cse_var_161] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_162: T.int32 = i_2_1_s * 16 + 77
                    Y_local_1[cse_var_162] = Y_local_1[cse_var_162] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                cse_var_163: T.int32 = i_2_1_s * 16 + 14
                Y_local_1[cse_var_163] = Y_local_1[cse_var_163] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_164: T.int32 = i_2_1_s * 16 + 78
                    Y_local_1[cse_var_164] = Y_local_1[cse_var_164] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                cse_var_165: T.int32 = i_2_1_s * 16 + 15
                Y_local_1[cse_var_165] = Y_local_1[cse_var_165] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[15]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_166: T.int32 = i_2_1_s * 16 + 79
                    Y_local_1[cse_var_166] = Y_local_1[cse_var_166] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[15]
            for ax0_0, ax0_1_s in T.grid(2, 4):
                if ax0_0 * 2 + ax0_1_s // 2 < 3:
                    A_shared_dyn_local_1[ax0_0 * 4 + ax0_1_s] = A_shared_dyn_1[threadIdx_x // 27 * 72 + threadIdx_x % 3 * 24 + ax0_0 * 16 + ax0_1_s * 4 + 2306]
            for ax1_0 in T.serial(4):
                cse_var_167: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_167:cse_var_167 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_167) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 3456 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_167) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 3456 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
            for i_2_1_s in T.serial(4):
                cse_var_168: T.int32 = i_2_1_s * 16
                Y_local_1[cse_var_168] = Y_local_1[cse_var_168] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[16]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_169: T.int32 = i_2_1_s * 16 + 64
                    Y_local_1[cse_var_169] = Y_local_1[cse_var_169] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[16]
            for i_2_1_s in T.serial(4):
                cse_var_170: T.int32 = i_2_1_s * 16 + 1
                Y_local_1[cse_var_170] = Y_local_1[cse_var_170] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[17]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_171: T.int32 = i_2_1_s * 16 + 65
                    Y_local_1[cse_var_171] = Y_local_1[cse_var_171] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[17]
            for i_2_1_s in T.serial(4):
                cse_var_172: T.int32 = i_2_1_s * 16 + 2
                Y_local_1[cse_var_172] = Y_local_1[cse_var_172] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[18]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_173: T.int32 = i_2_1_s * 16 + 66
                    Y_local_1[cse_var_173] = Y_local_1[cse_var_173] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[18]
            for i_2_1_s in T.serial(4):
                cse_var_174: T.int32 = i_2_1_s * 16 + 3
                Y_local_1[cse_var_174] = Y_local_1[cse_var_174] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[19]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_175: T.int32 = i_2_1_s * 16 + 67
                    Y_local_1[cse_var_175] = Y_local_1[cse_var_175] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[19]
            for i_2_1_s in T.serial(4):
                cse_var_176: T.int32 = i_2_1_s * 16 + 4
                Y_local_1[cse_var_176] = Y_local_1[cse_var_176] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[20]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_177: T.int32 = i_2_1_s * 16 + 68
                    Y_local_1[cse_var_177] = Y_local_1[cse_var_177] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[20]
            for i_2_1_s in T.serial(4):
                cse_var_178: T.int32 = i_2_1_s * 16 + 5
                Y_local_1[cse_var_178] = Y_local_1[cse_var_178] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[21]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_179: T.int32 = i_2_1_s * 16 + 69
                    Y_local_1[cse_var_179] = Y_local_1[cse_var_179] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[21]
            for i_2_1_s in T.serial(4):
                cse_var_180: T.int32 = i_2_1_s * 16 + 6
                Y_local_1[cse_var_180] = Y_local_1[cse_var_180] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[22]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_181: T.int32 = i_2_1_s * 16 + 70
                    Y_local_1[cse_var_181] = Y_local_1[cse_var_181] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[22]
            for i_2_1_s in T.serial(4):
                cse_var_182: T.int32 = i_2_1_s * 16 + 7
                Y_local_1[cse_var_182] = Y_local_1[cse_var_182] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[23]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_183: T.int32 = i_2_1_s * 16 + 71
                    Y_local_1[cse_var_183] = Y_local_1[cse_var_183] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[23]
            for i_2_1_s in T.serial(4):
                cse_var_184: T.int32 = i_2_1_s * 16 + 8
                Y_local_1[cse_var_184] = Y_local_1[cse_var_184] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[24]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_185: T.int32 = i_2_1_s * 16 + 72
                    Y_local_1[cse_var_185] = Y_local_1[cse_var_185] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[24]
            for i_2_1_s in T.serial(4):
                cse_var_186: T.int32 = i_2_1_s * 16 + 9
                Y_local_1[cse_var_186] = Y_local_1[cse_var_186] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[25]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_187: T.int32 = i_2_1_s * 16 + 73
                    Y_local_1[cse_var_187] = Y_local_1[cse_var_187] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[25]
            for i_2_1_s in T.serial(4):
                cse_var_188: T.int32 = i_2_1_s * 16 + 10
                Y_local_1[cse_var_188] = Y_local_1[cse_var_188] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[26]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_189: T.int32 = i_2_1_s * 16 + 74
                    Y_local_1[cse_var_189] = Y_local_1[cse_var_189] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[26]
            for i_2_1_s in T.serial(4):
                cse_var_190: T.int32 = i_2_1_s * 16 + 11
                Y_local_1[cse_var_190] = Y_local_1[cse_var_190] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[27]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_191: T.int32 = i_2_1_s * 16 + 75
                    Y_local_1[cse_var_191] = Y_local_1[cse_var_191] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[27]
            for i_2_1_s in T.serial(4):
                cse_var_192: T.int32 = i_2_1_s * 16 + 12
                Y_local_1[cse_var_192] = Y_local_1[cse_var_192] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[28]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_193: T.int32 = i_2_1_s * 16 + 76
                    Y_local_1[cse_var_193] = Y_local_1[cse_var_193] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[28]
            for i_2_1_s in T.serial(4):
                cse_var_194: T.int32 = i_2_1_s * 16 + 13
                Y_local_1[cse_var_194] = Y_local_1[cse_var_194] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[29]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_195: T.int32 = i_2_1_s * 16 + 77
                    Y_local_1[cse_var_195] = Y_local_1[cse_var_195] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[29]
            for i_2_1_s in T.serial(4):
                cse_var_196: T.int32 = i_2_1_s * 16 + 14
                Y_local_1[cse_var_196] = Y_local_1[cse_var_196] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[30]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_197: T.int32 = i_2_1_s * 16 + 78
                    Y_local_1[cse_var_197] = Y_local_1[cse_var_197] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[30]
            for i_2_1_s in T.serial(4):
                cse_var_198: T.int32 = i_2_1_s * 16 + 15
                Y_local_1[cse_var_198] = Y_local_1[cse_var_198] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[31]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_199: T.int32 = i_2_1_s * 16 + 79
                    Y_local_1[cse_var_199] = Y_local_1[cse_var_199] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[31]
            for ax0_0, ax0_1_s in T.grid(2, 4):
                if ax0_0 * 2 + ax0_1_s // 2 < 3:
                    A_shared_dyn_local_1[ax0_0 * 4 + ax0_1_s + 6] = A_shared_dyn_1[threadIdx_x // 27 * 72 + threadIdx_x % 3 * 24 + ax0_0 * 16 + ax0_1_s * 4 + 2307]
            for ax1_0 in T.serial(4):
                cse_var_200: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_200 + 16:cse_var_200 + 16 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_200) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 3648 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_200) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 3648 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
            for i_2_1_s in T.serial(4):
                cse_var_201: T.int32 = i_2_1_s * 16
                Y_local_1[cse_var_201] = Y_local_1[cse_var_201] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_202: T.int32 = i_2_1_s * 16 + 64
                    Y_local_1[cse_var_202] = Y_local_1[cse_var_202] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                cse_var_203: T.int32 = i_2_1_s * 16 + 1
                Y_local_1[cse_var_203] = Y_local_1[cse_var_203] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_204: T.int32 = i_2_1_s * 16 + 65
                    Y_local_1[cse_var_204] = Y_local_1[cse_var_204] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                cse_var_205: T.int32 = i_2_1_s * 16 + 2
                Y_local_1[cse_var_205] = Y_local_1[cse_var_205] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_206: T.int32 = i_2_1_s * 16 + 66
                    Y_local_1[cse_var_206] = Y_local_1[cse_var_206] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                cse_var_207: T.int32 = i_2_1_s * 16 + 3
                Y_local_1[cse_var_207] = Y_local_1[cse_var_207] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_208: T.int32 = i_2_1_s * 16 + 67
                    Y_local_1[cse_var_208] = Y_local_1[cse_var_208] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                cse_var_209: T.int32 = i_2_1_s * 16 + 4
                Y_local_1[cse_var_209] = Y_local_1[cse_var_209] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_210: T.int32 = i_2_1_s * 16 + 68
                    Y_local_1[cse_var_210] = Y_local_1[cse_var_210] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                cse_var_211: T.int32 = i_2_1_s * 16 + 5
                Y_local_1[cse_var_211] = Y_local_1[cse_var_211] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_212: T.int32 = i_2_1_s * 16 + 69
                    Y_local_1[cse_var_212] = Y_local_1[cse_var_212] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                cse_var_213: T.int32 = i_2_1_s * 16 + 6
                Y_local_1[cse_var_213] = Y_local_1[cse_var_213] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_214: T.int32 = i_2_1_s * 16 + 70
                    Y_local_1[cse_var_214] = Y_local_1[cse_var_214] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                cse_var_215: T.int32 = i_2_1_s * 16 + 7
                Y_local_1[cse_var_215] = Y_local_1[cse_var_215] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_216: T.int32 = i_2_1_s * 16 + 71
                    Y_local_1[cse_var_216] = Y_local_1[cse_var_216] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[7]
            for i_2_1_s in T.serial(4):
                cse_var_217: T.int32 = i_2_1_s * 16 + 8
                Y_local_1[cse_var_217] = Y_local_1[cse_var_217] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_218: T.int32 = i_2_1_s * 16 + 72
                    Y_local_1[cse_var_218] = Y_local_1[cse_var_218] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                cse_var_219: T.int32 = i_2_1_s * 16 + 9
                Y_local_1[cse_var_219] = Y_local_1[cse_var_219] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_220: T.int32 = i_2_1_s * 16 + 73
                    Y_local_1[cse_var_220] = Y_local_1[cse_var_220] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                cse_var_221: T.int32 = i_2_1_s * 16 + 10
                Y_local_1[cse_var_221] = Y_local_1[cse_var_221] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_222: T.int32 = i_2_1_s * 16 + 74
                    Y_local_1[cse_var_222] = Y_local_1[cse_var_222] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                cse_var_223: T.int32 = i_2_1_s * 16 + 11
                Y_local_1[cse_var_223] = Y_local_1[cse_var_223] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[11]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_224: T.int32 = i_2_1_s * 16 + 75
                    Y_local_1[cse_var_224] = Y_local_1[cse_var_224] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[11]
            for i_2_1_s in T.serial(4):
                cse_var_225: T.int32 = i_2_1_s * 16 + 12
                Y_local_1[cse_var_225] = Y_local_1[cse_var_225] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_226: T.int32 = i_2_1_s * 16 + 76
                    Y_local_1[cse_var_226] = Y_local_1[cse_var_226] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                cse_var_227: T.int32 = i_2_1_s * 16 + 13
                Y_local_1[cse_var_227] = Y_local_1[cse_var_227] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_228: T.int32 = i_2_1_s * 16 + 77
                    Y_local_1[cse_var_228] = Y_local_1[cse_var_228] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                cse_var_229: T.int32 = i_2_1_s * 16 + 14
                Y_local_1[cse_var_229] = Y_local_1[cse_var_229] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_230: T.int32 = i_2_1_s * 16 + 78
                    Y_local_1[cse_var_230] = Y_local_1[cse_var_230] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                cse_var_231: T.int32 = i_2_1_s * 16 + 15
                Y_local_1[cse_var_231] = Y_local_1[cse_var_231] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[15]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_232: T.int32 = i_2_1_s * 16 + 79
                    Y_local_1[cse_var_232] = Y_local_1[cse_var_232] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[15]
        for ax0_0, ax0_1_s in T.grid(2, 4):
            if ax0_0 * 2 + ax0_1_s // 2 < 3:
                A_shared_dyn_local_1[ax0_0 * 4 + ax0_1_s] = A_shared_dyn_1[threadIdx_x // 27 * 72 + threadIdx_x % 3 * 24 + ax0_0 * 16 + ax0_1_s * 4]
        for ax1_0 in T.serial(4):
            cse_var_233: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_233:cse_var_233 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_233) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_233) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
        for i_2_1_s in T.serial(4):
            cse_var_234: T.int32 = i_2_1_s * 16
            Y_local_1[cse_var_234] = Y_local_1[cse_var_234] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[16]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_235: T.int32 = i_2_1_s * 16 + 64
                Y_local_1[cse_var_235] = Y_local_1[cse_var_235] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[16]
        for i_2_1_s in T.serial(4):
            cse_var_236: T.int32 = i_2_1_s * 16 + 1
            Y_local_1[cse_var_236] = Y_local_1[cse_var_236] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[17]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_237: T.int32 = i_2_1_s * 16 + 65
                Y_local_1[cse_var_237] = Y_local_1[cse_var_237] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[17]
        for i_2_1_s in T.serial(4):
            cse_var_238: T.int32 = i_2_1_s * 16 + 2
            Y_local_1[cse_var_238] = Y_local_1[cse_var_238] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[18]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_239: T.int32 = i_2_1_s * 16 + 66
                Y_local_1[cse_var_239] = Y_local_1[cse_var_239] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[18]
        for i_2_1_s in T.serial(4):
            cse_var_240: T.int32 = i_2_1_s * 16 + 3
            Y_local_1[cse_var_240] = Y_local_1[cse_var_240] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[19]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_241: T.int32 = i_2_1_s * 16 + 67
                Y_local_1[cse_var_241] = Y_local_1[cse_var_241] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[19]
        for i_2_1_s in T.serial(4):
            cse_var_242: T.int32 = i_2_1_s * 16 + 4
            Y_local_1[cse_var_242] = Y_local_1[cse_var_242] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[20]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_243: T.int32 = i_2_1_s * 16 + 68
                Y_local_1[cse_var_243] = Y_local_1[cse_var_243] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[20]
        for i_2_1_s in T.serial(4):
            cse_var_244: T.int32 = i_2_1_s * 16 + 5
            Y_local_1[cse_var_244] = Y_local_1[cse_var_244] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[21]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_245: T.int32 = i_2_1_s * 16 + 69
                Y_local_1[cse_var_245] = Y_local_1[cse_var_245] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[21]
        for i_2_1_s in T.serial(4):
            cse_var_246: T.int32 = i_2_1_s * 16 + 6
            Y_local_1[cse_var_246] = Y_local_1[cse_var_246] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[22]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_247: T.int32 = i_2_1_s * 16 + 70
                Y_local_1[cse_var_247] = Y_local_1[cse_var_247] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[22]
        for i_2_1_s in T.serial(4):
            cse_var_248: T.int32 = i_2_1_s * 16 + 7
            Y_local_1[cse_var_248] = Y_local_1[cse_var_248] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[23]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_249: T.int32 = i_2_1_s * 16 + 71
                Y_local_1[cse_var_249] = Y_local_1[cse_var_249] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[23]
        for i_2_1_s in T.serial(4):
            cse_var_250: T.int32 = i_2_1_s * 16 + 8
            Y_local_1[cse_var_250] = Y_local_1[cse_var_250] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[24]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_251: T.int32 = i_2_1_s * 16 + 72
                Y_local_1[cse_var_251] = Y_local_1[cse_var_251] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[24]
        for i_2_1_s in T.serial(4):
            cse_var_252: T.int32 = i_2_1_s * 16 + 9
            Y_local_1[cse_var_252] = Y_local_1[cse_var_252] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[25]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_253: T.int32 = i_2_1_s * 16 + 73
                Y_local_1[cse_var_253] = Y_local_1[cse_var_253] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[25]
        for i_2_1_s in T.serial(4):
            cse_var_254: T.int32 = i_2_1_s * 16 + 10
            Y_local_1[cse_var_254] = Y_local_1[cse_var_254] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[26]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_255: T.int32 = i_2_1_s * 16 + 74
                Y_local_1[cse_var_255] = Y_local_1[cse_var_255] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[26]
        for i_2_1_s in T.serial(4):
            cse_var_256: T.int32 = i_2_1_s * 16 + 11
            Y_local_1[cse_var_256] = Y_local_1[cse_var_256] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[27]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_257: T.int32 = i_2_1_s * 16 + 75
                Y_local_1[cse_var_257] = Y_local_1[cse_var_257] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[27]
        for i_2_1_s in T.serial(4):
            cse_var_258: T.int32 = i_2_1_s * 16 + 12
            Y_local_1[cse_var_258] = Y_local_1[cse_var_258] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[28]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_259: T.int32 = i_2_1_s * 16 + 76
                Y_local_1[cse_var_259] = Y_local_1[cse_var_259] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[28]
        for i_2_1_s in T.serial(4):
            cse_var_260: T.int32 = i_2_1_s * 16 + 13
            Y_local_1[cse_var_260] = Y_local_1[cse_var_260] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[29]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_261: T.int32 = i_2_1_s * 16 + 77
                Y_local_1[cse_var_261] = Y_local_1[cse_var_261] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[29]
        for i_2_1_s in T.serial(4):
            cse_var_262: T.int32 = i_2_1_s * 16 + 14
            Y_local_1[cse_var_262] = Y_local_1[cse_var_262] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[30]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_263: T.int32 = i_2_1_s * 16 + 78
                Y_local_1[cse_var_263] = Y_local_1[cse_var_263] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[30]
        for i_2_1_s in T.serial(4):
            cse_var_264: T.int32 = i_2_1_s * 16 + 15
            Y_local_1[cse_var_264] = Y_local_1[cse_var_264] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[31]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_265: T.int32 = i_2_1_s * 16 + 79
                Y_local_1[cse_var_265] = Y_local_1[cse_var_265] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[31]
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 1)
            for ax0_0, ax0_1_s in T.grid(2, 4):
                if ax0_0 * 2 + ax0_1_s // 2 < 3:
                    A_shared_dyn_local_1[ax0_0 * 4 + ax0_1_s + 6] = A_shared_dyn_1[threadIdx_x // 27 * 72 + threadIdx_x % 3 * 24 + ax0_0 * 16 + ax0_1_s * 4 + 1]
            for ax1_0 in T.serial(4):
                cse_var_266: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_266 + 16:cse_var_266 + 16 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_266) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 192 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_266) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 192 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
            for i_2_1_s in T.serial(4):
                cse_var_267: T.int32 = i_2_1_s * 16
                Y_local_1[cse_var_267] = Y_local_1[cse_var_267] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_268: T.int32 = i_2_1_s * 16 + 64
                    Y_local_1[cse_var_268] = Y_local_1[cse_var_268] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                cse_var_269: T.int32 = i_2_1_s * 16 + 1
                Y_local_1[cse_var_269] = Y_local_1[cse_var_269] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_270: T.int32 = i_2_1_s * 16 + 65
                    Y_local_1[cse_var_270] = Y_local_1[cse_var_270] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                cse_var_271: T.int32 = i_2_1_s * 16 + 2
                Y_local_1[cse_var_271] = Y_local_1[cse_var_271] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_272: T.int32 = i_2_1_s * 16 + 66
                    Y_local_1[cse_var_272] = Y_local_1[cse_var_272] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                cse_var_273: T.int32 = i_2_1_s * 16 + 3
                Y_local_1[cse_var_273] = Y_local_1[cse_var_273] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_274: T.int32 = i_2_1_s * 16 + 67
                    Y_local_1[cse_var_274] = Y_local_1[cse_var_274] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                cse_var_275: T.int32 = i_2_1_s * 16 + 4
                Y_local_1[cse_var_275] = Y_local_1[cse_var_275] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_276: T.int32 = i_2_1_s * 16 + 68
                    Y_local_1[cse_var_276] = Y_local_1[cse_var_276] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                cse_var_277: T.int32 = i_2_1_s * 16 + 5
                Y_local_1[cse_var_277] = Y_local_1[cse_var_277] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_278: T.int32 = i_2_1_s * 16 + 69
                    Y_local_1[cse_var_278] = Y_local_1[cse_var_278] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                cse_var_279: T.int32 = i_2_1_s * 16 + 6
                Y_local_1[cse_var_279] = Y_local_1[cse_var_279] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_280: T.int32 = i_2_1_s * 16 + 70
                    Y_local_1[cse_var_280] = Y_local_1[cse_var_280] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                cse_var_281: T.int32 = i_2_1_s * 16 + 7
                Y_local_1[cse_var_281] = Y_local_1[cse_var_281] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_282: T.int32 = i_2_1_s * 16 + 71
                    Y_local_1[cse_var_282] = Y_local_1[cse_var_282] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[7]
            for i_2_1_s in T.serial(4):
                cse_var_283: T.int32 = i_2_1_s * 16 + 8
                Y_local_1[cse_var_283] = Y_local_1[cse_var_283] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_284: T.int32 = i_2_1_s * 16 + 72
                    Y_local_1[cse_var_284] = Y_local_1[cse_var_284] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                cse_var_285: T.int32 = i_2_1_s * 16 + 9
                Y_local_1[cse_var_285] = Y_local_1[cse_var_285] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_286: T.int32 = i_2_1_s * 16 + 73
                    Y_local_1[cse_var_286] = Y_local_1[cse_var_286] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                cse_var_287: T.int32 = i_2_1_s * 16 + 10
                Y_local_1[cse_var_287] = Y_local_1[cse_var_287] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_288: T.int32 = i_2_1_s * 16 + 74
                    Y_local_1[cse_var_288] = Y_local_1[cse_var_288] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                cse_var_289: T.int32 = i_2_1_s * 16 + 11
                Y_local_1[cse_var_289] = Y_local_1[cse_var_289] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[11]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_290: T.int32 = i_2_1_s * 16 + 75
                    Y_local_1[cse_var_290] = Y_local_1[cse_var_290] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[11]
            for i_2_1_s in T.serial(4):
                cse_var_291: T.int32 = i_2_1_s * 16 + 12
                Y_local_1[cse_var_291] = Y_local_1[cse_var_291] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_292: T.int32 = i_2_1_s * 16 + 76
                    Y_local_1[cse_var_292] = Y_local_1[cse_var_292] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                cse_var_293: T.int32 = i_2_1_s * 16 + 13
                Y_local_1[cse_var_293] = Y_local_1[cse_var_293] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_294: T.int32 = i_2_1_s * 16 + 77
                    Y_local_1[cse_var_294] = Y_local_1[cse_var_294] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                cse_var_295: T.int32 = i_2_1_s * 16 + 14
                Y_local_1[cse_var_295] = Y_local_1[cse_var_295] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_296: T.int32 = i_2_1_s * 16 + 78
                    Y_local_1[cse_var_296] = Y_local_1[cse_var_296] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                cse_var_297: T.int32 = i_2_1_s * 16 + 15
                Y_local_1[cse_var_297] = Y_local_1[cse_var_297] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[15]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_298: T.int32 = i_2_1_s * 16 + 79
                    Y_local_1[cse_var_298] = Y_local_1[cse_var_298] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[15]
            for ax0_0, ax0_1_s in T.grid(2, 4):
                if ax0_0 * 2 + ax0_1_s // 2 < 3:
                    A_shared_dyn_local_1[ax0_0 * 4 + ax0_1_s] = A_shared_dyn_1[threadIdx_x // 27 * 72 + threadIdx_x % 3 * 24 + ax0_0 * 16 + ax0_1_s * 4 + 2]
            for ax1_0 in T.serial(4):
                cse_var_299: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_299:cse_var_299 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_299) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 384 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_299) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 384 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
            for i_2_1_s in T.serial(4):
                cse_var_300: T.int32 = i_2_1_s * 16
                Y_local_1[cse_var_300] = Y_local_1[cse_var_300] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[16]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_301: T.int32 = i_2_1_s * 16 + 64
                    Y_local_1[cse_var_301] = Y_local_1[cse_var_301] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[16]
            for i_2_1_s in T.serial(4):
                cse_var_302: T.int32 = i_2_1_s * 16 + 1
                Y_local_1[cse_var_302] = Y_local_1[cse_var_302] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[17]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_303: T.int32 = i_2_1_s * 16 + 65
                    Y_local_1[cse_var_303] = Y_local_1[cse_var_303] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[17]
            for i_2_1_s in T.serial(4):
                cse_var_304: T.int32 = i_2_1_s * 16 + 2
                Y_local_1[cse_var_304] = Y_local_1[cse_var_304] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[18]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_305: T.int32 = i_2_1_s * 16 + 66
                    Y_local_1[cse_var_305] = Y_local_1[cse_var_305] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[18]
            for i_2_1_s in T.serial(4):
                cse_var_306: T.int32 = i_2_1_s * 16 + 3
                Y_local_1[cse_var_306] = Y_local_1[cse_var_306] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[19]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_307: T.int32 = i_2_1_s * 16 + 67
                    Y_local_1[cse_var_307] = Y_local_1[cse_var_307] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[19]
            for i_2_1_s in T.serial(4):
                cse_var_308: T.int32 = i_2_1_s * 16 + 4
                Y_local_1[cse_var_308] = Y_local_1[cse_var_308] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[20]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_309: T.int32 = i_2_1_s * 16 + 68
                    Y_local_1[cse_var_309] = Y_local_1[cse_var_309] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[20]
            for i_2_1_s in T.serial(4):
                cse_var_310: T.int32 = i_2_1_s * 16 + 5
                Y_local_1[cse_var_310] = Y_local_1[cse_var_310] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[21]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_311: T.int32 = i_2_1_s * 16 + 69
                    Y_local_1[cse_var_311] = Y_local_1[cse_var_311] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[21]
            for i_2_1_s in T.serial(4):
                cse_var_312: T.int32 = i_2_1_s * 16 + 6
                Y_local_1[cse_var_312] = Y_local_1[cse_var_312] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[22]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_313: T.int32 = i_2_1_s * 16 + 70
                    Y_local_1[cse_var_313] = Y_local_1[cse_var_313] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[22]
            for i_2_1_s in T.serial(4):
                cse_var_314: T.int32 = i_2_1_s * 16 + 7
                Y_local_1[cse_var_314] = Y_local_1[cse_var_314] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[23]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_315: T.int32 = i_2_1_s * 16 + 71
                    Y_local_1[cse_var_315] = Y_local_1[cse_var_315] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[23]
            for i_2_1_s in T.serial(4):
                cse_var_316: T.int32 = i_2_1_s * 16 + 8
                Y_local_1[cse_var_316] = Y_local_1[cse_var_316] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[24]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_317: T.int32 = i_2_1_s * 16 + 72
                    Y_local_1[cse_var_317] = Y_local_1[cse_var_317] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[24]
            for i_2_1_s in T.serial(4):
                cse_var_318: T.int32 = i_2_1_s * 16 + 9
                Y_local_1[cse_var_318] = Y_local_1[cse_var_318] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[25]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_319: T.int32 = i_2_1_s * 16 + 73
                    Y_local_1[cse_var_319] = Y_local_1[cse_var_319] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[25]
            for i_2_1_s in T.serial(4):
                cse_var_320: T.int32 = i_2_1_s * 16 + 10
                Y_local_1[cse_var_320] = Y_local_1[cse_var_320] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[26]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_321: T.int32 = i_2_1_s * 16 + 74
                    Y_local_1[cse_var_321] = Y_local_1[cse_var_321] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[26]
            for i_2_1_s in T.serial(4):
                cse_var_322: T.int32 = i_2_1_s * 16 + 11
                Y_local_1[cse_var_322] = Y_local_1[cse_var_322] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[27]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_323: T.int32 = i_2_1_s * 16 + 75
                    Y_local_1[cse_var_323] = Y_local_1[cse_var_323] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[27]
            for i_2_1_s in T.serial(4):
                cse_var_324: T.int32 = i_2_1_s * 16 + 12
                Y_local_1[cse_var_324] = Y_local_1[cse_var_324] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[28]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_325: T.int32 = i_2_1_s * 16 + 76
                    Y_local_1[cse_var_325] = Y_local_1[cse_var_325] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[28]
            for i_2_1_s in T.serial(4):
                cse_var_326: T.int32 = i_2_1_s * 16 + 13
                Y_local_1[cse_var_326] = Y_local_1[cse_var_326] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[29]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_327: T.int32 = i_2_1_s * 16 + 77
                    Y_local_1[cse_var_327] = Y_local_1[cse_var_327] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[29]
            for i_2_1_s in T.serial(4):
                cse_var_328: T.int32 = i_2_1_s * 16 + 14
                Y_local_1[cse_var_328] = Y_local_1[cse_var_328] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[30]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_329: T.int32 = i_2_1_s * 16 + 78
                    Y_local_1[cse_var_329] = Y_local_1[cse_var_329] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[30]
            for i_2_1_s in T.serial(4):
                cse_var_330: T.int32 = i_2_1_s * 16 + 15
                Y_local_1[cse_var_330] = Y_local_1[cse_var_330] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[31]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_331: T.int32 = i_2_1_s * 16 + 79
                    Y_local_1[cse_var_331] = Y_local_1[cse_var_331] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[31]
            for ax0_0, ax0_1_s in T.grid(2, 4):
                if ax0_0 * 2 + ax0_1_s // 2 < 3:
                    A_shared_dyn_local_1[ax0_0 * 4 + ax0_1_s + 6] = A_shared_dyn_1[threadIdx_x // 27 * 72 + threadIdx_x % 3 * 24 + ax0_0 * 16 + ax0_1_s * 4 + 3]
            for ax1_0 in T.serial(4):
                cse_var_332: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_332 + 16:cse_var_332 + 16 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_332) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 576 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_332) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 576 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
            for i_2_1_s in T.serial(4):
                cse_var_333: T.int32 = i_2_1_s * 16
                Y_local_1[cse_var_333] = Y_local_1[cse_var_333] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_334: T.int32 = i_2_1_s * 16 + 64
                    Y_local_1[cse_var_334] = Y_local_1[cse_var_334] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                cse_var_335: T.int32 = i_2_1_s * 16 + 1
                Y_local_1[cse_var_335] = Y_local_1[cse_var_335] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_336: T.int32 = i_2_1_s * 16 + 65
                    Y_local_1[cse_var_336] = Y_local_1[cse_var_336] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                cse_var_337: T.int32 = i_2_1_s * 16 + 2
                Y_local_1[cse_var_337] = Y_local_1[cse_var_337] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_338: T.int32 = i_2_1_s * 16 + 66
                    Y_local_1[cse_var_338] = Y_local_1[cse_var_338] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                cse_var_339: T.int32 = i_2_1_s * 16 + 3
                Y_local_1[cse_var_339] = Y_local_1[cse_var_339] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_340: T.int32 = i_2_1_s * 16 + 67
                    Y_local_1[cse_var_340] = Y_local_1[cse_var_340] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                cse_var_341: T.int32 = i_2_1_s * 16 + 4
                Y_local_1[cse_var_341] = Y_local_1[cse_var_341] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_342: T.int32 = i_2_1_s * 16 + 68
                    Y_local_1[cse_var_342] = Y_local_1[cse_var_342] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                cse_var_343: T.int32 = i_2_1_s * 16 + 5
                Y_local_1[cse_var_343] = Y_local_1[cse_var_343] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_344: T.int32 = i_2_1_s * 16 + 69
                    Y_local_1[cse_var_344] = Y_local_1[cse_var_344] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                cse_var_345: T.int32 = i_2_1_s * 16 + 6
                Y_local_1[cse_var_345] = Y_local_1[cse_var_345] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_346: T.int32 = i_2_1_s * 16 + 70
                    Y_local_1[cse_var_346] = Y_local_1[cse_var_346] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                cse_var_347: T.int32 = i_2_1_s * 16 + 7
                Y_local_1[cse_var_347] = Y_local_1[cse_var_347] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_348: T.int32 = i_2_1_s * 16 + 71
                    Y_local_1[cse_var_348] = Y_local_1[cse_var_348] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[7]
            for i_2_1_s in T.serial(4):
                cse_var_349: T.int32 = i_2_1_s * 16 + 8
                Y_local_1[cse_var_349] = Y_local_1[cse_var_349] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_350: T.int32 = i_2_1_s * 16 + 72
                    Y_local_1[cse_var_350] = Y_local_1[cse_var_350] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                cse_var_351: T.int32 = i_2_1_s * 16 + 9
                Y_local_1[cse_var_351] = Y_local_1[cse_var_351] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_352: T.int32 = i_2_1_s * 16 + 73
                    Y_local_1[cse_var_352] = Y_local_1[cse_var_352] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                cse_var_353: T.int32 = i_2_1_s * 16 + 10
                Y_local_1[cse_var_353] = Y_local_1[cse_var_353] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_354: T.int32 = i_2_1_s * 16 + 74
                    Y_local_1[cse_var_354] = Y_local_1[cse_var_354] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                cse_var_355: T.int32 = i_2_1_s * 16 + 11
                Y_local_1[cse_var_355] = Y_local_1[cse_var_355] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[11]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_356: T.int32 = i_2_1_s * 16 + 75
                    Y_local_1[cse_var_356] = Y_local_1[cse_var_356] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[11]
            for i_2_1_s in T.serial(4):
                cse_var_357: T.int32 = i_2_1_s * 16 + 12
                Y_local_1[cse_var_357] = Y_local_1[cse_var_357] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_358: T.int32 = i_2_1_s * 16 + 76
                    Y_local_1[cse_var_358] = Y_local_1[cse_var_358] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                cse_var_359: T.int32 = i_2_1_s * 16 + 13
                Y_local_1[cse_var_359] = Y_local_1[cse_var_359] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_360: T.int32 = i_2_1_s * 16 + 77
                    Y_local_1[cse_var_360] = Y_local_1[cse_var_360] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                cse_var_361: T.int32 = i_2_1_s * 16 + 14
                Y_local_1[cse_var_361] = Y_local_1[cse_var_361] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_362: T.int32 = i_2_1_s * 16 + 78
                    Y_local_1[cse_var_362] = Y_local_1[cse_var_362] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                cse_var_363: T.int32 = i_2_1_s * 16 + 15
                Y_local_1[cse_var_363] = Y_local_1[cse_var_363] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[15]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_364: T.int32 = i_2_1_s * 16 + 79
                    Y_local_1[cse_var_364] = Y_local_1[cse_var_364] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[15]
        for ax0_0, ax0_1_s in T.grid(2, 4):
            if ax0_0 * 2 + ax0_1_s // 2 < 3:
                A_shared_dyn_local_1[ax0_0 * 4 + ax0_1_s] = A_shared_dyn_1[threadIdx_x // 27 * 72 + threadIdx_x % 3 * 24 + ax0_0 * 16 + ax0_1_s * 4 + 576]
        for ax1_0 in T.serial(4):
            cse_var_365: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_365:cse_var_365 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_365) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 768 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_365) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 768 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
        for i_2_1_s in T.serial(4):
            cse_var_366: T.int32 = i_2_1_s * 16
            Y_local_1[cse_var_366] = Y_local_1[cse_var_366] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[16]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_367: T.int32 = i_2_1_s * 16 + 64
                Y_local_1[cse_var_367] = Y_local_1[cse_var_367] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[16]
        for i_2_1_s in T.serial(4):
            cse_var_368: T.int32 = i_2_1_s * 16 + 1
            Y_local_1[cse_var_368] = Y_local_1[cse_var_368] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[17]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_369: T.int32 = i_2_1_s * 16 + 65
                Y_local_1[cse_var_369] = Y_local_1[cse_var_369] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[17]
        for i_2_1_s in T.serial(4):
            cse_var_370: T.int32 = i_2_1_s * 16 + 2
            Y_local_1[cse_var_370] = Y_local_1[cse_var_370] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[18]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_371: T.int32 = i_2_1_s * 16 + 66
                Y_local_1[cse_var_371] = Y_local_1[cse_var_371] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[18]
        for i_2_1_s in T.serial(4):
            cse_var_372: T.int32 = i_2_1_s * 16 + 3
            Y_local_1[cse_var_372] = Y_local_1[cse_var_372] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[19]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_373: T.int32 = i_2_1_s * 16 + 67
                Y_local_1[cse_var_373] = Y_local_1[cse_var_373] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[19]
        for i_2_1_s in T.serial(4):
            cse_var_374: T.int32 = i_2_1_s * 16 + 4
            Y_local_1[cse_var_374] = Y_local_1[cse_var_374] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[20]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_375: T.int32 = i_2_1_s * 16 + 68
                Y_local_1[cse_var_375] = Y_local_1[cse_var_375] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[20]
        for i_2_1_s in T.serial(4):
            cse_var_376: T.int32 = i_2_1_s * 16 + 5
            Y_local_1[cse_var_376] = Y_local_1[cse_var_376] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[21]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_377: T.int32 = i_2_1_s * 16 + 69
                Y_local_1[cse_var_377] = Y_local_1[cse_var_377] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[21]
        for i_2_1_s in T.serial(4):
            cse_var_378: T.int32 = i_2_1_s * 16 + 6
            Y_local_1[cse_var_378] = Y_local_1[cse_var_378] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[22]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_379: T.int32 = i_2_1_s * 16 + 70
                Y_local_1[cse_var_379] = Y_local_1[cse_var_379] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[22]
        for i_2_1_s in T.serial(4):
            cse_var_380: T.int32 = i_2_1_s * 16 + 7
            Y_local_1[cse_var_380] = Y_local_1[cse_var_380] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[23]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_381: T.int32 = i_2_1_s * 16 + 71
                Y_local_1[cse_var_381] = Y_local_1[cse_var_381] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[23]
        for i_2_1_s in T.serial(4):
            cse_var_382: T.int32 = i_2_1_s * 16 + 8
            Y_local_1[cse_var_382] = Y_local_1[cse_var_382] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[24]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_383: T.int32 = i_2_1_s * 16 + 72
                Y_local_1[cse_var_383] = Y_local_1[cse_var_383] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[24]
        for i_2_1_s in T.serial(4):
            cse_var_384: T.int32 = i_2_1_s * 16 + 9
            Y_local_1[cse_var_384] = Y_local_1[cse_var_384] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[25]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_385: T.int32 = i_2_1_s * 16 + 73
                Y_local_1[cse_var_385] = Y_local_1[cse_var_385] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[25]
        for i_2_1_s in T.serial(4):
            cse_var_386: T.int32 = i_2_1_s * 16 + 10
            Y_local_1[cse_var_386] = Y_local_1[cse_var_386] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[26]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_387: T.int32 = i_2_1_s * 16 + 74
                Y_local_1[cse_var_387] = Y_local_1[cse_var_387] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[26]
        for i_2_1_s in T.serial(4):
            cse_var_388: T.int32 = i_2_1_s * 16 + 11
            Y_local_1[cse_var_388] = Y_local_1[cse_var_388] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[27]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_389: T.int32 = i_2_1_s * 16 + 75
                Y_local_1[cse_var_389] = Y_local_1[cse_var_389] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[27]
        for i_2_1_s in T.serial(4):
            cse_var_390: T.int32 = i_2_1_s * 16 + 12
            Y_local_1[cse_var_390] = Y_local_1[cse_var_390] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[28]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_391: T.int32 = i_2_1_s * 16 + 76
                Y_local_1[cse_var_391] = Y_local_1[cse_var_391] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[28]
        for i_2_1_s in T.serial(4):
            cse_var_392: T.int32 = i_2_1_s * 16 + 13
            Y_local_1[cse_var_392] = Y_local_1[cse_var_392] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[29]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_393: T.int32 = i_2_1_s * 16 + 77
                Y_local_1[cse_var_393] = Y_local_1[cse_var_393] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[29]
        for i_2_1_s in T.serial(4):
            cse_var_394: T.int32 = i_2_1_s * 16 + 14
            Y_local_1[cse_var_394] = Y_local_1[cse_var_394] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[30]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_395: T.int32 = i_2_1_s * 16 + 78
                Y_local_1[cse_var_395] = Y_local_1[cse_var_395] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[30]
        for i_2_1_s in T.serial(4):
            cse_var_396: T.int32 = i_2_1_s * 16 + 15
            Y_local_1[cse_var_396] = Y_local_1[cse_var_396] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[31]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_397: T.int32 = i_2_1_s * 16 + 79
                Y_local_1[cse_var_397] = Y_local_1[cse_var_397] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[31]
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 0)
            for ax0_0, ax0_1_s in T.grid(2, 4):
                if ax0_0 * 2 + ax0_1_s // 2 < 3:
                    A_shared_dyn_local_1[ax0_0 * 4 + ax0_1_s + 6] = A_shared_dyn_1[threadIdx_x // 27 * 72 + threadIdx_x % 3 * 24 + ax0_0 * 16 + ax0_1_s * 4 + 577]
            for ax1_0 in T.serial(4):
                cse_var_398: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_398 + 16:cse_var_398 + 16 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_398) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 960 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_398) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 960 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
            for i_2_1_s in T.serial(4):
                cse_var_399: T.int32 = i_2_1_s * 16
                Y_local_1[cse_var_399] = Y_local_1[cse_var_399] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_400: T.int32 = i_2_1_s * 16 + 64
                    Y_local_1[cse_var_400] = Y_local_1[cse_var_400] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                cse_var_401: T.int32 = i_2_1_s * 16 + 1
                Y_local_1[cse_var_401] = Y_local_1[cse_var_401] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_402: T.int32 = i_2_1_s * 16 + 65
                    Y_local_1[cse_var_402] = Y_local_1[cse_var_402] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                cse_var_403: T.int32 = i_2_1_s * 16 + 2
                Y_local_1[cse_var_403] = Y_local_1[cse_var_403] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_404: T.int32 = i_2_1_s * 16 + 66
                    Y_local_1[cse_var_404] = Y_local_1[cse_var_404] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                cse_var_405: T.int32 = i_2_1_s * 16 + 3
                Y_local_1[cse_var_405] = Y_local_1[cse_var_405] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_406: T.int32 = i_2_1_s * 16 + 67
                    Y_local_1[cse_var_406] = Y_local_1[cse_var_406] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                cse_var_407: T.int32 = i_2_1_s * 16 + 4
                Y_local_1[cse_var_407] = Y_local_1[cse_var_407] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_408: T.int32 = i_2_1_s * 16 + 68
                    Y_local_1[cse_var_408] = Y_local_1[cse_var_408] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                cse_var_409: T.int32 = i_2_1_s * 16 + 5
                Y_local_1[cse_var_409] = Y_local_1[cse_var_409] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_410: T.int32 = i_2_1_s * 16 + 69
                    Y_local_1[cse_var_410] = Y_local_1[cse_var_410] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                cse_var_411: T.int32 = i_2_1_s * 16 + 6
                Y_local_1[cse_var_411] = Y_local_1[cse_var_411] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_412: T.int32 = i_2_1_s * 16 + 70
                    Y_local_1[cse_var_412] = Y_local_1[cse_var_412] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                cse_var_413: T.int32 = i_2_1_s * 16 + 7
                Y_local_1[cse_var_413] = Y_local_1[cse_var_413] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_414: T.int32 = i_2_1_s * 16 + 71
                    Y_local_1[cse_var_414] = Y_local_1[cse_var_414] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[7]
            for i_2_1_s in T.serial(4):
                cse_var_415: T.int32 = i_2_1_s * 16 + 8
                Y_local_1[cse_var_415] = Y_local_1[cse_var_415] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_416: T.int32 = i_2_1_s * 16 + 72
                    Y_local_1[cse_var_416] = Y_local_1[cse_var_416] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                cse_var_417: T.int32 = i_2_1_s * 16 + 9
                Y_local_1[cse_var_417] = Y_local_1[cse_var_417] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_418: T.int32 = i_2_1_s * 16 + 73
                    Y_local_1[cse_var_418] = Y_local_1[cse_var_418] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                cse_var_419: T.int32 = i_2_1_s * 16 + 10
                Y_local_1[cse_var_419] = Y_local_1[cse_var_419] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_420: T.int32 = i_2_1_s * 16 + 74
                    Y_local_1[cse_var_420] = Y_local_1[cse_var_420] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                cse_var_421: T.int32 = i_2_1_s * 16 + 11
                Y_local_1[cse_var_421] = Y_local_1[cse_var_421] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[11]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_422: T.int32 = i_2_1_s * 16 + 75
                    Y_local_1[cse_var_422] = Y_local_1[cse_var_422] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[11]
            for i_2_1_s in T.serial(4):
                cse_var_423: T.int32 = i_2_1_s * 16 + 12
                Y_local_1[cse_var_423] = Y_local_1[cse_var_423] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_424: T.int32 = i_2_1_s * 16 + 76
                    Y_local_1[cse_var_424] = Y_local_1[cse_var_424] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                cse_var_425: T.int32 = i_2_1_s * 16 + 13
                Y_local_1[cse_var_425] = Y_local_1[cse_var_425] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_426: T.int32 = i_2_1_s * 16 + 77
                    Y_local_1[cse_var_426] = Y_local_1[cse_var_426] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                cse_var_427: T.int32 = i_2_1_s * 16 + 14
                Y_local_1[cse_var_427] = Y_local_1[cse_var_427] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_428: T.int32 = i_2_1_s * 16 + 78
                    Y_local_1[cse_var_428] = Y_local_1[cse_var_428] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                cse_var_429: T.int32 = i_2_1_s * 16 + 15
                Y_local_1[cse_var_429] = Y_local_1[cse_var_429] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[15]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_430: T.int32 = i_2_1_s * 16 + 79
                    Y_local_1[cse_var_430] = Y_local_1[cse_var_430] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[15]
            for ax0_0, ax0_1_s in T.grid(2, 4):
                if ax0_0 * 2 + ax0_1_s // 2 < 3:
                    A_shared_dyn_local_1[ax0_0 * 4 + ax0_1_s] = A_shared_dyn_1[threadIdx_x // 27 * 72 + threadIdx_x % 3 * 24 + ax0_0 * 16 + ax0_1_s * 4 + 578]
            for ax1_0 in T.serial(4):
                cse_var_431: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_431:cse_var_431 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_431) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 1152 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_431) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 1152 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
            for i_2_1_s in T.serial(4):
                cse_var_432: T.int32 = i_2_1_s * 16
                Y_local_1[cse_var_432] = Y_local_1[cse_var_432] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[16]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_433: T.int32 = i_2_1_s * 16 + 64
                    Y_local_1[cse_var_433] = Y_local_1[cse_var_433] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[16]
            for i_2_1_s in T.serial(4):
                cse_var_434: T.int32 = i_2_1_s * 16 + 1
                Y_local_1[cse_var_434] = Y_local_1[cse_var_434] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[17]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_435: T.int32 = i_2_1_s * 16 + 65
                    Y_local_1[cse_var_435] = Y_local_1[cse_var_435] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[17]
            for i_2_1_s in T.serial(4):
                cse_var_436: T.int32 = i_2_1_s * 16 + 2
                Y_local_1[cse_var_436] = Y_local_1[cse_var_436] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[18]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_437: T.int32 = i_2_1_s * 16 + 66
                    Y_local_1[cse_var_437] = Y_local_1[cse_var_437] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[18]
            for i_2_1_s in T.serial(4):
                cse_var_438: T.int32 = i_2_1_s * 16 + 3
                Y_local_1[cse_var_438] = Y_local_1[cse_var_438] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[19]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_439: T.int32 = i_2_1_s * 16 + 67
                    Y_local_1[cse_var_439] = Y_local_1[cse_var_439] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[19]
            for i_2_1_s in T.serial(4):
                cse_var_440: T.int32 = i_2_1_s * 16 + 4
                Y_local_1[cse_var_440] = Y_local_1[cse_var_440] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[20]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_441: T.int32 = i_2_1_s * 16 + 68
                    Y_local_1[cse_var_441] = Y_local_1[cse_var_441] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[20]
            for i_2_1_s in T.serial(4):
                cse_var_442: T.int32 = i_2_1_s * 16 + 5
                Y_local_1[cse_var_442] = Y_local_1[cse_var_442] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[21]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_443: T.int32 = i_2_1_s * 16 + 69
                    Y_local_1[cse_var_443] = Y_local_1[cse_var_443] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[21]
            for i_2_1_s in T.serial(4):
                cse_var_444: T.int32 = i_2_1_s * 16 + 6
                Y_local_1[cse_var_444] = Y_local_1[cse_var_444] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[22]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_445: T.int32 = i_2_1_s * 16 + 70
                    Y_local_1[cse_var_445] = Y_local_1[cse_var_445] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[22]
            for i_2_1_s in T.serial(4):
                cse_var_446: T.int32 = i_2_1_s * 16 + 7
                Y_local_1[cse_var_446] = Y_local_1[cse_var_446] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[23]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_447: T.int32 = i_2_1_s * 16 + 71
                    Y_local_1[cse_var_447] = Y_local_1[cse_var_447] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[23]
            for i_2_1_s in T.serial(4):
                cse_var_448: T.int32 = i_2_1_s * 16 + 8
                Y_local_1[cse_var_448] = Y_local_1[cse_var_448] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[24]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_449: T.int32 = i_2_1_s * 16 + 72
                    Y_local_1[cse_var_449] = Y_local_1[cse_var_449] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[24]
            for i_2_1_s in T.serial(4):
                cse_var_450: T.int32 = i_2_1_s * 16 + 9
                Y_local_1[cse_var_450] = Y_local_1[cse_var_450] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[25]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_451: T.int32 = i_2_1_s * 16 + 73
                    Y_local_1[cse_var_451] = Y_local_1[cse_var_451] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[25]
            for i_2_1_s in T.serial(4):
                cse_var_452: T.int32 = i_2_1_s * 16 + 10
                Y_local_1[cse_var_452] = Y_local_1[cse_var_452] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[26]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_453: T.int32 = i_2_1_s * 16 + 74
                    Y_local_1[cse_var_453] = Y_local_1[cse_var_453] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[26]
            for i_2_1_s in T.serial(4):
                cse_var_454: T.int32 = i_2_1_s * 16 + 11
                Y_local_1[cse_var_454] = Y_local_1[cse_var_454] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[27]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_455: T.int32 = i_2_1_s * 16 + 75
                    Y_local_1[cse_var_455] = Y_local_1[cse_var_455] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[27]
            for i_2_1_s in T.serial(4):
                cse_var_456: T.int32 = i_2_1_s * 16 + 12
                Y_local_1[cse_var_456] = Y_local_1[cse_var_456] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[28]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_457: T.int32 = i_2_1_s * 16 + 76
                    Y_local_1[cse_var_457] = Y_local_1[cse_var_457] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[28]
            for i_2_1_s in T.serial(4):
                cse_var_458: T.int32 = i_2_1_s * 16 + 13
                Y_local_1[cse_var_458] = Y_local_1[cse_var_458] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[29]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_459: T.int32 = i_2_1_s * 16 + 77
                    Y_local_1[cse_var_459] = Y_local_1[cse_var_459] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[29]
            for i_2_1_s in T.serial(4):
                cse_var_460: T.int32 = i_2_1_s * 16 + 14
                Y_local_1[cse_var_460] = Y_local_1[cse_var_460] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[30]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_461: T.int32 = i_2_1_s * 16 + 78
                    Y_local_1[cse_var_461] = Y_local_1[cse_var_461] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[30]
            for i_2_1_s in T.serial(4):
                cse_var_462: T.int32 = i_2_1_s * 16 + 15
                Y_local_1[cse_var_462] = Y_local_1[cse_var_462] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[31]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_463: T.int32 = i_2_1_s * 16 + 79
                    Y_local_1[cse_var_463] = Y_local_1[cse_var_463] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[31]
            for ax0_0, ax0_1_s in T.grid(2, 4):
                if ax0_0 * 2 + ax0_1_s // 2 < 3:
                    A_shared_dyn_local_1[ax0_0 * 4 + ax0_1_s + 6] = A_shared_dyn_1[threadIdx_x // 27 * 72 + threadIdx_x % 3 * 24 + ax0_0 * 16 + ax0_1_s * 4 + 579]
            for ax1_0 in T.serial(4):
                cse_var_464: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_464 + 16:cse_var_464 + 16 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_464) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 1344 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_464) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 1344 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
            for i_2_1_s in T.serial(4):
                cse_var_465: T.int32 = i_2_1_s * 16
                Y_local_1[cse_var_465] = Y_local_1[cse_var_465] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_466: T.int32 = i_2_1_s * 16 + 64
                    Y_local_1[cse_var_466] = Y_local_1[cse_var_466] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                cse_var_467: T.int32 = i_2_1_s * 16 + 1
                Y_local_1[cse_var_467] = Y_local_1[cse_var_467] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_468: T.int32 = i_2_1_s * 16 + 65
                    Y_local_1[cse_var_468] = Y_local_1[cse_var_468] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                cse_var_469: T.int32 = i_2_1_s * 16 + 2
                Y_local_1[cse_var_469] = Y_local_1[cse_var_469] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_470: T.int32 = i_2_1_s * 16 + 66
                    Y_local_1[cse_var_470] = Y_local_1[cse_var_470] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                cse_var_471: T.int32 = i_2_1_s * 16 + 3
                Y_local_1[cse_var_471] = Y_local_1[cse_var_471] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_472: T.int32 = i_2_1_s * 16 + 67
                    Y_local_1[cse_var_472] = Y_local_1[cse_var_472] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                cse_var_473: T.int32 = i_2_1_s * 16 + 4
                Y_local_1[cse_var_473] = Y_local_1[cse_var_473] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_474: T.int32 = i_2_1_s * 16 + 68
                    Y_local_1[cse_var_474] = Y_local_1[cse_var_474] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                cse_var_475: T.int32 = i_2_1_s * 16 + 5
                Y_local_1[cse_var_475] = Y_local_1[cse_var_475] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_476: T.int32 = i_2_1_s * 16 + 69
                    Y_local_1[cse_var_476] = Y_local_1[cse_var_476] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                cse_var_477: T.int32 = i_2_1_s * 16 + 6
                Y_local_1[cse_var_477] = Y_local_1[cse_var_477] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_478: T.int32 = i_2_1_s * 16 + 70
                    Y_local_1[cse_var_478] = Y_local_1[cse_var_478] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                cse_var_479: T.int32 = i_2_1_s * 16 + 7
                Y_local_1[cse_var_479] = Y_local_1[cse_var_479] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_480: T.int32 = i_2_1_s * 16 + 71
                    Y_local_1[cse_var_480] = Y_local_1[cse_var_480] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[7]
            for i_2_1_s in T.serial(4):
                cse_var_481: T.int32 = i_2_1_s * 16 + 8
                Y_local_1[cse_var_481] = Y_local_1[cse_var_481] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_482: T.int32 = i_2_1_s * 16 + 72
                    Y_local_1[cse_var_482] = Y_local_1[cse_var_482] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                cse_var_483: T.int32 = i_2_1_s * 16 + 9
                Y_local_1[cse_var_483] = Y_local_1[cse_var_483] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_484: T.int32 = i_2_1_s * 16 + 73
                    Y_local_1[cse_var_484] = Y_local_1[cse_var_484] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                cse_var_485: T.int32 = i_2_1_s * 16 + 10
                Y_local_1[cse_var_485] = Y_local_1[cse_var_485] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_486: T.int32 = i_2_1_s * 16 + 74
                    Y_local_1[cse_var_486] = Y_local_1[cse_var_486] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                cse_var_487: T.int32 = i_2_1_s * 16 + 11
                Y_local_1[cse_var_487] = Y_local_1[cse_var_487] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[11]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_488: T.int32 = i_2_1_s * 16 + 75
                    Y_local_1[cse_var_488] = Y_local_1[cse_var_488] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[11]
            for i_2_1_s in T.serial(4):
                cse_var_489: T.int32 = i_2_1_s * 16 + 12
                Y_local_1[cse_var_489] = Y_local_1[cse_var_489] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_490: T.int32 = i_2_1_s * 16 + 76
                    Y_local_1[cse_var_490] = Y_local_1[cse_var_490] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                cse_var_491: T.int32 = i_2_1_s * 16 + 13
                Y_local_1[cse_var_491] = Y_local_1[cse_var_491] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_492: T.int32 = i_2_1_s * 16 + 77
                    Y_local_1[cse_var_492] = Y_local_1[cse_var_492] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                cse_var_493: T.int32 = i_2_1_s * 16 + 14
                Y_local_1[cse_var_493] = Y_local_1[cse_var_493] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_494: T.int32 = i_2_1_s * 16 + 78
                    Y_local_1[cse_var_494] = Y_local_1[cse_var_494] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                cse_var_495: T.int32 = i_2_1_s * 16 + 15
                Y_local_1[cse_var_495] = Y_local_1[cse_var_495] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[15]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_496: T.int32 = i_2_1_s * 16 + 79
                    Y_local_1[cse_var_496] = Y_local_1[cse_var_496] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[15]
        for ax0_0, ax0_1_s in T.grid(2, 4):
            if ax0_0 * 2 + ax0_1_s // 2 < 3:
                A_shared_dyn_local_1[ax0_0 * 4 + ax0_1_s] = A_shared_dyn_1[threadIdx_x // 27 * 72 + threadIdx_x % 3 * 24 + ax0_0 * 16 + ax0_1_s * 4 + 1152]
        for ax1_0 in T.serial(4):
            cse_var_497: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_497:cse_var_497 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_497) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 1536 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_497) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 1536 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
        for i_2_1_s in T.serial(4):
            cse_var_498: T.int32 = i_2_1_s * 16
            Y_local_1[cse_var_498] = Y_local_1[cse_var_498] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[16]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_499: T.int32 = i_2_1_s * 16 + 64
                Y_local_1[cse_var_499] = Y_local_1[cse_var_499] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[16]
        for i_2_1_s in T.serial(4):
            cse_var_500: T.int32 = i_2_1_s * 16 + 1
            Y_local_1[cse_var_500] = Y_local_1[cse_var_500] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[17]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_501: T.int32 = i_2_1_s * 16 + 65
                Y_local_1[cse_var_501] = Y_local_1[cse_var_501] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[17]
        for i_2_1_s in T.serial(4):
            cse_var_502: T.int32 = i_2_1_s * 16 + 2
            Y_local_1[cse_var_502] = Y_local_1[cse_var_502] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[18]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_503: T.int32 = i_2_1_s * 16 + 66
                Y_local_1[cse_var_503] = Y_local_1[cse_var_503] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[18]
        for i_2_1_s in T.serial(4):
            cse_var_504: T.int32 = i_2_1_s * 16 + 3
            Y_local_1[cse_var_504] = Y_local_1[cse_var_504] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[19]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_505: T.int32 = i_2_1_s * 16 + 67
                Y_local_1[cse_var_505] = Y_local_1[cse_var_505] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[19]
        for i_2_1_s in T.serial(4):
            cse_var_506: T.int32 = i_2_1_s * 16 + 4
            Y_local_1[cse_var_506] = Y_local_1[cse_var_506] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[20]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_507: T.int32 = i_2_1_s * 16 + 68
                Y_local_1[cse_var_507] = Y_local_1[cse_var_507] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[20]
        for i_2_1_s in T.serial(4):
            cse_var_508: T.int32 = i_2_1_s * 16 + 5
            Y_local_1[cse_var_508] = Y_local_1[cse_var_508] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[21]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_509: T.int32 = i_2_1_s * 16 + 69
                Y_local_1[cse_var_509] = Y_local_1[cse_var_509] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[21]
        for i_2_1_s in T.serial(4):
            cse_var_510: T.int32 = i_2_1_s * 16 + 6
            Y_local_1[cse_var_510] = Y_local_1[cse_var_510] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[22]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_511: T.int32 = i_2_1_s * 16 + 70
                Y_local_1[cse_var_511] = Y_local_1[cse_var_511] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[22]
        for i_2_1_s in T.serial(4):
            cse_var_512: T.int32 = i_2_1_s * 16 + 7
            Y_local_1[cse_var_512] = Y_local_1[cse_var_512] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[23]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_513: T.int32 = i_2_1_s * 16 + 71
                Y_local_1[cse_var_513] = Y_local_1[cse_var_513] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[23]
        for i_2_1_s in T.serial(4):
            cse_var_514: T.int32 = i_2_1_s * 16 + 8
            Y_local_1[cse_var_514] = Y_local_1[cse_var_514] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[24]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_515: T.int32 = i_2_1_s * 16 + 72
                Y_local_1[cse_var_515] = Y_local_1[cse_var_515] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[24]
        for i_2_1_s in T.serial(4):
            cse_var_516: T.int32 = i_2_1_s * 16 + 9
            Y_local_1[cse_var_516] = Y_local_1[cse_var_516] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[25]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_517: T.int32 = i_2_1_s * 16 + 73
                Y_local_1[cse_var_517] = Y_local_1[cse_var_517] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[25]
        for i_2_1_s in T.serial(4):
            cse_var_518: T.int32 = i_2_1_s * 16 + 10
            Y_local_1[cse_var_518] = Y_local_1[cse_var_518] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[26]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_519: T.int32 = i_2_1_s * 16 + 74
                Y_local_1[cse_var_519] = Y_local_1[cse_var_519] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[26]
        for i_2_1_s in T.serial(4):
            cse_var_520: T.int32 = i_2_1_s * 16 + 11
            Y_local_1[cse_var_520] = Y_local_1[cse_var_520] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[27]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_521: T.int32 = i_2_1_s * 16 + 75
                Y_local_1[cse_var_521] = Y_local_1[cse_var_521] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[27]
        for i_2_1_s in T.serial(4):
            cse_var_522: T.int32 = i_2_1_s * 16 + 12
            Y_local_1[cse_var_522] = Y_local_1[cse_var_522] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[28]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_523: T.int32 = i_2_1_s * 16 + 76
                Y_local_1[cse_var_523] = Y_local_1[cse_var_523] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[28]
        for i_2_1_s in T.serial(4):
            cse_var_524: T.int32 = i_2_1_s * 16 + 13
            Y_local_1[cse_var_524] = Y_local_1[cse_var_524] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[29]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_525: T.int32 = i_2_1_s * 16 + 77
                Y_local_1[cse_var_525] = Y_local_1[cse_var_525] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[29]
        for i_2_1_s in T.serial(4):
            cse_var_526: T.int32 = i_2_1_s * 16 + 14
            Y_local_1[cse_var_526] = Y_local_1[cse_var_526] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[30]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_527: T.int32 = i_2_1_s * 16 + 78
                Y_local_1[cse_var_527] = Y_local_1[cse_var_527] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[30]
        for i_2_1_s in T.serial(4):
            cse_var_528: T.int32 = i_2_1_s * 16 + 15
            Y_local_1[cse_var_528] = Y_local_1[cse_var_528] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[31]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_529: T.int32 = i_2_1_s * 16 + 79
                Y_local_1[cse_var_529] = Y_local_1[cse_var_529] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[31]
        for ax0_0, ax0_1_s in T.grid(2, 4):
            if ax0_0 * 2 + ax0_1_s // 2 < 3:
                A_shared_dyn_local_1[ax0_0 * 4 + ax0_1_s + 6] = A_shared_dyn_1[threadIdx_x // 27 * 72 + threadIdx_x % 3 * 24 + ax0_0 * 16 + ax0_1_s * 4 + 1153]
        for ax1_0 in T.serial(4):
            cse_var_530: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_530 + 16:cse_var_530 + 16 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_530) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 1728 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_530) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 1728 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
        for i_2_1_s in T.serial(4):
            cse_var_531: T.int32 = i_2_1_s * 16
            Y_local_1[cse_var_531] = Y_local_1[cse_var_531] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_532: T.int32 = i_2_1_s * 16 + 64
                Y_local_1[cse_var_532] = Y_local_1[cse_var_532] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[0]
        for i_2_1_s in T.serial(4):
            cse_var_533: T.int32 = i_2_1_s * 16 + 1
            Y_local_1[cse_var_533] = Y_local_1[cse_var_533] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_534: T.int32 = i_2_1_s * 16 + 65
                Y_local_1[cse_var_534] = Y_local_1[cse_var_534] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[1]
        for i_2_1_s in T.serial(4):
            cse_var_535: T.int32 = i_2_1_s * 16 + 2
            Y_local_1[cse_var_535] = Y_local_1[cse_var_535] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_536: T.int32 = i_2_1_s * 16 + 66
                Y_local_1[cse_var_536] = Y_local_1[cse_var_536] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[2]
        for i_2_1_s in T.serial(4):
            cse_var_537: T.int32 = i_2_1_s * 16 + 3
            Y_local_1[cse_var_537] = Y_local_1[cse_var_537] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_538: T.int32 = i_2_1_s * 16 + 67
                Y_local_1[cse_var_538] = Y_local_1[cse_var_538] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[3]
        for i_2_1_s in T.serial(4):
            cse_var_539: T.int32 = i_2_1_s * 16 + 4
            Y_local_1[cse_var_539] = Y_local_1[cse_var_539] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_540: T.int32 = i_2_1_s * 16 + 68
                Y_local_1[cse_var_540] = Y_local_1[cse_var_540] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[4]
        for i_2_1_s in T.serial(4):
            cse_var_541: T.int32 = i_2_1_s * 16 + 5
            Y_local_1[cse_var_541] = Y_local_1[cse_var_541] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_542: T.int32 = i_2_1_s * 16 + 69
                Y_local_1[cse_var_542] = Y_local_1[cse_var_542] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[5]
        for i_2_1_s in T.serial(4):
            cse_var_543: T.int32 = i_2_1_s * 16 + 6
            Y_local_1[cse_var_543] = Y_local_1[cse_var_543] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_544: T.int32 = i_2_1_s * 16 + 70
                Y_local_1[cse_var_544] = Y_local_1[cse_var_544] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[6]
        for i_2_1_s in T.serial(4):
            cse_var_545: T.int32 = i_2_1_s * 16 + 7
            Y_local_1[cse_var_545] = Y_local_1[cse_var_545] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_546: T.int32 = i_2_1_s * 16 + 71
                Y_local_1[cse_var_546] = Y_local_1[cse_var_546] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[7]
        for i_2_1_s in T.serial(4):
            cse_var_547: T.int32 = i_2_1_s * 16 + 8
            Y_local_1[cse_var_547] = Y_local_1[cse_var_547] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[8]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_548: T.int32 = i_2_1_s * 16 + 72
                Y_local_1[cse_var_548] = Y_local_1[cse_var_548] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[8]
        for i_2_1_s in T.serial(4):
            cse_var_549: T.int32 = i_2_1_s * 16 + 9
            Y_local_1[cse_var_549] = Y_local_1[cse_var_549] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[9]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_550: T.int32 = i_2_1_s * 16 + 73
                Y_local_1[cse_var_550] = Y_local_1[cse_var_550] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[9]
        for i_2_1_s in T.serial(4):
            cse_var_551: T.int32 = i_2_1_s * 16 + 10
            Y_local_1[cse_var_551] = Y_local_1[cse_var_551] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[10]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_552: T.int32 = i_2_1_s * 16 + 74
                Y_local_1[cse_var_552] = Y_local_1[cse_var_552] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[10]
        for i_2_1_s in T.serial(4):
            cse_var_553: T.int32 = i_2_1_s * 16 + 11
            Y_local_1[cse_var_553] = Y_local_1[cse_var_553] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[11]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_554: T.int32 = i_2_1_s * 16 + 75
                Y_local_1[cse_var_554] = Y_local_1[cse_var_554] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[11]
        for i_2_1_s in T.serial(4):
            cse_var_555: T.int32 = i_2_1_s * 16 + 12
            Y_local_1[cse_var_555] = Y_local_1[cse_var_555] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[12]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_556: T.int32 = i_2_1_s * 16 + 76
                Y_local_1[cse_var_556] = Y_local_1[cse_var_556] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[12]
        for i_2_1_s in T.serial(4):
            cse_var_557: T.int32 = i_2_1_s * 16 + 13
            Y_local_1[cse_var_557] = Y_local_1[cse_var_557] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[13]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_558: T.int32 = i_2_1_s * 16 + 77
                Y_local_1[cse_var_558] = Y_local_1[cse_var_558] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[13]
        for i_2_1_s in T.serial(4):
            cse_var_559: T.int32 = i_2_1_s * 16 + 14
            Y_local_1[cse_var_559] = Y_local_1[cse_var_559] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[14]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_560: T.int32 = i_2_1_s * 16 + 78
                Y_local_1[cse_var_560] = Y_local_1[cse_var_560] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[14]
        for i_2_1_s in T.serial(4):
            cse_var_561: T.int32 = i_2_1_s * 16 + 15
            Y_local_1[cse_var_561] = Y_local_1[cse_var_561] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[15]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_562: T.int32 = i_2_1_s * 16 + 79
                Y_local_1[cse_var_562] = Y_local_1[cse_var_562] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[15]
        for ax0_0, ax0_1_s in T.grid(2, 4):
            if ax0_0 * 2 + ax0_1_s // 2 < 3:
                A_shared_dyn_local_1[ax0_0 * 4 + ax0_1_s] = A_shared_dyn_1[threadIdx_x // 27 * 72 + threadIdx_x % 3 * 24 + ax0_0 * 16 + ax0_1_s * 4 + 1154]
        for ax1_0 in T.serial(4):
            cse_var_563: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_563:cse_var_563 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_563) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 1920 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_563) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 1920 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
        for i_2_1_s in T.serial(4):
            cse_var_564: T.int32 = i_2_1_s * 16
            Y_local_1[cse_var_564] = Y_local_1[cse_var_564] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[16]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_565: T.int32 = i_2_1_s * 16 + 64
                Y_local_1[cse_var_565] = Y_local_1[cse_var_565] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[16]
        for i_2_1_s in T.serial(4):
            cse_var_566: T.int32 = i_2_1_s * 16 + 1
            Y_local_1[cse_var_566] = Y_local_1[cse_var_566] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[17]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_567: T.int32 = i_2_1_s * 16 + 65
                Y_local_1[cse_var_567] = Y_local_1[cse_var_567] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[17]
        for i_2_1_s in T.serial(4):
            cse_var_568: T.int32 = i_2_1_s * 16 + 2
            Y_local_1[cse_var_568] = Y_local_1[cse_var_568] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[18]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_569: T.int32 = i_2_1_s * 16 + 66
                Y_local_1[cse_var_569] = Y_local_1[cse_var_569] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[18]
        for i_2_1_s in T.serial(4):
            cse_var_570: T.int32 = i_2_1_s * 16 + 3
            Y_local_1[cse_var_570] = Y_local_1[cse_var_570] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[19]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_571: T.int32 = i_2_1_s * 16 + 67
                Y_local_1[cse_var_571] = Y_local_1[cse_var_571] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[19]
        for i_2_1_s in T.serial(4):
            cse_var_572: T.int32 = i_2_1_s * 16 + 4
            Y_local_1[cse_var_572] = Y_local_1[cse_var_572] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[20]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_573: T.int32 = i_2_1_s * 16 + 68
                Y_local_1[cse_var_573] = Y_local_1[cse_var_573] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[20]
        for i_2_1_s in T.serial(4):
            cse_var_574: T.int32 = i_2_1_s * 16 + 5
            Y_local_1[cse_var_574] = Y_local_1[cse_var_574] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[21]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_575: T.int32 = i_2_1_s * 16 + 69
                Y_local_1[cse_var_575] = Y_local_1[cse_var_575] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[21]
        for i_2_1_s in T.serial(4):
            cse_var_576: T.int32 = i_2_1_s * 16 + 6
            Y_local_1[cse_var_576] = Y_local_1[cse_var_576] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[22]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_577: T.int32 = i_2_1_s * 16 + 70
                Y_local_1[cse_var_577] = Y_local_1[cse_var_577] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[22]
        for i_2_1_s in T.serial(4):
            cse_var_578: T.int32 = i_2_1_s * 16 + 7
            Y_local_1[cse_var_578] = Y_local_1[cse_var_578] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[23]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_579: T.int32 = i_2_1_s * 16 + 71
                Y_local_1[cse_var_579] = Y_local_1[cse_var_579] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[23]
        for i_2_1_s in T.serial(4):
            cse_var_580: T.int32 = i_2_1_s * 16 + 8
            Y_local_1[cse_var_580] = Y_local_1[cse_var_580] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[24]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_581: T.int32 = i_2_1_s * 16 + 72
                Y_local_1[cse_var_581] = Y_local_1[cse_var_581] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[24]
        for i_2_1_s in T.serial(4):
            cse_var_582: T.int32 = i_2_1_s * 16 + 9
            Y_local_1[cse_var_582] = Y_local_1[cse_var_582] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[25]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_583: T.int32 = i_2_1_s * 16 + 73
                Y_local_1[cse_var_583] = Y_local_1[cse_var_583] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[25]
        for i_2_1_s in T.serial(4):
            cse_var_584: T.int32 = i_2_1_s * 16 + 10
            Y_local_1[cse_var_584] = Y_local_1[cse_var_584] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[26]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_585: T.int32 = i_2_1_s * 16 + 74
                Y_local_1[cse_var_585] = Y_local_1[cse_var_585] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[26]
        for i_2_1_s in T.serial(4):
            cse_var_586: T.int32 = i_2_1_s * 16 + 11
            Y_local_1[cse_var_586] = Y_local_1[cse_var_586] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[27]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_587: T.int32 = i_2_1_s * 16 + 75
                Y_local_1[cse_var_587] = Y_local_1[cse_var_587] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[27]
        for i_2_1_s in T.serial(4):
            cse_var_588: T.int32 = i_2_1_s * 16 + 12
            Y_local_1[cse_var_588] = Y_local_1[cse_var_588] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[28]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_589: T.int32 = i_2_1_s * 16 + 76
                Y_local_1[cse_var_589] = Y_local_1[cse_var_589] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[28]
        for i_2_1_s in T.serial(4):
            cse_var_590: T.int32 = i_2_1_s * 16 + 13
            Y_local_1[cse_var_590] = Y_local_1[cse_var_590] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[29]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_591: T.int32 = i_2_1_s * 16 + 77
                Y_local_1[cse_var_591] = Y_local_1[cse_var_591] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[29]
        for i_2_1_s in T.serial(4):
            cse_var_592: T.int32 = i_2_1_s * 16 + 14
            Y_local_1[cse_var_592] = Y_local_1[cse_var_592] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[30]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_593: T.int32 = i_2_1_s * 16 + 78
                Y_local_1[cse_var_593] = Y_local_1[cse_var_593] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[30]
        for i_2_1_s in T.serial(4):
            cse_var_594: T.int32 = i_2_1_s * 16 + 15
            Y_local_1[cse_var_594] = Y_local_1[cse_var_594] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[31]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_595: T.int32 = i_2_1_s * 16 + 79
                Y_local_1[cse_var_595] = Y_local_1[cse_var_595] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[31]
        for ax0_0, ax0_1_s in T.grid(2, 4):
            if ax0_0 * 2 + ax0_1_s // 2 < 3:
                A_shared_dyn_local_1[ax0_0 * 4 + ax0_1_s + 6] = A_shared_dyn_1[threadIdx_x // 27 * 72 + threadIdx_x % 3 * 24 + ax0_0 * 16 + ax0_1_s * 4 + 1155]
        for ax1_0 in T.serial(4):
            cse_var_596: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_596 + 16:cse_var_596 + 16 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_596) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 2112 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_596) // 64 * 64 + ax1_0 % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x % 27 // 3 * 2 + ax1_0 // 2) % 8 * 4 + 2112 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
        for i_2_1_s in T.serial(4):
            cse_var_597: T.int32 = i_2_1_s * 16
            Y_local_1[cse_var_597] = Y_local_1[cse_var_597] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_598: T.int32 = i_2_1_s * 16 + 64
                Y_local_1[cse_var_598] = Y_local_1[cse_var_598] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[0]
        for i_2_1_s in T.serial(4):
            cse_var_599: T.int32 = i_2_1_s * 16 + 1
            Y_local_1[cse_var_599] = Y_local_1[cse_var_599] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_600: T.int32 = i_2_1_s * 16 + 65
                Y_local_1[cse_var_600] = Y_local_1[cse_var_600] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[1]
        for i_2_1_s in T.serial(4):
            cse_var_601: T.int32 = i_2_1_s * 16 + 2
            Y_local_1[cse_var_601] = Y_local_1[cse_var_601] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_602: T.int32 = i_2_1_s * 16 + 66
                Y_local_1[cse_var_602] = Y_local_1[cse_var_602] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[2]
        for i_2_1_s in T.serial(4):
            cse_var_603: T.int32 = i_2_1_s * 16 + 3
            Y_local_1[cse_var_603] = Y_local_1[cse_var_603] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_604: T.int32 = i_2_1_s * 16 + 67
                Y_local_1[cse_var_604] = Y_local_1[cse_var_604] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[3]
        for i_2_1_s in T.serial(4):
            cse_var_605: T.int32 = i_2_1_s * 16 + 4
            Y_local_1[cse_var_605] = Y_local_1[cse_var_605] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_606: T.int32 = i_2_1_s * 16 + 68
                Y_local_1[cse_var_606] = Y_local_1[cse_var_606] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[4]
        for i_2_1_s in T.serial(4):
            cse_var_607: T.int32 = i_2_1_s * 16 + 5
            Y_local_1[cse_var_607] = Y_local_1[cse_var_607] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_608: T.int32 = i_2_1_s * 16 + 69
                Y_local_1[cse_var_608] = Y_local_1[cse_var_608] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[5]
        for i_2_1_s in T.serial(4):
            cse_var_609: T.int32 = i_2_1_s * 16 + 6
            Y_local_1[cse_var_609] = Y_local_1[cse_var_609] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_610: T.int32 = i_2_1_s * 16 + 70
                Y_local_1[cse_var_610] = Y_local_1[cse_var_610] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[6]
        for i_2_1_s in T.serial(4):
            cse_var_611: T.int32 = i_2_1_s * 16 + 7
            Y_local_1[cse_var_611] = Y_local_1[cse_var_611] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_612: T.int32 = i_2_1_s * 16 + 71
                Y_local_1[cse_var_612] = Y_local_1[cse_var_612] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[7]
        for i_2_1_s in T.serial(4):
            cse_var_613: T.int32 = i_2_1_s * 16 + 8
            Y_local_1[cse_var_613] = Y_local_1[cse_var_613] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[8]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_614: T.int32 = i_2_1_s * 16 + 72
                Y_local_1[cse_var_614] = Y_local_1[cse_var_614] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[8]
        for i_2_1_s in T.serial(4):
            cse_var_615: T.int32 = i_2_1_s * 16 + 9
            Y_local_1[cse_var_615] = Y_local_1[cse_var_615] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[9]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_616: T.int32 = i_2_1_s * 16 + 73
                Y_local_1[cse_var_616] = Y_local_1[cse_var_616] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[9]
        for i_2_1_s in T.serial(4):
            cse_var_617: T.int32 = i_2_1_s * 16 + 10
            Y_local_1[cse_var_617] = Y_local_1[cse_var_617] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[10]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_618: T.int32 = i_2_1_s * 16 + 74
                Y_local_1[cse_var_618] = Y_local_1[cse_var_618] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[10]
        for i_2_1_s in T.serial(4):
            cse_var_619: T.int32 = i_2_1_s * 16 + 11
            Y_local_1[cse_var_619] = Y_local_1[cse_var_619] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[11]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_620: T.int32 = i_2_1_s * 16 + 75
                Y_local_1[cse_var_620] = Y_local_1[cse_var_620] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[11]
        for i_2_1_s in T.serial(4):
            cse_var_621: T.int32 = i_2_1_s * 16 + 12
            Y_local_1[cse_var_621] = Y_local_1[cse_var_621] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[12]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_622: T.int32 = i_2_1_s * 16 + 76
                Y_local_1[cse_var_622] = Y_local_1[cse_var_622] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[12]
        for i_2_1_s in T.serial(4):
            cse_var_623: T.int32 = i_2_1_s * 16 + 13
            Y_local_1[cse_var_623] = Y_local_1[cse_var_623] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[13]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_624: T.int32 = i_2_1_s * 16 + 77
                Y_local_1[cse_var_624] = Y_local_1[cse_var_624] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[13]
        for i_2_1_s in T.serial(4):
            cse_var_625: T.int32 = i_2_1_s * 16 + 14
            Y_local_1[cse_var_625] = Y_local_1[cse_var_625] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[14]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_626: T.int32 = i_2_1_s * 16 + 78
                Y_local_1[cse_var_626] = Y_local_1[cse_var_626] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[14]
        for i_2_1_s in T.serial(4):
            cse_var_627: T.int32 = i_2_1_s * 16 + 15
            Y_local_1[cse_var_627] = Y_local_1[cse_var_627] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[15]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_628: T.int32 = i_2_1_s * 16 + 79
                Y_local_1[cse_var_628] = Y_local_1[cse_var_628] + A_shared_dyn_local_1[i_2_1_s + 4] * B_shared_dyn_local_1[15]
        for i_2_1_s in T.serial(4):
            cse_var_629: T.int32 = i_2_1_s * 16
            Y_local_1[cse_var_629] = Y_local_1[cse_var_629] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[16]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_630: T.int32 = i_2_1_s * 16 + 64
                Y_local_1[cse_var_630] = Y_local_1[cse_var_630] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[16]
        for i_2_1_s in T.serial(4):
            cse_var_631: T.int32 = i_2_1_s * 16 + 1
            Y_local_1[cse_var_631] = Y_local_1[cse_var_631] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[17]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_632: T.int32 = i_2_1_s * 16 + 65
                Y_local_1[cse_var_632] = Y_local_1[cse_var_632] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[17]
        for i_2_1_s in T.serial(4):
            cse_var_633: T.int32 = i_2_1_s * 16 + 2
            Y_local_1[cse_var_633] = Y_local_1[cse_var_633] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[18]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_634: T.int32 = i_2_1_s * 16 + 66
                Y_local_1[cse_var_634] = Y_local_1[cse_var_634] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[18]
        for i_2_1_s in T.serial(4):
            cse_var_635: T.int32 = i_2_1_s * 16 + 3
            Y_local_1[cse_var_635] = Y_local_1[cse_var_635] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[19]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_636: T.int32 = i_2_1_s * 16 + 67
                Y_local_1[cse_var_636] = Y_local_1[cse_var_636] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[19]
        for i_2_1_s in T.serial(4):
            cse_var_637: T.int32 = i_2_1_s * 16 + 4
            Y_local_1[cse_var_637] = Y_local_1[cse_var_637] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[20]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_638: T.int32 = i_2_1_s * 16 + 68
                Y_local_1[cse_var_638] = Y_local_1[cse_var_638] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[20]
        for i_2_1_s in T.serial(4):
            cse_var_639: T.int32 = i_2_1_s * 16 + 5
            Y_local_1[cse_var_639] = Y_local_1[cse_var_639] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[21]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_640: T.int32 = i_2_1_s * 16 + 69
                Y_local_1[cse_var_640] = Y_local_1[cse_var_640] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[21]
        for i_2_1_s in T.serial(4):
            cse_var_641: T.int32 = i_2_1_s * 16 + 6
            Y_local_1[cse_var_641] = Y_local_1[cse_var_641] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[22]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_642: T.int32 = i_2_1_s * 16 + 70
                Y_local_1[cse_var_642] = Y_local_1[cse_var_642] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[22]
        for i_2_1_s in T.serial(4):
            cse_var_643: T.int32 = i_2_1_s * 16 + 7
            Y_local_1[cse_var_643] = Y_local_1[cse_var_643] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[23]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_644: T.int32 = i_2_1_s * 16 + 71
                Y_local_1[cse_var_644] = Y_local_1[cse_var_644] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[23]
        for i_2_1_s in T.serial(4):
            cse_var_645: T.int32 = i_2_1_s * 16 + 8
            Y_local_1[cse_var_645] = Y_local_1[cse_var_645] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[24]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_646: T.int32 = i_2_1_s * 16 + 72
                Y_local_1[cse_var_646] = Y_local_1[cse_var_646] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[24]
        for i_2_1_s in T.serial(4):
            cse_var_647: T.int32 = i_2_1_s * 16 + 9
            Y_local_1[cse_var_647] = Y_local_1[cse_var_647] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[25]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_648: T.int32 = i_2_1_s * 16 + 73
                Y_local_1[cse_var_648] = Y_local_1[cse_var_648] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[25]
        for i_2_1_s in T.serial(4):
            cse_var_649: T.int32 = i_2_1_s * 16 + 10
            Y_local_1[cse_var_649] = Y_local_1[cse_var_649] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[26]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_650: T.int32 = i_2_1_s * 16 + 74
                Y_local_1[cse_var_650] = Y_local_1[cse_var_650] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[26]
        for i_2_1_s in T.serial(4):
            cse_var_651: T.int32 = i_2_1_s * 16 + 11
            Y_local_1[cse_var_651] = Y_local_1[cse_var_651] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[27]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_652: T.int32 = i_2_1_s * 16 + 75
                Y_local_1[cse_var_652] = Y_local_1[cse_var_652] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[27]
        for i_2_1_s in T.serial(4):
            cse_var_653: T.int32 = i_2_1_s * 16 + 12
            Y_local_1[cse_var_653] = Y_local_1[cse_var_653] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[28]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_654: T.int32 = i_2_1_s * 16 + 76
                Y_local_1[cse_var_654] = Y_local_1[cse_var_654] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[28]
        for i_2_1_s in T.serial(4):
            cse_var_655: T.int32 = i_2_1_s * 16 + 13
            Y_local_1[cse_var_655] = Y_local_1[cse_var_655] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[29]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_656: T.int32 = i_2_1_s * 16 + 77
                Y_local_1[cse_var_656] = Y_local_1[cse_var_656] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[29]
        for i_2_1_s in T.serial(4):
            cse_var_657: T.int32 = i_2_1_s * 16 + 14
            Y_local_1[cse_var_657] = Y_local_1[cse_var_657] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[30]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_658: T.int32 = i_2_1_s * 16 + 78
                Y_local_1[cse_var_658] = Y_local_1[cse_var_658] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[30]
        for i_2_1_s in T.serial(4):
            cse_var_659: T.int32 = i_2_1_s * 16 + 15
            Y_local_1[cse_var_659] = Y_local_1[cse_var_659] + A_shared_dyn_local_1[i_2_1_s + 6] * B_shared_dyn_local_1[31]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_660: T.int32 = i_2_1_s * 16 + 79
                Y_local_1[cse_var_660] = Y_local_1[cse_var_660] + A_shared_dyn_local_1[i_2_1_s + 10] * B_shared_dyn_local_1[31]
        for ax1_0 in T.serial(4):
            cse_var_661: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 8 * 165888 + threadIdx_x // 27 * 20736 + threadIdx_x % 3 * 6912 + blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_661:blockIdx_x // 8 * 165888 + threadIdx_x // 27 * 20736 + threadIdx_x % 3 * 6912 + blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_661 + 4] = Y_local_1[cse_var_661:cse_var_661 + 4]
        for ax1_0 in T.serial(4):
            cse_var_662: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 8 * 165888 + threadIdx_x // 27 * 20736 + threadIdx_x % 3 * 6912 + blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_662 + 1152:blockIdx_x // 8 * 165888 + threadIdx_x // 27 * 20736 + threadIdx_x % 3 * 6912 + blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_662 + 1152 + 4] = Y_local_1[cse_var_662 + 16:cse_var_662 + 16 + 4]
        for ax1_0 in T.serial(4):
            cse_var_663: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 8 * 165888 + threadIdx_x // 27 * 20736 + threadIdx_x % 3 * 6912 + blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_663 + 2304:blockIdx_x // 8 * 165888 + threadIdx_x // 27 * 20736 + threadIdx_x % 3 * 6912 + blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_663 + 2304 + 4] = Y_local_1[cse_var_663 + 32:cse_var_663 + 32 + 4]
        for ax1_0 in T.serial(4):
            cse_var_664: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 8 * 165888 + threadIdx_x // 27 * 20736 + threadIdx_x % 3 * 6912 + blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_664 + 3456:blockIdx_x // 8 * 165888 + threadIdx_x // 27 * 20736 + threadIdx_x % 3 * 6912 + blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_664 + 3456 + 4] = Y_local_1[cse_var_664 + 48:cse_var_664 + 48 + 4]
        for ax1_0 in T.serial(4):
            cse_var_665: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 8 * 165888 + threadIdx_x // 27 * 20736 + threadIdx_x % 3 * 6912 + blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_665 + 4608:blockIdx_x // 8 * 165888 + threadIdx_x // 27 * 20736 + threadIdx_x % 3 * 6912 + blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_665 + 4608 + 4] = Y_local_1[cse_var_665 + 64:cse_var_665 + 64 + 4]
        for ax1_0 in T.serial(4):
            cse_var_666: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 8 * 165888 + threadIdx_x // 27 * 20736 + threadIdx_x % 3 * 6912 + blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_666 + 5760:blockIdx_x // 8 * 165888 + threadIdx_x // 27 * 20736 + threadIdx_x % 3 * 6912 + blockIdx_x % 8 * 144 + threadIdx_x % 27 // 3 * 16 + cse_var_666 + 5760 + 4] = Y_local_1[cse_var_666 + 80:cse_var_666 + 80 + 4]
    

