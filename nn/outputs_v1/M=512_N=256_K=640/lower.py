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
        A_shared_dyn = T.allocate([1280], "float32", "shared.dyn")
        A_shared_dyn_1 = T.buffer_decl([1280], dtype="float32", data=A_shared_dyn, scope="shared.dyn")
        B_shared_dyn = T.allocate([2560], "float32", "shared.dyn")
        B_shared_dyn_1 = T.buffer_decl([2560], dtype="float32", data=B_shared_dyn, scope="shared.dyn")
        A_shared_dyn_local = T.allocate([2], "float32x4", "local")
        A_shared_dyn_local_1 = T.buffer_decl([2], dtype="float32x4", data=A_shared_dyn_local, scope="local")
        B_shared_dyn_local = T.allocate([8], "float32", "local")
        B_shared_dyn_local_1 = T.buffer_decl([8], dtype="float32", data=B_shared_dyn_local, scope="local")
        T.launch_thread(threadIdx_x, 128)
        Y_local_1[0] = T.float32(0)
        Y_local_1[4] = T.float32(0)
        Y_local_1[8] = T.float32(0)
        Y_local_1[12] = T.float32(0)
        Y_local_1[1] = T.float32(0)
        Y_local_1[5] = T.float32(0)
        Y_local_1[9] = T.float32(0)
        Y_local_1[13] = T.float32(0)
        Y_local_1[2] = T.float32(0)
        Y_local_1[6] = T.float32(0)
        Y_local_1[10] = T.float32(0)
        Y_local_1[14] = T.float32(0)
        Y_local_1[3] = T.float32(0)
        Y_local_1[7] = T.float32(0)
        Y_local_1[11] = T.float32(0)
        Y_local_1[15] = T.float32(0)
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x % 4 * 64 + threadIdx_x % 32 // 16 * 16 + threadIdx_x // 32 * 4 + threadIdx_x % 16 // 4] = A_1[blockIdx_x // 4 * 20480 + threadIdx_x // 4 * 640 + threadIdx_x % 4 * 2]
                A_shared_dyn_1[threadIdx_x % 4 * 64 + threadIdx_x % 32 // 16 * 16 + threadIdx_x // 32 * 4 + threadIdx_x % 16 // 4 + 32] = A_1[blockIdx_x // 4 * 20480 + threadIdx_x // 4 * 640 + threadIdx_x % 4 * 2 + 1]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 4] = B_1[threadIdx_x // 16 * 256 + blockIdx_x % 4 * 64 + threadIdx_x % 16 * 4:threadIdx_x // 16 * 256 + blockIdx_x % 4 * 64 + threadIdx_x % 16 * 4 + 4]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x % 4 * 64 + threadIdx_x % 32 // 16 * 16 + threadIdx_x // 32 * 4 + threadIdx_x % 16 // 4 + 256] = A_1[blockIdx_x // 4 * 20480 + threadIdx_x // 4 * 640 + threadIdx_x % 4 * 2 + 8]
                A_shared_dyn_1[threadIdx_x % 4 * 64 + threadIdx_x % 32 // 16 * 16 + threadIdx_x // 32 * 4 + threadIdx_x % 16 // 4 + 288] = A_1[blockIdx_x // 4 * 20480 + threadIdx_x // 4 * 640 + threadIdx_x % 4 * 2 + 9]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 512:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 512 + 4] = B_1[threadIdx_x // 16 * 256 + blockIdx_x % 4 * 64 + threadIdx_x % 16 * 4 + 2048:threadIdx_x // 16 * 256 + blockIdx_x % 4 * 64 + threadIdx_x % 16 * 4 + 2048 + 4]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x % 4 * 64 + threadIdx_x % 32 // 16 * 16 + threadIdx_x // 32 * 4 + threadIdx_x % 16 // 4 + 512] = A_1[blockIdx_x // 4 * 20480 + threadIdx_x // 4 * 640 + threadIdx_x % 4 * 2 + 16]
                A_shared_dyn_1[threadIdx_x % 4 * 64 + threadIdx_x % 32 // 16 * 16 + threadIdx_x // 32 * 4 + threadIdx_x % 16 // 4 + 544] = A_1[blockIdx_x // 4 * 20480 + threadIdx_x // 4 * 640 + threadIdx_x % 4 * 2 + 17]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 1024:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 1024 + 4] = B_1[threadIdx_x // 16 * 256 + blockIdx_x % 4 * 64 + threadIdx_x % 16 * 4 + 4096:threadIdx_x // 16 * 256 + blockIdx_x % 4 * 64 + threadIdx_x % 16 * 4 + 4096 + 4]
        with T.attr(0, "async_commit_queue_scope", 0):
            with T.attr(0, "async_scope", 1):
                A_shared_dyn_1[threadIdx_x % 4 * 64 + threadIdx_x % 32 // 16 * 16 + threadIdx_x // 32 * 4 + threadIdx_x % 16 // 4 + 768] = A_1[blockIdx_x // 4 * 20480 + threadIdx_x // 4 * 640 + threadIdx_x % 4 * 2 + 24]
                A_shared_dyn_1[threadIdx_x % 4 * 64 + threadIdx_x % 32 // 16 * 16 + threadIdx_x // 32 * 4 + threadIdx_x % 16 // 4 + 800] = A_1[blockIdx_x // 4 * 20480 + threadIdx_x // 4 * 640 + threadIdx_x % 4 * 2 + 25]
            T.attr(0, "async_scope", 1)
            B_shared_dyn_1[threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 1536:threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 1536 + 4] = B_1[threadIdx_x // 16 * 256 + blockIdx_x % 4 * 64 + threadIdx_x % 16 * 4 + 6144:threadIdx_x // 16 * 256 + blockIdx_x % 4 * 64 + threadIdx_x % 16 * 4 + 6144 + 4]
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 3)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 4]
        for k_0 in T.serial(76):
            cse_var_3: T.int32 = k_0 % 5
            cse_var_2: T.int32 = (k_0 + 4) % 5
            cse_var_1: T.int32 = (k_0 + 1) % 5
            with T.attr(0, "async_commit_queue_scope", 0):
                with T.attr(0, "async_scope", 1):
                    A_shared_dyn_1[cse_var_2 * 256 + threadIdx_x % 4 * 64 + threadIdx_x % 32 // 16 * 16 + threadIdx_x // 32 * 4 + threadIdx_x % 16 // 4] = A_1[blockIdx_x // 4 * 20480 + threadIdx_x // 4 * 640 + k_0 * 8 + threadIdx_x % 4 * 2 + 32]
                    A_shared_dyn_1[cse_var_2 * 256 + threadIdx_x % 4 * 64 + threadIdx_x % 32 // 16 * 16 + threadIdx_x // 32 * 4 + threadIdx_x % 16 // 4 + 32] = A_1[blockIdx_x // 4 * 20480 + threadIdx_x // 4 * 640 + k_0 * 8 + threadIdx_x % 4 * 2 + 33]
                T.attr(0, "async_scope", 1)
                B_shared_dyn_1[cse_var_2 * 512 + threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4:cse_var_2 * 512 + threadIdx_x // 16 * 64 + threadIdx_x % 2 * 32 + threadIdx_x % 16 // 2 * 4 + 4] = B_1[k_0 * 2048 + threadIdx_x // 16 * 256 + blockIdx_x % 4 * 64 + threadIdx_x % 16 * 4 + 8192:k_0 * 2048 + threadIdx_x // 16 * 256 + blockIdx_x % 4 * 64 + threadIdx_x % 16 * 4 + 8192 + 4]
            with T.attr(0, "async_wait_queue_scope", 0):
                T.attr(0, "async_wait_inflight_count", 3)
                A_shared_dyn_local_1[1] = A_shared_dyn_1[cse_var_3 * 256 + threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 32:cse_var_3 * 256 + threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 32 + 4]
                B_shared_dyn_local_1[4:8] = B_shared_dyn_1[cse_var_3 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 64:cse_var_3 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 64 + 4]
                Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                A_shared_dyn_local_1[0] = A_shared_dyn_1[cse_var_3 * 256 + threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 64:cse_var_3 * 256 + threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 64 + 4]
                B_shared_dyn_local_1[0:4] = B_shared_dyn_1[cse_var_3 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 128:cse_var_3 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 128 + 4]
                Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
                A_shared_dyn_local_1[1] = A_shared_dyn_1[cse_var_3 * 256 + threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 96:cse_var_3 * 256 + threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 96 + 4]
                B_shared_dyn_local_1[4:8] = B_shared_dyn_1[cse_var_3 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 192:cse_var_3 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 192 + 4]
                Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                A_shared_dyn_local_1[0] = A_shared_dyn_1[cse_var_3 * 256 + threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 128:cse_var_3 * 256 + threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 128 + 4]
                B_shared_dyn_local_1[0:4] = B_shared_dyn_1[cse_var_3 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 256:cse_var_3 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 256 + 4]
                Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
                A_shared_dyn_local_1[1] = A_shared_dyn_1[cse_var_3 * 256 + threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 160:cse_var_3 * 256 + threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 160 + 4]
                B_shared_dyn_local_1[4:8] = B_shared_dyn_1[cse_var_3 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 320:cse_var_3 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 320 + 4]
                Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
                A_shared_dyn_local_1[0] = A_shared_dyn_1[cse_var_3 * 256 + threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 192:cse_var_3 * 256 + threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 192 + 4]
                B_shared_dyn_local_1[0:4] = B_shared_dyn_1[cse_var_3 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 384:cse_var_3 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 384 + 4]
                Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
                Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
                Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
                Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
                A_shared_dyn_local_1[1] = A_shared_dyn_1[cse_var_3 * 256 + threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 224:cse_var_3 * 256 + threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 224 + 4]
                B_shared_dyn_local_1[4:8] = B_shared_dyn_1[cse_var_3 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 448:cse_var_3 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 448 + 4]
                Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
                Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
                Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
                Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[cse_var_1 * 256 + threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4:cse_var_1 * 256 + threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[cse_var_1 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4:cse_var_1 * 512 + threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 2)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 288:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 288 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 576:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 576 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 320:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 320 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 640:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 640 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 352:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 352 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 704:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 704 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 384:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 384 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 768:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 768 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 416:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 416 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 832:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 832 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 448:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 448 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 896:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 896 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 480:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 480 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 960:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 960 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 512:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 512 + 4]
        B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1024:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1024 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 1)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 544:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 544 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1088:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1088 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 576:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 576 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1152:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1152 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 608:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 608 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1216:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1216 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 640:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 640 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1280:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1280 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 672:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 672 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1344:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1344 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 704:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 704 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1408:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1408 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 736:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 736 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1472:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1472 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 768:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 768 + 4]
        B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1536:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1536 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
        with T.attr(0, "async_wait_queue_scope", 0):
            T.attr(0, "async_wait_inflight_count", 0)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 800:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 800 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1600:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1600 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 832:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 832 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1664:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1664 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 864:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 864 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1728:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1728 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 896:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 896 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1792:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1792 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 928:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 928 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1856:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1856 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
            A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 960:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 960 + 4]
            B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1920:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1920 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
            A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 992:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 992 + 4]
            B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1984:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 1984 + 4]
            Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
            Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
            Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
            Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1024:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1024 + 4]
        B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 2048:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 2048 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
        A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1056:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1056 + 4]
        B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 2112:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 2112 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1088:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1088 + 4]
        B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 2176:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 2176 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
        A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1120:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1120 + 4]
        B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 2240:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 2240 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1152:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1152 + 4]
        B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 2304:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 2304 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
        A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1184:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1184 + 4]
        B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 2368:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 2368 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        A_shared_dyn_local_1[0] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1216:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1216 + 4]
        B_shared_dyn_local_1[0:4] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 2432:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 2432 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
        A_shared_dyn_local_1[1] = A_shared_dyn_1[threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1248:threadIdx_x % 2 * 16 + threadIdx_x % 16 // 4 * 4 + 1248 + 4]
        B_shared_dyn_local_1[4:8] = B_shared_dyn_1[threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 2496:threadIdx_x % 4 // 2 * 32 + threadIdx_x // 16 * 4 + 2496 + 4]
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[0], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[1], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[2], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[0] * T.broadcast(B_shared_dyn_local_1[3], 4)
        Y_local_1[0:16:4] = Y_local_1[0:16:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[4], 4)
        Y_local_1[1:17:4] = Y_local_1[1:17:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[5], 4)
        Y_local_1[2:18:4] = Y_local_1[2:18:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[6], 4)
        Y_local_1[3:19:4] = Y_local_1[3:19:4] + A_shared_dyn_local_1[1] * T.broadcast(B_shared_dyn_local_1[7], 4)
        Y_1[blockIdx_x // 4 * 8192 + threadIdx_x % 16 // 4 * 2048 + threadIdx_x % 2 * 1024 + blockIdx_x % 4 * 64 + threadIdx_x // 16 * 8 + threadIdx_x % 4 // 2 * 4:blockIdx_x // 4 * 8192 + threadIdx_x % 16 // 4 * 2048 + threadIdx_x % 2 * 1024 + blockIdx_x % 4 * 64 + threadIdx_x // 16 * 8 + threadIdx_x % 4 // 2 * 4 + 4] = Y_local_1[0:4]
        Y_1[blockIdx_x // 4 * 8192 + threadIdx_x % 16 // 4 * 2048 + threadIdx_x % 2 * 1024 + blockIdx_x % 4 * 64 + threadIdx_x // 16 * 8 + threadIdx_x % 4 // 2 * 4 + 256:blockIdx_x // 4 * 8192 + threadIdx_x % 16 // 4 * 2048 + threadIdx_x % 2 * 1024 + blockIdx_x % 4 * 64 + threadIdx_x // 16 * 8 + threadIdx_x % 4 // 2 * 4 + 256 + 4] = Y_local_1[4:8]
        Y_1[blockIdx_x // 4 * 8192 + threadIdx_x % 16 // 4 * 2048 + threadIdx_x % 2 * 1024 + blockIdx_x % 4 * 64 + threadIdx_x // 16 * 8 + threadIdx_x % 4 // 2 * 4 + 512:blockIdx_x // 4 * 8192 + threadIdx_x % 16 // 4 * 2048 + threadIdx_x % 2 * 1024 + blockIdx_x % 4 * 64 + threadIdx_x // 16 * 8 + threadIdx_x % 4 // 2 * 4 + 512 + 4] = Y_local_1[8:12]
        Y_1[blockIdx_x // 4 * 8192 + threadIdx_x % 16 // 4 * 2048 + threadIdx_x % 2 * 1024 + blockIdx_x % 4 * 64 + threadIdx_x // 16 * 8 + threadIdx_x % 4 // 2 * 4 + 768:blockIdx_x // 4 * 8192 + threadIdx_x % 16 // 4 * 2048 + threadIdx_x % 2 * 1024 + blockIdx_x % 4 * 64 + threadIdx_x // 16 * 8 + threadIdx_x % 4 // 2 * 4 + 768 + 4] = Y_local_1[12:16]
    

