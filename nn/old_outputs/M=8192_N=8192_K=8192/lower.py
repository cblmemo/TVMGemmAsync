# from tvm.script import tir as T
@tvm.script.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer[(8192, 8192), "float32"], B: T.Buffer[(8192, 8192), "float32"], Y: T.Buffer[(8192, 8192), "float32"]):
        # function attr dict
        T.func_attr({"global_symbol": "main", "tir.noalias": True})
        # var definition
        threadIdx_x = T.env_thread("threadIdx.x")
        blockIdx_x = T.env_thread("blockIdx.x")
        # buffer definition
        A_1 = T.buffer_decl([67108864], dtype="float32", data=A.data)
        B_1 = T.buffer_decl([67108864], dtype="float32", data=B.data)
        Y_1 = T.buffer_decl([67108864], dtype="float32", data=Y.data)
        # body
        T.launch_thread(blockIdx_x, 4096)
        Y_local = T.allocate([128], "float32", "local")
        Y_local_1 = T.buffer_decl([256], dtype="float32", data=Y_local, scope="local")
        A_shared = T.allocate([2048], "float32", "shared")
        A_shared_1 = T.buffer_decl([2048], dtype="float32", data=A_shared, scope="shared")
        B_shared = T.allocate([2048], "float32", "shared")
        B_shared_1 = T.buffer_decl([2048], dtype="float32", data=B_shared, scope="shared")
        T.launch_thread(threadIdx_x, 128)
        for i_3_init, j_3_init, i_4_init in T.grid(2, 2, 4):
            cse_var_1: T.int32 = i_3_init * 8 + i_4_init * 2 + j_3_init
            Y_local_1[cse_var_1] = T.float32(0)
            Y_local_1[cse_var_1 + 16] = T.float32(0)
            Y_local_1[cse_var_1 + 32] = T.float32(0)
            Y_local_1[cse_var_1 + 48] = T.float32(0)
            Y_local_1[cse_var_1 + 64] = T.float32(0)
            Y_local_1[cse_var_1 + 80] = T.float32(0)
            Y_local_1[cse_var_1 + 96] = T.float32(0)
            Y_local_1[cse_var_1 + 112] = T.float32(0)
        for k_0 in T.serial(512):
            A_shared_1[threadIdx_x * 4:threadIdx_x * 4 + 4] = A_1[blockIdx_x // 64 * 1048576 + threadIdx_x // 4 * 8192 + k_0 * 16 + threadIdx_x % 4 * 4:blockIdx_x // 64 * 1048576 + threadIdx_x // 4 * 8192 + k_0 * 16 + threadIdx_x % 4 * 4 + 4]
            A_shared_1[threadIdx_x * 4 + 512:threadIdx_x * 4 + 512 + 4] = A_1[blockIdx_x // 64 * 1048576 + threadIdx_x // 4 * 8192 + k_0 * 16 + threadIdx_x % 4 * 4 + 262144:blockIdx_x // 64 * 1048576 + threadIdx_x // 4 * 8192 + k_0 * 16 + threadIdx_x % 4 * 4 + 262144 + 4]
            A_shared_1[threadIdx_x * 4 + 1024:threadIdx_x * 4 + 1024 + 4] = A_1[blockIdx_x // 64 * 1048576 + threadIdx_x // 4 * 8192 + k_0 * 16 + threadIdx_x % 4 * 4 + 524288:blockIdx_x // 64 * 1048576 + threadIdx_x // 4 * 8192 + k_0 * 16 + threadIdx_x % 4 * 4 + 524288 + 4]
            A_shared_1[threadIdx_x * 4 + 1536:threadIdx_x * 4 + 1536 + 4] = A_1[blockIdx_x // 64 * 1048576 + threadIdx_x // 4 * 8192 + k_0 * 16 + threadIdx_x % 4 * 4 + 786432:blockIdx_x // 64 * 1048576 + threadIdx_x // 4 * 8192 + k_0 * 16 + threadIdx_x % 4 * 4 + 786432 + 4]
            B_shared_1[threadIdx_x * 4:threadIdx_x * 4 + 4] = B_1[k_0 * 131072 + threadIdx_x // 32 * 8192 + blockIdx_x % 64 * 128 + threadIdx_x % 32 * 4:k_0 * 131072 + threadIdx_x // 32 * 8192 + blockIdx_x % 64 * 128 + threadIdx_x % 32 * 4 + 4]
            B_shared_1[threadIdx_x * 4 + 512:threadIdx_x * 4 + 512 + 4] = B_1[k_0 * 131072 + threadIdx_x // 32 * 8192 + blockIdx_x % 64 * 128 + threadIdx_x % 32 * 4 + 32768:k_0 * 131072 + threadIdx_x // 32 * 8192 + blockIdx_x % 64 * 128 + threadIdx_x % 32 * 4 + 32768 + 4]
            B_shared_1[threadIdx_x * 4 + 1024:threadIdx_x * 4 + 1024 + 4] = B_1[k_0 * 131072 + threadIdx_x // 32 * 8192 + blockIdx_x % 64 * 128 + threadIdx_x % 32 * 4 + 65536:k_0 * 131072 + threadIdx_x // 32 * 8192 + blockIdx_x % 64 * 128 + threadIdx_x % 32 * 4 + 65536 + 4]
            B_shared_1[threadIdx_x * 4 + 1536:threadIdx_x * 4 + 1536 + 4] = B_1[k_0 * 131072 + threadIdx_x // 32 * 8192 + blockIdx_x % 64 * 128 + threadIdx_x % 32 * 4 + 98304:k_0 * 131072 + threadIdx_x // 32 * 8192 + blockIdx_x % 64 * 128 + threadIdx_x % 32 * 4 + 98304 + 4]
            for k_1, i_3, j_3, k_2, i_4 in T.grid(4, 2, 2, 4, 4):
                cse_var_9: T.int32 = i_3 * 8 + i_4 * 2 + j_3
                cse_var_8: T.int32 = cse_var_9 + 96
                cse_var_7: T.int32 = cse_var_9 + 80
                cse_var_6: T.int32 = cse_var_9 + 64
                cse_var_5: T.int32 = cse_var_9 + 48
                cse_var_4: T.int32 = cse_var_9 + 32
                cse_var_3: T.int32 = cse_var_9 + 16
                cse_var_2: T.int32 = cse_var_9 + 112
                Y_local_1[cse_var_9] = Y_local_1[cse_var_9] + A_shared_1[threadIdx_x // 16 * 128 + i_3 * 64 + i_4 * 16 + k_1 * 4 + k_2] * B_shared_1[k_1 * 512 + k_2 * 128 + threadIdx_x % 16 * 2 + j_3]
                Y_local_1[cse_var_3] = Y_local_1[cse_var_3] + A_shared_1[threadIdx_x // 16 * 128 + i_3 * 64 + i_4 * 16 + k_1 * 4 + k_2] * B_shared_1[k_1 * 512 + k_2 * 128 + threadIdx_x % 16 * 2 + j_3 + 32]
                Y_local_1[cse_var_4] = Y_local_1[cse_var_4] + A_shared_1[threadIdx_x // 16 * 128 + i_3 * 64 + i_4 * 16 + k_1 * 4 + k_2] * B_shared_1[k_1 * 512 + k_2 * 128 + threadIdx_x % 16 * 2 + j_3 + 64]
                Y_local_1[cse_var_5] = Y_local_1[cse_var_5] + A_shared_1[threadIdx_x // 16 * 128 + i_3 * 64 + i_4 * 16 + k_1 * 4 + k_2] * B_shared_1[k_1 * 512 + k_2 * 128 + threadIdx_x % 16 * 2 + j_3 + 96]
                Y_local_1[cse_var_6] = Y_local_1[cse_var_6] + A_shared_1[threadIdx_x // 16 * 128 + i_3 * 64 + i_4 * 16 + k_1 * 4 + k_2 + 1024] * B_shared_1[k_1 * 512 + k_2 * 128 + threadIdx_x % 16 * 2 + j_3]
                Y_local_1[cse_var_7] = Y_local_1[cse_var_7] + A_shared_1[threadIdx_x // 16 * 128 + i_3 * 64 + i_4 * 16 + k_1 * 4 + k_2 + 1024] * B_shared_1[k_1 * 512 + k_2 * 128 + threadIdx_x % 16 * 2 + j_3 + 32]
                Y_local_1[cse_var_8] = Y_local_1[cse_var_8] + A_shared_1[threadIdx_x // 16 * 128 + i_3 * 64 + i_4 * 16 + k_1 * 4 + k_2 + 1024] * B_shared_1[k_1 * 512 + k_2 * 128 + threadIdx_x % 16 * 2 + j_3 + 64]
                Y_local_1[cse_var_2] = Y_local_1[cse_var_2] + A_shared_1[threadIdx_x // 16 * 128 + i_3 * 64 + i_4 * 16 + k_1 * 4 + k_2 + 1024] * B_shared_1[k_1 * 512 + k_2 * 128 + threadIdx_x % 16 * 2 + j_3 + 96]
        for ax0 in T.serial(8):
            cse_var_10: T.int32 = ax0 * 2
            Y_1[blockIdx_x // 64 * 1048576 + threadIdx_x // 16 * 65536 + ax0 * 8192 + blockIdx_x % 64 * 128 + threadIdx_x % 16 * 2] = Y_local_1[cse_var_10]
            Y_1[blockIdx_x // 64 * 1048576 + threadIdx_x // 16 * 65536 + ax0 * 8192 + blockIdx_x % 64 * 128 + threadIdx_x % 16 * 2 + 32] = Y_local_1[cse_var_10 + 16]
            Y_1[blockIdx_x // 64 * 1048576 + threadIdx_x // 16 * 65536 + ax0 * 8192 + blockIdx_x % 64 * 128 + threadIdx_x % 16 * 2 + 64] = Y_local_1[cse_var_10 + 32]
            Y_1[blockIdx_x // 64 * 1048576 + threadIdx_x // 16 * 65536 + ax0 * 8192 + blockIdx_x % 64 * 128 + threadIdx_x % 16 * 2 + 96] = Y_local_1[cse_var_10 + 48]
            Y_1[blockIdx_x // 64 * 1048576 + threadIdx_x // 16 * 65536 + ax0 * 8192 + blockIdx_x % 64 * 128 + threadIdx_x % 16 * 2 + 524288] = Y_local_1[cse_var_10 + 64]
            Y_1[blockIdx_x // 64 * 1048576 + threadIdx_x // 16 * 65536 + ax0 * 8192 + blockIdx_x % 64 * 128 + threadIdx_x % 16 * 2 + 524320] = Y_local_1[cse_var_10 + 80]
            Y_1[blockIdx_x // 64 * 1048576 + threadIdx_x // 16 * 65536 + ax0 * 8192 + blockIdx_x % 64 * 128 + threadIdx_x % 16 * 2 + 524352] = Y_local_1[cse_var_10 + 96]
            Y_1[blockIdx_x // 64 * 1048576 + threadIdx_x // 16 * 65536 + ax0 * 8192 + blockIdx_x % 64 * 128 + threadIdx_x % 16 * 2 + 524384] = Y_local_1[cse_var_10 + 112]
            Y_1[blockIdx_x // 64 * 1048576 + threadIdx_x // 16 * 65536 + ax0 * 8192 + blockIdx_x % 64 * 128 + threadIdx_x % 16 * 2 + 1] = Y_local_1[cse_var_10 + 1]
            Y_1[blockIdx_x // 64 * 1048576 + threadIdx_x // 16 * 65536 + ax0 * 8192 + blockIdx_x % 64 * 128 + threadIdx_x % 16 * 2 + 33] = Y_local_1[cse_var_10 + 17]
            Y_1[blockIdx_x // 64 * 1048576 + threadIdx_x // 16 * 65536 + ax0 * 8192 + blockIdx_x % 64 * 128 + threadIdx_x % 16 * 2 + 65] = Y_local_1[cse_var_10 + 33]
            Y_1[blockIdx_x // 64 * 1048576 + threadIdx_x // 16 * 65536 + ax0 * 8192 + blockIdx_x % 64 * 128 + threadIdx_x % 16 * 2 + 97] = Y_local_1[cse_var_10 + 49]
            Y_1[blockIdx_x // 64 * 1048576 + threadIdx_x // 16 * 65536 + ax0 * 8192 + blockIdx_x % 64 * 128 + threadIdx_x % 16 * 2 + 524289] = Y_local_1[cse_var_10 + 65]
            Y_1[blockIdx_x // 64 * 1048576 + threadIdx_x // 16 * 65536 + ax0 * 8192 + blockIdx_x % 64 * 128 + threadIdx_x % 16 * 2 + 524321] = Y_local_1[cse_var_10 + 81]
            Y_1[blockIdx_x // 64 * 1048576 + threadIdx_x // 16 * 65536 + ax0 * 8192 + blockIdx_x % 64 * 128 + threadIdx_x % 16 * 2 + 524353] = Y_local_1[cse_var_10 + 97]
            Y_1[blockIdx_x // 64 * 1048576 + threadIdx_x // 16 * 65536 + ax0 * 8192 + blockIdx_x % 64 * 128 + threadIdx_x % 16 * 2 + 524385] = Y_local_1[cse_var_10 + 113]
    

