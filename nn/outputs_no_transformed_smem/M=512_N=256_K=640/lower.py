# from tvm.script import tir as T
@tvm.script.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer[(512, 640), "float32"], B: T.Buffer[(640, 256), "float32"], Y: T.Buffer[(512, 256), "float32"]):
        # function attr dict
        T.func_attr({"global_symbol": "main", "tir.noalias": True})
        # var definition
        threadIdx_x = T.env_thread("threadIdx.x")
        blockIdx_x = T.env_thread("blockIdx.x")
        # buffer definition
        A_1 = T.buffer_decl([327680], dtype="float32", data=A.data)
        B_1 = T.buffer_decl([163840], dtype="float32", data=B.data)
        Y_1 = T.buffer_decl([131072], dtype="float32", data=Y.data)
        # body
        T.launch_thread(blockIdx_x, 64)
        Y_local = T.allocate([16], "float32", "local")
        Y_local_1 = T.buffer_decl([16], dtype="float32", data=Y_local, scope="local")
        A_shared_dyn = T.allocate([3200], "float32", "shared.dyn")
        A_shared_dyn_1 = T.buffer_decl([3200], dtype="float32", data=A_shared_dyn, scope="shared.dyn")
        B_shared_dyn = T.allocate([2560], "float32", "shared.dyn")
        B_shared_dyn_1 = T.buffer_decl([2560], dtype="float32", data=B_shared_dyn, scope="shared.dyn")
        A_shared_dyn_local = T.allocate([4], "float32", "local")
        A_shared_dyn_local_1 = T.buffer_decl([4], dtype="float32", data=A_shared_dyn_local, scope="local")
        B_shared_dyn_local = T.allocate([16], "float32", "local")
        B_shared_dyn_local_1 = T.buffer_decl([16], dtype="float32", data=B_shared_dyn_local, scope="local")
        T.launch_thread(threadIdx_x, 128)
        Y_local_1[0] = T.float32(0)
        Y_local_1[8] = T.float32(0)
        Y_local_1[1] = T.float32(0)
        Y_local_1[9] = T.float32(0)
        Y_local_1[2] = T.float32(0)
        Y_local_1[10] = T.float32(0)
        Y_local_1[3] = T.float32(0)
        Y_local_1[11] = T.float32(0)
        Y_local_1[4] = T.float32(0)
        Y_local_1[12] = T.float32(0)
        Y_local_1[5] = T.float32(0)
        Y_local_1[13] = T.float32(0)
        Y_local_1[6] = T.float32(0)
        Y_local_1[14] = T.float32(0)
        Y_local_1[7] = T.float32(0)
        Y_local_1[15] = T.float32(0)
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x // 4 * 20 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 2 * 2:threadIdx_x // 4 * 20 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 2 * 2 + 2] = A_1[blockIdx_x // 4 * 20480 + threadIdx_x // 4 * 640 + threadIdx_x % 4 * 2:blockIdx_x // 4 * 20480 + threadIdx_x // 4 * 640 + threadIdx_x % 4 * 2 + 2]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 4] = B_1[threadIdx_x // 16 * 256 + blockIdx_x % 4 * 64 + threadIdx_x % 16 * 4:threadIdx_x // 16 * 256 + blockIdx_x % 4 * 64 + threadIdx_x % 16 * 4 + 4]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x // 4 * 20 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 2 * 2 + 640:threadIdx_x // 4 * 20 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 2 * 2 + 640 + 2] = A_1[blockIdx_x // 4 * 20480 + threadIdx_x // 4 * 640 + threadIdx_x % 4 * 2 + 8:blockIdx_x // 4 * 20480 + threadIdx_x // 4 * 640 + threadIdx_x % 4 * 2 + 8 + 2]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 512:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 512 + 4] = B_1[threadIdx_x // 16 * 256 + blockIdx_x % 4 * 64 + threadIdx_x % 16 * 4 + 2048:threadIdx_x // 16 * 256 + blockIdx_x % 4 * 64 + threadIdx_x % 16 * 4 + 2048 + 4]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x // 4 * 20 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 2 * 2 + 1280:threadIdx_x // 4 * 20 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 2 * 2 + 1280 + 2] = A_1[blockIdx_x // 4 * 20480 + threadIdx_x // 4 * 640 + threadIdx_x % 4 * 2 + 16:blockIdx_x // 4 * 20480 + threadIdx_x // 4 * 640 + threadIdx_x % 4 * 2 + 16 + 2]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 1024:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 1024 + 4] = B_1[threadIdx_x // 16 * 256 + blockIdx_x % 4 * 64 + threadIdx_x % 16 * 4 + 4096:threadIdx_x // 16 * 256 + blockIdx_x % 4 * 64 + threadIdx_x % 16 * 4 + 4096 + 4]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x // 4 * 20 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 2 * 2 + 1920:threadIdx_x // 4 * 20 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 2 * 2 + 1920 + 2] = A_1[blockIdx_x // 4 * 20480 + threadIdx_x // 4 * 640 + threadIdx_x % 4 * 2 + 24:blockIdx_x // 4 * 20480 + threadIdx_x // 4 * 640 + threadIdx_x % 4 * 2 + 24 + 2]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 1536:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 1536 + 4] = B_1[threadIdx_x // 16 * 256 + blockIdx_x % 4 * 64 + threadIdx_x % 16 * 4 + 6144:threadIdx_x // 16 * 256 + blockIdx_x % 4 * 64 + threadIdx_x % 16 * 4 + 6144 + 4]
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 3)
            for ax0_1_s in T.serial(4):
                if ax0_1_s < 2:
                    A_shared_dyn_local_1[ax0_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 4]
        for k_0 in T.serial(76):
            cse_var_1: T.int32 = (k_0 + 4) % 5
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    A_shared_dyn_1[cse_var_1 * 640 + threadIdx_x // 4 * 20 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 2 * 2:cse_var_1 * 640 + threadIdx_x // 4 * 20 + threadIdx_x % 4 // 2 * 16 + threadIdx_x % 2 * 2 + 2] = A_1[blockIdx_x // 4 * 20480 + threadIdx_x // 4 * 640 + k_0 * 8 + threadIdx_x % 4 * 2 + 32:blockIdx_x // 4 * 20480 + threadIdx_x // 4 * 640 + k_0 * 8 + threadIdx_x % 4 * 2 + 32 + 2]
                T.attr(0, "async_scope", 1)
                B_shared_dyn_1[cse_var_1 * 512 + threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4:cse_var_1 * 512 + threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 4] = B_1[k_0 * 2048 + threadIdx_x // 16 * 256 + blockIdx_x % 4 * 64 + threadIdx_x % 16 * 4 + 8192:k_0 * 2048 + threadIdx_x // 16 * 256 + blockIdx_x % 4 * 64 + threadIdx_x % 16 * 4 + 8192 + 4]
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 3)
                for ax0_1_s in T.serial(4):
                    if ax0_1_s < 2:
                        A_shared_dyn_local_1[ax0_1_s + 2] = A_shared_dyn_1[k_0 % 5 * 640 + threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 1]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 64:k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 64 + 4]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_2: T.int32 = i_2_1_s * 8
                        Y_local_1[cse_var_2] = Y_local_1[cse_var_2] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_3: T.int32 = i_2_1_s * 8 + 1
                        Y_local_1[cse_var_3] = Y_local_1[cse_var_3] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_4: T.int32 = i_2_1_s * 8 + 2
                        Y_local_1[cse_var_4] = Y_local_1[cse_var_4] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_5: T.int32 = i_2_1_s * 8 + 3
                        Y_local_1[cse_var_5] = Y_local_1[cse_var_5] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_6: T.int32 = i_2_1_s * 8 + 4
                        Y_local_1[cse_var_6] = Y_local_1[cse_var_6] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_7: T.int32 = i_2_1_s * 8 + 5
                        Y_local_1[cse_var_7] = Y_local_1[cse_var_7] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_8: T.int32 = i_2_1_s * 8 + 6
                        Y_local_1[cse_var_8] = Y_local_1[cse_var_8] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_9: T.int32 = i_2_1_s * 8 + 7
                        Y_local_1[cse_var_9] = Y_local_1[cse_var_9] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
                for ax0_1_s in T.serial(4):
                    if ax0_1_s < 2:
                        A_shared_dyn_local_1[ax0_1_s] = A_shared_dyn_1[k_0 % 5 * 640 + threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 2]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 128:k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 128 + 4]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_10: T.int32 = i_2_1_s * 8
                        Y_local_1[cse_var_10] = Y_local_1[cse_var_10] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[8]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_11: T.int32 = i_2_1_s * 8 + 1
                        Y_local_1[cse_var_11] = Y_local_1[cse_var_11] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[9]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_12: T.int32 = i_2_1_s * 8 + 2
                        Y_local_1[cse_var_12] = Y_local_1[cse_var_12] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[10]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_13: T.int32 = i_2_1_s * 8 + 3
                        Y_local_1[cse_var_13] = Y_local_1[cse_var_13] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[11]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_14: T.int32 = i_2_1_s * 8 + 4
                        Y_local_1[cse_var_14] = Y_local_1[cse_var_14] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_15: T.int32 = i_2_1_s * 8 + 5
                        Y_local_1[cse_var_15] = Y_local_1[cse_var_15] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_16: T.int32 = i_2_1_s * 8 + 6
                        Y_local_1[cse_var_16] = Y_local_1[cse_var_16] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_17: T.int32 = i_2_1_s * 8 + 7
                        Y_local_1[cse_var_17] = Y_local_1[cse_var_17] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
                for ax0_1_s in T.serial(4):
                    if ax0_1_s < 2:
                        A_shared_dyn_local_1[ax0_1_s + 2] = A_shared_dyn_1[k_0 % 5 * 640 + threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 3]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 192:k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 192 + 4]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_18: T.int32 = i_2_1_s * 8
                        Y_local_1[cse_var_18] = Y_local_1[cse_var_18] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_19: T.int32 = i_2_1_s * 8 + 1
                        Y_local_1[cse_var_19] = Y_local_1[cse_var_19] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_20: T.int32 = i_2_1_s * 8 + 2
                        Y_local_1[cse_var_20] = Y_local_1[cse_var_20] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_21: T.int32 = i_2_1_s * 8 + 3
                        Y_local_1[cse_var_21] = Y_local_1[cse_var_21] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_22: T.int32 = i_2_1_s * 8 + 4
                        Y_local_1[cse_var_22] = Y_local_1[cse_var_22] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_23: T.int32 = i_2_1_s * 8 + 5
                        Y_local_1[cse_var_23] = Y_local_1[cse_var_23] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_24: T.int32 = i_2_1_s * 8 + 6
                        Y_local_1[cse_var_24] = Y_local_1[cse_var_24] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_25: T.int32 = i_2_1_s * 8 + 7
                        Y_local_1[cse_var_25] = Y_local_1[cse_var_25] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
                for ax0_1_s in T.serial(4):
                    if ax0_1_s < 2:
                        A_shared_dyn_local_1[ax0_1_s] = A_shared_dyn_1[k_0 % 5 * 640 + threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 16]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 256:k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 256 + 4]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_26: T.int32 = i_2_1_s * 8
                        Y_local_1[cse_var_26] = Y_local_1[cse_var_26] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[8]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_27: T.int32 = i_2_1_s * 8 + 1
                        Y_local_1[cse_var_27] = Y_local_1[cse_var_27] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[9]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_28: T.int32 = i_2_1_s * 8 + 2
                        Y_local_1[cse_var_28] = Y_local_1[cse_var_28] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[10]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_29: T.int32 = i_2_1_s * 8 + 3
                        Y_local_1[cse_var_29] = Y_local_1[cse_var_29] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[11]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_30: T.int32 = i_2_1_s * 8 + 4
                        Y_local_1[cse_var_30] = Y_local_1[cse_var_30] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_31: T.int32 = i_2_1_s * 8 + 5
                        Y_local_1[cse_var_31] = Y_local_1[cse_var_31] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_32: T.int32 = i_2_1_s * 8 + 6
                        Y_local_1[cse_var_32] = Y_local_1[cse_var_32] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_33: T.int32 = i_2_1_s * 8 + 7
                        Y_local_1[cse_var_33] = Y_local_1[cse_var_33] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
                for ax0_1_s in T.serial(4):
                    if ax0_1_s < 2:
                        A_shared_dyn_local_1[ax0_1_s + 2] = A_shared_dyn_1[k_0 % 5 * 640 + threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 17]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 320:k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 320 + 4]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_34: T.int32 = i_2_1_s * 8
                        Y_local_1[cse_var_34] = Y_local_1[cse_var_34] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_35: T.int32 = i_2_1_s * 8 + 1
                        Y_local_1[cse_var_35] = Y_local_1[cse_var_35] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_36: T.int32 = i_2_1_s * 8 + 2
                        Y_local_1[cse_var_36] = Y_local_1[cse_var_36] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_37: T.int32 = i_2_1_s * 8 + 3
                        Y_local_1[cse_var_37] = Y_local_1[cse_var_37] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_38: T.int32 = i_2_1_s * 8 + 4
                        Y_local_1[cse_var_38] = Y_local_1[cse_var_38] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_39: T.int32 = i_2_1_s * 8 + 5
                        Y_local_1[cse_var_39] = Y_local_1[cse_var_39] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_40: T.int32 = i_2_1_s * 8 + 6
                        Y_local_1[cse_var_40] = Y_local_1[cse_var_40] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_41: T.int32 = i_2_1_s * 8 + 7
                        Y_local_1[cse_var_41] = Y_local_1[cse_var_41] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
                for ax0_1_s in T.serial(4):
                    if ax0_1_s < 2:
                        A_shared_dyn_local_1[ax0_1_s] = A_shared_dyn_1[k_0 % 5 * 640 + threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 18]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 384:k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 384 + 4]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_42: T.int32 = i_2_1_s * 8
                        Y_local_1[cse_var_42] = Y_local_1[cse_var_42] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[8]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_43: T.int32 = i_2_1_s * 8 + 1
                        Y_local_1[cse_var_43] = Y_local_1[cse_var_43] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[9]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_44: T.int32 = i_2_1_s * 8 + 2
                        Y_local_1[cse_var_44] = Y_local_1[cse_var_44] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[10]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_45: T.int32 = i_2_1_s * 8 + 3
                        Y_local_1[cse_var_45] = Y_local_1[cse_var_45] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[11]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_46: T.int32 = i_2_1_s * 8 + 4
                        Y_local_1[cse_var_46] = Y_local_1[cse_var_46] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_47: T.int32 = i_2_1_s * 8 + 5
                        Y_local_1[cse_var_47] = Y_local_1[cse_var_47] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_48: T.int32 = i_2_1_s * 8 + 6
                        Y_local_1[cse_var_48] = Y_local_1[cse_var_48] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_49: T.int32 = i_2_1_s * 8 + 7
                        Y_local_1[cse_var_49] = Y_local_1[cse_var_49] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
                for ax0_1_s in T.serial(4):
                    if ax0_1_s < 2:
                        A_shared_dyn_local_1[ax0_1_s + 2] = A_shared_dyn_1[k_0 % 5 * 640 + threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 19]
                for ax1_0 in T.serial(2):
                    B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 448:k_0 % 5 * 512 + ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 448 + 4]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_50: T.int32 = i_2_1_s * 8
                        Y_local_1[cse_var_50] = Y_local_1[cse_var_50] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_51: T.int32 = i_2_1_s * 8 + 1
                        Y_local_1[cse_var_51] = Y_local_1[cse_var_51] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_52: T.int32 = i_2_1_s * 8 + 2
                        Y_local_1[cse_var_52] = Y_local_1[cse_var_52] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_53: T.int32 = i_2_1_s * 8 + 3
                        Y_local_1[cse_var_53] = Y_local_1[cse_var_53] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_54: T.int32 = i_2_1_s * 8 + 4
                        Y_local_1[cse_var_54] = Y_local_1[cse_var_54] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_55: T.int32 = i_2_1_s * 8 + 5
                        Y_local_1[cse_var_55] = Y_local_1[cse_var_55] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_56: T.int32 = i_2_1_s * 8 + 6
                        Y_local_1[cse_var_56] = Y_local_1[cse_var_56] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
                for i_2_1_s in T.serial(4):
                    if i_2_1_s < 2:
                        cse_var_57: T.int32 = i_2_1_s * 8 + 7
                        Y_local_1[cse_var_57] = Y_local_1[cse_var_57] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
            for ax0_1_s in T.serial(4):
                if ax0_1_s < 2:
                    A_shared_dyn_local_1[ax0_1_s] = A_shared_dyn_1[(k_0 + 1) % 5 * 640 + threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[(k_0 + 1) % 5 * 512 + ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4:(k_0 + 1) % 5 * 512 + ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_58: T.int32 = i_2_1_s * 8
                    Y_local_1[cse_var_58] = Y_local_1[cse_var_58] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_59: T.int32 = i_2_1_s * 8 + 1
                    Y_local_1[cse_var_59] = Y_local_1[cse_var_59] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_60: T.int32 = i_2_1_s * 8 + 2
                    Y_local_1[cse_var_60] = Y_local_1[cse_var_60] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_61: T.int32 = i_2_1_s * 8 + 3
                    Y_local_1[cse_var_61] = Y_local_1[cse_var_61] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[11]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_62: T.int32 = i_2_1_s * 8 + 4
                    Y_local_1[cse_var_62] = Y_local_1[cse_var_62] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_63: T.int32 = i_2_1_s * 8 + 5
                    Y_local_1[cse_var_63] = Y_local_1[cse_var_63] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_64: T.int32 = i_2_1_s * 8 + 6
                    Y_local_1[cse_var_64] = Y_local_1[cse_var_64] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_65: T.int32 = i_2_1_s * 8 + 7
                    Y_local_1[cse_var_65] = Y_local_1[cse_var_65] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 2)
            for ax0_1_s in T.serial(4):
                if ax0_1_s < 2:
                    A_shared_dyn_local_1[ax0_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 641]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 576:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 576 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_66: T.int32 = i_2_1_s * 8
                    Y_local_1[cse_var_66] = Y_local_1[cse_var_66] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_67: T.int32 = i_2_1_s * 8 + 1
                    Y_local_1[cse_var_67] = Y_local_1[cse_var_67] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_68: T.int32 = i_2_1_s * 8 + 2
                    Y_local_1[cse_var_68] = Y_local_1[cse_var_68] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_69: T.int32 = i_2_1_s * 8 + 3
                    Y_local_1[cse_var_69] = Y_local_1[cse_var_69] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_70: T.int32 = i_2_1_s * 8 + 4
                    Y_local_1[cse_var_70] = Y_local_1[cse_var_70] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_71: T.int32 = i_2_1_s * 8 + 5
                    Y_local_1[cse_var_71] = Y_local_1[cse_var_71] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_72: T.int32 = i_2_1_s * 8 + 6
                    Y_local_1[cse_var_72] = Y_local_1[cse_var_72] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_73: T.int32 = i_2_1_s * 8 + 7
                    Y_local_1[cse_var_73] = Y_local_1[cse_var_73] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
            for ax0_1_s in T.serial(4):
                if ax0_1_s < 2:
                    A_shared_dyn_local_1[ax0_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 642]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 640:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 640 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_74: T.int32 = i_2_1_s * 8
                    Y_local_1[cse_var_74] = Y_local_1[cse_var_74] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_75: T.int32 = i_2_1_s * 8 + 1
                    Y_local_1[cse_var_75] = Y_local_1[cse_var_75] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_76: T.int32 = i_2_1_s * 8 + 2
                    Y_local_1[cse_var_76] = Y_local_1[cse_var_76] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_77: T.int32 = i_2_1_s * 8 + 3
                    Y_local_1[cse_var_77] = Y_local_1[cse_var_77] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[11]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_78: T.int32 = i_2_1_s * 8 + 4
                    Y_local_1[cse_var_78] = Y_local_1[cse_var_78] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_79: T.int32 = i_2_1_s * 8 + 5
                    Y_local_1[cse_var_79] = Y_local_1[cse_var_79] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_80: T.int32 = i_2_1_s * 8 + 6
                    Y_local_1[cse_var_80] = Y_local_1[cse_var_80] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_81: T.int32 = i_2_1_s * 8 + 7
                    Y_local_1[cse_var_81] = Y_local_1[cse_var_81] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
            for ax0_1_s in T.serial(4):
                if ax0_1_s < 2:
                    A_shared_dyn_local_1[ax0_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 643]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 704:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 704 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_82: T.int32 = i_2_1_s * 8
                    Y_local_1[cse_var_82] = Y_local_1[cse_var_82] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_83: T.int32 = i_2_1_s * 8 + 1
                    Y_local_1[cse_var_83] = Y_local_1[cse_var_83] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_84: T.int32 = i_2_1_s * 8 + 2
                    Y_local_1[cse_var_84] = Y_local_1[cse_var_84] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_85: T.int32 = i_2_1_s * 8 + 3
                    Y_local_1[cse_var_85] = Y_local_1[cse_var_85] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_86: T.int32 = i_2_1_s * 8 + 4
                    Y_local_1[cse_var_86] = Y_local_1[cse_var_86] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_87: T.int32 = i_2_1_s * 8 + 5
                    Y_local_1[cse_var_87] = Y_local_1[cse_var_87] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_88: T.int32 = i_2_1_s * 8 + 6
                    Y_local_1[cse_var_88] = Y_local_1[cse_var_88] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_89: T.int32 = i_2_1_s * 8 + 7
                    Y_local_1[cse_var_89] = Y_local_1[cse_var_89] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
            for ax0_1_s in T.serial(4):
                if ax0_1_s < 2:
                    A_shared_dyn_local_1[ax0_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 656]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 768:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 768 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_90: T.int32 = i_2_1_s * 8
                    Y_local_1[cse_var_90] = Y_local_1[cse_var_90] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_91: T.int32 = i_2_1_s * 8 + 1
                    Y_local_1[cse_var_91] = Y_local_1[cse_var_91] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_92: T.int32 = i_2_1_s * 8 + 2
                    Y_local_1[cse_var_92] = Y_local_1[cse_var_92] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_93: T.int32 = i_2_1_s * 8 + 3
                    Y_local_1[cse_var_93] = Y_local_1[cse_var_93] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[11]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_94: T.int32 = i_2_1_s * 8 + 4
                    Y_local_1[cse_var_94] = Y_local_1[cse_var_94] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_95: T.int32 = i_2_1_s * 8 + 5
                    Y_local_1[cse_var_95] = Y_local_1[cse_var_95] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_96: T.int32 = i_2_1_s * 8 + 6
                    Y_local_1[cse_var_96] = Y_local_1[cse_var_96] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_97: T.int32 = i_2_1_s * 8 + 7
                    Y_local_1[cse_var_97] = Y_local_1[cse_var_97] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
            for ax0_1_s in T.serial(4):
                if ax0_1_s < 2:
                    A_shared_dyn_local_1[ax0_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 657]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 832:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 832 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_98: T.int32 = i_2_1_s * 8
                    Y_local_1[cse_var_98] = Y_local_1[cse_var_98] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_99: T.int32 = i_2_1_s * 8 + 1
                    Y_local_1[cse_var_99] = Y_local_1[cse_var_99] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_100: T.int32 = i_2_1_s * 8 + 2
                    Y_local_1[cse_var_100] = Y_local_1[cse_var_100] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_101: T.int32 = i_2_1_s * 8 + 3
                    Y_local_1[cse_var_101] = Y_local_1[cse_var_101] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_102: T.int32 = i_2_1_s * 8 + 4
                    Y_local_1[cse_var_102] = Y_local_1[cse_var_102] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_103: T.int32 = i_2_1_s * 8 + 5
                    Y_local_1[cse_var_103] = Y_local_1[cse_var_103] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_104: T.int32 = i_2_1_s * 8 + 6
                    Y_local_1[cse_var_104] = Y_local_1[cse_var_104] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_105: T.int32 = i_2_1_s * 8 + 7
                    Y_local_1[cse_var_105] = Y_local_1[cse_var_105] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
            for ax0_1_s in T.serial(4):
                if ax0_1_s < 2:
                    A_shared_dyn_local_1[ax0_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 658]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 896:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 896 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_106: T.int32 = i_2_1_s * 8
                    Y_local_1[cse_var_106] = Y_local_1[cse_var_106] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_107: T.int32 = i_2_1_s * 8 + 1
                    Y_local_1[cse_var_107] = Y_local_1[cse_var_107] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_108: T.int32 = i_2_1_s * 8 + 2
                    Y_local_1[cse_var_108] = Y_local_1[cse_var_108] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_109: T.int32 = i_2_1_s * 8 + 3
                    Y_local_1[cse_var_109] = Y_local_1[cse_var_109] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[11]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_110: T.int32 = i_2_1_s * 8 + 4
                    Y_local_1[cse_var_110] = Y_local_1[cse_var_110] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_111: T.int32 = i_2_1_s * 8 + 5
                    Y_local_1[cse_var_111] = Y_local_1[cse_var_111] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_112: T.int32 = i_2_1_s * 8 + 6
                    Y_local_1[cse_var_112] = Y_local_1[cse_var_112] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_113: T.int32 = i_2_1_s * 8 + 7
                    Y_local_1[cse_var_113] = Y_local_1[cse_var_113] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
            for ax0_1_s in T.serial(4):
                if ax0_1_s < 2:
                    A_shared_dyn_local_1[ax0_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 659]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 960:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 960 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_114: T.int32 = i_2_1_s * 8
                    Y_local_1[cse_var_114] = Y_local_1[cse_var_114] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_115: T.int32 = i_2_1_s * 8 + 1
                    Y_local_1[cse_var_115] = Y_local_1[cse_var_115] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_116: T.int32 = i_2_1_s * 8 + 2
                    Y_local_1[cse_var_116] = Y_local_1[cse_var_116] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_117: T.int32 = i_2_1_s * 8 + 3
                    Y_local_1[cse_var_117] = Y_local_1[cse_var_117] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_118: T.int32 = i_2_1_s * 8 + 4
                    Y_local_1[cse_var_118] = Y_local_1[cse_var_118] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_119: T.int32 = i_2_1_s * 8 + 5
                    Y_local_1[cse_var_119] = Y_local_1[cse_var_119] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_120: T.int32 = i_2_1_s * 8 + 6
                    Y_local_1[cse_var_120] = Y_local_1[cse_var_120] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_121: T.int32 = i_2_1_s * 8 + 7
                    Y_local_1[cse_var_121] = Y_local_1[cse_var_121] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
        for ax0_1_s in T.serial(4):
            if ax0_1_s < 2:
                A_shared_dyn_local_1[ax0_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 1280]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1024:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1024 + 4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_122: T.int32 = i_2_1_s * 8
                Y_local_1[cse_var_122] = Y_local_1[cse_var_122] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[8]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_123: T.int32 = i_2_1_s * 8 + 1
                Y_local_1[cse_var_123] = Y_local_1[cse_var_123] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[9]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_124: T.int32 = i_2_1_s * 8 + 2
                Y_local_1[cse_var_124] = Y_local_1[cse_var_124] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[10]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_125: T.int32 = i_2_1_s * 8 + 3
                Y_local_1[cse_var_125] = Y_local_1[cse_var_125] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[11]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_126: T.int32 = i_2_1_s * 8 + 4
                Y_local_1[cse_var_126] = Y_local_1[cse_var_126] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_127: T.int32 = i_2_1_s * 8 + 5
                Y_local_1[cse_var_127] = Y_local_1[cse_var_127] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_128: T.int32 = i_2_1_s * 8 + 6
                Y_local_1[cse_var_128] = Y_local_1[cse_var_128] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_129: T.int32 = i_2_1_s * 8 + 7
                Y_local_1[cse_var_129] = Y_local_1[cse_var_129] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 1)
            for ax0_1_s in T.serial(4):
                if ax0_1_s < 2:
                    A_shared_dyn_local_1[ax0_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 1281]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1088:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1088 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_130: T.int32 = i_2_1_s * 8
                    Y_local_1[cse_var_130] = Y_local_1[cse_var_130] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_131: T.int32 = i_2_1_s * 8 + 1
                    Y_local_1[cse_var_131] = Y_local_1[cse_var_131] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_132: T.int32 = i_2_1_s * 8 + 2
                    Y_local_1[cse_var_132] = Y_local_1[cse_var_132] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_133: T.int32 = i_2_1_s * 8 + 3
                    Y_local_1[cse_var_133] = Y_local_1[cse_var_133] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_134: T.int32 = i_2_1_s * 8 + 4
                    Y_local_1[cse_var_134] = Y_local_1[cse_var_134] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_135: T.int32 = i_2_1_s * 8 + 5
                    Y_local_1[cse_var_135] = Y_local_1[cse_var_135] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_136: T.int32 = i_2_1_s * 8 + 6
                    Y_local_1[cse_var_136] = Y_local_1[cse_var_136] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_137: T.int32 = i_2_1_s * 8 + 7
                    Y_local_1[cse_var_137] = Y_local_1[cse_var_137] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
            for ax0_1_s in T.serial(4):
                if ax0_1_s < 2:
                    A_shared_dyn_local_1[ax0_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 1282]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1152:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1152 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_138: T.int32 = i_2_1_s * 8
                    Y_local_1[cse_var_138] = Y_local_1[cse_var_138] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_139: T.int32 = i_2_1_s * 8 + 1
                    Y_local_1[cse_var_139] = Y_local_1[cse_var_139] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_140: T.int32 = i_2_1_s * 8 + 2
                    Y_local_1[cse_var_140] = Y_local_1[cse_var_140] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_141: T.int32 = i_2_1_s * 8 + 3
                    Y_local_1[cse_var_141] = Y_local_1[cse_var_141] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[11]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_142: T.int32 = i_2_1_s * 8 + 4
                    Y_local_1[cse_var_142] = Y_local_1[cse_var_142] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_143: T.int32 = i_2_1_s * 8 + 5
                    Y_local_1[cse_var_143] = Y_local_1[cse_var_143] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_144: T.int32 = i_2_1_s * 8 + 6
                    Y_local_1[cse_var_144] = Y_local_1[cse_var_144] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_145: T.int32 = i_2_1_s * 8 + 7
                    Y_local_1[cse_var_145] = Y_local_1[cse_var_145] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
            for ax0_1_s in T.serial(4):
                if ax0_1_s < 2:
                    A_shared_dyn_local_1[ax0_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 1283]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1216:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1216 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_146: T.int32 = i_2_1_s * 8
                    Y_local_1[cse_var_146] = Y_local_1[cse_var_146] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_147: T.int32 = i_2_1_s * 8 + 1
                    Y_local_1[cse_var_147] = Y_local_1[cse_var_147] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_148: T.int32 = i_2_1_s * 8 + 2
                    Y_local_1[cse_var_148] = Y_local_1[cse_var_148] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_149: T.int32 = i_2_1_s * 8 + 3
                    Y_local_1[cse_var_149] = Y_local_1[cse_var_149] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_150: T.int32 = i_2_1_s * 8 + 4
                    Y_local_1[cse_var_150] = Y_local_1[cse_var_150] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_151: T.int32 = i_2_1_s * 8 + 5
                    Y_local_1[cse_var_151] = Y_local_1[cse_var_151] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_152: T.int32 = i_2_1_s * 8 + 6
                    Y_local_1[cse_var_152] = Y_local_1[cse_var_152] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_153: T.int32 = i_2_1_s * 8 + 7
                    Y_local_1[cse_var_153] = Y_local_1[cse_var_153] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
            for ax0_1_s in T.serial(4):
                if ax0_1_s < 2:
                    A_shared_dyn_local_1[ax0_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 1296]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1280:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1280 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_154: T.int32 = i_2_1_s * 8
                    Y_local_1[cse_var_154] = Y_local_1[cse_var_154] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_155: T.int32 = i_2_1_s * 8 + 1
                    Y_local_1[cse_var_155] = Y_local_1[cse_var_155] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_156: T.int32 = i_2_1_s * 8 + 2
                    Y_local_1[cse_var_156] = Y_local_1[cse_var_156] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_157: T.int32 = i_2_1_s * 8 + 3
                    Y_local_1[cse_var_157] = Y_local_1[cse_var_157] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[11]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_158: T.int32 = i_2_1_s * 8 + 4
                    Y_local_1[cse_var_158] = Y_local_1[cse_var_158] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_159: T.int32 = i_2_1_s * 8 + 5
                    Y_local_1[cse_var_159] = Y_local_1[cse_var_159] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_160: T.int32 = i_2_1_s * 8 + 6
                    Y_local_1[cse_var_160] = Y_local_1[cse_var_160] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_161: T.int32 = i_2_1_s * 8 + 7
                    Y_local_1[cse_var_161] = Y_local_1[cse_var_161] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
            for ax0_1_s in T.serial(4):
                if ax0_1_s < 2:
                    A_shared_dyn_local_1[ax0_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 1297]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1344:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1344 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_162: T.int32 = i_2_1_s * 8
                    Y_local_1[cse_var_162] = Y_local_1[cse_var_162] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_163: T.int32 = i_2_1_s * 8 + 1
                    Y_local_1[cse_var_163] = Y_local_1[cse_var_163] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_164: T.int32 = i_2_1_s * 8 + 2
                    Y_local_1[cse_var_164] = Y_local_1[cse_var_164] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_165: T.int32 = i_2_1_s * 8 + 3
                    Y_local_1[cse_var_165] = Y_local_1[cse_var_165] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_166: T.int32 = i_2_1_s * 8 + 4
                    Y_local_1[cse_var_166] = Y_local_1[cse_var_166] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_167: T.int32 = i_2_1_s * 8 + 5
                    Y_local_1[cse_var_167] = Y_local_1[cse_var_167] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_168: T.int32 = i_2_1_s * 8 + 6
                    Y_local_1[cse_var_168] = Y_local_1[cse_var_168] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_169: T.int32 = i_2_1_s * 8 + 7
                    Y_local_1[cse_var_169] = Y_local_1[cse_var_169] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
            for ax0_1_s in T.serial(4):
                if ax0_1_s < 2:
                    A_shared_dyn_local_1[ax0_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 1298]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1408:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1408 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_170: T.int32 = i_2_1_s * 8
                    Y_local_1[cse_var_170] = Y_local_1[cse_var_170] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_171: T.int32 = i_2_1_s * 8 + 1
                    Y_local_1[cse_var_171] = Y_local_1[cse_var_171] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_172: T.int32 = i_2_1_s * 8 + 2
                    Y_local_1[cse_var_172] = Y_local_1[cse_var_172] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_173: T.int32 = i_2_1_s * 8 + 3
                    Y_local_1[cse_var_173] = Y_local_1[cse_var_173] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[11]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_174: T.int32 = i_2_1_s * 8 + 4
                    Y_local_1[cse_var_174] = Y_local_1[cse_var_174] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_175: T.int32 = i_2_1_s * 8 + 5
                    Y_local_1[cse_var_175] = Y_local_1[cse_var_175] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_176: T.int32 = i_2_1_s * 8 + 6
                    Y_local_1[cse_var_176] = Y_local_1[cse_var_176] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_177: T.int32 = i_2_1_s * 8 + 7
                    Y_local_1[cse_var_177] = Y_local_1[cse_var_177] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
            for ax0_1_s in T.serial(4):
                if ax0_1_s < 2:
                    A_shared_dyn_local_1[ax0_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 1299]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1472:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1472 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_178: T.int32 = i_2_1_s * 8
                    Y_local_1[cse_var_178] = Y_local_1[cse_var_178] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_179: T.int32 = i_2_1_s * 8 + 1
                    Y_local_1[cse_var_179] = Y_local_1[cse_var_179] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_180: T.int32 = i_2_1_s * 8 + 2
                    Y_local_1[cse_var_180] = Y_local_1[cse_var_180] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_181: T.int32 = i_2_1_s * 8 + 3
                    Y_local_1[cse_var_181] = Y_local_1[cse_var_181] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_182: T.int32 = i_2_1_s * 8 + 4
                    Y_local_1[cse_var_182] = Y_local_1[cse_var_182] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_183: T.int32 = i_2_1_s * 8 + 5
                    Y_local_1[cse_var_183] = Y_local_1[cse_var_183] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_184: T.int32 = i_2_1_s * 8 + 6
                    Y_local_1[cse_var_184] = Y_local_1[cse_var_184] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_185: T.int32 = i_2_1_s * 8 + 7
                    Y_local_1[cse_var_185] = Y_local_1[cse_var_185] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
        for ax0_1_s in T.serial(4):
            if ax0_1_s < 2:
                A_shared_dyn_local_1[ax0_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 1920]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1536:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1536 + 4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_186: T.int32 = i_2_1_s * 8
                Y_local_1[cse_var_186] = Y_local_1[cse_var_186] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[8]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_187: T.int32 = i_2_1_s * 8 + 1
                Y_local_1[cse_var_187] = Y_local_1[cse_var_187] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[9]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_188: T.int32 = i_2_1_s * 8 + 2
                Y_local_1[cse_var_188] = Y_local_1[cse_var_188] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[10]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_189: T.int32 = i_2_1_s * 8 + 3
                Y_local_1[cse_var_189] = Y_local_1[cse_var_189] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[11]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_190: T.int32 = i_2_1_s * 8 + 4
                Y_local_1[cse_var_190] = Y_local_1[cse_var_190] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_191: T.int32 = i_2_1_s * 8 + 5
                Y_local_1[cse_var_191] = Y_local_1[cse_var_191] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_192: T.int32 = i_2_1_s * 8 + 6
                Y_local_1[cse_var_192] = Y_local_1[cse_var_192] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_193: T.int32 = i_2_1_s * 8 + 7
                Y_local_1[cse_var_193] = Y_local_1[cse_var_193] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 0)
            for ax0_1_s in T.serial(4):
                if ax0_1_s < 2:
                    A_shared_dyn_local_1[ax0_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 1921]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1600:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1600 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_194: T.int32 = i_2_1_s * 8
                    Y_local_1[cse_var_194] = Y_local_1[cse_var_194] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_195: T.int32 = i_2_1_s * 8 + 1
                    Y_local_1[cse_var_195] = Y_local_1[cse_var_195] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_196: T.int32 = i_2_1_s * 8 + 2
                    Y_local_1[cse_var_196] = Y_local_1[cse_var_196] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_197: T.int32 = i_2_1_s * 8 + 3
                    Y_local_1[cse_var_197] = Y_local_1[cse_var_197] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_198: T.int32 = i_2_1_s * 8 + 4
                    Y_local_1[cse_var_198] = Y_local_1[cse_var_198] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_199: T.int32 = i_2_1_s * 8 + 5
                    Y_local_1[cse_var_199] = Y_local_1[cse_var_199] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_200: T.int32 = i_2_1_s * 8 + 6
                    Y_local_1[cse_var_200] = Y_local_1[cse_var_200] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_201: T.int32 = i_2_1_s * 8 + 7
                    Y_local_1[cse_var_201] = Y_local_1[cse_var_201] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
            for ax0_1_s in T.serial(4):
                if ax0_1_s < 2:
                    A_shared_dyn_local_1[ax0_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 1922]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1664:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1664 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_202: T.int32 = i_2_1_s * 8
                    Y_local_1[cse_var_202] = Y_local_1[cse_var_202] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_203: T.int32 = i_2_1_s * 8 + 1
                    Y_local_1[cse_var_203] = Y_local_1[cse_var_203] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_204: T.int32 = i_2_1_s * 8 + 2
                    Y_local_1[cse_var_204] = Y_local_1[cse_var_204] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_205: T.int32 = i_2_1_s * 8 + 3
                    Y_local_1[cse_var_205] = Y_local_1[cse_var_205] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[11]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_206: T.int32 = i_2_1_s * 8 + 4
                    Y_local_1[cse_var_206] = Y_local_1[cse_var_206] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_207: T.int32 = i_2_1_s * 8 + 5
                    Y_local_1[cse_var_207] = Y_local_1[cse_var_207] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_208: T.int32 = i_2_1_s * 8 + 6
                    Y_local_1[cse_var_208] = Y_local_1[cse_var_208] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_209: T.int32 = i_2_1_s * 8 + 7
                    Y_local_1[cse_var_209] = Y_local_1[cse_var_209] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
            for ax0_1_s in T.serial(4):
                if ax0_1_s < 2:
                    A_shared_dyn_local_1[ax0_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 1923]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1728:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1728 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_210: T.int32 = i_2_1_s * 8
                    Y_local_1[cse_var_210] = Y_local_1[cse_var_210] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_211: T.int32 = i_2_1_s * 8 + 1
                    Y_local_1[cse_var_211] = Y_local_1[cse_var_211] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_212: T.int32 = i_2_1_s * 8 + 2
                    Y_local_1[cse_var_212] = Y_local_1[cse_var_212] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_213: T.int32 = i_2_1_s * 8 + 3
                    Y_local_1[cse_var_213] = Y_local_1[cse_var_213] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_214: T.int32 = i_2_1_s * 8 + 4
                    Y_local_1[cse_var_214] = Y_local_1[cse_var_214] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_215: T.int32 = i_2_1_s * 8 + 5
                    Y_local_1[cse_var_215] = Y_local_1[cse_var_215] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_216: T.int32 = i_2_1_s * 8 + 6
                    Y_local_1[cse_var_216] = Y_local_1[cse_var_216] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_217: T.int32 = i_2_1_s * 8 + 7
                    Y_local_1[cse_var_217] = Y_local_1[cse_var_217] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
            for ax0_1_s in T.serial(4):
                if ax0_1_s < 2:
                    A_shared_dyn_local_1[ax0_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 1936]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1792:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1792 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_218: T.int32 = i_2_1_s * 8
                    Y_local_1[cse_var_218] = Y_local_1[cse_var_218] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_219: T.int32 = i_2_1_s * 8 + 1
                    Y_local_1[cse_var_219] = Y_local_1[cse_var_219] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_220: T.int32 = i_2_1_s * 8 + 2
                    Y_local_1[cse_var_220] = Y_local_1[cse_var_220] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_221: T.int32 = i_2_1_s * 8 + 3
                    Y_local_1[cse_var_221] = Y_local_1[cse_var_221] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[11]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_222: T.int32 = i_2_1_s * 8 + 4
                    Y_local_1[cse_var_222] = Y_local_1[cse_var_222] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_223: T.int32 = i_2_1_s * 8 + 5
                    Y_local_1[cse_var_223] = Y_local_1[cse_var_223] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_224: T.int32 = i_2_1_s * 8 + 6
                    Y_local_1[cse_var_224] = Y_local_1[cse_var_224] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_225: T.int32 = i_2_1_s * 8 + 7
                    Y_local_1[cse_var_225] = Y_local_1[cse_var_225] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
            for ax0_1_s in T.serial(4):
                if ax0_1_s < 2:
                    A_shared_dyn_local_1[ax0_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 1937]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1856:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1856 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_226: T.int32 = i_2_1_s * 8
                    Y_local_1[cse_var_226] = Y_local_1[cse_var_226] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_227: T.int32 = i_2_1_s * 8 + 1
                    Y_local_1[cse_var_227] = Y_local_1[cse_var_227] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_228: T.int32 = i_2_1_s * 8 + 2
                    Y_local_1[cse_var_228] = Y_local_1[cse_var_228] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_229: T.int32 = i_2_1_s * 8 + 3
                    Y_local_1[cse_var_229] = Y_local_1[cse_var_229] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_230: T.int32 = i_2_1_s * 8 + 4
                    Y_local_1[cse_var_230] = Y_local_1[cse_var_230] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_231: T.int32 = i_2_1_s * 8 + 5
                    Y_local_1[cse_var_231] = Y_local_1[cse_var_231] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_232: T.int32 = i_2_1_s * 8 + 6
                    Y_local_1[cse_var_232] = Y_local_1[cse_var_232] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_233: T.int32 = i_2_1_s * 8 + 7
                    Y_local_1[cse_var_233] = Y_local_1[cse_var_233] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
            for ax0_1_s in T.serial(4):
                if ax0_1_s < 2:
                    A_shared_dyn_local_1[ax0_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 1938]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1920:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1920 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_234: T.int32 = i_2_1_s * 8
                    Y_local_1[cse_var_234] = Y_local_1[cse_var_234] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[8]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_235: T.int32 = i_2_1_s * 8 + 1
                    Y_local_1[cse_var_235] = Y_local_1[cse_var_235] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[9]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_236: T.int32 = i_2_1_s * 8 + 2
                    Y_local_1[cse_var_236] = Y_local_1[cse_var_236] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[10]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_237: T.int32 = i_2_1_s * 8 + 3
                    Y_local_1[cse_var_237] = Y_local_1[cse_var_237] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[11]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_238: T.int32 = i_2_1_s * 8 + 4
                    Y_local_1[cse_var_238] = Y_local_1[cse_var_238] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_239: T.int32 = i_2_1_s * 8 + 5
                    Y_local_1[cse_var_239] = Y_local_1[cse_var_239] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_240: T.int32 = i_2_1_s * 8 + 6
                    Y_local_1[cse_var_240] = Y_local_1[cse_var_240] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_241: T.int32 = i_2_1_s * 8 + 7
                    Y_local_1[cse_var_241] = Y_local_1[cse_var_241] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
            for ax0_1_s in T.serial(4):
                if ax0_1_s < 2:
                    A_shared_dyn_local_1[ax0_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 1939]
            for ax1_0 in T.serial(2):
                B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1984:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 1984 + 4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_242: T.int32 = i_2_1_s * 8
                    Y_local_1[cse_var_242] = Y_local_1[cse_var_242] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_243: T.int32 = i_2_1_s * 8 + 1
                    Y_local_1[cse_var_243] = Y_local_1[cse_var_243] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_244: T.int32 = i_2_1_s * 8 + 2
                    Y_local_1[cse_var_244] = Y_local_1[cse_var_244] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_245: T.int32 = i_2_1_s * 8 + 3
                    Y_local_1[cse_var_245] = Y_local_1[cse_var_245] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_246: T.int32 = i_2_1_s * 8 + 4
                    Y_local_1[cse_var_246] = Y_local_1[cse_var_246] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_247: T.int32 = i_2_1_s * 8 + 5
                    Y_local_1[cse_var_247] = Y_local_1[cse_var_247] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_248: T.int32 = i_2_1_s * 8 + 6
                    Y_local_1[cse_var_248] = Y_local_1[cse_var_248] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
            for i_2_1_s in T.serial(4):
                if i_2_1_s < 2:
                    cse_var_249: T.int32 = i_2_1_s * 8 + 7
                    Y_local_1[cse_var_249] = Y_local_1[cse_var_249] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
        for ax0_1_s in T.serial(4):
            if ax0_1_s < 2:
                A_shared_dyn_local_1[ax0_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 2560]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 2048:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 2048 + 4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_250: T.int32 = i_2_1_s * 8
                Y_local_1[cse_var_250] = Y_local_1[cse_var_250] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[8]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_251: T.int32 = i_2_1_s * 8 + 1
                Y_local_1[cse_var_251] = Y_local_1[cse_var_251] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[9]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_252: T.int32 = i_2_1_s * 8 + 2
                Y_local_1[cse_var_252] = Y_local_1[cse_var_252] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[10]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_253: T.int32 = i_2_1_s * 8 + 3
                Y_local_1[cse_var_253] = Y_local_1[cse_var_253] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[11]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_254: T.int32 = i_2_1_s * 8 + 4
                Y_local_1[cse_var_254] = Y_local_1[cse_var_254] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_255: T.int32 = i_2_1_s * 8 + 5
                Y_local_1[cse_var_255] = Y_local_1[cse_var_255] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_256: T.int32 = i_2_1_s * 8 + 6
                Y_local_1[cse_var_256] = Y_local_1[cse_var_256] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_257: T.int32 = i_2_1_s * 8 + 7
                Y_local_1[cse_var_257] = Y_local_1[cse_var_257] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
        for ax0_1_s in T.serial(4):
            if ax0_1_s < 2:
                A_shared_dyn_local_1[ax0_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 2561]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 2112:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 2112 + 4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_258: T.int32 = i_2_1_s * 8
                Y_local_1[cse_var_258] = Y_local_1[cse_var_258] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_259: T.int32 = i_2_1_s * 8 + 1
                Y_local_1[cse_var_259] = Y_local_1[cse_var_259] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_260: T.int32 = i_2_1_s * 8 + 2
                Y_local_1[cse_var_260] = Y_local_1[cse_var_260] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_261: T.int32 = i_2_1_s * 8 + 3
                Y_local_1[cse_var_261] = Y_local_1[cse_var_261] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_262: T.int32 = i_2_1_s * 8 + 4
                Y_local_1[cse_var_262] = Y_local_1[cse_var_262] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_263: T.int32 = i_2_1_s * 8 + 5
                Y_local_1[cse_var_263] = Y_local_1[cse_var_263] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_264: T.int32 = i_2_1_s * 8 + 6
                Y_local_1[cse_var_264] = Y_local_1[cse_var_264] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_265: T.int32 = i_2_1_s * 8 + 7
                Y_local_1[cse_var_265] = Y_local_1[cse_var_265] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
        for ax0_1_s in T.serial(4):
            if ax0_1_s < 2:
                A_shared_dyn_local_1[ax0_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 2562]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 2176:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 2176 + 4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_266: T.int32 = i_2_1_s * 8
                Y_local_1[cse_var_266] = Y_local_1[cse_var_266] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[8]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_267: T.int32 = i_2_1_s * 8 + 1
                Y_local_1[cse_var_267] = Y_local_1[cse_var_267] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[9]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_268: T.int32 = i_2_1_s * 8 + 2
                Y_local_1[cse_var_268] = Y_local_1[cse_var_268] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[10]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_269: T.int32 = i_2_1_s * 8 + 3
                Y_local_1[cse_var_269] = Y_local_1[cse_var_269] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[11]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_270: T.int32 = i_2_1_s * 8 + 4
                Y_local_1[cse_var_270] = Y_local_1[cse_var_270] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_271: T.int32 = i_2_1_s * 8 + 5
                Y_local_1[cse_var_271] = Y_local_1[cse_var_271] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_272: T.int32 = i_2_1_s * 8 + 6
                Y_local_1[cse_var_272] = Y_local_1[cse_var_272] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_273: T.int32 = i_2_1_s * 8 + 7
                Y_local_1[cse_var_273] = Y_local_1[cse_var_273] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
        for ax0_1_s in T.serial(4):
            if ax0_1_s < 2:
                A_shared_dyn_local_1[ax0_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 2563]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 2240:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 2240 + 4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_274: T.int32 = i_2_1_s * 8
                Y_local_1[cse_var_274] = Y_local_1[cse_var_274] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_275: T.int32 = i_2_1_s * 8 + 1
                Y_local_1[cse_var_275] = Y_local_1[cse_var_275] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_276: T.int32 = i_2_1_s * 8 + 2
                Y_local_1[cse_var_276] = Y_local_1[cse_var_276] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_277: T.int32 = i_2_1_s * 8 + 3
                Y_local_1[cse_var_277] = Y_local_1[cse_var_277] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_278: T.int32 = i_2_1_s * 8 + 4
                Y_local_1[cse_var_278] = Y_local_1[cse_var_278] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_279: T.int32 = i_2_1_s * 8 + 5
                Y_local_1[cse_var_279] = Y_local_1[cse_var_279] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_280: T.int32 = i_2_1_s * 8 + 6
                Y_local_1[cse_var_280] = Y_local_1[cse_var_280] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_281: T.int32 = i_2_1_s * 8 + 7
                Y_local_1[cse_var_281] = Y_local_1[cse_var_281] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
        for ax0_1_s in T.serial(4):
            if ax0_1_s < 2:
                A_shared_dyn_local_1[ax0_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 2576]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 2304:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 2304 + 4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_282: T.int32 = i_2_1_s * 8
                Y_local_1[cse_var_282] = Y_local_1[cse_var_282] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[8]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_283: T.int32 = i_2_1_s * 8 + 1
                Y_local_1[cse_var_283] = Y_local_1[cse_var_283] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[9]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_284: T.int32 = i_2_1_s * 8 + 2
                Y_local_1[cse_var_284] = Y_local_1[cse_var_284] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[10]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_285: T.int32 = i_2_1_s * 8 + 3
                Y_local_1[cse_var_285] = Y_local_1[cse_var_285] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[11]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_286: T.int32 = i_2_1_s * 8 + 4
                Y_local_1[cse_var_286] = Y_local_1[cse_var_286] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_287: T.int32 = i_2_1_s * 8 + 5
                Y_local_1[cse_var_287] = Y_local_1[cse_var_287] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_288: T.int32 = i_2_1_s * 8 + 6
                Y_local_1[cse_var_288] = Y_local_1[cse_var_288] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_289: T.int32 = i_2_1_s * 8 + 7
                Y_local_1[cse_var_289] = Y_local_1[cse_var_289] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
        for ax0_1_s in T.serial(4):
            if ax0_1_s < 2:
                A_shared_dyn_local_1[ax0_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 2577]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 2368:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 2368 + 4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_290: T.int32 = i_2_1_s * 8
                Y_local_1[cse_var_290] = Y_local_1[cse_var_290] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_291: T.int32 = i_2_1_s * 8 + 1
                Y_local_1[cse_var_291] = Y_local_1[cse_var_291] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_292: T.int32 = i_2_1_s * 8 + 2
                Y_local_1[cse_var_292] = Y_local_1[cse_var_292] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_293: T.int32 = i_2_1_s * 8 + 3
                Y_local_1[cse_var_293] = Y_local_1[cse_var_293] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_294: T.int32 = i_2_1_s * 8 + 4
                Y_local_1[cse_var_294] = Y_local_1[cse_var_294] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_295: T.int32 = i_2_1_s * 8 + 5
                Y_local_1[cse_var_295] = Y_local_1[cse_var_295] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_296: T.int32 = i_2_1_s * 8 + 6
                Y_local_1[cse_var_296] = Y_local_1[cse_var_296] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_297: T.int32 = i_2_1_s * 8 + 7
                Y_local_1[cse_var_297] = Y_local_1[cse_var_297] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
        for ax0_1_s in T.serial(4):
            if ax0_1_s < 2:
                A_shared_dyn_local_1[ax0_1_s] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 2578]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4:ax1_0 * 4 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 2432:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 2432 + 4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_298: T.int32 = i_2_1_s * 8
                Y_local_1[cse_var_298] = Y_local_1[cse_var_298] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[8]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_299: T.int32 = i_2_1_s * 8 + 1
                Y_local_1[cse_var_299] = Y_local_1[cse_var_299] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[9]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_300: T.int32 = i_2_1_s * 8 + 2
                Y_local_1[cse_var_300] = Y_local_1[cse_var_300] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[10]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_301: T.int32 = i_2_1_s * 8 + 3
                Y_local_1[cse_var_301] = Y_local_1[cse_var_301] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[11]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_302: T.int32 = i_2_1_s * 8 + 4
                Y_local_1[cse_var_302] = Y_local_1[cse_var_302] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_303: T.int32 = i_2_1_s * 8 + 5
                Y_local_1[cse_var_303] = Y_local_1[cse_var_303] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_304: T.int32 = i_2_1_s * 8 + 6
                Y_local_1[cse_var_304] = Y_local_1[cse_var_304] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_305: T.int32 = i_2_1_s * 8 + 7
                Y_local_1[cse_var_305] = Y_local_1[cse_var_305] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
        for ax0_1_s in T.serial(4):
            if ax0_1_s < 2:
                A_shared_dyn_local_1[ax0_1_s + 2] = A_shared_dyn_1[threadIdx_x % 64 // 8 * 80 + threadIdx_x % 2 * 40 + ax0_1_s * 20 + 2579]
        for ax1_0 in T.serial(2):
            B_shared_dyn_local_1[ax1_0 * 4 + 8:ax1_0 * 4 + 8 + 4] = B_shared_dyn_1[ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 2496:ax1_0 * 32 + threadIdx_x // 64 * 16 + threadIdx_x % 8 // 2 * 4 + 2496 + 4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_306: T.int32 = i_2_1_s * 8
                Y_local_1[cse_var_306] = Y_local_1[cse_var_306] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[0]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_307: T.int32 = i_2_1_s * 8 + 1
                Y_local_1[cse_var_307] = Y_local_1[cse_var_307] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[1]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_308: T.int32 = i_2_1_s * 8 + 2
                Y_local_1[cse_var_308] = Y_local_1[cse_var_308] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[2]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_309: T.int32 = i_2_1_s * 8 + 3
                Y_local_1[cse_var_309] = Y_local_1[cse_var_309] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[3]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_310: T.int32 = i_2_1_s * 8 + 4
                Y_local_1[cse_var_310] = Y_local_1[cse_var_310] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[4]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_311: T.int32 = i_2_1_s * 8 + 5
                Y_local_1[cse_var_311] = Y_local_1[cse_var_311] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[5]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_312: T.int32 = i_2_1_s * 8 + 6
                Y_local_1[cse_var_312] = Y_local_1[cse_var_312] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[6]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_313: T.int32 = i_2_1_s * 8 + 7
                Y_local_1[cse_var_313] = Y_local_1[cse_var_313] + A_shared_dyn_local_1[i_2_1_s] * B_shared_dyn_local_1[7]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_314: T.int32 = i_2_1_s * 8
                Y_local_1[cse_var_314] = Y_local_1[cse_var_314] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[8]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_315: T.int32 = i_2_1_s * 8 + 1
                Y_local_1[cse_var_315] = Y_local_1[cse_var_315] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[9]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_316: T.int32 = i_2_1_s * 8 + 2
                Y_local_1[cse_var_316] = Y_local_1[cse_var_316] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[10]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_317: T.int32 = i_2_1_s * 8 + 3
                Y_local_1[cse_var_317] = Y_local_1[cse_var_317] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[11]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_318: T.int32 = i_2_1_s * 8 + 4
                Y_local_1[cse_var_318] = Y_local_1[cse_var_318] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[12]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_319: T.int32 = i_2_1_s * 8 + 5
                Y_local_1[cse_var_319] = Y_local_1[cse_var_319] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[13]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_320: T.int32 = i_2_1_s * 8 + 6
                Y_local_1[cse_var_320] = Y_local_1[cse_var_320] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[14]
        for i_2_1_s in T.serial(4):
            if i_2_1_s < 2:
                cse_var_321: T.int32 = i_2_1_s * 8 + 7
                Y_local_1[cse_var_321] = Y_local_1[cse_var_321] + A_shared_dyn_local_1[i_2_1_s + 2] * B_shared_dyn_local_1[15]
        for ax1_0 in T.serial(2):
            cse_var_322: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 4 * 8192 + threadIdx_x % 64 // 8 * 1024 + threadIdx_x % 2 * 512 + blockIdx_x % 4 * 64 + threadIdx_x // 64 * 32 + threadIdx_x % 8 // 2 * 8 + cse_var_322:blockIdx_x // 4 * 8192 + threadIdx_x % 64 // 8 * 1024 + threadIdx_x % 2 * 512 + blockIdx_x % 4 * 64 + threadIdx_x // 64 * 32 + threadIdx_x % 8 // 2 * 8 + cse_var_322 + 4] = Y_local_1[cse_var_322:cse_var_322 + 4]
        for ax1_0 in T.serial(2):
            cse_var_323: T.int32 = ax1_0 * 4
            Y_1[blockIdx_x // 4 * 8192 + threadIdx_x % 64 // 8 * 1024 + threadIdx_x % 2 * 512 + blockIdx_x % 4 * 64 + threadIdx_x // 64 * 32 + threadIdx_x % 8 // 2 * 8 + cse_var_323 + 256:blockIdx_x // 4 * 8192 + threadIdx_x % 64 // 8 * 1024 + threadIdx_x % 2 * 512 + blockIdx_x % 4 * 64 + threadIdx_x // 64 * 32 + threadIdx_x % 8 // 2 * 8 + cse_var_323 + 256 + 4] = Y_local_1[cse_var_323 + 8:cse_var_323 + 8 + 4]
    

