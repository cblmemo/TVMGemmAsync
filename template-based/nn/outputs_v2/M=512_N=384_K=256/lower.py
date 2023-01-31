# from tvm.script import tir as T
@tvm.script.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer[(512, 256), "float32"], B: T.Buffer[(256, 384), "float32"], Y: T.Buffer[(512, 384), "float32"]):
        # function attr dict
        T.func_attr({"global_symbol": "main", "tir.noalias": True})
        # var definition
        threadIdx_x = T.env_thread("threadIdx.x")
        blockIdx_x = T.env_thread("blockIdx.x")
        # buffer definition
        A_1 = T.buffer_decl([131072], dtype="float32", data=A.data)
        B_1 = T.buffer_decl([98304], dtype="float32", data=B.data)
        Y_1 = T.buffer_decl([196608], dtype="float32", data=Y.data)
        # body
        T.launch_thread(blockIdx_x, 48)
        Y_local = T.allocate([32], "float32", "local")
        Y_local_1 = T.buffer_decl([32], dtype="float32", data=Y_local, scope="local")
        A_shared_dyn = T.allocate([2560], "float32", "shared.dyn")
        A_shared_dyn_1 = T.buffer_decl([2560], dtype="float32", data=A_shared_dyn, scope="shared.dyn")
        B_shared_dyn = T.allocate([2560], "float32", "shared.dyn")
        B_shared_dyn_1 = T.buffer_decl([2560], dtype="float32", data=B_shared_dyn, scope="shared.dyn")
        A_shared_dyn_local = T.allocate([4], "float32x4", "local")
        A_shared_dyn_local_1 = T.buffer_decl([4], dtype="float32x4", data=A_shared_dyn_local, scope="local")
        B_shared_dyn_local = T.allocate([8], "float32", "local")
        B_shared_dyn_local_1 = T.buffer_decl([8], dtype="float32", data=B_shared_dyn_local, scope="local")
        T.launch_thread(threadIdx_x, 128)
        Y_local_1[0] = T.float32(0)
        Y_local_1[4] = T.float32(0)
        Y_local_1[8] = T.float32(0)
        Y_local_1[12] = T.float32(0)
        Y_local_1[16] = T.float32(0)
        Y_local_1[20] = T.float32(0)
        Y_local_1[24] = T.float32(0)
        Y_local_1[28] = T.float32(0)
        Y_local_1[1] = T.float32(0)
        Y_local_1[5] = T.float32(0)
        Y_local_1[9] = T.float32(0)
        Y_local_1[13] = T.float32(0)
        Y_local_1[17] = T.float32(0)
        Y_local_1[21] = T.float32(0)
        Y_local_1[25] = T.float32(0)
        Y_local_1[29] = T.float32(0)
        Y_local_1[2] = T.float32(0)
        Y_local_1[6] = T.float32(0)
        Y_local_1[10] = T.float32(0)
        Y_local_1[14] = T.float32(0)
        Y_local_1[18] = T.float32(0)
        Y_local_1[22] = T.float32(0)
        Y_local_1[26] = T.float32(0)
        Y_local_1[30] = T.float32(0)
        Y_local_1[3] = T.float32(0)
        Y_local_1[7] = T.float32(0)
        Y_local_1[11] = T.float32(0)
        Y_local_1[15] = T.float32(0)
        Y_local_1[19] = T.float32(0)
        Y_local_1[23] = T.float32(0)
        Y_local_1[27] = T.float32(0)
        Y_local_1[31] = T.float32(0)
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x % 8 * 64 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 8 * 16 + threadIdx_x % 64 // 16 * 4] = A_1[blockIdx_x // 6 * 16384 + threadIdx_x // 8 * 1024 + threadIdx_x % 8]
                A_shared_dyn_1[threadIdx_x % 8 * 64 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 8 * 16 + threadIdx_x % 64 // 16 * 4 + 1] = A_1[blockIdx_x // 6 * 16384 + threadIdx_x // 8 * 1024 + threadIdx_x % 8 + 256]
                A_shared_dyn_1[threadIdx_x % 8 * 64 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 8 * 16 + threadIdx_x % 64 // 16 * 4 + 2] = A_1[blockIdx_x // 6 * 16384 + threadIdx_x // 8 * 1024 + threadIdx_x % 8 + 512]
                A_shared_dyn_1[threadIdx_x % 8 * 64 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 8 * 16 + threadIdx_x % 64 // 16 * 4 + 3] = A_1[blockIdx_x // 6 * 16384 + threadIdx_x // 8 * 1024 + threadIdx_x % 8 + 768]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 4] = B_1[threadIdx_x // 16 * 384 + blockIdx_x % 6 * 64 + threadIdx_x % 16 * 4:threadIdx_x // 16 * 384 + blockIdx_x % 6 * 64 + threadIdx_x % 16 * 4 + 4]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x % 8 * 64 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 8 * 16 + threadIdx_x % 64 // 16 * 4 + 512] = A_1[blockIdx_x // 6 * 16384 + threadIdx_x // 8 * 1024 + threadIdx_x % 8 + 8]
                A_shared_dyn_1[threadIdx_x % 8 * 64 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 8 * 16 + threadIdx_x % 64 // 16 * 4 + 513] = A_1[blockIdx_x // 6 * 16384 + threadIdx_x // 8 * 1024 + threadIdx_x % 8 + 264]
                A_shared_dyn_1[threadIdx_x % 8 * 64 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 8 * 16 + threadIdx_x % 64 // 16 * 4 + 514] = A_1[blockIdx_x // 6 * 16384 + threadIdx_x // 8 * 1024 + threadIdx_x % 8 + 520]
                A_shared_dyn_1[threadIdx_x % 8 * 64 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 8 * 16 + threadIdx_x % 64 // 16 * 4 + 515] = A_1[blockIdx_x // 6 * 16384 + threadIdx_x // 8 * 1024 + threadIdx_x % 8 + 776]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 512:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 512 + 4] = B_1[threadIdx_x // 16 * 384 + blockIdx_x % 6 * 64 + threadIdx_x % 16 * 4 + 3072:threadIdx_x // 16 * 384 + blockIdx_x % 6 * 64 + threadIdx_x % 16 * 4 + 3072 + 4]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x % 8 * 64 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 8 * 16 + threadIdx_x % 64 // 16 * 4 + 1024] = A_1[blockIdx_x // 6 * 16384 + threadIdx_x // 8 * 1024 + threadIdx_x % 8 + 16]
                A_shared_dyn_1[threadIdx_x % 8 * 64 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 8 * 16 + threadIdx_x % 64 // 16 * 4 + 1025] = A_1[blockIdx_x // 6 * 16384 + threadIdx_x // 8 * 1024 + threadIdx_x % 8 + 272]
                A_shared_dyn_1[threadIdx_x % 8 * 64 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 8 * 16 + threadIdx_x % 64 // 16 * 4 + 1026] = A_1[blockIdx_x // 6 * 16384 + threadIdx_x // 8 * 1024 + threadIdx_x % 8 + 528]
                A_shared_dyn_1[threadIdx_x % 8 * 64 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 8 * 16 + threadIdx_x % 64 // 16 * 4 + 1027] = A_1[blockIdx_x // 6 * 16384 + threadIdx_x // 8 * 1024 + threadIdx_x % 8 + 784]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 1024:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 1024 + 4] = B_1[threadIdx_x // 16 * 384 + blockIdx_x % 6 * 64 + threadIdx_x % 16 * 4 + 6144:threadIdx_x // 16 * 384 + blockIdx_x % 6 * 64 + threadIdx_x % 16 * 4 + 6144 + 4]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x % 8 * 64 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 8 * 16 + threadIdx_x % 64 // 16 * 4 + 1536] = A_1[blockIdx_x // 6 * 16384 + threadIdx_x // 8 * 1024 + threadIdx_x % 8 + 24]
                A_shared_dyn_1[threadIdx_x % 8 * 64 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 8 * 16 + threadIdx_x % 64 // 16 * 4 + 1537] = A_1[blockIdx_x // 6 * 16384 + threadIdx_x // 8 * 1024 + threadIdx_x % 8 + 280]
                A_shared_dyn_1[threadIdx_x % 8 * 64 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 8 * 16 + threadIdx_x % 64 // 16 * 4 + 1538] = A_1[blockIdx_x // 6 * 16384 + threadIdx_x // 8 * 1024 + threadIdx_x % 8 + 536]
                A_shared_dyn_1[threadIdx_x % 8 * 64 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 8 * 16 + threadIdx_x % 64 // 16 * 4 + 1539] = A_1[blockIdx_x // 6 * 16384 + threadIdx_x // 8 * 1024 + threadIdx_x % 8 + 792]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 1536:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 1536 + 4] = B_1[threadIdx_x // 16 * 384 + blockIdx_x % 6 * 64 + threadIdx_x % 16 * 4 + 9216:threadIdx_x // 16 * 384 + blockIdx_x % 6 * 64 + threadIdx_x % 16 * 4 + 9216 + 4]
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 3)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 4]
        for k_0 in T.serial(28):
            cse_var_1: T.int32 = (k_0 + 4) % 5 * 512
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    A_shared_dyn_1[cse_var_1 + threadIdx_x % 8 * 64 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 8 * 16 + threadIdx_x % 64 // 16 * 4] = A_1[blockIdx_x // 6 * 16384 + threadIdx_x // 8 * 1024 + k_0 * 8 + threadIdx_x % 8 + 32]
                    A_shared_dyn_1[cse_var_1 + threadIdx_x % 8 * 64 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 8 * 16 + threadIdx_x % 64 // 16 * 4 + 1] = A_1[blockIdx_x // 6 * 16384 + threadIdx_x // 8 * 1024 + k_0 * 8 + threadIdx_x % 8 + 288]
                    A_shared_dyn_1[cse_var_1 + threadIdx_x % 8 * 64 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 8 * 16 + threadIdx_x % 64 // 16 * 4 + 2] = A_1[blockIdx_x // 6 * 16384 + threadIdx_x // 8 * 1024 + k_0 * 8 + threadIdx_x % 8 + 544]
                    A_shared_dyn_1[cse_var_1 + threadIdx_x % 8 * 64 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 8 * 16 + threadIdx_x % 64 // 16 * 4 + 3] = A_1[blockIdx_x // 6 * 16384 + threadIdx_x // 8 * 1024 + k_0 * 8 + threadIdx_x % 8 + 800]
                T.attr(0, "async_scope", 1)
                B_shared_dyn_1[cse_var_1 + threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4:cse_var_1 + threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 4] = B_1[k_0 * 3072 + threadIdx_x // 16 * 384 + blockIdx_x % 6 * 64 + threadIdx_x % 16 * 4 + 12288:k_0 * 3072 + threadIdx_x // 16 * 384 + blockIdx_x % 6 * 64 + threadIdx_x % 16 * 4 + 12288 + 4]
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 3)
                for ax0_0 in T.serial(2):
                    A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[k_0 % 5 * 512 + threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 64:k_0 % 5 * 512 + threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 64 + 4]
                B_shared_dyn_local_1[4:8] = B_shared_dyn_1[k_0 % 5 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 64:k_0 % 5 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 64 + 4]
                Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
                for ax0_0 in T.serial(2):
                    A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[k_0 % 5 * 512 + threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 128:k_0 % 5 * 512 + threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 128 + 4]
                B_shared_dyn_local_1[0:4] = B_shared_dyn_1[k_0 % 5 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 128:k_0 % 5 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 128 + 4]
                Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[7], 4)
                for ax0_0 in T.serial(2):
                    A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[k_0 % 5 * 512 + threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 192:k_0 % 5 * 512 + threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 192 + 4]
                B_shared_dyn_local_1[4:8] = B_shared_dyn_1[k_0 % 5 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 192:k_0 % 5 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 192 + 4]
                Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
                for ax0_0 in T.serial(2):
                    A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[k_0 % 5 * 512 + threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 256:k_0 % 5 * 512 + threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 256 + 4]
                B_shared_dyn_local_1[0:4] = B_shared_dyn_1[k_0 % 5 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 256:k_0 % 5 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 256 + 4]
                Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[7], 4)
                for ax0_0 in T.serial(2):
                    A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[k_0 % 5 * 512 + threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 320:k_0 % 5 * 512 + threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 320 + 4]
                B_shared_dyn_local_1[4:8] = B_shared_dyn_1[k_0 % 5 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 320:k_0 % 5 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 320 + 4]
                Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
                for ax0_0 in T.serial(2):
                    A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[k_0 % 5 * 512 + threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 384:k_0 % 5 * 512 + threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 384 + 4]
                B_shared_dyn_local_1[0:4] = B_shared_dyn_1[k_0 % 5 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 384:k_0 % 5 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 384 + 4]
                Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[7], 4)
                for ax0_0 in T.serial(2):
                    A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[k_0 % 5 * 512 + threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 448:k_0 % 5 * 512 + threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 448 + 4]
                B_shared_dyn_local_1[4:8] = B_shared_dyn_1[k_0 % 5 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 448:k_0 % 5 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 448 + 4]
                Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[(k_0 + 1) % 5 * 512 + threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4:(k_0 + 1) % 5 * 512 + threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[(k_0 + 1) % 5 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4:(k_0 + 1) % 5 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[7], 4)
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 2)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 1600:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 1600 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 1600:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 1600 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 1664:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 1664 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 1664:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 1664 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[7], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 1728:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 1728 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 1728:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 1728 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 1792:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 1792 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 1792:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 1792 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[7], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 1856:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 1856 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 1856:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 1856 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 1920:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 1920 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 1920:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 1920 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[7], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 1984:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 1984 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 1984:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 1984 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
        for ax0_0 in T.serial(2):
            A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 2048:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 2048 + 4]
        B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 2048:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 2048 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[7], 4)
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 1)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 2112:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 2112 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 2112:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 2112 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 2176:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 2176 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 2176:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 2176 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[7], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 2240:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 2240 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 2240:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 2240 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 2304:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 2304 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 2304:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 2304 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[7], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 2368:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 2368 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 2368:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 2368 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 2432:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 2432 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 2432:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 2432 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[7], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 2496:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 2496 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 2496:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 2496 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
        for ax0_0 in T.serial(2):
            A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 4]
        B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[7], 4)
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 0)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 64:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 64 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 64:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 64 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 128:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 128 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 128:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 128 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[7], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 192:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 192 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 192:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 192 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 256:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 256 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 256:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 256 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[7], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 320:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 320 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 320:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 320 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 384:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 384 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 384:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 384 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[7], 4)
            for ax0_0 in T.serial(2):
                A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 448:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 448 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 448:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 448 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
        for ax0_0 in T.serial(2):
            A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 512:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 512 + 4]
        B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 512:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 512 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[7], 4)
        for ax0_0 in T.serial(2):
            A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 576:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 576 + 4]
        B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 576:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 576 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
        for ax0_0 in T.serial(2):
            A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 640:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 640 + 4]
        B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 640:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 640 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[7], 4)
        for ax0_0 in T.serial(2):
            A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 704:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 704 + 4]
        B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 704:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 704 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
        for ax0_0 in T.serial(2):
            A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 768:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 768 + 4]
        B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 768:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 768 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[7], 4)
        for ax0_0 in T.serial(2):
            A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 832:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 832 + 4]
        B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 832:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 832 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
        for ax0_0 in T.serial(2):
            A_shared_dyn_local_1[ax0_0] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 896:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 896 + 4]
        B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 896:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 896 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[7], 4)
        for ax0_0 in T.serial(2):
            A_shared_dyn_local_1[ax0_0 + 2] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 960:threadIdx_x % 32 // 16 * 32 + ax0_0 * 16 + threadIdx_x % 16 // 8 * 8 + threadIdx_x % 2 * 4 + 960 + 4]
        B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 960:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 8 // 4 * 4 + 960 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_1[blockIdx_x // 6 * 24576 + threadIdx_x % 32 // 8 * 6144 + threadIdx_x % 2 * 3072 + blockIdx_x % 6 * 64 + threadIdx_x // 32 * 16 + threadIdx_x % 8 // 2 * 4:blockIdx_x // 6 * 24576 + threadIdx_x % 32 // 8 * 6144 + threadIdx_x % 2 * 3072 + blockIdx_x % 6 * 64 + threadIdx_x // 32 * 16 + threadIdx_x % 8 // 2 * 4 + 4] = Y_local_1[0:4]
        Y_1[blockIdx_x // 6 * 24576 + threadIdx_x % 32 // 8 * 6144 + threadIdx_x % 2 * 3072 + blockIdx_x % 6 * 64 + threadIdx_x // 32 * 16 + threadIdx_x % 8 // 2 * 4 + 384:blockIdx_x // 6 * 24576 + threadIdx_x % 32 // 8 * 6144 + threadIdx_x % 2 * 3072 + blockIdx_x % 6 * 64 + threadIdx_x // 32 * 16 + threadIdx_x % 8 // 2 * 4 + 384 + 4] = Y_local_1[4:8]
        Y_1[blockIdx_x // 6 * 24576 + threadIdx_x % 32 // 8 * 6144 + threadIdx_x % 2 * 3072 + blockIdx_x % 6 * 64 + threadIdx_x // 32 * 16 + threadIdx_x % 8 // 2 * 4 + 768:blockIdx_x // 6 * 24576 + threadIdx_x % 32 // 8 * 6144 + threadIdx_x % 2 * 3072 + blockIdx_x % 6 * 64 + threadIdx_x // 32 * 16 + threadIdx_x % 8 // 2 * 4 + 768 + 4] = Y_local_1[8:12]
        Y_1[blockIdx_x // 6 * 24576 + threadIdx_x % 32 // 8 * 6144 + threadIdx_x % 2 * 3072 + blockIdx_x % 6 * 64 + threadIdx_x // 32 * 16 + threadIdx_x % 8 // 2 * 4 + 1152:blockIdx_x // 6 * 24576 + threadIdx_x % 32 // 8 * 6144 + threadIdx_x % 2 * 3072 + blockIdx_x % 6 * 64 + threadIdx_x // 32 * 16 + threadIdx_x % 8 // 2 * 4 + 1152 + 4] = Y_local_1[12:16]
        Y_1[blockIdx_x // 6 * 24576 + threadIdx_x % 32 // 8 * 6144 + threadIdx_x % 2 * 3072 + blockIdx_x % 6 * 64 + threadIdx_x // 32 * 16 + threadIdx_x % 8 // 2 * 4 + 1536:blockIdx_x // 6 * 24576 + threadIdx_x % 32 // 8 * 6144 + threadIdx_x % 2 * 3072 + blockIdx_x % 6 * 64 + threadIdx_x // 32 * 16 + threadIdx_x % 8 // 2 * 4 + 1536 + 4] = Y_local_1[16:20]
        Y_1[blockIdx_x // 6 * 24576 + threadIdx_x % 32 // 8 * 6144 + threadIdx_x % 2 * 3072 + blockIdx_x % 6 * 64 + threadIdx_x // 32 * 16 + threadIdx_x % 8 // 2 * 4 + 1920:blockIdx_x // 6 * 24576 + threadIdx_x % 32 // 8 * 6144 + threadIdx_x % 2 * 3072 + blockIdx_x % 6 * 64 + threadIdx_x // 32 * 16 + threadIdx_x % 8 // 2 * 4 + 1920 + 4] = Y_local_1[20:24]
        Y_1[blockIdx_x // 6 * 24576 + threadIdx_x % 32 // 8 * 6144 + threadIdx_x % 2 * 3072 + blockIdx_x % 6 * 64 + threadIdx_x // 32 * 16 + threadIdx_x % 8 // 2 * 4 + 2304:blockIdx_x // 6 * 24576 + threadIdx_x % 32 // 8 * 6144 + threadIdx_x % 2 * 3072 + blockIdx_x % 6 * 64 + threadIdx_x // 32 * 16 + threadIdx_x % 8 // 2 * 4 + 2304 + 4] = Y_local_1[24:28]
        Y_1[blockIdx_x // 6 * 24576 + threadIdx_x % 32 // 8 * 6144 + threadIdx_x % 2 * 3072 + blockIdx_x % 6 * 64 + threadIdx_x // 32 * 16 + threadIdx_x % 8 // 2 * 4 + 2688:blockIdx_x // 6 * 24576 + threadIdx_x % 32 // 8 * 6144 + threadIdx_x % 2 * 3072 + blockIdx_x % 6 * 64 + threadIdx_x // 32 * 16 + threadIdx_x % 8 // 2 * 4 + 2688 + 4] = Y_local_1[28:32]
    

