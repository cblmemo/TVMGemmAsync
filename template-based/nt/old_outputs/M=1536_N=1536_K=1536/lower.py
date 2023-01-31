# from tvm.script import tir as T
@tvm.script.ir_module
class Module:
    @T.prim_func
    def main(A: T.Buffer[(1536, 1536), "float32"], B: T.Buffer[(1536, 1536), "float32"], Y: T.Buffer[(1536, 1536), "float32"]):
        # function attr dict
        T.func_attr({"global_symbol": "main", "tir.noalias": True})
        # var definition
        threadIdx_x = T.env_thread("threadIdx.x")
        blockIdx_x = T.env_thread("blockIdx.x")
        # buffer definition
        A_1 = T.buffer_decl([2359296], dtype="float32", data=A.data)
        B_1 = T.buffer_decl([2359296], dtype="float32", data=B.data)
        Y_1 = T.buffer_decl([2359296], dtype="float32", data=Y.data)
        # body
        T.launch_thread(blockIdx_x, 192)
        Y_local = T.allocate([96], "float32", "local")
        Y_local_1 = T.buffer_decl([2304], dtype="float32", data=Y_local, scope="local")
        A_shared = T.allocate([768], "float32", "shared")
        A_shared_1 = T.buffer_decl([768], dtype="float32", data=A_shared, scope="shared")
        B_shared = T.allocate([4096], "float32", "shared")
        B_shared_1 = T.buffer_decl([4096], dtype="float32", data=B_shared, scope="shared")
        T.launch_thread(threadIdx_x, 128)
        for i_3_init in T.serial(12):
            cse_var_1: T.int32 = i_3_init * 4
            Y_local_1[cse_var_1] = T.float32(0)
            Y_local_1[cse_var_1 + 48] = T.float32(0)
            Y_local_1[cse_var_1 + 1] = T.float32(0)
            Y_local_1[cse_var_1 + 49] = T.float32(0)
            Y_local_1[cse_var_1 + 2] = T.float32(0)
            Y_local_1[cse_var_1 + 50] = T.float32(0)
            Y_local_1[cse_var_1 + 3] = T.float32(0)
            Y_local_1[cse_var_1 + 51] = T.float32(0)
        for k_0 in T.serial(96):
            cse_var_2: T.int32 = k_0 * 24576
            A_shared_1[threadIdx_x * 2:threadIdx_x * 2 + 2] = A_1[cse_var_2 + threadIdx_x // 24 * 1536 + blockIdx_x // 6 * 48 + threadIdx_x % 24 * 2:cse_var_2 + threadIdx_x // 24 * 1536 + blockIdx_x // 6 * 48 + threadIdx_x % 24 * 2 + 2]
            A_shared_1[threadIdx_x * 2 + 256:threadIdx_x * 2 + 256 + 2] = A_1[cse_var_2 + (threadIdx_x * 2 + 256) // 48 * 1536 + blockIdx_x // 6 * 48 + (threadIdx_x * 2 + 16) % 48:cse_var_2 + (threadIdx_x * 2 + 256) // 48 * 1536 + blockIdx_x // 6 * 48 + (threadIdx_x * 2 + 16) % 48 + 2]
            A_shared_1[threadIdx_x * 2 + 512:threadIdx_x * 2 + 512 + 2] = A_1[cse_var_2 + (threadIdx_x * 2 + 512) // 48 * 1536 + blockIdx_x // 6 * 48 + (threadIdx_x * 2 + 32) % 48:cse_var_2 + (threadIdx_x * 2 + 512) // 48 * 1536 + blockIdx_x // 6 * 48 + (threadIdx_x * 2 + 32) % 48 + 2]
            B_shared_1[threadIdx_x * 4:threadIdx_x * 4 + 4] = B_1[cse_var_2 + threadIdx_x // 64 * 1536 + blockIdx_x % 6 * 256 + threadIdx_x % 64 * 4:cse_var_2 + threadIdx_x // 64 * 1536 + blockIdx_x % 6 * 256 + threadIdx_x % 64 * 4 + 4]
            B_shared_1[threadIdx_x * 4 + 512:threadIdx_x * 4 + 512 + 4] = B_1[cse_var_2 + threadIdx_x // 64 * 1536 + blockIdx_x % 6 * 256 + threadIdx_x % 64 * 4 + 3072:cse_var_2 + threadIdx_x // 64 * 1536 + blockIdx_x % 6 * 256 + threadIdx_x % 64 * 4 + 3072 + 4]
            B_shared_1[threadIdx_x * 4 + 1024:threadIdx_x * 4 + 1024 + 4] = B_1[cse_var_2 + threadIdx_x // 64 * 1536 + blockIdx_x % 6 * 256 + threadIdx_x % 64 * 4 + 6144:cse_var_2 + threadIdx_x // 64 * 1536 + blockIdx_x % 6 * 256 + threadIdx_x % 64 * 4 + 6144 + 4]
            B_shared_1[threadIdx_x * 4 + 1536:threadIdx_x * 4 + 1536 + 4] = B_1[cse_var_2 + threadIdx_x // 64 * 1536 + blockIdx_x % 6 * 256 + threadIdx_x % 64 * 4 + 9216:cse_var_2 + threadIdx_x // 64 * 1536 + blockIdx_x % 6 * 256 + threadIdx_x % 64 * 4 + 9216 + 4]
            B_shared_1[threadIdx_x * 4 + 2048:threadIdx_x * 4 + 2048 + 4] = B_1[cse_var_2 + threadIdx_x // 64 * 1536 + blockIdx_x % 6 * 256 + threadIdx_x % 64 * 4 + 12288:cse_var_2 + threadIdx_x // 64 * 1536 + blockIdx_x % 6 * 256 + threadIdx_x % 64 * 4 + 12288 + 4]
            B_shared_1[threadIdx_x * 4 + 2560:threadIdx_x * 4 + 2560 + 4] = B_1[cse_var_2 + threadIdx_x // 64 * 1536 + blockIdx_x % 6 * 256 + threadIdx_x % 64 * 4 + 15360:cse_var_2 + threadIdx_x // 64 * 1536 + blockIdx_x % 6 * 256 + threadIdx_x % 64 * 4 + 15360 + 4]
            B_shared_1[threadIdx_x * 4 + 3072:threadIdx_x * 4 + 3072 + 4] = B_1[cse_var_2 + threadIdx_x // 64 * 1536 + blockIdx_x % 6 * 256 + threadIdx_x % 64 * 4 + 18432:cse_var_2 + threadIdx_x // 64 * 1536 + blockIdx_x % 6 * 256 + threadIdx_x % 64 * 4 + 18432 + 4]
            B_shared_1[threadIdx_x * 4 + 3584:threadIdx_x * 4 + 3584 + 4] = B_1[cse_var_2 + threadIdx_x // 64 * 1536 + blockIdx_x % 6 * 256 + threadIdx_x % 64 * 4 + 21504:cse_var_2 + threadIdx_x // 64 * 1536 + blockIdx_x % 6 * 256 + threadIdx_x % 64 * 4 + 21504 + 4]
            for k_1, i_3 in T.grid(16, 12):
                cse_var_10: T.int32 = i_3 * 4
                cse_var_9: T.int32 = cse_var_10 + 51
                cse_var_8: T.int32 = cse_var_10 + 50
                cse_var_7: T.int32 = cse_var_10 + 49
                cse_var_6: T.int32 = cse_var_10 + 48
                cse_var_5: T.int32 = cse_var_10 + 3
                cse_var_4: T.int32 = cse_var_10 + 2
                cse_var_3: T.int32 = cse_var_10 + 1
                Y_local_1[cse_var_10] = Y_local_1[cse_var_10] + A_shared_1[k_1 * 48 + threadIdx_x // 32 * 12 + i_3] * B_shared_1[k_1 * 256 + threadIdx_x % 32 * 4]
                Y_local_1[cse_var_6] = Y_local_1[cse_var_6] + A_shared_1[k_1 * 48 + threadIdx_x // 32 * 12 + i_3] * B_shared_1[k_1 * 256 + threadIdx_x % 32 * 4 + 128]
                Y_local_1[cse_var_3] = Y_local_1[cse_var_3] + A_shared_1[k_1 * 48 + threadIdx_x // 32 * 12 + i_3] * B_shared_1[k_1 * 256 + threadIdx_x % 32 * 4 + 1]
                Y_local_1[cse_var_7] = Y_local_1[cse_var_7] + A_shared_1[k_1 * 48 + threadIdx_x // 32 * 12 + i_3] * B_shared_1[k_1 * 256 + threadIdx_x % 32 * 4 + 129]
                Y_local_1[cse_var_4] = Y_local_1[cse_var_4] + A_shared_1[k_1 * 48 + threadIdx_x // 32 * 12 + i_3] * B_shared_1[k_1 * 256 + threadIdx_x % 32 * 4 + 2]
                Y_local_1[cse_var_8] = Y_local_1[cse_var_8] + A_shared_1[k_1 * 48 + threadIdx_x // 32 * 12 + i_3] * B_shared_1[k_1 * 256 + threadIdx_x % 32 * 4 + 130]
                Y_local_1[cse_var_5] = Y_local_1[cse_var_5] + A_shared_1[k_1 * 48 + threadIdx_x // 32 * 12 + i_3] * B_shared_1[k_1 * 256 + threadIdx_x % 32 * 4 + 3]
                Y_local_1[cse_var_9] = Y_local_1[cse_var_9] + A_shared_1[k_1 * 48 + threadIdx_x // 32 * 12 + i_3] * B_shared_1[k_1 * 256 + threadIdx_x % 32 * 4 + 131]
        for ax0 in T.serial(12):
            cse_var_11: T.int32 = ax0 * 4
            Y_1[blockIdx_x // 6 * 73728 + threadIdx_x // 32 * 18432 + ax0 * 1536 + blockIdx_x % 6 * 256 + threadIdx_x % 32 * 4] = Y_local_1[cse_var_11]
            Y_1[blockIdx_x // 6 * 73728 + threadIdx_x // 32 * 18432 + ax0 * 1536 + blockIdx_x % 6 * 256 + threadIdx_x % 32 * 4 + 128] = Y_local_1[cse_var_11 + 48]
            Y_1[blockIdx_x // 6 * 73728 + threadIdx_x // 32 * 18432 + ax0 * 1536 + blockIdx_x % 6 * 256 + threadIdx_x % 32 * 4 + 1] = Y_local_1[cse_var_11 + 1]
            Y_1[blockIdx_x // 6 * 73728 + threadIdx_x // 32 * 18432 + ax0 * 1536 + blockIdx_x % 6 * 256 + threadIdx_x % 32 * 4 + 129] = Y_local_1[cse_var_11 + 49]
            Y_1[blockIdx_x // 6 * 73728 + threadIdx_x // 32 * 18432 + ax0 * 1536 + blockIdx_x % 6 * 256 + threadIdx_x % 32 * 4 + 2] = Y_local_1[cse_var_11 + 2]
            Y_1[blockIdx_x // 6 * 73728 + threadIdx_x // 32 * 18432 + ax0 * 1536 + blockIdx_x % 6 * 256 + threadIdx_x % 32 * 4 + 130] = Y_local_1[cse_var_11 + 50]
            Y_1[blockIdx_x // 6 * 73728 + threadIdx_x // 32 * 18432 + ax0 * 1536 + blockIdx_x % 6 * 256 + threadIdx_x % 32 * 4 + 3] = Y_local_1[cse_var_11 + 3]
            Y_1[blockIdx_x // 6 * 73728 + threadIdx_x // 32 * 18432 + ax0 * 1536 + blockIdx_x % 6 * 256 + threadIdx_x % 32 * 4 + 131] = Y_local_1[cse_var_11 + 51]
    

