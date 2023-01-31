# from tvm.script import tir as T
@tvm.script.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer[(8192, 8192), "float32"], B: T.Buffer[(8192, 8192), "float32"], Y: T.Buffer[(8192, 8192), "float32"]):
        # function attr dict
        T.func_attr({"global_symbol": "main", "tir.noalias": True})
        # var definition
        threadIdx_x = T.env_thread("threadIdx.x")
        blockIdx_x = T.env_thread("blockIdx.x")
        # buffer definition
        A_1 = T.buffer_decl([67108864], dtype="float32", data=A.data)
        B_1 = T.buffer_decl([67108864], dtype="float32", data=B.data)
        Y_1 = T.buffer_decl([67108864], dtype="float32", data=Y.data)
        # body
        T.launch_thread(blockIdx_x, 2048)
        Y_local = T.allocate([64], "float32", "local")
        Y_local_1 = T.buffer_decl([64], dtype="float32", data=Y_local, scope="local")
        A_shared_dyn = T.allocate([2560], "float32", "shared.dyn")
        A_shared_dyn_1 = T.buffer_decl([2560], dtype="float32", data=A_shared_dyn, scope="shared.dyn")
        B_shared_dyn = T.allocate([5120], "float32", "shared.dyn")
        B_shared_dyn_1 = T.buffer_decl([5120], dtype="float32", data=B_shared_dyn, scope="shared.dyn")
        A_shared_dyn_local = T.allocate([4], "float32x4", "local")
        A_shared_dyn_local_1 = T.buffer_decl([4], dtype="float32x4", data=A_shared_dyn_local, scope="local")
        B_shared_dyn_local = T.allocate([16], "float32", "local")
        B_shared_dyn_local_1 = T.buffer_decl([16], dtype="float32", data=B_shared_dyn_local, scope="local")
        T.launch_thread(threadIdx_x, 512)
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
                A_shared_dyn_1[threadIdx_x % 4 * 128 + threadIdx_x // 128 * 32 + threadIdx_x % 32 // 16 * 16 + threadIdx_x % 128 // 32 * 4 + threadIdx_x % 16 // 4] = A_1[blockIdx_x // 32 * 1048576 + threadIdx_x // 4 * 8192 + threadIdx_x % 4]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 32 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 32 // 4 * 4 + threadIdx_x % 2 * 2:threadIdx_x // 32 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 32 // 4 * 4 + threadIdx_x % 2 * 2 + 2] = B_1[threadIdx_x // 128 * 8192 + blockIdx_x % 32 * 256 + threadIdx_x % 128 * 2:threadIdx_x // 128 * 8192 + blockIdx_x % 32 * 256 + threadIdx_x % 128 * 2 + 2]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x % 4 * 128 + threadIdx_x // 128 * 32 + threadIdx_x % 32 // 16 * 16 + threadIdx_x % 128 // 32 * 4 + threadIdx_x % 16 // 4 + 512] = A_1[blockIdx_x // 32 * 1048576 + threadIdx_x // 4 * 8192 + threadIdx_x % 4 + 4]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 32 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 32 // 4 * 4 + threadIdx_x % 2 * 2 + 1024:threadIdx_x // 32 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 32 // 4 * 4 + threadIdx_x % 2 * 2 + 1024 + 2] = B_1[threadIdx_x // 128 * 8192 + blockIdx_x % 32 * 256 + threadIdx_x % 128 * 2 + 32768:threadIdx_x // 128 * 8192 + blockIdx_x % 32 * 256 + threadIdx_x % 128 * 2 + 32768 + 2]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x % 4 * 128 + threadIdx_x // 128 * 32 + threadIdx_x % 32 // 16 * 16 + threadIdx_x % 128 // 32 * 4 + threadIdx_x % 16 // 4 + 1024] = A_1[blockIdx_x // 32 * 1048576 + threadIdx_x // 4 * 8192 + threadIdx_x % 4 + 8]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 32 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 32 // 4 * 4 + threadIdx_x % 2 * 2 + 2048:threadIdx_x // 32 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 32 // 4 * 4 + threadIdx_x % 2 * 2 + 2048 + 2] = B_1[threadIdx_x // 128 * 8192 + blockIdx_x % 32 * 256 + threadIdx_x % 128 * 2 + 65536:threadIdx_x // 128 * 8192 + blockIdx_x % 32 * 256 + threadIdx_x % 128 * 2 + 65536 + 2]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x % 4 * 128 + threadIdx_x // 128 * 32 + threadIdx_x % 32 // 16 * 16 + threadIdx_x % 128 // 32 * 4 + threadIdx_x % 16 // 4 + 1536] = A_1[blockIdx_x // 32 * 1048576 + threadIdx_x // 4 * 8192 + threadIdx_x % 4 + 12]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 32 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 32 // 4 * 4 + threadIdx_x % 2 * 2 + 3072:threadIdx_x // 32 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 32 // 4 * 4 + threadIdx_x % 2 * 2 + 3072 + 2] = B_1[threadIdx_x // 128 * 8192 + blockIdx_x % 32 * 256 + threadIdx_x % 128 * 2 + 98304:threadIdx_x // 128 * 8192 + blockIdx_x % 32 * 256 + threadIdx_x % 128 * 2 + 98304 + 2]
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 3)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4:threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4]
        for k_0 in T.serial(2044):
            cse_var_1: T.int32 = (k_0 + 4) % 5
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    A_shared_dyn_1[cse_var_1 * 512 + threadIdx_x % 4 * 128 + threadIdx_x // 128 * 32 + threadIdx_x % 32 // 16 * 16 + threadIdx_x % 128 // 32 * 4 + threadIdx_x % 16 // 4] = A_1[blockIdx_x // 32 * 1048576 + threadIdx_x // 4 * 8192 + k_0 * 4 + threadIdx_x % 4 + 16]
                T.attr(0, "async_scope", 1)
                B_shared_dyn_1[cse_var_1 * 1024 + threadIdx_x // 32 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 32 // 4 * 4 + threadIdx_x % 2 * 2:cse_var_1 * 1024 + threadIdx_x // 32 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 32 // 4 * 4 + threadIdx_x % 2 * 2 + 2] = B_1[k_0 * 32768 + threadIdx_x // 128 * 8192 + blockIdx_x % 32 * 256 + threadIdx_x % 128 * 2 + 131072:k_0 * 32768 + threadIdx_x // 128 * 8192 + blockIdx_x % 32 * 256 + threadIdx_x % 128 * 2 + 131072 + 2]
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 3)
                for ax0_0 in T.serial(2):
                    A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[k_0 % 5 * 512 + threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 128:k_0 % 5 * 512 + threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 128 + 4]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[k_0 % 5 * 1024 + threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 256:k_0 % 5 * 1024 + threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 256 + 4]
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
                    A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[k_0 % 5 * 512 + threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 256:k_0 % 5 * 512 + threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 256 + 4]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[k_0 % 5 * 1024 + threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 512:k_0 % 5 * 1024 + threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 512 + 4]
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
                    A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[k_0 % 5 * 512 + threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 384:k_0 % 5 * 512 + threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 384 + 4]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[k_0 % 5 * 1024 + threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 768:k_0 % 5 * 1024 + threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 768 + 4]
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
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[(k_0 + 1) % 5 * 512 + threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4:(k_0 + 1) % 5 * 512 + threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[(k_0 + 1) % 5 * 1024 + threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4:(k_0 + 1) % 5 * 1024 + threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4]
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
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 2176:threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 2176 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4352:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4352 + 4]
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
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 2304:threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 2304 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4608:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4608 + 4]
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
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 2432:threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 2432 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4864:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4864 + 4]
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
            A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4:threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 4]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4]
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
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 128:threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 128 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 256:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 256 + 4]
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
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 256:threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 256 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 512:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 512 + 4]
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
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 384:threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 384 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 768:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 768 + 4]
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
            A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 512:threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 512 + 4]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1024:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1024 + 4]
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
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 640:threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 640 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1280:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1280 + 4]
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
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 768:threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 768 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1536:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1536 + 4]
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
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 896:threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 896 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1792:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1792 + 4]
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
            A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 1024:threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 1024 + 4]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2048:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2048 + 4]
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
            A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 1152:threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 1152 + 4]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2304:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2304 + 4]
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
            A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 1280:threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 1280 + 4]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2560:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2560 + 4]
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
            A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 1408:threadIdx_x % 128 // 32 * 32 + ax0_0 * 16 + threadIdx_x % 32 // 16 * 8 + threadIdx_x % 2 * 4 + 1408 + 4]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2816:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2816 + 4]
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
        Y_1[blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8:blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 4] = Y_local_1[0:4]
        Y_1[blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 4:blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 4 + 4] = Y_local_1[4:8]
        Y_1[blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 8192:blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 8192 + 4] = Y_local_1[8:12]
        Y_1[blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 8196:blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 8196 + 4] = Y_local_1[12:16]
        Y_1[blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 16384:blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 16384 + 4] = Y_local_1[16:20]
        Y_1[blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 16388:blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 16388 + 4] = Y_local_1[20:24]
        Y_1[blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 24576:blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 24576 + 4] = Y_local_1[24:28]
        Y_1[blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 24580:blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 24580 + 4] = Y_local_1[28:32]
        Y_1[blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 32768:blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 32768 + 4] = Y_local_1[32:36]
        Y_1[blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 32772:blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 32772 + 4] = Y_local_1[36:40]
        Y_1[blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 40960:blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 40960 + 4] = Y_local_1[40:44]
        Y_1[blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 40964:blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 40964 + 4] = Y_local_1[44:48]
        Y_1[blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 49152:blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 49152 + 4] = Y_local_1[48:52]
        Y_1[blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 49156:blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 49156 + 4] = Y_local_1[52:56]
        Y_1[blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 57344:blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 57344 + 4] = Y_local_1[56:60]
        Y_1[blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 57348:blockIdx_x // 32 * 1048576 + threadIdx_x % 128 // 16 * 131072 + threadIdx_x % 2 * 65536 + blockIdx_x % 32 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + 57348 + 4] = Y_local_1[60:64]
    

