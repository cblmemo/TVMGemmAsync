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
        T.launch_thread(blockIdx_x, 196)
        Y_local = T.allocate([32], "float32", "local")
        Y_local_1 = T.buffer_decl([32], dtype="float32", data=Y_local, scope="local")
        A_shared_dyn = T.allocate([1024], "float32", "shared.dyn")
        A_shared_dyn_1 = T.buffer_decl([1024], dtype="float32", data=A_shared_dyn, scope="shared.dyn")
        B_shared_dyn = T.allocate([1024], "float32", "shared.dyn")
        B_shared_dyn_1 = T.buffer_decl([1024], dtype="float32", data=B_shared_dyn, scope="shared.dyn")
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
                A_shared_dyn_1[threadIdx_x // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + threadIdx_x % 2 * 2:threadIdx_x // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + threadIdx_x % 2 * 2 + 2] = A_1[threadIdx_x // 32 * 896 + blockIdx_x // 14 * 64 + threadIdx_x % 32 * 2:threadIdx_x // 32 * 896 + blockIdx_x // 14 * 64 + threadIdx_x % 32 * 2 + 2]
            T.attr(0, "async_scope", 1)
            for ax0_ax1_fused_2 in T.serial(2):
                B_shared_dyn_1[threadIdx_x // 32 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 32 // 4 * 4 + threadIdx_x % 2 * 2 + ax0_ax1_fused_2] = B_1[threadIdx_x // 32 * 896 + blockIdx_x % 14 * 64 + threadIdx_x % 32 * 2 + ax0_ax1_fused_2]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + threadIdx_x % 2 * 2 + 256:threadIdx_x // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + threadIdx_x % 2 * 2 + 256 + 2] = A_1[threadIdx_x // 32 * 896 + blockIdx_x // 14 * 64 + threadIdx_x % 32 * 2 + 3584:threadIdx_x // 32 * 896 + blockIdx_x // 14 * 64 + threadIdx_x % 32 * 2 + 3584 + 2]
            T.attr(0, "async_scope", 1)
            for ax0_ax1_fused_2 in T.serial(2):
                B_shared_dyn_1[threadIdx_x // 32 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 32 // 4 * 4 + threadIdx_x % 2 * 2 + ax0_ax1_fused_2 + 256] = B_1[threadIdx_x // 32 * 896 + blockIdx_x % 14 * 64 + threadIdx_x % 32 * 2 + ax0_ax1_fused_2 + 3584]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + threadIdx_x % 2 * 2 + 512:threadIdx_x // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + threadIdx_x % 2 * 2 + 512 + 2] = A_1[threadIdx_x // 32 * 896 + blockIdx_x // 14 * 64 + threadIdx_x % 32 * 2 + 7168:threadIdx_x // 32 * 896 + blockIdx_x // 14 * 64 + threadIdx_x % 32 * 2 + 7168 + 2]
            T.attr(0, "async_scope", 1)
            for ax0_ax1_fused_2 in T.serial(2):
                B_shared_dyn_1[threadIdx_x // 32 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 32 // 4 * 4 + threadIdx_x % 2 * 2 + ax0_ax1_fused_2 + 512] = B_1[threadIdx_x // 32 * 896 + blockIdx_x % 14 * 64 + threadIdx_x % 32 * 2 + ax0_ax1_fused_2 + 7168]
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 2)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4:threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4:ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 4]
        for k_0 in T.serial(221):
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    A_shared_dyn_1[(k_0 + 3) % 4 * 256 + threadIdx_x // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + threadIdx_x % 2 * 2:(k_0 + 3) % 4 * 256 + threadIdx_x // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + threadIdx_x % 2 * 2 + 2] = A_1[k_0 * 3584 + threadIdx_x // 32 * 896 + blockIdx_x // 14 * 64 + threadIdx_x % 32 * 2 + 10752:k_0 * 3584 + threadIdx_x // 32 * 896 + blockIdx_x // 14 * 64 + threadIdx_x % 32 * 2 + 10752 + 2]
                T.attr(0, "async_scope", 1)
                for ax0_ax1_fused_2 in T.serial(2):
                    B_shared_dyn_1[(k_0 + 3) % 4 * 256 + threadIdx_x // 32 * 64 + threadIdx_x % 4 // 2 * 32 + threadIdx_x % 32 // 4 * 4 + threadIdx_x % 2 * 2 + ax0_ax1_fused_2] = B_1[k_0 * 3584 + threadIdx_x // 32 * 896 + blockIdx_x % 14 * 64 + threadIdx_x % 32 * 2 + ax0_ax1_fused_2 + 10752]
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 2)
                A_shared_dyn_local_1[1] = A_shared_dyn_1[k_0 % 4 * 256 + threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 64:k_0 % 4 * 256 + threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 64 + 4]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[k_0 % 4 * 256 + ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 64:k_0 % 4 * 256 + ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 64 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
                A_shared_dyn_local_1[0] = A_shared_dyn_1[k_0 % 4 * 256 + threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 128:k_0 % 4 * 256 + threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 128 + 4]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[k_0 % 4 * 256 + ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 128:k_0 % 4 * 256 + ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 128 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
                A_shared_dyn_local_1[1] = A_shared_dyn_1[k_0 % 4 * 256 + threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 192:k_0 % 4 * 256 + threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 192 + 4]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[k_0 % 4 * 256 + ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 192:k_0 % 4 * 256 + ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 192 + 4]
                Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[(k_0 + 1) % 4 * 256 + threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4:(k_0 + 1) % 4 * 256 + threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[(k_0 + 1) % 4 * 256 + ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4:(k_0 + 1) % 4 * 256 + ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 4]
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
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 320:threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 320 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 320:ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 320 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 384:threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 384 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 384:ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 384 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 448:threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 448 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 448:ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 448 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 512:threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 512 + 4]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 512:ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 512 + 4]
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
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 576:threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 576 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 576:ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 576 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 640:threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 640 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 640:ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 640 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 704:threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 704 + 4]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 704:ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 704 + 4]
            Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 768:threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 768 + 4]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 768:ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 768 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
        A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 832:threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 832 + 4]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 832:ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 832 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[7], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 896:threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 896 + 4]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 896:ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 896 + 4]
        Y_local_1[0:32:8] = Y_local_1[0:32:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[8], 4)
        Y_local_1[1:33:8] = Y_local_1[1:33:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[9], 4)
        Y_local_1[2:34:8] = Y_local_1[2:34:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[10], 4)
        Y_local_1[3:35:8] = Y_local_1[3:35:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[11], 4)
        Y_local_1[4:36:8] = Y_local_1[4:36:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[12], 4)
        Y_local_1[5:37:8] = Y_local_1[5:37:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[13], 4)
        Y_local_1[6:38:8] = Y_local_1[6:38:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[14], 4)
        Y_local_1[7:39:8] = Y_local_1[7:39:8] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[15], 4)
        A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 960:threadIdx_x % 32 // 16 * 32 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 16 // 4 * 4 + 960 + 4]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 960:ax1_0 * 32 + threadIdx_x // 32 * 8 + threadIdx_x % 2 * 4 + 960 + 4]
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
            cse_var_1: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 14 * 57344 + threadIdx_x % 32 // 2 * 3584 + blockIdx_x % 14 * 64 + threadIdx_x // 32 * 16 + threadIdx_x % 2 * 8 + cse_var_1:blockIdx_x // 14 * 57344 + threadIdx_x % 32 // 2 * 3584 + blockIdx_x % 14 * 64 + threadIdx_x // 32 * 16 + threadIdx_x % 2 * 8 + cse_var_1 + 4] = Y_local_1[cse_var_1:cse_var_1 + 4]
        for ax1_0 in T.serial(2):
            cse_var_2: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 14 * 57344 + threadIdx_x % 32 // 2 * 3584 + blockIdx_x % 14 * 64 + threadIdx_x // 32 * 16 + threadIdx_x % 2 * 8 + cse_var_2 + 896:blockIdx_x // 14 * 57344 + threadIdx_x % 32 // 2 * 3584 + blockIdx_x % 14 * 64 + threadIdx_x // 32 * 16 + threadIdx_x % 2 * 8 + cse_var_2 + 896 + 4] = Y_local_1[cse_var_2 + 8:cse_var_2 + 8 + 4]
        for ax1_0 in T.serial(2):
            cse_var_3: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 14 * 57344 + threadIdx_x % 32 // 2 * 3584 + blockIdx_x % 14 * 64 + threadIdx_x // 32 * 16 + threadIdx_x % 2 * 8 + cse_var_3 + 1792:blockIdx_x // 14 * 57344 + threadIdx_x % 32 // 2 * 3584 + blockIdx_x % 14 * 64 + threadIdx_x // 32 * 16 + threadIdx_x % 2 * 8 + cse_var_3 + 1792 + 4] = Y_local_1[cse_var_3 + 16:cse_var_3 + 16 + 4]
        for ax1_0 in T.serial(2):
            cse_var_4: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 14 * 57344 + threadIdx_x % 32 // 2 * 3584 + blockIdx_x % 14 * 64 + threadIdx_x // 32 * 16 + threadIdx_x % 2 * 8 + cse_var_4 + 2688:blockIdx_x // 14 * 57344 + threadIdx_x % 32 // 2 * 3584 + blockIdx_x % 14 * 64 + threadIdx_x // 32 * 16 + threadIdx_x % 2 * 8 + cse_var_4 + 2688 + 4] = Y_local_1[cse_var_4 + 24:cse_var_4 + 24 + 4]
    

