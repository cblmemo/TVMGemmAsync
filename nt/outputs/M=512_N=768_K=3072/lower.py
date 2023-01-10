# from tvm.script import tir as T
@tvm.script.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer[(3072, 512), "float32"], B: T.Buffer[(3072, 768), "float32"], Y: T.Buffer[(512, 768), "float32"]):
        # function attr dict
        T.func_attr({"global_symbol": "main", "tir.noalias": True})
        # var definition
        threadIdx_x = T.env_thread("threadIdx.x")
        blockIdx_x = T.env_thread("blockIdx.x")
        # buffer definition
        A_1 = T.buffer_decl([1572864], dtype="float32", data=A.data)
        B_1 = T.buffer_decl([2359296], dtype="float32", data=B.data)
        Y_1 = T.buffer_decl([393216], dtype="float32", data=Y.data)
        # body
        T.launch_thread(blockIdx_x, 64)
        Y_local = T.allocate([48], "float32", "local")
        Y_local_1 = T.buffer_decl([48], dtype="float32", data=Y_local, scope="local")
        A_shared_dyn = T.allocate([1024], "float32", "shared.dyn")
        A_shared_dyn_1 = T.buffer_decl([1024], dtype="float32", data=A_shared_dyn, scope="shared.dyn")
        B_shared_dyn = T.allocate([12288], "float32", "shared.dyn")
        B_shared_dyn_1 = T.buffer_decl([12288], dtype="float32", data=B_shared_dyn, scope="shared.dyn")
        A_shared_dyn_local = T.allocate([2], "float32x4", "local")
        A_shared_dyn_local_1 = T.buffer_decl([2], dtype="float32x4", data=A_shared_dyn_local, scope="local")
        B_shared_dyn_local = T.allocate([24], "float32", "local")
        B_shared_dyn_local_1 = T.buffer_decl([24], dtype="float32", data=B_shared_dyn_local, scope="local")
        T.launch_thread(threadIdx_x, 128)
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
                A_shared_dyn_1[threadIdx_x // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + threadIdx_x % 2 * 2:threadIdx_x // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + threadIdx_x % 2 * 2 + 2] = A_1[threadIdx_x // 32 * 512 + blockIdx_x // 8 * 64 + threadIdx_x % 32 * 2:threadIdx_x // 32 * 512 + blockIdx_x // 8 * 64 + threadIdx_x % 32 * 2 + 2]
            T.attr(0, "async_scope", 1)
            for ax0_ax1_fused_2 in T.serial(3):
                B_shared_dyn_1[threadIdx_x // 32 * 768 + (blockIdx_x % 8 * 3 + (threadIdx_x % 32 * 3 + ax0_ax1_fused_2) // 32) // 2 * 64 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 8 // 4 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 * 3 + ax0_ax1_fused_2) // 8) % 8 * 4 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 4 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64)] = B_1[threadIdx_x // 32 * 768 + blockIdx_x % 8 * 96 + threadIdx_x % 32 * 3 + ax0_ax1_fused_2]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + threadIdx_x % 2 * 2 + 256:threadIdx_x // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + threadIdx_x % 2 * 2 + 256 + 2] = A_1[threadIdx_x // 32 * 512 + blockIdx_x // 8 * 64 + threadIdx_x % 32 * 2 + 2048:threadIdx_x // 32 * 512 + blockIdx_x // 8 * 64 + threadIdx_x % 32 * 2 + 2048 + 2]
            T.attr(0, "async_scope", 1)
            for ax0_ax1_fused_2 in T.serial(3):
                B_shared_dyn_1[threadIdx_x // 32 * 768 + (blockIdx_x % 8 * 3 + (threadIdx_x % 32 * 3 + ax0_ax1_fused_2) // 32) // 2 * 64 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 8 // 4 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 * 3 + ax0_ax1_fused_2) // 8) % 8 * 4 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 4 + 3072 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64)] = B_1[threadIdx_x // 32 * 768 + blockIdx_x % 8 * 96 + threadIdx_x % 32 * 3 + ax0_ax1_fused_2 + 3072]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + threadIdx_x % 2 * 2 + 512:threadIdx_x // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + threadIdx_x % 2 * 2 + 512 + 2] = A_1[threadIdx_x // 32 * 512 + blockIdx_x // 8 * 64 + threadIdx_x % 32 * 2 + 4096:threadIdx_x // 32 * 512 + blockIdx_x // 8 * 64 + threadIdx_x % 32 * 2 + 4096 + 2]
            T.attr(0, "async_scope", 1)
            for ax0_ax1_fused_2 in T.serial(3):
                B_shared_dyn_1[threadIdx_x // 32 * 768 + (blockIdx_x % 8 * 3 + (threadIdx_x % 32 * 3 + ax0_ax1_fused_2) // 32) // 2 * 64 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 8 // 4 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 * 3 + ax0_ax1_fused_2) // 8) % 8 * 4 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 4 + 6144 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64)] = B_1[threadIdx_x // 32 * 768 + blockIdx_x % 8 * 96 + threadIdx_x % 32 * 3 + ax0_ax1_fused_2 + 6144]
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 2)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4:threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 4]
            for ax1_0 in T.serial(3):
                cse_var_1: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_1:cse_var_1 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_1) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_1) // 8) % 8 * 4 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64):(blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_1) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_1) // 8) % 8 * 4 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64) + 4]
        for k_0 in T.serial(765):
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    A_shared_dyn_1[(k_0 + 3) % 4 * 256 + threadIdx_x // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + threadIdx_x % 2 * 2:(k_0 + 3) % 4 * 256 + threadIdx_x // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + threadIdx_x % 2 * 2 + 2] = A_1[k_0 * 2048 + threadIdx_x // 32 * 512 + blockIdx_x // 8 * 64 + threadIdx_x % 32 * 2 + 6144:k_0 * 2048 + threadIdx_x // 32 * 512 + blockIdx_x // 8 * 64 + threadIdx_x % 32 * 2 + 6144 + 2]
                T.attr(0, "async_scope", 1)
                for ax0_ax1_fused_2 in T.serial(3):
                    B_shared_dyn_1[(k_0 + 3) % 4 * 3072 + threadIdx_x // 32 * 768 + (blockIdx_x % 8 * 3 + (threadIdx_x % 32 * 3 + ax0_ax1_fused_2) // 32) // 2 * 64 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 8 // 4 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 * 3 + ax0_ax1_fused_2) // 8) % 8 * 4 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 4 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64)] = B_1[k_0 * 3072 + threadIdx_x // 32 * 768 + blockIdx_x % 8 * 96 + threadIdx_x % 32 * 3 + ax0_ax1_fused_2 + 9216]
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 2)
                A_shared_dyn_local_1[1] = A_shared_dyn_1[k_0 % 4 * 256 + threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 64:k_0 % 4 * 256 + threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 64 + 4]
                for ax1_0 in T.serial(3):
                    cse_var_2: T.int32 = ax1_0 * 4
                    B_shared_dyn_local_1[cse_var_2 + 12:cse_var_2 + 12 + 4] = B_shared_dyn_1[k_0 % 4 * 3072 + (blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_2) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_2) // 8) % 8 * 4 + 768 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64):k_0 % 4 * 3072 + (blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_2) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_2) // 8) % 8 * 4 + 768 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64) + 4]
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
                A_shared_dyn_local_1[0] = A_shared_dyn_1[k_0 % 4 * 256 + threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 128:k_0 % 4 * 256 + threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 128 + 4]
                for ax1_0 in T.serial(3):
                    cse_var_3: T.int32 = ax1_0 * 4
                    B_shared_dyn_local_1[cse_var_3:cse_var_3 + 4] = B_shared_dyn_1[k_0 % 4 * 3072 + (blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_3) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_3) // 8) % 8 * 4 + 1536 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64):k_0 % 4 * 3072 + (blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_3) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_3) // 8) % 8 * 4 + 1536 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64) + 4]
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
                A_shared_dyn_local_1[1] = A_shared_dyn_1[k_0 % 4 * 256 + threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 192:k_0 % 4 * 256 + threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 192 + 4]
                for ax1_0 in T.serial(3):
                    cse_var_4: T.int32 = ax1_0 * 4
                    B_shared_dyn_local_1[cse_var_4 + 12:cse_var_4 + 12 + 4] = B_shared_dyn_1[k_0 % 4 * 3072 + (blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_4) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_4) // 8) % 8 * 4 + 2304 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64):k_0 % 4 * 3072 + (blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_4) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_4) // 8) % 8 * 4 + 2304 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64) + 4]
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
            A_shared_dyn_local_1[0] = A_shared_dyn_1[(k_0 + 1) % 4 * 256 + threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4:(k_0 + 1) % 4 * 256 + threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 4]
            for ax1_0 in T.serial(3):
                cse_var_5: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_5:cse_var_5 + 4] = B_shared_dyn_1[(k_0 + 1) % 4 * 3072 + (blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_5) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_5) // 8) % 8 * 4 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64):(k_0 + 1) % 4 * 3072 + (blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_5) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_5) // 8) % 8 * 4 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64) + 4]
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
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 320:threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 320 + 4]
            for ax1_0 in T.serial(3):
                cse_var_6: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_6 + 12:cse_var_6 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_6) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_6) // 8) % 8 * 4 + 3840 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64):(blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_6) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_6) // 8) % 8 * 4 + 3840 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64) + 4]
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
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 384:threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 384 + 4]
            for ax1_0 in T.serial(3):
                cse_var_7: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_7:cse_var_7 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_7) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_7) // 8) % 8 * 4 + 4608 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64):(blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_7) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_7) // 8) % 8 * 4 + 4608 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64) + 4]
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
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 448:threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 448 + 4]
            for ax1_0 in T.serial(3):
                cse_var_8: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_8 + 12:cse_var_8 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_8) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_8) // 8) % 8 * 4 + 5376 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64):(blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_8) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_8) // 8) % 8 * 4 + 5376 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64) + 4]
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
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 512:threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 512 + 4]
        for ax1_0 in T.serial(3):
            cse_var_9: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_9:cse_var_9 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_9) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_9) // 8) % 8 * 4 + 6144 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64):(blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_9) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_9) // 8) % 8 * 4 + 6144 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64) + 4]
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
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 576:threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 576 + 4]
            for ax1_0 in T.serial(3):
                cse_var_10: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_10 + 12:cse_var_10 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_10) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_10) // 8) % 8 * 4 + 6912 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64):(blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_10) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_10) // 8) % 8 * 4 + 6912 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64) + 4]
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
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 640:threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 640 + 4]
            for ax1_0 in T.serial(3):
                cse_var_11: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_11:cse_var_11 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_11) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_11) // 8) % 8 * 4 + 7680 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64):(blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_11) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_11) // 8) % 8 * 4 + 7680 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64) + 4]
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
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 704:threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 704 + 4]
            for ax1_0 in T.serial(3):
                cse_var_12: T.int32 = ax1_0 * 4
                B_shared_dyn_local_1[cse_var_12 + 12:cse_var_12 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_12) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_12) // 8) % 8 * 4 + 8448 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64):(blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_12) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_12) // 8) % 8 * 4 + 8448 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64) + 4]
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
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 768:threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 768 + 4]
        for ax1_0 in T.serial(3):
            cse_var_13: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_13:cse_var_13 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_13) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_13) // 8) % 8 * 4 + 9216 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64):(blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_13) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_13) // 8) % 8 * 4 + 9216 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64) + 4]
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
        A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 832:threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 832 + 4]
        for ax1_0 in T.serial(3):
            cse_var_14: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_14 + 12:cse_var_14 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_14) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_14) // 8) % 8 * 4 + 9984 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64):(blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_14) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_14) // 8) % 8 * 4 + 9984 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64) + 4]
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
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 896:threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 896 + 4]
        for ax1_0 in T.serial(3):
            cse_var_15: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_15:cse_var_15 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_15) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_15) // 8) % 8 * 4 + 10752 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64):(blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_15) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_15) // 8) % 8 * 4 + 10752 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64) + 4]
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
        A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 960:threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + threadIdx_x % 64 // 32 * 8 + threadIdx_x % 4 // 2 * 4 + 960 + 4]
        for ax1_0 in T.serial(3):
            cse_var_16: T.int32 = ax1_0 * 4
            B_shared_dyn_local_1[cse_var_16 + 12:cse_var_16 + 12 + 4] = B_shared_dyn_1[(blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_16) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_16) // 8) % 8 * 4 + 11520 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64):(blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_16) // 64 * 64 + (threadIdx_x % 32 // 4 + ax1_0) % 2 * 32 + (blockIdx_x % 8 * 4 + (threadIdx_x % 32 // 4 * 12 + cse_var_16) // 8) % 8 * 4 + 11520 - T.max(0, T.min(blockIdx_x % 8 * 96 - blockIdx_x % 2 * 32, blockIdx_x % 8 * 96) // 64 * 64) + 4]
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
        for ax1_0 in T.serial(3):
            cse_var_17: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 8 * 49152 + threadIdx_x // 32 * 12288 + threadIdx_x % 4 * 3072 + blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_17:blockIdx_x // 8 * 49152 + threadIdx_x // 32 * 12288 + threadIdx_x % 4 * 3072 + blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_17 + 4] = Y_local_1[cse_var_17:cse_var_17 + 4]
        for ax1_0 in T.serial(3):
            cse_var_18: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 8 * 49152 + threadIdx_x // 32 * 12288 + threadIdx_x % 4 * 3072 + blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_18 + 768:blockIdx_x // 8 * 49152 + threadIdx_x // 32 * 12288 + threadIdx_x % 4 * 3072 + blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_18 + 768 + 4] = Y_local_1[cse_var_18 + 12:cse_var_18 + 12 + 4]
        for ax1_0 in T.serial(3):
            cse_var_19: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 8 * 49152 + threadIdx_x // 32 * 12288 + threadIdx_x % 4 * 3072 + blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_19 + 1536:blockIdx_x // 8 * 49152 + threadIdx_x // 32 * 12288 + threadIdx_x % 4 * 3072 + blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_19 + 1536 + 4] = Y_local_1[cse_var_19 + 24:cse_var_19 + 24 + 4]
        for ax1_0 in T.serial(3):
            cse_var_20: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 8 * 49152 + threadIdx_x // 32 * 12288 + threadIdx_x % 4 * 3072 + blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_20 + 2304:blockIdx_x // 8 * 49152 + threadIdx_x // 32 * 12288 + threadIdx_x % 4 * 3072 + blockIdx_x % 8 * 96 + threadIdx_x % 32 // 4 * 12 + cse_var_20 + 2304 + 4] = Y_local_1[cse_var_20 + 36:cse_var_20 + 36 + 4]
    

