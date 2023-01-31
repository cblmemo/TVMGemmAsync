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
        T.launch_thread(blockIdx_x, 54)
        Y_local = T.allocate([64], "float32", "local")
        Y_local_1 = T.buffer_decl([64], dtype="float32", data=Y_local, scope="local")
        A_shared_dyn = T.allocate([3072], "float32", "shared.dyn")
        A_shared_dyn_1 = T.buffer_decl([3072], dtype="float32", data=A_shared_dyn, scope="shared.dyn")
        B_shared_dyn = T.allocate([4608], "float32", "shared.dyn")
        B_shared_dyn_1 = T.buffer_decl([4608], dtype="float32", data=B_shared_dyn, scope="shared.dyn")
        A_shared_dyn_local = T.allocate([2], "float32x4", "local")
        A_shared_dyn_local_1 = T.buffer_decl([2], dtype="float32x4", data=A_shared_dyn_local, scope="local")
        B_shared_dyn_local = T.allocate([32], "float32", "local")
        B_shared_dyn_local_1 = T.buffer_decl([32], dtype="float32", data=B_shared_dyn_local, scope="local")
        T.launch_thread(threadIdx_x, 384)
        Y_local_1[0] = T.float32(0)
        Y_local_1[16] = T.float32(0)
        Y_local_1[32] = T.float32(0)
        Y_local_1[48] = T.float32(0)
        Y_local_1[1] = T.float32(0)
        Y_local_1[17] = T.float32(0)
        Y_local_1[33] = T.float32(0)
        Y_local_1[49] = T.float32(0)
        Y_local_1[2] = T.float32(0)
        Y_local_1[18] = T.float32(0)
        Y_local_1[34] = T.float32(0)
        Y_local_1[50] = T.float32(0)
        Y_local_1[3] = T.float32(0)
        Y_local_1[19] = T.float32(0)
        Y_local_1[35] = T.float32(0)
        Y_local_1[51] = T.float32(0)
        Y_local_1[4] = T.float32(0)
        Y_local_1[20] = T.float32(0)
        Y_local_1[36] = T.float32(0)
        Y_local_1[52] = T.float32(0)
        Y_local_1[5] = T.float32(0)
        Y_local_1[21] = T.float32(0)
        Y_local_1[37] = T.float32(0)
        Y_local_1[53] = T.float32(0)
        Y_local_1[6] = T.float32(0)
        Y_local_1[22] = T.float32(0)
        Y_local_1[38] = T.float32(0)
        Y_local_1[54] = T.float32(0)
        Y_local_1[7] = T.float32(0)
        Y_local_1[23] = T.float32(0)
        Y_local_1[39] = T.float32(0)
        Y_local_1[55] = T.float32(0)
        Y_local_1[8] = T.float32(0)
        Y_local_1[24] = T.float32(0)
        Y_local_1[40] = T.float32(0)
        Y_local_1[56] = T.float32(0)
        Y_local_1[9] = T.float32(0)
        Y_local_1[25] = T.float32(0)
        Y_local_1[41] = T.float32(0)
        Y_local_1[57] = T.float32(0)
        Y_local_1[10] = T.float32(0)
        Y_local_1[26] = T.float32(0)
        Y_local_1[42] = T.float32(0)
        Y_local_1[58] = T.float32(0)
        Y_local_1[11] = T.float32(0)
        Y_local_1[27] = T.float32(0)
        Y_local_1[43] = T.float32(0)
        Y_local_1[59] = T.float32(0)
        Y_local_1[12] = T.float32(0)
        Y_local_1[28] = T.float32(0)
        Y_local_1[44] = T.float32(0)
        Y_local_1[60] = T.float32(0)
        Y_local_1[13] = T.float32(0)
        Y_local_1[29] = T.float32(0)
        Y_local_1[45] = T.float32(0)
        Y_local_1[61] = T.float32(0)
        Y_local_1[14] = T.float32(0)
        Y_local_1[30] = T.float32(0)
        Y_local_1[46] = T.float32(0)
        Y_local_1[62] = T.float32(0)
        Y_local_1[15] = T.float32(0)
        Y_local_1[31] = T.float32(0)
        Y_local_1[47] = T.float32(0)
        Y_local_1[63] = T.float32(0)
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + threadIdx_x % 2 * 2:threadIdx_x // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + threadIdx_x % 2 * 2 + 2] = A_1[threadIdx_x // 64 * 1152 + blockIdx_x // 6 * 128 + threadIdx_x % 64 * 2:threadIdx_x // 64 * 1152 + blockIdx_x // 6 * 128 + threadIdx_x % 64 * 2 + 2]
            T.attr(0, "async_scope", 1)
            for ax0_ax1_fused_2 in T.serial(3):
                B_shared_dyn_1[(threadIdx_x * 3 + ax0_ax1_fused_2) // 64 * 64 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 8 // 4 * 32 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 64 // 8 * 4 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 4] = B_1[threadIdx_x // 64 * 1152 + blockIdx_x % 6 * 192 + threadIdx_x % 64 * 3 + ax0_ax1_fused_2]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + threadIdx_x % 2 * 2 + 768:threadIdx_x // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + threadIdx_x % 2 * 2 + 768 + 2] = A_1[threadIdx_x // 64 * 1152 + blockIdx_x // 6 * 128 + threadIdx_x % 64 * 2 + 6912:threadIdx_x // 64 * 1152 + blockIdx_x // 6 * 128 + threadIdx_x % 64 * 2 + 6912 + 2]
            T.attr(0, "async_scope", 1)
            for ax0_ax1_fused_2 in T.serial(3):
                B_shared_dyn_1[(threadIdx_x * 3 + ax0_ax1_fused_2) // 64 * 64 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 8 // 4 * 32 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 64 // 8 * 4 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 4 + 1152] = B_1[threadIdx_x // 64 * 1152 + blockIdx_x % 6 * 192 + threadIdx_x % 64 * 3 + ax0_ax1_fused_2 + 6912]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + threadIdx_x % 2 * 2 + 1536:threadIdx_x // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + threadIdx_x % 2 * 2 + 1536 + 2] = A_1[threadIdx_x // 64 * 1152 + blockIdx_x // 6 * 128 + threadIdx_x % 64 * 2 + 13824:threadIdx_x // 64 * 1152 + blockIdx_x // 6 * 128 + threadIdx_x % 64 * 2 + 13824 + 2]
            T.attr(0, "async_scope", 1)
            for ax0_ax1_fused_2 in T.serial(3):
                B_shared_dyn_1[(threadIdx_x * 3 + ax0_ax1_fused_2) // 64 * 64 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 8 // 4 * 32 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 64 // 8 * 4 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 4 + 2304] = B_1[threadIdx_x // 64 * 1152 + blockIdx_x % 6 * 192 + threadIdx_x % 64 * 3 + ax0_ax1_fused_2 + 13824]
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 2)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4:threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 4]
            for ax1_0 in T.serial(4):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4:threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 4]
        for k_0 in T.serial(189):
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    A_shared_dyn_1[(k_0 + 3) % 4 * 768 + threadIdx_x // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + threadIdx_x % 2 * 2:(k_0 + 3) % 4 * 768 + threadIdx_x // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + threadIdx_x % 2 * 2 + 2] = A_1[k_0 * 6912 + threadIdx_x // 64 * 1152 + blockIdx_x // 6 * 128 + threadIdx_x % 64 * 2 + 20736:k_0 * 6912 + threadIdx_x // 64 * 1152 + blockIdx_x // 6 * 128 + threadIdx_x % 64 * 2 + 20736 + 2]
                T.attr(0, "async_scope", 1)
                for ax0_ax1_fused_2 in T.serial(3):
                    B_shared_dyn_1[(k_0 + 3) % 4 * 1152 + (threadIdx_x * 3 + ax0_ax1_fused_2) // 64 * 64 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 8 // 4 * 32 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 64 // 8 * 4 + (threadIdx_x * 3 + ax0_ax1_fused_2) % 4] = B_1[k_0 * 6912 + threadIdx_x // 64 * 1152 + blockIdx_x % 6 * 192 + threadIdx_x % 64 * 3 + ax0_ax1_fused_2 + 20736]
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 2)
                A_shared_dyn_local_1[1] = A_shared_dyn_1[k_0 % 4 * 768 + threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 128:k_0 % 4 * 768 + threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 128 + 4]
                for ax1_0 in T.serial(4):
                    B_shared_dyn_local_1[ax1_0 * 4 + 16:ax1_0 * 4 + 16 + 4] = B_shared_dyn_1[k_0 % 4 * 1152 + threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 192:k_0 % 4 * 1152 + threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 192 + 4]
                Y_local_1[0:64:16] = Y_local_1[0:64:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:65:16] = Y_local_1[1:65:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:66:16] = Y_local_1[2:66:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:67:16] = Y_local_1[3:67:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[4:68:16] = Y_local_1[4:68:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[5:69:16] = Y_local_1[5:69:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[6:70:16] = Y_local_1[6:70:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[7:71:16] = Y_local_1[7:71:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[8:72:16] = Y_local_1[8:72:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
                Y_local_1[9:73:16] = Y_local_1[9:73:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
                Y_local_1[10:74:16] = Y_local_1[10:74:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
                Y_local_1[11:75:16] = Y_local_1[11:75:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
                Y_local_1[12:76:16] = Y_local_1[12:76:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[12], 4)
                Y_local_1[13:77:16] = Y_local_1[13:77:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[13], 4)
                Y_local_1[14:78:16] = Y_local_1[14:78:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[14], 4)
                Y_local_1[15:79:16] = Y_local_1[15:79:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[15], 4)
                A_shared_dyn_local_1[0] = A_shared_dyn_1[k_0 % 4 * 768 + threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 256:k_0 % 4 * 768 + threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 256 + 4]
                for ax1_0 in T.serial(4):
                    B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[k_0 % 4 * 1152 + threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 384:k_0 % 4 * 1152 + threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 384 + 4]
                Y_local_1[0:64:16] = Y_local_1[0:64:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[16], 4)
                Y_local_1[1:65:16] = Y_local_1[1:65:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[17], 4)
                Y_local_1[2:66:16] = Y_local_1[2:66:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[18], 4)
                Y_local_1[3:67:16] = Y_local_1[3:67:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[19], 4)
                Y_local_1[4:68:16] = Y_local_1[4:68:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[20], 4)
                Y_local_1[5:69:16] = Y_local_1[5:69:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[21], 4)
                Y_local_1[6:70:16] = Y_local_1[6:70:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[22], 4)
                Y_local_1[7:71:16] = Y_local_1[7:71:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[23], 4)
                Y_local_1[8:72:16] = Y_local_1[8:72:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[24], 4)
                Y_local_1[9:73:16] = Y_local_1[9:73:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[25], 4)
                Y_local_1[10:74:16] = Y_local_1[10:74:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[26], 4)
                Y_local_1[11:75:16] = Y_local_1[11:75:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[27], 4)
                Y_local_1[12:76:16] = Y_local_1[12:76:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[28], 4)
                Y_local_1[13:77:16] = Y_local_1[13:77:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[29], 4)
                Y_local_1[14:78:16] = Y_local_1[14:78:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[30], 4)
                Y_local_1[15:79:16] = Y_local_1[15:79:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[31], 4)
                A_shared_dyn_local_1[1] = A_shared_dyn_1[k_0 % 4 * 768 + threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 384:k_0 % 4 * 768 + threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 384 + 4]
                for ax1_0 in T.serial(4):
                    B_shared_dyn_local_1[ax1_0 * 4 + 16:ax1_0 * 4 + 16 + 4] = B_shared_dyn_1[k_0 % 4 * 1152 + threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 576:k_0 % 4 * 1152 + threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 576 + 4]
                Y_local_1[0:64:16] = Y_local_1[0:64:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:65:16] = Y_local_1[1:65:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:66:16] = Y_local_1[2:66:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:67:16] = Y_local_1[3:67:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[4:68:16] = Y_local_1[4:68:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[5:69:16] = Y_local_1[5:69:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[6:70:16] = Y_local_1[6:70:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[7:71:16] = Y_local_1[7:71:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[8:72:16] = Y_local_1[8:72:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
                Y_local_1[9:73:16] = Y_local_1[9:73:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
                Y_local_1[10:74:16] = Y_local_1[10:74:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
                Y_local_1[11:75:16] = Y_local_1[11:75:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
                Y_local_1[12:76:16] = Y_local_1[12:76:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[12], 4)
                Y_local_1[13:77:16] = Y_local_1[13:77:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[13], 4)
                Y_local_1[14:78:16] = Y_local_1[14:78:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[14], 4)
                Y_local_1[15:79:16] = Y_local_1[15:79:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[15], 4)
                A_shared_dyn_local_1[0] = A_shared_dyn_1[k_0 % 4 * 768 + threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 512:k_0 % 4 * 768 + threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 512 + 4]
                for ax1_0 in T.serial(4):
                    B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[k_0 % 4 * 1152 + threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 768:k_0 % 4 * 1152 + threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 768 + 4]
                Y_local_1[0:64:16] = Y_local_1[0:64:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[16], 4)
                Y_local_1[1:65:16] = Y_local_1[1:65:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[17], 4)
                Y_local_1[2:66:16] = Y_local_1[2:66:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[18], 4)
                Y_local_1[3:67:16] = Y_local_1[3:67:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[19], 4)
                Y_local_1[4:68:16] = Y_local_1[4:68:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[20], 4)
                Y_local_1[5:69:16] = Y_local_1[5:69:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[21], 4)
                Y_local_1[6:70:16] = Y_local_1[6:70:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[22], 4)
                Y_local_1[7:71:16] = Y_local_1[7:71:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[23], 4)
                Y_local_1[8:72:16] = Y_local_1[8:72:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[24], 4)
                Y_local_1[9:73:16] = Y_local_1[9:73:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[25], 4)
                Y_local_1[10:74:16] = Y_local_1[10:74:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[26], 4)
                Y_local_1[11:75:16] = Y_local_1[11:75:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[27], 4)
                Y_local_1[12:76:16] = Y_local_1[12:76:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[28], 4)
                Y_local_1[13:77:16] = Y_local_1[13:77:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[29], 4)
                Y_local_1[14:78:16] = Y_local_1[14:78:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[30], 4)
                Y_local_1[15:79:16] = Y_local_1[15:79:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[31], 4)
                A_shared_dyn_local_1[1] = A_shared_dyn_1[k_0 % 4 * 768 + threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 640:k_0 % 4 * 768 + threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 640 + 4]
                for ax1_0 in T.serial(4):
                    B_shared_dyn_local_1[ax1_0 * 4 + 16:ax1_0 * 4 + 16 + 4] = B_shared_dyn_1[k_0 % 4 * 1152 + threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 960:k_0 % 4 * 1152 + threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 960 + 4]
                Y_local_1[0:64:16] = Y_local_1[0:64:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:65:16] = Y_local_1[1:65:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:66:16] = Y_local_1[2:66:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:67:16] = Y_local_1[3:67:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[4:68:16] = Y_local_1[4:68:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[5:69:16] = Y_local_1[5:69:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[6:70:16] = Y_local_1[6:70:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[7:71:16] = Y_local_1[7:71:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
                Y_local_1[8:72:16] = Y_local_1[8:72:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
                Y_local_1[9:73:16] = Y_local_1[9:73:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
                Y_local_1[10:74:16] = Y_local_1[10:74:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
                Y_local_1[11:75:16] = Y_local_1[11:75:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
                Y_local_1[12:76:16] = Y_local_1[12:76:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[12], 4)
                Y_local_1[13:77:16] = Y_local_1[13:77:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[13], 4)
                Y_local_1[14:78:16] = Y_local_1[14:78:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[14], 4)
                Y_local_1[15:79:16] = Y_local_1[15:79:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[(k_0 + 1) % 4 * 768 + threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4:(k_0 + 1) % 4 * 768 + threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 4]
            for ax1_0 in T.serial(4):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[(k_0 + 1) % 4 * 1152 + threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4:(k_0 + 1) % 4 * 1152 + threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 4]
            Y_local_1[0:64:16] = Y_local_1[0:64:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[16], 4)
            Y_local_1[1:65:16] = Y_local_1[1:65:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[17], 4)
            Y_local_1[2:66:16] = Y_local_1[2:66:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[18], 4)
            Y_local_1[3:67:16] = Y_local_1[3:67:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[19], 4)
            Y_local_1[4:68:16] = Y_local_1[4:68:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[20], 4)
            Y_local_1[5:69:16] = Y_local_1[5:69:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[21], 4)
            Y_local_1[6:70:16] = Y_local_1[6:70:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[22], 4)
            Y_local_1[7:71:16] = Y_local_1[7:71:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[23], 4)
            Y_local_1[8:72:16] = Y_local_1[8:72:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[24], 4)
            Y_local_1[9:73:16] = Y_local_1[9:73:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[25], 4)
            Y_local_1[10:74:16] = Y_local_1[10:74:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[26], 4)
            Y_local_1[11:75:16] = Y_local_1[11:75:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[27], 4)
            Y_local_1[12:76:16] = Y_local_1[12:76:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[28], 4)
            Y_local_1[13:77:16] = Y_local_1[13:77:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[29], 4)
            Y_local_1[14:78:16] = Y_local_1[14:78:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[30], 4)
            Y_local_1[15:79:16] = Y_local_1[15:79:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[31], 4)
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 1)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 896:threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 896 + 4]
            for ax1_0 in T.serial(4):
                B_shared_dyn_local_1[ax1_0 * 4 + 16:ax1_0 * 4 + 16 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 1344:threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 1344 + 4]
            Y_local_1[0:64:16] = Y_local_1[0:64:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:65:16] = Y_local_1[1:65:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:66:16] = Y_local_1[2:66:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:67:16] = Y_local_1[3:67:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:68:16] = Y_local_1[4:68:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:69:16] = Y_local_1[5:69:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:70:16] = Y_local_1[6:70:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:71:16] = Y_local_1[7:71:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[8:72:16] = Y_local_1[8:72:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[9:73:16] = Y_local_1[9:73:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[10:74:16] = Y_local_1[10:74:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[11:75:16] = Y_local_1[11:75:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[12:76:16] = Y_local_1[12:76:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[13:77:16] = Y_local_1[13:77:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[14:78:16] = Y_local_1[14:78:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[15:79:16] = Y_local_1[15:79:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1024:threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1024 + 4]
            for ax1_0 in T.serial(4):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 1536:threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 1536 + 4]
            Y_local_1[0:64:16] = Y_local_1[0:64:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[16], 4)
            Y_local_1[1:65:16] = Y_local_1[1:65:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[17], 4)
            Y_local_1[2:66:16] = Y_local_1[2:66:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[18], 4)
            Y_local_1[3:67:16] = Y_local_1[3:67:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[19], 4)
            Y_local_1[4:68:16] = Y_local_1[4:68:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[20], 4)
            Y_local_1[5:69:16] = Y_local_1[5:69:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[21], 4)
            Y_local_1[6:70:16] = Y_local_1[6:70:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[22], 4)
            Y_local_1[7:71:16] = Y_local_1[7:71:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[23], 4)
            Y_local_1[8:72:16] = Y_local_1[8:72:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[24], 4)
            Y_local_1[9:73:16] = Y_local_1[9:73:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[25], 4)
            Y_local_1[10:74:16] = Y_local_1[10:74:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[26], 4)
            Y_local_1[11:75:16] = Y_local_1[11:75:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[27], 4)
            Y_local_1[12:76:16] = Y_local_1[12:76:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[28], 4)
            Y_local_1[13:77:16] = Y_local_1[13:77:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[29], 4)
            Y_local_1[14:78:16] = Y_local_1[14:78:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[30], 4)
            Y_local_1[15:79:16] = Y_local_1[15:79:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[31], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1152:threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1152 + 4]
            for ax1_0 in T.serial(4):
                B_shared_dyn_local_1[ax1_0 * 4 + 16:ax1_0 * 4 + 16 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 1728:threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 1728 + 4]
            Y_local_1[0:64:16] = Y_local_1[0:64:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:65:16] = Y_local_1[1:65:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:66:16] = Y_local_1[2:66:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:67:16] = Y_local_1[3:67:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:68:16] = Y_local_1[4:68:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:69:16] = Y_local_1[5:69:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:70:16] = Y_local_1[6:70:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:71:16] = Y_local_1[7:71:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[8:72:16] = Y_local_1[8:72:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[9:73:16] = Y_local_1[9:73:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[10:74:16] = Y_local_1[10:74:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[11:75:16] = Y_local_1[11:75:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[12:76:16] = Y_local_1[12:76:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[13:77:16] = Y_local_1[13:77:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[14:78:16] = Y_local_1[14:78:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[15:79:16] = Y_local_1[15:79:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1280:threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1280 + 4]
            for ax1_0 in T.serial(4):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 1920:threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 1920 + 4]
            Y_local_1[0:64:16] = Y_local_1[0:64:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[16], 4)
            Y_local_1[1:65:16] = Y_local_1[1:65:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[17], 4)
            Y_local_1[2:66:16] = Y_local_1[2:66:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[18], 4)
            Y_local_1[3:67:16] = Y_local_1[3:67:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[19], 4)
            Y_local_1[4:68:16] = Y_local_1[4:68:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[20], 4)
            Y_local_1[5:69:16] = Y_local_1[5:69:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[21], 4)
            Y_local_1[6:70:16] = Y_local_1[6:70:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[22], 4)
            Y_local_1[7:71:16] = Y_local_1[7:71:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[23], 4)
            Y_local_1[8:72:16] = Y_local_1[8:72:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[24], 4)
            Y_local_1[9:73:16] = Y_local_1[9:73:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[25], 4)
            Y_local_1[10:74:16] = Y_local_1[10:74:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[26], 4)
            Y_local_1[11:75:16] = Y_local_1[11:75:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[27], 4)
            Y_local_1[12:76:16] = Y_local_1[12:76:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[28], 4)
            Y_local_1[13:77:16] = Y_local_1[13:77:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[29], 4)
            Y_local_1[14:78:16] = Y_local_1[14:78:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[30], 4)
            Y_local_1[15:79:16] = Y_local_1[15:79:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[31], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1408:threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1408 + 4]
            for ax1_0 in T.serial(4):
                B_shared_dyn_local_1[ax1_0 * 4 + 16:ax1_0 * 4 + 16 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 2112:threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 2112 + 4]
            Y_local_1[0:64:16] = Y_local_1[0:64:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:65:16] = Y_local_1[1:65:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:66:16] = Y_local_1[2:66:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:67:16] = Y_local_1[3:67:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:68:16] = Y_local_1[4:68:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:69:16] = Y_local_1[5:69:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:70:16] = Y_local_1[6:70:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:71:16] = Y_local_1[7:71:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[8:72:16] = Y_local_1[8:72:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[9:73:16] = Y_local_1[9:73:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[10:74:16] = Y_local_1[10:74:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[11:75:16] = Y_local_1[11:75:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[12:76:16] = Y_local_1[12:76:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[13:77:16] = Y_local_1[13:77:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[14:78:16] = Y_local_1[14:78:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[15:79:16] = Y_local_1[15:79:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[15], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1536:threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1536 + 4]
        for ax1_0 in T.serial(4):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 2304:threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 2304 + 4]
        Y_local_1[0:64:16] = Y_local_1[0:64:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[16], 4)
        Y_local_1[1:65:16] = Y_local_1[1:65:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[17], 4)
        Y_local_1[2:66:16] = Y_local_1[2:66:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[18], 4)
        Y_local_1[3:67:16] = Y_local_1[3:67:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[19], 4)
        Y_local_1[4:68:16] = Y_local_1[4:68:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[20], 4)
        Y_local_1[5:69:16] = Y_local_1[5:69:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[21], 4)
        Y_local_1[6:70:16] = Y_local_1[6:70:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[22], 4)
        Y_local_1[7:71:16] = Y_local_1[7:71:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[23], 4)
        Y_local_1[8:72:16] = Y_local_1[8:72:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[24], 4)
        Y_local_1[9:73:16] = Y_local_1[9:73:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[25], 4)
        Y_local_1[10:74:16] = Y_local_1[10:74:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[26], 4)
        Y_local_1[11:75:16] = Y_local_1[11:75:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[27], 4)
        Y_local_1[12:76:16] = Y_local_1[12:76:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[28], 4)
        Y_local_1[13:77:16] = Y_local_1[13:77:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[29], 4)
        Y_local_1[14:78:16] = Y_local_1[14:78:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[30], 4)
        Y_local_1[15:79:16] = Y_local_1[15:79:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[31], 4)
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 0)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1664:threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1664 + 4]
            for ax1_0 in T.serial(4):
                B_shared_dyn_local_1[ax1_0 * 4 + 16:ax1_0 * 4 + 16 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 2496:threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 2496 + 4]
            Y_local_1[0:64:16] = Y_local_1[0:64:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:65:16] = Y_local_1[1:65:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:66:16] = Y_local_1[2:66:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:67:16] = Y_local_1[3:67:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:68:16] = Y_local_1[4:68:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:69:16] = Y_local_1[5:69:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:70:16] = Y_local_1[6:70:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:71:16] = Y_local_1[7:71:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[8:72:16] = Y_local_1[8:72:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[9:73:16] = Y_local_1[9:73:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[10:74:16] = Y_local_1[10:74:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[11:75:16] = Y_local_1[11:75:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[12:76:16] = Y_local_1[12:76:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[13:77:16] = Y_local_1[13:77:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[14:78:16] = Y_local_1[14:78:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[15:79:16] = Y_local_1[15:79:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1792:threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1792 + 4]
            for ax1_0 in T.serial(4):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 2688:threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 2688 + 4]
            Y_local_1[0:64:16] = Y_local_1[0:64:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[16], 4)
            Y_local_1[1:65:16] = Y_local_1[1:65:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[17], 4)
            Y_local_1[2:66:16] = Y_local_1[2:66:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[18], 4)
            Y_local_1[3:67:16] = Y_local_1[3:67:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[19], 4)
            Y_local_1[4:68:16] = Y_local_1[4:68:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[20], 4)
            Y_local_1[5:69:16] = Y_local_1[5:69:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[21], 4)
            Y_local_1[6:70:16] = Y_local_1[6:70:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[22], 4)
            Y_local_1[7:71:16] = Y_local_1[7:71:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[23], 4)
            Y_local_1[8:72:16] = Y_local_1[8:72:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[24], 4)
            Y_local_1[9:73:16] = Y_local_1[9:73:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[25], 4)
            Y_local_1[10:74:16] = Y_local_1[10:74:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[26], 4)
            Y_local_1[11:75:16] = Y_local_1[11:75:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[27], 4)
            Y_local_1[12:76:16] = Y_local_1[12:76:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[28], 4)
            Y_local_1[13:77:16] = Y_local_1[13:77:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[29], 4)
            Y_local_1[14:78:16] = Y_local_1[14:78:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[30], 4)
            Y_local_1[15:79:16] = Y_local_1[15:79:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[31], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1920:threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1920 + 4]
            for ax1_0 in T.serial(4):
                B_shared_dyn_local_1[ax1_0 * 4 + 16:ax1_0 * 4 + 16 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 2880:threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 2880 + 4]
            Y_local_1[0:64:16] = Y_local_1[0:64:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:65:16] = Y_local_1[1:65:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:66:16] = Y_local_1[2:66:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:67:16] = Y_local_1[3:67:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:68:16] = Y_local_1[4:68:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:69:16] = Y_local_1[5:69:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:70:16] = Y_local_1[6:70:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:71:16] = Y_local_1[7:71:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[8:72:16] = Y_local_1[8:72:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[9:73:16] = Y_local_1[9:73:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[10:74:16] = Y_local_1[10:74:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[11:75:16] = Y_local_1[11:75:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[12:76:16] = Y_local_1[12:76:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[13:77:16] = Y_local_1[13:77:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[14:78:16] = Y_local_1[14:78:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[15:79:16] = Y_local_1[15:79:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 2048:threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 2048 + 4]
            for ax1_0 in T.serial(4):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 3072:threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 3072 + 4]
            Y_local_1[0:64:16] = Y_local_1[0:64:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[16], 4)
            Y_local_1[1:65:16] = Y_local_1[1:65:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[17], 4)
            Y_local_1[2:66:16] = Y_local_1[2:66:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[18], 4)
            Y_local_1[3:67:16] = Y_local_1[3:67:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[19], 4)
            Y_local_1[4:68:16] = Y_local_1[4:68:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[20], 4)
            Y_local_1[5:69:16] = Y_local_1[5:69:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[21], 4)
            Y_local_1[6:70:16] = Y_local_1[6:70:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[22], 4)
            Y_local_1[7:71:16] = Y_local_1[7:71:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[23], 4)
            Y_local_1[8:72:16] = Y_local_1[8:72:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[24], 4)
            Y_local_1[9:73:16] = Y_local_1[9:73:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[25], 4)
            Y_local_1[10:74:16] = Y_local_1[10:74:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[26], 4)
            Y_local_1[11:75:16] = Y_local_1[11:75:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[27], 4)
            Y_local_1[12:76:16] = Y_local_1[12:76:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[28], 4)
            Y_local_1[13:77:16] = Y_local_1[13:77:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[29], 4)
            Y_local_1[14:78:16] = Y_local_1[14:78:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[30], 4)
            Y_local_1[15:79:16] = Y_local_1[15:79:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[31], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 2176:threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 2176 + 4]
            for ax1_0 in T.serial(4):
                B_shared_dyn_local_1[ax1_0 * 4 + 16:ax1_0 * 4 + 16 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 3264:threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 3264 + 4]
            Y_local_1[0:64:16] = Y_local_1[0:64:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:65:16] = Y_local_1[1:65:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:66:16] = Y_local_1[2:66:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:67:16] = Y_local_1[3:67:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:68:16] = Y_local_1[4:68:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:69:16] = Y_local_1[5:69:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:70:16] = Y_local_1[6:70:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:71:16] = Y_local_1[7:71:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            Y_local_1[8:72:16] = Y_local_1[8:72:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[9:73:16] = Y_local_1[9:73:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[10:74:16] = Y_local_1[10:74:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[11:75:16] = Y_local_1[11:75:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[12:76:16] = Y_local_1[12:76:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[13:77:16] = Y_local_1[13:77:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[14:78:16] = Y_local_1[14:78:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[15:79:16] = Y_local_1[15:79:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[15], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 2304:threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 2304 + 4]
        for ax1_0 in T.serial(4):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 3456:threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 3456 + 4]
        Y_local_1[0:64:16] = Y_local_1[0:64:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[16], 4)
        Y_local_1[1:65:16] = Y_local_1[1:65:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[17], 4)
        Y_local_1[2:66:16] = Y_local_1[2:66:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[18], 4)
        Y_local_1[3:67:16] = Y_local_1[3:67:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[19], 4)
        Y_local_1[4:68:16] = Y_local_1[4:68:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[20], 4)
        Y_local_1[5:69:16] = Y_local_1[5:69:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[21], 4)
        Y_local_1[6:70:16] = Y_local_1[6:70:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[22], 4)
        Y_local_1[7:71:16] = Y_local_1[7:71:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[23], 4)
        Y_local_1[8:72:16] = Y_local_1[8:72:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[24], 4)
        Y_local_1[9:73:16] = Y_local_1[9:73:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[25], 4)
        Y_local_1[10:74:16] = Y_local_1[10:74:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[26], 4)
        Y_local_1[11:75:16] = Y_local_1[11:75:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[27], 4)
        Y_local_1[12:76:16] = Y_local_1[12:76:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[28], 4)
        Y_local_1[13:77:16] = Y_local_1[13:77:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[29], 4)
        Y_local_1[14:78:16] = Y_local_1[14:78:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[30], 4)
        Y_local_1[15:79:16] = Y_local_1[15:79:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[31], 4)
        A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 2432:threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 2432 + 4]
        for ax1_0 in T.serial(4):
            B_shared_dyn_local_1[ax1_0 * 4 + 16:ax1_0 * 4 + 16 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 3648:threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 3648 + 4]
        Y_local_1[0:64:16] = Y_local_1[0:64:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:65:16] = Y_local_1[1:65:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:66:16] = Y_local_1[2:66:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:67:16] = Y_local_1[3:67:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[4:68:16] = Y_local_1[4:68:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[5:69:16] = Y_local_1[5:69:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[6:70:16] = Y_local_1[6:70:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[7:71:16] = Y_local_1[7:71:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[8:72:16] = Y_local_1[8:72:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[9:73:16] = Y_local_1[9:73:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[10:74:16] = Y_local_1[10:74:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[11:75:16] = Y_local_1[11:75:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[12:76:16] = Y_local_1[12:76:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[13:77:16] = Y_local_1[13:77:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[14:78:16] = Y_local_1[14:78:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[15:79:16] = Y_local_1[15:79:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[15], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 2560:threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 2560 + 4]
        for ax1_0 in T.serial(4):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 3840:threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 3840 + 4]
        Y_local_1[0:64:16] = Y_local_1[0:64:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[16], 4)
        Y_local_1[1:65:16] = Y_local_1[1:65:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[17], 4)
        Y_local_1[2:66:16] = Y_local_1[2:66:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[18], 4)
        Y_local_1[3:67:16] = Y_local_1[3:67:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[19], 4)
        Y_local_1[4:68:16] = Y_local_1[4:68:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[20], 4)
        Y_local_1[5:69:16] = Y_local_1[5:69:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[21], 4)
        Y_local_1[6:70:16] = Y_local_1[6:70:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[22], 4)
        Y_local_1[7:71:16] = Y_local_1[7:71:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[23], 4)
        Y_local_1[8:72:16] = Y_local_1[8:72:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[24], 4)
        Y_local_1[9:73:16] = Y_local_1[9:73:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[25], 4)
        Y_local_1[10:74:16] = Y_local_1[10:74:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[26], 4)
        Y_local_1[11:75:16] = Y_local_1[11:75:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[27], 4)
        Y_local_1[12:76:16] = Y_local_1[12:76:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[28], 4)
        Y_local_1[13:77:16] = Y_local_1[13:77:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[29], 4)
        Y_local_1[14:78:16] = Y_local_1[14:78:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[30], 4)
        Y_local_1[15:79:16] = Y_local_1[15:79:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[31], 4)
        A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 2688:threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 2688 + 4]
        for ax1_0 in T.serial(4):
            B_shared_dyn_local_1[ax1_0 * 4 + 16:ax1_0 * 4 + 16 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 4032:threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 4032 + 4]
        Y_local_1[0:64:16] = Y_local_1[0:64:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:65:16] = Y_local_1[1:65:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:66:16] = Y_local_1[2:66:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:67:16] = Y_local_1[3:67:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[4:68:16] = Y_local_1[4:68:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[5:69:16] = Y_local_1[5:69:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[6:70:16] = Y_local_1[6:70:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[7:71:16] = Y_local_1[7:71:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[8:72:16] = Y_local_1[8:72:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[9:73:16] = Y_local_1[9:73:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[10:74:16] = Y_local_1[10:74:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[11:75:16] = Y_local_1[11:75:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[12:76:16] = Y_local_1[12:76:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[13:77:16] = Y_local_1[13:77:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[14:78:16] = Y_local_1[14:78:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[15:79:16] = Y_local_1[15:79:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[15], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 2816:threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 2816 + 4]
        for ax1_0 in T.serial(4):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 4224:threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 4224 + 4]
        Y_local_1[0:64:16] = Y_local_1[0:64:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[16], 4)
        Y_local_1[1:65:16] = Y_local_1[1:65:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[17], 4)
        Y_local_1[2:66:16] = Y_local_1[2:66:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[18], 4)
        Y_local_1[3:67:16] = Y_local_1[3:67:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[19], 4)
        Y_local_1[4:68:16] = Y_local_1[4:68:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[20], 4)
        Y_local_1[5:69:16] = Y_local_1[5:69:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[21], 4)
        Y_local_1[6:70:16] = Y_local_1[6:70:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[22], 4)
        Y_local_1[7:71:16] = Y_local_1[7:71:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[23], 4)
        Y_local_1[8:72:16] = Y_local_1[8:72:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[24], 4)
        Y_local_1[9:73:16] = Y_local_1[9:73:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[25], 4)
        Y_local_1[10:74:16] = Y_local_1[10:74:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[26], 4)
        Y_local_1[11:75:16] = Y_local_1[11:75:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[27], 4)
        Y_local_1[12:76:16] = Y_local_1[12:76:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[28], 4)
        Y_local_1[13:77:16] = Y_local_1[13:77:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[29], 4)
        Y_local_1[14:78:16] = Y_local_1[14:78:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[30], 4)
        Y_local_1[15:79:16] = Y_local_1[15:79:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[31], 4)
        A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 2944:threadIdx_x % 64 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 2944 + 4]
        for ax1_0 in T.serial(4):
            B_shared_dyn_local_1[ax1_0 * 4 + 16:ax1_0 * 4 + 16 + 4] = B_shared_dyn_1[threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 4416:threadIdx_x // 128 * 64 + ax1_0 % 2 * 32 + (threadIdx_x // 64 * 4 + threadIdx_x % 2 * 2 + ax1_0 // 2) % 8 * 4 + 4416 + 4]
        Y_local_1[0:64:16] = Y_local_1[0:64:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:65:16] = Y_local_1[1:65:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:66:16] = Y_local_1[2:66:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:67:16] = Y_local_1[3:67:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[4:68:16] = Y_local_1[4:68:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[5:69:16] = Y_local_1[5:69:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[6:70:16] = Y_local_1[6:70:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[7:71:16] = Y_local_1[7:71:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_local_1[8:72:16] = Y_local_1[8:72:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[9:73:16] = Y_local_1[9:73:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[10:74:16] = Y_local_1[10:74:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[11:75:16] = Y_local_1[11:75:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[12:76:16] = Y_local_1[12:76:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[13:77:16] = Y_local_1[13:77:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[14:78:16] = Y_local_1[14:78:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[15:79:16] = Y_local_1[15:79:16] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[15], 4)
        Y_local_1[0:64:16] = Y_local_1[0:64:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[16], 4)
        Y_local_1[1:65:16] = Y_local_1[1:65:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[17], 4)
        Y_local_1[2:66:16] = Y_local_1[2:66:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[18], 4)
        Y_local_1[3:67:16] = Y_local_1[3:67:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[19], 4)
        Y_local_1[4:68:16] = Y_local_1[4:68:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[20], 4)
        Y_local_1[5:69:16] = Y_local_1[5:69:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[21], 4)
        Y_local_1[6:70:16] = Y_local_1[6:70:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[22], 4)
        Y_local_1[7:71:16] = Y_local_1[7:71:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[23], 4)
        Y_local_1[8:72:16] = Y_local_1[8:72:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[24], 4)
        Y_local_1[9:73:16] = Y_local_1[9:73:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[25], 4)
        Y_local_1[10:74:16] = Y_local_1[10:74:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[26], 4)
        Y_local_1[11:75:16] = Y_local_1[11:75:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[27], 4)
        Y_local_1[12:76:16] = Y_local_1[12:76:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[28], 4)
        Y_local_1[13:77:16] = Y_local_1[13:77:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[29], 4)
        Y_local_1[14:78:16] = Y_local_1[14:78:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[30], 4)
        Y_local_1[15:79:16] = Y_local_1[15:79:16] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[31], 4)
        for ax1_0 in T.serial(4):
            cse_var_1: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 6 * 147456 + threadIdx_x % 64 // 2 * 4608 + blockIdx_x % 6 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + cse_var_1:blockIdx_x // 6 * 147456 + threadIdx_x % 64 // 2 * 4608 + blockIdx_x % 6 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + cse_var_1 + 4] = Y_local_1[cse_var_1:cse_var_1 + 4]
        for ax1_0 in T.serial(4):
            cse_var_2: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 6 * 147456 + threadIdx_x % 64 // 2 * 4608 + blockIdx_x % 6 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + cse_var_2 + 1152:blockIdx_x // 6 * 147456 + threadIdx_x % 64 // 2 * 4608 + blockIdx_x % 6 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + cse_var_2 + 1152 + 4] = Y_local_1[cse_var_2 + 16:cse_var_2 + 16 + 4]
        for ax1_0 in T.serial(4):
            cse_var_3: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 6 * 147456 + threadIdx_x % 64 // 2 * 4608 + blockIdx_x % 6 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + cse_var_3 + 2304:blockIdx_x // 6 * 147456 + threadIdx_x % 64 // 2 * 4608 + blockIdx_x % 6 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + cse_var_3 + 2304 + 4] = Y_local_1[cse_var_3 + 32:cse_var_3 + 32 + 4]
        for ax1_0 in T.serial(4):
            cse_var_4: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 6 * 147456 + threadIdx_x % 64 // 2 * 4608 + blockIdx_x % 6 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + cse_var_4 + 3456:blockIdx_x // 6 * 147456 + threadIdx_x % 64 // 2 * 4608 + blockIdx_x % 6 * 192 + threadIdx_x // 64 * 32 + threadIdx_x % 2 * 16 + cse_var_4 + 3456 + 4] = Y_local_1[cse_var_4 + 48:cse_var_4 + 48 + 4]
    

