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
        T.launch_thread(blockIdx_x, 128)
        Y_local = T.allocate([56], "float32", "local")
        Y_local_1 = T.buffer_decl([64], dtype="float32", data=Y_local, scope="local")
        A_shared = T.allocate([1568], "float32", "shared")
        A_shared_1 = T.buffer_decl([1568], dtype="float32", data=A_shared, scope="shared")
        B_shared = T.allocate([3136], "float32", "shared")
        B_shared_1 = T.buffer_decl([3136], dtype="float32", data=B_shared, scope="shared")
        T.launch_thread(threadIdx_x, 112)
        for i_3_init, j_3_init in T.grid(4, 2):
            cse_var_1: T.int32 = i_3_init * 2 + j_3_init
            Y_local_1[cse_var_1] = T.float32(0)
            Y_local_1[cse_var_1 + 8] = T.float32(0)
            Y_local_1[cse_var_1 + 16] = T.float32(0)
            Y_local_1[cse_var_1 + 24] = T.float32(0)
            Y_local_1[cse_var_1 + 32] = T.float32(0)
            Y_local_1[cse_var_1 + 40] = T.float32(0)
            Y_local_1[cse_var_1 + 48] = T.float32(0)
        for k_0 in T.serial(32):
            for ax0_ax1_fused_0 in T.serial(14):
                A_shared_1[ax0_ax1_fused_0 * 112 + threadIdx_x] = A_1[k_0 * 25088 + ax0_ax1_fused_0 * 1792 + threadIdx_x // 56 * 896 + blockIdx_x // 8 * 56 + threadIdx_x % 56]
            for ax0_ax1_fused_0 in T.serial(7):
                B_shared_1[ax0_ax1_fused_0 * 448 + threadIdx_x * 4:ax0_ax1_fused_0 * 448 + threadIdx_x * 4 + 4] = B_1[k_0 * 25088 + ax0_ax1_fused_0 * 3584 + threadIdx_x // 28 * 896 + blockIdx_x % 8 * 112 + threadIdx_x % 28 * 4:k_0 * 25088 + ax0_ax1_fused_0 * 3584 + threadIdx_x // 28 * 896 + blockIdx_x % 8 * 112 + threadIdx_x % 28 * 4 + 4]
            for k_1, i_3, j_3, k_2 in T.grid(4, 4, 2, 7):
                cse_var_8: T.int32 = i_3 * 2 + j_3
                cse_var_7: T.int32 = cse_var_8 + 8
                cse_var_6: T.int32 = cse_var_8 + 48
                cse_var_5: T.int32 = cse_var_8 + 40
                cse_var_4: T.int32 = cse_var_8 + 32
                cse_var_3: T.int32 = cse_var_8 + 24
                cse_var_2: T.int32 = cse_var_8 + 16
                Y_local_1[cse_var_8] = Y_local_1[cse_var_8] + A_shared_1[k_1 * 392 + k_2 * 56 + threadIdx_x // 8 * 4 + i_3] * B_shared_1[k_1 * 784 + k_2 * 112 + threadIdx_x % 8 * 2 + j_3]
                Y_local_1[cse_var_7] = Y_local_1[cse_var_7] + A_shared_1[k_1 * 392 + k_2 * 56 + threadIdx_x // 8 * 4 + i_3] * B_shared_1[k_1 * 784 + k_2 * 112 + threadIdx_x % 8 * 2 + j_3 + 16]
                Y_local_1[cse_var_2] = Y_local_1[cse_var_2] + A_shared_1[k_1 * 392 + k_2 * 56 + threadIdx_x // 8 * 4 + i_3] * B_shared_1[k_1 * 784 + k_2 * 112 + threadIdx_x % 8 * 2 + j_3 + 32]
                Y_local_1[cse_var_3] = Y_local_1[cse_var_3] + A_shared_1[k_1 * 392 + k_2 * 56 + threadIdx_x // 8 * 4 + i_3] * B_shared_1[k_1 * 784 + k_2 * 112 + threadIdx_x % 8 * 2 + j_3 + 48]
                Y_local_1[cse_var_4] = Y_local_1[cse_var_4] + A_shared_1[k_1 * 392 + k_2 * 56 + threadIdx_x // 8 * 4 + i_3] * B_shared_1[k_1 * 784 + k_2 * 112 + threadIdx_x % 8 * 2 + j_3 + 64]
                Y_local_1[cse_var_5] = Y_local_1[cse_var_5] + A_shared_1[k_1 * 392 + k_2 * 56 + threadIdx_x // 8 * 4 + i_3] * B_shared_1[k_1 * 784 + k_2 * 112 + threadIdx_x % 8 * 2 + j_3 + 80]
                Y_local_1[cse_var_6] = Y_local_1[cse_var_6] + A_shared_1[k_1 * 392 + k_2 * 56 + threadIdx_x // 8 * 4 + i_3] * B_shared_1[k_1 * 784 + k_2 * 112 + threadIdx_x % 8 * 2 + j_3 + 96]
        for ax0, ax1 in T.grid(4, 2):
            cse_var_9: T.int32 = ax0 * 2 + ax1
            Y_1[blockIdx_x // 8 * 50176 + threadIdx_x // 8 * 3584 + ax0 * 896 + blockIdx_x % 8 * 112 + threadIdx_x % 8 * 2 + ax1] = Y_local_1[cse_var_9]
            Y_1[blockIdx_x // 8 * 50176 + threadIdx_x // 8 * 3584 + ax0 * 896 + blockIdx_x % 8 * 112 + threadIdx_x % 8 * 2 + ax1 + 16] = Y_local_1[cse_var_9 + 8]
            Y_1[blockIdx_x // 8 * 50176 + threadIdx_x // 8 * 3584 + ax0 * 896 + blockIdx_x % 8 * 112 + threadIdx_x % 8 * 2 + ax1 + 32] = Y_local_1[cse_var_9 + 16]
            Y_1[blockIdx_x // 8 * 50176 + threadIdx_x // 8 * 3584 + ax0 * 896 + blockIdx_x % 8 * 112 + threadIdx_x % 8 * 2 + ax1 + 48] = Y_local_1[cse_var_9 + 24]
            Y_1[blockIdx_x // 8 * 50176 + threadIdx_x // 8 * 3584 + ax0 * 896 + blockIdx_x % 8 * 112 + threadIdx_x % 8 * 2 + ax1 + 64] = Y_local_1[cse_var_9 + 32]
            Y_1[blockIdx_x // 8 * 50176 + threadIdx_x // 8 * 3584 + ax0 * 896 + blockIdx_x % 8 * 112 + threadIdx_x % 8 * 2 + ax1 + 80] = Y_local_1[cse_var_9 + 40]
            Y_1[blockIdx_x // 8 * 50176 + threadIdx_x // 8 * 3584 + ax0 * 896 + blockIdx_x % 8 * 112 + threadIdx_x % 8 * 2 + ax1 + 96] = Y_local_1[cse_var_9 + 48]
    

