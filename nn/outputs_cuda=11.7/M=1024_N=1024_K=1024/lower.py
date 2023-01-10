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
        A_shared_dyn = T.allocate([12800], "float32", "shared.dyn")
        A_shared_dyn_1 = T.buffer_decl([12800], dtype="float32", data=A_shared_dyn, scope="shared.dyn")
        B_shared_dyn = T.allocate([5120], "float32", "shared.dyn")
        B_shared_dyn_1 = T.buffer_decl([5120], dtype="float32", data=B_shared_dyn, scope="shared.dyn")
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
                A_shared_dyn_1[threadIdx_x // 4 * 20 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 2 * 2:threadIdx_x // 4 * 20 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 2 * 2 + 2] = A_1[blockIdx_x // 8 * 131072 + threadIdx_x // 4 * 1024 + threadIdx_x % 4 * 2:blockIdx_x // 8 * 131072 + threadIdx_x // 4 * 1024 + threadIdx_x % 4 * 2 + 2]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 32 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 32 // 4 * 4 + threadIdx_x % 2 * 2:threadIdx_x // 32 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 32 // 4 * 4 + threadIdx_x % 2 * 2 + 2] = B_1[threadIdx_x // 64 * 1024 + blockIdx_x % 8 * 128 + threadIdx_x % 64 * 2:threadIdx_x // 64 * 1024 + blockIdx_x % 8 * 128 + threadIdx_x % 64 * 2 + 2]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x // 4 * 20 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 2 * 2 + 2560:threadIdx_x // 4 * 20 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 2 * 2 + 2560 + 2] = A_1[blockIdx_x // 8 * 131072 + threadIdx_x // 4 * 1024 + threadIdx_x % 4 * 2 + 8:blockIdx_x // 8 * 131072 + threadIdx_x // 4 * 1024 + threadIdx_x % 4 * 2 + 8 + 2]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 32 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 32 // 4 * 4 + threadIdx_x % 2 * 2 + 1024:threadIdx_x // 32 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 32 // 4 * 4 + threadIdx_x % 2 * 2 + 1024 + 2] = B_1[threadIdx_x // 64 * 1024 + blockIdx_x % 8 * 128 + threadIdx_x % 64 * 2 + 8192:threadIdx_x // 64 * 1024 + blockIdx_x % 8 * 128 + threadIdx_x % 64 * 2 + 8192 + 2]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x // 4 * 20 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 2 * 2 + 5120:threadIdx_x // 4 * 20 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 2 * 2 + 5120 + 2] = A_1[blockIdx_x // 8 * 131072 + threadIdx_x // 4 * 1024 + threadIdx_x % 4 * 2 + 16:blockIdx_x // 8 * 131072 + threadIdx_x // 4 * 1024 + threadIdx_x % 4 * 2 + 16 + 2]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 32 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 32 // 4 * 4 + threadIdx_x % 2 * 2 + 2048:threadIdx_x // 32 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 32 // 4 * 4 + threadIdx_x % 2 * 2 + 2048 + 2] = B_1[threadIdx_x // 64 * 1024 + blockIdx_x % 8 * 128 + threadIdx_x % 64 * 2 + 16384:threadIdx_x // 64 * 1024 + blockIdx_x % 8 * 128 + threadIdx_x % 64 * 2 + 16384 + 2]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x // 4 * 20 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 2 * 2 + 7680:threadIdx_x // 4 * 20 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 2 * 2 + 7680 + 2] = A_1[blockIdx_x // 8 * 131072 + threadIdx_x // 4 * 1024 + threadIdx_x % 4 * 2 + 24:blockIdx_x // 8 * 131072 + threadIdx_x // 4 * 1024 + threadIdx_x % 4 * 2 + 24 + 2]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 32 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 32 // 4 * 4 + threadIdx_x % 2 * 2 + 3072:threadIdx_x // 32 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 32 // 4 * 4 + threadIdx_x % 2 * 2 + 3072 + 2] = B_1[threadIdx_x // 64 * 1024 + blockIdx_x % 8 * 128 + threadIdx_x % 64 * 2 + 24576:threadIdx_x // 64 * 1024 + blockIdx_x % 8 * 128 + threadIdx_x % 64 * 2 + 24576 + 2]
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 3)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4]
        for k_0 in T.serial(124):
            cse_var_1: T.int32 = (k_0 + 4) % 5
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    A_shared_dyn_1[cse_var_1 * 2560 + threadIdx_x // 4 * 20 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 2 * 2:cse_var_1 * 2560 + threadIdx_x // 4 * 20 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 2 * 2 + 2] = A_1[blockIdx_x // 8 * 131072 + threadIdx_x // 4 * 1024 + k_0 * 8 + threadIdx_x % 4 * 2 + 32:blockIdx_x // 8 * 131072 + threadIdx_x // 4 * 1024 + k_0 * 8 + threadIdx_x % 4 * 2 + 32 + 2]
                T.attr(0, "async_scope", 1)
                B_shared_dyn_1[cse_var_1 * 1024 + threadIdx_x // 32 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 32 // 4 * 4 + threadIdx_x % 2 * 2:cse_var_1 * 1024 + threadIdx_x // 32 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 32 // 4 * 4 + threadIdx_x % 2 * 2 + 2] = B_1[k_0 * 8192 + threadIdx_x // 64 * 1024 + blockIdx_x % 8 * 128 + threadIdx_x % 64 * 2 + 32768:k_0 * 8192 + threadIdx_x // 64 * 1024 + blockIdx_x % 8 * 128 + threadIdx_x % 64 * 2 + 32768 + 2]
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 3)
                A_shared_dyn_local_1[1] = A_shared_dyn_1[k_0 % 5 * 2560 + threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 1:k_0 % 5 * 2560 + threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 1 + 80:20]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[k_0 % 5 * 1024 + threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 128:k_0 % 5 * 1024 + threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 128 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
                A_shared_dyn_local_1[0] = A_shared_dyn_1[k_0 % 5 * 2560 + threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 2:k_0 % 5 * 2560 + threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 2 + 80:20]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[k_0 % 5 * 1024 + threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 256:k_0 % 5 * 1024 + threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 256 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
                A_shared_dyn_local_1[1] = A_shared_dyn_1[k_0 % 5 * 2560 + threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 3:k_0 % 5 * 2560 + threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 3 + 80:20]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[k_0 % 5 * 1024 + threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 384:k_0 % 5 * 1024 + threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 384 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
                A_shared_dyn_local_1[0] = A_shared_dyn_1[k_0 % 5 * 2560 + threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 16:k_0 % 5 * 2560 + threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 16 + 80:20]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[k_0 % 5 * 1024 + threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 512:k_0 % 5 * 1024 + threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 512 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
                A_shared_dyn_local_1[1] = A_shared_dyn_1[k_0 % 5 * 2560 + threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 17:k_0 % 5 * 2560 + threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 17 + 80:20]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[k_0 % 5 * 1024 + threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 640:k_0 % 5 * 1024 + threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 640 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
                A_shared_dyn_local_1[0] = A_shared_dyn_1[k_0 % 5 * 2560 + threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 18:k_0 % 5 * 2560 + threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 18 + 80:20]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[k_0 % 5 * 1024 + threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 768:k_0 % 5 * 1024 + threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 768 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
                A_shared_dyn_local_1[1] = A_shared_dyn_1[k_0 % 5 * 2560 + threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 19:k_0 % 5 * 2560 + threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 19 + 80:20]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[k_0 % 5 * 1024 + threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 896:k_0 % 5 * 1024 + threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 896 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[(k_0 + 1) % 5 * 2560 + threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80:(k_0 + 1) % 5 * 2560 + threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[(k_0 + 1) % 5 * 1024 + threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4:(k_0 + 1) % 5 * 1024 + threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4]
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
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 10241:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 10241 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4224:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4224 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 10242:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 10242 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4352:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4352 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 10243:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 10243 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4480:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4480 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 10256:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 10256 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4608:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4608 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 10257:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 10257 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4736:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4736 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 10258:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 10258 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4864:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4864 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 10259:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 10259 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4992:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4992 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 4]
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
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 1:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 1 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 128:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 128 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 2:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 2 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 256:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 256 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 3:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 3 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 384:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 384 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 16:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 16 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 512:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 512 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 17:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 17 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 640:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 640 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 18:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 18 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 768:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 768 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 19:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 19 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 896:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 896 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 2560:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 2560 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1024:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1024 + 4]
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
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 2561:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 2561 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1152:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1152 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 2562:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 2562 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1280:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1280 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 2563:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 2563 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1408:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1408 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 2576:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 2576 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1536:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1536 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 2577:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 2577 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1664:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1664 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 2578:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 2578 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1792:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1792 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 2579:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 2579 + 80:20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1920:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 1920 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 5120:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 5120 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2048:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2048 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
        A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 5121:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 5121 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2176:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2176 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 5122:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 5122 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2304:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2304 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
        A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 5123:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 5123 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2432:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2432 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 5136:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 5136 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2560:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2560 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
        A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 5137:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 5137 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2688:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2688 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 5138:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 5138 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2816:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2816 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
        A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 5139:threadIdx_x % 256 // 16 * 160 + threadIdx_x % 2 * 80 + 5139 + 80:20]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2944:threadIdx_x // 256 * 64 + ax1_0 * 32 + threadIdx_x % 16 // 2 * 4 + 2944 + 4]
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
            Y_1[blockIdx_x // 8 * 131072 + threadIdx_x % 256 // 16 * 8192 + threadIdx_x % 2 * 4096 + blockIdx_x % 8 * 128 + threadIdx_x // 256 * 64 + threadIdx_x % 16 // 2 * 8 + cse_var_2:blockIdx_x // 8 * 131072 + threadIdx_x % 256 // 16 * 8192 + threadIdx_x % 2 * 4096 + blockIdx_x % 8 * 128 + threadIdx_x // 256 * 64 + threadIdx_x % 16 // 2 * 8 + cse_var_2 + 4] = Y_local_1[cse_var_2:cse_var_2 + 4]
        for ax1_0 in T.serial(2):
            cse_var_3: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 8 * 131072 + threadIdx_x % 256 // 16 * 8192 + threadIdx_x % 2 * 4096 + blockIdx_x % 8 * 128 + threadIdx_x // 256 * 64 + threadIdx_x % 16 // 2 * 8 + cse_var_3 + 1024:blockIdx_x // 8 * 131072 + threadIdx_x % 256 // 16 * 8192 + threadIdx_x % 2 * 4096 + blockIdx_x % 8 * 128 + threadIdx_x // 256 * 64 + threadIdx_x % 16 // 2 * 8 + cse_var_3 + 1024 + 4] = Y_local_1[cse_var_3 + 8:cse_var_3 + 8 + 4]
        for ax1_0 in T.serial(2):
            cse_var_4: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 8 * 131072 + threadIdx_x % 256 // 16 * 8192 + threadIdx_x % 2 * 4096 + blockIdx_x % 8 * 128 + threadIdx_x // 256 * 64 + threadIdx_x % 16 // 2 * 8 + cse_var_4 + 2048:blockIdx_x // 8 * 131072 + threadIdx_x % 256 // 16 * 8192 + threadIdx_x % 2 * 4096 + blockIdx_x % 8 * 128 + threadIdx_x // 256 * 64 + threadIdx_x % 16 // 2 * 8 + cse_var_4 + 2048 + 4] = Y_local_1[cse_var_4 + 16:cse_var_4 + 16 + 4]
        for ax1_0 in T.serial(2):
            cse_var_5: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 8 * 131072 + threadIdx_x % 256 // 16 * 8192 + threadIdx_x % 2 * 4096 + blockIdx_x % 8 * 128 + threadIdx_x // 256 * 64 + threadIdx_x % 16 // 2 * 8 + cse_var_5 + 3072:blockIdx_x // 8 * 131072 + threadIdx_x % 256 // 16 * 8192 + threadIdx_x % 2 * 4096 + blockIdx_x % 8 * 128 + threadIdx_x // 256 * 64 + threadIdx_x % 16 // 2 * 8 + cse_var_5 + 3072 + 4] = Y_local_1[cse_var_5 + 24:cse_var_5 + 24 + 4]
    

