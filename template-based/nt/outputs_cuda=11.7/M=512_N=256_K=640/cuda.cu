
#ifdef _WIN32
  using uint = unsigned int;
  using uchar = unsigned char;
  using ushort = unsigned short;
  using int64_t = long long;
  using uint64_t = unsigned long long;
#else
  #define uint unsigned int
  #define uchar unsigned char
  #define ushort unsigned short
  #define int64_t long long
  #define uint64_t unsigned long long
#endif
extern "C" __global__ void __launch_bounds__(64) main_kernel0(float* __restrict__ A, float* __restrict__ B, float* __restrict__ Y) {
  extern __shared__ uchar buf_dyn_shmem[];
  float Y_local[16];
  float A_shared_dyn_local[4];
  float B_shared_dyn_local[16];
  Y_local[0] = 0.000000e+00f;
  Y_local[8] = 0.000000e+00f;
  Y_local[1] = 0.000000e+00f;
  Y_local[9] = 0.000000e+00f;
  Y_local[2] = 0.000000e+00f;
  Y_local[10] = 0.000000e+00f;
  Y_local[3] = 0.000000e+00f;
  Y_local[11] = 0.000000e+00f;
  Y_local[4] = 0.000000e+00f;
  Y_local[12] = 0.000000e+00f;
  Y_local[5] = 0.000000e+00f;
  Y_local[13] = 0.000000e+00f;
  Y_local[6] = 0.000000e+00f;
  Y_local[14] = 0.000000e+00f;
  Y_local[7] = 0.000000e+00f;
  Y_local[15] = 0.000000e+00f;

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + ((((((int)threadIdx.x) >> 3) * 128) + ((((int)threadIdx.x) & 1) * 64)) + (((((int)threadIdx.x) & 7) >> 1) * 16))))
    );
    __asm__ __volatile__(
      "cp.async.cg.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(A + ((((((int)threadIdx.x) >> 3) * 512) + ((((int)blockIdx.x) >> 3) * 32)) + ((((int)threadIdx.x) & 7) * 4)))), "n"(16)
    );
  }
  for (int ax0_ax1_fused_2 = 0; ax0_ax1_fused_2 < 4; ++ax0_ax1_fused_2) {

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + ((((((((int)threadIdx.x) >> 3) * 192) + ((((int)threadIdx.x) & 1) * 128)) + (((((int)threadIdx.x) & 7) >> 1) * 16)) + (ax0_ax1_fused_2 * 4)) + 4096)))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(B + (((((((int)threadIdx.x) >> 3) * 256) + ((((int)blockIdx.x) & 7) * 32)) + ((((int)threadIdx.x) & 7) * 4)) + ax0_ax1_fused_2))), "n"(4)
    );
  }
  }
__asm__ __volatile__("cp.async.commit_group;");


  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + (((((((int)threadIdx.x) >> 3) * 128) + ((((int)threadIdx.x) & 1) * 64)) + (((((int)threadIdx.x) & 7) >> 1) * 16)) + 1024)))
    );
    __asm__ __volatile__(
      "cp.async.cg.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(A + (((((((int)threadIdx.x) >> 3) * 512) + ((((int)blockIdx.x) >> 3) * 32)) + ((((int)threadIdx.x) & 7) * 4)) + 4096))), "n"(16)
    );
  }
  for (int ax0_ax1_fused_2_1 = 0; ax0_ax1_fused_2_1 < 4; ++ax0_ax1_fused_2_1) {

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + ((((((((int)threadIdx.x) >> 3) * 192) + ((((int)threadIdx.x) & 1) * 128)) + (((((int)threadIdx.x) & 7) >> 1) * 16)) + (ax0_ax1_fused_2_1 * 4)) + 5632)))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(B + ((((((((int)threadIdx.x) >> 3) * 256) + ((((int)blockIdx.x) & 7) * 32)) + ((((int)threadIdx.x) & 7) * 4)) + ax0_ax1_fused_2_1) + 2048))), "n"(4)
    );
  }
  }
__asm__ __volatile__("cp.async.commit_group;");


  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + (((((((int)threadIdx.x) >> 3) * 128) + ((((int)threadIdx.x) & 1) * 64)) + (((((int)threadIdx.x) & 7) >> 1) * 16)) + 2048)))
    );
    __asm__ __volatile__(
      "cp.async.cg.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(A + (((((((int)threadIdx.x) >> 3) * 512) + ((((int)blockIdx.x) >> 3) * 32)) + ((((int)threadIdx.x) & 7) * 4)) + 8192))), "n"(16)
    );
  }
  for (int ax0_ax1_fused_2_2 = 0; ax0_ax1_fused_2_2 < 4; ++ax0_ax1_fused_2_2) {

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + ((((((((int)threadIdx.x) >> 3) * 192) + ((((int)threadIdx.x) & 1) * 128)) + (((((int)threadIdx.x) & 7) >> 1) * 16)) + (ax0_ax1_fused_2_2 * 4)) + 7168)))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(B + ((((((((int)threadIdx.x) >> 3) * 256) + ((((int)blockIdx.x) & 7) * 32)) + ((((int)threadIdx.x) & 7) * 4)) + ax0_ax1_fused_2_2) + 4096))), "n"(4)
    );
  }
  }
__asm__ __volatile__("cp.async.commit_group;");

__asm__ __volatile__("cp.async.wait_group 2;");

  __syncthreads();
  for (int ax1_1_s = 0; ax1_1_s < 4; ++ax1_1_s) {
    if (ax1_1_s < 2) {
      A_shared_dyn_local[ax1_1_s] = ((float*)buf_dyn_shmem)[((((((((int)threadIdx.x) & 7) >> 2) * 16) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s)];
    }
  }
  for (int ax1_0 = 0; ax1_0 < 2; ++ax1_0) {
    *(float4*)(B_shared_dyn_local + (ax1_0 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0 * 4)) >> 6) * 64) + (ax1_0 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 1024) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
  }
  for (int k_0 = 0; k_0 < 77; ++k_0) {
    __syncthreads();

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + ((((((k_0 + 3) & 3) * 1024) + ((((int)threadIdx.x) >> 3) * 128)) + ((((int)threadIdx.x) & 1) * 64)) + (((((int)threadIdx.x) & 7) >> 1) * 16))))
    );
    __asm__ __volatile__(
      "cp.async.cg.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(A + (((((k_0 * 4096) + ((((int)threadIdx.x) >> 3) * 512)) + ((((int)blockIdx.x) >> 3) * 32)) + ((((int)threadIdx.x) & 7) * 4)) + 12288))), "n"(16)
    );
  }
    for (int ax0_ax1_fused_2_3 = 0; ax0_ax1_fused_2_3 < 4; ++ax0_ax1_fused_2_3) {

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + ((((((((k_0 + 3) & 3) * 1536) + ((((int)threadIdx.x) >> 3) * 192)) + ((((int)threadIdx.x) & 1) * 128)) + (((((int)threadIdx.x) & 7) >> 1) * 16)) + (ax0_ax1_fused_2_3 * 4)) + 4096)))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(B + ((((((k_0 * 2048) + ((((int)threadIdx.x) >> 3) * 256)) + ((((int)blockIdx.x) & 7) * 32)) + ((((int)threadIdx.x) & 7) * 4)) + ax0_ax1_fused_2_3) + 6144))), "n"(4)
    );
  }
    }
__asm__ __volatile__("cp.async.commit_group;");

__asm__ __volatile__("cp.async.wait_group 2;");

    __syncthreads();
    for (int ax1_1_s_1 = 0; ax1_1_s_1 < 4; ++ax1_1_s_1) {
      if (ax1_1_s_1 < 2) {
        A_shared_dyn_local[(ax1_1_s_1 + 2)] = ((float*)buf_dyn_shmem)[(((((((k_0 & 3) * 256) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_1) + 32)];
      }
    }
    for (int ax1_0_1 = 0; ax1_0_1 < 2; ++ax1_0_1) {
      *(float4*)(B_shared_dyn_local + ((ax1_0_1 * 4) + 8)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((k_0 & 3) * 384) + (((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_1 * 4)) >> 6) * 64)) + (ax1_0_1 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 1072) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
    }
    for (int i_2_1_s = 0; i_2_1_s < 4; ++i_2_1_s) {
      if (i_2_1_s < 2) {
        Y_local[(i_2_1_s * 8)] = (Y_local[(i_2_1_s * 8)] + (A_shared_dyn_local[i_2_1_s] * B_shared_dyn_local[0]));
      }
    }
    for (int i_2_1_s_1 = 0; i_2_1_s_1 < 4; ++i_2_1_s_1) {
      if (i_2_1_s_1 < 2) {
        Y_local[((i_2_1_s_1 * 8) + 1)] = (Y_local[((i_2_1_s_1 * 8) + 1)] + (A_shared_dyn_local[i_2_1_s_1] * B_shared_dyn_local[1]));
      }
    }
    for (int i_2_1_s_2 = 0; i_2_1_s_2 < 4; ++i_2_1_s_2) {
      if (i_2_1_s_2 < 2) {
        Y_local[((i_2_1_s_2 * 8) + 2)] = (Y_local[((i_2_1_s_2 * 8) + 2)] + (A_shared_dyn_local[i_2_1_s_2] * B_shared_dyn_local[2]));
      }
    }
    for (int i_2_1_s_3 = 0; i_2_1_s_3 < 4; ++i_2_1_s_3) {
      if (i_2_1_s_3 < 2) {
        Y_local[((i_2_1_s_3 * 8) + 3)] = (Y_local[((i_2_1_s_3 * 8) + 3)] + (A_shared_dyn_local[i_2_1_s_3] * B_shared_dyn_local[3]));
      }
    }
    for (int i_2_1_s_4 = 0; i_2_1_s_4 < 4; ++i_2_1_s_4) {
      if (i_2_1_s_4 < 2) {
        Y_local[((i_2_1_s_4 * 8) + 4)] = (Y_local[((i_2_1_s_4 * 8) + 4)] + (A_shared_dyn_local[i_2_1_s_4] * B_shared_dyn_local[4]));
      }
    }
    for (int i_2_1_s_5 = 0; i_2_1_s_5 < 4; ++i_2_1_s_5) {
      if (i_2_1_s_5 < 2) {
        Y_local[((i_2_1_s_5 * 8) + 5)] = (Y_local[((i_2_1_s_5 * 8) + 5)] + (A_shared_dyn_local[i_2_1_s_5] * B_shared_dyn_local[5]));
      }
    }
    for (int i_2_1_s_6 = 0; i_2_1_s_6 < 4; ++i_2_1_s_6) {
      if (i_2_1_s_6 < 2) {
        Y_local[((i_2_1_s_6 * 8) + 6)] = (Y_local[((i_2_1_s_6 * 8) + 6)] + (A_shared_dyn_local[i_2_1_s_6] * B_shared_dyn_local[6]));
      }
    }
    for (int i_2_1_s_7 = 0; i_2_1_s_7 < 4; ++i_2_1_s_7) {
      if (i_2_1_s_7 < 2) {
        Y_local[((i_2_1_s_7 * 8) + 7)] = (Y_local[((i_2_1_s_7 * 8) + 7)] + (A_shared_dyn_local[i_2_1_s_7] * B_shared_dyn_local[7]));
      }
    }
    for (int ax1_1_s_2 = 0; ax1_1_s_2 < 4; ++ax1_1_s_2) {
      if (ax1_1_s_2 < 2) {
        A_shared_dyn_local[ax1_1_s_2] = ((float*)buf_dyn_shmem)[(((((((k_0 & 3) * 256) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_2) + 64)];
      }
    }
    for (int ax1_0_2 = 0; ax1_0_2 < 2; ++ax1_0_2) {
      *(float4*)(B_shared_dyn_local + (ax1_0_2 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((k_0 & 3) * 384) + (((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_2 * 4)) >> 6) * 64)) + (ax1_0_2 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 1120) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
    }
    for (int i_2_1_s_8 = 0; i_2_1_s_8 < 4; ++i_2_1_s_8) {
      if (i_2_1_s_8 < 2) {
        Y_local[(i_2_1_s_8 * 8)] = (Y_local[(i_2_1_s_8 * 8)] + (A_shared_dyn_local[(i_2_1_s_8 + 2)] * B_shared_dyn_local[8]));
      }
    }
    for (int i_2_1_s_9 = 0; i_2_1_s_9 < 4; ++i_2_1_s_9) {
      if (i_2_1_s_9 < 2) {
        Y_local[((i_2_1_s_9 * 8) + 1)] = (Y_local[((i_2_1_s_9 * 8) + 1)] + (A_shared_dyn_local[(i_2_1_s_9 + 2)] * B_shared_dyn_local[9]));
      }
    }
    for (int i_2_1_s_10 = 0; i_2_1_s_10 < 4; ++i_2_1_s_10) {
      if (i_2_1_s_10 < 2) {
        Y_local[((i_2_1_s_10 * 8) + 2)] = (Y_local[((i_2_1_s_10 * 8) + 2)] + (A_shared_dyn_local[(i_2_1_s_10 + 2)] * B_shared_dyn_local[10]));
      }
    }
    for (int i_2_1_s_11 = 0; i_2_1_s_11 < 4; ++i_2_1_s_11) {
      if (i_2_1_s_11 < 2) {
        Y_local[((i_2_1_s_11 * 8) + 3)] = (Y_local[((i_2_1_s_11 * 8) + 3)] + (A_shared_dyn_local[(i_2_1_s_11 + 2)] * B_shared_dyn_local[11]));
      }
    }
    for (int i_2_1_s_12 = 0; i_2_1_s_12 < 4; ++i_2_1_s_12) {
      if (i_2_1_s_12 < 2) {
        Y_local[((i_2_1_s_12 * 8) + 4)] = (Y_local[((i_2_1_s_12 * 8) + 4)] + (A_shared_dyn_local[(i_2_1_s_12 + 2)] * B_shared_dyn_local[12]));
      }
    }
    for (int i_2_1_s_13 = 0; i_2_1_s_13 < 4; ++i_2_1_s_13) {
      if (i_2_1_s_13 < 2) {
        Y_local[((i_2_1_s_13 * 8) + 5)] = (Y_local[((i_2_1_s_13 * 8) + 5)] + (A_shared_dyn_local[(i_2_1_s_13 + 2)] * B_shared_dyn_local[13]));
      }
    }
    for (int i_2_1_s_14 = 0; i_2_1_s_14 < 4; ++i_2_1_s_14) {
      if (i_2_1_s_14 < 2) {
        Y_local[((i_2_1_s_14 * 8) + 6)] = (Y_local[((i_2_1_s_14 * 8) + 6)] + (A_shared_dyn_local[(i_2_1_s_14 + 2)] * B_shared_dyn_local[14]));
      }
    }
    for (int i_2_1_s_15 = 0; i_2_1_s_15 < 4; ++i_2_1_s_15) {
      if (i_2_1_s_15 < 2) {
        Y_local[((i_2_1_s_15 * 8) + 7)] = (Y_local[((i_2_1_s_15 * 8) + 7)] + (A_shared_dyn_local[(i_2_1_s_15 + 2)] * B_shared_dyn_local[15]));
      }
    }
    for (int ax1_1_s_3 = 0; ax1_1_s_3 < 4; ++ax1_1_s_3) {
      if (ax1_1_s_3 < 2) {
        A_shared_dyn_local[(ax1_1_s_3 + 2)] = ((float*)buf_dyn_shmem)[(((((((k_0 & 3) * 256) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_3) + 96)];
      }
    }
    for (int ax1_0_3 = 0; ax1_0_3 < 2; ++ax1_0_3) {
      *(float4*)(B_shared_dyn_local + ((ax1_0_3 * 4) + 8)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((k_0 & 3) * 384) + (((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_3 * 4)) >> 6) * 64)) + (ax1_0_3 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 1168) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
    }
    for (int i_2_1_s_16 = 0; i_2_1_s_16 < 4; ++i_2_1_s_16) {
      if (i_2_1_s_16 < 2) {
        Y_local[(i_2_1_s_16 * 8)] = (Y_local[(i_2_1_s_16 * 8)] + (A_shared_dyn_local[i_2_1_s_16] * B_shared_dyn_local[0]));
      }
    }
    for (int i_2_1_s_17 = 0; i_2_1_s_17 < 4; ++i_2_1_s_17) {
      if (i_2_1_s_17 < 2) {
        Y_local[((i_2_1_s_17 * 8) + 1)] = (Y_local[((i_2_1_s_17 * 8) + 1)] + (A_shared_dyn_local[i_2_1_s_17] * B_shared_dyn_local[1]));
      }
    }
    for (int i_2_1_s_18 = 0; i_2_1_s_18 < 4; ++i_2_1_s_18) {
      if (i_2_1_s_18 < 2) {
        Y_local[((i_2_1_s_18 * 8) + 2)] = (Y_local[((i_2_1_s_18 * 8) + 2)] + (A_shared_dyn_local[i_2_1_s_18] * B_shared_dyn_local[2]));
      }
    }
    for (int i_2_1_s_19 = 0; i_2_1_s_19 < 4; ++i_2_1_s_19) {
      if (i_2_1_s_19 < 2) {
        Y_local[((i_2_1_s_19 * 8) + 3)] = (Y_local[((i_2_1_s_19 * 8) + 3)] + (A_shared_dyn_local[i_2_1_s_19] * B_shared_dyn_local[3]));
      }
    }
    for (int i_2_1_s_20 = 0; i_2_1_s_20 < 4; ++i_2_1_s_20) {
      if (i_2_1_s_20 < 2) {
        Y_local[((i_2_1_s_20 * 8) + 4)] = (Y_local[((i_2_1_s_20 * 8) + 4)] + (A_shared_dyn_local[i_2_1_s_20] * B_shared_dyn_local[4]));
      }
    }
    for (int i_2_1_s_21 = 0; i_2_1_s_21 < 4; ++i_2_1_s_21) {
      if (i_2_1_s_21 < 2) {
        Y_local[((i_2_1_s_21 * 8) + 5)] = (Y_local[((i_2_1_s_21 * 8) + 5)] + (A_shared_dyn_local[i_2_1_s_21] * B_shared_dyn_local[5]));
      }
    }
    for (int i_2_1_s_22 = 0; i_2_1_s_22 < 4; ++i_2_1_s_22) {
      if (i_2_1_s_22 < 2) {
        Y_local[((i_2_1_s_22 * 8) + 6)] = (Y_local[((i_2_1_s_22 * 8) + 6)] + (A_shared_dyn_local[i_2_1_s_22] * B_shared_dyn_local[6]));
      }
    }
    for (int i_2_1_s_23 = 0; i_2_1_s_23 < 4; ++i_2_1_s_23) {
      if (i_2_1_s_23 < 2) {
        Y_local[((i_2_1_s_23 * 8) + 7)] = (Y_local[((i_2_1_s_23 * 8) + 7)] + (A_shared_dyn_local[i_2_1_s_23] * B_shared_dyn_local[7]));
      }
    }
    for (int ax1_1_s_4 = 0; ax1_1_s_4 < 4; ++ax1_1_s_4) {
      if (ax1_1_s_4 < 2) {
        A_shared_dyn_local[ax1_1_s_4] = ((float*)buf_dyn_shmem)[(((((((k_0 & 3) * 256) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_4) + 128)];
      }
    }
    for (int ax1_0_4 = 0; ax1_0_4 < 2; ++ax1_0_4) {
      *(float4*)(B_shared_dyn_local + (ax1_0_4 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((k_0 & 3) * 384) + (((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_4 * 4)) >> 6) * 64)) + (ax1_0_4 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 1216) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
    }
    for (int i_2_1_s_24 = 0; i_2_1_s_24 < 4; ++i_2_1_s_24) {
      if (i_2_1_s_24 < 2) {
        Y_local[(i_2_1_s_24 * 8)] = (Y_local[(i_2_1_s_24 * 8)] + (A_shared_dyn_local[(i_2_1_s_24 + 2)] * B_shared_dyn_local[8]));
      }
    }
    for (int i_2_1_s_25 = 0; i_2_1_s_25 < 4; ++i_2_1_s_25) {
      if (i_2_1_s_25 < 2) {
        Y_local[((i_2_1_s_25 * 8) + 1)] = (Y_local[((i_2_1_s_25 * 8) + 1)] + (A_shared_dyn_local[(i_2_1_s_25 + 2)] * B_shared_dyn_local[9]));
      }
    }
    for (int i_2_1_s_26 = 0; i_2_1_s_26 < 4; ++i_2_1_s_26) {
      if (i_2_1_s_26 < 2) {
        Y_local[((i_2_1_s_26 * 8) + 2)] = (Y_local[((i_2_1_s_26 * 8) + 2)] + (A_shared_dyn_local[(i_2_1_s_26 + 2)] * B_shared_dyn_local[10]));
      }
    }
    for (int i_2_1_s_27 = 0; i_2_1_s_27 < 4; ++i_2_1_s_27) {
      if (i_2_1_s_27 < 2) {
        Y_local[((i_2_1_s_27 * 8) + 3)] = (Y_local[((i_2_1_s_27 * 8) + 3)] + (A_shared_dyn_local[(i_2_1_s_27 + 2)] * B_shared_dyn_local[11]));
      }
    }
    for (int i_2_1_s_28 = 0; i_2_1_s_28 < 4; ++i_2_1_s_28) {
      if (i_2_1_s_28 < 2) {
        Y_local[((i_2_1_s_28 * 8) + 4)] = (Y_local[((i_2_1_s_28 * 8) + 4)] + (A_shared_dyn_local[(i_2_1_s_28 + 2)] * B_shared_dyn_local[12]));
      }
    }
    for (int i_2_1_s_29 = 0; i_2_1_s_29 < 4; ++i_2_1_s_29) {
      if (i_2_1_s_29 < 2) {
        Y_local[((i_2_1_s_29 * 8) + 5)] = (Y_local[((i_2_1_s_29 * 8) + 5)] + (A_shared_dyn_local[(i_2_1_s_29 + 2)] * B_shared_dyn_local[13]));
      }
    }
    for (int i_2_1_s_30 = 0; i_2_1_s_30 < 4; ++i_2_1_s_30) {
      if (i_2_1_s_30 < 2) {
        Y_local[((i_2_1_s_30 * 8) + 6)] = (Y_local[((i_2_1_s_30 * 8) + 6)] + (A_shared_dyn_local[(i_2_1_s_30 + 2)] * B_shared_dyn_local[14]));
      }
    }
    for (int i_2_1_s_31 = 0; i_2_1_s_31 < 4; ++i_2_1_s_31) {
      if (i_2_1_s_31 < 2) {
        Y_local[((i_2_1_s_31 * 8) + 7)] = (Y_local[((i_2_1_s_31 * 8) + 7)] + (A_shared_dyn_local[(i_2_1_s_31 + 2)] * B_shared_dyn_local[15]));
      }
    }
    for (int ax1_1_s_5 = 0; ax1_1_s_5 < 4; ++ax1_1_s_5) {
      if (ax1_1_s_5 < 2) {
        A_shared_dyn_local[(ax1_1_s_5 + 2)] = ((float*)buf_dyn_shmem)[(((((((k_0 & 3) * 256) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_5) + 160)];
      }
    }
    for (int ax1_0_5 = 0; ax1_0_5 < 2; ++ax1_0_5) {
      *(float4*)(B_shared_dyn_local + ((ax1_0_5 * 4) + 8)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((k_0 & 3) * 384) + (((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_5 * 4)) >> 6) * 64)) + (ax1_0_5 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 1264) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
    }
    for (int i_2_1_s_32 = 0; i_2_1_s_32 < 4; ++i_2_1_s_32) {
      if (i_2_1_s_32 < 2) {
        Y_local[(i_2_1_s_32 * 8)] = (Y_local[(i_2_1_s_32 * 8)] + (A_shared_dyn_local[i_2_1_s_32] * B_shared_dyn_local[0]));
      }
    }
    for (int i_2_1_s_33 = 0; i_2_1_s_33 < 4; ++i_2_1_s_33) {
      if (i_2_1_s_33 < 2) {
        Y_local[((i_2_1_s_33 * 8) + 1)] = (Y_local[((i_2_1_s_33 * 8) + 1)] + (A_shared_dyn_local[i_2_1_s_33] * B_shared_dyn_local[1]));
      }
    }
    for (int i_2_1_s_34 = 0; i_2_1_s_34 < 4; ++i_2_1_s_34) {
      if (i_2_1_s_34 < 2) {
        Y_local[((i_2_1_s_34 * 8) + 2)] = (Y_local[((i_2_1_s_34 * 8) + 2)] + (A_shared_dyn_local[i_2_1_s_34] * B_shared_dyn_local[2]));
      }
    }
    for (int i_2_1_s_35 = 0; i_2_1_s_35 < 4; ++i_2_1_s_35) {
      if (i_2_1_s_35 < 2) {
        Y_local[((i_2_1_s_35 * 8) + 3)] = (Y_local[((i_2_1_s_35 * 8) + 3)] + (A_shared_dyn_local[i_2_1_s_35] * B_shared_dyn_local[3]));
      }
    }
    for (int i_2_1_s_36 = 0; i_2_1_s_36 < 4; ++i_2_1_s_36) {
      if (i_2_1_s_36 < 2) {
        Y_local[((i_2_1_s_36 * 8) + 4)] = (Y_local[((i_2_1_s_36 * 8) + 4)] + (A_shared_dyn_local[i_2_1_s_36] * B_shared_dyn_local[4]));
      }
    }
    for (int i_2_1_s_37 = 0; i_2_1_s_37 < 4; ++i_2_1_s_37) {
      if (i_2_1_s_37 < 2) {
        Y_local[((i_2_1_s_37 * 8) + 5)] = (Y_local[((i_2_1_s_37 * 8) + 5)] + (A_shared_dyn_local[i_2_1_s_37] * B_shared_dyn_local[5]));
      }
    }
    for (int i_2_1_s_38 = 0; i_2_1_s_38 < 4; ++i_2_1_s_38) {
      if (i_2_1_s_38 < 2) {
        Y_local[((i_2_1_s_38 * 8) + 6)] = (Y_local[((i_2_1_s_38 * 8) + 6)] + (A_shared_dyn_local[i_2_1_s_38] * B_shared_dyn_local[6]));
      }
    }
    for (int i_2_1_s_39 = 0; i_2_1_s_39 < 4; ++i_2_1_s_39) {
      if (i_2_1_s_39 < 2) {
        Y_local[((i_2_1_s_39 * 8) + 7)] = (Y_local[((i_2_1_s_39 * 8) + 7)] + (A_shared_dyn_local[i_2_1_s_39] * B_shared_dyn_local[7]));
      }
    }
    for (int ax1_1_s_6 = 0; ax1_1_s_6 < 4; ++ax1_1_s_6) {
      if (ax1_1_s_6 < 2) {
        A_shared_dyn_local[ax1_1_s_6] = ((float*)buf_dyn_shmem)[(((((((k_0 & 3) * 256) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_6) + 192)];
      }
    }
    for (int ax1_0_6 = 0; ax1_0_6 < 2; ++ax1_0_6) {
      *(float4*)(B_shared_dyn_local + (ax1_0_6 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((k_0 & 3) * 384) + (((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_6 * 4)) >> 6) * 64)) + (ax1_0_6 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 1312) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
    }
    for (int i_2_1_s_40 = 0; i_2_1_s_40 < 4; ++i_2_1_s_40) {
      if (i_2_1_s_40 < 2) {
        Y_local[(i_2_1_s_40 * 8)] = (Y_local[(i_2_1_s_40 * 8)] + (A_shared_dyn_local[(i_2_1_s_40 + 2)] * B_shared_dyn_local[8]));
      }
    }
    for (int i_2_1_s_41 = 0; i_2_1_s_41 < 4; ++i_2_1_s_41) {
      if (i_2_1_s_41 < 2) {
        Y_local[((i_2_1_s_41 * 8) + 1)] = (Y_local[((i_2_1_s_41 * 8) + 1)] + (A_shared_dyn_local[(i_2_1_s_41 + 2)] * B_shared_dyn_local[9]));
      }
    }
    for (int i_2_1_s_42 = 0; i_2_1_s_42 < 4; ++i_2_1_s_42) {
      if (i_2_1_s_42 < 2) {
        Y_local[((i_2_1_s_42 * 8) + 2)] = (Y_local[((i_2_1_s_42 * 8) + 2)] + (A_shared_dyn_local[(i_2_1_s_42 + 2)] * B_shared_dyn_local[10]));
      }
    }
    for (int i_2_1_s_43 = 0; i_2_1_s_43 < 4; ++i_2_1_s_43) {
      if (i_2_1_s_43 < 2) {
        Y_local[((i_2_1_s_43 * 8) + 3)] = (Y_local[((i_2_1_s_43 * 8) + 3)] + (A_shared_dyn_local[(i_2_1_s_43 + 2)] * B_shared_dyn_local[11]));
      }
    }
    for (int i_2_1_s_44 = 0; i_2_1_s_44 < 4; ++i_2_1_s_44) {
      if (i_2_1_s_44 < 2) {
        Y_local[((i_2_1_s_44 * 8) + 4)] = (Y_local[((i_2_1_s_44 * 8) + 4)] + (A_shared_dyn_local[(i_2_1_s_44 + 2)] * B_shared_dyn_local[12]));
      }
    }
    for (int i_2_1_s_45 = 0; i_2_1_s_45 < 4; ++i_2_1_s_45) {
      if (i_2_1_s_45 < 2) {
        Y_local[((i_2_1_s_45 * 8) + 5)] = (Y_local[((i_2_1_s_45 * 8) + 5)] + (A_shared_dyn_local[(i_2_1_s_45 + 2)] * B_shared_dyn_local[13]));
      }
    }
    for (int i_2_1_s_46 = 0; i_2_1_s_46 < 4; ++i_2_1_s_46) {
      if (i_2_1_s_46 < 2) {
        Y_local[((i_2_1_s_46 * 8) + 6)] = (Y_local[((i_2_1_s_46 * 8) + 6)] + (A_shared_dyn_local[(i_2_1_s_46 + 2)] * B_shared_dyn_local[14]));
      }
    }
    for (int i_2_1_s_47 = 0; i_2_1_s_47 < 4; ++i_2_1_s_47) {
      if (i_2_1_s_47 < 2) {
        Y_local[((i_2_1_s_47 * 8) + 7)] = (Y_local[((i_2_1_s_47 * 8) + 7)] + (A_shared_dyn_local[(i_2_1_s_47 + 2)] * B_shared_dyn_local[15]));
      }
    }
    for (int ax1_1_s_7 = 0; ax1_1_s_7 < 4; ++ax1_1_s_7) {
      if (ax1_1_s_7 < 2) {
        A_shared_dyn_local[(ax1_1_s_7 + 2)] = ((float*)buf_dyn_shmem)[(((((((k_0 & 3) * 256) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_7) + 224)];
      }
    }
    for (int ax1_0_7 = 0; ax1_0_7 < 2; ++ax1_0_7) {
      *(float4*)(B_shared_dyn_local + ((ax1_0_7 * 4) + 8)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((k_0 & 3) * 384) + (((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_7 * 4)) >> 6) * 64)) + (ax1_0_7 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 1360) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
    }
    for (int i_2_1_s_48 = 0; i_2_1_s_48 < 4; ++i_2_1_s_48) {
      if (i_2_1_s_48 < 2) {
        Y_local[(i_2_1_s_48 * 8)] = (Y_local[(i_2_1_s_48 * 8)] + (A_shared_dyn_local[i_2_1_s_48] * B_shared_dyn_local[0]));
      }
    }
    for (int i_2_1_s_49 = 0; i_2_1_s_49 < 4; ++i_2_1_s_49) {
      if (i_2_1_s_49 < 2) {
        Y_local[((i_2_1_s_49 * 8) + 1)] = (Y_local[((i_2_1_s_49 * 8) + 1)] + (A_shared_dyn_local[i_2_1_s_49] * B_shared_dyn_local[1]));
      }
    }
    for (int i_2_1_s_50 = 0; i_2_1_s_50 < 4; ++i_2_1_s_50) {
      if (i_2_1_s_50 < 2) {
        Y_local[((i_2_1_s_50 * 8) + 2)] = (Y_local[((i_2_1_s_50 * 8) + 2)] + (A_shared_dyn_local[i_2_1_s_50] * B_shared_dyn_local[2]));
      }
    }
    for (int i_2_1_s_51 = 0; i_2_1_s_51 < 4; ++i_2_1_s_51) {
      if (i_2_1_s_51 < 2) {
        Y_local[((i_2_1_s_51 * 8) + 3)] = (Y_local[((i_2_1_s_51 * 8) + 3)] + (A_shared_dyn_local[i_2_1_s_51] * B_shared_dyn_local[3]));
      }
    }
    for (int i_2_1_s_52 = 0; i_2_1_s_52 < 4; ++i_2_1_s_52) {
      if (i_2_1_s_52 < 2) {
        Y_local[((i_2_1_s_52 * 8) + 4)] = (Y_local[((i_2_1_s_52 * 8) + 4)] + (A_shared_dyn_local[i_2_1_s_52] * B_shared_dyn_local[4]));
      }
    }
    for (int i_2_1_s_53 = 0; i_2_1_s_53 < 4; ++i_2_1_s_53) {
      if (i_2_1_s_53 < 2) {
        Y_local[((i_2_1_s_53 * 8) + 5)] = (Y_local[((i_2_1_s_53 * 8) + 5)] + (A_shared_dyn_local[i_2_1_s_53] * B_shared_dyn_local[5]));
      }
    }
    for (int i_2_1_s_54 = 0; i_2_1_s_54 < 4; ++i_2_1_s_54) {
      if (i_2_1_s_54 < 2) {
        Y_local[((i_2_1_s_54 * 8) + 6)] = (Y_local[((i_2_1_s_54 * 8) + 6)] + (A_shared_dyn_local[i_2_1_s_54] * B_shared_dyn_local[6]));
      }
    }
    for (int i_2_1_s_55 = 0; i_2_1_s_55 < 4; ++i_2_1_s_55) {
      if (i_2_1_s_55 < 2) {
        Y_local[((i_2_1_s_55 * 8) + 7)] = (Y_local[((i_2_1_s_55 * 8) + 7)] + (A_shared_dyn_local[i_2_1_s_55] * B_shared_dyn_local[7]));
      }
    }
    for (int ax1_1_s_8 = 0; ax1_1_s_8 < 4; ++ax1_1_s_8) {
      if (ax1_1_s_8 < 2) {
        A_shared_dyn_local[ax1_1_s_8] = ((float*)buf_dyn_shmem)[(((((((k_0 + 1) & 3) * 256) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_8)];
      }
    }
    for (int ax1_0_8 = 0; ax1_0_8 < 2; ++ax1_0_8) {
      *(float4*)(B_shared_dyn_local + (ax1_0_8 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((((k_0 + 1) & 3) * 384) + (((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_8 * 4)) >> 6) * 64)) + (ax1_0_8 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 1024) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
    }
    for (int i_2_1_s_56 = 0; i_2_1_s_56 < 4; ++i_2_1_s_56) {
      if (i_2_1_s_56 < 2) {
        Y_local[(i_2_1_s_56 * 8)] = (Y_local[(i_2_1_s_56 * 8)] + (A_shared_dyn_local[(i_2_1_s_56 + 2)] * B_shared_dyn_local[8]));
      }
    }
    for (int i_2_1_s_57 = 0; i_2_1_s_57 < 4; ++i_2_1_s_57) {
      if (i_2_1_s_57 < 2) {
        Y_local[((i_2_1_s_57 * 8) + 1)] = (Y_local[((i_2_1_s_57 * 8) + 1)] + (A_shared_dyn_local[(i_2_1_s_57 + 2)] * B_shared_dyn_local[9]));
      }
    }
    for (int i_2_1_s_58 = 0; i_2_1_s_58 < 4; ++i_2_1_s_58) {
      if (i_2_1_s_58 < 2) {
        Y_local[((i_2_1_s_58 * 8) + 2)] = (Y_local[((i_2_1_s_58 * 8) + 2)] + (A_shared_dyn_local[(i_2_1_s_58 + 2)] * B_shared_dyn_local[10]));
      }
    }
    for (int i_2_1_s_59 = 0; i_2_1_s_59 < 4; ++i_2_1_s_59) {
      if (i_2_1_s_59 < 2) {
        Y_local[((i_2_1_s_59 * 8) + 3)] = (Y_local[((i_2_1_s_59 * 8) + 3)] + (A_shared_dyn_local[(i_2_1_s_59 + 2)] * B_shared_dyn_local[11]));
      }
    }
    for (int i_2_1_s_60 = 0; i_2_1_s_60 < 4; ++i_2_1_s_60) {
      if (i_2_1_s_60 < 2) {
        Y_local[((i_2_1_s_60 * 8) + 4)] = (Y_local[((i_2_1_s_60 * 8) + 4)] + (A_shared_dyn_local[(i_2_1_s_60 + 2)] * B_shared_dyn_local[12]));
      }
    }
    for (int i_2_1_s_61 = 0; i_2_1_s_61 < 4; ++i_2_1_s_61) {
      if (i_2_1_s_61 < 2) {
        Y_local[((i_2_1_s_61 * 8) + 5)] = (Y_local[((i_2_1_s_61 * 8) + 5)] + (A_shared_dyn_local[(i_2_1_s_61 + 2)] * B_shared_dyn_local[13]));
      }
    }
    for (int i_2_1_s_62 = 0; i_2_1_s_62 < 4; ++i_2_1_s_62) {
      if (i_2_1_s_62 < 2) {
        Y_local[((i_2_1_s_62 * 8) + 6)] = (Y_local[((i_2_1_s_62 * 8) + 6)] + (A_shared_dyn_local[(i_2_1_s_62 + 2)] * B_shared_dyn_local[14]));
      }
    }
    for (int i_2_1_s_63 = 0; i_2_1_s_63 < 4; ++i_2_1_s_63) {
      if (i_2_1_s_63 < 2) {
        Y_local[((i_2_1_s_63 * 8) + 7)] = (Y_local[((i_2_1_s_63 * 8) + 7)] + (A_shared_dyn_local[(i_2_1_s_63 + 2)] * B_shared_dyn_local[15]));
      }
    }
  }
__asm__ __volatile__("cp.async.wait_group 1;");

  __syncthreads();
  for (int ax1_1_s_9 = 0; ax1_1_s_9 < 4; ++ax1_1_s_9) {
    if (ax1_1_s_9 < 2) {
      A_shared_dyn_local[(ax1_1_s_9 + 2)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 7) >> 2) * 16) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_9) + 288)];
    }
  }
  for (int ax1_0_9 = 0; ax1_0_9 < 2; ++ax1_0_9) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_9 * 4) + 8)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_9 * 4)) >> 6) * 64) + (ax1_0_9 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 1456) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
  }
  for (int i_2_1_s_64 = 0; i_2_1_s_64 < 4; ++i_2_1_s_64) {
    if (i_2_1_s_64 < 2) {
      Y_local[(i_2_1_s_64 * 8)] = (Y_local[(i_2_1_s_64 * 8)] + (A_shared_dyn_local[i_2_1_s_64] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_65 = 0; i_2_1_s_65 < 4; ++i_2_1_s_65) {
    if (i_2_1_s_65 < 2) {
      Y_local[((i_2_1_s_65 * 8) + 1)] = (Y_local[((i_2_1_s_65 * 8) + 1)] + (A_shared_dyn_local[i_2_1_s_65] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_66 = 0; i_2_1_s_66 < 4; ++i_2_1_s_66) {
    if (i_2_1_s_66 < 2) {
      Y_local[((i_2_1_s_66 * 8) + 2)] = (Y_local[((i_2_1_s_66 * 8) + 2)] + (A_shared_dyn_local[i_2_1_s_66] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_67 = 0; i_2_1_s_67 < 4; ++i_2_1_s_67) {
    if (i_2_1_s_67 < 2) {
      Y_local[((i_2_1_s_67 * 8) + 3)] = (Y_local[((i_2_1_s_67 * 8) + 3)] + (A_shared_dyn_local[i_2_1_s_67] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_68 = 0; i_2_1_s_68 < 4; ++i_2_1_s_68) {
    if (i_2_1_s_68 < 2) {
      Y_local[((i_2_1_s_68 * 8) + 4)] = (Y_local[((i_2_1_s_68 * 8) + 4)] + (A_shared_dyn_local[i_2_1_s_68] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_69 = 0; i_2_1_s_69 < 4; ++i_2_1_s_69) {
    if (i_2_1_s_69 < 2) {
      Y_local[((i_2_1_s_69 * 8) + 5)] = (Y_local[((i_2_1_s_69 * 8) + 5)] + (A_shared_dyn_local[i_2_1_s_69] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_70 = 0; i_2_1_s_70 < 4; ++i_2_1_s_70) {
    if (i_2_1_s_70 < 2) {
      Y_local[((i_2_1_s_70 * 8) + 6)] = (Y_local[((i_2_1_s_70 * 8) + 6)] + (A_shared_dyn_local[i_2_1_s_70] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_71 = 0; i_2_1_s_71 < 4; ++i_2_1_s_71) {
    if (i_2_1_s_71 < 2) {
      Y_local[((i_2_1_s_71 * 8) + 7)] = (Y_local[((i_2_1_s_71 * 8) + 7)] + (A_shared_dyn_local[i_2_1_s_71] * B_shared_dyn_local[7]));
    }
  }
  for (int ax1_1_s_10 = 0; ax1_1_s_10 < 4; ++ax1_1_s_10) {
    if (ax1_1_s_10 < 2) {
      A_shared_dyn_local[ax1_1_s_10] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 7) >> 2) * 16) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_10) + 320)];
    }
  }
  for (int ax1_0_10 = 0; ax1_0_10 < 2; ++ax1_0_10) {
    *(float4*)(B_shared_dyn_local + (ax1_0_10 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_10 * 4)) >> 6) * 64) + (ax1_0_10 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 1504) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
  }
  for (int i_2_1_s_72 = 0; i_2_1_s_72 < 4; ++i_2_1_s_72) {
    if (i_2_1_s_72 < 2) {
      Y_local[(i_2_1_s_72 * 8)] = (Y_local[(i_2_1_s_72 * 8)] + (A_shared_dyn_local[(i_2_1_s_72 + 2)] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_73 = 0; i_2_1_s_73 < 4; ++i_2_1_s_73) {
    if (i_2_1_s_73 < 2) {
      Y_local[((i_2_1_s_73 * 8) + 1)] = (Y_local[((i_2_1_s_73 * 8) + 1)] + (A_shared_dyn_local[(i_2_1_s_73 + 2)] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_74 = 0; i_2_1_s_74 < 4; ++i_2_1_s_74) {
    if (i_2_1_s_74 < 2) {
      Y_local[((i_2_1_s_74 * 8) + 2)] = (Y_local[((i_2_1_s_74 * 8) + 2)] + (A_shared_dyn_local[(i_2_1_s_74 + 2)] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_75 = 0; i_2_1_s_75 < 4; ++i_2_1_s_75) {
    if (i_2_1_s_75 < 2) {
      Y_local[((i_2_1_s_75 * 8) + 3)] = (Y_local[((i_2_1_s_75 * 8) + 3)] + (A_shared_dyn_local[(i_2_1_s_75 + 2)] * B_shared_dyn_local[11]));
    }
  }
  for (int i_2_1_s_76 = 0; i_2_1_s_76 < 4; ++i_2_1_s_76) {
    if (i_2_1_s_76 < 2) {
      Y_local[((i_2_1_s_76 * 8) + 4)] = (Y_local[((i_2_1_s_76 * 8) + 4)] + (A_shared_dyn_local[(i_2_1_s_76 + 2)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_77 = 0; i_2_1_s_77 < 4; ++i_2_1_s_77) {
    if (i_2_1_s_77 < 2) {
      Y_local[((i_2_1_s_77 * 8) + 5)] = (Y_local[((i_2_1_s_77 * 8) + 5)] + (A_shared_dyn_local[(i_2_1_s_77 + 2)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_78 = 0; i_2_1_s_78 < 4; ++i_2_1_s_78) {
    if (i_2_1_s_78 < 2) {
      Y_local[((i_2_1_s_78 * 8) + 6)] = (Y_local[((i_2_1_s_78 * 8) + 6)] + (A_shared_dyn_local[(i_2_1_s_78 + 2)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_79 = 0; i_2_1_s_79 < 4; ++i_2_1_s_79) {
    if (i_2_1_s_79 < 2) {
      Y_local[((i_2_1_s_79 * 8) + 7)] = (Y_local[((i_2_1_s_79 * 8) + 7)] + (A_shared_dyn_local[(i_2_1_s_79 + 2)] * B_shared_dyn_local[15]));
    }
  }
  for (int ax1_1_s_11 = 0; ax1_1_s_11 < 4; ++ax1_1_s_11) {
    if (ax1_1_s_11 < 2) {
      A_shared_dyn_local[(ax1_1_s_11 + 2)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 7) >> 2) * 16) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_11) + 352)];
    }
  }
  for (int ax1_0_11 = 0; ax1_0_11 < 2; ++ax1_0_11) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_11 * 4) + 8)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_11 * 4)) >> 6) * 64) + (ax1_0_11 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 1552) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
  }
  for (int i_2_1_s_80 = 0; i_2_1_s_80 < 4; ++i_2_1_s_80) {
    if (i_2_1_s_80 < 2) {
      Y_local[(i_2_1_s_80 * 8)] = (Y_local[(i_2_1_s_80 * 8)] + (A_shared_dyn_local[i_2_1_s_80] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_81 = 0; i_2_1_s_81 < 4; ++i_2_1_s_81) {
    if (i_2_1_s_81 < 2) {
      Y_local[((i_2_1_s_81 * 8) + 1)] = (Y_local[((i_2_1_s_81 * 8) + 1)] + (A_shared_dyn_local[i_2_1_s_81] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_82 = 0; i_2_1_s_82 < 4; ++i_2_1_s_82) {
    if (i_2_1_s_82 < 2) {
      Y_local[((i_2_1_s_82 * 8) + 2)] = (Y_local[((i_2_1_s_82 * 8) + 2)] + (A_shared_dyn_local[i_2_1_s_82] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_83 = 0; i_2_1_s_83 < 4; ++i_2_1_s_83) {
    if (i_2_1_s_83 < 2) {
      Y_local[((i_2_1_s_83 * 8) + 3)] = (Y_local[((i_2_1_s_83 * 8) + 3)] + (A_shared_dyn_local[i_2_1_s_83] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_84 = 0; i_2_1_s_84 < 4; ++i_2_1_s_84) {
    if (i_2_1_s_84 < 2) {
      Y_local[((i_2_1_s_84 * 8) + 4)] = (Y_local[((i_2_1_s_84 * 8) + 4)] + (A_shared_dyn_local[i_2_1_s_84] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_85 = 0; i_2_1_s_85 < 4; ++i_2_1_s_85) {
    if (i_2_1_s_85 < 2) {
      Y_local[((i_2_1_s_85 * 8) + 5)] = (Y_local[((i_2_1_s_85 * 8) + 5)] + (A_shared_dyn_local[i_2_1_s_85] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_86 = 0; i_2_1_s_86 < 4; ++i_2_1_s_86) {
    if (i_2_1_s_86 < 2) {
      Y_local[((i_2_1_s_86 * 8) + 6)] = (Y_local[((i_2_1_s_86 * 8) + 6)] + (A_shared_dyn_local[i_2_1_s_86] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_87 = 0; i_2_1_s_87 < 4; ++i_2_1_s_87) {
    if (i_2_1_s_87 < 2) {
      Y_local[((i_2_1_s_87 * 8) + 7)] = (Y_local[((i_2_1_s_87 * 8) + 7)] + (A_shared_dyn_local[i_2_1_s_87] * B_shared_dyn_local[7]));
    }
  }
  for (int ax1_1_s_12 = 0; ax1_1_s_12 < 4; ++ax1_1_s_12) {
    if (ax1_1_s_12 < 2) {
      A_shared_dyn_local[ax1_1_s_12] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 7) >> 2) * 16) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_12) + 384)];
    }
  }
  for (int ax1_0_12 = 0; ax1_0_12 < 2; ++ax1_0_12) {
    *(float4*)(B_shared_dyn_local + (ax1_0_12 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_12 * 4)) >> 6) * 64) + (ax1_0_12 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 1600) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
  }
  for (int i_2_1_s_88 = 0; i_2_1_s_88 < 4; ++i_2_1_s_88) {
    if (i_2_1_s_88 < 2) {
      Y_local[(i_2_1_s_88 * 8)] = (Y_local[(i_2_1_s_88 * 8)] + (A_shared_dyn_local[(i_2_1_s_88 + 2)] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_89 = 0; i_2_1_s_89 < 4; ++i_2_1_s_89) {
    if (i_2_1_s_89 < 2) {
      Y_local[((i_2_1_s_89 * 8) + 1)] = (Y_local[((i_2_1_s_89 * 8) + 1)] + (A_shared_dyn_local[(i_2_1_s_89 + 2)] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_90 = 0; i_2_1_s_90 < 4; ++i_2_1_s_90) {
    if (i_2_1_s_90 < 2) {
      Y_local[((i_2_1_s_90 * 8) + 2)] = (Y_local[((i_2_1_s_90 * 8) + 2)] + (A_shared_dyn_local[(i_2_1_s_90 + 2)] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_91 = 0; i_2_1_s_91 < 4; ++i_2_1_s_91) {
    if (i_2_1_s_91 < 2) {
      Y_local[((i_2_1_s_91 * 8) + 3)] = (Y_local[((i_2_1_s_91 * 8) + 3)] + (A_shared_dyn_local[(i_2_1_s_91 + 2)] * B_shared_dyn_local[11]));
    }
  }
  for (int i_2_1_s_92 = 0; i_2_1_s_92 < 4; ++i_2_1_s_92) {
    if (i_2_1_s_92 < 2) {
      Y_local[((i_2_1_s_92 * 8) + 4)] = (Y_local[((i_2_1_s_92 * 8) + 4)] + (A_shared_dyn_local[(i_2_1_s_92 + 2)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_93 = 0; i_2_1_s_93 < 4; ++i_2_1_s_93) {
    if (i_2_1_s_93 < 2) {
      Y_local[((i_2_1_s_93 * 8) + 5)] = (Y_local[((i_2_1_s_93 * 8) + 5)] + (A_shared_dyn_local[(i_2_1_s_93 + 2)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_94 = 0; i_2_1_s_94 < 4; ++i_2_1_s_94) {
    if (i_2_1_s_94 < 2) {
      Y_local[((i_2_1_s_94 * 8) + 6)] = (Y_local[((i_2_1_s_94 * 8) + 6)] + (A_shared_dyn_local[(i_2_1_s_94 + 2)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_95 = 0; i_2_1_s_95 < 4; ++i_2_1_s_95) {
    if (i_2_1_s_95 < 2) {
      Y_local[((i_2_1_s_95 * 8) + 7)] = (Y_local[((i_2_1_s_95 * 8) + 7)] + (A_shared_dyn_local[(i_2_1_s_95 + 2)] * B_shared_dyn_local[15]));
    }
  }
  for (int ax1_1_s_13 = 0; ax1_1_s_13 < 4; ++ax1_1_s_13) {
    if (ax1_1_s_13 < 2) {
      A_shared_dyn_local[(ax1_1_s_13 + 2)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 7) >> 2) * 16) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_13) + 416)];
    }
  }
  for (int ax1_0_13 = 0; ax1_0_13 < 2; ++ax1_0_13) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_13 * 4) + 8)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_13 * 4)) >> 6) * 64) + (ax1_0_13 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 1648) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
  }
  for (int i_2_1_s_96 = 0; i_2_1_s_96 < 4; ++i_2_1_s_96) {
    if (i_2_1_s_96 < 2) {
      Y_local[(i_2_1_s_96 * 8)] = (Y_local[(i_2_1_s_96 * 8)] + (A_shared_dyn_local[i_2_1_s_96] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_97 = 0; i_2_1_s_97 < 4; ++i_2_1_s_97) {
    if (i_2_1_s_97 < 2) {
      Y_local[((i_2_1_s_97 * 8) + 1)] = (Y_local[((i_2_1_s_97 * 8) + 1)] + (A_shared_dyn_local[i_2_1_s_97] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_98 = 0; i_2_1_s_98 < 4; ++i_2_1_s_98) {
    if (i_2_1_s_98 < 2) {
      Y_local[((i_2_1_s_98 * 8) + 2)] = (Y_local[((i_2_1_s_98 * 8) + 2)] + (A_shared_dyn_local[i_2_1_s_98] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_99 = 0; i_2_1_s_99 < 4; ++i_2_1_s_99) {
    if (i_2_1_s_99 < 2) {
      Y_local[((i_2_1_s_99 * 8) + 3)] = (Y_local[((i_2_1_s_99 * 8) + 3)] + (A_shared_dyn_local[i_2_1_s_99] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_100 = 0; i_2_1_s_100 < 4; ++i_2_1_s_100) {
    if (i_2_1_s_100 < 2) {
      Y_local[((i_2_1_s_100 * 8) + 4)] = (Y_local[((i_2_1_s_100 * 8) + 4)] + (A_shared_dyn_local[i_2_1_s_100] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_101 = 0; i_2_1_s_101 < 4; ++i_2_1_s_101) {
    if (i_2_1_s_101 < 2) {
      Y_local[((i_2_1_s_101 * 8) + 5)] = (Y_local[((i_2_1_s_101 * 8) + 5)] + (A_shared_dyn_local[i_2_1_s_101] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_102 = 0; i_2_1_s_102 < 4; ++i_2_1_s_102) {
    if (i_2_1_s_102 < 2) {
      Y_local[((i_2_1_s_102 * 8) + 6)] = (Y_local[((i_2_1_s_102 * 8) + 6)] + (A_shared_dyn_local[i_2_1_s_102] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_103 = 0; i_2_1_s_103 < 4; ++i_2_1_s_103) {
    if (i_2_1_s_103 < 2) {
      Y_local[((i_2_1_s_103 * 8) + 7)] = (Y_local[((i_2_1_s_103 * 8) + 7)] + (A_shared_dyn_local[i_2_1_s_103] * B_shared_dyn_local[7]));
    }
  }
  for (int ax1_1_s_14 = 0; ax1_1_s_14 < 4; ++ax1_1_s_14) {
    if (ax1_1_s_14 < 2) {
      A_shared_dyn_local[ax1_1_s_14] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 7) >> 2) * 16) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_14) + 448)];
    }
  }
  for (int ax1_0_14 = 0; ax1_0_14 < 2; ++ax1_0_14) {
    *(float4*)(B_shared_dyn_local + (ax1_0_14 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_14 * 4)) >> 6) * 64) + (ax1_0_14 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 1696) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
  }
  for (int i_2_1_s_104 = 0; i_2_1_s_104 < 4; ++i_2_1_s_104) {
    if (i_2_1_s_104 < 2) {
      Y_local[(i_2_1_s_104 * 8)] = (Y_local[(i_2_1_s_104 * 8)] + (A_shared_dyn_local[(i_2_1_s_104 + 2)] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_105 = 0; i_2_1_s_105 < 4; ++i_2_1_s_105) {
    if (i_2_1_s_105 < 2) {
      Y_local[((i_2_1_s_105 * 8) + 1)] = (Y_local[((i_2_1_s_105 * 8) + 1)] + (A_shared_dyn_local[(i_2_1_s_105 + 2)] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_106 = 0; i_2_1_s_106 < 4; ++i_2_1_s_106) {
    if (i_2_1_s_106 < 2) {
      Y_local[((i_2_1_s_106 * 8) + 2)] = (Y_local[((i_2_1_s_106 * 8) + 2)] + (A_shared_dyn_local[(i_2_1_s_106 + 2)] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_107 = 0; i_2_1_s_107 < 4; ++i_2_1_s_107) {
    if (i_2_1_s_107 < 2) {
      Y_local[((i_2_1_s_107 * 8) + 3)] = (Y_local[((i_2_1_s_107 * 8) + 3)] + (A_shared_dyn_local[(i_2_1_s_107 + 2)] * B_shared_dyn_local[11]));
    }
  }
  for (int i_2_1_s_108 = 0; i_2_1_s_108 < 4; ++i_2_1_s_108) {
    if (i_2_1_s_108 < 2) {
      Y_local[((i_2_1_s_108 * 8) + 4)] = (Y_local[((i_2_1_s_108 * 8) + 4)] + (A_shared_dyn_local[(i_2_1_s_108 + 2)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_109 = 0; i_2_1_s_109 < 4; ++i_2_1_s_109) {
    if (i_2_1_s_109 < 2) {
      Y_local[((i_2_1_s_109 * 8) + 5)] = (Y_local[((i_2_1_s_109 * 8) + 5)] + (A_shared_dyn_local[(i_2_1_s_109 + 2)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_110 = 0; i_2_1_s_110 < 4; ++i_2_1_s_110) {
    if (i_2_1_s_110 < 2) {
      Y_local[((i_2_1_s_110 * 8) + 6)] = (Y_local[((i_2_1_s_110 * 8) + 6)] + (A_shared_dyn_local[(i_2_1_s_110 + 2)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_111 = 0; i_2_1_s_111 < 4; ++i_2_1_s_111) {
    if (i_2_1_s_111 < 2) {
      Y_local[((i_2_1_s_111 * 8) + 7)] = (Y_local[((i_2_1_s_111 * 8) + 7)] + (A_shared_dyn_local[(i_2_1_s_111 + 2)] * B_shared_dyn_local[15]));
    }
  }
  for (int ax1_1_s_15 = 0; ax1_1_s_15 < 4; ++ax1_1_s_15) {
    if (ax1_1_s_15 < 2) {
      A_shared_dyn_local[(ax1_1_s_15 + 2)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 7) >> 2) * 16) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_15) + 480)];
    }
  }
  for (int ax1_0_15 = 0; ax1_0_15 < 2; ++ax1_0_15) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_15 * 4) + 8)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_15 * 4)) >> 6) * 64) + (ax1_0_15 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 1744) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
  }
  for (int i_2_1_s_112 = 0; i_2_1_s_112 < 4; ++i_2_1_s_112) {
    if (i_2_1_s_112 < 2) {
      Y_local[(i_2_1_s_112 * 8)] = (Y_local[(i_2_1_s_112 * 8)] + (A_shared_dyn_local[i_2_1_s_112] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_113 = 0; i_2_1_s_113 < 4; ++i_2_1_s_113) {
    if (i_2_1_s_113 < 2) {
      Y_local[((i_2_1_s_113 * 8) + 1)] = (Y_local[((i_2_1_s_113 * 8) + 1)] + (A_shared_dyn_local[i_2_1_s_113] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_114 = 0; i_2_1_s_114 < 4; ++i_2_1_s_114) {
    if (i_2_1_s_114 < 2) {
      Y_local[((i_2_1_s_114 * 8) + 2)] = (Y_local[((i_2_1_s_114 * 8) + 2)] + (A_shared_dyn_local[i_2_1_s_114] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_115 = 0; i_2_1_s_115 < 4; ++i_2_1_s_115) {
    if (i_2_1_s_115 < 2) {
      Y_local[((i_2_1_s_115 * 8) + 3)] = (Y_local[((i_2_1_s_115 * 8) + 3)] + (A_shared_dyn_local[i_2_1_s_115] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_116 = 0; i_2_1_s_116 < 4; ++i_2_1_s_116) {
    if (i_2_1_s_116 < 2) {
      Y_local[((i_2_1_s_116 * 8) + 4)] = (Y_local[((i_2_1_s_116 * 8) + 4)] + (A_shared_dyn_local[i_2_1_s_116] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_117 = 0; i_2_1_s_117 < 4; ++i_2_1_s_117) {
    if (i_2_1_s_117 < 2) {
      Y_local[((i_2_1_s_117 * 8) + 5)] = (Y_local[((i_2_1_s_117 * 8) + 5)] + (A_shared_dyn_local[i_2_1_s_117] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_118 = 0; i_2_1_s_118 < 4; ++i_2_1_s_118) {
    if (i_2_1_s_118 < 2) {
      Y_local[((i_2_1_s_118 * 8) + 6)] = (Y_local[((i_2_1_s_118 * 8) + 6)] + (A_shared_dyn_local[i_2_1_s_118] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_119 = 0; i_2_1_s_119 < 4; ++i_2_1_s_119) {
    if (i_2_1_s_119 < 2) {
      Y_local[((i_2_1_s_119 * 8) + 7)] = (Y_local[((i_2_1_s_119 * 8) + 7)] + (A_shared_dyn_local[i_2_1_s_119] * B_shared_dyn_local[7]));
    }
  }
  for (int ax1_1_s_16 = 0; ax1_1_s_16 < 4; ++ax1_1_s_16) {
    if (ax1_1_s_16 < 2) {
      A_shared_dyn_local[ax1_1_s_16] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 7) >> 2) * 16) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_16) + 512)];
    }
  }
  for (int ax1_0_16 = 0; ax1_0_16 < 2; ++ax1_0_16) {
    *(float4*)(B_shared_dyn_local + (ax1_0_16 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_16 * 4)) >> 6) * 64) + (ax1_0_16 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 1792) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
  }
  for (int i_2_1_s_120 = 0; i_2_1_s_120 < 4; ++i_2_1_s_120) {
    if (i_2_1_s_120 < 2) {
      Y_local[(i_2_1_s_120 * 8)] = (Y_local[(i_2_1_s_120 * 8)] + (A_shared_dyn_local[(i_2_1_s_120 + 2)] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_121 = 0; i_2_1_s_121 < 4; ++i_2_1_s_121) {
    if (i_2_1_s_121 < 2) {
      Y_local[((i_2_1_s_121 * 8) + 1)] = (Y_local[((i_2_1_s_121 * 8) + 1)] + (A_shared_dyn_local[(i_2_1_s_121 + 2)] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_122 = 0; i_2_1_s_122 < 4; ++i_2_1_s_122) {
    if (i_2_1_s_122 < 2) {
      Y_local[((i_2_1_s_122 * 8) + 2)] = (Y_local[((i_2_1_s_122 * 8) + 2)] + (A_shared_dyn_local[(i_2_1_s_122 + 2)] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_123 = 0; i_2_1_s_123 < 4; ++i_2_1_s_123) {
    if (i_2_1_s_123 < 2) {
      Y_local[((i_2_1_s_123 * 8) + 3)] = (Y_local[((i_2_1_s_123 * 8) + 3)] + (A_shared_dyn_local[(i_2_1_s_123 + 2)] * B_shared_dyn_local[11]));
    }
  }
  for (int i_2_1_s_124 = 0; i_2_1_s_124 < 4; ++i_2_1_s_124) {
    if (i_2_1_s_124 < 2) {
      Y_local[((i_2_1_s_124 * 8) + 4)] = (Y_local[((i_2_1_s_124 * 8) + 4)] + (A_shared_dyn_local[(i_2_1_s_124 + 2)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_125 = 0; i_2_1_s_125 < 4; ++i_2_1_s_125) {
    if (i_2_1_s_125 < 2) {
      Y_local[((i_2_1_s_125 * 8) + 5)] = (Y_local[((i_2_1_s_125 * 8) + 5)] + (A_shared_dyn_local[(i_2_1_s_125 + 2)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_126 = 0; i_2_1_s_126 < 4; ++i_2_1_s_126) {
    if (i_2_1_s_126 < 2) {
      Y_local[((i_2_1_s_126 * 8) + 6)] = (Y_local[((i_2_1_s_126 * 8) + 6)] + (A_shared_dyn_local[(i_2_1_s_126 + 2)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_127 = 0; i_2_1_s_127 < 4; ++i_2_1_s_127) {
    if (i_2_1_s_127 < 2) {
      Y_local[((i_2_1_s_127 * 8) + 7)] = (Y_local[((i_2_1_s_127 * 8) + 7)] + (A_shared_dyn_local[(i_2_1_s_127 + 2)] * B_shared_dyn_local[15]));
    }
  }
__asm__ __volatile__("cp.async.wait_group 0;");

  __syncthreads();
  for (int ax1_1_s_17 = 0; ax1_1_s_17 < 4; ++ax1_1_s_17) {
    if (ax1_1_s_17 < 2) {
      A_shared_dyn_local[(ax1_1_s_17 + 2)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 7) >> 2) * 16) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_17) + 544)];
    }
  }
  for (int ax1_0_17 = 0; ax1_0_17 < 2; ++ax1_0_17) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_17 * 4) + 8)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_17 * 4)) >> 6) * 64) + (ax1_0_17 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 1840) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
  }
  for (int i_2_1_s_128 = 0; i_2_1_s_128 < 4; ++i_2_1_s_128) {
    if (i_2_1_s_128 < 2) {
      Y_local[(i_2_1_s_128 * 8)] = (Y_local[(i_2_1_s_128 * 8)] + (A_shared_dyn_local[i_2_1_s_128] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_129 = 0; i_2_1_s_129 < 4; ++i_2_1_s_129) {
    if (i_2_1_s_129 < 2) {
      Y_local[((i_2_1_s_129 * 8) + 1)] = (Y_local[((i_2_1_s_129 * 8) + 1)] + (A_shared_dyn_local[i_2_1_s_129] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_130 = 0; i_2_1_s_130 < 4; ++i_2_1_s_130) {
    if (i_2_1_s_130 < 2) {
      Y_local[((i_2_1_s_130 * 8) + 2)] = (Y_local[((i_2_1_s_130 * 8) + 2)] + (A_shared_dyn_local[i_2_1_s_130] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_131 = 0; i_2_1_s_131 < 4; ++i_2_1_s_131) {
    if (i_2_1_s_131 < 2) {
      Y_local[((i_2_1_s_131 * 8) + 3)] = (Y_local[((i_2_1_s_131 * 8) + 3)] + (A_shared_dyn_local[i_2_1_s_131] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_132 = 0; i_2_1_s_132 < 4; ++i_2_1_s_132) {
    if (i_2_1_s_132 < 2) {
      Y_local[((i_2_1_s_132 * 8) + 4)] = (Y_local[((i_2_1_s_132 * 8) + 4)] + (A_shared_dyn_local[i_2_1_s_132] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_133 = 0; i_2_1_s_133 < 4; ++i_2_1_s_133) {
    if (i_2_1_s_133 < 2) {
      Y_local[((i_2_1_s_133 * 8) + 5)] = (Y_local[((i_2_1_s_133 * 8) + 5)] + (A_shared_dyn_local[i_2_1_s_133] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_134 = 0; i_2_1_s_134 < 4; ++i_2_1_s_134) {
    if (i_2_1_s_134 < 2) {
      Y_local[((i_2_1_s_134 * 8) + 6)] = (Y_local[((i_2_1_s_134 * 8) + 6)] + (A_shared_dyn_local[i_2_1_s_134] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_135 = 0; i_2_1_s_135 < 4; ++i_2_1_s_135) {
    if (i_2_1_s_135 < 2) {
      Y_local[((i_2_1_s_135 * 8) + 7)] = (Y_local[((i_2_1_s_135 * 8) + 7)] + (A_shared_dyn_local[i_2_1_s_135] * B_shared_dyn_local[7]));
    }
  }
  for (int ax1_1_s_18 = 0; ax1_1_s_18 < 4; ++ax1_1_s_18) {
    if (ax1_1_s_18 < 2) {
      A_shared_dyn_local[ax1_1_s_18] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 7) >> 2) * 16) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_18) + 576)];
    }
  }
  for (int ax1_0_18 = 0; ax1_0_18 < 2; ++ax1_0_18) {
    *(float4*)(B_shared_dyn_local + (ax1_0_18 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_18 * 4)) >> 6) * 64) + (ax1_0_18 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 1888) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
  }
  for (int i_2_1_s_136 = 0; i_2_1_s_136 < 4; ++i_2_1_s_136) {
    if (i_2_1_s_136 < 2) {
      Y_local[(i_2_1_s_136 * 8)] = (Y_local[(i_2_1_s_136 * 8)] + (A_shared_dyn_local[(i_2_1_s_136 + 2)] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_137 = 0; i_2_1_s_137 < 4; ++i_2_1_s_137) {
    if (i_2_1_s_137 < 2) {
      Y_local[((i_2_1_s_137 * 8) + 1)] = (Y_local[((i_2_1_s_137 * 8) + 1)] + (A_shared_dyn_local[(i_2_1_s_137 + 2)] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_138 = 0; i_2_1_s_138 < 4; ++i_2_1_s_138) {
    if (i_2_1_s_138 < 2) {
      Y_local[((i_2_1_s_138 * 8) + 2)] = (Y_local[((i_2_1_s_138 * 8) + 2)] + (A_shared_dyn_local[(i_2_1_s_138 + 2)] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_139 = 0; i_2_1_s_139 < 4; ++i_2_1_s_139) {
    if (i_2_1_s_139 < 2) {
      Y_local[((i_2_1_s_139 * 8) + 3)] = (Y_local[((i_2_1_s_139 * 8) + 3)] + (A_shared_dyn_local[(i_2_1_s_139 + 2)] * B_shared_dyn_local[11]));
    }
  }
  for (int i_2_1_s_140 = 0; i_2_1_s_140 < 4; ++i_2_1_s_140) {
    if (i_2_1_s_140 < 2) {
      Y_local[((i_2_1_s_140 * 8) + 4)] = (Y_local[((i_2_1_s_140 * 8) + 4)] + (A_shared_dyn_local[(i_2_1_s_140 + 2)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_141 = 0; i_2_1_s_141 < 4; ++i_2_1_s_141) {
    if (i_2_1_s_141 < 2) {
      Y_local[((i_2_1_s_141 * 8) + 5)] = (Y_local[((i_2_1_s_141 * 8) + 5)] + (A_shared_dyn_local[(i_2_1_s_141 + 2)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_142 = 0; i_2_1_s_142 < 4; ++i_2_1_s_142) {
    if (i_2_1_s_142 < 2) {
      Y_local[((i_2_1_s_142 * 8) + 6)] = (Y_local[((i_2_1_s_142 * 8) + 6)] + (A_shared_dyn_local[(i_2_1_s_142 + 2)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_143 = 0; i_2_1_s_143 < 4; ++i_2_1_s_143) {
    if (i_2_1_s_143 < 2) {
      Y_local[((i_2_1_s_143 * 8) + 7)] = (Y_local[((i_2_1_s_143 * 8) + 7)] + (A_shared_dyn_local[(i_2_1_s_143 + 2)] * B_shared_dyn_local[15]));
    }
  }
  for (int ax1_1_s_19 = 0; ax1_1_s_19 < 4; ++ax1_1_s_19) {
    if (ax1_1_s_19 < 2) {
      A_shared_dyn_local[(ax1_1_s_19 + 2)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 7) >> 2) * 16) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_19) + 608)];
    }
  }
  for (int ax1_0_19 = 0; ax1_0_19 < 2; ++ax1_0_19) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_19 * 4) + 8)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_19 * 4)) >> 6) * 64) + (ax1_0_19 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 1936) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
  }
  for (int i_2_1_s_144 = 0; i_2_1_s_144 < 4; ++i_2_1_s_144) {
    if (i_2_1_s_144 < 2) {
      Y_local[(i_2_1_s_144 * 8)] = (Y_local[(i_2_1_s_144 * 8)] + (A_shared_dyn_local[i_2_1_s_144] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_145 = 0; i_2_1_s_145 < 4; ++i_2_1_s_145) {
    if (i_2_1_s_145 < 2) {
      Y_local[((i_2_1_s_145 * 8) + 1)] = (Y_local[((i_2_1_s_145 * 8) + 1)] + (A_shared_dyn_local[i_2_1_s_145] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_146 = 0; i_2_1_s_146 < 4; ++i_2_1_s_146) {
    if (i_2_1_s_146 < 2) {
      Y_local[((i_2_1_s_146 * 8) + 2)] = (Y_local[((i_2_1_s_146 * 8) + 2)] + (A_shared_dyn_local[i_2_1_s_146] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_147 = 0; i_2_1_s_147 < 4; ++i_2_1_s_147) {
    if (i_2_1_s_147 < 2) {
      Y_local[((i_2_1_s_147 * 8) + 3)] = (Y_local[((i_2_1_s_147 * 8) + 3)] + (A_shared_dyn_local[i_2_1_s_147] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_148 = 0; i_2_1_s_148 < 4; ++i_2_1_s_148) {
    if (i_2_1_s_148 < 2) {
      Y_local[((i_2_1_s_148 * 8) + 4)] = (Y_local[((i_2_1_s_148 * 8) + 4)] + (A_shared_dyn_local[i_2_1_s_148] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_149 = 0; i_2_1_s_149 < 4; ++i_2_1_s_149) {
    if (i_2_1_s_149 < 2) {
      Y_local[((i_2_1_s_149 * 8) + 5)] = (Y_local[((i_2_1_s_149 * 8) + 5)] + (A_shared_dyn_local[i_2_1_s_149] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_150 = 0; i_2_1_s_150 < 4; ++i_2_1_s_150) {
    if (i_2_1_s_150 < 2) {
      Y_local[((i_2_1_s_150 * 8) + 6)] = (Y_local[((i_2_1_s_150 * 8) + 6)] + (A_shared_dyn_local[i_2_1_s_150] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_151 = 0; i_2_1_s_151 < 4; ++i_2_1_s_151) {
    if (i_2_1_s_151 < 2) {
      Y_local[((i_2_1_s_151 * 8) + 7)] = (Y_local[((i_2_1_s_151 * 8) + 7)] + (A_shared_dyn_local[i_2_1_s_151] * B_shared_dyn_local[7]));
    }
  }
  for (int ax1_1_s_20 = 0; ax1_1_s_20 < 4; ++ax1_1_s_20) {
    if (ax1_1_s_20 < 2) {
      A_shared_dyn_local[ax1_1_s_20] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 7) >> 2) * 16) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_20) + 640)];
    }
  }
  for (int ax1_0_20 = 0; ax1_0_20 < 2; ++ax1_0_20) {
    *(float4*)(B_shared_dyn_local + (ax1_0_20 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_20 * 4)) >> 6) * 64) + (ax1_0_20 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 1984) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
  }
  for (int i_2_1_s_152 = 0; i_2_1_s_152 < 4; ++i_2_1_s_152) {
    if (i_2_1_s_152 < 2) {
      Y_local[(i_2_1_s_152 * 8)] = (Y_local[(i_2_1_s_152 * 8)] + (A_shared_dyn_local[(i_2_1_s_152 + 2)] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_153 = 0; i_2_1_s_153 < 4; ++i_2_1_s_153) {
    if (i_2_1_s_153 < 2) {
      Y_local[((i_2_1_s_153 * 8) + 1)] = (Y_local[((i_2_1_s_153 * 8) + 1)] + (A_shared_dyn_local[(i_2_1_s_153 + 2)] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_154 = 0; i_2_1_s_154 < 4; ++i_2_1_s_154) {
    if (i_2_1_s_154 < 2) {
      Y_local[((i_2_1_s_154 * 8) + 2)] = (Y_local[((i_2_1_s_154 * 8) + 2)] + (A_shared_dyn_local[(i_2_1_s_154 + 2)] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_155 = 0; i_2_1_s_155 < 4; ++i_2_1_s_155) {
    if (i_2_1_s_155 < 2) {
      Y_local[((i_2_1_s_155 * 8) + 3)] = (Y_local[((i_2_1_s_155 * 8) + 3)] + (A_shared_dyn_local[(i_2_1_s_155 + 2)] * B_shared_dyn_local[11]));
    }
  }
  for (int i_2_1_s_156 = 0; i_2_1_s_156 < 4; ++i_2_1_s_156) {
    if (i_2_1_s_156 < 2) {
      Y_local[((i_2_1_s_156 * 8) + 4)] = (Y_local[((i_2_1_s_156 * 8) + 4)] + (A_shared_dyn_local[(i_2_1_s_156 + 2)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_157 = 0; i_2_1_s_157 < 4; ++i_2_1_s_157) {
    if (i_2_1_s_157 < 2) {
      Y_local[((i_2_1_s_157 * 8) + 5)] = (Y_local[((i_2_1_s_157 * 8) + 5)] + (A_shared_dyn_local[(i_2_1_s_157 + 2)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_158 = 0; i_2_1_s_158 < 4; ++i_2_1_s_158) {
    if (i_2_1_s_158 < 2) {
      Y_local[((i_2_1_s_158 * 8) + 6)] = (Y_local[((i_2_1_s_158 * 8) + 6)] + (A_shared_dyn_local[(i_2_1_s_158 + 2)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_159 = 0; i_2_1_s_159 < 4; ++i_2_1_s_159) {
    if (i_2_1_s_159 < 2) {
      Y_local[((i_2_1_s_159 * 8) + 7)] = (Y_local[((i_2_1_s_159 * 8) + 7)] + (A_shared_dyn_local[(i_2_1_s_159 + 2)] * B_shared_dyn_local[15]));
    }
  }
  for (int ax1_1_s_21 = 0; ax1_1_s_21 < 4; ++ax1_1_s_21) {
    if (ax1_1_s_21 < 2) {
      A_shared_dyn_local[(ax1_1_s_21 + 2)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 7) >> 2) * 16) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_21) + 672)];
    }
  }
  for (int ax1_0_21 = 0; ax1_0_21 < 2; ++ax1_0_21) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_21 * 4) + 8)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_21 * 4)) >> 6) * 64) + (ax1_0_21 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 2032) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
  }
  for (int i_2_1_s_160 = 0; i_2_1_s_160 < 4; ++i_2_1_s_160) {
    if (i_2_1_s_160 < 2) {
      Y_local[(i_2_1_s_160 * 8)] = (Y_local[(i_2_1_s_160 * 8)] + (A_shared_dyn_local[i_2_1_s_160] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_161 = 0; i_2_1_s_161 < 4; ++i_2_1_s_161) {
    if (i_2_1_s_161 < 2) {
      Y_local[((i_2_1_s_161 * 8) + 1)] = (Y_local[((i_2_1_s_161 * 8) + 1)] + (A_shared_dyn_local[i_2_1_s_161] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_162 = 0; i_2_1_s_162 < 4; ++i_2_1_s_162) {
    if (i_2_1_s_162 < 2) {
      Y_local[((i_2_1_s_162 * 8) + 2)] = (Y_local[((i_2_1_s_162 * 8) + 2)] + (A_shared_dyn_local[i_2_1_s_162] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_163 = 0; i_2_1_s_163 < 4; ++i_2_1_s_163) {
    if (i_2_1_s_163 < 2) {
      Y_local[((i_2_1_s_163 * 8) + 3)] = (Y_local[((i_2_1_s_163 * 8) + 3)] + (A_shared_dyn_local[i_2_1_s_163] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_164 = 0; i_2_1_s_164 < 4; ++i_2_1_s_164) {
    if (i_2_1_s_164 < 2) {
      Y_local[((i_2_1_s_164 * 8) + 4)] = (Y_local[((i_2_1_s_164 * 8) + 4)] + (A_shared_dyn_local[i_2_1_s_164] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_165 = 0; i_2_1_s_165 < 4; ++i_2_1_s_165) {
    if (i_2_1_s_165 < 2) {
      Y_local[((i_2_1_s_165 * 8) + 5)] = (Y_local[((i_2_1_s_165 * 8) + 5)] + (A_shared_dyn_local[i_2_1_s_165] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_166 = 0; i_2_1_s_166 < 4; ++i_2_1_s_166) {
    if (i_2_1_s_166 < 2) {
      Y_local[((i_2_1_s_166 * 8) + 6)] = (Y_local[((i_2_1_s_166 * 8) + 6)] + (A_shared_dyn_local[i_2_1_s_166] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_167 = 0; i_2_1_s_167 < 4; ++i_2_1_s_167) {
    if (i_2_1_s_167 < 2) {
      Y_local[((i_2_1_s_167 * 8) + 7)] = (Y_local[((i_2_1_s_167 * 8) + 7)] + (A_shared_dyn_local[i_2_1_s_167] * B_shared_dyn_local[7]));
    }
  }
  for (int ax1_1_s_22 = 0; ax1_1_s_22 < 4; ++ax1_1_s_22) {
    if (ax1_1_s_22 < 2) {
      A_shared_dyn_local[ax1_1_s_22] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 7) >> 2) * 16) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_22) + 704)];
    }
  }
  for (int ax1_0_22 = 0; ax1_0_22 < 2; ++ax1_0_22) {
    *(float4*)(B_shared_dyn_local + (ax1_0_22 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_22 * 4)) >> 6) * 64) + (ax1_0_22 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 2080) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
  }
  for (int i_2_1_s_168 = 0; i_2_1_s_168 < 4; ++i_2_1_s_168) {
    if (i_2_1_s_168 < 2) {
      Y_local[(i_2_1_s_168 * 8)] = (Y_local[(i_2_1_s_168 * 8)] + (A_shared_dyn_local[(i_2_1_s_168 + 2)] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_169 = 0; i_2_1_s_169 < 4; ++i_2_1_s_169) {
    if (i_2_1_s_169 < 2) {
      Y_local[((i_2_1_s_169 * 8) + 1)] = (Y_local[((i_2_1_s_169 * 8) + 1)] + (A_shared_dyn_local[(i_2_1_s_169 + 2)] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_170 = 0; i_2_1_s_170 < 4; ++i_2_1_s_170) {
    if (i_2_1_s_170 < 2) {
      Y_local[((i_2_1_s_170 * 8) + 2)] = (Y_local[((i_2_1_s_170 * 8) + 2)] + (A_shared_dyn_local[(i_2_1_s_170 + 2)] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_171 = 0; i_2_1_s_171 < 4; ++i_2_1_s_171) {
    if (i_2_1_s_171 < 2) {
      Y_local[((i_2_1_s_171 * 8) + 3)] = (Y_local[((i_2_1_s_171 * 8) + 3)] + (A_shared_dyn_local[(i_2_1_s_171 + 2)] * B_shared_dyn_local[11]));
    }
  }
  for (int i_2_1_s_172 = 0; i_2_1_s_172 < 4; ++i_2_1_s_172) {
    if (i_2_1_s_172 < 2) {
      Y_local[((i_2_1_s_172 * 8) + 4)] = (Y_local[((i_2_1_s_172 * 8) + 4)] + (A_shared_dyn_local[(i_2_1_s_172 + 2)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_173 = 0; i_2_1_s_173 < 4; ++i_2_1_s_173) {
    if (i_2_1_s_173 < 2) {
      Y_local[((i_2_1_s_173 * 8) + 5)] = (Y_local[((i_2_1_s_173 * 8) + 5)] + (A_shared_dyn_local[(i_2_1_s_173 + 2)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_174 = 0; i_2_1_s_174 < 4; ++i_2_1_s_174) {
    if (i_2_1_s_174 < 2) {
      Y_local[((i_2_1_s_174 * 8) + 6)] = (Y_local[((i_2_1_s_174 * 8) + 6)] + (A_shared_dyn_local[(i_2_1_s_174 + 2)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_175 = 0; i_2_1_s_175 < 4; ++i_2_1_s_175) {
    if (i_2_1_s_175 < 2) {
      Y_local[((i_2_1_s_175 * 8) + 7)] = (Y_local[((i_2_1_s_175 * 8) + 7)] + (A_shared_dyn_local[(i_2_1_s_175 + 2)] * B_shared_dyn_local[15]));
    }
  }
  for (int ax1_1_s_23 = 0; ax1_1_s_23 < 4; ++ax1_1_s_23) {
    if (ax1_1_s_23 < 2) {
      A_shared_dyn_local[(ax1_1_s_23 + 2)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 7) >> 2) * 16) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_23) + 736)];
    }
  }
  for (int ax1_0_23 = 0; ax1_0_23 < 2; ++ax1_0_23) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_23 * 4) + 8)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_23 * 4)) >> 6) * 64) + (ax1_0_23 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 2128) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
  }
  for (int i_2_1_s_176 = 0; i_2_1_s_176 < 4; ++i_2_1_s_176) {
    if (i_2_1_s_176 < 2) {
      Y_local[(i_2_1_s_176 * 8)] = (Y_local[(i_2_1_s_176 * 8)] + (A_shared_dyn_local[i_2_1_s_176] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_177 = 0; i_2_1_s_177 < 4; ++i_2_1_s_177) {
    if (i_2_1_s_177 < 2) {
      Y_local[((i_2_1_s_177 * 8) + 1)] = (Y_local[((i_2_1_s_177 * 8) + 1)] + (A_shared_dyn_local[i_2_1_s_177] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_178 = 0; i_2_1_s_178 < 4; ++i_2_1_s_178) {
    if (i_2_1_s_178 < 2) {
      Y_local[((i_2_1_s_178 * 8) + 2)] = (Y_local[((i_2_1_s_178 * 8) + 2)] + (A_shared_dyn_local[i_2_1_s_178] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_179 = 0; i_2_1_s_179 < 4; ++i_2_1_s_179) {
    if (i_2_1_s_179 < 2) {
      Y_local[((i_2_1_s_179 * 8) + 3)] = (Y_local[((i_2_1_s_179 * 8) + 3)] + (A_shared_dyn_local[i_2_1_s_179] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_180 = 0; i_2_1_s_180 < 4; ++i_2_1_s_180) {
    if (i_2_1_s_180 < 2) {
      Y_local[((i_2_1_s_180 * 8) + 4)] = (Y_local[((i_2_1_s_180 * 8) + 4)] + (A_shared_dyn_local[i_2_1_s_180] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_181 = 0; i_2_1_s_181 < 4; ++i_2_1_s_181) {
    if (i_2_1_s_181 < 2) {
      Y_local[((i_2_1_s_181 * 8) + 5)] = (Y_local[((i_2_1_s_181 * 8) + 5)] + (A_shared_dyn_local[i_2_1_s_181] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_182 = 0; i_2_1_s_182 < 4; ++i_2_1_s_182) {
    if (i_2_1_s_182 < 2) {
      Y_local[((i_2_1_s_182 * 8) + 6)] = (Y_local[((i_2_1_s_182 * 8) + 6)] + (A_shared_dyn_local[i_2_1_s_182] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_183 = 0; i_2_1_s_183 < 4; ++i_2_1_s_183) {
    if (i_2_1_s_183 < 2) {
      Y_local[((i_2_1_s_183 * 8) + 7)] = (Y_local[((i_2_1_s_183 * 8) + 7)] + (A_shared_dyn_local[i_2_1_s_183] * B_shared_dyn_local[7]));
    }
  }
  for (int ax1_1_s_24 = 0; ax1_1_s_24 < 4; ++ax1_1_s_24) {
    if (ax1_1_s_24 < 2) {
      A_shared_dyn_local[ax1_1_s_24] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 7) >> 2) * 16) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_24) + 768)];
    }
  }
  for (int ax1_0_24 = 0; ax1_0_24 < 2; ++ax1_0_24) {
    *(float4*)(B_shared_dyn_local + (ax1_0_24 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_24 * 4)) >> 6) * 64) + (ax1_0_24 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 2176) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
  }
  for (int i_2_1_s_184 = 0; i_2_1_s_184 < 4; ++i_2_1_s_184) {
    if (i_2_1_s_184 < 2) {
      Y_local[(i_2_1_s_184 * 8)] = (Y_local[(i_2_1_s_184 * 8)] + (A_shared_dyn_local[(i_2_1_s_184 + 2)] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_185 = 0; i_2_1_s_185 < 4; ++i_2_1_s_185) {
    if (i_2_1_s_185 < 2) {
      Y_local[((i_2_1_s_185 * 8) + 1)] = (Y_local[((i_2_1_s_185 * 8) + 1)] + (A_shared_dyn_local[(i_2_1_s_185 + 2)] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_186 = 0; i_2_1_s_186 < 4; ++i_2_1_s_186) {
    if (i_2_1_s_186 < 2) {
      Y_local[((i_2_1_s_186 * 8) + 2)] = (Y_local[((i_2_1_s_186 * 8) + 2)] + (A_shared_dyn_local[(i_2_1_s_186 + 2)] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_187 = 0; i_2_1_s_187 < 4; ++i_2_1_s_187) {
    if (i_2_1_s_187 < 2) {
      Y_local[((i_2_1_s_187 * 8) + 3)] = (Y_local[((i_2_1_s_187 * 8) + 3)] + (A_shared_dyn_local[(i_2_1_s_187 + 2)] * B_shared_dyn_local[11]));
    }
  }
  for (int i_2_1_s_188 = 0; i_2_1_s_188 < 4; ++i_2_1_s_188) {
    if (i_2_1_s_188 < 2) {
      Y_local[((i_2_1_s_188 * 8) + 4)] = (Y_local[((i_2_1_s_188 * 8) + 4)] + (A_shared_dyn_local[(i_2_1_s_188 + 2)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_189 = 0; i_2_1_s_189 < 4; ++i_2_1_s_189) {
    if (i_2_1_s_189 < 2) {
      Y_local[((i_2_1_s_189 * 8) + 5)] = (Y_local[((i_2_1_s_189 * 8) + 5)] + (A_shared_dyn_local[(i_2_1_s_189 + 2)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_190 = 0; i_2_1_s_190 < 4; ++i_2_1_s_190) {
    if (i_2_1_s_190 < 2) {
      Y_local[((i_2_1_s_190 * 8) + 6)] = (Y_local[((i_2_1_s_190 * 8) + 6)] + (A_shared_dyn_local[(i_2_1_s_190 + 2)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_191 = 0; i_2_1_s_191 < 4; ++i_2_1_s_191) {
    if (i_2_1_s_191 < 2) {
      Y_local[((i_2_1_s_191 * 8) + 7)] = (Y_local[((i_2_1_s_191 * 8) + 7)] + (A_shared_dyn_local[(i_2_1_s_191 + 2)] * B_shared_dyn_local[15]));
    }
  }
  for (int ax1_1_s_25 = 0; ax1_1_s_25 < 4; ++ax1_1_s_25) {
    if (ax1_1_s_25 < 2) {
      A_shared_dyn_local[(ax1_1_s_25 + 2)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 7) >> 2) * 16) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_25) + 800)];
    }
  }
  for (int ax1_0_25 = 0; ax1_0_25 < 2; ++ax1_0_25) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_25 * 4) + 8)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_25 * 4)) >> 6) * 64) + (ax1_0_25 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 2224) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
  }
  for (int i_2_1_s_192 = 0; i_2_1_s_192 < 4; ++i_2_1_s_192) {
    if (i_2_1_s_192 < 2) {
      Y_local[(i_2_1_s_192 * 8)] = (Y_local[(i_2_1_s_192 * 8)] + (A_shared_dyn_local[i_2_1_s_192] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_193 = 0; i_2_1_s_193 < 4; ++i_2_1_s_193) {
    if (i_2_1_s_193 < 2) {
      Y_local[((i_2_1_s_193 * 8) + 1)] = (Y_local[((i_2_1_s_193 * 8) + 1)] + (A_shared_dyn_local[i_2_1_s_193] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_194 = 0; i_2_1_s_194 < 4; ++i_2_1_s_194) {
    if (i_2_1_s_194 < 2) {
      Y_local[((i_2_1_s_194 * 8) + 2)] = (Y_local[((i_2_1_s_194 * 8) + 2)] + (A_shared_dyn_local[i_2_1_s_194] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_195 = 0; i_2_1_s_195 < 4; ++i_2_1_s_195) {
    if (i_2_1_s_195 < 2) {
      Y_local[((i_2_1_s_195 * 8) + 3)] = (Y_local[((i_2_1_s_195 * 8) + 3)] + (A_shared_dyn_local[i_2_1_s_195] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_196 = 0; i_2_1_s_196 < 4; ++i_2_1_s_196) {
    if (i_2_1_s_196 < 2) {
      Y_local[((i_2_1_s_196 * 8) + 4)] = (Y_local[((i_2_1_s_196 * 8) + 4)] + (A_shared_dyn_local[i_2_1_s_196] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_197 = 0; i_2_1_s_197 < 4; ++i_2_1_s_197) {
    if (i_2_1_s_197 < 2) {
      Y_local[((i_2_1_s_197 * 8) + 5)] = (Y_local[((i_2_1_s_197 * 8) + 5)] + (A_shared_dyn_local[i_2_1_s_197] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_198 = 0; i_2_1_s_198 < 4; ++i_2_1_s_198) {
    if (i_2_1_s_198 < 2) {
      Y_local[((i_2_1_s_198 * 8) + 6)] = (Y_local[((i_2_1_s_198 * 8) + 6)] + (A_shared_dyn_local[i_2_1_s_198] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_199 = 0; i_2_1_s_199 < 4; ++i_2_1_s_199) {
    if (i_2_1_s_199 < 2) {
      Y_local[((i_2_1_s_199 * 8) + 7)] = (Y_local[((i_2_1_s_199 * 8) + 7)] + (A_shared_dyn_local[i_2_1_s_199] * B_shared_dyn_local[7]));
    }
  }
  for (int ax1_1_s_26 = 0; ax1_1_s_26 < 4; ++ax1_1_s_26) {
    if (ax1_1_s_26 < 2) {
      A_shared_dyn_local[ax1_1_s_26] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 7) >> 2) * 16) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_26) + 832)];
    }
  }
  for (int ax1_0_26 = 0; ax1_0_26 < 2; ++ax1_0_26) {
    *(float4*)(B_shared_dyn_local + (ax1_0_26 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_26 * 4)) >> 6) * 64) + (ax1_0_26 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 2272) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
  }
  for (int i_2_1_s_200 = 0; i_2_1_s_200 < 4; ++i_2_1_s_200) {
    if (i_2_1_s_200 < 2) {
      Y_local[(i_2_1_s_200 * 8)] = (Y_local[(i_2_1_s_200 * 8)] + (A_shared_dyn_local[(i_2_1_s_200 + 2)] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_201 = 0; i_2_1_s_201 < 4; ++i_2_1_s_201) {
    if (i_2_1_s_201 < 2) {
      Y_local[((i_2_1_s_201 * 8) + 1)] = (Y_local[((i_2_1_s_201 * 8) + 1)] + (A_shared_dyn_local[(i_2_1_s_201 + 2)] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_202 = 0; i_2_1_s_202 < 4; ++i_2_1_s_202) {
    if (i_2_1_s_202 < 2) {
      Y_local[((i_2_1_s_202 * 8) + 2)] = (Y_local[((i_2_1_s_202 * 8) + 2)] + (A_shared_dyn_local[(i_2_1_s_202 + 2)] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_203 = 0; i_2_1_s_203 < 4; ++i_2_1_s_203) {
    if (i_2_1_s_203 < 2) {
      Y_local[((i_2_1_s_203 * 8) + 3)] = (Y_local[((i_2_1_s_203 * 8) + 3)] + (A_shared_dyn_local[(i_2_1_s_203 + 2)] * B_shared_dyn_local[11]));
    }
  }
  for (int i_2_1_s_204 = 0; i_2_1_s_204 < 4; ++i_2_1_s_204) {
    if (i_2_1_s_204 < 2) {
      Y_local[((i_2_1_s_204 * 8) + 4)] = (Y_local[((i_2_1_s_204 * 8) + 4)] + (A_shared_dyn_local[(i_2_1_s_204 + 2)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_205 = 0; i_2_1_s_205 < 4; ++i_2_1_s_205) {
    if (i_2_1_s_205 < 2) {
      Y_local[((i_2_1_s_205 * 8) + 5)] = (Y_local[((i_2_1_s_205 * 8) + 5)] + (A_shared_dyn_local[(i_2_1_s_205 + 2)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_206 = 0; i_2_1_s_206 < 4; ++i_2_1_s_206) {
    if (i_2_1_s_206 < 2) {
      Y_local[((i_2_1_s_206 * 8) + 6)] = (Y_local[((i_2_1_s_206 * 8) + 6)] + (A_shared_dyn_local[(i_2_1_s_206 + 2)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_207 = 0; i_2_1_s_207 < 4; ++i_2_1_s_207) {
    if (i_2_1_s_207 < 2) {
      Y_local[((i_2_1_s_207 * 8) + 7)] = (Y_local[((i_2_1_s_207 * 8) + 7)] + (A_shared_dyn_local[(i_2_1_s_207 + 2)] * B_shared_dyn_local[15]));
    }
  }
  for (int ax1_1_s_27 = 0; ax1_1_s_27 < 4; ++ax1_1_s_27) {
    if (ax1_1_s_27 < 2) {
      A_shared_dyn_local[(ax1_1_s_27 + 2)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 7) >> 2) * 16) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_27) + 864)];
    }
  }
  for (int ax1_0_27 = 0; ax1_0_27 < 2; ++ax1_0_27) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_27 * 4) + 8)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_27 * 4)) >> 6) * 64) + (ax1_0_27 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 2320) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
  }
  for (int i_2_1_s_208 = 0; i_2_1_s_208 < 4; ++i_2_1_s_208) {
    if (i_2_1_s_208 < 2) {
      Y_local[(i_2_1_s_208 * 8)] = (Y_local[(i_2_1_s_208 * 8)] + (A_shared_dyn_local[i_2_1_s_208] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_209 = 0; i_2_1_s_209 < 4; ++i_2_1_s_209) {
    if (i_2_1_s_209 < 2) {
      Y_local[((i_2_1_s_209 * 8) + 1)] = (Y_local[((i_2_1_s_209 * 8) + 1)] + (A_shared_dyn_local[i_2_1_s_209] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_210 = 0; i_2_1_s_210 < 4; ++i_2_1_s_210) {
    if (i_2_1_s_210 < 2) {
      Y_local[((i_2_1_s_210 * 8) + 2)] = (Y_local[((i_2_1_s_210 * 8) + 2)] + (A_shared_dyn_local[i_2_1_s_210] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_211 = 0; i_2_1_s_211 < 4; ++i_2_1_s_211) {
    if (i_2_1_s_211 < 2) {
      Y_local[((i_2_1_s_211 * 8) + 3)] = (Y_local[((i_2_1_s_211 * 8) + 3)] + (A_shared_dyn_local[i_2_1_s_211] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_212 = 0; i_2_1_s_212 < 4; ++i_2_1_s_212) {
    if (i_2_1_s_212 < 2) {
      Y_local[((i_2_1_s_212 * 8) + 4)] = (Y_local[((i_2_1_s_212 * 8) + 4)] + (A_shared_dyn_local[i_2_1_s_212] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_213 = 0; i_2_1_s_213 < 4; ++i_2_1_s_213) {
    if (i_2_1_s_213 < 2) {
      Y_local[((i_2_1_s_213 * 8) + 5)] = (Y_local[((i_2_1_s_213 * 8) + 5)] + (A_shared_dyn_local[i_2_1_s_213] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_214 = 0; i_2_1_s_214 < 4; ++i_2_1_s_214) {
    if (i_2_1_s_214 < 2) {
      Y_local[((i_2_1_s_214 * 8) + 6)] = (Y_local[((i_2_1_s_214 * 8) + 6)] + (A_shared_dyn_local[i_2_1_s_214] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_215 = 0; i_2_1_s_215 < 4; ++i_2_1_s_215) {
    if (i_2_1_s_215 < 2) {
      Y_local[((i_2_1_s_215 * 8) + 7)] = (Y_local[((i_2_1_s_215 * 8) + 7)] + (A_shared_dyn_local[i_2_1_s_215] * B_shared_dyn_local[7]));
    }
  }
  for (int ax1_1_s_28 = 0; ax1_1_s_28 < 4; ++ax1_1_s_28) {
    if (ax1_1_s_28 < 2) {
      A_shared_dyn_local[ax1_1_s_28] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 7) >> 2) * 16) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_28) + 896)];
    }
  }
  for (int ax1_0_28 = 0; ax1_0_28 < 2; ++ax1_0_28) {
    *(float4*)(B_shared_dyn_local + (ax1_0_28 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_28 * 4)) >> 6) * 64) + (ax1_0_28 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 2368) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
  }
  for (int i_2_1_s_216 = 0; i_2_1_s_216 < 4; ++i_2_1_s_216) {
    if (i_2_1_s_216 < 2) {
      Y_local[(i_2_1_s_216 * 8)] = (Y_local[(i_2_1_s_216 * 8)] + (A_shared_dyn_local[(i_2_1_s_216 + 2)] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_217 = 0; i_2_1_s_217 < 4; ++i_2_1_s_217) {
    if (i_2_1_s_217 < 2) {
      Y_local[((i_2_1_s_217 * 8) + 1)] = (Y_local[((i_2_1_s_217 * 8) + 1)] + (A_shared_dyn_local[(i_2_1_s_217 + 2)] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_218 = 0; i_2_1_s_218 < 4; ++i_2_1_s_218) {
    if (i_2_1_s_218 < 2) {
      Y_local[((i_2_1_s_218 * 8) + 2)] = (Y_local[((i_2_1_s_218 * 8) + 2)] + (A_shared_dyn_local[(i_2_1_s_218 + 2)] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_219 = 0; i_2_1_s_219 < 4; ++i_2_1_s_219) {
    if (i_2_1_s_219 < 2) {
      Y_local[((i_2_1_s_219 * 8) + 3)] = (Y_local[((i_2_1_s_219 * 8) + 3)] + (A_shared_dyn_local[(i_2_1_s_219 + 2)] * B_shared_dyn_local[11]));
    }
  }
  for (int i_2_1_s_220 = 0; i_2_1_s_220 < 4; ++i_2_1_s_220) {
    if (i_2_1_s_220 < 2) {
      Y_local[((i_2_1_s_220 * 8) + 4)] = (Y_local[((i_2_1_s_220 * 8) + 4)] + (A_shared_dyn_local[(i_2_1_s_220 + 2)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_221 = 0; i_2_1_s_221 < 4; ++i_2_1_s_221) {
    if (i_2_1_s_221 < 2) {
      Y_local[((i_2_1_s_221 * 8) + 5)] = (Y_local[((i_2_1_s_221 * 8) + 5)] + (A_shared_dyn_local[(i_2_1_s_221 + 2)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_222 = 0; i_2_1_s_222 < 4; ++i_2_1_s_222) {
    if (i_2_1_s_222 < 2) {
      Y_local[((i_2_1_s_222 * 8) + 6)] = (Y_local[((i_2_1_s_222 * 8) + 6)] + (A_shared_dyn_local[(i_2_1_s_222 + 2)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_223 = 0; i_2_1_s_223 < 4; ++i_2_1_s_223) {
    if (i_2_1_s_223 < 2) {
      Y_local[((i_2_1_s_223 * 8) + 7)] = (Y_local[((i_2_1_s_223 * 8) + 7)] + (A_shared_dyn_local[(i_2_1_s_223 + 2)] * B_shared_dyn_local[15]));
    }
  }
  for (int ax1_1_s_29 = 0; ax1_1_s_29 < 4; ++ax1_1_s_29) {
    if (ax1_1_s_29 < 2) {
      A_shared_dyn_local[(ax1_1_s_29 + 2)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 7) >> 2) * 16) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_29) + 928)];
    }
  }
  for (int ax1_0_29 = 0; ax1_0_29 < 2; ++ax1_0_29) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_29 * 4) + 8)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_29 * 4)) >> 6) * 64) + (ax1_0_29 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 2416) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
  }
  for (int i_2_1_s_224 = 0; i_2_1_s_224 < 4; ++i_2_1_s_224) {
    if (i_2_1_s_224 < 2) {
      Y_local[(i_2_1_s_224 * 8)] = (Y_local[(i_2_1_s_224 * 8)] + (A_shared_dyn_local[i_2_1_s_224] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_225 = 0; i_2_1_s_225 < 4; ++i_2_1_s_225) {
    if (i_2_1_s_225 < 2) {
      Y_local[((i_2_1_s_225 * 8) + 1)] = (Y_local[((i_2_1_s_225 * 8) + 1)] + (A_shared_dyn_local[i_2_1_s_225] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_226 = 0; i_2_1_s_226 < 4; ++i_2_1_s_226) {
    if (i_2_1_s_226 < 2) {
      Y_local[((i_2_1_s_226 * 8) + 2)] = (Y_local[((i_2_1_s_226 * 8) + 2)] + (A_shared_dyn_local[i_2_1_s_226] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_227 = 0; i_2_1_s_227 < 4; ++i_2_1_s_227) {
    if (i_2_1_s_227 < 2) {
      Y_local[((i_2_1_s_227 * 8) + 3)] = (Y_local[((i_2_1_s_227 * 8) + 3)] + (A_shared_dyn_local[i_2_1_s_227] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_228 = 0; i_2_1_s_228 < 4; ++i_2_1_s_228) {
    if (i_2_1_s_228 < 2) {
      Y_local[((i_2_1_s_228 * 8) + 4)] = (Y_local[((i_2_1_s_228 * 8) + 4)] + (A_shared_dyn_local[i_2_1_s_228] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_229 = 0; i_2_1_s_229 < 4; ++i_2_1_s_229) {
    if (i_2_1_s_229 < 2) {
      Y_local[((i_2_1_s_229 * 8) + 5)] = (Y_local[((i_2_1_s_229 * 8) + 5)] + (A_shared_dyn_local[i_2_1_s_229] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_230 = 0; i_2_1_s_230 < 4; ++i_2_1_s_230) {
    if (i_2_1_s_230 < 2) {
      Y_local[((i_2_1_s_230 * 8) + 6)] = (Y_local[((i_2_1_s_230 * 8) + 6)] + (A_shared_dyn_local[i_2_1_s_230] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_231 = 0; i_2_1_s_231 < 4; ++i_2_1_s_231) {
    if (i_2_1_s_231 < 2) {
      Y_local[((i_2_1_s_231 * 8) + 7)] = (Y_local[((i_2_1_s_231 * 8) + 7)] + (A_shared_dyn_local[i_2_1_s_231] * B_shared_dyn_local[7]));
    }
  }
  for (int ax1_1_s_30 = 0; ax1_1_s_30 < 4; ++ax1_1_s_30) {
    if (ax1_1_s_30 < 2) {
      A_shared_dyn_local[ax1_1_s_30] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 7) >> 2) * 16) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_30) + 960)];
    }
  }
  for (int ax1_0_30 = 0; ax1_0_30 < 2; ++ax1_0_30) {
    *(float4*)(B_shared_dyn_local + (ax1_0_30 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_30 * 4)) >> 6) * 64) + (ax1_0_30 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 2464) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
  }
  for (int i_2_1_s_232 = 0; i_2_1_s_232 < 4; ++i_2_1_s_232) {
    if (i_2_1_s_232 < 2) {
      Y_local[(i_2_1_s_232 * 8)] = (Y_local[(i_2_1_s_232 * 8)] + (A_shared_dyn_local[(i_2_1_s_232 + 2)] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_233 = 0; i_2_1_s_233 < 4; ++i_2_1_s_233) {
    if (i_2_1_s_233 < 2) {
      Y_local[((i_2_1_s_233 * 8) + 1)] = (Y_local[((i_2_1_s_233 * 8) + 1)] + (A_shared_dyn_local[(i_2_1_s_233 + 2)] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_234 = 0; i_2_1_s_234 < 4; ++i_2_1_s_234) {
    if (i_2_1_s_234 < 2) {
      Y_local[((i_2_1_s_234 * 8) + 2)] = (Y_local[((i_2_1_s_234 * 8) + 2)] + (A_shared_dyn_local[(i_2_1_s_234 + 2)] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_235 = 0; i_2_1_s_235 < 4; ++i_2_1_s_235) {
    if (i_2_1_s_235 < 2) {
      Y_local[((i_2_1_s_235 * 8) + 3)] = (Y_local[((i_2_1_s_235 * 8) + 3)] + (A_shared_dyn_local[(i_2_1_s_235 + 2)] * B_shared_dyn_local[11]));
    }
  }
  for (int i_2_1_s_236 = 0; i_2_1_s_236 < 4; ++i_2_1_s_236) {
    if (i_2_1_s_236 < 2) {
      Y_local[((i_2_1_s_236 * 8) + 4)] = (Y_local[((i_2_1_s_236 * 8) + 4)] + (A_shared_dyn_local[(i_2_1_s_236 + 2)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_237 = 0; i_2_1_s_237 < 4; ++i_2_1_s_237) {
    if (i_2_1_s_237 < 2) {
      Y_local[((i_2_1_s_237 * 8) + 5)] = (Y_local[((i_2_1_s_237 * 8) + 5)] + (A_shared_dyn_local[(i_2_1_s_237 + 2)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_238 = 0; i_2_1_s_238 < 4; ++i_2_1_s_238) {
    if (i_2_1_s_238 < 2) {
      Y_local[((i_2_1_s_238 * 8) + 6)] = (Y_local[((i_2_1_s_238 * 8) + 6)] + (A_shared_dyn_local[(i_2_1_s_238 + 2)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_239 = 0; i_2_1_s_239 < 4; ++i_2_1_s_239) {
    if (i_2_1_s_239 < 2) {
      Y_local[((i_2_1_s_239 * 8) + 7)] = (Y_local[((i_2_1_s_239 * 8) + 7)] + (A_shared_dyn_local[(i_2_1_s_239 + 2)] * B_shared_dyn_local[15]));
    }
  }
  for (int ax1_1_s_31 = 0; ax1_1_s_31 < 4; ++ax1_1_s_31) {
    if (ax1_1_s_31 < 2) {
      A_shared_dyn_local[(ax1_1_s_31 + 2)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 7) >> 2) * 16) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + ((((int)threadIdx.x) & 1) * 2)) + ax1_1_s_31) + 992)];
    }
  }
  for (int ax1_0_31 = 0; ax1_0_31 < 2; ++ax1_0_31) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_31 * 4) + 8)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((((int)blockIdx.x) & 7) * 32) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_31 * 4)) >> 6) * 64) + (ax1_0_31 * 32)) + ((((((((int)blockIdx.x) & 7) * 4) + ((((int)threadIdx.x) >> 5) * 2)) + ((((int)threadIdx.x) & 3) >> 1)) & 7) * 4)) + 2512) - ((((int)blockIdx.x) & 1) * 16)) - (((((int)blockIdx.x) & 7) >> 1) * 64)));
  }
  for (int i_2_1_s_240 = 0; i_2_1_s_240 < 4; ++i_2_1_s_240) {
    if (i_2_1_s_240 < 2) {
      Y_local[(i_2_1_s_240 * 8)] = (Y_local[(i_2_1_s_240 * 8)] + (A_shared_dyn_local[i_2_1_s_240] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_241 = 0; i_2_1_s_241 < 4; ++i_2_1_s_241) {
    if (i_2_1_s_241 < 2) {
      Y_local[((i_2_1_s_241 * 8) + 1)] = (Y_local[((i_2_1_s_241 * 8) + 1)] + (A_shared_dyn_local[i_2_1_s_241] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_242 = 0; i_2_1_s_242 < 4; ++i_2_1_s_242) {
    if (i_2_1_s_242 < 2) {
      Y_local[((i_2_1_s_242 * 8) + 2)] = (Y_local[((i_2_1_s_242 * 8) + 2)] + (A_shared_dyn_local[i_2_1_s_242] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_243 = 0; i_2_1_s_243 < 4; ++i_2_1_s_243) {
    if (i_2_1_s_243 < 2) {
      Y_local[((i_2_1_s_243 * 8) + 3)] = (Y_local[((i_2_1_s_243 * 8) + 3)] + (A_shared_dyn_local[i_2_1_s_243] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_244 = 0; i_2_1_s_244 < 4; ++i_2_1_s_244) {
    if (i_2_1_s_244 < 2) {
      Y_local[((i_2_1_s_244 * 8) + 4)] = (Y_local[((i_2_1_s_244 * 8) + 4)] + (A_shared_dyn_local[i_2_1_s_244] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_245 = 0; i_2_1_s_245 < 4; ++i_2_1_s_245) {
    if (i_2_1_s_245 < 2) {
      Y_local[((i_2_1_s_245 * 8) + 5)] = (Y_local[((i_2_1_s_245 * 8) + 5)] + (A_shared_dyn_local[i_2_1_s_245] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_246 = 0; i_2_1_s_246 < 4; ++i_2_1_s_246) {
    if (i_2_1_s_246 < 2) {
      Y_local[((i_2_1_s_246 * 8) + 6)] = (Y_local[((i_2_1_s_246 * 8) + 6)] + (A_shared_dyn_local[i_2_1_s_246] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_247 = 0; i_2_1_s_247 < 4; ++i_2_1_s_247) {
    if (i_2_1_s_247 < 2) {
      Y_local[((i_2_1_s_247 * 8) + 7)] = (Y_local[((i_2_1_s_247 * 8) + 7)] + (A_shared_dyn_local[i_2_1_s_247] * B_shared_dyn_local[7]));
    }
  }
  for (int i_2_1_s_248 = 0; i_2_1_s_248 < 4; ++i_2_1_s_248) {
    if (i_2_1_s_248 < 2) {
      Y_local[(i_2_1_s_248 * 8)] = (Y_local[(i_2_1_s_248 * 8)] + (A_shared_dyn_local[(i_2_1_s_248 + 2)] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_249 = 0; i_2_1_s_249 < 4; ++i_2_1_s_249) {
    if (i_2_1_s_249 < 2) {
      Y_local[((i_2_1_s_249 * 8) + 1)] = (Y_local[((i_2_1_s_249 * 8) + 1)] + (A_shared_dyn_local[(i_2_1_s_249 + 2)] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_250 = 0; i_2_1_s_250 < 4; ++i_2_1_s_250) {
    if (i_2_1_s_250 < 2) {
      Y_local[((i_2_1_s_250 * 8) + 2)] = (Y_local[((i_2_1_s_250 * 8) + 2)] + (A_shared_dyn_local[(i_2_1_s_250 + 2)] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_251 = 0; i_2_1_s_251 < 4; ++i_2_1_s_251) {
    if (i_2_1_s_251 < 2) {
      Y_local[((i_2_1_s_251 * 8) + 3)] = (Y_local[((i_2_1_s_251 * 8) + 3)] + (A_shared_dyn_local[(i_2_1_s_251 + 2)] * B_shared_dyn_local[11]));
    }
  }
  for (int i_2_1_s_252 = 0; i_2_1_s_252 < 4; ++i_2_1_s_252) {
    if (i_2_1_s_252 < 2) {
      Y_local[((i_2_1_s_252 * 8) + 4)] = (Y_local[((i_2_1_s_252 * 8) + 4)] + (A_shared_dyn_local[(i_2_1_s_252 + 2)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_253 = 0; i_2_1_s_253 < 4; ++i_2_1_s_253) {
    if (i_2_1_s_253 < 2) {
      Y_local[((i_2_1_s_253 * 8) + 5)] = (Y_local[((i_2_1_s_253 * 8) + 5)] + (A_shared_dyn_local[(i_2_1_s_253 + 2)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_254 = 0; i_2_1_s_254 < 4; ++i_2_1_s_254) {
    if (i_2_1_s_254 < 2) {
      Y_local[((i_2_1_s_254 * 8) + 6)] = (Y_local[((i_2_1_s_254 * 8) + 6)] + (A_shared_dyn_local[(i_2_1_s_254 + 2)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_255 = 0; i_2_1_s_255 < 4; ++i_2_1_s_255) {
    if (i_2_1_s_255 < 2) {
      Y_local[((i_2_1_s_255 * 8) + 7)] = (Y_local[((i_2_1_s_255 * 8) + 7)] + (A_shared_dyn_local[(i_2_1_s_255 + 2)] * B_shared_dyn_local[15]));
    }
  }
  for (int ax1_0_32 = 0; ax1_0_32 < 2; ++ax1_0_32) {
    *(float4*)(Y + ((((((((((int)blockIdx.x) >> 3) * 8192) + (((((int)threadIdx.x) & 31) >> 2) * 1024)) + ((((int)threadIdx.x) & 1) * 512)) + ((((int)blockIdx.x) & 7) * 32)) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_32 * 4))) = *(float4*)(Y_local + (ax1_0_32 * 4));
  }
  for (int ax1_0_33 = 0; ax1_0_33 < 2; ++ax1_0_33) {
    *(float4*)(Y + (((((((((((int)blockIdx.x) >> 3) * 8192) + (((((int)threadIdx.x) & 31) >> 2) * 1024)) + ((((int)threadIdx.x) & 1) * 512)) + ((((int)blockIdx.x) & 7) * 32)) + ((((int)threadIdx.x) >> 5) * 16)) + (((((int)threadIdx.x) & 3) >> 1) * 8)) + (ax1_0_33 * 4)) + 256)) = *(float4*)(Y_local + ((ax1_0_33 * 4) + 8));
  }
}


