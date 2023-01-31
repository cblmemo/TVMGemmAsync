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
        A_shared_dyn_local = T.allocate([6], "float32x4", "local")
        A_shared_dyn_local_1 = T.buffer_decl([6], dtype="float32x4", data=A_shared_dyn_local, scope="local")
        B_shared_dyn_local = T.allocate([16], "float32", "local")
        B_shared_dyn_local_1 = T.buffer_decl([16], dtype="float32", data=B_shared_dyn_local, scope="local")
        T.launch_thread(threadIdx_x, 384)
        Y_local_1[0] = T.float32(0)
        Y_local_1[8] = T.float32(0)
        Y_local_1[16] = T.float32(0)
        Y_local_1[24] = T.float32(0)
        Y_local_1[32] = T.float32(0)
        Y_local_1[40] = T.float32(0)
        Y_local_1[48] = T.float32(0)
        Y_local_1[56] = T.float32(0)
        Y_local_1[64] = T.float32(0)
        Y_local_1[72] = T.float32(0)
        Y_local_1[80] = T.float32(0)
        Y_local_1[88] = T.float32(0)
        Y_local_1[1] = T.float32(0)
        Y_local_1[9] = T.float32(0)
        Y_local_1[17] = T.float32(0)
        Y_local_1[25] = T.float32(0)
        Y_local_1[33] = T.float32(0)
        Y_local_1[41] = T.float32(0)
        Y_local_1[49] = T.float32(0)
        Y_local_1[57] = T.float32(0)
        Y_local_1[65] = T.float32(0)
        Y_local_1[73] = T.float32(0)
        Y_local_1[81] = T.float32(0)
        Y_local_1[89] = T.float32(0)
        Y_local_1[2] = T.float32(0)
        Y_local_1[10] = T.float32(0)
        Y_local_1[18] = T.float32(0)
        Y_local_1[26] = T.float32(0)
        Y_local_1[34] = T.float32(0)
        Y_local_1[42] = T.float32(0)
        Y_local_1[50] = T.float32(0)
        Y_local_1[58] = T.float32(0)
        Y_local_1[66] = T.float32(0)
        Y_local_1[74] = T.float32(0)
        Y_local_1[82] = T.float32(0)
        Y_local_1[90] = T.float32(0)
        Y_local_1[3] = T.float32(0)
        Y_local_1[11] = T.float32(0)
        Y_local_1[19] = T.float32(0)
        Y_local_1[27] = T.float32(0)
        Y_local_1[35] = T.float32(0)
        Y_local_1[43] = T.float32(0)
        Y_local_1[51] = T.float32(0)
        Y_local_1[59] = T.float32(0)
        Y_local_1[67] = T.float32(0)
        Y_local_1[75] = T.float32(0)
        Y_local_1[83] = T.float32(0)
        Y_local_1[91] = T.float32(0)
        Y_local_1[4] = T.float32(0)
        Y_local_1[12] = T.float32(0)
        Y_local_1[20] = T.float32(0)
        Y_local_1[28] = T.float32(0)
        Y_local_1[36] = T.float32(0)
        Y_local_1[44] = T.float32(0)
        Y_local_1[52] = T.float32(0)
        Y_local_1[60] = T.float32(0)
        Y_local_1[68] = T.float32(0)
        Y_local_1[76] = T.float32(0)
        Y_local_1[84] = T.float32(0)
        Y_local_1[92] = T.float32(0)
        Y_local_1[5] = T.float32(0)
        Y_local_1[13] = T.float32(0)
        Y_local_1[21] = T.float32(0)
        Y_local_1[29] = T.float32(0)
        Y_local_1[37] = T.float32(0)
        Y_local_1[45] = T.float32(0)
        Y_local_1[53] = T.float32(0)
        Y_local_1[61] = T.float32(0)
        Y_local_1[69] = T.float32(0)
        Y_local_1[77] = T.float32(0)
        Y_local_1[85] = T.float32(0)
        Y_local_1[93] = T.float32(0)
        Y_local_1[6] = T.float32(0)
        Y_local_1[14] = T.float32(0)
        Y_local_1[22] = T.float32(0)
        Y_local_1[30] = T.float32(0)
        Y_local_1[38] = T.float32(0)
        Y_local_1[46] = T.float32(0)
        Y_local_1[54] = T.float32(0)
        Y_local_1[62] = T.float32(0)
        Y_local_1[70] = T.float32(0)
        Y_local_1[78] = T.float32(0)
        Y_local_1[86] = T.float32(0)
        Y_local_1[94] = T.float32(0)
        Y_local_1[7] = T.float32(0)
        Y_local_1[15] = T.float32(0)
        Y_local_1[23] = T.float32(0)
        Y_local_1[31] = T.float32(0)
        Y_local_1[39] = T.float32(0)
        Y_local_1[47] = T.float32(0)
        Y_local_1[55] = T.float32(0)
        Y_local_1[63] = T.float32(0)
        Y_local_1[71] = T.float32(0)
        Y_local_1[79] = T.float32(0)
        Y_local_1[87] = T.float32(0)
        Y_local_1[95] = T.float32(0)
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x] = A_1[blockIdx_x // 4 * 147456 + threadIdx_x // 4 * 1536 + threadIdx_x % 4]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 4] = B_1[threadIdx_x // 96 * 1536 + blockIdx_x % 4 * 384 + threadIdx_x % 96 * 4:threadIdx_x // 96 * 1536 + blockIdx_x % 4 * 384 + threadIdx_x % 96 * 4 + 4]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x + 384] = A_1[blockIdx_x // 4 * 147456 + threadIdx_x // 4 * 1536 + threadIdx_x % 4 + 4]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 1536:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 1536 + 4] = B_1[threadIdx_x // 96 * 1536 + blockIdx_x % 4 * 384 + threadIdx_x % 96 * 4 + 6144:threadIdx_x // 96 * 1536 + blockIdx_x % 4 * 384 + threadIdx_x % 96 * 4 + 6144 + 4]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x + 768] = A_1[blockIdx_x // 4 * 147456 + threadIdx_x // 4 * 1536 + threadIdx_x % 4 + 8]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 3072:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 3072 + 4] = B_1[threadIdx_x // 96 * 1536 + blockIdx_x % 4 * 384 + threadIdx_x % 96 * 4 + 12288:threadIdx_x // 96 * 1536 + blockIdx_x % 4 * 384 + threadIdx_x % 96 * 4 + 12288 + 4]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x + 1152] = A_1[blockIdx_x // 4 * 147456 + threadIdx_x // 4 * 1536 + threadIdx_x % 4 + 12]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 4608:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 4608 + 4] = B_1[threadIdx_x // 96 * 1536 + blockIdx_x % 4 * 384 + threadIdx_x % 96 * 4 + 18432:threadIdx_x // 96 * 1536 + blockIdx_x % 4 * 384 + threadIdx_x % 96 * 4 + 18432 + 4]
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 3)
            for ax0_0 in T.serial(3):
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16:threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 16:4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4:threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4]
        for k_0 in T.serial(380):
            cse_var_1: T.int32 = (k_0 + 4) % 5
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    A_shared_dyn_1[cse_var_1 * 384 + threadIdx_x] = A_1[blockIdx_x // 4 * 147456 + threadIdx_x // 4 * 1536 + k_0 * 4 + threadIdx_x % 4 + 16]
                T.attr(0, "async_scope", 1)
                B_shared_dyn_1[cse_var_1 * 1536 + threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4:cse_var_1 * 1536 + threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 4] = B_1[k_0 * 6144 + threadIdx_x // 96 * 1536 + blockIdx_x % 4 * 384 + threadIdx_x % 96 * 4 + 24576:k_0 * 6144 + threadIdx_x // 96 * 1536 + blockIdx_x % 4 * 384 + threadIdx_x % 96 * 4 + 24576 + 4]
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 3)
                for ax0_0 in T.serial(3):
                    A_shared_dyn_local_1[ax0_0 + 3] = A_shared_dyn_1[k_0 % 5 * 384 + threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 1:k_0 % 5 * 384 + threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 1 + 16:4]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[k_0 % 5 * 1536 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 384:k_0 % 5 * 1536 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 384 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[64:96:8] = Y_local_1[64:96:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[65:97:8] = Y_local_1[65:97:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[66:98:8] = Y_local_1[66:98:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[67:99:8] = Y_local_1[67:99:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[68:100:8] = Y_local_1[68:100:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[69:101:8] = Y_local_1[69:101:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[70:102:8] = Y_local_1[70:102:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[71:103:8] = Y_local_1[71:103:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
                for ax0_0 in T.serial(3):
                    A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[k_0 % 5 * 384 + threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 2:k_0 % 5 * 384 + threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 2 + 16:4]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[k_0 % 5 * 1536 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 768:k_0 % 5 * 1536 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 768 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[8], 4)
                Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[8], 4)
                Y_local_1[64:96:8] = Y_local_1[64:96:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[8], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[9], 4)
                Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[9], 4)
                Y_local_1[65:97:8] = Y_local_1[65:97:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[9], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[10], 4)
                Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[10], 4)
                Y_local_1[66:98:8] = Y_local_1[66:98:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[10], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[11], 4)
                Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[11], 4)
                Y_local_1[67:99:8] = Y_local_1[67:99:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[11], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
                Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[12], 4)
                Y_local_1[68:100:8] = Y_local_1[68:100:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[12], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
                Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[13], 4)
                Y_local_1[69:101:8] = Y_local_1[69:101:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[13], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
                Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[14], 4)
                Y_local_1[70:102:8] = Y_local_1[70:102:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[14], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
                Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[15], 4)
                Y_local_1[71:103:8] = Y_local_1[71:103:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[15], 4)
                for ax0_0 in T.serial(3):
                    A_shared_dyn_local_1[ax0_0 + 3] = A_shared_dyn_1[k_0 % 5 * 384 + threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 3:k_0 % 5 * 384 + threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 3 + 16:4]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[k_0 % 5 * 1536 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1152:k_0 % 5 * 1536 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1152 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[64:96:8] = Y_local_1[64:96:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[65:97:8] = Y_local_1[65:97:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[66:98:8] = Y_local_1[66:98:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[67:99:8] = Y_local_1[67:99:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[68:100:8] = Y_local_1[68:100:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[69:101:8] = Y_local_1[69:101:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[70:102:8] = Y_local_1[70:102:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[71:103:8] = Y_local_1[71:103:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
            for ax0_0 in T.serial(3):
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[(k_0 + 1) % 5 * 384 + threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16:(k_0 + 1) % 5 * 384 + threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 16:4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[(k_0 + 1) % 5 * 1536 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4:(k_0 + 1) % 5 * 1536 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[64:96:8] = Y_local_1[64:96:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[65:97:8] = Y_local_1[65:97:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[66:98:8] = Y_local_1[66:98:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[67:99:8] = Y_local_1[67:99:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[68:100:8] = Y_local_1[68:100:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[69:101:8] = Y_local_1[69:101:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[70:102:8] = Y_local_1[70:102:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
            Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[15], 4)
            Y_local_1[71:103:8] = Y_local_1[71:103:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[15], 4)
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 2)
            for ax0_0 in T.serial(3):
                A_shared_dyn_local_1[ax0_0 + 3] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 1:threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 1 + 16:4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 384:threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 384 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[64:96:8] = Y_local_1[64:96:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[65:97:8] = Y_local_1[65:97:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[66:98:8] = Y_local_1[66:98:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[67:99:8] = Y_local_1[67:99:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[68:100:8] = Y_local_1[68:100:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[69:101:8] = Y_local_1[69:101:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[70:102:8] = Y_local_1[70:102:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[71:103:8] = Y_local_1[71:103:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
            for ax0_0 in T.serial(3):
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 2:threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 2 + 16:4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 768:threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 768 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[64:96:8] = Y_local_1[64:96:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[65:97:8] = Y_local_1[65:97:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[66:98:8] = Y_local_1[66:98:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[67:99:8] = Y_local_1[67:99:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[68:100:8] = Y_local_1[68:100:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[69:101:8] = Y_local_1[69:101:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[70:102:8] = Y_local_1[70:102:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
            Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[15], 4)
            Y_local_1[71:103:8] = Y_local_1[71:103:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[15], 4)
            for ax0_0 in T.serial(3):
                A_shared_dyn_local_1[ax0_0 + 3] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 3:threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 3 + 16:4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1152:threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1152 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[64:96:8] = Y_local_1[64:96:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[65:97:8] = Y_local_1[65:97:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[66:98:8] = Y_local_1[66:98:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[67:99:8] = Y_local_1[67:99:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[68:100:8] = Y_local_1[68:100:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[69:101:8] = Y_local_1[69:101:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[70:102:8] = Y_local_1[70:102:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[71:103:8] = Y_local_1[71:103:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
        for ax0_0 in T.serial(3):
            A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 384:threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 384 + 16:4]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1536:threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1536 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[64:96:8] = Y_local_1[64:96:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[65:97:8] = Y_local_1[65:97:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[66:98:8] = Y_local_1[66:98:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[67:99:8] = Y_local_1[67:99:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[68:100:8] = Y_local_1[68:100:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[69:101:8] = Y_local_1[69:101:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[70:102:8] = Y_local_1[70:102:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[71:103:8] = Y_local_1[71:103:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[15], 4)
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 1)
            for ax0_0 in T.serial(3):
                A_shared_dyn_local_1[ax0_0 + 3] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 385:threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 385 + 16:4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1920:threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1920 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[64:96:8] = Y_local_1[64:96:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[65:97:8] = Y_local_1[65:97:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[66:98:8] = Y_local_1[66:98:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[67:99:8] = Y_local_1[67:99:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[68:100:8] = Y_local_1[68:100:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[69:101:8] = Y_local_1[69:101:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[70:102:8] = Y_local_1[70:102:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[71:103:8] = Y_local_1[71:103:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
            for ax0_0 in T.serial(3):
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 386:threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 386 + 16:4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2304:threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2304 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[64:96:8] = Y_local_1[64:96:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[65:97:8] = Y_local_1[65:97:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[66:98:8] = Y_local_1[66:98:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[67:99:8] = Y_local_1[67:99:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[68:100:8] = Y_local_1[68:100:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[69:101:8] = Y_local_1[69:101:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[70:102:8] = Y_local_1[70:102:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
            Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[15], 4)
            Y_local_1[71:103:8] = Y_local_1[71:103:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[15], 4)
            for ax0_0 in T.serial(3):
                A_shared_dyn_local_1[ax0_0 + 3] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 387:threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 387 + 16:4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2688:threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2688 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[64:96:8] = Y_local_1[64:96:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[65:97:8] = Y_local_1[65:97:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[66:98:8] = Y_local_1[66:98:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[67:99:8] = Y_local_1[67:99:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[68:100:8] = Y_local_1[68:100:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[69:101:8] = Y_local_1[69:101:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[70:102:8] = Y_local_1[70:102:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[71:103:8] = Y_local_1[71:103:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
        for ax0_0 in T.serial(3):
            A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 768:threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 768 + 16:4]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 3072:threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 3072 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[64:96:8] = Y_local_1[64:96:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[65:97:8] = Y_local_1[65:97:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[66:98:8] = Y_local_1[66:98:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[67:99:8] = Y_local_1[67:99:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[68:100:8] = Y_local_1[68:100:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[69:101:8] = Y_local_1[69:101:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[70:102:8] = Y_local_1[70:102:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[71:103:8] = Y_local_1[71:103:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[15], 4)
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 0)
            for ax0_0 in T.serial(3):
                A_shared_dyn_local_1[ax0_0 + 3] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 769:threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 769 + 16:4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 3456:threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 3456 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[64:96:8] = Y_local_1[64:96:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[65:97:8] = Y_local_1[65:97:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[66:98:8] = Y_local_1[66:98:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[67:99:8] = Y_local_1[67:99:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[68:100:8] = Y_local_1[68:100:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[69:101:8] = Y_local_1[69:101:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[70:102:8] = Y_local_1[70:102:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[71:103:8] = Y_local_1[71:103:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
            for ax0_0 in T.serial(3):
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 770:threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 770 + 16:4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 3840:threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 3840 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[64:96:8] = Y_local_1[64:96:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[65:97:8] = Y_local_1[65:97:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[66:98:8] = Y_local_1[66:98:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[67:99:8] = Y_local_1[67:99:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[68:100:8] = Y_local_1[68:100:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[69:101:8] = Y_local_1[69:101:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[70:102:8] = Y_local_1[70:102:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
            Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[15], 4)
            Y_local_1[71:103:8] = Y_local_1[71:103:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[15], 4)
            for ax0_0 in T.serial(3):
                A_shared_dyn_local_1[ax0_0 + 3] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 771:threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 771 + 16:4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4224:threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4224 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[64:96:8] = Y_local_1[64:96:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[65:97:8] = Y_local_1[65:97:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[66:98:8] = Y_local_1[66:98:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[67:99:8] = Y_local_1[67:99:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[68:100:8] = Y_local_1[68:100:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[69:101:8] = Y_local_1[69:101:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[70:102:8] = Y_local_1[70:102:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[71:103:8] = Y_local_1[71:103:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
        for ax0_0 in T.serial(3):
            A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 1152:threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 1152 + 16:4]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4608:threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4608 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[64:96:8] = Y_local_1[64:96:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[65:97:8] = Y_local_1[65:97:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[66:98:8] = Y_local_1[66:98:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[67:99:8] = Y_local_1[67:99:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[68:100:8] = Y_local_1[68:100:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[69:101:8] = Y_local_1[69:101:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[70:102:8] = Y_local_1[70:102:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[71:103:8] = Y_local_1[71:103:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[15], 4)
        for ax0_0 in T.serial(3):
            A_shared_dyn_local_1[ax0_0 + 3] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 1153:threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 1153 + 16:4]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4992:threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4992 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[64:96:8] = Y_local_1[64:96:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[65:97:8] = Y_local_1[65:97:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[66:98:8] = Y_local_1[66:98:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[67:99:8] = Y_local_1[67:99:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[68:100:8] = Y_local_1[68:100:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[69:101:8] = Y_local_1[69:101:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[70:102:8] = Y_local_1[70:102:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[71:103:8] = Y_local_1[71:103:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
        for ax0_0 in T.serial(3):
            A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 1154:threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 1154 + 16:4]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 5376:threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 5376 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[64:96:8] = Y_local_1[64:96:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[65:97:8] = Y_local_1[65:97:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[66:98:8] = Y_local_1[66:98:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[67:99:8] = Y_local_1[67:99:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[68:100:8] = Y_local_1[68:100:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[69:101:8] = Y_local_1[69:101:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[70:102:8] = Y_local_1[70:102:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[71:103:8] = Y_local_1[71:103:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[15], 4)
        for ax0_0 in T.serial(3):
            A_shared_dyn_local_1[ax0_0 + 3] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 1155:threadIdx_x % 128 // 32 * 96 + threadIdx_x % 2 * 48 + ax0_0 * 16 + 1155 + 16:4]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 5760:threadIdx_x // 128 * 128 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 5760 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[64:96:8] = Y_local_1[64:96:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[65:97:8] = Y_local_1[65:97:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[66:98:8] = Y_local_1[66:98:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[67:99:8] = Y_local_1[67:99:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[68:100:8] = Y_local_1[68:100:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[69:101:8] = Y_local_1[69:101:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[70:102:8] = Y_local_1[70:102:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[71:103:8] = Y_local_1[71:103:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[64:96:8] = Y_local_1[64:96:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[65:97:8] = Y_local_1[65:97:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[66:98:8] = Y_local_1[66:98:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[67:99:8] = Y_local_1[67:99:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[68:100:8] = Y_local_1[68:100:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[69:101:8] = Y_local_1[69:101:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[70:102:8] = Y_local_1[70:102:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[71:103:8] = Y_local_1[71:103:8] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[15], 4)
        for ax1_0 in T.serial(2):
            cse_var_2: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 128 // 32 * 36864 + threadIdx_x % 2 * 18432 + blockIdx_x % 4 * 384 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 2 * 8 + cse_var_2:blockIdx_x // 4 * 147456 + threadIdx_x % 128 // 32 * 36864 + threadIdx_x % 2 * 18432 + blockIdx_x % 4 * 384 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 2 * 8 + cse_var_2 + 4] = Y_local_1[cse_var_2:cse_var_2 + 4]
        for ax1_0 in T.serial(2):
            cse_var_3: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 128 // 32 * 36864 + threadIdx_x % 2 * 18432 + blockIdx_x % 4 * 384 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 2 * 8 + cse_var_3 + 1536:blockIdx_x // 4 * 147456 + threadIdx_x % 128 // 32 * 36864 + threadIdx_x % 2 * 18432 + blockIdx_x % 4 * 384 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 2 * 8 + cse_var_3 + 1536 + 4] = Y_local_1[cse_var_3 + 8:cse_var_3 + 8 + 4]
        for ax1_0 in T.serial(2):
            cse_var_4: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 128 // 32 * 36864 + threadIdx_x % 2 * 18432 + blockIdx_x % 4 * 384 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 2 * 8 + cse_var_4 + 3072:blockIdx_x // 4 * 147456 + threadIdx_x % 128 // 32 * 36864 + threadIdx_x % 2 * 18432 + blockIdx_x % 4 * 384 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 2 * 8 + cse_var_4 + 3072 + 4] = Y_local_1[cse_var_4 + 16:cse_var_4 + 16 + 4]
        for ax1_0 in T.serial(2):
            cse_var_5: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 128 // 32 * 36864 + threadIdx_x % 2 * 18432 + blockIdx_x % 4 * 384 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 2 * 8 + cse_var_5 + 4608:blockIdx_x // 4 * 147456 + threadIdx_x % 128 // 32 * 36864 + threadIdx_x % 2 * 18432 + blockIdx_x % 4 * 384 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 2 * 8 + cse_var_5 + 4608 + 4] = Y_local_1[cse_var_5 + 24:cse_var_5 + 24 + 4]
        for ax1_0 in T.serial(2):
            cse_var_6: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 128 // 32 * 36864 + threadIdx_x % 2 * 18432 + blockIdx_x % 4 * 384 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 2 * 8 + cse_var_6 + 6144:blockIdx_x // 4 * 147456 + threadIdx_x % 128 // 32 * 36864 + threadIdx_x % 2 * 18432 + blockIdx_x % 4 * 384 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 2 * 8 + cse_var_6 + 6144 + 4] = Y_local_1[cse_var_6 + 32:cse_var_6 + 32 + 4]
        for ax1_0 in T.serial(2):
            cse_var_7: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 128 // 32 * 36864 + threadIdx_x % 2 * 18432 + blockIdx_x % 4 * 384 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 2 * 8 + cse_var_7 + 7680:blockIdx_x // 4 * 147456 + threadIdx_x % 128 // 32 * 36864 + threadIdx_x % 2 * 18432 + blockIdx_x % 4 * 384 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 2 * 8 + cse_var_7 + 7680 + 4] = Y_local_1[cse_var_7 + 40:cse_var_7 + 40 + 4]
        for ax1_0 in T.serial(2):
            cse_var_8: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 128 // 32 * 36864 + threadIdx_x % 2 * 18432 + blockIdx_x % 4 * 384 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 2 * 8 + cse_var_8 + 9216:blockIdx_x // 4 * 147456 + threadIdx_x % 128 // 32 * 36864 + threadIdx_x % 2 * 18432 + blockIdx_x % 4 * 384 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 2 * 8 + cse_var_8 + 9216 + 4] = Y_local_1[cse_var_8 + 48:cse_var_8 + 48 + 4]
        for ax1_0 in T.serial(2):
            cse_var_9: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 128 // 32 * 36864 + threadIdx_x % 2 * 18432 + blockIdx_x % 4 * 384 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 2 * 8 + cse_var_9 + 10752:blockIdx_x // 4 * 147456 + threadIdx_x % 128 // 32 * 36864 + threadIdx_x % 2 * 18432 + blockIdx_x % 4 * 384 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 2 * 8 + cse_var_9 + 10752 + 4] = Y_local_1[cse_var_9 + 56:cse_var_9 + 56 + 4]
        for ax1_0 in T.serial(2):
            cse_var_10: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 128 // 32 * 36864 + threadIdx_x % 2 * 18432 + blockIdx_x % 4 * 384 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 2 * 8 + cse_var_10 + 12288:blockIdx_x // 4 * 147456 + threadIdx_x % 128 // 32 * 36864 + threadIdx_x % 2 * 18432 + blockIdx_x % 4 * 384 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 2 * 8 + cse_var_10 + 12288 + 4] = Y_local_1[cse_var_10 + 64:cse_var_10 + 64 + 4]
        for ax1_0 in T.serial(2):
            cse_var_11: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 128 // 32 * 36864 + threadIdx_x % 2 * 18432 + blockIdx_x % 4 * 384 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 2 * 8 + cse_var_11 + 13824:blockIdx_x // 4 * 147456 + threadIdx_x % 128 // 32 * 36864 + threadIdx_x % 2 * 18432 + blockIdx_x % 4 * 384 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 2 * 8 + cse_var_11 + 13824 + 4] = Y_local_1[cse_var_11 + 72:cse_var_11 + 72 + 4]
        for ax1_0 in T.serial(2):
            cse_var_12: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 128 // 32 * 36864 + threadIdx_x % 2 * 18432 + blockIdx_x % 4 * 384 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 2 * 8 + cse_var_12 + 15360:blockIdx_x // 4 * 147456 + threadIdx_x % 128 // 32 * 36864 + threadIdx_x % 2 * 18432 + blockIdx_x % 4 * 384 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 2 * 8 + cse_var_12 + 15360 + 4] = Y_local_1[cse_var_12 + 80:cse_var_12 + 80 + 4]
        for ax1_0 in T.serial(2):
            cse_var_13: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 4 * 147456 + threadIdx_x % 128 // 32 * 36864 + threadIdx_x % 2 * 18432 + blockIdx_x % 4 * 384 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 2 * 8 + cse_var_13 + 16896:blockIdx_x // 4 * 147456 + threadIdx_x % 128 // 32 * 36864 + threadIdx_x % 2 * 18432 + blockIdx_x % 4 * 384 + threadIdx_x // 128 * 128 + threadIdx_x % 32 // 2 * 8 + cse_var_13 + 16896 + 4] = Y_local_1[cse_var_13 + 88:cse_var_13 + 88 + 4]
    

