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
        Y_local = T.allocate([48], "float32", "local")
        Y_local_1 = T.buffer_decl([48], dtype="float32", data=Y_local, scope="local")
        A_shared_dyn = T.allocate([4800], "float32", "shared.dyn")
        A_shared_dyn_1 = T.buffer_decl([4800], dtype="float32", data=A_shared_dyn, scope="shared.dyn")
        B_shared_dyn = T.allocate([5760], "float32", "shared.dyn")
        B_shared_dyn_1 = T.buffer_decl([5760], dtype="float32", data=B_shared_dyn, scope="shared.dyn")
        A_shared_dyn_local = T.allocate([2], "float32x4", "local")
        A_shared_dyn_local_1 = T.buffer_decl([2], dtype="float32x4", data=A_shared_dyn_local, scope="local")
        B_shared_dyn_local = T.allocate([24], "float32", "local")
        B_shared_dyn_local_1 = T.buffer_decl([24], dtype="float32", data=B_shared_dyn_local, scope="local")
        T.launch_thread(threadIdx_x, 432)
        Y_local_1[0] = T.float32(0)
        Y_local_1[12] = T.float32(0)
        Y_local_1[24] = T.float32(0)
        Y_local_1[36] = T.float32(0)
        Y_local_1[1] = T.float32(0)
        Y_local_1[13] = T.float32(0)
        Y_local_1[25] = T.float32(0)
        Y_local_1[37] = T.float32(0)
        Y_local_1[2] = T.float32(0)
        Y_local_1[14] = T.float32(0)
        Y_local_1[26] = T.float32(0)
        Y_local_1[38] = T.float32(0)
        Y_local_1[3] = T.float32(0)
        Y_local_1[15] = T.float32(0)
        Y_local_1[27] = T.float32(0)
        Y_local_1[39] = T.float32(0)
        Y_local_1[4] = T.float32(0)
        Y_local_1[16] = T.float32(0)
        Y_local_1[28] = T.float32(0)
        Y_local_1[40] = T.float32(0)
        Y_local_1[5] = T.float32(0)
        Y_local_1[17] = T.float32(0)
        Y_local_1[29] = T.float32(0)
        Y_local_1[41] = T.float32(0)
        Y_local_1[6] = T.float32(0)
        Y_local_1[18] = T.float32(0)
        Y_local_1[30] = T.float32(0)
        Y_local_1[42] = T.float32(0)
        Y_local_1[7] = T.float32(0)
        Y_local_1[19] = T.float32(0)
        Y_local_1[31] = T.float32(0)
        Y_local_1[43] = T.float32(0)
        Y_local_1[8] = T.float32(0)
        Y_local_1[20] = T.float32(0)
        Y_local_1[32] = T.float32(0)
        Y_local_1[44] = T.float32(0)
        Y_local_1[9] = T.float32(0)
        Y_local_1[21] = T.float32(0)
        Y_local_1[33] = T.float32(0)
        Y_local_1[45] = T.float32(0)
        Y_local_1[10] = T.float32(0)
        Y_local_1[22] = T.float32(0)
        Y_local_1[34] = T.float32(0)
        Y_local_1[46] = T.float32(0)
        Y_local_1[11] = T.float32(0)
        Y_local_1[23] = T.float32(0)
        Y_local_1[35] = T.float32(0)
        Y_local_1[47] = T.float32(0)
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x % 3 * 320 + (blockIdx_x // 8 * 9 + threadIdx_x // 48) // 2 * 32 + threadIdx_x % 24 // 12 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x // 24) % 4 * 4 + threadIdx_x % 12 // 3 - blockIdx_x // 8 * 144 // 32 * 32] = A_1[blockIdx_x // 8 * 165888 + threadIdx_x // 3 * 1152 + threadIdx_x % 3 * 2]
                A_shared_dyn_1[threadIdx_x % 3 * 320 + (blockIdx_x // 8 * 9 + threadIdx_x // 48) // 2 * 32 + threadIdx_x % 24 // 12 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x // 24) % 4 * 4 + threadIdx_x % 12 // 3 + 160 - blockIdx_x // 8 * 144 // 32 * 32] = A_1[blockIdx_x // 8 * 165888 + threadIdx_x // 3 * 1152 + threadIdx_x % 3 * 2 + 1]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 72 * 192 + (blockIdx_x % 8 * 144 + threadIdx_x % 72 * 2) // 64 * 64 + threadIdx_x % 4 // 2 * 32 + (blockIdx_x % 8 * 2 + threadIdx_x % 72 // 4) % 8 * 4 + threadIdx_x % 2 * 2 - blockIdx_x % 8 * 144 // 64 * 64:threadIdx_x // 72 * 192 + (blockIdx_x % 8 * 144 + threadIdx_x % 72 * 2) // 64 * 64 + threadIdx_x % 4 // 2 * 32 + (blockIdx_x % 8 * 2 + threadIdx_x % 72 // 4) % 8 * 4 + threadIdx_x % 2 * 2 - blockIdx_x % 8 * 144 // 64 * 64 + 2] = B_1[threadIdx_x // 72 * 1152 + blockIdx_x % 8 * 144 + threadIdx_x % 72 * 2:threadIdx_x // 72 * 1152 + blockIdx_x % 8 * 144 + threadIdx_x % 72 * 2 + 2]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x % 3 * 320 + (blockIdx_x // 8 * 9 + threadIdx_x // 48) // 2 * 32 + threadIdx_x % 24 // 12 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x // 24) % 4 * 4 + threadIdx_x % 12 // 3 + 960 - blockIdx_x // 8 * 144 // 32 * 32] = A_1[blockIdx_x // 8 * 165888 + threadIdx_x // 3 * 1152 + threadIdx_x % 3 * 2 + 6]
                A_shared_dyn_1[threadIdx_x % 3 * 320 + (blockIdx_x // 8 * 9 + threadIdx_x // 48) // 2 * 32 + threadIdx_x % 24 // 12 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x // 24) % 4 * 4 + threadIdx_x % 12 // 3 + 1120 - blockIdx_x // 8 * 144 // 32 * 32] = A_1[blockIdx_x // 8 * 165888 + threadIdx_x // 3 * 1152 + threadIdx_x % 3 * 2 + 7]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 72 * 192 + (blockIdx_x % 8 * 144 + threadIdx_x % 72 * 2) // 64 * 64 + threadIdx_x % 4 // 2 * 32 + (blockIdx_x % 8 * 2 + threadIdx_x % 72 // 4) % 8 * 4 + threadIdx_x % 2 * 2 + 1152 - blockIdx_x % 8 * 144 // 64 * 64:threadIdx_x // 72 * 192 + (blockIdx_x % 8 * 144 + threadIdx_x % 72 * 2) // 64 * 64 + threadIdx_x % 4 // 2 * 32 + (blockIdx_x % 8 * 2 + threadIdx_x % 72 // 4) % 8 * 4 + threadIdx_x % 2 * 2 + 1152 - blockIdx_x % 8 * 144 // 64 * 64 + 2] = B_1[threadIdx_x // 72 * 1152 + blockIdx_x % 8 * 144 + threadIdx_x % 72 * 2 + 6912:threadIdx_x // 72 * 1152 + blockIdx_x % 8 * 144 + threadIdx_x % 72 * 2 + 6912 + 2]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x % 3 * 320 + (blockIdx_x // 8 * 9 + threadIdx_x // 48) // 2 * 32 + threadIdx_x % 24 // 12 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x // 24) % 4 * 4 + threadIdx_x % 12 // 3 + 1920 - blockIdx_x // 8 * 144 // 32 * 32] = A_1[blockIdx_x // 8 * 165888 + threadIdx_x // 3 * 1152 + threadIdx_x % 3 * 2 + 12]
                A_shared_dyn_1[threadIdx_x % 3 * 320 + (blockIdx_x // 8 * 9 + threadIdx_x // 48) // 2 * 32 + threadIdx_x % 24 // 12 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x // 24) % 4 * 4 + threadIdx_x % 12 // 3 + 2080 - blockIdx_x // 8 * 144 // 32 * 32] = A_1[blockIdx_x // 8 * 165888 + threadIdx_x // 3 * 1152 + threadIdx_x % 3 * 2 + 13]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 72 * 192 + (blockIdx_x % 8 * 144 + threadIdx_x % 72 * 2) // 64 * 64 + threadIdx_x % 4 // 2 * 32 + (blockIdx_x % 8 * 2 + threadIdx_x % 72 // 4) % 8 * 4 + threadIdx_x % 2 * 2 + 2304 - blockIdx_x % 8 * 144 // 64 * 64:threadIdx_x // 72 * 192 + (blockIdx_x % 8 * 144 + threadIdx_x % 72 * 2) // 64 * 64 + threadIdx_x % 4 // 2 * 32 + (blockIdx_x % 8 * 2 + threadIdx_x % 72 // 4) % 8 * 4 + threadIdx_x % 2 * 2 + 2304 - blockIdx_x % 8 * 144 // 64 * 64 + 2] = B_1[threadIdx_x // 72 * 1152 + blockIdx_x % 8 * 144 + threadIdx_x % 72 * 2 + 13824:threadIdx_x // 72 * 1152 + blockIdx_x % 8 * 144 + threadIdx_x % 72 * 2 + 13824 + 2]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x % 3 * 320 + (blockIdx_x // 8 * 9 + threadIdx_x // 48) // 2 * 32 + threadIdx_x % 24 // 12 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x // 24) % 4 * 4 + threadIdx_x % 12 // 3 + 2880 - blockIdx_x // 8 * 144 // 32 * 32] = A_1[blockIdx_x // 8 * 165888 + threadIdx_x // 3 * 1152 + threadIdx_x % 3 * 2 + 18]
                A_shared_dyn_1[threadIdx_x % 3 * 320 + (blockIdx_x // 8 * 9 + threadIdx_x // 48) // 2 * 32 + threadIdx_x % 24 // 12 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x // 24) % 4 * 4 + threadIdx_x % 12 // 3 + 3040 - blockIdx_x // 8 * 144 // 32 * 32] = A_1[blockIdx_x // 8 * 165888 + threadIdx_x // 3 * 1152 + threadIdx_x % 3 * 2 + 19]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 72 * 192 + (blockIdx_x % 8 * 144 + threadIdx_x % 72 * 2) // 64 * 64 + threadIdx_x % 4 // 2 * 32 + (blockIdx_x % 8 * 2 + threadIdx_x % 72 // 4) % 8 * 4 + threadIdx_x % 2 * 2 + 3456 - blockIdx_x % 8 * 144 // 64 * 64:threadIdx_x // 72 * 192 + (blockIdx_x % 8 * 144 + threadIdx_x % 72 * 2) // 64 * 64 + threadIdx_x % 4 // 2 * 32 + (blockIdx_x % 8 * 2 + threadIdx_x % 72 // 4) % 8 * 4 + threadIdx_x % 2 * 2 + 3456 - blockIdx_x % 8 * 144 // 64 * 64 + 2] = B_1[threadIdx_x // 72 * 1152 + blockIdx_x % 8 * 144 + threadIdx_x % 72 * 2 + 20736:threadIdx_x // 72 * 1152 + blockIdx_x % 8 * 144 + threadIdx_x % 72 * 2 + 20736 + 2]
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 3)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 - blockIdx_x // 8 * 144 // 32 * 32:(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
            for ax1_0 in T.serial(3):
                cse_var_1: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_1:cse_var_1 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_1) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_1) // 8) % 8 * 4 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_1) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_1) // 8) % 8 * 4 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
        for k_0 in T.serial(188):
            cse_var_2: T.int32 = (k_0 + 4) % 5
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    A_shared_dyn_1[cse_var_2 * 960 + threadIdx_x % 3 * 320 + (blockIdx_x // 8 * 9 + threadIdx_x // 48) // 2 * 32 + threadIdx_x % 24 // 12 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x // 24) % 4 * 4 + threadIdx_x % 12 // 3 - blockIdx_x // 8 * 144 // 32 * 32] = A_1[blockIdx_x // 8 * 165888 + threadIdx_x // 3 * 1152 + k_0 * 6 + threadIdx_x % 3 * 2 + 24]
                    A_shared_dyn_1[cse_var_2 * 960 + threadIdx_x % 3 * 320 + (blockIdx_x // 8 * 9 + threadIdx_x // 48) // 2 * 32 + threadIdx_x % 24 // 12 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x // 24) % 4 * 4 + threadIdx_x % 12 // 3 + 160 - blockIdx_x // 8 * 144 // 32 * 32] = A_1[blockIdx_x // 8 * 165888 + threadIdx_x // 3 * 1152 + k_0 * 6 + threadIdx_x % 3 * 2 + 25]
                T.attr(0, "async_scope", 1)
                B_shared_dyn_1[cse_var_2 * 1152 + threadIdx_x // 72 * 192 + (blockIdx_x % 8 * 144 + threadIdx_x % 72 * 2) // 64 * 64 + threadIdx_x % 4 // 2 * 32 + (blockIdx_x % 8 * 2 + threadIdx_x % 72 // 4) % 8 * 4 + threadIdx_x % 2 * 2 - blockIdx_x % 8 * 144 // 64 * 64:cse_var_2 * 1152 + threadIdx_x // 72 * 192 + (blockIdx_x % 8 * 144 + threadIdx_x % 72 * 2) // 64 * 64 + threadIdx_x % 4 // 2 * 32 + (blockIdx_x % 8 * 2 + threadIdx_x % 72 // 4) % 8 * 4 + threadIdx_x % 2 * 2 - blockIdx_x % 8 * 144 // 64 * 64 + 2] = B_1[k_0 * 6912 + threadIdx_x // 72 * 1152 + blockIdx_x % 8 * 144 + threadIdx_x % 72 * 2 + 27648:k_0 * 6912 + threadIdx_x // 72 * 1152 + blockIdx_x % 8 * 144 + threadIdx_x % 72 * 2 + 27648 + 2]
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 3)
                A_shared_dyn_local_1[1] = A_shared_dyn_1[k_0 % 5 * 960 + (blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 160 - blockIdx_x // 8 * 144 // 32 * 32:k_0 % 5 * 960 + (blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 160 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
                for ax1_0 in T.serial(3):
                    cse_var_3: T.int32 = ax1_0 * 4
                    B_shared_dyn_local_1[cse_var_3 + 12:cse_var_3 + 12 + 4] = B_shared_dyn_1[k_0 % 5 * 1152 + (blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_3) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_3) // 8) % 8 * 4 + 192 - blockIdx_x % 8 * 144 // 64 * 64:k_0 % 5 * 1152 + (blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_3) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_3) // 8) % 8 * 4 + 192 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
                Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
                Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
                Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
                Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
                A_shared_dyn_local_1[0] = A_shared_dyn_1[k_0 % 5 * 960 + (blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 320 - blockIdx_x // 8 * 144 // 32 * 32:k_0 % 5 * 960 + (blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 320 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
                for ax1_0 in T.serial(3):
                    cse_var_4: T.int32 = ax1_0 * 4
                    B_shared_dyn_local_1[cse_var_4:cse_var_4 + 4] = B_shared_dyn_1[k_0 % 5 * 1152 + (blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_4) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_4) // 8) % 8 * 4 + 384 - blockIdx_x % 8 * 144 // 64 * 64:k_0 % 5 * 1152 + (blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_4) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_4) // 8) % 8 * 4 + 384 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
                Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
                Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
                Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
                Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
                Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[16], 4)
                Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[17], 4)
                Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[18], 4)
                Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[19], 4)
                Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[20], 4)
                Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[21], 4)
                Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[22], 4)
                Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[23], 4)
                A_shared_dyn_local_1[1] = A_shared_dyn_1[k_0 % 5 * 960 + (blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 480 - blockIdx_x // 8 * 144 // 32 * 32:k_0 % 5 * 960 + (blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 480 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
                for ax1_0 in T.serial(3):
                    cse_var_5: T.int32 = ax1_0 * 4
                    B_shared_dyn_local_1[cse_var_5 + 12:cse_var_5 + 12 + 4] = B_shared_dyn_1[k_0 % 5 * 1152 + (blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_5) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_5) // 8) % 8 * 4 + 576 - blockIdx_x % 8 * 144 // 64 * 64:k_0 % 5 * 1152 + (blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_5) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_5) // 8) % 8 * 4 + 576 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
                Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
                Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
                Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
                Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
                A_shared_dyn_local_1[0] = A_shared_dyn_1[k_0 % 5 * 960 + (blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 640 - blockIdx_x // 8 * 144 // 32 * 32:k_0 % 5 * 960 + (blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 640 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
                for ax1_0 in T.serial(3):
                    cse_var_6: T.int32 = ax1_0 * 4
                    B_shared_dyn_local_1[cse_var_6:cse_var_6 + 4] = B_shared_dyn_1[k_0 % 5 * 1152 + (blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_6) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_6) // 8) % 8 * 4 + 768 - blockIdx_x % 8 * 144 // 64 * 64:k_0 % 5 * 1152 + (blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_6) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_6) // 8) % 8 * 4 + 768 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
                Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
                Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
                Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
                Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
                Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[16], 4)
                Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[17], 4)
                Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[18], 4)
                Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[19], 4)
                Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[20], 4)
                Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[21], 4)
                Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[22], 4)
                Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[23], 4)
                A_shared_dyn_local_1[1] = A_shared_dyn_1[k_0 % 5 * 960 + (blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 800 - blockIdx_x // 8 * 144 // 32 * 32:k_0 % 5 * 960 + (blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 800 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
                for ax1_0 in T.serial(3):
                    cse_var_7: T.int32 = ax1_0 * 4
                    B_shared_dyn_local_1[cse_var_7 + 12:cse_var_7 + 12 + 4] = B_shared_dyn_1[k_0 % 5 * 1152 + (blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_7) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_7) // 8) % 8 * 4 + 960 - blockIdx_x % 8 * 144 // 64 * 64:k_0 % 5 * 1152 + (blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_7) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_7) // 8) % 8 * 4 + 960 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
                Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
                Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
                Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
                Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[(k_0 + 1) % 5 * 960 + (blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 - blockIdx_x // 8 * 144 // 32 * 32:(k_0 + 1) % 5 * 960 + (blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
            for ax1_0 in T.serial(3):
                cse_var_8: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_8:cse_var_8 + 4] = B_shared_dyn_1[(k_0 + 1) % 5 * 1152 + (blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_8) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_8) // 8) % 8 * 4 - blockIdx_x % 8 * 144 // 64 * 64:(k_0 + 1) % 5 * 1152 + (blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_8) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_8) // 8) % 8 * 4 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
            Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[16], 4)
            Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[17], 4)
            Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[18], 4)
            Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[19], 4)
            Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[20], 4)
            Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[21], 4)
            Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[22], 4)
            Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[23], 4)
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 2)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 3040 - blockIdx_x // 8 * 144 // 32 * 32:(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 3040 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
            for ax1_0 in T.serial(3):
                cse_var_9: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_9 + 12:cse_var_9 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_9) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_9) // 8) % 8 * 4 + 3648 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_9) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_9) // 8) % 8 * 4 + 3648 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
            Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 3200 - blockIdx_x // 8 * 144 // 32 * 32:(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 3200 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
            for ax1_0 in T.serial(3):
                cse_var_10: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_10:cse_var_10 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_10) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_10) // 8) % 8 * 4 + 3840 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_10) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_10) // 8) % 8 * 4 + 3840 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
            Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[16], 4)
            Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[17], 4)
            Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[18], 4)
            Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[19], 4)
            Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[20], 4)
            Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[21], 4)
            Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[22], 4)
            Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[23], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 3360 - blockIdx_x // 8 * 144 // 32 * 32:(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 3360 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
            for ax1_0 in T.serial(3):
                cse_var_11: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_11 + 12:cse_var_11 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_11) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_11) // 8) % 8 * 4 + 4032 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_11) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_11) // 8) % 8 * 4 + 4032 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
            Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 3520 - blockIdx_x // 8 * 144 // 32 * 32:(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 3520 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
            for ax1_0 in T.serial(3):
                cse_var_12: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_12:cse_var_12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_12) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_12) // 8) % 8 * 4 + 4224 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_12) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_12) // 8) % 8 * 4 + 4224 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
            Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[16], 4)
            Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[17], 4)
            Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[18], 4)
            Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[19], 4)
            Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[20], 4)
            Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[21], 4)
            Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[22], 4)
            Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[23], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 3680 - blockIdx_x // 8 * 144 // 32 * 32:(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 3680 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
            for ax1_0 in T.serial(3):
                cse_var_13: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_13 + 12:cse_var_13 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_13) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_13) // 8) % 8 * 4 + 4416 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_13) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_13) // 8) % 8 * 4 + 4416 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
            Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 3840 - blockIdx_x // 8 * 144 // 32 * 32:(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 3840 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
        for ax1_0 in T.serial(3):
            cse_var_14: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_14:cse_var_14 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_14) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_14) // 8) % 8 * 4 + 4608 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_14) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_14) // 8) % 8 * 4 + 4608 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
        Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[16], 4)
        Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[17], 4)
        Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[18], 4)
        Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[19], 4)
        Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[20], 4)
        Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[21], 4)
        Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[22], 4)
        Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[23], 4)
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 1)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 4000 - blockIdx_x // 8 * 144 // 32 * 32:(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 4000 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
            for ax1_0 in T.serial(3):
                cse_var_15: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_15 + 12:cse_var_15 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_15) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_15) // 8) % 8 * 4 + 4800 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_15) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_15) // 8) % 8 * 4 + 4800 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
            Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 4160 - blockIdx_x // 8 * 144 // 32 * 32:(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 4160 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
            for ax1_0 in T.serial(3):
                cse_var_16: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_16:cse_var_16 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_16) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_16) // 8) % 8 * 4 + 4992 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_16) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_16) // 8) % 8 * 4 + 4992 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
            Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[16], 4)
            Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[17], 4)
            Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[18], 4)
            Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[19], 4)
            Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[20], 4)
            Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[21], 4)
            Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[22], 4)
            Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[23], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 4320 - blockIdx_x // 8 * 144 // 32 * 32:(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 4320 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
            for ax1_0 in T.serial(3):
                cse_var_17: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_17 + 12:cse_var_17 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_17) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_17) // 8) % 8 * 4 + 5184 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_17) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_17) // 8) % 8 * 4 + 5184 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
            Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 4480 - blockIdx_x // 8 * 144 // 32 * 32:(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 4480 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
            for ax1_0 in T.serial(3):
                cse_var_18: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_18:cse_var_18 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_18) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_18) // 8) % 8 * 4 + 5376 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_18) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_18) // 8) % 8 * 4 + 5376 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
            Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[16], 4)
            Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[17], 4)
            Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[18], 4)
            Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[19], 4)
            Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[20], 4)
            Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[21], 4)
            Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[22], 4)
            Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[23], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 4640 - blockIdx_x // 8 * 144 // 32 * 32:(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 4640 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
            for ax1_0 in T.serial(3):
                cse_var_19: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_19 + 12:cse_var_19 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_19) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_19) // 8) % 8 * 4 + 5568 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_19) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_19) // 8) % 8 * 4 + 5568 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
            Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 - blockIdx_x // 8 * 144 // 32 * 32:(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
        for ax1_0 in T.serial(3):
            cse_var_20: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_20:cse_var_20 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_20) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_20) // 8) % 8 * 4 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_20) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_20) // 8) % 8 * 4 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
        Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[16], 4)
        Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[17], 4)
        Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[18], 4)
        Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[19], 4)
        Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[20], 4)
        Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[21], 4)
        Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[22], 4)
        Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[23], 4)
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 0)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 160 - blockIdx_x // 8 * 144 // 32 * 32:(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 160 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
            for ax1_0 in T.serial(3):
                cse_var_21: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_21 + 12:cse_var_21 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_21) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_21) // 8) % 8 * 4 + 192 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_21) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_21) // 8) % 8 * 4 + 192 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
            Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 320 - blockIdx_x // 8 * 144 // 32 * 32:(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 320 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
            for ax1_0 in T.serial(3):
                cse_var_22: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_22:cse_var_22 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_22) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_22) // 8) % 8 * 4 + 384 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_22) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_22) // 8) % 8 * 4 + 384 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
            Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[16], 4)
            Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[17], 4)
            Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[18], 4)
            Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[19], 4)
            Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[20], 4)
            Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[21], 4)
            Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[22], 4)
            Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[23], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 480 - blockIdx_x // 8 * 144 // 32 * 32:(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 480 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
            for ax1_0 in T.serial(3):
                cse_var_23: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_23 + 12:cse_var_23 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_23) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_23) // 8) % 8 * 4 + 576 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_23) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_23) // 8) % 8 * 4 + 576 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
            Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 640 - blockIdx_x // 8 * 144 // 32 * 32:(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 640 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
            for ax1_0 in T.serial(3):
                cse_var_24: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_24:cse_var_24 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_24) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_24) // 8) % 8 * 4 + 768 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_24) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_24) // 8) % 8 * 4 + 768 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
            Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[16], 4)
            Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[17], 4)
            Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[18], 4)
            Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[19], 4)
            Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[20], 4)
            Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[21], 4)
            Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[22], 4)
            Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[23], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 800 - blockIdx_x // 8 * 144 // 32 * 32:(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 800 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
            for ax1_0 in T.serial(3):
                cse_var_25: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_25 + 12:cse_var_25 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_25) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_25) // 8) % 8 * 4 + 960 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_25) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_25) // 8) % 8 * 4 + 960 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
            Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 960 - blockIdx_x // 8 * 144 // 32 * 32:(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 960 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
        for ax1_0 in T.serial(3):
            cse_var_26: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_26:cse_var_26 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_26) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_26) // 8) % 8 * 4 + 1152 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_26) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_26) // 8) % 8 * 4 + 1152 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
        Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[16], 4)
        Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[17], 4)
        Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[18], 4)
        Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[19], 4)
        Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[20], 4)
        Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[21], 4)
        Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[22], 4)
        Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[23], 4)
        A_shared_dyn_local_1[1] = A_shared_dyn_1[(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 1120 - blockIdx_x // 8 * 144 // 32 * 32:(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 1120 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
        for ax1_0 in T.serial(3):
            cse_var_27: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_27 + 12:cse_var_27 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_27) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_27) // 8) % 8 * 4 + 1344 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_27) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_27) // 8) % 8 * 4 + 1344 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
        Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 1280 - blockIdx_x // 8 * 144 // 32 * 32:(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 1280 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
        for ax1_0 in T.serial(3):
            cse_var_28: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_28:cse_var_28 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_28) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_28) // 8) % 8 * 4 + 1536 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_28) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_28) // 8) % 8 * 4 + 1536 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
        Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[16], 4)
        Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[17], 4)
        Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[18], 4)
        Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[19], 4)
        Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[20], 4)
        Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[21], 4)
        Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[22], 4)
        Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[23], 4)
        A_shared_dyn_local_1[1] = A_shared_dyn_1[(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 1440 - blockIdx_x // 8 * 144 // 32 * 32:(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 1440 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
        for ax1_0 in T.serial(3):
            cse_var_29: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_29 + 12:cse_var_29 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_29) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_29) // 8) % 8 * 4 + 1728 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_29) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_29) // 8) % 8 * 4 + 1728 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
        Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 1600 - blockIdx_x // 8 * 144 // 32 * 32:(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 1600 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
        for ax1_0 in T.serial(3):
            cse_var_30: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_30:cse_var_30 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_30) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_30) // 8) % 8 * 4 + 1920 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_30) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_30) // 8) % 8 * 4 + 1920 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
        Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[16], 4)
        Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[17], 4)
        Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[18], 4)
        Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[19], 4)
        Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[20], 4)
        Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[21], 4)
        Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[22], 4)
        Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[23], 4)
        A_shared_dyn_local_1[1] = A_shared_dyn_1[(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 1760 - blockIdx_x // 8 * 144 // 32 * 32:(blockIdx_x // 8 * 144 + threadIdx_x % 72 // 2 * 4) // 32 * 32 + threadIdx_x % 4 // 2 * 16 + (blockIdx_x // 8 * 2 + threadIdx_x % 72 // 4) % 4 * 4 + 1760 - blockIdx_x // 8 * 144 // 32 * 32 + 4]
        for ax1_0 in T.serial(3):
            cse_var_31: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_31 + 12:cse_var_31 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_31) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_31) // 8) % 8 * 4 + 2112 - blockIdx_x % 8 * 144 // 64 * 64:(blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + cse_var_31) // 64 * 64 + (ax1_0 + threadIdx_x % 2) % 2 * 32 + (blockIdx_x % 8 * 18 + threadIdx_x // 72 * 3 + (threadIdx_x % 2 * 12 + cse_var_31) // 8) % 8 * 4 + 2112 - blockIdx_x % 8 * 144 // 64 * 64 + 4]
        Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[0:48:12] = Y_local_1[0:48:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[1:49:12] = Y_local_1[1:49:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[2:50:12] = Y_local_1[2:50:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[3:51:12] = Y_local_1[3:51:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[4:52:12] = Y_local_1[4:52:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[16], 4)
        Y_local_1[5:53:12] = Y_local_1[5:53:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[17], 4)
        Y_local_1[6:54:12] = Y_local_1[6:54:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[18], 4)
        Y_local_1[7:55:12] = Y_local_1[7:55:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[19], 4)
        Y_local_1[8:56:12] = Y_local_1[8:56:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[20], 4)
        Y_local_1[9:57:12] = Y_local_1[9:57:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[21], 4)
        Y_local_1[10:58:12] = Y_local_1[10:58:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[22], 4)
        Y_local_1[11:59:12] = Y_local_1[11:59:12] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[23], 4)
        Y_1[blockIdx_x // 8 * 165888 + threadIdx_x % 72 // 2 * 4608 + blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12:blockIdx_x // 8 * 165888 + threadIdx_x % 72 // 2 * 4608 + blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + 4] = Y_local_1[0:4]
        Y_1[blockIdx_x // 8 * 165888 + threadIdx_x % 72 // 2 * 4608 + blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + 4:blockIdx_x // 8 * 165888 + threadIdx_x % 72 // 2 * 4608 + blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + 4 + 4] = Y_local_1[4:8]
        Y_1[blockIdx_x // 8 * 165888 + threadIdx_x % 72 // 2 * 4608 + blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + 8:blockIdx_x // 8 * 165888 + threadIdx_x % 72 // 2 * 4608 + blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + 8 + 4] = Y_local_1[8:12]
        Y_1[blockIdx_x // 8 * 165888 + threadIdx_x % 72 // 2 * 4608 + blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + 1152:blockIdx_x // 8 * 165888 + threadIdx_x % 72 // 2 * 4608 + blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + 1152 + 4] = Y_local_1[12:16]
        Y_1[blockIdx_x // 8 * 165888 + threadIdx_x % 72 // 2 * 4608 + blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + 1156:blockIdx_x // 8 * 165888 + threadIdx_x % 72 // 2 * 4608 + blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + 1156 + 4] = Y_local_1[16:20]
        Y_1[blockIdx_x // 8 * 165888 + threadIdx_x % 72 // 2 * 4608 + blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + 1160:blockIdx_x // 8 * 165888 + threadIdx_x % 72 // 2 * 4608 + blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + 1160 + 4] = Y_local_1[20:24]
        Y_1[blockIdx_x // 8 * 165888 + threadIdx_x % 72 // 2 * 4608 + blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + 2304:blockIdx_x // 8 * 165888 + threadIdx_x % 72 // 2 * 4608 + blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + 2304 + 4] = Y_local_1[24:28]
        Y_1[blockIdx_x // 8 * 165888 + threadIdx_x % 72 // 2 * 4608 + blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + 2308:blockIdx_x // 8 * 165888 + threadIdx_x % 72 // 2 * 4608 + blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + 2308 + 4] = Y_local_1[28:32]
        Y_1[blockIdx_x // 8 * 165888 + threadIdx_x % 72 // 2 * 4608 + blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + 2312:blockIdx_x // 8 * 165888 + threadIdx_x % 72 // 2 * 4608 + blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + 2312 + 4] = Y_local_1[32:36]
        Y_1[blockIdx_x // 8 * 165888 + threadIdx_x % 72 // 2 * 4608 + blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + 3456:blockIdx_x // 8 * 165888 + threadIdx_x % 72 // 2 * 4608 + blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + 3456 + 4] = Y_local_1[36:40]
        Y_1[blockIdx_x // 8 * 165888 + threadIdx_x % 72 // 2 * 4608 + blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + 3460:blockIdx_x // 8 * 165888 + threadIdx_x % 72 // 2 * 4608 + blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + 3460 + 4] = Y_local_1[40:44]
        Y_1[blockIdx_x // 8 * 165888 + threadIdx_x % 72 // 2 * 4608 + blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + 3464:blockIdx_x // 8 * 165888 + threadIdx_x % 72 // 2 * 4608 + blockIdx_x % 8 * 144 + threadIdx_x // 72 * 24 + threadIdx_x % 2 * 12 + 3464 + 4] = Y_local_1[44:48]
    

