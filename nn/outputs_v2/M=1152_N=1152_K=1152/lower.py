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
        T.launch_thread(blockIdx_x, 108)
        Y_local = T.allocate([96], "float32", "local")
        Y_local_1 = T.buffer_decl([96], dtype="float32", data=Y_local, scope="local")
        A_shared_dyn = T.allocate([1920], "float32", "shared.dyn")
        A_shared_dyn_1 = T.buffer_decl([1920], dtype="float32", data=A_shared_dyn, scope="shared.dyn")
        B_shared_dyn = T.allocate([2560], "float32", "shared.dyn")
        B_shared_dyn_1 = T.buffer_decl([2560], dtype="float32", data=B_shared_dyn, scope="shared.dyn")
        A_shared_dyn_local = T.allocate([6], "float32x4", "local")
        A_shared_dyn_local_1 = T.buffer_decl([6], dtype="float32x4", data=A_shared_dyn_local, scope="local")
        B_shared_dyn_local = T.allocate([16], "float32", "local")
        B_shared_dyn_local_1 = T.buffer_decl([16], dtype="float32", data=B_shared_dyn_local, scope="local")
        T.launch_thread(threadIdx_x, 128)
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
                A_shared_dyn_1[threadIdx_x % 4 * 96 + threadIdx_x // 4 * 3 // 32 * 32 + threadIdx_x // 4 * 3 % 8 // 4 * 16 + threadIdx_x // 4 * 3 % 32 // 8 * 4 + threadIdx_x // 4 * 3 % 4] = A_1[blockIdx_x // 9 * 110592 + threadIdx_x // 4 * 3456 + threadIdx_x % 4]
                A_shared_dyn_1[threadIdx_x % 4 * 96 + (threadIdx_x // 4 * 3 + 1) // 32 * 32 + (threadIdx_x // 4 * 3 + 1) % 8 // 4 * 16 + (threadIdx_x // 4 * 3 + 1) % 32 // 8 * 4 + (threadIdx_x // 4 * 3 + 1) % 4] = A_1[blockIdx_x // 9 * 110592 + threadIdx_x // 4 * 3456 + threadIdx_x % 4 + 1152]
                A_shared_dyn_1[threadIdx_x % 4 * 96 + (threadIdx_x // 4 * 3 + 2) // 32 * 32 + (threadIdx_x // 4 * 3 + 2) % 8 // 4 * 16 + (threadIdx_x // 4 * 3 + 2) % 32 // 8 * 4 + (threadIdx_x // 4 * 3 + 2) % 4] = A_1[blockIdx_x // 9 * 110592 + threadIdx_x // 4 * 3456 + threadIdx_x % 4 + 2304]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 4] = B_1[threadIdx_x // 32 * 1152 + blockIdx_x % 9 * 128 + threadIdx_x % 32 * 4:threadIdx_x // 32 * 1152 + blockIdx_x % 9 * 128 + threadIdx_x % 32 * 4 + 4]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x % 4 * 96 + threadIdx_x // 4 * 3 // 32 * 32 + threadIdx_x // 4 * 3 % 8 // 4 * 16 + threadIdx_x // 4 * 3 % 32 // 8 * 4 + threadIdx_x // 4 * 3 % 4 + 384] = A_1[blockIdx_x // 9 * 110592 + threadIdx_x // 4 * 3456 + threadIdx_x % 4 + 4]
                A_shared_dyn_1[threadIdx_x % 4 * 96 + (threadIdx_x // 4 * 3 + 1) // 32 * 32 + (threadIdx_x // 4 * 3 + 1) % 8 // 4 * 16 + (threadIdx_x // 4 * 3 + 1) % 32 // 8 * 4 + (threadIdx_x // 4 * 3 + 1) % 4 + 384] = A_1[blockIdx_x // 9 * 110592 + threadIdx_x // 4 * 3456 + threadIdx_x % 4 + 1156]
                A_shared_dyn_1[threadIdx_x % 4 * 96 + (threadIdx_x // 4 * 3 + 2) // 32 * 32 + (threadIdx_x // 4 * 3 + 2) % 8 // 4 * 16 + (threadIdx_x // 4 * 3 + 2) % 32 // 8 * 4 + (threadIdx_x // 4 * 3 + 2) % 4 + 384] = A_1[blockIdx_x // 9 * 110592 + threadIdx_x // 4 * 3456 + threadIdx_x % 4 + 2308]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 512:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 512 + 4] = B_1[threadIdx_x // 32 * 1152 + blockIdx_x % 9 * 128 + threadIdx_x % 32 * 4 + 4608:threadIdx_x // 32 * 1152 + blockIdx_x % 9 * 128 + threadIdx_x % 32 * 4 + 4608 + 4]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x % 4 * 96 + threadIdx_x // 4 * 3 // 32 * 32 + threadIdx_x // 4 * 3 % 8 // 4 * 16 + threadIdx_x // 4 * 3 % 32 // 8 * 4 + threadIdx_x // 4 * 3 % 4 + 768] = A_1[blockIdx_x // 9 * 110592 + threadIdx_x // 4 * 3456 + threadIdx_x % 4 + 8]
                A_shared_dyn_1[threadIdx_x % 4 * 96 + (threadIdx_x // 4 * 3 + 1) // 32 * 32 + (threadIdx_x // 4 * 3 + 1) % 8 // 4 * 16 + (threadIdx_x // 4 * 3 + 1) % 32 // 8 * 4 + (threadIdx_x // 4 * 3 + 1) % 4 + 768] = A_1[blockIdx_x // 9 * 110592 + threadIdx_x // 4 * 3456 + threadIdx_x % 4 + 1160]
                A_shared_dyn_1[threadIdx_x % 4 * 96 + (threadIdx_x // 4 * 3 + 2) // 32 * 32 + (threadIdx_x // 4 * 3 + 2) % 8 // 4 * 16 + (threadIdx_x // 4 * 3 + 2) % 32 // 8 * 4 + (threadIdx_x // 4 * 3 + 2) % 4 + 768] = A_1[blockIdx_x // 9 * 110592 + threadIdx_x // 4 * 3456 + threadIdx_x % 4 + 2312]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 1024:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 1024 + 4] = B_1[threadIdx_x // 32 * 1152 + blockIdx_x % 9 * 128 + threadIdx_x % 32 * 4 + 9216:threadIdx_x // 32 * 1152 + blockIdx_x % 9 * 128 + threadIdx_x % 32 * 4 + 9216 + 4]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x % 4 * 96 + threadIdx_x // 4 * 3 // 32 * 32 + threadIdx_x // 4 * 3 % 8 // 4 * 16 + threadIdx_x // 4 * 3 % 32 // 8 * 4 + threadIdx_x // 4 * 3 % 4 + 1152] = A_1[blockIdx_x // 9 * 110592 + threadIdx_x // 4 * 3456 + threadIdx_x % 4 + 12]
                A_shared_dyn_1[threadIdx_x % 4 * 96 + (threadIdx_x // 4 * 3 + 1) // 32 * 32 + (threadIdx_x // 4 * 3 + 1) % 8 // 4 * 16 + (threadIdx_x // 4 * 3 + 1) % 32 // 8 * 4 + (threadIdx_x // 4 * 3 + 1) % 4 + 1152] = A_1[blockIdx_x // 9 * 110592 + threadIdx_x // 4 * 3456 + threadIdx_x % 4 + 1164]
                A_shared_dyn_1[threadIdx_x % 4 * 96 + (threadIdx_x // 4 * 3 + 2) // 32 * 32 + (threadIdx_x // 4 * 3 + 2) % 8 // 4 * 16 + (threadIdx_x // 4 * 3 + 2) % 32 // 8 * 4 + (threadIdx_x // 4 * 3 + 2) % 4 + 1152] = A_1[blockIdx_x // 9 * 110592 + threadIdx_x // 4 * 3456 + threadIdx_x % 4 + 2316]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 1536:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 1536 + 4] = B_1[threadIdx_x // 32 * 1152 + blockIdx_x % 9 * 128 + threadIdx_x % 32 * 4 + 13824:threadIdx_x // 32 * 1152 + blockIdx_x % 9 * 128 + threadIdx_x % 32 * 4 + 13824 + 4]
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 3)
            for ax0_0 in T.serial(3):
                cse_var_1: T.int32 = ax0_0 * 4
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_1) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_1) // 8) % 4 * 4:(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_1) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_1) // 8) % 4 * 4 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4:threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4]
        for k_0 in T.serial(284):
            cse_var_2: T.int32 = (k_0 + 4) % 5
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    A_shared_dyn_1[cse_var_2 * 384 + threadIdx_x % 4 * 96 + threadIdx_x // 4 * 3 // 32 * 32 + threadIdx_x // 4 * 3 % 8 // 4 * 16 + threadIdx_x // 4 * 3 % 32 // 8 * 4 + threadIdx_x // 4 * 3 % 4] = A_1[blockIdx_x // 9 * 110592 + threadIdx_x // 4 * 3456 + k_0 * 4 + threadIdx_x % 4 + 16]
                    A_shared_dyn_1[cse_var_2 * 384 + threadIdx_x % 4 * 96 + (threadIdx_x // 4 * 3 + 1) // 32 * 32 + (threadIdx_x // 4 * 3 + 1) % 8 // 4 * 16 + (threadIdx_x // 4 * 3 + 1) % 32 // 8 * 4 + (threadIdx_x // 4 * 3 + 1) % 4] = A_1[blockIdx_x // 9 * 110592 + threadIdx_x // 4 * 3456 + k_0 * 4 + threadIdx_x % 4 + 1168]
                    A_shared_dyn_1[cse_var_2 * 384 + threadIdx_x % 4 * 96 + (threadIdx_x // 4 * 3 + 2) // 32 * 32 + (threadIdx_x // 4 * 3 + 2) % 8 // 4 * 16 + (threadIdx_x // 4 * 3 + 2) % 32 // 8 * 4 + (threadIdx_x // 4 * 3 + 2) % 4] = A_1[blockIdx_x // 9 * 110592 + threadIdx_x // 4 * 3456 + k_0 * 4 + threadIdx_x % 4 + 2320]
                T.attr(0, "async_scope", 1)
                B_shared_dyn_1[cse_var_2 * 512 + threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4:cse_var_2 * 512 + threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 4] = B_1[k_0 * 4608 + threadIdx_x // 32 * 1152 + blockIdx_x % 9 * 128 + threadIdx_x % 32 * 4 + 18432:k_0 * 4608 + threadIdx_x // 32 * 1152 + blockIdx_x % 9 * 128 + threadIdx_x % 32 * 4 + 18432 + 4]
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 3)
                for ax0_0 in T.serial(3):
                    cse_var_3: T.int32 = ax0_0 * 4
                    A_shared_dyn_local_1[ax0_0 + 3] = A_shared_dyn_1[k_0 % 5 * 384 + (threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_3) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_3) // 8) % 4 * 4 + 96:k_0 % 5 * 384 + (threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_3) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_3) // 8) % 4 * 4 + 96 + 4]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[k_0 % 5 * 512 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 128:k_0 % 5 * 512 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 128 + 4]
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
                    cse_var_4: T.int32 = ax0_0 * 4
                    A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[k_0 % 5 * 384 + (threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_4) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_4) // 8) % 4 * 4 + 192:k_0 % 5 * 384 + (threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_4) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_4) // 8) % 4 * 4 + 192 + 4]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[k_0 % 5 * 512 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 256:k_0 % 5 * 512 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 256 + 4]
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
                    cse_var_5: T.int32 = ax0_0 * 4
                    A_shared_dyn_local_1[ax0_0 + 3] = A_shared_dyn_1[k_0 % 5 * 384 + (threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_5) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_5) // 8) % 4 * 4 + 288:k_0 % 5 * 384 + (threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_5) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_5) // 8) % 4 * 4 + 288 + 4]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[k_0 % 5 * 512 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 384:k_0 % 5 * 512 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 384 + 4]
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
                cse_var_6: T.int32 = ax0_0 * 4
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[(k_0 + 1) % 5 * 384 + (threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_6) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_6) // 8) % 4 * 4:(k_0 + 1) % 5 * 384 + (threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_6) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_6) // 8) % 4 * 4 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[(k_0 + 1) % 5 * 512 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4:(k_0 + 1) % 5 * 512 + threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4]
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
                cse_var_7: T.int32 = ax0_0 * 4
                A_shared_dyn_local_1[ax0_0 + 3] = A_shared_dyn_1[(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_7) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_7) // 8) % 4 * 4 + 1632:(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_7) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_7) // 8) % 4 * 4 + 1632 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2176:threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2176 + 4]
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
                cse_var_8: T.int32 = ax0_0 * 4
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_8) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_8) // 8) % 4 * 4 + 1728:(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_8) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_8) // 8) % 4 * 4 + 1728 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2304:threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2304 + 4]
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
                cse_var_9: T.int32 = ax0_0 * 4
                A_shared_dyn_local_1[ax0_0 + 3] = A_shared_dyn_1[(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_9) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_9) // 8) % 4 * 4 + 1824:(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_9) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_9) // 8) % 4 * 4 + 1824 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2432:threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2432 + 4]
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
            cse_var_10: T.int32 = ax0_0 * 4
            A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_10) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_10) // 8) % 4 * 4:(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_10) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_10) // 8) % 4 * 4 + 4]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4:threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4]
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
                cse_var_11: T.int32 = ax0_0 * 4
                A_shared_dyn_local_1[ax0_0 + 3] = A_shared_dyn_1[(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_11) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_11) // 8) % 4 * 4 + 96:(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_11) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_11) // 8) % 4 * 4 + 96 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 128:threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 128 + 4]
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
                cse_var_12: T.int32 = ax0_0 * 4
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_12) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_12) // 8) % 4 * 4 + 192:(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_12) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_12) // 8) % 4 * 4 + 192 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 256:threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 256 + 4]
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
                cse_var_13: T.int32 = ax0_0 * 4
                A_shared_dyn_local_1[ax0_0 + 3] = A_shared_dyn_1[(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_13) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_13) // 8) % 4 * 4 + 288:(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_13) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_13) // 8) % 4 * 4 + 288 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 384:threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 384 + 4]
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
            cse_var_14: T.int32 = ax0_0 * 4
            A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_14) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_14) // 8) % 4 * 4 + 384:(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_14) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_14) // 8) % 4 * 4 + 384 + 4]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 512:threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 512 + 4]
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
                cse_var_15: T.int32 = ax0_0 * 4
                A_shared_dyn_local_1[ax0_0 + 3] = A_shared_dyn_1[(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_15) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_15) // 8) % 4 * 4 + 480:(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_15) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_15) // 8) % 4 * 4 + 480 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 640:threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 640 + 4]
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
                cse_var_16: T.int32 = ax0_0 * 4
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_16) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_16) // 8) % 4 * 4 + 576:(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_16) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_16) // 8) % 4 * 4 + 576 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 768:threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 768 + 4]
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
                cse_var_17: T.int32 = ax0_0 * 4
                A_shared_dyn_local_1[ax0_0 + 3] = A_shared_dyn_1[(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_17) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_17) // 8) % 4 * 4 + 672:(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_17) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_17) // 8) % 4 * 4 + 672 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 896:threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 896 + 4]
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
            cse_var_18: T.int32 = ax0_0 * 4
            A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_18) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_18) // 8) % 4 * 4 + 768:(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_18) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_18) // 8) % 4 * 4 + 768 + 4]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1024:threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1024 + 4]
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
            cse_var_19: T.int32 = ax0_0 * 4
            A_shared_dyn_local_1[ax0_0 + 3] = A_shared_dyn_1[(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_19) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_19) // 8) % 4 * 4 + 864:(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_19) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_19) // 8) % 4 * 4 + 864 + 4]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1152:threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1152 + 4]
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
            cse_var_20: T.int32 = ax0_0 * 4
            A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_20) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_20) // 8) % 4 * 4 + 960:(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_20) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_20) // 8) % 4 * 4 + 960 + 4]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1280:threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1280 + 4]
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
            cse_var_21: T.int32 = ax0_0 * 4
            A_shared_dyn_local_1[ax0_0 + 3] = A_shared_dyn_1[(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_21) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_21) // 8) % 4 * 4 + 1056:(threadIdx_x // 32 * 24 + threadIdx_x % 2 * 12 + cse_var_21) // 32 * 32 + (ax0_0 + threadIdx_x % 2) % 2 * 16 + (threadIdx_x // 32 * 3 + (threadIdx_x % 2 * 12 + cse_var_21) // 8) % 4 * 4 + 1056 + 4]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1408:threadIdx_x % 32 // 16 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1408 + 4]
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
        Y_1[blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8:blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 4] = Y_local_1[0:4]
        Y_1[blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 4:blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 4 + 4] = Y_local_1[4:8]
        Y_1[blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 1152:blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 1152 + 4] = Y_local_1[8:12]
        Y_1[blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 1156:blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 1156 + 4] = Y_local_1[12:16]
        Y_1[blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 2304:blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 2304 + 4] = Y_local_1[16:20]
        Y_1[blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 2308:blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 2308 + 4] = Y_local_1[20:24]
        Y_1[blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 3456:blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 3456 + 4] = Y_local_1[24:28]
        Y_1[blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 3460:blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 3460 + 4] = Y_local_1[28:32]
        Y_1[blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 4608:blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 4608 + 4] = Y_local_1[32:36]
        Y_1[blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 4612:blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 4612 + 4] = Y_local_1[36:40]
        Y_1[blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 5760:blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 5760 + 4] = Y_local_1[40:44]
        Y_1[blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 5764:blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 5764 + 4] = Y_local_1[44:48]
        Y_1[blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 6912:blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 6912 + 4] = Y_local_1[48:52]
        Y_1[blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 6916:blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 6916 + 4] = Y_local_1[52:56]
        Y_1[blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 8064:blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 8064 + 4] = Y_local_1[56:60]
        Y_1[blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 8068:blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 8068 + 4] = Y_local_1[60:64]
        Y_1[blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 9216:blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 9216 + 4] = Y_local_1[64:68]
        Y_1[blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 9220:blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 9220 + 4] = Y_local_1[68:72]
        Y_1[blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 10368:blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 10368 + 4] = Y_local_1[72:76]
        Y_1[blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 10372:blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 10372 + 4] = Y_local_1[76:80]
        Y_1[blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 11520:blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 11520 + 4] = Y_local_1[80:84]
        Y_1[blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 11524:blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 11524 + 4] = Y_local_1[84:88]
        Y_1[blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 12672:blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 12672 + 4] = Y_local_1[88:92]
        Y_1[blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 12676:blockIdx_x // 9 * 110592 + threadIdx_x // 32 * 27648 + threadIdx_x % 2 * 13824 + blockIdx_x % 9 * 128 + threadIdx_x % 32 // 2 * 8 + 12676 + 4] = Y_local_1[92:96]
    

