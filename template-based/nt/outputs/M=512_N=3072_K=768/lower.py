# from tvm.script import tir as T
@tvm.script.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer[(768, 512), "float32"], B: T.Buffer[(768, 3072), "float32"], Y: T.Buffer[(512, 3072), "float32"]):
        # function attr dict
        T.func_attr({"global_symbol": "main", "tir.noalias": True})
        # var definition
        threadIdx_x = T.env_thread("threadIdx.x")
        blockIdx_x = T.env_thread("blockIdx.x")
        # buffer definition
        A_1 = T.buffer_decl([393216], dtype="float32", data=A.data)
        B_1 = T.buffer_decl([2359296], dtype="float32", data=B.data)
        Y_1 = T.buffer_decl([1572864], dtype="float32", data=Y.data)
        # body
        T.launch_thread(blockIdx_x, 64)
        Y_local = T.allocate([64], "float32", "local")
        Y_local_1 = T.buffer_decl([64], dtype="float32", data=Y_local, scope="local")
        A_shared_dyn = T.allocate([4096], "float32", "shared.dyn")
        A_shared_dyn_1 = T.buffer_decl([4096], dtype="float32", data=A_shared_dyn, scope="shared.dyn")
        B_shared_dyn = T.allocate([6144], "float32", "shared.dyn")
        B_shared_dyn_1 = T.buffer_decl([6144], dtype="float32", data=B_shared_dyn, scope="shared.dyn")
        A_shared_dyn_local = T.allocate([8], "float32x4", "local")
        A_shared_dyn_local_1 = T.buffer_decl([8], dtype="float32x4", data=A_shared_dyn_local, scope="local")
        B_shared_dyn_local = T.allocate([8], "float32", "local")
        B_shared_dyn_local_1 = T.buffer_decl([8], dtype="float32", data=B_shared_dyn_local, scope="local")
        T.launch_thread(threadIdx_x, 384)
        Y_local_1[0] = T.float32(0)
        Y_local_1[4] = T.float32(0)
        Y_local_1[8] = T.float32(0)
        Y_local_1[12] = T.float32(0)
        Y_local_1[16] = T.float32(0)
        Y_local_1[20] = T.float32(0)
        Y_local_1[24] = T.float32(0)
        Y_local_1[28] = T.float32(0)
        Y_local_1[32] = T.float32(0)
        Y_local_1[36] = T.float32(0)
        Y_local_1[40] = T.float32(0)
        Y_local_1[44] = T.float32(0)
        Y_local_1[48] = T.float32(0)
        Y_local_1[52] = T.float32(0)
        Y_local_1[56] = T.float32(0)
        Y_local_1[60] = T.float32(0)
        Y_local_1[1] = T.float32(0)
        Y_local_1[5] = T.float32(0)
        Y_local_1[9] = T.float32(0)
        Y_local_1[13] = T.float32(0)
        Y_local_1[17] = T.float32(0)
        Y_local_1[21] = T.float32(0)
        Y_local_1[25] = T.float32(0)
        Y_local_1[29] = T.float32(0)
        Y_local_1[33] = T.float32(0)
        Y_local_1[37] = T.float32(0)
        Y_local_1[41] = T.float32(0)
        Y_local_1[45] = T.float32(0)
        Y_local_1[49] = T.float32(0)
        Y_local_1[53] = T.float32(0)
        Y_local_1[57] = T.float32(0)
        Y_local_1[61] = T.float32(0)
        Y_local_1[2] = T.float32(0)
        Y_local_1[6] = T.float32(0)
        Y_local_1[10] = T.float32(0)
        Y_local_1[14] = T.float32(0)
        Y_local_1[18] = T.float32(0)
        Y_local_1[22] = T.float32(0)
        Y_local_1[26] = T.float32(0)
        Y_local_1[30] = T.float32(0)
        Y_local_1[34] = T.float32(0)
        Y_local_1[38] = T.float32(0)
        Y_local_1[42] = T.float32(0)
        Y_local_1[46] = T.float32(0)
        Y_local_1[50] = T.float32(0)
        Y_local_1[54] = T.float32(0)
        Y_local_1[58] = T.float32(0)
        Y_local_1[62] = T.float32(0)
        Y_local_1[3] = T.float32(0)
        Y_local_1[7] = T.float32(0)
        Y_local_1[11] = T.float32(0)
        Y_local_1[15] = T.float32(0)
        Y_local_1[19] = T.float32(0)
        Y_local_1[23] = T.float32(0)
        Y_local_1[27] = T.float32(0)
        Y_local_1[31] = T.float32(0)
        Y_local_1[35] = T.float32(0)
        Y_local_1[39] = T.float32(0)
        Y_local_1[43] = T.float32(0)
        Y_local_1[47] = T.float32(0)
        Y_local_1[51] = T.float32(0)
        Y_local_1[55] = T.float32(0)
        Y_local_1[59] = T.float32(0)
        Y_local_1[63] = T.float32(0)
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                for ax0_ax1_fused_2_s in T.serial(3):
                    if threadIdx_x * 3 + ax0_ax1_fused_2_s < 1024:
                        A_shared_dyn_1[(threadIdx_x * 3 + ax0_ax1_fused_2_s) // 32 * 32 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 8 // 4 * 16 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 32 // 8 * 4 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 4] = A_1[(threadIdx_x * 3 + ax0_ax1_fused_2_s) // 128 * 512 + blockIdx_x // 16 * 128 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 128]
            T.attr(0, "async_scope", 1)
            for ax0_ax1_fused_2 in T.serial(4):
                B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + ax0_ax1_fused_2] = B_1[threadIdx_x // 48 * 3072 + blockIdx_x % 16 * 192 + threadIdx_x % 48 * 4 + ax0_ax1_fused_2]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                for ax0_ax1_fused_2_s in T.serial(3):
                    if threadIdx_x * 3 + ax0_ax1_fused_2_s < 1024:
                        A_shared_dyn_1[(threadIdx_x * 3 + ax0_ax1_fused_2_s) // 32 * 32 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 8 // 4 * 16 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 32 // 8 * 4 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 4 + 1024] = A_1[(threadIdx_x * 3 + ax0_ax1_fused_2_s) // 128 * 512 + blockIdx_x // 16 * 128 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 128 + 4096]
            T.attr(0, "async_scope", 1)
            for ax0_ax1_fused_2 in T.serial(4):
                B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + ax0_ax1_fused_2 + 1536] = B_1[threadIdx_x // 48 * 3072 + blockIdx_x % 16 * 192 + threadIdx_x % 48 * 4 + ax0_ax1_fused_2 + 24576]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                for ax0_ax1_fused_2_s in T.serial(3):
                    if threadIdx_x * 3 + ax0_ax1_fused_2_s < 1024:
                        A_shared_dyn_1[(threadIdx_x * 3 + ax0_ax1_fused_2_s) // 32 * 32 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 8 // 4 * 16 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 32 // 8 * 4 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 4 + 2048] = A_1[(threadIdx_x * 3 + ax0_ax1_fused_2_s) // 128 * 512 + blockIdx_x // 16 * 128 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 128 + 8192]
            T.attr(0, "async_scope", 1)
            for ax0_ax1_fused_2 in T.serial(4):
                B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + ax0_ax1_fused_2 + 3072] = B_1[threadIdx_x // 48 * 3072 + blockIdx_x % 16 * 192 + threadIdx_x % 48 * 4 + ax0_ax1_fused_2 + 49152]
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 2)
            for ax1_0 in T.serial(4):
                A_shared_dyn_local_1[ax1_0] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4:threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4:threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 4]
        for k_0 in T.serial(93):
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    for ax0_ax1_fused_2_s in T.serial(3):
                        if threadIdx_x * 3 + ax0_ax1_fused_2_s < 1024:
                            A_shared_dyn_1[(k_0 + 3) % 4 * 1024 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) // 32 * 32 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 8 // 4 * 16 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 32 // 8 * 4 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 4] = A_1[k_0 * 4096 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) // 128 * 512 + blockIdx_x // 16 * 128 + (threadIdx_x * 3 + ax0_ax1_fused_2_s) % 128 + 12288]
                T.attr(0, "async_scope", 1)
                for ax0_ax1_fused_2 in T.serial(4):
                    B_shared_dyn_1[(k_0 + 3) % 4 * 1536 + threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + ax0_ax1_fused_2] = B_1[k_0 * 24576 + threadIdx_x // 48 * 3072 + blockIdx_x % 16 * 192 + threadIdx_x % 48 * 4 + ax0_ax1_fused_2 + 73728]
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 2)
                for ax1_0 in T.serial(4):
                    A_shared_dyn_local_1[ax1_0 + 4] = A_shared_dyn_1[k_0 % 4 * 1024 + threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 128:k_0 % 4 * 1024 + threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 128 + 4]
                B_shared_dyn_local_1[4:8] = B_shared_dyn_1[k_0 % 4 * 1536 + threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 192:k_0 % 4 * 1536 + threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 192 + 4]
                Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[3], 4)
                for ax1_0 in T.serial(4):
                    A_shared_dyn_local_1[ax1_0] = A_shared_dyn_1[k_0 % 4 * 1024 + threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 256:k_0 % 4 * 1024 + threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 256 + 4]
                B_shared_dyn_local_1[0:4] = B_shared_dyn_1[k_0 % 4 * 1536 + threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 384:k_0 % 4 * 1536 + threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 384 + 4]
                Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[7], 4)
                for ax1_0 in T.serial(4):
                    A_shared_dyn_local_1[ax1_0 + 4] = A_shared_dyn_1[k_0 % 4 * 1024 + threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 384:k_0 % 4 * 1024 + threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 384 + 4]
                B_shared_dyn_local_1[4:8] = B_shared_dyn_1[k_0 % 4 * 1536 + threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 576:k_0 % 4 * 1536 + threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 576 + 4]
                Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[3], 4)
                for ax1_0 in T.serial(4):
                    A_shared_dyn_local_1[ax1_0] = A_shared_dyn_1[k_0 % 4 * 1024 + threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 512:k_0 % 4 * 1024 + threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 512 + 4]
                B_shared_dyn_local_1[0:4] = B_shared_dyn_1[k_0 % 4 * 1536 + threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 768:k_0 % 4 * 1536 + threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 768 + 4]
                Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[7], 4)
                for ax1_0 in T.serial(4):
                    A_shared_dyn_local_1[ax1_0 + 4] = A_shared_dyn_1[k_0 % 4 * 1024 + threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 640:k_0 % 4 * 1024 + threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 640 + 4]
                B_shared_dyn_local_1[4:8] = B_shared_dyn_1[k_0 % 4 * 1536 + threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 960:k_0 % 4 * 1536 + threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 960 + 4]
                Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[3], 4)
                for ax1_0 in T.serial(4):
                    A_shared_dyn_local_1[ax1_0] = A_shared_dyn_1[k_0 % 4 * 1024 + threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 768:k_0 % 4 * 1024 + threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 768 + 4]
                B_shared_dyn_local_1[0:4] = B_shared_dyn_1[k_0 % 4 * 1536 + threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 1152:k_0 % 4 * 1536 + threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 1152 + 4]
                Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[7], 4)
                for ax1_0 in T.serial(4):
                    A_shared_dyn_local_1[ax1_0 + 4] = A_shared_dyn_1[k_0 % 4 * 1024 + threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 896:k_0 % 4 * 1024 + threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 896 + 4]
                B_shared_dyn_local_1[4:8] = B_shared_dyn_1[k_0 % 4 * 1536 + threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 1344:k_0 % 4 * 1536 + threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 1344 + 4]
                Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[3], 4)
            for ax1_0 in T.serial(4):
                A_shared_dyn_local_1[ax1_0] = A_shared_dyn_1[(k_0 + 1) % 4 * 1024 + threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4:(k_0 + 1) % 4 * 1024 + threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[(k_0 + 1) % 4 * 1536 + threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4:(k_0 + 1) % 4 * 1536 + threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[7], 4)
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 1)
            for ax1_0 in T.serial(4):
                A_shared_dyn_local_1[ax1_0 + 4] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 1152:threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 1152 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 1728:threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 1728 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[3], 4)
            for ax1_0 in T.serial(4):
                A_shared_dyn_local_1[ax1_0] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 1280:threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 1280 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 1920:threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 1920 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[7], 4)
            for ax1_0 in T.serial(4):
                A_shared_dyn_local_1[ax1_0 + 4] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 1408:threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 1408 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 2112:threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 2112 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[3], 4)
            for ax1_0 in T.serial(4):
                A_shared_dyn_local_1[ax1_0] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 1536:threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 1536 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 2304:threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 2304 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[7], 4)
            for ax1_0 in T.serial(4):
                A_shared_dyn_local_1[ax1_0 + 4] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 1664:threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 1664 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 2496:threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 2496 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[3], 4)
            for ax1_0 in T.serial(4):
                A_shared_dyn_local_1[ax1_0] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 1792:threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 1792 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 2688:threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 2688 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[7], 4)
            for ax1_0 in T.serial(4):
                A_shared_dyn_local_1[ax1_0 + 4] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 1920:threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 1920 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 2880:threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 2880 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[3], 4)
        for ax1_0 in T.serial(4):
            A_shared_dyn_local_1[ax1_0] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 2048:threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 2048 + 4]
        B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 3072:threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 3072 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[7], 4)
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 0)
            for ax1_0 in T.serial(4):
                A_shared_dyn_local_1[ax1_0 + 4] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 2176:threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 2176 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 3264:threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 3264 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[3], 4)
            for ax1_0 in T.serial(4):
                A_shared_dyn_local_1[ax1_0] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 2304:threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 2304 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 3456:threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 3456 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[7], 4)
            for ax1_0 in T.serial(4):
                A_shared_dyn_local_1[ax1_0 + 4] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 2432:threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 2432 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 3648:threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 3648 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[3], 4)
            for ax1_0 in T.serial(4):
                A_shared_dyn_local_1[ax1_0] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 2560:threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 2560 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 3840:threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 3840 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[7], 4)
            for ax1_0 in T.serial(4):
                A_shared_dyn_local_1[ax1_0 + 4] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 2688:threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 2688 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 4032:threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 4032 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[3], 4)
            for ax1_0 in T.serial(4):
                A_shared_dyn_local_1[ax1_0] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 2816:threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 2816 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 4224:threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 4224 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[7], 4)
            for ax1_0 in T.serial(4):
                A_shared_dyn_local_1[ax1_0 + 4] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 2944:threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 2944 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 4416:threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 4416 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[3], 4)
        for ax1_0 in T.serial(4):
            A_shared_dyn_local_1[ax1_0] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 3072:threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 3072 + 4]
        B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 4608:threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 4608 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[7], 4)
        for ax1_0 in T.serial(4):
            A_shared_dyn_local_1[ax1_0 + 4] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 3200:threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 3200 + 4]
        B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 4800:threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 4800 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[3], 4)
        for ax1_0 in T.serial(4):
            A_shared_dyn_local_1[ax1_0] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 3328:threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 3328 + 4]
        B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 4992:threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 4992 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[7], 4)
        for ax1_0 in T.serial(4):
            A_shared_dyn_local_1[ax1_0 + 4] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 3456:threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 3456 + 4]
        B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 5184:threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 5184 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[3], 4)
        for ax1_0 in T.serial(4):
            A_shared_dyn_local_1[ax1_0] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 3584:threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 3584 + 4]
        B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 5376:threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 5376 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[7], 4)
        for ax1_0 in T.serial(4):
            A_shared_dyn_local_1[ax1_0 + 4] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 3712:threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 3712 + 4]
        B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 5568:threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 5568 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[3], 4)
        for ax1_0 in T.serial(4):
            A_shared_dyn_local_1[ax1_0] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 3840:threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 3840 + 4]
        B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 5760:threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 5760 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[7], 4)
        for ax1_0 in T.serial(4):
            A_shared_dyn_local_1[ax1_0 + 4] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 3968:threadIdx_x % 64 // 16 * 32 + ax1_0 % 2 * 16 + threadIdx_x % 2 * 8 + ax1_0 // 2 * 4 + 3968 + 4]
        B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 5952:threadIdx_x // 128 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 128 // 64 * 16 + threadIdx_x % 16 // 4 * 4 + 5952 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[2] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[3] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[16:32:4] = Y_local_1[16:32:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[32:48:4] = Y_local_1[32:48:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[48:64:4] = Y_local_1[48:64:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[17:33:4] = Y_local_1[17:33:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[33:49:4] = Y_local_1[33:49:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[49:65:4] = Y_local_1[49:65:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[18:34:4] = Y_local_1[18:34:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[34:50:4] = Y_local_1[34:50:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[50:66:4] = Y_local_1[50:66:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[4] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[19:35:4] = Y_local_1[19:35:4] + A_shared_dyn_local_1[5] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[35:51:4] = Y_local_1[35:51:4] + A_shared_dyn_local_1[6] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[51:67:4] = Y_local_1[51:67:4] + A_shared_dyn_local_1[7] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_1[blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4:blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 4] = Y_local_1[0:4]
        Y_1[blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 3072:blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 3072 + 4] = Y_local_1[4:8]
        Y_1[blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 6144:blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 6144 + 4] = Y_local_1[8:12]
        Y_1[blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 9216:blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 9216 + 4] = Y_local_1[12:16]
        Y_1[blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 12288:blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 12288 + 4] = Y_local_1[16:20]
        Y_1[blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 15360:blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 15360 + 4] = Y_local_1[20:24]
        Y_1[blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 18432:blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 18432 + 4] = Y_local_1[24:28]
        Y_1[blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 21504:blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 21504 + 4] = Y_local_1[28:32]
        Y_1[blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 24576:blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 24576 + 4] = Y_local_1[32:36]
        Y_1[blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 27648:blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 27648 + 4] = Y_local_1[36:40]
        Y_1[blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 30720:blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 30720 + 4] = Y_local_1[40:44]
        Y_1[blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 33792:blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 33792 + 4] = Y_local_1[44:48]
        Y_1[blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 36864:blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 36864 + 4] = Y_local_1[48:52]
        Y_1[blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 39936:blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 39936 + 4] = Y_local_1[52:56]
        Y_1[blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 43008:blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 43008 + 4] = Y_local_1[56:60]
        Y_1[blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 46080:blockIdx_x // 16 * 393216 + threadIdx_x % 64 // 16 * 98304 + threadIdx_x % 2 * 49152 + blockIdx_x % 16 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 16 // 2 * 4 + 46080 + 4] = Y_local_1[60:64]
    

