# from tvm.script import tir as T
@tvm.script.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer[(1536, 1536), "float32"], B: T.Buffer[(1536, 1536), "float32"], Y: T.Buffer[(1536, 1536), "float32"]):
        # function attr dict
        T.func_attr({"global_symbol": "main", "tir.noalias": True})
        # var definition
        threadIdx_x = T.env_thread("threadIdx.x")
        blockIdx_x = T.env_thread("blockIdx.x")
        # buffer definition
        A_1 = T.buffer_decl([2359296], dtype="float32", data=A.data)
        B_1 = T.buffer_decl([2359296], dtype="float32", data=B.data)
        Y_1 = T.buffer_decl([2359296], dtype="float32", data=Y.data)
        # body
        T.launch_thread(blockIdx_x, 64)
        Y_local = T.allocate([96], "float32", "local")
        Y_local_1 = T.buffer_decl([96], dtype="float32", data=Y_local, scope="local")
        A_shared_dyn = T.allocate([1920], "float32", "shared.dyn")
        A_shared_dyn_1 = T.buffer_decl([1920], dtype="float32", data=A_shared_dyn, scope="shared.dyn")
        B_shared_dyn = T.allocate([7680], "float32", "shared.dyn")
        B_shared_dyn_1 = T.buffer_decl([7680], dtype="float32", data=B_shared_dyn, scope="shared.dyn")
        A_shared_dyn_local = T.allocate([4], "float32x4", "local")
        A_shared_dyn_local_1 = T.buffer_decl([4], dtype="float32x4", data=A_shared_dyn_local, scope="local")
        B_shared_dyn_local = T.allocate([24], "float32", "local")
        B_shared_dyn_local_1 = T.buffer_decl([24], dtype="float32", data=B_shared_dyn_local, scope="local")
        T.launch_thread(threadIdx_x, 384)
        Y_local_1[0] = T.float32(0)
        Y_local_1[12] = T.float32(0)
        Y_local_1[24] = T.float32(0)
        Y_local_1[36] = T.float32(0)
        Y_local_1[48] = T.float32(0)
        Y_local_1[60] = T.float32(0)
        Y_local_1[72] = T.float32(0)
        Y_local_1[84] = T.float32(0)
        Y_local_1[1] = T.float32(0)
        Y_local_1[13] = T.float32(0)
        Y_local_1[25] = T.float32(0)
        Y_local_1[37] = T.float32(0)
        Y_local_1[49] = T.float32(0)
        Y_local_1[61] = T.float32(0)
        Y_local_1[73] = T.float32(0)
        Y_local_1[85] = T.float32(0)
        Y_local_1[2] = T.float32(0)
        Y_local_1[14] = T.float32(0)
        Y_local_1[26] = T.float32(0)
        Y_local_1[38] = T.float32(0)
        Y_local_1[50] = T.float32(0)
        Y_local_1[62] = T.float32(0)
        Y_local_1[74] = T.float32(0)
        Y_local_1[86] = T.float32(0)
        Y_local_1[3] = T.float32(0)
        Y_local_1[15] = T.float32(0)
        Y_local_1[27] = T.float32(0)
        Y_local_1[39] = T.float32(0)
        Y_local_1[51] = T.float32(0)
        Y_local_1[63] = T.float32(0)
        Y_local_1[75] = T.float32(0)
        Y_local_1[87] = T.float32(0)
        Y_local_1[4] = T.float32(0)
        Y_local_1[16] = T.float32(0)
        Y_local_1[28] = T.float32(0)
        Y_local_1[40] = T.float32(0)
        Y_local_1[52] = T.float32(0)
        Y_local_1[64] = T.float32(0)
        Y_local_1[76] = T.float32(0)
        Y_local_1[88] = T.float32(0)
        Y_local_1[5] = T.float32(0)
        Y_local_1[17] = T.float32(0)
        Y_local_1[29] = T.float32(0)
        Y_local_1[41] = T.float32(0)
        Y_local_1[53] = T.float32(0)
        Y_local_1[65] = T.float32(0)
        Y_local_1[77] = T.float32(0)
        Y_local_1[89] = T.float32(0)
        Y_local_1[6] = T.float32(0)
        Y_local_1[18] = T.float32(0)
        Y_local_1[30] = T.float32(0)
        Y_local_1[42] = T.float32(0)
        Y_local_1[54] = T.float32(0)
        Y_local_1[66] = T.float32(0)
        Y_local_1[78] = T.float32(0)
        Y_local_1[90] = T.float32(0)
        Y_local_1[7] = T.float32(0)
        Y_local_1[19] = T.float32(0)
        Y_local_1[31] = T.float32(0)
        Y_local_1[43] = T.float32(0)
        Y_local_1[55] = T.float32(0)
        Y_local_1[67] = T.float32(0)
        Y_local_1[79] = T.float32(0)
        Y_local_1[91] = T.float32(0)
        Y_local_1[8] = T.float32(0)
        Y_local_1[20] = T.float32(0)
        Y_local_1[32] = T.float32(0)
        Y_local_1[44] = T.float32(0)
        Y_local_1[56] = T.float32(0)
        Y_local_1[68] = T.float32(0)
        Y_local_1[80] = T.float32(0)
        Y_local_1[92] = T.float32(0)
        Y_local_1[9] = T.float32(0)
        Y_local_1[21] = T.float32(0)
        Y_local_1[33] = T.float32(0)
        Y_local_1[45] = T.float32(0)
        Y_local_1[57] = T.float32(0)
        Y_local_1[69] = T.float32(0)
        Y_local_1[81] = T.float32(0)
        Y_local_1[93] = T.float32(0)
        Y_local_1[10] = T.float32(0)
        Y_local_1[22] = T.float32(0)
        Y_local_1[34] = T.float32(0)
        Y_local_1[46] = T.float32(0)
        Y_local_1[58] = T.float32(0)
        Y_local_1[70] = T.float32(0)
        Y_local_1[82] = T.float32(0)
        Y_local_1[94] = T.float32(0)
        Y_local_1[11] = T.float32(0)
        Y_local_1[23] = T.float32(0)
        Y_local_1[35] = T.float32(0)
        Y_local_1[47] = T.float32(0)
        Y_local_1[59] = T.float32(0)
        Y_local_1[71] = T.float32(0)
        Y_local_1[83] = T.float32(0)
        Y_local_1[95] = T.float32(0)
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x % 4 * 96 + threadIdx_x // 128 * 32 + threadIdx_x % 32 // 16 * 16 + threadIdx_x % 128 // 32 * 4 + threadIdx_x % 16 // 4] = A_1[blockIdx_x // 4 * 147456 + threadIdx_x // 4 * 1536 + threadIdx_x % 4]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 4] = B_1[threadIdx_x // 96 * 1536 + blockIdx_x % 4 * 384 + threadIdx_x % 96 * 4:threadIdx_x // 96 * 1536 + blockIdx_x % 4 * 384 + threadIdx_x % 96 * 4 + 4]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x % 4 * 96 + threadIdx_x // 128 * 32 + threadIdx_x % 32 // 16 * 16 + threadIdx_x % 128 // 32 * 4 + threadIdx_x % 16 // 4 + 384] = A_1[blockIdx_x // 4 * 147456 + threadIdx_x // 4 * 1536 + threadIdx_x % 4 + 4]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 1536:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 1536 + 4] = B_1[threadIdx_x // 96 * 1536 + blockIdx_x % 4 * 384 + threadIdx_x % 96 * 4 + 6144:threadIdx_x // 96 * 1536 + blockIdx_x % 4 * 384 + threadIdx_x % 96 * 4 + 6144 + 4]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x % 4 * 96 + threadIdx_x // 128 * 32 + threadIdx_x % 32 // 16 * 16 + threadIdx_x % 128 // 32 * 4 + threadIdx_x % 16 // 4 + 768] = A_1[blockIdx_x // 4 * 147456 + threadIdx_x // 4 * 1536 + threadIdx_x % 4 + 8]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 3072:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 3072 + 4] = B_1[threadIdx_x // 96 * 1536 + blockIdx_x % 4 * 384 + threadIdx_x % 96 * 4 + 12288:threadIdx_x // 96 * 1536 + blockIdx_x % 4 * 384 + threadIdx_x % 96 * 4 + 12288 + 4]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x % 4 * 96 + threadIdx_x // 128 * 32 + threadIdx_x % 32 // 16 * 16 + threadIdx_x % 128 // 32 * 4 + threadIdx_x % 16 // 4 + 1152] = A_1[blockIdx_x // 4 * 147456 + threadIdx_x // 4 * 1536 + threadIdx_x % 4 + 12]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 4608:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 4608 + 4] = B_1[threadIdx_x // 96 * 1536 + blockIdx_x % 4 * 384 + threadIdx_x % 96 * 4 + 18432:threadIdx_x // 96 * 1536 + blockIdx_x % 4 * 384 + threadIdx_x % 96 * 4 + 18432 + 4]
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 3)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4:threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 4]
            for ax1_0 in T.serial(3):
                cse_var_1: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_1:cse_var_1 + 4] = B_shared_dyn_1[(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_1) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_1) // 8) % 8 * 4:(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_1) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_1) // 8) % 8 * 4 + 4]
        for k_0 in T.serial(380):
            cse_var_2: T.int32 = (k_0 + 4) % 5
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    A_shared_dyn_1[cse_var_2 * 384 + threadIdx_x % 4 * 96 + threadIdx_x // 128 * 32 + threadIdx_x % 32 // 16 * 16 + threadIdx_x % 128 // 32 * 4 + threadIdx_x % 16 // 4] = A_1[blockIdx_x // 4 * 147456 + threadIdx_x // 4 * 1536 + k_0 * 4 + threadIdx_x % 4 + 16]
                T.attr(0, "async_scope", 1)
                B_shared_dyn_1[cse_var_2 * 1536 + threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4:cse_var_2 * 1536 + threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 4] = B_1[k_0 * 6144 + threadIdx_x // 96 * 1536 + blockIdx_x % 4 * 384 + threadIdx_x % 96 * 4 + 24576:k_0 * 6144 + threadIdx_x // 96 * 1536 + blockIdx_x % 4 * 384 + threadIdx_x % 96 * 4 + 24576 + 4]
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 3)
                for ax0_0 in T.serial(2):
                    A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[k_0 % 5 * 384 + threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 96:k_0 % 5 * 384 + threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 96 + 4]
                for ax1_0 in T.serial(3):
                    cse_var_3: T.int32 = ax1_0 * 4
                    B_shared_dyn_local_1[cse_var_3 + 12:cse_var_3 + 12 + 4] = B_shared_dyn_1[k_0 % 5 * 1536 + (threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_3) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_3) // 8) % 8 * 4 + 384:k_0 % 5 * 1536 + (threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_3) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_3) // 8) % 8 * 4 + 384 + 4]
                Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[48:96:12] = Y_local_1[48:96:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[49:97:12] = Y_local_1[49:97:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[50:98:12] = Y_local_1[50:98:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[51:99:12] = Y_local_1[51:99:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[52:100:12] = Y_local_1[52:100:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[53:101:12] = Y_local_1[53:101:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[54:102:12] = Y_local_1[54:102:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[55:103:12] = Y_local_1[55:103:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
                Y_local_1[56:104:12] = Y_local_1[56:104:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
                Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
                Y_local_1[57:105:12] = Y_local_1[57:105:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
                Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
                Y_local_1[58:106:12] = Y_local_1[58:106:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
                Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
                Y_local_1[59:107:12] = Y_local_1[59:107:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
                for ax0_0 in T.serial(2):
                    A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[k_0 % 5 * 384 + threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 192:k_0 % 5 * 384 + threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 192 + 4]
                for ax1_0 in T.serial(3):
                    cse_var_4: T.int32 = ax1_0 * 4
                    B_shared_dyn_local_1[cse_var_4:cse_var_4 + 4] = B_shared_dyn_1[k_0 % 5 * 1536 + (threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_4) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_4) // 8) % 8 * 4 + 768:k_0 % 5 * 1536 + (threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_4) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_4) // 8) % 8 * 4 + 768 + 4]
                Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[12], 4)
                Y_local_1[48:96:12] = Y_local_1[48:96:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
                Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[13], 4)
                Y_local_1[49:97:12] = Y_local_1[49:97:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
                Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[14], 4)
                Y_local_1[50:98:12] = Y_local_1[50:98:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
                Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[15], 4)
                Y_local_1[51:99:12] = Y_local_1[51:99:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
                Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[16], 4)
                Y_local_1[52:100:12] = Y_local_1[52:100:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[16], 4)
                Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[17], 4)
                Y_local_1[53:101:12] = Y_local_1[53:101:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[17], 4)
                Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[18], 4)
                Y_local_1[54:102:12] = Y_local_1[54:102:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[18], 4)
                Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[19], 4)
                Y_local_1[55:103:12] = Y_local_1[55:103:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[19], 4)
                Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[20], 4)
                Y_local_1[56:104:12] = Y_local_1[56:104:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[20], 4)
                Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[21], 4)
                Y_local_1[57:105:12] = Y_local_1[57:105:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[21], 4)
                Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[22], 4)
                Y_local_1[58:106:12] = Y_local_1[58:106:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[22], 4)
                Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[23], 4)
                Y_local_1[59:107:12] = Y_local_1[59:107:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[23], 4)
                for ax0_0 in T.serial(2):
                    A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[k_0 % 5 * 384 + threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 288:k_0 % 5 * 384 + threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 288 + 4]
                for ax1_0 in T.serial(3):
                    cse_var_5: T.int32 = ax1_0 * 4
                    B_shared_dyn_local_1[cse_var_5 + 12:cse_var_5 + 12 + 4] = B_shared_dyn_1[k_0 % 5 * 1536 + (threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_5) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_5) // 8) % 8 * 4 + 1152:k_0 % 5 * 1536 + (threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_5) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_5) // 8) % 8 * 4 + 1152 + 4]
                Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[48:96:12] = Y_local_1[48:96:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[49:97:12] = Y_local_1[49:97:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[50:98:12] = Y_local_1[50:98:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[51:99:12] = Y_local_1[51:99:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[52:100:12] = Y_local_1[52:100:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[53:101:12] = Y_local_1[53:101:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[54:102:12] = Y_local_1[54:102:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[55:103:12] = Y_local_1[55:103:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
                Y_local_1[56:104:12] = Y_local_1[56:104:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
                Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
                Y_local_1[57:105:12] = Y_local_1[57:105:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
                Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
                Y_local_1[58:106:12] = Y_local_1[58:106:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
                Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
                Y_local_1[59:107:12] = Y_local_1[59:107:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[(k_0 + 1) % 5 * 384 + threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4:(k_0 + 1) % 5 * 384 + threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 4]
            for ax1_0 in T.serial(3):
                cse_var_6: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_6:cse_var_6 + 4] = B_shared_dyn_1[(k_0 + 1) % 5 * 1536 + (threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_6) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_6) // 8) % 8 * 4:(k_0 + 1) % 5 * 1536 + (threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_6) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_6) // 8) % 8 * 4 + 4]
            Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[48:96:12] = Y_local_1[48:96:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[49:97:12] = Y_local_1[49:97:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[50:98:12] = Y_local_1[50:98:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[15], 4)
            Y_local_1[51:99:12] = Y_local_1[51:99:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
            Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[16], 4)
            Y_local_1[52:100:12] = Y_local_1[52:100:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[16], 4)
            Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[17], 4)
            Y_local_1[53:101:12] = Y_local_1[53:101:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[17], 4)
            Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[18], 4)
            Y_local_1[54:102:12] = Y_local_1[54:102:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[18], 4)
            Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[19], 4)
            Y_local_1[55:103:12] = Y_local_1[55:103:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[19], 4)
            Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[20], 4)
            Y_local_1[56:104:12] = Y_local_1[56:104:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[20], 4)
            Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[21], 4)
            Y_local_1[57:105:12] = Y_local_1[57:105:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[21], 4)
            Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[22], 4)
            Y_local_1[58:106:12] = Y_local_1[58:106:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[22], 4)
            Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[23], 4)
            Y_local_1[59:107:12] = Y_local_1[59:107:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[23], 4)
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 2)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 96:threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 96 + 4]
            for ax1_0 in T.serial(3):
                cse_var_7: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_7 + 12:cse_var_7 + 12 + 4] = B_shared_dyn_1[(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_7) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_7) // 8) % 8 * 4 + 384:(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_7) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_7) // 8) % 8 * 4 + 384 + 4]
            Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[48:96:12] = Y_local_1[48:96:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[49:97:12] = Y_local_1[49:97:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[50:98:12] = Y_local_1[50:98:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[51:99:12] = Y_local_1[51:99:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[52:100:12] = Y_local_1[52:100:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[53:101:12] = Y_local_1[53:101:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[54:102:12] = Y_local_1[54:102:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[55:103:12] = Y_local_1[55:103:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[56:104:12] = Y_local_1[56:104:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[57:105:12] = Y_local_1[57:105:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[58:106:12] = Y_local_1[58:106:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[59:107:12] = Y_local_1[59:107:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 192:threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 192 + 4]
            for ax1_0 in T.serial(3):
                cse_var_8: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_8:cse_var_8 + 4] = B_shared_dyn_1[(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_8) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_8) // 8) % 8 * 4 + 768:(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_8) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_8) // 8) % 8 * 4 + 768 + 4]
            Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[48:96:12] = Y_local_1[48:96:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[49:97:12] = Y_local_1[49:97:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[50:98:12] = Y_local_1[50:98:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[15], 4)
            Y_local_1[51:99:12] = Y_local_1[51:99:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
            Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[16], 4)
            Y_local_1[52:100:12] = Y_local_1[52:100:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[16], 4)
            Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[17], 4)
            Y_local_1[53:101:12] = Y_local_1[53:101:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[17], 4)
            Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[18], 4)
            Y_local_1[54:102:12] = Y_local_1[54:102:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[18], 4)
            Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[19], 4)
            Y_local_1[55:103:12] = Y_local_1[55:103:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[19], 4)
            Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[20], 4)
            Y_local_1[56:104:12] = Y_local_1[56:104:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[20], 4)
            Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[21], 4)
            Y_local_1[57:105:12] = Y_local_1[57:105:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[21], 4)
            Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[22], 4)
            Y_local_1[58:106:12] = Y_local_1[58:106:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[22], 4)
            Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[23], 4)
            Y_local_1[59:107:12] = Y_local_1[59:107:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[23], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 288:threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 288 + 4]
            for ax1_0 in T.serial(3):
                cse_var_9: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_9 + 12:cse_var_9 + 12 + 4] = B_shared_dyn_1[(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_9) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_9) // 8) % 8 * 4 + 1152:(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_9) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_9) // 8) % 8 * 4 + 1152 + 4]
            Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[48:96:12] = Y_local_1[48:96:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[49:97:12] = Y_local_1[49:97:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[50:98:12] = Y_local_1[50:98:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[51:99:12] = Y_local_1[51:99:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[52:100:12] = Y_local_1[52:100:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[53:101:12] = Y_local_1[53:101:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[54:102:12] = Y_local_1[54:102:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[55:103:12] = Y_local_1[55:103:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[56:104:12] = Y_local_1[56:104:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[57:105:12] = Y_local_1[57:105:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[58:106:12] = Y_local_1[58:106:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[59:107:12] = Y_local_1[59:107:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
        for ax0_0 in T.serial(2):
            A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 384:threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 384 + 4]
        for ax1_0 in T.serial(3):
            cse_var_10: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_10:cse_var_10 + 4] = B_shared_dyn_1[(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_10) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_10) // 8) % 8 * 4 + 1536:(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_10) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_10) // 8) % 8 * 4 + 1536 + 4]
        Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[48:96:12] = Y_local_1[48:96:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[49:97:12] = Y_local_1[49:97:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[50:98:12] = Y_local_1[50:98:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[51:99:12] = Y_local_1[51:99:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[16], 4)
        Y_local_1[52:100:12] = Y_local_1[52:100:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[16], 4)
        Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[17], 4)
        Y_local_1[53:101:12] = Y_local_1[53:101:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[17], 4)
        Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[18], 4)
        Y_local_1[54:102:12] = Y_local_1[54:102:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[18], 4)
        Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[19], 4)
        Y_local_1[55:103:12] = Y_local_1[55:103:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[19], 4)
        Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[20], 4)
        Y_local_1[56:104:12] = Y_local_1[56:104:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[20], 4)
        Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[21], 4)
        Y_local_1[57:105:12] = Y_local_1[57:105:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[21], 4)
        Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[22], 4)
        Y_local_1[58:106:12] = Y_local_1[58:106:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[22], 4)
        Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[23], 4)
        Y_local_1[59:107:12] = Y_local_1[59:107:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[23], 4)
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 1)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 480:threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 480 + 4]
            for ax1_0 in T.serial(3):
                cse_var_11: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_11 + 12:cse_var_11 + 12 + 4] = B_shared_dyn_1[(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_11) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_11) // 8) % 8 * 4 + 1920:(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_11) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_11) // 8) % 8 * 4 + 1920 + 4]
            Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[48:96:12] = Y_local_1[48:96:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[49:97:12] = Y_local_1[49:97:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[50:98:12] = Y_local_1[50:98:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[51:99:12] = Y_local_1[51:99:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[52:100:12] = Y_local_1[52:100:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[53:101:12] = Y_local_1[53:101:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[54:102:12] = Y_local_1[54:102:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[55:103:12] = Y_local_1[55:103:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[56:104:12] = Y_local_1[56:104:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[57:105:12] = Y_local_1[57:105:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[58:106:12] = Y_local_1[58:106:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[59:107:12] = Y_local_1[59:107:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 576:threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 576 + 4]
            for ax1_0 in T.serial(3):
                cse_var_12: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_12:cse_var_12 + 4] = B_shared_dyn_1[(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_12) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_12) // 8) % 8 * 4 + 2304:(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_12) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_12) // 8) % 8 * 4 + 2304 + 4]
            Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[48:96:12] = Y_local_1[48:96:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[49:97:12] = Y_local_1[49:97:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[50:98:12] = Y_local_1[50:98:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[15], 4)
            Y_local_1[51:99:12] = Y_local_1[51:99:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
            Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[16], 4)
            Y_local_1[52:100:12] = Y_local_1[52:100:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[16], 4)
            Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[17], 4)
            Y_local_1[53:101:12] = Y_local_1[53:101:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[17], 4)
            Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[18], 4)
            Y_local_1[54:102:12] = Y_local_1[54:102:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[18], 4)
            Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[19], 4)
            Y_local_1[55:103:12] = Y_local_1[55:103:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[19], 4)
            Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[20], 4)
            Y_local_1[56:104:12] = Y_local_1[56:104:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[20], 4)
            Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[21], 4)
            Y_local_1[57:105:12] = Y_local_1[57:105:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[21], 4)
            Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[22], 4)
            Y_local_1[58:106:12] = Y_local_1[58:106:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[22], 4)
            Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[23], 4)
            Y_local_1[59:107:12] = Y_local_1[59:107:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[23], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 672:threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 672 + 4]
            for ax1_0 in T.serial(3):
                cse_var_13: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_13 + 12:cse_var_13 + 12 + 4] = B_shared_dyn_1[(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_13) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_13) // 8) % 8 * 4 + 2688:(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_13) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_13) // 8) % 8 * 4 + 2688 + 4]
            Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[48:96:12] = Y_local_1[48:96:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[49:97:12] = Y_local_1[49:97:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[50:98:12] = Y_local_1[50:98:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[51:99:12] = Y_local_1[51:99:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[52:100:12] = Y_local_1[52:100:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[53:101:12] = Y_local_1[53:101:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[54:102:12] = Y_local_1[54:102:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[55:103:12] = Y_local_1[55:103:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[56:104:12] = Y_local_1[56:104:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[57:105:12] = Y_local_1[57:105:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[58:106:12] = Y_local_1[58:106:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[59:107:12] = Y_local_1[59:107:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
        for ax0_0 in T.serial(2):
            A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 768:threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 768 + 4]
        for ax1_0 in T.serial(3):
            cse_var_14: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_14:cse_var_14 + 4] = B_shared_dyn_1[(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_14) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_14) // 8) % 8 * 4 + 3072:(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_14) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_14) // 8) % 8 * 4 + 3072 + 4]
        Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[48:96:12] = Y_local_1[48:96:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[49:97:12] = Y_local_1[49:97:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[50:98:12] = Y_local_1[50:98:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[51:99:12] = Y_local_1[51:99:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[16], 4)
        Y_local_1[52:100:12] = Y_local_1[52:100:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[16], 4)
        Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[17], 4)
        Y_local_1[53:101:12] = Y_local_1[53:101:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[17], 4)
        Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[18], 4)
        Y_local_1[54:102:12] = Y_local_1[54:102:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[18], 4)
        Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[19], 4)
        Y_local_1[55:103:12] = Y_local_1[55:103:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[19], 4)
        Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[20], 4)
        Y_local_1[56:104:12] = Y_local_1[56:104:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[20], 4)
        Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[21], 4)
        Y_local_1[57:105:12] = Y_local_1[57:105:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[21], 4)
        Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[22], 4)
        Y_local_1[58:106:12] = Y_local_1[58:106:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[22], 4)
        Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[23], 4)
        Y_local_1[59:107:12] = Y_local_1[59:107:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[23], 4)
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 0)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 864:threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 864 + 4]
            for ax1_0 in T.serial(3):
                cse_var_15: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_15 + 12:cse_var_15 + 12 + 4] = B_shared_dyn_1[(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_15) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_15) // 8) % 8 * 4 + 3456:(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_15) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_15) // 8) % 8 * 4 + 3456 + 4]
            Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[48:96:12] = Y_local_1[48:96:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[49:97:12] = Y_local_1[49:97:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[50:98:12] = Y_local_1[50:98:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[51:99:12] = Y_local_1[51:99:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[52:100:12] = Y_local_1[52:100:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[53:101:12] = Y_local_1[53:101:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[54:102:12] = Y_local_1[54:102:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[55:103:12] = Y_local_1[55:103:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[56:104:12] = Y_local_1[56:104:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[57:105:12] = Y_local_1[57:105:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[58:106:12] = Y_local_1[58:106:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[59:107:12] = Y_local_1[59:107:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 960:threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 960 + 4]
            for ax1_0 in T.serial(3):
                cse_var_16: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_16:cse_var_16 + 4] = B_shared_dyn_1[(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_16) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_16) // 8) % 8 * 4 + 3840:(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_16) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_16) // 8) % 8 * 4 + 3840 + 4]
            Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[48:96:12] = Y_local_1[48:96:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[49:97:12] = Y_local_1[49:97:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[50:98:12] = Y_local_1[50:98:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[15], 4)
            Y_local_1[51:99:12] = Y_local_1[51:99:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
            Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[16], 4)
            Y_local_1[52:100:12] = Y_local_1[52:100:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[16], 4)
            Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[17], 4)
            Y_local_1[53:101:12] = Y_local_1[53:101:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[17], 4)
            Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[18], 4)
            Y_local_1[54:102:12] = Y_local_1[54:102:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[18], 4)
            Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[19], 4)
            Y_local_1[55:103:12] = Y_local_1[55:103:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[19], 4)
            Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[20], 4)
            Y_local_1[56:104:12] = Y_local_1[56:104:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[20], 4)
            Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[21], 4)
            Y_local_1[57:105:12] = Y_local_1[57:105:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[21], 4)
            Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[22], 4)
            Y_local_1[58:106:12] = Y_local_1[58:106:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[22], 4)
            Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[23], 4)
            Y_local_1[59:107:12] = Y_local_1[59:107:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[23], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 1056:threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 1056 + 4]
            for ax1_0 in T.serial(3):
                cse_var_17: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_17 + 12:cse_var_17 + 12 + 4] = B_shared_dyn_1[(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_17) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_17) // 8) % 8 * 4 + 4224:(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_17) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_17) // 8) % 8 * 4 + 4224 + 4]
            Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[48:96:12] = Y_local_1[48:96:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[49:97:12] = Y_local_1[49:97:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[50:98:12] = Y_local_1[50:98:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[51:99:12] = Y_local_1[51:99:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[52:100:12] = Y_local_1[52:100:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[53:101:12] = Y_local_1[53:101:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[54:102:12] = Y_local_1[54:102:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[55:103:12] = Y_local_1[55:103:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[56:104:12] = Y_local_1[56:104:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[57:105:12] = Y_local_1[57:105:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[58:106:12] = Y_local_1[58:106:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[59:107:12] = Y_local_1[59:107:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
        for ax0_0 in T.serial(2):
            A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 1152:threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 1152 + 4]
        for ax1_0 in T.serial(3):
            cse_var_18: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_18:cse_var_18 + 4] = B_shared_dyn_1[(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_18) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_18) // 8) % 8 * 4 + 4608:(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_18) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_18) // 8) % 8 * 4 + 4608 + 4]
        Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[48:96:12] = Y_local_1[48:96:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[49:97:12] = Y_local_1[49:97:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[50:98:12] = Y_local_1[50:98:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[51:99:12] = Y_local_1[51:99:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[16], 4)
        Y_local_1[52:100:12] = Y_local_1[52:100:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[16], 4)
        Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[17], 4)
        Y_local_1[53:101:12] = Y_local_1[53:101:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[17], 4)
        Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[18], 4)
        Y_local_1[54:102:12] = Y_local_1[54:102:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[18], 4)
        Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[19], 4)
        Y_local_1[55:103:12] = Y_local_1[55:103:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[19], 4)
        Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[20], 4)
        Y_local_1[56:104:12] = Y_local_1[56:104:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[20], 4)
        Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[21], 4)
        Y_local_1[57:105:12] = Y_local_1[57:105:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[21], 4)
        Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[22], 4)
        Y_local_1[58:106:12] = Y_local_1[58:106:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[22], 4)
        Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[23], 4)
        Y_local_1[59:107:12] = Y_local_1[59:107:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[23], 4)
        for ax0_0 in T.serial(2):
            A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 1248:threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 1248 + 4]
        for ax1_0 in T.serial(3):
            cse_var_19: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_19 + 12:cse_var_19 + 12 + 4] = B_shared_dyn_1[(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_19) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_19) // 8) % 8 * 4 + 4992:(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_19) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_19) // 8) % 8 * 4 + 4992 + 4]
        Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[48:96:12] = Y_local_1[48:96:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[49:97:12] = Y_local_1[49:97:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[50:98:12] = Y_local_1[50:98:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[51:99:12] = Y_local_1[51:99:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[52:100:12] = Y_local_1[52:100:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[53:101:12] = Y_local_1[53:101:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[54:102:12] = Y_local_1[54:102:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[55:103:12] = Y_local_1[55:103:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[56:104:12] = Y_local_1[56:104:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[57:105:12] = Y_local_1[57:105:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[58:106:12] = Y_local_1[58:106:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[59:107:12] = Y_local_1[59:107:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
        for ax0_0 in T.serial(2):
            A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 1344:threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 1344 + 4]
        for ax1_0 in T.serial(3):
            cse_var_20: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_20:cse_var_20 + 4] = B_shared_dyn_1[(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_20) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_20) // 8) % 8 * 4 + 5376:(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_20) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_20) // 8) % 8 * 4 + 5376 + 4]
        Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[48:96:12] = Y_local_1[48:96:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[49:97:12] = Y_local_1[49:97:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[50:98:12] = Y_local_1[50:98:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[51:99:12] = Y_local_1[51:99:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[16], 4)
        Y_local_1[52:100:12] = Y_local_1[52:100:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[16], 4)
        Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[17], 4)
        Y_local_1[53:101:12] = Y_local_1[53:101:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[17], 4)
        Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[18], 4)
        Y_local_1[54:102:12] = Y_local_1[54:102:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[18], 4)
        Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[19], 4)
        Y_local_1[55:103:12] = Y_local_1[55:103:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[19], 4)
        Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[20], 4)
        Y_local_1[56:104:12] = Y_local_1[56:104:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[20], 4)
        Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[21], 4)
        Y_local_1[57:105:12] = Y_local_1[57:105:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[21], 4)
        Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[22], 4)
        Y_local_1[58:106:12] = Y_local_1[58:106:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[22], 4)
        Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[23], 4)
        Y_local_1[59:107:12] = Y_local_1[59:107:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[23], 4)
        for ax0_0 in T.serial(2):
            A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 1440:threadIdx_x % 96 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 1440 + 4]
        for ax1_0 in T.serial(3):
            cse_var_21: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_21 + 12:cse_var_21 + 12 + 4] = B_shared_dyn_1[(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_21) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_21) // 8) % 8 * 4 + 5760:(threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + cse_var_21) // 64 * 64 + (threadIdx_x % 16 // 2 + ax1_0) % 2 * 32 + (threadIdx_x // 96 * 4 + (threadIdx_x % 16 // 2 * 12 + cse_var_21) // 8) % 8 * 4 + 5760 + 4]
        Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[48:96:12] = Y_local_1[48:96:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[49:97:12] = Y_local_1[49:97:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[50:98:12] = Y_local_1[50:98:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[51:99:12] = Y_local_1[51:99:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[52:100:12] = Y_local_1[52:100:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[53:101:12] = Y_local_1[53:101:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[54:102:12] = Y_local_1[54:102:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[55:103:12] = Y_local_1[55:103:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[56:104:12] = Y_local_1[56:104:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[57:105:12] = Y_local_1[57:105:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[58:106:12] = Y_local_1[58:106:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[59:107:12] = Y_local_1[59:107:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[48:96:12] = Y_local_1[48:96:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[49:97:12] = Y_local_1[49:97:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[50:98:12] = Y_local_1[50:98:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[51:99:12] = Y_local_1[51:99:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[16], 4)
        Y_local_1[52:100:12] = Y_local_1[52:100:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[16], 4)
        Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[17], 4)
        Y_local_1[53:101:12] = Y_local_1[53:101:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[17], 4)
        Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[18], 4)
        Y_local_1[54:102:12] = Y_local_1[54:102:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[18], 4)
        Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[19], 4)
        Y_local_1[55:103:12] = Y_local_1[55:103:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[19], 4)
        Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[20], 4)
        Y_local_1[56:104:12] = Y_local_1[56:104:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[20], 4)
        Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[21], 4)
        Y_local_1[57:105:12] = Y_local_1[57:105:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[21], 4)
        Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[22], 4)
        Y_local_1[58:106:12] = Y_local_1[58:106:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[22], 4)
        Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[23], 4)
        Y_local_1[59:107:12] = Y_local_1[59:107:12] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[23], 4)
        Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12:blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 4] = Y_local_1[0:4]
        Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 4:blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 4 + 4] = Y_local_1[4:8]
        Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 8:blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 8 + 4] = Y_local_1[8:12]
        Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 1536:blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 1536 + 4] = Y_local_1[12:16]
        Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 1540:blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 1540 + 4] = Y_local_1[16:20]
        Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 1544:blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 1544 + 4] = Y_local_1[20:24]
        Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 3072:blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 3072 + 4] = Y_local_1[24:28]
        Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 3076:blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 3076 + 4] = Y_local_1[28:32]
        Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 3080:blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 3080 + 4] = Y_local_1[32:36]
        Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 4608:blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 4608 + 4] = Y_local_1[36:40]
        Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 4612:blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 4612 + 4] = Y_local_1[40:44]
        Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 4616:blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 4616 + 4] = Y_local_1[44:48]
        Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 6144:blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 6144 + 4] = Y_local_1[48:52]
        Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 6148:blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 6148 + 4] = Y_local_1[52:56]
        Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 6152:blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 6152 + 4] = Y_local_1[56:60]
        Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 7680:blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 7680 + 4] = Y_local_1[60:64]
        Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 7684:blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 7684 + 4] = Y_local_1[64:68]
        Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 7688:blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 7688 + 4] = Y_local_1[68:72]
        Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 9216:blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 9216 + 4] = Y_local_1[72:76]
        Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 9220:blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 9220 + 4] = Y_local_1[76:80]
        Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 9224:blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 9224 + 4] = Y_local_1[80:84]
        Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 10752:blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 10752 + 4] = Y_local_1[84:88]
        Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 10756:blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 10756 + 4] = Y_local_1[88:92]
        Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 10760:blockIdx_x // 4 * 147456 + threadIdx_x % 96 // 16 * 24576 + threadIdx_x % 2 * 12288 + blockIdx_x % 4 * 384 + threadIdx_x // 96 * 96 + threadIdx_x % 16 // 2 * 12 + 10760 + 4] = Y_local_1[92:96]
    

