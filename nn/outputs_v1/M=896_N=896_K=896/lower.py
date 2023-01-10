# from tvm.script import tir as T
@tvm.script.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer[(896, 896), "float32"], B: T.Buffer[(896, 896), "float32"], Y: T.Buffer[(896, 896), "float32"]):
        # function attr dict
        T.func_attr({"global_symbol": "main", "tir.noalias": True})
        # var definition
        threadIdx_x = T.env_thread("threadIdx.x")
        blockIdx_x = T.env_thread("blockIdx.x")
        # buffer definition
        A_1 = T.buffer_decl([802816], dtype="float32", data=A.data)
        B_1 = T.buffer_decl([802816], dtype="float32", data=B.data)
        Y_1 = T.buffer_decl([802816], dtype="float32", data=Y.data)
        # body
        T.launch_thread(blockIdx_x, 56)
        Y_local = T.allocate([64], "float32", "local")
        Y_local_1 = T.buffer_decl([64], dtype="float32", data=Y_local, scope="local")
        A_shared_dyn = T.allocate([1280], "float32", "shared.dyn")
        A_shared_dyn_1 = T.buffer_decl([1280], dtype="float32", data=A_shared_dyn, scope="shared.dyn")
        B_shared_dyn = T.allocate([5120], "float32", "shared.dyn")
        B_shared_dyn_1 = T.buffer_decl([5120], dtype="float32", data=B_shared_dyn, scope="shared.dyn")
        A_shared_dyn_local = T.allocate([4], "float32x4", "local")
        A_shared_dyn_local_1 = T.buffer_decl([4], dtype="float32x4", data=A_shared_dyn_local, scope="local")
        B_shared_dyn_local = T.allocate([16], "float32", "local")
        B_shared_dyn_local_1 = T.buffer_decl([16], dtype="float32", data=B_shared_dyn_local, scope="local")
        T.launch_thread(threadIdx_x, 224)
        Y_local_1[0] = T.float32(0)
        Y_local_1[8] = T.float32(0)
        Y_local_1[16] = T.float32(0)
        Y_local_1[24] = T.float32(0)
        Y_local_1[32] = T.float32(0)
        Y_local_1[40] = T.float32(0)
        Y_local_1[48] = T.float32(0)
        Y_local_1[56] = T.float32(0)
        Y_local_1[1] = T.float32(0)
        Y_local_1[9] = T.float32(0)
        Y_local_1[17] = T.float32(0)
        Y_local_1[25] = T.float32(0)
        Y_local_1[33] = T.float32(0)
        Y_local_1[41] = T.float32(0)
        Y_local_1[49] = T.float32(0)
        Y_local_1[57] = T.float32(0)
        Y_local_1[2] = T.float32(0)
        Y_local_1[10] = T.float32(0)
        Y_local_1[18] = T.float32(0)
        Y_local_1[26] = T.float32(0)
        Y_local_1[34] = T.float32(0)
        Y_local_1[42] = T.float32(0)
        Y_local_1[50] = T.float32(0)
        Y_local_1[58] = T.float32(0)
        Y_local_1[3] = T.float32(0)
        Y_local_1[11] = T.float32(0)
        Y_local_1[19] = T.float32(0)
        Y_local_1[27] = T.float32(0)
        Y_local_1[35] = T.float32(0)
        Y_local_1[43] = T.float32(0)
        Y_local_1[51] = T.float32(0)
        Y_local_1[59] = T.float32(0)
        Y_local_1[4] = T.float32(0)
        Y_local_1[12] = T.float32(0)
        Y_local_1[20] = T.float32(0)
        Y_local_1[28] = T.float32(0)
        Y_local_1[36] = T.float32(0)
        Y_local_1[44] = T.float32(0)
        Y_local_1[52] = T.float32(0)
        Y_local_1[60] = T.float32(0)
        Y_local_1[5] = T.float32(0)
        Y_local_1[13] = T.float32(0)
        Y_local_1[21] = T.float32(0)
        Y_local_1[29] = T.float32(0)
        Y_local_1[37] = T.float32(0)
        Y_local_1[45] = T.float32(0)
        Y_local_1[53] = T.float32(0)
        Y_local_1[61] = T.float32(0)
        Y_local_1[6] = T.float32(0)
        Y_local_1[14] = T.float32(0)
        Y_local_1[22] = T.float32(0)
        Y_local_1[30] = T.float32(0)
        Y_local_1[38] = T.float32(0)
        Y_local_1[46] = T.float32(0)
        Y_local_1[54] = T.float32(0)
        Y_local_1[62] = T.float32(0)
        Y_local_1[7] = T.float32(0)
        Y_local_1[15] = T.float32(0)
        Y_local_1[23] = T.float32(0)
        Y_local_1[31] = T.float32(0)
        Y_local_1[39] = T.float32(0)
        Y_local_1[47] = T.float32(0)
        Y_local_1[55] = T.float32(0)
        Y_local_1[63] = T.float32(0)
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                if threadIdx_x < 128:
                    A_shared_dyn_1[threadIdx_x % 2 * 128 + threadIdx_x // 64 * 32 + (threadIdx_x // 28 * 3 + threadIdx_x % 28 // 4) % 4 // 2 * 16 + threadIdx_x % 64 // 16 * 4 + (threadIdx_x // 28 * 2 + threadIdx_x % 28 // 2) % 4] = A_1[blockIdx_x // 4 * 57344 + threadIdx_x // 2 * 896 + threadIdx_x % 2 * 2]
                if threadIdx_x < 128:
                    A_shared_dyn_1[threadIdx_x % 2 * 128 + threadIdx_x // 64 * 32 + (threadIdx_x // 28 * 3 + threadIdx_x % 28 // 4) % 4 // 2 * 16 + threadIdx_x % 64 // 16 * 4 + (threadIdx_x // 28 * 2 + threadIdx_x % 28 // 2) % 4 + 64] = A_1[blockIdx_x // 4 * 57344 + threadIdx_x // 2 * 896 + threadIdx_x % 2 * 2 + 1]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 56 * 256 + (blockIdx_x % 4 * 224 + threadIdx_x % 56 * 4) // 64 * 64 + threadIdx_x % 2 * 32 + (blockIdx_x % 4 * 4 + threadIdx_x % 56 // 2) % 8 * 4 - blockIdx_x % 4 * 224 // 64 * 64:threadIdx_x // 56 * 256 + (blockIdx_x % 4 * 224 + threadIdx_x % 56 * 4) // 64 * 64 + threadIdx_x % 2 * 32 + (blockIdx_x % 4 * 4 + threadIdx_x % 56 // 2) % 8 * 4 - blockIdx_x % 4 * 224 // 64 * 64 + 4] = B_1[threadIdx_x // 56 * 896 + blockIdx_x % 4 * 224 + threadIdx_x % 56 * 4:threadIdx_x // 56 * 896 + blockIdx_x % 4 * 224 + threadIdx_x % 56 * 4 + 4]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                if threadIdx_x < 128:
                    A_shared_dyn_1[threadIdx_x % 2 * 128 + threadIdx_x // 64 * 32 + (threadIdx_x // 28 * 3 + threadIdx_x % 28 // 4) % 4 // 2 * 16 + threadIdx_x % 64 // 16 * 4 + (threadIdx_x // 28 * 2 + threadIdx_x % 28 // 2) % 4 + 256] = A_1[blockIdx_x // 4 * 57344 + threadIdx_x // 2 * 896 + threadIdx_x % 2 * 2 + 4]
                if threadIdx_x < 128:
                    A_shared_dyn_1[threadIdx_x % 2 * 128 + threadIdx_x // 64 * 32 + (threadIdx_x // 28 * 3 + threadIdx_x % 28 // 4) % 4 // 2 * 16 + threadIdx_x % 64 // 16 * 4 + (threadIdx_x // 28 * 2 + threadIdx_x % 28 // 2) % 4 + 320] = A_1[blockIdx_x // 4 * 57344 + threadIdx_x // 2 * 896 + threadIdx_x % 2 * 2 + 5]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 56 * 256 + (blockIdx_x % 4 * 224 + threadIdx_x % 56 * 4) // 64 * 64 + threadIdx_x % 2 * 32 + (blockIdx_x % 4 * 4 + threadIdx_x % 56 // 2) % 8 * 4 + 1024 - blockIdx_x % 4 * 224 // 64 * 64:threadIdx_x // 56 * 256 + (blockIdx_x % 4 * 224 + threadIdx_x % 56 * 4) // 64 * 64 + threadIdx_x % 2 * 32 + (blockIdx_x % 4 * 4 + threadIdx_x % 56 // 2) % 8 * 4 + 1024 - blockIdx_x % 4 * 224 // 64 * 64 + 4] = B_1[threadIdx_x // 56 * 896 + blockIdx_x % 4 * 224 + threadIdx_x % 56 * 4 + 3584:threadIdx_x // 56 * 896 + blockIdx_x % 4 * 224 + threadIdx_x % 56 * 4 + 3584 + 4]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                if threadIdx_x < 128:
                    A_shared_dyn_1[threadIdx_x % 2 * 128 + threadIdx_x // 64 * 32 + (threadIdx_x // 28 * 3 + threadIdx_x % 28 // 4) % 4 // 2 * 16 + threadIdx_x % 64 // 16 * 4 + (threadIdx_x // 28 * 2 + threadIdx_x % 28 // 2) % 4 + 512] = A_1[blockIdx_x // 4 * 57344 + threadIdx_x // 2 * 896 + threadIdx_x % 2 * 2 + 8]
                if threadIdx_x < 128:
                    A_shared_dyn_1[threadIdx_x % 2 * 128 + threadIdx_x // 64 * 32 + (threadIdx_x // 28 * 3 + threadIdx_x % 28 // 4) % 4 // 2 * 16 + threadIdx_x % 64 // 16 * 4 + (threadIdx_x // 28 * 2 + threadIdx_x % 28 // 2) % 4 + 576] = A_1[blockIdx_x // 4 * 57344 + threadIdx_x // 2 * 896 + threadIdx_x % 2 * 2 + 9]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 56 * 256 + (blockIdx_x % 4 * 224 + threadIdx_x % 56 * 4) // 64 * 64 + threadIdx_x % 2 * 32 + (blockIdx_x % 4 * 4 + threadIdx_x % 56 // 2) % 8 * 4 + 2048 - blockIdx_x % 4 * 224 // 64 * 64:threadIdx_x // 56 * 256 + (blockIdx_x % 4 * 224 + threadIdx_x % 56 * 4) // 64 * 64 + threadIdx_x % 2 * 32 + (blockIdx_x % 4 * 4 + threadIdx_x % 56 // 2) % 8 * 4 + 2048 - blockIdx_x % 4 * 224 // 64 * 64 + 4] = B_1[threadIdx_x // 56 * 896 + blockIdx_x % 4 * 224 + threadIdx_x % 56 * 4 + 7168:threadIdx_x // 56 * 896 + blockIdx_x % 4 * 224 + threadIdx_x % 56 * 4 + 7168 + 4]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                if threadIdx_x < 128:
                    A_shared_dyn_1[threadIdx_x % 2 * 128 + threadIdx_x // 64 * 32 + (threadIdx_x // 28 * 3 + threadIdx_x % 28 // 4) % 4 // 2 * 16 + threadIdx_x % 64 // 16 * 4 + (threadIdx_x // 28 * 2 + threadIdx_x % 28 // 2) % 4 + 768] = A_1[blockIdx_x // 4 * 57344 + threadIdx_x // 2 * 896 + threadIdx_x % 2 * 2 + 12]
                if threadIdx_x < 128:
                    A_shared_dyn_1[threadIdx_x % 2 * 128 + threadIdx_x // 64 * 32 + (threadIdx_x // 28 * 3 + threadIdx_x % 28 // 4) % 4 // 2 * 16 + threadIdx_x % 64 // 16 * 4 + (threadIdx_x // 28 * 2 + threadIdx_x % 28 // 2) % 4 + 832] = A_1[blockIdx_x // 4 * 57344 + threadIdx_x // 2 * 896 + threadIdx_x % 2 * 2 + 13]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 56 * 256 + (blockIdx_x % 4 * 224 + threadIdx_x % 56 * 4) // 64 * 64 + threadIdx_x % 2 * 32 + (blockIdx_x % 4 * 4 + threadIdx_x % 56 // 2) % 8 * 4 + 3072 - blockIdx_x % 4 * 224 // 64 * 64:threadIdx_x // 56 * 256 + (blockIdx_x % 4 * 224 + threadIdx_x % 56 * 4) // 64 * 64 + threadIdx_x % 2 * 32 + (blockIdx_x % 4 * 4 + threadIdx_x % 56 // 2) % 8 * 4 + 3072 - blockIdx_x % 4 * 224 // 64 * 64 + 4] = B_1[threadIdx_x // 56 * 896 + blockIdx_x % 4 * 224 + threadIdx_x % 56 * 4 + 10752:threadIdx_x // 56 * 896 + blockIdx_x % 4 * 224 + threadIdx_x % 56 * 4 + 10752 + 4]
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 3)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4:threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 4]
            for ax1_0 in T.serial(2):
                cse_var_1: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_1:cse_var_1 + 4] = B_shared_dyn_1[(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_1) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 - blockIdx_x % 4 * 224 // 64 * 64:(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_1) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 - blockIdx_x % 4 * 224 // 64 * 64 + 4]
        for k_0 in T.serial(220):
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    if threadIdx_x < 128:
                        A_shared_dyn_1[(k_0 + 4) % 5 * 256 + threadIdx_x % 2 * 128 + threadIdx_x // 64 * 32 + (threadIdx_x // 28 * 3 + threadIdx_x % 28 // 4) % 4 // 2 * 16 + threadIdx_x % 64 // 16 * 4 + (threadIdx_x // 28 * 2 + threadIdx_x % 28 // 2) % 4] = A_1[blockIdx_x // 4 * 57344 + threadIdx_x // 2 * 896 + k_0 * 4 + threadIdx_x % 2 * 2 + 16]
                    if threadIdx_x < 128:
                        A_shared_dyn_1[(k_0 + 4) % 5 * 256 + threadIdx_x % 2 * 128 + threadIdx_x // 64 * 32 + (threadIdx_x // 28 * 3 + threadIdx_x % 28 // 4) % 4 // 2 * 16 + threadIdx_x % 64 // 16 * 4 + (threadIdx_x // 28 * 2 + threadIdx_x % 28 // 2) % 4 + 64] = A_1[blockIdx_x // 4 * 57344 + threadIdx_x // 2 * 896 + k_0 * 4 + threadIdx_x % 2 * 2 + 17]
                T.attr(0, "async_scope", 1)
                B_shared_dyn_1[(k_0 + 4) % 5 * 1024 + threadIdx_x // 56 * 256 + (blockIdx_x % 4 * 224 + threadIdx_x % 56 * 4) // 64 * 64 + threadIdx_x % 2 * 32 + (blockIdx_x % 4 * 4 + threadIdx_x % 56 // 2) % 8 * 4 - blockIdx_x % 4 * 224 // 64 * 64:(k_0 + 4) % 5 * 1024 + threadIdx_x // 56 * 256 + (blockIdx_x % 4 * 224 + threadIdx_x % 56 * 4) // 64 * 64 + threadIdx_x % 2 * 32 + (blockIdx_x % 4 * 4 + threadIdx_x % 56 // 2) % 8 * 4 - blockIdx_x % 4 * 224 // 64 * 64 + 4] = B_1[k_0 * 3584 + threadIdx_x // 56 * 896 + blockIdx_x % 4 * 224 + threadIdx_x % 56 * 4 + 14336:k_0 * 3584 + threadIdx_x // 56 * 896 + blockIdx_x % 4 * 224 + threadIdx_x % 56 * 4 + 14336 + 4]
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 3)
                for ax0_0 in T.serial(2):
                    A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[k_0 % 5 * 256 + threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 64:k_0 % 5 * 256 + threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 64 + 4]
                for ax1_0 in T.serial(2):
                    cse_var_2: T.int32 = ax1_0 * 4
                    B_shared_dyn_local_1[cse_var_2 + 8:cse_var_2 + 8 + 4] = B_shared_dyn_1[k_0 % 5 * 1024 + (blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_2) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 256 - blockIdx_x % 4 * 224 // 64 * 64:k_0 % 5 * 1024 + (blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_2) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 256 - blockIdx_x % 4 * 224 // 64 * 64 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
                for ax0_0 in T.serial(2):
                    A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[k_0 % 5 * 256 + threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 128:k_0 % 5 * 256 + threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 128 + 4]
                for ax1_0 in T.serial(2):
                    cse_var_3: T.int32 = ax1_0 * 4
                    B_shared_dyn_local_1[cse_var_3:cse_var_3 + 4] = B_shared_dyn_1[k_0 % 5 * 1024 + (blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_3) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 512 - blockIdx_x % 4 * 224 // 64 * 64:k_0 % 5 * 1024 + (blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_3) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 512 - blockIdx_x % 4 * 224 // 64 * 64 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[8], 4)
                Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[8], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[9], 4)
                Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[9], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[10], 4)
                Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[10], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[11], 4)
                Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[11], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[12], 4)
                Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[13], 4)
                Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[14], 4)
                Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[15], 4)
                Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
                for ax0_0 in T.serial(2):
                    A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[k_0 % 5 * 256 + threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 192:k_0 % 5 * 256 + threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 192 + 4]
                for ax1_0 in T.serial(2):
                    cse_var_4: T.int32 = ax1_0 * 4
                    B_shared_dyn_local_1[cse_var_4 + 8:cse_var_4 + 8 + 4] = B_shared_dyn_1[k_0 % 5 * 1024 + (blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_4) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 768 - blockIdx_x % 4 * 224 // 64 * 64:k_0 % 5 * 1024 + (blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_4) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 768 - blockIdx_x % 4 * 224 // 64 * 64 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[(k_0 + 1) % 5 * 256 + threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4:(k_0 + 1) % 5 * 256 + threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 4]
            for ax1_0 in T.serial(2):
                cse_var_5: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_5:cse_var_5 + 4] = B_shared_dyn_1[(k_0 + 1) % 5 * 1024 + (blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_5) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 - blockIdx_x % 4 * 224 // 64 * 64:(k_0 + 1) % 5 * 1024 + (blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_5) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 - blockIdx_x % 4 * 224 // 64 * 64 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[15], 4)
            Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 2)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 64:threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 64 + 4]
            for ax1_0 in T.serial(2):
                cse_var_6: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_6 + 8:cse_var_6 + 8 + 4] = B_shared_dyn_1[(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_6) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 256 - blockIdx_x % 4 * 224 // 64 * 64:(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_6) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 256 - blockIdx_x % 4 * 224 // 64 * 64 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 128:threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 128 + 4]
            for ax1_0 in T.serial(2):
                cse_var_7: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_7:cse_var_7 + 4] = B_shared_dyn_1[(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_7) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 512 - blockIdx_x % 4 * 224 // 64 * 64:(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_7) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 512 - blockIdx_x % 4 * 224 // 64 * 64 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[15], 4)
            Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 192:threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 192 + 4]
            for ax1_0 in T.serial(2):
                cse_var_8: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_8 + 8:cse_var_8 + 8 + 4] = B_shared_dyn_1[(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_8) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 768 - blockIdx_x % 4 * 224 // 64 * 64:(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_8) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 768 - blockIdx_x % 4 * 224 // 64 * 64 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
        for ax0_0 in T.serial(2):
            A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 256:threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 256 + 4]
        for ax1_0 in T.serial(2):
            cse_var_9: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_9:cse_var_9 + 4] = B_shared_dyn_1[(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_9) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 1024 - blockIdx_x % 4 * 224 // 64 * 64:(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_9) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 1024 - blockIdx_x % 4 * 224 // 64 * 64 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 1)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 320:threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 320 + 4]
            for ax1_0 in T.serial(2):
                cse_var_10: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_10 + 8:cse_var_10 + 8 + 4] = B_shared_dyn_1[(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_10) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 1280 - blockIdx_x % 4 * 224 // 64 * 64:(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_10) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 1280 - blockIdx_x % 4 * 224 // 64 * 64 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 384:threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 384 + 4]
            for ax1_0 in T.serial(2):
                cse_var_11: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_11:cse_var_11 + 4] = B_shared_dyn_1[(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_11) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 1536 - blockIdx_x % 4 * 224 // 64 * 64:(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_11) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 1536 - blockIdx_x % 4 * 224 // 64 * 64 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[15], 4)
            Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 448:threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 448 + 4]
            for ax1_0 in T.serial(2):
                cse_var_12: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_12 + 8:cse_var_12 + 8 + 4] = B_shared_dyn_1[(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_12) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 1792 - blockIdx_x % 4 * 224 // 64 * 64:(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_12) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 1792 - blockIdx_x % 4 * 224 // 64 * 64 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
        for ax0_0 in T.serial(2):
            A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 512:threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 512 + 4]
        for ax1_0 in T.serial(2):
            cse_var_13: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_13:cse_var_13 + 4] = B_shared_dyn_1[(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_13) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 2048 - blockIdx_x % 4 * 224 // 64 * 64:(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_13) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 2048 - blockIdx_x % 4 * 224 // 64 * 64 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 0)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 576:threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 576 + 4]
            for ax1_0 in T.serial(2):
                cse_var_14: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_14 + 8:cse_var_14 + 8 + 4] = B_shared_dyn_1[(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_14) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 2304 - blockIdx_x % 4 * 224 // 64 * 64:(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_14) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 2304 - blockIdx_x % 4 * 224 // 64 * 64 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 640:threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 640 + 4]
            for ax1_0 in T.serial(2):
                cse_var_15: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_15:cse_var_15 + 4] = B_shared_dyn_1[(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_15) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 2560 - blockIdx_x % 4 * 224 // 64 * 64:(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_15) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 2560 - blockIdx_x % 4 * 224 // 64 * 64 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[15], 4)
            Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 704:threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 704 + 4]
            for ax1_0 in T.serial(2):
                cse_var_16: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_16 + 8:cse_var_16 + 8 + 4] = B_shared_dyn_1[(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_16) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 2816 - blockIdx_x % 4 * 224 // 64 * 64:(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_16) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 2816 - blockIdx_x % 4 * 224 // 64 * 64 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
        for ax0_0 in T.serial(2):
            A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 768:threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 768 + 4]
        for ax1_0 in T.serial(2):
            cse_var_17: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_17:cse_var_17 + 4] = B_shared_dyn_1[(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_17) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 3072 - blockIdx_x % 4 * 224 // 64 * 64:(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_17) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 3072 - blockIdx_x % 4 * 224 // 64 * 64 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
        for ax0_0 in T.serial(2):
            A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 832:threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 832 + 4]
        for ax1_0 in T.serial(2):
            cse_var_18: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_18 + 8:cse_var_18 + 8 + 4] = B_shared_dyn_1[(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_18) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 3328 - blockIdx_x % 4 * 224 // 64 * 64:(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_18) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 3328 - blockIdx_x % 4 * 224 // 64 * 64 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
        for ax0_0 in T.serial(2):
            A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 896:threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 896 + 4]
        for ax1_0 in T.serial(2):
            cse_var_19: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_19:cse_var_19 + 4] = B_shared_dyn_1[(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_19) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 3584 - blockIdx_x % 4 * 224 // 64 * 64:(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_19) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 3584 - blockIdx_x % 4 * 224 // 64 * 64 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
        for ax0_0 in T.serial(2):
            A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 960:threadIdx_x % 16 // 8 * 32 + ax0_0 * 16 + threadIdx_x % 8 // 2 * 4 + 960 + 4]
        for ax1_0 in T.serial(2):
            cse_var_20: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_20 + 8:cse_var_20 + 8 + 4] = B_shared_dyn_1[(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_20) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 3840 - blockIdx_x % 4 * 224 // 64 * 64:(blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + cse_var_20) // 64 * 64 + ax1_0 * 32 + (blockIdx_x % 4 * 28 + threadIdx_x // 16 * 2 + threadIdx_x % 2) % 8 * 4 + 3840 - blockIdx_x % 4 * 224 // 64 * 64 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[32:64:8] = Y_local_1[32:64:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[33:65:8] = Y_local_1[33:65:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[34:66:8] = Y_local_1[34:66:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[35:67:8] = Y_local_1[35:67:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[36:68:8] = Y_local_1[36:68:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[37:69:8] = Y_local_1[37:69:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[38:70:8] = Y_local_1[38:70:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[39:71:8] = Y_local_1[39:71:8] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_1[blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8:blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 4] = Y_local_1[0:4]
        Y_1[blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 4:blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 4 + 4] = Y_local_1[4:8]
        Y_1[blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 896:blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 896 + 4] = Y_local_1[8:12]
        Y_1[blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 900:blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 900 + 4] = Y_local_1[12:16]
        Y_1[blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 1792:blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 1792 + 4] = Y_local_1[16:20]
        Y_1[blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 1796:blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 1796 + 4] = Y_local_1[20:24]
        Y_1[blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 2688:blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 2688 + 4] = Y_local_1[24:28]
        Y_1[blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 2692:blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 2692 + 4] = Y_local_1[28:32]
        Y_1[blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 3584:blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 3584 + 4] = Y_local_1[32:36]
        Y_1[blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 3588:blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 3588 + 4] = Y_local_1[36:40]
        Y_1[blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 4480:blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 4480 + 4] = Y_local_1[40:44]
        Y_1[blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 4484:blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 4484 + 4] = Y_local_1[44:48]
        Y_1[blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 5376:blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 5376 + 4] = Y_local_1[48:52]
        Y_1[blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 5380:blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 5380 + 4] = Y_local_1[52:56]
        Y_1[blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 6272:blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 6272 + 4] = Y_local_1[56:60]
        Y_1[blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 6276:blockIdx_x // 4 * 57344 + threadIdx_x % 16 // 2 * 7168 + blockIdx_x % 4 * 224 + threadIdx_x // 16 * 16 + threadIdx_x % 2 * 8 + 6276 + 4] = Y_local_1[60:64]
    

