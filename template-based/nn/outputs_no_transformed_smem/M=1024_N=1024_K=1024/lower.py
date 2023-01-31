# from tvm.script import tir as T
@tvm.script.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer[(1024, 1024), "float32"], B: T.Buffer[(1024, 1024), "float32"], Y: T.Buffer[(1024, 1024), "float32"]):
        # function attr dict
        T.func_attr({"global_symbol": "main", "tir.noalias": True})
        # var definition
        threadIdx_x = T.env_thread("threadIdx.x")
        blockIdx_x = T.env_thread("blockIdx.x")
        # buffer definition
        A_1 = T.buffer_decl([1048576], dtype="float32", data=A.data)
        B_1 = T.buffer_decl([1048576], dtype="float32", data=B.data)
        Y_1 = T.buffer_decl([1048576], dtype="float32", data=Y.data)
        # body
        T.launch_thread(blockIdx_x, 64)
        Y_local = T.allocate([32], "float32", "local")
        Y_local_1 = T.buffer_decl([32], dtype="float32", data=Y_local, scope="local")
        A_shared_dyn = T.allocate([6400], "float32", "shared.dyn")
        A_shared_dyn_1 = T.buffer_decl([6400], dtype="float32", data=A_shared_dyn, scope="shared.dyn")
        B_shared_dyn = T.allocate([10240], "float32", "shared.dyn")
        B_shared_dyn_1 = T.buffer_decl([10240], dtype="float32", data=B_shared_dyn, scope="shared.dyn")
        A_shared_dyn_local = T.allocate([2], "float32x4", "local")
        A_shared_dyn_local_1 = T.buffer_decl([2], dtype="float32x4", data=A_shared_dyn_local, scope="local")
        B_shared_dyn_local = T.allocate([16], "float32", "local")
        B_shared_dyn_local_1 = T.buffer_decl([16], dtype="float32", data=B_shared_dyn_local, scope="local")
        T.launch_thread(threadIdx_x, 512)
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
                A_shared_dyn_1[threadIdx_x // 8 * 20 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 4] = A_1[blockIdx_x // 4 * 65536 + threadIdx_x // 8 * 1024 + threadIdx_x % 8]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 4] = B_1[threadIdx_x // 64 * 1024 + blockIdx_x % 4 * 256 + threadIdx_x % 64 * 4:threadIdx_x // 64 * 1024 + blockIdx_x % 4 * 256 + threadIdx_x % 64 * 4 + 4]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x // 8 * 20 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 4 + 1280] = A_1[blockIdx_x // 4 * 65536 + threadIdx_x // 8 * 1024 + threadIdx_x % 8 + 8]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 2048:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 2048 + 4] = B_1[threadIdx_x // 64 * 1024 + blockIdx_x % 4 * 256 + threadIdx_x % 64 * 4 + 8192:threadIdx_x // 64 * 1024 + blockIdx_x % 4 * 256 + threadIdx_x % 64 * 4 + 8192 + 4]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x // 8 * 20 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 4 + 2560] = A_1[blockIdx_x // 4 * 65536 + threadIdx_x // 8 * 1024 + threadIdx_x % 8 + 16]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 4096:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 4096 + 4] = B_1[threadIdx_x // 64 * 1024 + blockIdx_x % 4 * 256 + threadIdx_x % 64 * 4 + 16384:threadIdx_x // 64 * 1024 + blockIdx_x % 4 * 256 + threadIdx_x % 64 * 4 + 16384 + 4]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x // 8 * 20 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 4 + 3840] = A_1[blockIdx_x // 4 * 65536 + threadIdx_x // 8 * 1024 + threadIdx_x % 8 + 24]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 6144:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 6144 + 4] = B_1[threadIdx_x // 64 * 1024 + blockIdx_x % 4 * 256 + threadIdx_x % 64 * 4 + 24576:threadIdx_x // 64 * 1024 + blockIdx_x % 4 * 256 + threadIdx_x % 64 * 4 + 24576 + 4]
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 3)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4]
        for k_0 in T.serial(124):
            cse_var_1: T.int32 = (k_0 + 4) % 5
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    A_shared_dyn_1[cse_var_1 * 1280 + threadIdx_x // 8 * 20 + threadIdx_x % 8 // 4 * 16 + threadIdx_x % 4] = A_1[blockIdx_x // 4 * 65536 + threadIdx_x // 8 * 1024 + k_0 * 8 + threadIdx_x % 8 + 32]
                T.attr(0, "async_scope", 1)
                B_shared_dyn_1[cse_var_1 * 2048 + threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4:cse_var_1 * 2048 + threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 4] = B_1[k_0 * 8192 + threadIdx_x // 64 * 1024 + blockIdx_x % 4 * 256 + threadIdx_x % 64 * 4 + 32768:k_0 * 8192 + threadIdx_x // 64 * 1024 + blockIdx_x % 4 * 256 + threadIdx_x % 64 * 4 + 32768 + 4]
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 3)
                A_shared_dyn_local_1[1] = A_shared_dyn_1[k_0 % 5 * 1280 + threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 1:k_0 % 5 * 1280 + threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 1 + 80:20]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[k_0 % 5 * 2048 + threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 256:k_0 % 5 * 2048 + threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 256 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
                A_shared_dyn_local_1[0] = A_shared_dyn_1[k_0 % 5 * 1280 + threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 2:k_0 % 5 * 1280 + threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 2 + 80:20]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[k_0 % 5 * 2048 + threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 512:k_0 % 5 * 2048 + threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 512 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
                A_shared_dyn_local_1[1] = A_shared_dyn_1[k_0 % 5 * 1280 + threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 3:k_0 % 5 * 1280 + threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 3 + 80:20]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[k_0 % 5 * 2048 + threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 768:k_0 % 5 * 2048 + threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 768 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
                A_shared_dyn_local_1[0] = A_shared_dyn_1[k_0 % 5 * 1280 + threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 16:k_0 % 5 * 1280 + threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 16 + 80:20]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[k_0 % 5 * 2048 + threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1024:k_0 % 5 * 2048 + threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1024 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
                A_shared_dyn_local_1[1] = A_shared_dyn_1[k_0 % 5 * 1280 + threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 17:k_0 % 5 * 1280 + threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 17 + 80:20]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[k_0 % 5 * 2048 + threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1280:k_0 % 5 * 2048 + threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1280 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
                A_shared_dyn_local_1[0] = A_shared_dyn_1[k_0 % 5 * 1280 + threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 18:k_0 % 5 * 1280 + threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 18 + 80:20]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[k_0 % 5 * 2048 + threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1536:k_0 % 5 * 2048 + threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1536 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
                A_shared_dyn_local_1[1] = A_shared_dyn_1[k_0 % 5 * 1280 + threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 19:k_0 % 5 * 1280 + threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 19 + 80:20]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[k_0 % 5 * 2048 + threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1792:k_0 % 5 * 2048 + threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1792 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[(k_0 + 1) % 5 * 1280 + threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80:(k_0 + 1) % 5 * 1280 + threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[(k_0 + 1) % 5 * 2048 + threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4:(k_0 + 1) % 5 * 2048 + threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4]
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
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 5121:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 5121 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 8448:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 8448 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 5122:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 5122 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 8704:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 8704 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 5123:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 5123 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 8960:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 8960 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 5136:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 5136 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 9216:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 9216 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 5137:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 5137 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 9472:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 9472 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 5138:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 5138 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 9728:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 9728 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 5139:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 5139 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 9984:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 9984 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4]
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
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 1:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 1 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 256:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 256 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 2:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 2 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 512:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 512 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 3:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 3 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 768:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 768 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 16:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 16 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1024:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1024 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 17:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 17 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1280:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1280 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 18:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 18 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1536:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1536 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 19:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 19 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1792:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1792 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 1280:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 1280 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2048:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2048 + 4]
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
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 1281:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 1281 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2304:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2304 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 1282:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 1282 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2560:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2560 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 1283:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 1283 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2816:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2816 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 1296:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 1296 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 3072:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 3072 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 1297:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 1297 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 3328:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 3328 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 1298:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 1298 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 3584:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 3584 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 1299:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 1299 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 3840:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 3840 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 2560:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 2560 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4096:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4096 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
        A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 2561:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 2561 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4352:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4352 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 2562:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 2562 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4608:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4608 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
        A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 2563:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 2563 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4864:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4864 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 2576:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 2576 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 5120:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 5120 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
        A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 2577:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 2577 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 5376:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 5376 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 2578:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 2578 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 5632:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 5632 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
        A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 2579:threadIdx_x % 128 // 16 * 160 + threadIdx_x % 2 * 80 + 2579 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 5888:threadIdx_x // 128 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 5888 + 4]
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
            Y_1[blockIdx_x // 4 * 65536 + threadIdx_x % 128 // 16 * 8192 + threadIdx_x % 2 * 4096 + blockIdx_x % 4 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + cse_var_2:blockIdx_x // 4 * 65536 + threadIdx_x % 128 // 16 * 8192 + threadIdx_x % 2 * 4096 + blockIdx_x % 4 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + cse_var_2 + 4] = Y_local_1[cse_var_2:cse_var_2 + 4]
        for ax1_0 in T.serial(2):
            cse_var_3: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 4 * 65536 + threadIdx_x % 128 // 16 * 8192 + threadIdx_x % 2 * 4096 + blockIdx_x % 4 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + cse_var_3 + 1024:blockIdx_x // 4 * 65536 + threadIdx_x % 128 // 16 * 8192 + threadIdx_x % 2 * 4096 + blockIdx_x % 4 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + cse_var_3 + 1024 + 4] = Y_local_1[cse_var_3 + 8:cse_var_3 + 8 + 4]
        for ax1_0 in T.serial(2):
            cse_var_4: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 4 * 65536 + threadIdx_x % 128 // 16 * 8192 + threadIdx_x % 2 * 4096 + blockIdx_x % 4 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + cse_var_4 + 2048:blockIdx_x // 4 * 65536 + threadIdx_x % 128 // 16 * 8192 + threadIdx_x % 2 * 4096 + blockIdx_x % 4 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + cse_var_4 + 2048 + 4] = Y_local_1[cse_var_4 + 16:cse_var_4 + 16 + 4]
        for ax1_0 in T.serial(2):
            cse_var_5: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 4 * 65536 + threadIdx_x % 128 // 16 * 8192 + threadIdx_x % 2 * 4096 + blockIdx_x % 4 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + cse_var_5 + 3072:blockIdx_x // 4 * 65536 + threadIdx_x % 128 // 16 * 8192 + threadIdx_x % 2 * 4096 + blockIdx_x % 4 * 256 + threadIdx_x // 128 * 64 + threadIdx_x % 16 // 2 * 8 + cse_var_5 + 3072 + 4] = Y_local_1[cse_var_5 + 24:cse_var_5 + 24 + 4]
    

