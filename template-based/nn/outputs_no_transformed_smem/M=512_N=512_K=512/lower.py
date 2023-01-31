# from tvm.script import tir as T
@tvm.script.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer[(512, 512), "float32"], B: T.Buffer[(512, 512), "float32"], Y: T.Buffer[(512, 512), "float32"]):
        # function attr dict
        T.func_attr({"global_symbol": "main", "tir.noalias": True})
        # var definition
        threadIdx_x = T.env_thread("threadIdx.x")
        blockIdx_x = T.env_thread("blockIdx.x")
        # buffer definition
        A_1 = T.buffer_decl([262144], dtype="float32", data=A.data)
        B_1 = T.buffer_decl([262144], dtype="float32", data=B.data)
        Y_1 = T.buffer_decl([262144], dtype="float32", data=Y.data)
        # body
        T.launch_thread(blockIdx_x, 64)
        Y_local = T.allocate([32], "float32", "local")
        Y_local_1 = T.buffer_decl([32], dtype="float32", data=Y_local, scope="local")
        A_shared_dyn = T.allocate([6400], "float32", "shared.dyn")
        A_shared_dyn_1 = T.buffer_decl([6400], dtype="float32", data=A_shared_dyn, scope="shared.dyn")
        B_shared_dyn = T.allocate([2560], "float32", "shared.dyn")
        B_shared_dyn_1 = T.buffer_decl([2560], dtype="float32", data=B_shared_dyn, scope="shared.dyn")
        A_shared_dyn_local = T.allocate([2], "float32x4", "local")
        A_shared_dyn_local_1 = T.buffer_decl([2], dtype="float32x4", data=A_shared_dyn_local, scope="local")
        B_shared_dyn_local = T.allocate([16], "float32", "local")
        B_shared_dyn_local_1 = T.buffer_decl([16], dtype="float32", data=B_shared_dyn_local, scope="local")
        T.launch_thread(threadIdx_x, 128)
        Y_local_1[0] = T.float32(0)
        Y_local_1[8] = T.float32(0)
        Y_local_1[16] = T.float32(0)
        Y_local_1[24] = T.float32(0)
        Y_local_1[1] = T.float32(0)
        Y_local_1[9] = T.float32(0)
        Y_local_1[17] = T.float32(0)
        Y_local_1[25] = T.float32(0)
        Y_local_1[2] = T.float32(0)
        Y_local_1[10] = T.float32(0)
        Y_local_1[18] = T.float32(0)
        Y_local_1[26] = T.float32(0)
        Y_local_1[3] = T.float32(0)
        Y_local_1[11] = T.float32(0)
        Y_local_1[19] = T.float32(0)
        Y_local_1[27] = T.float32(0)
        Y_local_1[4] = T.float32(0)
        Y_local_1[12] = T.float32(0)
        Y_local_1[20] = T.float32(0)
        Y_local_1[28] = T.float32(0)
        Y_local_1[5] = T.float32(0)
        Y_local_1[13] = T.float32(0)
        Y_local_1[21] = T.float32(0)
        Y_local_1[29] = T.float32(0)
        Y_local_1[6] = T.float32(0)
        Y_local_1[14] = T.float32(0)
        Y_local_1[22] = T.float32(0)
        Y_local_1[30] = T.float32(0)
        Y_local_1[7] = T.float32(0)
        Y_local_1[15] = T.float32(0)
        Y_local_1[23] = T.float32(0)
        Y_local_1[31] = T.float32(0)
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x // 2 * 20 + threadIdx_x % 2 * 16:threadIdx_x // 2 * 20 + threadIdx_x % 2 * 16 + 4] = A_1[blockIdx_x // 8 * 32768 + threadIdx_x // 2 * 512 + threadIdx_x % 2 * 4:blockIdx_x // 8 * 32768 + threadIdx_x // 2 * 512 + threadIdx_x % 2 * 4 + 4]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 4] = B_1[threadIdx_x // 16 * 512 + blockIdx_x % 8 * 64 + threadIdx_x % 16 * 4:threadIdx_x // 16 * 512 + blockIdx_x % 8 * 64 + threadIdx_x % 16 * 4 + 4]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x // 2 * 20 + threadIdx_x % 2 * 16 + 1280:threadIdx_x // 2 * 20 + threadIdx_x % 2 * 16 + 1280 + 4] = A_1[blockIdx_x // 8 * 32768 + threadIdx_x // 2 * 512 + threadIdx_x % 2 * 4 + 8:blockIdx_x // 8 * 32768 + threadIdx_x // 2 * 512 + threadIdx_x % 2 * 4 + 8 + 4]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 512:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 512 + 4] = B_1[threadIdx_x // 16 * 512 + blockIdx_x % 8 * 64 + threadIdx_x % 16 * 4 + 4096:threadIdx_x // 16 * 512 + blockIdx_x % 8 * 64 + threadIdx_x % 16 * 4 + 4096 + 4]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x // 2 * 20 + threadIdx_x % 2 * 16 + 2560:threadIdx_x // 2 * 20 + threadIdx_x % 2 * 16 + 2560 + 4] = A_1[blockIdx_x // 8 * 32768 + threadIdx_x // 2 * 512 + threadIdx_x % 2 * 4 + 16:blockIdx_x // 8 * 32768 + threadIdx_x // 2 * 512 + threadIdx_x % 2 * 4 + 16 + 4]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 1024:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 1024 + 4] = B_1[threadIdx_x // 16 * 512 + blockIdx_x % 8 * 64 + threadIdx_x % 16 * 4 + 8192:threadIdx_x // 16 * 512 + blockIdx_x % 8 * 64 + threadIdx_x % 16 * 4 + 8192 + 4]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x // 2 * 20 + threadIdx_x % 2 * 16 + 3840:threadIdx_x // 2 * 20 + threadIdx_x % 2 * 16 + 3840 + 4] = A_1[blockIdx_x // 8 * 32768 + threadIdx_x // 2 * 512 + threadIdx_x % 2 * 4 + 24:blockIdx_x // 8 * 32768 + threadIdx_x // 2 * 512 + threadIdx_x % 2 * 4 + 24 + 4]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 1536:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 1536 + 4] = B_1[threadIdx_x // 16 * 512 + blockIdx_x % 8 * 64 + threadIdx_x % 16 * 4 + 12288:threadIdx_x // 16 * 512 + blockIdx_x % 8 * 64 + threadIdx_x % 16 * 4 + 12288 + 4]
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 3)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4]
        for k_0 in T.serial(60):
            cse_var_1: T.int32 = (k_0 + 4) % 5
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    A_shared_dyn_1[cse_var_1 * 1280 + threadIdx_x // 2 * 20 + threadIdx_x % 2 * 16:cse_var_1 * 1280 + threadIdx_x // 2 * 20 + threadIdx_x % 2 * 16 + 4] = A_1[blockIdx_x // 8 * 32768 + threadIdx_x // 2 * 512 + k_0 * 8 + threadIdx_x % 2 * 4 + 32:blockIdx_x // 8 * 32768 + threadIdx_x // 2 * 512 + k_0 * 8 + threadIdx_x % 2 * 4 + 32 + 4]
                T.attr(0, "async_scope", 1)
                B_shared_dyn_1[cse_var_1 * 512 + threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4:cse_var_1 * 512 + threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 4] = B_1[k_0 * 4096 + threadIdx_x // 16 * 512 + blockIdx_x % 8 * 64 + threadIdx_x % 16 * 4 + 16384:k_0 * 4096 + threadIdx_x // 16 * 512 + blockIdx_x % 8 * 64 + threadIdx_x % 16 * 4 + 16384 + 4]
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 3)
                A_shared_dyn_local_1[1] = A_shared_dyn_1[k_0 % 5 * 1280 + threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 1:k_0 % 5 * 1280 + threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 1 + 80:20]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 64:k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 64 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
                A_shared_dyn_local_1[0] = A_shared_dyn_1[k_0 % 5 * 1280 + threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 2:k_0 % 5 * 1280 + threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 2 + 80:20]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 128:k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 128 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
                A_shared_dyn_local_1[1] = A_shared_dyn_1[k_0 % 5 * 1280 + threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 3:k_0 % 5 * 1280 + threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 3 + 80:20]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 192:k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 192 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
                A_shared_dyn_local_1[0] = A_shared_dyn_1[k_0 % 5 * 1280 + threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 16:k_0 % 5 * 1280 + threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 16 + 80:20]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 256:k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 256 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
                A_shared_dyn_local_1[1] = A_shared_dyn_1[k_0 % 5 * 1280 + threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 17:k_0 % 5 * 1280 + threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 17 + 80:20]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 320:k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 320 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
                A_shared_dyn_local_1[0] = A_shared_dyn_1[k_0 % 5 * 1280 + threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 18:k_0 % 5 * 1280 + threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 18 + 80:20]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 384:k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 384 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
                A_shared_dyn_local_1[1] = A_shared_dyn_1[k_0 % 5 * 1280 + threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 19:k_0 % 5 * 1280 + threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 19 + 80:20]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 448:k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 448 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[(k_0 + 1) % 5 * 1280 + threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80:(k_0 + 1) % 5 * 1280 + threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[(k_0 + 1) % 5 * 512 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4:(k_0 + 1) % 5 * 512 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 2)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 1:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 1 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 64:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 64 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 2:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 2 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 128:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 128 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 3:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 3 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 192:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 192 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 16:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 16 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 256:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 256 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 17:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 17 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 320:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 320 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 18:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 18 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 384:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 384 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 19:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 19 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 448:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 448 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 1280:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 1280 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 512:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 512 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 1)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 1281:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 1281 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 576:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 576 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 1282:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 1282 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 640:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 640 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 1283:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 1283 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 704:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 704 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 1296:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 1296 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 768:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 768 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 1297:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 1297 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 832:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 832 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 1298:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 1298 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 896:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 896 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 1299:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 1299 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 960:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 960 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 2560:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 2560 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1024:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1024 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 0)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 2561:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 2561 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1088:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1088 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 2562:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 2562 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1152:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1152 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 2563:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 2563 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1216:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1216 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 2576:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 2576 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1280:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1280 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 2577:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 2577 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1344:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1344 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 2578:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 2578 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1408:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1408 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 2579:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 2579 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1472:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1472 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 3840:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 3840 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1536:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1536 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
        A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 3841:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 3841 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1600:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1600 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 3842:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 3842 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1664:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1664 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
        A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 3843:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 3843 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1728:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1728 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 3856:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 3856 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1792:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1792 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
        A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 3857:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 3857 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1856:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1856 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 3858:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 3858 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1920:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1920 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
        A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 3859:threadIdx_x // 16 * 160 + threadIdx_x % 2 * 80 + 3859 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1984:ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1984 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
        for ax1_0 in T.serial(2):
            cse_var_2: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 8 * 32768 + threadIdx_x // 16 * 4096 + threadIdx_x % 2 * 2048 + blockIdx_x % 8 * 64 + threadIdx_x % 16 // 2 * 8 + cse_var_2:blockIdx_x // 8 * 32768 + threadIdx_x // 16 * 4096 + threadIdx_x % 2 * 2048 + blockIdx_x % 8 * 64 + threadIdx_x % 16 // 2 * 8 + cse_var_2 + 4] = Y_local_1[cse_var_2:cse_var_2 + 4]
        for ax1_0 in T.serial(2):
            cse_var_3: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 8 * 32768 + threadIdx_x // 16 * 4096 + threadIdx_x % 2 * 2048 + blockIdx_x % 8 * 64 + threadIdx_x % 16 // 2 * 8 + cse_var_3 + 512:blockIdx_x // 8 * 32768 + threadIdx_x // 16 * 4096 + threadIdx_x % 2 * 2048 + blockIdx_x % 8 * 64 + threadIdx_x % 16 // 2 * 8 + cse_var_3 + 512 + 4] = Y_local_1[cse_var_3 + 8:cse_var_3 + 8 + 4]
        for ax1_0 in T.serial(2):
            cse_var_4: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 8 * 32768 + threadIdx_x // 16 * 4096 + threadIdx_x % 2 * 2048 + blockIdx_x % 8 * 64 + threadIdx_x % 16 // 2 * 8 + cse_var_4 + 1024:blockIdx_x // 8 * 32768 + threadIdx_x // 16 * 4096 + threadIdx_x % 2 * 2048 + blockIdx_x % 8 * 64 + threadIdx_x % 16 // 2 * 8 + cse_var_4 + 1024 + 4] = Y_local_1[cse_var_4 + 16:cse_var_4 + 16 + 4]
        for ax1_0 in T.serial(2):
            cse_var_5: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 8 * 32768 + threadIdx_x // 16 * 4096 + threadIdx_x % 2 * 2048 + blockIdx_x % 8 * 64 + threadIdx_x % 16 // 2 * 8 + cse_var_5 + 1536:blockIdx_x // 8 * 32768 + threadIdx_x // 16 * 4096 + threadIdx_x % 2 * 2048 + blockIdx_x % 8 * 64 + threadIdx_x % 16 // 2 * 8 + cse_var_5 + 1536 + 4] = Y_local_1[cse_var_5 + 24:cse_var_5 + 24 + 4]
    

