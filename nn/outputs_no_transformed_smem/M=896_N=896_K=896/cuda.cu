
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
extern "C" __global__ void __launch_bounds__(512) main_kernel0(float* __restrict__ A, float* __restrict__ B, float* __restrict__ Y) {
  extern __shared__ uchar buf_dyn_shmem[];
  float Y_local[28];
  float A_shared_dyn_local[14];
  float B_shared_dyn_local[8];
  Y_local[0] = 0.000000e+00f;
  Y_local[4] = 0.000000e+00f;
  Y_local[8] = 0.000000e+00f;
  Y_local[12] = 0.000000e+00f;
  Y_local[16] = 0.000000e+00f;
  Y_local[20] = 0.000000e+00f;
  Y_local[24] = 0.000000e+00f;
  Y_local[1] = 0.000000e+00f;
  Y_local[5] = 0.000000e+00f;
  Y_local[9] = 0.000000e+00f;
  Y_local[13] = 0.000000e+00f;
  Y_local[17] = 0.000000e+00f;
  Y_local[21] = 0.000000e+00f;
  Y_local[25] = 0.000000e+00f;
  Y_local[2] = 0.000000e+00f;
  Y_local[6] = 0.000000e+00f;
  Y_local[10] = 0.000000e+00f;
  Y_local[14] = 0.000000e+00f;
  Y_local[18] = 0.000000e+00f;
  Y_local[22] = 0.000000e+00f;
  Y_local[26] = 0.000000e+00f;
  Y_local[3] = 0.000000e+00f;
  Y_local[7] = 0.000000e+00f;
  Y_local[11] = 0.000000e+00f;
  Y_local[15] = 0.000000e+00f;
  Y_local[19] = 0.000000e+00f;
  Y_local[23] = 0.000000e+00f;
  Y_local[27] = 0.000000e+00f;
  for (int ax0_ax1_fused_2_s = 0; ax0_ax1_fused_2_s < 2; ++ax0_ax1_fused_2_s) {
    if (((int)threadIdx.x) < 448) {

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + ((((((((int)threadIdx.x) >> 2) * 80) + (((((int)threadIdx.x) & 3) >> 1) * 64)) + ((((int)threadIdx.x) & 1) * 8)) + (ax0_ax1_fused_2_s * 4)) + 20480)))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(A + (((((((int)blockIdx.x) / 7) * 100352) + ((((int)threadIdx.x) >> 2) * 896)) + ((((int)threadIdx.x) & 3) * 2)) + ax0_ax1_fused_2_s))), "n"(4)
    );
  }
    }
  }

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + (((((((int)threadIdx.x) >> 5) * 256) + (((((int)threadIdx.x) & 3) >> 1) * 128)) + (((((int)threadIdx.x) & 31) >> 2) * 16)) + ((((int)threadIdx.x) & 1) * 8))))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(B + ((((((int)threadIdx.x) >> 6) * 896) + ((((int)blockIdx.x) % 7) * 128)) + ((((int)threadIdx.x) & 63) * 2)))), "n"(8)
    );
  }
__asm__ __volatile__("cp.async.commit_group;");

  for (int ax0_ax1_fused_2_s_1 = 0; ax0_ax1_fused_2_s_1 < 2; ++ax0_ax1_fused_2_s_1) {
    if (((int)threadIdx.x) < 448) {

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + ((((((((int)threadIdx.x) >> 2) * 80) + (((((int)threadIdx.x) & 3) >> 1) * 64)) + ((((int)threadIdx.x) & 1) * 8)) + (ax0_ax1_fused_2_s_1 * 4)) + 29440)))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(A + ((((((((int)blockIdx.x) / 7) * 100352) + ((((int)threadIdx.x) >> 2) * 896)) + ((((int)threadIdx.x) & 3) * 2)) + ax0_ax1_fused_2_s_1) + 8))), "n"(4)
    );
  }
    }
  }

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + ((((((((int)threadIdx.x) >> 5) * 256) + (((((int)threadIdx.x) & 3) >> 1) * 128)) + (((((int)threadIdx.x) & 31) >> 2) * 16)) + ((((int)threadIdx.x) & 1) * 8)) + 4096)))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(B + (((((((int)threadIdx.x) >> 6) * 896) + ((((int)blockIdx.x) % 7) * 128)) + ((((int)threadIdx.x) & 63) * 2)) + 7168))), "n"(8)
    );
  }
__asm__ __volatile__("cp.async.commit_group;");

  for (int ax0_ax1_fused_2_s_2 = 0; ax0_ax1_fused_2_s_2 < 2; ++ax0_ax1_fused_2_s_2) {
    if (((int)threadIdx.x) < 448) {

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + ((((((((int)threadIdx.x) >> 2) * 80) + (((((int)threadIdx.x) & 3) >> 1) * 64)) + ((((int)threadIdx.x) & 1) * 8)) + (ax0_ax1_fused_2_s_2 * 4)) + 38400)))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(A + ((((((((int)blockIdx.x) / 7) * 100352) + ((((int)threadIdx.x) >> 2) * 896)) + ((((int)threadIdx.x) & 3) * 2)) + ax0_ax1_fused_2_s_2) + 16))), "n"(4)
    );
  }
    }
  }

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + ((((((((int)threadIdx.x) >> 5) * 256) + (((((int)threadIdx.x) & 3) >> 1) * 128)) + (((((int)threadIdx.x) & 31) >> 2) * 16)) + ((((int)threadIdx.x) & 1) * 8)) + 8192)))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(B + (((((((int)threadIdx.x) >> 6) * 896) + ((((int)blockIdx.x) % 7) * 128)) + ((((int)threadIdx.x) & 63) * 2)) + 14336))), "n"(8)
    );
  }
__asm__ __volatile__("cp.async.commit_group;");

  for (int ax0_ax1_fused_2_s_3 = 0; ax0_ax1_fused_2_s_3 < 2; ++ax0_ax1_fused_2_s_3) {
    if (((int)threadIdx.x) < 448) {

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + ((((((((int)threadIdx.x) >> 2) * 80) + (((((int)threadIdx.x) & 3) >> 1) * 64)) + ((((int)threadIdx.x) & 1) * 8)) + (ax0_ax1_fused_2_s_3 * 4)) + 47360)))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(A + ((((((((int)blockIdx.x) / 7) * 100352) + ((((int)threadIdx.x) >> 2) * 896)) + ((((int)threadIdx.x) & 3) * 2)) + ax0_ax1_fused_2_s_3) + 24))), "n"(4)
    );
  }
    }
  }

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + ((((((((int)threadIdx.x) >> 5) * 256) + (((((int)threadIdx.x) & 3) >> 1) * 128)) + (((((int)threadIdx.x) & 31) >> 2) * 16)) + ((((int)threadIdx.x) & 1) * 8)) + 12288)))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(B + (((((((int)threadIdx.x) >> 6) * 896) + ((((int)blockIdx.x) % 7) * 128)) + ((((int)threadIdx.x) & 63) * 2)) + 21504))), "n"(8)
    );
  }
__asm__ __volatile__("cp.async.commit_group;");

__asm__ __volatile__("cp.async.wait_group 3;");

  __syncthreads();
  for (int ax0_0 = 0; ax0_0 < 2; ++ax0_0) {
    for (int ax0_1_s = 0; ax0_1_s < 4; ++ax0_1_s) {
      if (((ax0_0 * 4) + ax0_1_s) < 7) {
        A_shared_dyn_local[((ax0_0 * 4) + ax0_1_s)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0 * 80)) + (ax0_1_s * 20)) + 5120)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 0) = *(float4*)(((float*)buf_dyn_shmem) + (((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)));
  for (int k_0 = 0; k_0 < 108; ++k_0) {
    __syncthreads();
    for (int ax0_ax1_fused_2_s_4 = 0; ax0_ax1_fused_2_s_4 < 2; ++ax0_ax1_fused_2_s_4) {
      if (((int)threadIdx.x) < 448) {

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + ((((((((k_0 + 4) % 5) * 8960) + ((((int)threadIdx.x) >> 2) * 80)) + (((((int)threadIdx.x) & 3) >> 1) * 64)) + ((((int)threadIdx.x) & 1) * 8)) + (ax0_ax1_fused_2_s_4 * 4)) + 20480)))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(A + (((((((((int)blockIdx.x) / 7) * 100352) + ((((int)threadIdx.x) >> 2) * 896)) + (k_0 * 8)) + ((((int)threadIdx.x) & 3) * 2)) + ax0_ax1_fused_2_s_4) + 32))), "n"(4)
    );
  }
      }
    }

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + (((((((k_0 + 4) % 5) * 4096) + ((((int)threadIdx.x) >> 5) * 256)) + (((((int)threadIdx.x) & 3) >> 1) * 128)) + (((((int)threadIdx.x) & 31) >> 2) * 16)) + ((((int)threadIdx.x) & 1) * 8))))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(B + (((((k_0 * 7168) + ((((int)threadIdx.x) >> 6) * 896)) + ((((int)blockIdx.x) % 7) * 128)) + ((((int)threadIdx.x) & 63) * 2)) + 28672))), "n"(8)
    );
  }
__asm__ __volatile__("cp.async.commit_group;");

__asm__ __volatile__("cp.async.wait_group 3;");

    __syncthreads();
    for (int ax0_0_1 = 0; ax0_0_1 < 2; ++ax0_0_1) {
      for (int ax0_1_s_1 = 0; ax0_1_s_1 < 4; ++ax0_1_s_1) {
        if (((ax0_0_1 * 4) + ax0_1_s_1) < 7) {
          A_shared_dyn_local[(((ax0_0_1 * 4) + ax0_1_s_1) + 7)] = ((float*)buf_dyn_shmem)[(((((((k_0 % 5) * 2240) + (((((int)threadIdx.x) & 63) >> 3) * 280)) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_1 * 80)) + (ax0_1_s_1 * 20)) + 5121)];
        }
      }
    }
    *(float4*)(B_shared_dyn_local + 4) = *(float4*)(((float*)buf_dyn_shmem) + (((((((k_0 % 5) * 1024) + ((((int)threadIdx.x) >> 8) * 64)) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 128));
    for (int i_2_1_s = 0; i_2_1_s < 4; ++i_2_1_s) {
      Y_local[(i_2_1_s * 4)] = (Y_local[(i_2_1_s * 4)] + (A_shared_dyn_local[i_2_1_s] * B_shared_dyn_local[0]));
    }
    for (int i_2_1_s_1 = 0; i_2_1_s_1 < 4; ++i_2_1_s_1) {
      if (i_2_1_s_1 < 3) {
        Y_local[((i_2_1_s_1 * 4) + 16)] = (Y_local[((i_2_1_s_1 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_1 + 4)] * B_shared_dyn_local[0]));
      }
    }
    for (int i_2_1_s_2 = 0; i_2_1_s_2 < 4; ++i_2_1_s_2) {
      Y_local[((i_2_1_s_2 * 4) + 1)] = (Y_local[((i_2_1_s_2 * 4) + 1)] + (A_shared_dyn_local[i_2_1_s_2] * B_shared_dyn_local[1]));
    }
    for (int i_2_1_s_3 = 0; i_2_1_s_3 < 4; ++i_2_1_s_3) {
      if (i_2_1_s_3 < 3) {
        Y_local[((i_2_1_s_3 * 4) + 17)] = (Y_local[((i_2_1_s_3 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_3 + 4)] * B_shared_dyn_local[1]));
      }
    }
    for (int i_2_1_s_4 = 0; i_2_1_s_4 < 4; ++i_2_1_s_4) {
      Y_local[((i_2_1_s_4 * 4) + 2)] = (Y_local[((i_2_1_s_4 * 4) + 2)] + (A_shared_dyn_local[i_2_1_s_4] * B_shared_dyn_local[2]));
    }
    for (int i_2_1_s_5 = 0; i_2_1_s_5 < 4; ++i_2_1_s_5) {
      if (i_2_1_s_5 < 3) {
        Y_local[((i_2_1_s_5 * 4) + 18)] = (Y_local[((i_2_1_s_5 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_5 + 4)] * B_shared_dyn_local[2]));
      }
    }
    for (int i_2_1_s_6 = 0; i_2_1_s_6 < 4; ++i_2_1_s_6) {
      Y_local[((i_2_1_s_6 * 4) + 3)] = (Y_local[((i_2_1_s_6 * 4) + 3)] + (A_shared_dyn_local[i_2_1_s_6] * B_shared_dyn_local[3]));
    }
    for (int i_2_1_s_7 = 0; i_2_1_s_7 < 4; ++i_2_1_s_7) {
      if (i_2_1_s_7 < 3) {
        Y_local[((i_2_1_s_7 * 4) + 19)] = (Y_local[((i_2_1_s_7 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_7 + 4)] * B_shared_dyn_local[3]));
      }
    }
    for (int ax0_0_2 = 0; ax0_0_2 < 2; ++ax0_0_2) {
      for (int ax0_1_s_2 = 0; ax0_1_s_2 < 4; ++ax0_1_s_2) {
        if (((ax0_0_2 * 4) + ax0_1_s_2) < 7) {
          A_shared_dyn_local[((ax0_0_2 * 4) + ax0_1_s_2)] = ((float*)buf_dyn_shmem)[(((((((k_0 % 5) * 2240) + (((((int)threadIdx.x) & 63) >> 3) * 280)) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_2 * 80)) + (ax0_1_s_2 * 20)) + 5122)];
        }
      }
    }
    *(float4*)(B_shared_dyn_local + 0) = *(float4*)(((float*)buf_dyn_shmem) + (((((((k_0 % 5) * 1024) + ((((int)threadIdx.x) >> 8) * 64)) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 256));
    for (int i_2_1_s_8 = 0; i_2_1_s_8 < 4; ++i_2_1_s_8) {
      Y_local[(i_2_1_s_8 * 4)] = (Y_local[(i_2_1_s_8 * 4)] + (A_shared_dyn_local[(i_2_1_s_8 + 7)] * B_shared_dyn_local[4]));
    }
    for (int i_2_1_s_9 = 0; i_2_1_s_9 < 4; ++i_2_1_s_9) {
      if (i_2_1_s_9 < 3) {
        Y_local[((i_2_1_s_9 * 4) + 16)] = (Y_local[((i_2_1_s_9 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_9 + 11)] * B_shared_dyn_local[4]));
      }
    }
    for (int i_2_1_s_10 = 0; i_2_1_s_10 < 4; ++i_2_1_s_10) {
      Y_local[((i_2_1_s_10 * 4) + 1)] = (Y_local[((i_2_1_s_10 * 4) + 1)] + (A_shared_dyn_local[(i_2_1_s_10 + 7)] * B_shared_dyn_local[5]));
    }
    for (int i_2_1_s_11 = 0; i_2_1_s_11 < 4; ++i_2_1_s_11) {
      if (i_2_1_s_11 < 3) {
        Y_local[((i_2_1_s_11 * 4) + 17)] = (Y_local[((i_2_1_s_11 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_11 + 11)] * B_shared_dyn_local[5]));
      }
    }
    for (int i_2_1_s_12 = 0; i_2_1_s_12 < 4; ++i_2_1_s_12) {
      Y_local[((i_2_1_s_12 * 4) + 2)] = (Y_local[((i_2_1_s_12 * 4) + 2)] + (A_shared_dyn_local[(i_2_1_s_12 + 7)] * B_shared_dyn_local[6]));
    }
    for (int i_2_1_s_13 = 0; i_2_1_s_13 < 4; ++i_2_1_s_13) {
      if (i_2_1_s_13 < 3) {
        Y_local[((i_2_1_s_13 * 4) + 18)] = (Y_local[((i_2_1_s_13 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_13 + 11)] * B_shared_dyn_local[6]));
      }
    }
    for (int i_2_1_s_14 = 0; i_2_1_s_14 < 4; ++i_2_1_s_14) {
      Y_local[((i_2_1_s_14 * 4) + 3)] = (Y_local[((i_2_1_s_14 * 4) + 3)] + (A_shared_dyn_local[(i_2_1_s_14 + 7)] * B_shared_dyn_local[7]));
    }
    for (int i_2_1_s_15 = 0; i_2_1_s_15 < 4; ++i_2_1_s_15) {
      if (i_2_1_s_15 < 3) {
        Y_local[((i_2_1_s_15 * 4) + 19)] = (Y_local[((i_2_1_s_15 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_15 + 11)] * B_shared_dyn_local[7]));
      }
    }
    for (int ax0_0_3 = 0; ax0_0_3 < 2; ++ax0_0_3) {
      for (int ax0_1_s_3 = 0; ax0_1_s_3 < 4; ++ax0_1_s_3) {
        if (((ax0_0_3 * 4) + ax0_1_s_3) < 7) {
          A_shared_dyn_local[(((ax0_0_3 * 4) + ax0_1_s_3) + 7)] = ((float*)buf_dyn_shmem)[(((((((k_0 % 5) * 2240) + (((((int)threadIdx.x) & 63) >> 3) * 280)) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_3 * 80)) + (ax0_1_s_3 * 20)) + 5123)];
        }
      }
    }
    *(float4*)(B_shared_dyn_local + 4) = *(float4*)(((float*)buf_dyn_shmem) + (((((((k_0 % 5) * 1024) + ((((int)threadIdx.x) >> 8) * 64)) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 384));
    for (int i_2_1_s_16 = 0; i_2_1_s_16 < 4; ++i_2_1_s_16) {
      Y_local[(i_2_1_s_16 * 4)] = (Y_local[(i_2_1_s_16 * 4)] + (A_shared_dyn_local[i_2_1_s_16] * B_shared_dyn_local[0]));
    }
    for (int i_2_1_s_17 = 0; i_2_1_s_17 < 4; ++i_2_1_s_17) {
      if (i_2_1_s_17 < 3) {
        Y_local[((i_2_1_s_17 * 4) + 16)] = (Y_local[((i_2_1_s_17 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_17 + 4)] * B_shared_dyn_local[0]));
      }
    }
    for (int i_2_1_s_18 = 0; i_2_1_s_18 < 4; ++i_2_1_s_18) {
      Y_local[((i_2_1_s_18 * 4) + 1)] = (Y_local[((i_2_1_s_18 * 4) + 1)] + (A_shared_dyn_local[i_2_1_s_18] * B_shared_dyn_local[1]));
    }
    for (int i_2_1_s_19 = 0; i_2_1_s_19 < 4; ++i_2_1_s_19) {
      if (i_2_1_s_19 < 3) {
        Y_local[((i_2_1_s_19 * 4) + 17)] = (Y_local[((i_2_1_s_19 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_19 + 4)] * B_shared_dyn_local[1]));
      }
    }
    for (int i_2_1_s_20 = 0; i_2_1_s_20 < 4; ++i_2_1_s_20) {
      Y_local[((i_2_1_s_20 * 4) + 2)] = (Y_local[((i_2_1_s_20 * 4) + 2)] + (A_shared_dyn_local[i_2_1_s_20] * B_shared_dyn_local[2]));
    }
    for (int i_2_1_s_21 = 0; i_2_1_s_21 < 4; ++i_2_1_s_21) {
      if (i_2_1_s_21 < 3) {
        Y_local[((i_2_1_s_21 * 4) + 18)] = (Y_local[((i_2_1_s_21 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_21 + 4)] * B_shared_dyn_local[2]));
      }
    }
    for (int i_2_1_s_22 = 0; i_2_1_s_22 < 4; ++i_2_1_s_22) {
      Y_local[((i_2_1_s_22 * 4) + 3)] = (Y_local[((i_2_1_s_22 * 4) + 3)] + (A_shared_dyn_local[i_2_1_s_22] * B_shared_dyn_local[3]));
    }
    for (int i_2_1_s_23 = 0; i_2_1_s_23 < 4; ++i_2_1_s_23) {
      if (i_2_1_s_23 < 3) {
        Y_local[((i_2_1_s_23 * 4) + 19)] = (Y_local[((i_2_1_s_23 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_23 + 4)] * B_shared_dyn_local[3]));
      }
    }
    for (int ax0_0_4 = 0; ax0_0_4 < 2; ++ax0_0_4) {
      for (int ax0_1_s_4 = 0; ax0_1_s_4 < 4; ++ax0_1_s_4) {
        if (((ax0_0_4 * 4) + ax0_1_s_4) < 7) {
          A_shared_dyn_local[((ax0_0_4 * 4) + ax0_1_s_4)] = ((float*)buf_dyn_shmem)[(((((((k_0 % 5) * 2240) + (((((int)threadIdx.x) & 63) >> 3) * 280)) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_4 * 80)) + (ax0_1_s_4 * 20)) + 5136)];
        }
      }
    }
    *(float4*)(B_shared_dyn_local + 0) = *(float4*)(((float*)buf_dyn_shmem) + (((((((k_0 % 5) * 1024) + ((((int)threadIdx.x) >> 8) * 64)) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 512));
    for (int i_2_1_s_24 = 0; i_2_1_s_24 < 4; ++i_2_1_s_24) {
      Y_local[(i_2_1_s_24 * 4)] = (Y_local[(i_2_1_s_24 * 4)] + (A_shared_dyn_local[(i_2_1_s_24 + 7)] * B_shared_dyn_local[4]));
    }
    for (int i_2_1_s_25 = 0; i_2_1_s_25 < 4; ++i_2_1_s_25) {
      if (i_2_1_s_25 < 3) {
        Y_local[((i_2_1_s_25 * 4) + 16)] = (Y_local[((i_2_1_s_25 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_25 + 11)] * B_shared_dyn_local[4]));
      }
    }
    for (int i_2_1_s_26 = 0; i_2_1_s_26 < 4; ++i_2_1_s_26) {
      Y_local[((i_2_1_s_26 * 4) + 1)] = (Y_local[((i_2_1_s_26 * 4) + 1)] + (A_shared_dyn_local[(i_2_1_s_26 + 7)] * B_shared_dyn_local[5]));
    }
    for (int i_2_1_s_27 = 0; i_2_1_s_27 < 4; ++i_2_1_s_27) {
      if (i_2_1_s_27 < 3) {
        Y_local[((i_2_1_s_27 * 4) + 17)] = (Y_local[((i_2_1_s_27 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_27 + 11)] * B_shared_dyn_local[5]));
      }
    }
    for (int i_2_1_s_28 = 0; i_2_1_s_28 < 4; ++i_2_1_s_28) {
      Y_local[((i_2_1_s_28 * 4) + 2)] = (Y_local[((i_2_1_s_28 * 4) + 2)] + (A_shared_dyn_local[(i_2_1_s_28 + 7)] * B_shared_dyn_local[6]));
    }
    for (int i_2_1_s_29 = 0; i_2_1_s_29 < 4; ++i_2_1_s_29) {
      if (i_2_1_s_29 < 3) {
        Y_local[((i_2_1_s_29 * 4) + 18)] = (Y_local[((i_2_1_s_29 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_29 + 11)] * B_shared_dyn_local[6]));
      }
    }
    for (int i_2_1_s_30 = 0; i_2_1_s_30 < 4; ++i_2_1_s_30) {
      Y_local[((i_2_1_s_30 * 4) + 3)] = (Y_local[((i_2_1_s_30 * 4) + 3)] + (A_shared_dyn_local[(i_2_1_s_30 + 7)] * B_shared_dyn_local[7]));
    }
    for (int i_2_1_s_31 = 0; i_2_1_s_31 < 4; ++i_2_1_s_31) {
      if (i_2_1_s_31 < 3) {
        Y_local[((i_2_1_s_31 * 4) + 19)] = (Y_local[((i_2_1_s_31 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_31 + 11)] * B_shared_dyn_local[7]));
      }
    }
    for (int ax0_0_5 = 0; ax0_0_5 < 2; ++ax0_0_5) {
      for (int ax0_1_s_5 = 0; ax0_1_s_5 < 4; ++ax0_1_s_5) {
        if (((ax0_0_5 * 4) + ax0_1_s_5) < 7) {
          A_shared_dyn_local[(((ax0_0_5 * 4) + ax0_1_s_5) + 7)] = ((float*)buf_dyn_shmem)[(((((((k_0 % 5) * 2240) + (((((int)threadIdx.x) & 63) >> 3) * 280)) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_5 * 80)) + (ax0_1_s_5 * 20)) + 5137)];
        }
      }
    }
    *(float4*)(B_shared_dyn_local + 4) = *(float4*)(((float*)buf_dyn_shmem) + (((((((k_0 % 5) * 1024) + ((((int)threadIdx.x) >> 8) * 64)) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 640));
    for (int i_2_1_s_32 = 0; i_2_1_s_32 < 4; ++i_2_1_s_32) {
      Y_local[(i_2_1_s_32 * 4)] = (Y_local[(i_2_1_s_32 * 4)] + (A_shared_dyn_local[i_2_1_s_32] * B_shared_dyn_local[0]));
    }
    for (int i_2_1_s_33 = 0; i_2_1_s_33 < 4; ++i_2_1_s_33) {
      if (i_2_1_s_33 < 3) {
        Y_local[((i_2_1_s_33 * 4) + 16)] = (Y_local[((i_2_1_s_33 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_33 + 4)] * B_shared_dyn_local[0]));
      }
    }
    for (int i_2_1_s_34 = 0; i_2_1_s_34 < 4; ++i_2_1_s_34) {
      Y_local[((i_2_1_s_34 * 4) + 1)] = (Y_local[((i_2_1_s_34 * 4) + 1)] + (A_shared_dyn_local[i_2_1_s_34] * B_shared_dyn_local[1]));
    }
    for (int i_2_1_s_35 = 0; i_2_1_s_35 < 4; ++i_2_1_s_35) {
      if (i_2_1_s_35 < 3) {
        Y_local[((i_2_1_s_35 * 4) + 17)] = (Y_local[((i_2_1_s_35 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_35 + 4)] * B_shared_dyn_local[1]));
      }
    }
    for (int i_2_1_s_36 = 0; i_2_1_s_36 < 4; ++i_2_1_s_36) {
      Y_local[((i_2_1_s_36 * 4) + 2)] = (Y_local[((i_2_1_s_36 * 4) + 2)] + (A_shared_dyn_local[i_2_1_s_36] * B_shared_dyn_local[2]));
    }
    for (int i_2_1_s_37 = 0; i_2_1_s_37 < 4; ++i_2_1_s_37) {
      if (i_2_1_s_37 < 3) {
        Y_local[((i_2_1_s_37 * 4) + 18)] = (Y_local[((i_2_1_s_37 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_37 + 4)] * B_shared_dyn_local[2]));
      }
    }
    for (int i_2_1_s_38 = 0; i_2_1_s_38 < 4; ++i_2_1_s_38) {
      Y_local[((i_2_1_s_38 * 4) + 3)] = (Y_local[((i_2_1_s_38 * 4) + 3)] + (A_shared_dyn_local[i_2_1_s_38] * B_shared_dyn_local[3]));
    }
    for (int i_2_1_s_39 = 0; i_2_1_s_39 < 4; ++i_2_1_s_39) {
      if (i_2_1_s_39 < 3) {
        Y_local[((i_2_1_s_39 * 4) + 19)] = (Y_local[((i_2_1_s_39 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_39 + 4)] * B_shared_dyn_local[3]));
      }
    }
    for (int ax0_0_6 = 0; ax0_0_6 < 2; ++ax0_0_6) {
      for (int ax0_1_s_6 = 0; ax0_1_s_6 < 4; ++ax0_1_s_6) {
        if (((ax0_0_6 * 4) + ax0_1_s_6) < 7) {
          A_shared_dyn_local[((ax0_0_6 * 4) + ax0_1_s_6)] = ((float*)buf_dyn_shmem)[(((((((k_0 % 5) * 2240) + (((((int)threadIdx.x) & 63) >> 3) * 280)) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_6 * 80)) + (ax0_1_s_6 * 20)) + 5138)];
        }
      }
    }
    *(float4*)(B_shared_dyn_local + 0) = *(float4*)(((float*)buf_dyn_shmem) + (((((((k_0 % 5) * 1024) + ((((int)threadIdx.x) >> 8) * 64)) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 768));
    for (int i_2_1_s_40 = 0; i_2_1_s_40 < 4; ++i_2_1_s_40) {
      Y_local[(i_2_1_s_40 * 4)] = (Y_local[(i_2_1_s_40 * 4)] + (A_shared_dyn_local[(i_2_1_s_40 + 7)] * B_shared_dyn_local[4]));
    }
    for (int i_2_1_s_41 = 0; i_2_1_s_41 < 4; ++i_2_1_s_41) {
      if (i_2_1_s_41 < 3) {
        Y_local[((i_2_1_s_41 * 4) + 16)] = (Y_local[((i_2_1_s_41 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_41 + 11)] * B_shared_dyn_local[4]));
      }
    }
    for (int i_2_1_s_42 = 0; i_2_1_s_42 < 4; ++i_2_1_s_42) {
      Y_local[((i_2_1_s_42 * 4) + 1)] = (Y_local[((i_2_1_s_42 * 4) + 1)] + (A_shared_dyn_local[(i_2_1_s_42 + 7)] * B_shared_dyn_local[5]));
    }
    for (int i_2_1_s_43 = 0; i_2_1_s_43 < 4; ++i_2_1_s_43) {
      if (i_2_1_s_43 < 3) {
        Y_local[((i_2_1_s_43 * 4) + 17)] = (Y_local[((i_2_1_s_43 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_43 + 11)] * B_shared_dyn_local[5]));
      }
    }
    for (int i_2_1_s_44 = 0; i_2_1_s_44 < 4; ++i_2_1_s_44) {
      Y_local[((i_2_1_s_44 * 4) + 2)] = (Y_local[((i_2_1_s_44 * 4) + 2)] + (A_shared_dyn_local[(i_2_1_s_44 + 7)] * B_shared_dyn_local[6]));
    }
    for (int i_2_1_s_45 = 0; i_2_1_s_45 < 4; ++i_2_1_s_45) {
      if (i_2_1_s_45 < 3) {
        Y_local[((i_2_1_s_45 * 4) + 18)] = (Y_local[((i_2_1_s_45 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_45 + 11)] * B_shared_dyn_local[6]));
      }
    }
    for (int i_2_1_s_46 = 0; i_2_1_s_46 < 4; ++i_2_1_s_46) {
      Y_local[((i_2_1_s_46 * 4) + 3)] = (Y_local[((i_2_1_s_46 * 4) + 3)] + (A_shared_dyn_local[(i_2_1_s_46 + 7)] * B_shared_dyn_local[7]));
    }
    for (int i_2_1_s_47 = 0; i_2_1_s_47 < 4; ++i_2_1_s_47) {
      if (i_2_1_s_47 < 3) {
        Y_local[((i_2_1_s_47 * 4) + 19)] = (Y_local[((i_2_1_s_47 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_47 + 11)] * B_shared_dyn_local[7]));
      }
    }
    for (int ax0_0_7 = 0; ax0_0_7 < 2; ++ax0_0_7) {
      for (int ax0_1_s_7 = 0; ax0_1_s_7 < 4; ++ax0_1_s_7) {
        if (((ax0_0_7 * 4) + ax0_1_s_7) < 7) {
          A_shared_dyn_local[(((ax0_0_7 * 4) + ax0_1_s_7) + 7)] = ((float*)buf_dyn_shmem)[(((((((k_0 % 5) * 2240) + (((((int)threadIdx.x) & 63) >> 3) * 280)) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_7 * 80)) + (ax0_1_s_7 * 20)) + 5139)];
        }
      }
    }
    *(float4*)(B_shared_dyn_local + 4) = *(float4*)(((float*)buf_dyn_shmem) + (((((((k_0 % 5) * 1024) + ((((int)threadIdx.x) >> 8) * 64)) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 896));
    for (int i_2_1_s_48 = 0; i_2_1_s_48 < 4; ++i_2_1_s_48) {
      Y_local[(i_2_1_s_48 * 4)] = (Y_local[(i_2_1_s_48 * 4)] + (A_shared_dyn_local[i_2_1_s_48] * B_shared_dyn_local[0]));
    }
    for (int i_2_1_s_49 = 0; i_2_1_s_49 < 4; ++i_2_1_s_49) {
      if (i_2_1_s_49 < 3) {
        Y_local[((i_2_1_s_49 * 4) + 16)] = (Y_local[((i_2_1_s_49 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_49 + 4)] * B_shared_dyn_local[0]));
      }
    }
    for (int i_2_1_s_50 = 0; i_2_1_s_50 < 4; ++i_2_1_s_50) {
      Y_local[((i_2_1_s_50 * 4) + 1)] = (Y_local[((i_2_1_s_50 * 4) + 1)] + (A_shared_dyn_local[i_2_1_s_50] * B_shared_dyn_local[1]));
    }
    for (int i_2_1_s_51 = 0; i_2_1_s_51 < 4; ++i_2_1_s_51) {
      if (i_2_1_s_51 < 3) {
        Y_local[((i_2_1_s_51 * 4) + 17)] = (Y_local[((i_2_1_s_51 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_51 + 4)] * B_shared_dyn_local[1]));
      }
    }
    for (int i_2_1_s_52 = 0; i_2_1_s_52 < 4; ++i_2_1_s_52) {
      Y_local[((i_2_1_s_52 * 4) + 2)] = (Y_local[((i_2_1_s_52 * 4) + 2)] + (A_shared_dyn_local[i_2_1_s_52] * B_shared_dyn_local[2]));
    }
    for (int i_2_1_s_53 = 0; i_2_1_s_53 < 4; ++i_2_1_s_53) {
      if (i_2_1_s_53 < 3) {
        Y_local[((i_2_1_s_53 * 4) + 18)] = (Y_local[((i_2_1_s_53 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_53 + 4)] * B_shared_dyn_local[2]));
      }
    }
    for (int i_2_1_s_54 = 0; i_2_1_s_54 < 4; ++i_2_1_s_54) {
      Y_local[((i_2_1_s_54 * 4) + 3)] = (Y_local[((i_2_1_s_54 * 4) + 3)] + (A_shared_dyn_local[i_2_1_s_54] * B_shared_dyn_local[3]));
    }
    for (int i_2_1_s_55 = 0; i_2_1_s_55 < 4; ++i_2_1_s_55) {
      if (i_2_1_s_55 < 3) {
        Y_local[((i_2_1_s_55 * 4) + 19)] = (Y_local[((i_2_1_s_55 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_55 + 4)] * B_shared_dyn_local[3]));
      }
    }
    for (int ax0_0_8 = 0; ax0_0_8 < 2; ++ax0_0_8) {
      for (int ax0_1_s_8 = 0; ax0_1_s_8 < 4; ++ax0_1_s_8) {
        if (((ax0_0_8 * 4) + ax0_1_s_8) < 7) {
          A_shared_dyn_local[((ax0_0_8 * 4) + ax0_1_s_8)] = ((float*)buf_dyn_shmem)[((((((((k_0 + 1) % 5) * 2240) + (((((int)threadIdx.x) & 63) >> 3) * 280)) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_8 * 80)) + (ax0_1_s_8 * 20)) + 5120)];
        }
      }
    }
    *(float4*)(B_shared_dyn_local + 0) = *(float4*)(((float*)buf_dyn_shmem) + (((((((k_0 + 1) % 5) * 1024) + ((((int)threadIdx.x) >> 8) * 64)) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)));
    for (int i_2_1_s_56 = 0; i_2_1_s_56 < 4; ++i_2_1_s_56) {
      Y_local[(i_2_1_s_56 * 4)] = (Y_local[(i_2_1_s_56 * 4)] + (A_shared_dyn_local[(i_2_1_s_56 + 7)] * B_shared_dyn_local[4]));
    }
    for (int i_2_1_s_57 = 0; i_2_1_s_57 < 4; ++i_2_1_s_57) {
      if (i_2_1_s_57 < 3) {
        Y_local[((i_2_1_s_57 * 4) + 16)] = (Y_local[((i_2_1_s_57 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_57 + 11)] * B_shared_dyn_local[4]));
      }
    }
    for (int i_2_1_s_58 = 0; i_2_1_s_58 < 4; ++i_2_1_s_58) {
      Y_local[((i_2_1_s_58 * 4) + 1)] = (Y_local[((i_2_1_s_58 * 4) + 1)] + (A_shared_dyn_local[(i_2_1_s_58 + 7)] * B_shared_dyn_local[5]));
    }
    for (int i_2_1_s_59 = 0; i_2_1_s_59 < 4; ++i_2_1_s_59) {
      if (i_2_1_s_59 < 3) {
        Y_local[((i_2_1_s_59 * 4) + 17)] = (Y_local[((i_2_1_s_59 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_59 + 11)] * B_shared_dyn_local[5]));
      }
    }
    for (int i_2_1_s_60 = 0; i_2_1_s_60 < 4; ++i_2_1_s_60) {
      Y_local[((i_2_1_s_60 * 4) + 2)] = (Y_local[((i_2_1_s_60 * 4) + 2)] + (A_shared_dyn_local[(i_2_1_s_60 + 7)] * B_shared_dyn_local[6]));
    }
    for (int i_2_1_s_61 = 0; i_2_1_s_61 < 4; ++i_2_1_s_61) {
      if (i_2_1_s_61 < 3) {
        Y_local[((i_2_1_s_61 * 4) + 18)] = (Y_local[((i_2_1_s_61 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_61 + 11)] * B_shared_dyn_local[6]));
      }
    }
    for (int i_2_1_s_62 = 0; i_2_1_s_62 < 4; ++i_2_1_s_62) {
      Y_local[((i_2_1_s_62 * 4) + 3)] = (Y_local[((i_2_1_s_62 * 4) + 3)] + (A_shared_dyn_local[(i_2_1_s_62 + 7)] * B_shared_dyn_local[7]));
    }
    for (int i_2_1_s_63 = 0; i_2_1_s_63 < 4; ++i_2_1_s_63) {
      if (i_2_1_s_63 < 3) {
        Y_local[((i_2_1_s_63 * 4) + 19)] = (Y_local[((i_2_1_s_63 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_63 + 11)] * B_shared_dyn_local[7]));
      }
    }
  }
__asm__ __volatile__("cp.async.wait_group 2;");

  __syncthreads();
  for (int ax0_0_9 = 0; ax0_0_9 < 2; ++ax0_0_9) {
    for (int ax0_1_s_9 = 0; ax0_1_s_9 < 4; ++ax0_1_s_9) {
      if (((ax0_0_9 * 4) + ax0_1_s_9) < 7) {
        A_shared_dyn_local[(((ax0_0_9 * 4) + ax0_1_s_9) + 7)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_9 * 80)) + (ax0_1_s_9 * 20)) + 11841)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 4) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 3200));
  for (int i_2_1_s_64 = 0; i_2_1_s_64 < 4; ++i_2_1_s_64) {
    Y_local[(i_2_1_s_64 * 4)] = (Y_local[(i_2_1_s_64 * 4)] + (A_shared_dyn_local[i_2_1_s_64] * B_shared_dyn_local[0]));
  }
  for (int i_2_1_s_65 = 0; i_2_1_s_65 < 4; ++i_2_1_s_65) {
    if (i_2_1_s_65 < 3) {
      Y_local[((i_2_1_s_65 * 4) + 16)] = (Y_local[((i_2_1_s_65 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_65 + 4)] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_66 = 0; i_2_1_s_66 < 4; ++i_2_1_s_66) {
    Y_local[((i_2_1_s_66 * 4) + 1)] = (Y_local[((i_2_1_s_66 * 4) + 1)] + (A_shared_dyn_local[i_2_1_s_66] * B_shared_dyn_local[1]));
  }
  for (int i_2_1_s_67 = 0; i_2_1_s_67 < 4; ++i_2_1_s_67) {
    if (i_2_1_s_67 < 3) {
      Y_local[((i_2_1_s_67 * 4) + 17)] = (Y_local[((i_2_1_s_67 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_67 + 4)] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_68 = 0; i_2_1_s_68 < 4; ++i_2_1_s_68) {
    Y_local[((i_2_1_s_68 * 4) + 2)] = (Y_local[((i_2_1_s_68 * 4) + 2)] + (A_shared_dyn_local[i_2_1_s_68] * B_shared_dyn_local[2]));
  }
  for (int i_2_1_s_69 = 0; i_2_1_s_69 < 4; ++i_2_1_s_69) {
    if (i_2_1_s_69 < 3) {
      Y_local[((i_2_1_s_69 * 4) + 18)] = (Y_local[((i_2_1_s_69 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_69 + 4)] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_70 = 0; i_2_1_s_70 < 4; ++i_2_1_s_70) {
    Y_local[((i_2_1_s_70 * 4) + 3)] = (Y_local[((i_2_1_s_70 * 4) + 3)] + (A_shared_dyn_local[i_2_1_s_70] * B_shared_dyn_local[3]));
  }
  for (int i_2_1_s_71 = 0; i_2_1_s_71 < 4; ++i_2_1_s_71) {
    if (i_2_1_s_71 < 3) {
      Y_local[((i_2_1_s_71 * 4) + 19)] = (Y_local[((i_2_1_s_71 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_71 + 4)] * B_shared_dyn_local[3]));
    }
  }
  for (int ax0_0_10 = 0; ax0_0_10 < 2; ++ax0_0_10) {
    for (int ax0_1_s_10 = 0; ax0_1_s_10 < 4; ++ax0_1_s_10) {
      if (((ax0_0_10 * 4) + ax0_1_s_10) < 7) {
        A_shared_dyn_local[((ax0_0_10 * 4) + ax0_1_s_10)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_10 * 80)) + (ax0_1_s_10 * 20)) + 11842)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 0) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 3328));
  for (int i_2_1_s_72 = 0; i_2_1_s_72 < 4; ++i_2_1_s_72) {
    Y_local[(i_2_1_s_72 * 4)] = (Y_local[(i_2_1_s_72 * 4)] + (A_shared_dyn_local[(i_2_1_s_72 + 7)] * B_shared_dyn_local[4]));
  }
  for (int i_2_1_s_73 = 0; i_2_1_s_73 < 4; ++i_2_1_s_73) {
    if (i_2_1_s_73 < 3) {
      Y_local[((i_2_1_s_73 * 4) + 16)] = (Y_local[((i_2_1_s_73 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_73 + 11)] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_74 = 0; i_2_1_s_74 < 4; ++i_2_1_s_74) {
    Y_local[((i_2_1_s_74 * 4) + 1)] = (Y_local[((i_2_1_s_74 * 4) + 1)] + (A_shared_dyn_local[(i_2_1_s_74 + 7)] * B_shared_dyn_local[5]));
  }
  for (int i_2_1_s_75 = 0; i_2_1_s_75 < 4; ++i_2_1_s_75) {
    if (i_2_1_s_75 < 3) {
      Y_local[((i_2_1_s_75 * 4) + 17)] = (Y_local[((i_2_1_s_75 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_75 + 11)] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_76 = 0; i_2_1_s_76 < 4; ++i_2_1_s_76) {
    Y_local[((i_2_1_s_76 * 4) + 2)] = (Y_local[((i_2_1_s_76 * 4) + 2)] + (A_shared_dyn_local[(i_2_1_s_76 + 7)] * B_shared_dyn_local[6]));
  }
  for (int i_2_1_s_77 = 0; i_2_1_s_77 < 4; ++i_2_1_s_77) {
    if (i_2_1_s_77 < 3) {
      Y_local[((i_2_1_s_77 * 4) + 18)] = (Y_local[((i_2_1_s_77 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_77 + 11)] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_78 = 0; i_2_1_s_78 < 4; ++i_2_1_s_78) {
    Y_local[((i_2_1_s_78 * 4) + 3)] = (Y_local[((i_2_1_s_78 * 4) + 3)] + (A_shared_dyn_local[(i_2_1_s_78 + 7)] * B_shared_dyn_local[7]));
  }
  for (int i_2_1_s_79 = 0; i_2_1_s_79 < 4; ++i_2_1_s_79) {
    if (i_2_1_s_79 < 3) {
      Y_local[((i_2_1_s_79 * 4) + 19)] = (Y_local[((i_2_1_s_79 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_79 + 11)] * B_shared_dyn_local[7]));
    }
  }
  for (int ax0_0_11 = 0; ax0_0_11 < 2; ++ax0_0_11) {
    for (int ax0_1_s_11 = 0; ax0_1_s_11 < 4; ++ax0_1_s_11) {
      if (((ax0_0_11 * 4) + ax0_1_s_11) < 7) {
        A_shared_dyn_local[(((ax0_0_11 * 4) + ax0_1_s_11) + 7)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_11 * 80)) + (ax0_1_s_11 * 20)) + 11843)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 4) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 3456));
  for (int i_2_1_s_80 = 0; i_2_1_s_80 < 4; ++i_2_1_s_80) {
    Y_local[(i_2_1_s_80 * 4)] = (Y_local[(i_2_1_s_80 * 4)] + (A_shared_dyn_local[i_2_1_s_80] * B_shared_dyn_local[0]));
  }
  for (int i_2_1_s_81 = 0; i_2_1_s_81 < 4; ++i_2_1_s_81) {
    if (i_2_1_s_81 < 3) {
      Y_local[((i_2_1_s_81 * 4) + 16)] = (Y_local[((i_2_1_s_81 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_81 + 4)] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_82 = 0; i_2_1_s_82 < 4; ++i_2_1_s_82) {
    Y_local[((i_2_1_s_82 * 4) + 1)] = (Y_local[((i_2_1_s_82 * 4) + 1)] + (A_shared_dyn_local[i_2_1_s_82] * B_shared_dyn_local[1]));
  }
  for (int i_2_1_s_83 = 0; i_2_1_s_83 < 4; ++i_2_1_s_83) {
    if (i_2_1_s_83 < 3) {
      Y_local[((i_2_1_s_83 * 4) + 17)] = (Y_local[((i_2_1_s_83 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_83 + 4)] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_84 = 0; i_2_1_s_84 < 4; ++i_2_1_s_84) {
    Y_local[((i_2_1_s_84 * 4) + 2)] = (Y_local[((i_2_1_s_84 * 4) + 2)] + (A_shared_dyn_local[i_2_1_s_84] * B_shared_dyn_local[2]));
  }
  for (int i_2_1_s_85 = 0; i_2_1_s_85 < 4; ++i_2_1_s_85) {
    if (i_2_1_s_85 < 3) {
      Y_local[((i_2_1_s_85 * 4) + 18)] = (Y_local[((i_2_1_s_85 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_85 + 4)] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_86 = 0; i_2_1_s_86 < 4; ++i_2_1_s_86) {
    Y_local[((i_2_1_s_86 * 4) + 3)] = (Y_local[((i_2_1_s_86 * 4) + 3)] + (A_shared_dyn_local[i_2_1_s_86] * B_shared_dyn_local[3]));
  }
  for (int i_2_1_s_87 = 0; i_2_1_s_87 < 4; ++i_2_1_s_87) {
    if (i_2_1_s_87 < 3) {
      Y_local[((i_2_1_s_87 * 4) + 19)] = (Y_local[((i_2_1_s_87 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_87 + 4)] * B_shared_dyn_local[3]));
    }
  }
  for (int ax0_0_12 = 0; ax0_0_12 < 2; ++ax0_0_12) {
    for (int ax0_1_s_12 = 0; ax0_1_s_12 < 4; ++ax0_1_s_12) {
      if (((ax0_0_12 * 4) + ax0_1_s_12) < 7) {
        A_shared_dyn_local[((ax0_0_12 * 4) + ax0_1_s_12)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_12 * 80)) + (ax0_1_s_12 * 20)) + 11856)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 0) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 3584));
  for (int i_2_1_s_88 = 0; i_2_1_s_88 < 4; ++i_2_1_s_88) {
    Y_local[(i_2_1_s_88 * 4)] = (Y_local[(i_2_1_s_88 * 4)] + (A_shared_dyn_local[(i_2_1_s_88 + 7)] * B_shared_dyn_local[4]));
  }
  for (int i_2_1_s_89 = 0; i_2_1_s_89 < 4; ++i_2_1_s_89) {
    if (i_2_1_s_89 < 3) {
      Y_local[((i_2_1_s_89 * 4) + 16)] = (Y_local[((i_2_1_s_89 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_89 + 11)] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_90 = 0; i_2_1_s_90 < 4; ++i_2_1_s_90) {
    Y_local[((i_2_1_s_90 * 4) + 1)] = (Y_local[((i_2_1_s_90 * 4) + 1)] + (A_shared_dyn_local[(i_2_1_s_90 + 7)] * B_shared_dyn_local[5]));
  }
  for (int i_2_1_s_91 = 0; i_2_1_s_91 < 4; ++i_2_1_s_91) {
    if (i_2_1_s_91 < 3) {
      Y_local[((i_2_1_s_91 * 4) + 17)] = (Y_local[((i_2_1_s_91 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_91 + 11)] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_92 = 0; i_2_1_s_92 < 4; ++i_2_1_s_92) {
    Y_local[((i_2_1_s_92 * 4) + 2)] = (Y_local[((i_2_1_s_92 * 4) + 2)] + (A_shared_dyn_local[(i_2_1_s_92 + 7)] * B_shared_dyn_local[6]));
  }
  for (int i_2_1_s_93 = 0; i_2_1_s_93 < 4; ++i_2_1_s_93) {
    if (i_2_1_s_93 < 3) {
      Y_local[((i_2_1_s_93 * 4) + 18)] = (Y_local[((i_2_1_s_93 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_93 + 11)] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_94 = 0; i_2_1_s_94 < 4; ++i_2_1_s_94) {
    Y_local[((i_2_1_s_94 * 4) + 3)] = (Y_local[((i_2_1_s_94 * 4) + 3)] + (A_shared_dyn_local[(i_2_1_s_94 + 7)] * B_shared_dyn_local[7]));
  }
  for (int i_2_1_s_95 = 0; i_2_1_s_95 < 4; ++i_2_1_s_95) {
    if (i_2_1_s_95 < 3) {
      Y_local[((i_2_1_s_95 * 4) + 19)] = (Y_local[((i_2_1_s_95 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_95 + 11)] * B_shared_dyn_local[7]));
    }
  }
  for (int ax0_0_13 = 0; ax0_0_13 < 2; ++ax0_0_13) {
    for (int ax0_1_s_13 = 0; ax0_1_s_13 < 4; ++ax0_1_s_13) {
      if (((ax0_0_13 * 4) + ax0_1_s_13) < 7) {
        A_shared_dyn_local[(((ax0_0_13 * 4) + ax0_1_s_13) + 7)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_13 * 80)) + (ax0_1_s_13 * 20)) + 11857)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 4) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 3712));
  for (int i_2_1_s_96 = 0; i_2_1_s_96 < 4; ++i_2_1_s_96) {
    Y_local[(i_2_1_s_96 * 4)] = (Y_local[(i_2_1_s_96 * 4)] + (A_shared_dyn_local[i_2_1_s_96] * B_shared_dyn_local[0]));
  }
  for (int i_2_1_s_97 = 0; i_2_1_s_97 < 4; ++i_2_1_s_97) {
    if (i_2_1_s_97 < 3) {
      Y_local[((i_2_1_s_97 * 4) + 16)] = (Y_local[((i_2_1_s_97 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_97 + 4)] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_98 = 0; i_2_1_s_98 < 4; ++i_2_1_s_98) {
    Y_local[((i_2_1_s_98 * 4) + 1)] = (Y_local[((i_2_1_s_98 * 4) + 1)] + (A_shared_dyn_local[i_2_1_s_98] * B_shared_dyn_local[1]));
  }
  for (int i_2_1_s_99 = 0; i_2_1_s_99 < 4; ++i_2_1_s_99) {
    if (i_2_1_s_99 < 3) {
      Y_local[((i_2_1_s_99 * 4) + 17)] = (Y_local[((i_2_1_s_99 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_99 + 4)] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_100 = 0; i_2_1_s_100 < 4; ++i_2_1_s_100) {
    Y_local[((i_2_1_s_100 * 4) + 2)] = (Y_local[((i_2_1_s_100 * 4) + 2)] + (A_shared_dyn_local[i_2_1_s_100] * B_shared_dyn_local[2]));
  }
  for (int i_2_1_s_101 = 0; i_2_1_s_101 < 4; ++i_2_1_s_101) {
    if (i_2_1_s_101 < 3) {
      Y_local[((i_2_1_s_101 * 4) + 18)] = (Y_local[((i_2_1_s_101 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_101 + 4)] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_102 = 0; i_2_1_s_102 < 4; ++i_2_1_s_102) {
    Y_local[((i_2_1_s_102 * 4) + 3)] = (Y_local[((i_2_1_s_102 * 4) + 3)] + (A_shared_dyn_local[i_2_1_s_102] * B_shared_dyn_local[3]));
  }
  for (int i_2_1_s_103 = 0; i_2_1_s_103 < 4; ++i_2_1_s_103) {
    if (i_2_1_s_103 < 3) {
      Y_local[((i_2_1_s_103 * 4) + 19)] = (Y_local[((i_2_1_s_103 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_103 + 4)] * B_shared_dyn_local[3]));
    }
  }
  for (int ax0_0_14 = 0; ax0_0_14 < 2; ++ax0_0_14) {
    for (int ax0_1_s_14 = 0; ax0_1_s_14 < 4; ++ax0_1_s_14) {
      if (((ax0_0_14 * 4) + ax0_1_s_14) < 7) {
        A_shared_dyn_local[((ax0_0_14 * 4) + ax0_1_s_14)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_14 * 80)) + (ax0_1_s_14 * 20)) + 11858)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 0) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 3840));
  for (int i_2_1_s_104 = 0; i_2_1_s_104 < 4; ++i_2_1_s_104) {
    Y_local[(i_2_1_s_104 * 4)] = (Y_local[(i_2_1_s_104 * 4)] + (A_shared_dyn_local[(i_2_1_s_104 + 7)] * B_shared_dyn_local[4]));
  }
  for (int i_2_1_s_105 = 0; i_2_1_s_105 < 4; ++i_2_1_s_105) {
    if (i_2_1_s_105 < 3) {
      Y_local[((i_2_1_s_105 * 4) + 16)] = (Y_local[((i_2_1_s_105 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_105 + 11)] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_106 = 0; i_2_1_s_106 < 4; ++i_2_1_s_106) {
    Y_local[((i_2_1_s_106 * 4) + 1)] = (Y_local[((i_2_1_s_106 * 4) + 1)] + (A_shared_dyn_local[(i_2_1_s_106 + 7)] * B_shared_dyn_local[5]));
  }
  for (int i_2_1_s_107 = 0; i_2_1_s_107 < 4; ++i_2_1_s_107) {
    if (i_2_1_s_107 < 3) {
      Y_local[((i_2_1_s_107 * 4) + 17)] = (Y_local[((i_2_1_s_107 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_107 + 11)] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_108 = 0; i_2_1_s_108 < 4; ++i_2_1_s_108) {
    Y_local[((i_2_1_s_108 * 4) + 2)] = (Y_local[((i_2_1_s_108 * 4) + 2)] + (A_shared_dyn_local[(i_2_1_s_108 + 7)] * B_shared_dyn_local[6]));
  }
  for (int i_2_1_s_109 = 0; i_2_1_s_109 < 4; ++i_2_1_s_109) {
    if (i_2_1_s_109 < 3) {
      Y_local[((i_2_1_s_109 * 4) + 18)] = (Y_local[((i_2_1_s_109 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_109 + 11)] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_110 = 0; i_2_1_s_110 < 4; ++i_2_1_s_110) {
    Y_local[((i_2_1_s_110 * 4) + 3)] = (Y_local[((i_2_1_s_110 * 4) + 3)] + (A_shared_dyn_local[(i_2_1_s_110 + 7)] * B_shared_dyn_local[7]));
  }
  for (int i_2_1_s_111 = 0; i_2_1_s_111 < 4; ++i_2_1_s_111) {
    if (i_2_1_s_111 < 3) {
      Y_local[((i_2_1_s_111 * 4) + 19)] = (Y_local[((i_2_1_s_111 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_111 + 11)] * B_shared_dyn_local[7]));
    }
  }
  for (int ax0_0_15 = 0; ax0_0_15 < 2; ++ax0_0_15) {
    for (int ax0_1_s_15 = 0; ax0_1_s_15 < 4; ++ax0_1_s_15) {
      if (((ax0_0_15 * 4) + ax0_1_s_15) < 7) {
        A_shared_dyn_local[(((ax0_0_15 * 4) + ax0_1_s_15) + 7)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_15 * 80)) + (ax0_1_s_15 * 20)) + 11859)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 4) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 3968));
  for (int i_2_1_s_112 = 0; i_2_1_s_112 < 4; ++i_2_1_s_112) {
    Y_local[(i_2_1_s_112 * 4)] = (Y_local[(i_2_1_s_112 * 4)] + (A_shared_dyn_local[i_2_1_s_112] * B_shared_dyn_local[0]));
  }
  for (int i_2_1_s_113 = 0; i_2_1_s_113 < 4; ++i_2_1_s_113) {
    if (i_2_1_s_113 < 3) {
      Y_local[((i_2_1_s_113 * 4) + 16)] = (Y_local[((i_2_1_s_113 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_113 + 4)] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_114 = 0; i_2_1_s_114 < 4; ++i_2_1_s_114) {
    Y_local[((i_2_1_s_114 * 4) + 1)] = (Y_local[((i_2_1_s_114 * 4) + 1)] + (A_shared_dyn_local[i_2_1_s_114] * B_shared_dyn_local[1]));
  }
  for (int i_2_1_s_115 = 0; i_2_1_s_115 < 4; ++i_2_1_s_115) {
    if (i_2_1_s_115 < 3) {
      Y_local[((i_2_1_s_115 * 4) + 17)] = (Y_local[((i_2_1_s_115 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_115 + 4)] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_116 = 0; i_2_1_s_116 < 4; ++i_2_1_s_116) {
    Y_local[((i_2_1_s_116 * 4) + 2)] = (Y_local[((i_2_1_s_116 * 4) + 2)] + (A_shared_dyn_local[i_2_1_s_116] * B_shared_dyn_local[2]));
  }
  for (int i_2_1_s_117 = 0; i_2_1_s_117 < 4; ++i_2_1_s_117) {
    if (i_2_1_s_117 < 3) {
      Y_local[((i_2_1_s_117 * 4) + 18)] = (Y_local[((i_2_1_s_117 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_117 + 4)] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_118 = 0; i_2_1_s_118 < 4; ++i_2_1_s_118) {
    Y_local[((i_2_1_s_118 * 4) + 3)] = (Y_local[((i_2_1_s_118 * 4) + 3)] + (A_shared_dyn_local[i_2_1_s_118] * B_shared_dyn_local[3]));
  }
  for (int i_2_1_s_119 = 0; i_2_1_s_119 < 4; ++i_2_1_s_119) {
    if (i_2_1_s_119 < 3) {
      Y_local[((i_2_1_s_119 * 4) + 19)] = (Y_local[((i_2_1_s_119 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_119 + 4)] * B_shared_dyn_local[3]));
    }
  }
  for (int ax0_0_16 = 0; ax0_0_16 < 2; ++ax0_0_16) {
    for (int ax0_1_s_16 = 0; ax0_1_s_16 < 4; ++ax0_1_s_16) {
      if (((ax0_0_16 * 4) + ax0_1_s_16) < 7) {
        A_shared_dyn_local[((ax0_0_16 * 4) + ax0_1_s_16)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_16 * 80)) + (ax0_1_s_16 * 20)) + 14080)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 0) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 4096));
  for (int i_2_1_s_120 = 0; i_2_1_s_120 < 4; ++i_2_1_s_120) {
    Y_local[(i_2_1_s_120 * 4)] = (Y_local[(i_2_1_s_120 * 4)] + (A_shared_dyn_local[(i_2_1_s_120 + 7)] * B_shared_dyn_local[4]));
  }
  for (int i_2_1_s_121 = 0; i_2_1_s_121 < 4; ++i_2_1_s_121) {
    if (i_2_1_s_121 < 3) {
      Y_local[((i_2_1_s_121 * 4) + 16)] = (Y_local[((i_2_1_s_121 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_121 + 11)] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_122 = 0; i_2_1_s_122 < 4; ++i_2_1_s_122) {
    Y_local[((i_2_1_s_122 * 4) + 1)] = (Y_local[((i_2_1_s_122 * 4) + 1)] + (A_shared_dyn_local[(i_2_1_s_122 + 7)] * B_shared_dyn_local[5]));
  }
  for (int i_2_1_s_123 = 0; i_2_1_s_123 < 4; ++i_2_1_s_123) {
    if (i_2_1_s_123 < 3) {
      Y_local[((i_2_1_s_123 * 4) + 17)] = (Y_local[((i_2_1_s_123 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_123 + 11)] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_124 = 0; i_2_1_s_124 < 4; ++i_2_1_s_124) {
    Y_local[((i_2_1_s_124 * 4) + 2)] = (Y_local[((i_2_1_s_124 * 4) + 2)] + (A_shared_dyn_local[(i_2_1_s_124 + 7)] * B_shared_dyn_local[6]));
  }
  for (int i_2_1_s_125 = 0; i_2_1_s_125 < 4; ++i_2_1_s_125) {
    if (i_2_1_s_125 < 3) {
      Y_local[((i_2_1_s_125 * 4) + 18)] = (Y_local[((i_2_1_s_125 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_125 + 11)] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_126 = 0; i_2_1_s_126 < 4; ++i_2_1_s_126) {
    Y_local[((i_2_1_s_126 * 4) + 3)] = (Y_local[((i_2_1_s_126 * 4) + 3)] + (A_shared_dyn_local[(i_2_1_s_126 + 7)] * B_shared_dyn_local[7]));
  }
  for (int i_2_1_s_127 = 0; i_2_1_s_127 < 4; ++i_2_1_s_127) {
    if (i_2_1_s_127 < 3) {
      Y_local[((i_2_1_s_127 * 4) + 19)] = (Y_local[((i_2_1_s_127 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_127 + 11)] * B_shared_dyn_local[7]));
    }
  }
__asm__ __volatile__("cp.async.wait_group 1;");

  __syncthreads();
  for (int ax0_0_17 = 0; ax0_0_17 < 2; ++ax0_0_17) {
    for (int ax0_1_s_17 = 0; ax0_1_s_17 < 4; ++ax0_1_s_17) {
      if (((ax0_0_17 * 4) + ax0_1_s_17) < 7) {
        A_shared_dyn_local[(((ax0_0_17 * 4) + ax0_1_s_17) + 7)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_17 * 80)) + (ax0_1_s_17 * 20)) + 14081)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 4) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 4224));
  for (int i_2_1_s_128 = 0; i_2_1_s_128 < 4; ++i_2_1_s_128) {
    Y_local[(i_2_1_s_128 * 4)] = (Y_local[(i_2_1_s_128 * 4)] + (A_shared_dyn_local[i_2_1_s_128] * B_shared_dyn_local[0]));
  }
  for (int i_2_1_s_129 = 0; i_2_1_s_129 < 4; ++i_2_1_s_129) {
    if (i_2_1_s_129 < 3) {
      Y_local[((i_2_1_s_129 * 4) + 16)] = (Y_local[((i_2_1_s_129 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_129 + 4)] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_130 = 0; i_2_1_s_130 < 4; ++i_2_1_s_130) {
    Y_local[((i_2_1_s_130 * 4) + 1)] = (Y_local[((i_2_1_s_130 * 4) + 1)] + (A_shared_dyn_local[i_2_1_s_130] * B_shared_dyn_local[1]));
  }
  for (int i_2_1_s_131 = 0; i_2_1_s_131 < 4; ++i_2_1_s_131) {
    if (i_2_1_s_131 < 3) {
      Y_local[((i_2_1_s_131 * 4) + 17)] = (Y_local[((i_2_1_s_131 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_131 + 4)] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_132 = 0; i_2_1_s_132 < 4; ++i_2_1_s_132) {
    Y_local[((i_2_1_s_132 * 4) + 2)] = (Y_local[((i_2_1_s_132 * 4) + 2)] + (A_shared_dyn_local[i_2_1_s_132] * B_shared_dyn_local[2]));
  }
  for (int i_2_1_s_133 = 0; i_2_1_s_133 < 4; ++i_2_1_s_133) {
    if (i_2_1_s_133 < 3) {
      Y_local[((i_2_1_s_133 * 4) + 18)] = (Y_local[((i_2_1_s_133 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_133 + 4)] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_134 = 0; i_2_1_s_134 < 4; ++i_2_1_s_134) {
    Y_local[((i_2_1_s_134 * 4) + 3)] = (Y_local[((i_2_1_s_134 * 4) + 3)] + (A_shared_dyn_local[i_2_1_s_134] * B_shared_dyn_local[3]));
  }
  for (int i_2_1_s_135 = 0; i_2_1_s_135 < 4; ++i_2_1_s_135) {
    if (i_2_1_s_135 < 3) {
      Y_local[((i_2_1_s_135 * 4) + 19)] = (Y_local[((i_2_1_s_135 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_135 + 4)] * B_shared_dyn_local[3]));
    }
  }
  for (int ax0_0_18 = 0; ax0_0_18 < 2; ++ax0_0_18) {
    for (int ax0_1_s_18 = 0; ax0_1_s_18 < 4; ++ax0_1_s_18) {
      if (((ax0_0_18 * 4) + ax0_1_s_18) < 7) {
        A_shared_dyn_local[((ax0_0_18 * 4) + ax0_1_s_18)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_18 * 80)) + (ax0_1_s_18 * 20)) + 14082)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 0) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 4352));
  for (int i_2_1_s_136 = 0; i_2_1_s_136 < 4; ++i_2_1_s_136) {
    Y_local[(i_2_1_s_136 * 4)] = (Y_local[(i_2_1_s_136 * 4)] + (A_shared_dyn_local[(i_2_1_s_136 + 7)] * B_shared_dyn_local[4]));
  }
  for (int i_2_1_s_137 = 0; i_2_1_s_137 < 4; ++i_2_1_s_137) {
    if (i_2_1_s_137 < 3) {
      Y_local[((i_2_1_s_137 * 4) + 16)] = (Y_local[((i_2_1_s_137 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_137 + 11)] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_138 = 0; i_2_1_s_138 < 4; ++i_2_1_s_138) {
    Y_local[((i_2_1_s_138 * 4) + 1)] = (Y_local[((i_2_1_s_138 * 4) + 1)] + (A_shared_dyn_local[(i_2_1_s_138 + 7)] * B_shared_dyn_local[5]));
  }
  for (int i_2_1_s_139 = 0; i_2_1_s_139 < 4; ++i_2_1_s_139) {
    if (i_2_1_s_139 < 3) {
      Y_local[((i_2_1_s_139 * 4) + 17)] = (Y_local[((i_2_1_s_139 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_139 + 11)] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_140 = 0; i_2_1_s_140 < 4; ++i_2_1_s_140) {
    Y_local[((i_2_1_s_140 * 4) + 2)] = (Y_local[((i_2_1_s_140 * 4) + 2)] + (A_shared_dyn_local[(i_2_1_s_140 + 7)] * B_shared_dyn_local[6]));
  }
  for (int i_2_1_s_141 = 0; i_2_1_s_141 < 4; ++i_2_1_s_141) {
    if (i_2_1_s_141 < 3) {
      Y_local[((i_2_1_s_141 * 4) + 18)] = (Y_local[((i_2_1_s_141 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_141 + 11)] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_142 = 0; i_2_1_s_142 < 4; ++i_2_1_s_142) {
    Y_local[((i_2_1_s_142 * 4) + 3)] = (Y_local[((i_2_1_s_142 * 4) + 3)] + (A_shared_dyn_local[(i_2_1_s_142 + 7)] * B_shared_dyn_local[7]));
  }
  for (int i_2_1_s_143 = 0; i_2_1_s_143 < 4; ++i_2_1_s_143) {
    if (i_2_1_s_143 < 3) {
      Y_local[((i_2_1_s_143 * 4) + 19)] = (Y_local[((i_2_1_s_143 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_143 + 11)] * B_shared_dyn_local[7]));
    }
  }
  for (int ax0_0_19 = 0; ax0_0_19 < 2; ++ax0_0_19) {
    for (int ax0_1_s_19 = 0; ax0_1_s_19 < 4; ++ax0_1_s_19) {
      if (((ax0_0_19 * 4) + ax0_1_s_19) < 7) {
        A_shared_dyn_local[(((ax0_0_19 * 4) + ax0_1_s_19) + 7)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_19 * 80)) + (ax0_1_s_19 * 20)) + 14083)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 4) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 4480));
  for (int i_2_1_s_144 = 0; i_2_1_s_144 < 4; ++i_2_1_s_144) {
    Y_local[(i_2_1_s_144 * 4)] = (Y_local[(i_2_1_s_144 * 4)] + (A_shared_dyn_local[i_2_1_s_144] * B_shared_dyn_local[0]));
  }
  for (int i_2_1_s_145 = 0; i_2_1_s_145 < 4; ++i_2_1_s_145) {
    if (i_2_1_s_145 < 3) {
      Y_local[((i_2_1_s_145 * 4) + 16)] = (Y_local[((i_2_1_s_145 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_145 + 4)] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_146 = 0; i_2_1_s_146 < 4; ++i_2_1_s_146) {
    Y_local[((i_2_1_s_146 * 4) + 1)] = (Y_local[((i_2_1_s_146 * 4) + 1)] + (A_shared_dyn_local[i_2_1_s_146] * B_shared_dyn_local[1]));
  }
  for (int i_2_1_s_147 = 0; i_2_1_s_147 < 4; ++i_2_1_s_147) {
    if (i_2_1_s_147 < 3) {
      Y_local[((i_2_1_s_147 * 4) + 17)] = (Y_local[((i_2_1_s_147 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_147 + 4)] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_148 = 0; i_2_1_s_148 < 4; ++i_2_1_s_148) {
    Y_local[((i_2_1_s_148 * 4) + 2)] = (Y_local[((i_2_1_s_148 * 4) + 2)] + (A_shared_dyn_local[i_2_1_s_148] * B_shared_dyn_local[2]));
  }
  for (int i_2_1_s_149 = 0; i_2_1_s_149 < 4; ++i_2_1_s_149) {
    if (i_2_1_s_149 < 3) {
      Y_local[((i_2_1_s_149 * 4) + 18)] = (Y_local[((i_2_1_s_149 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_149 + 4)] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_150 = 0; i_2_1_s_150 < 4; ++i_2_1_s_150) {
    Y_local[((i_2_1_s_150 * 4) + 3)] = (Y_local[((i_2_1_s_150 * 4) + 3)] + (A_shared_dyn_local[i_2_1_s_150] * B_shared_dyn_local[3]));
  }
  for (int i_2_1_s_151 = 0; i_2_1_s_151 < 4; ++i_2_1_s_151) {
    if (i_2_1_s_151 < 3) {
      Y_local[((i_2_1_s_151 * 4) + 19)] = (Y_local[((i_2_1_s_151 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_151 + 4)] * B_shared_dyn_local[3]));
    }
  }
  for (int ax0_0_20 = 0; ax0_0_20 < 2; ++ax0_0_20) {
    for (int ax0_1_s_20 = 0; ax0_1_s_20 < 4; ++ax0_1_s_20) {
      if (((ax0_0_20 * 4) + ax0_1_s_20) < 7) {
        A_shared_dyn_local[((ax0_0_20 * 4) + ax0_1_s_20)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_20 * 80)) + (ax0_1_s_20 * 20)) + 14096)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 0) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 4608));
  for (int i_2_1_s_152 = 0; i_2_1_s_152 < 4; ++i_2_1_s_152) {
    Y_local[(i_2_1_s_152 * 4)] = (Y_local[(i_2_1_s_152 * 4)] + (A_shared_dyn_local[(i_2_1_s_152 + 7)] * B_shared_dyn_local[4]));
  }
  for (int i_2_1_s_153 = 0; i_2_1_s_153 < 4; ++i_2_1_s_153) {
    if (i_2_1_s_153 < 3) {
      Y_local[((i_2_1_s_153 * 4) + 16)] = (Y_local[((i_2_1_s_153 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_153 + 11)] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_154 = 0; i_2_1_s_154 < 4; ++i_2_1_s_154) {
    Y_local[((i_2_1_s_154 * 4) + 1)] = (Y_local[((i_2_1_s_154 * 4) + 1)] + (A_shared_dyn_local[(i_2_1_s_154 + 7)] * B_shared_dyn_local[5]));
  }
  for (int i_2_1_s_155 = 0; i_2_1_s_155 < 4; ++i_2_1_s_155) {
    if (i_2_1_s_155 < 3) {
      Y_local[((i_2_1_s_155 * 4) + 17)] = (Y_local[((i_2_1_s_155 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_155 + 11)] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_156 = 0; i_2_1_s_156 < 4; ++i_2_1_s_156) {
    Y_local[((i_2_1_s_156 * 4) + 2)] = (Y_local[((i_2_1_s_156 * 4) + 2)] + (A_shared_dyn_local[(i_2_1_s_156 + 7)] * B_shared_dyn_local[6]));
  }
  for (int i_2_1_s_157 = 0; i_2_1_s_157 < 4; ++i_2_1_s_157) {
    if (i_2_1_s_157 < 3) {
      Y_local[((i_2_1_s_157 * 4) + 18)] = (Y_local[((i_2_1_s_157 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_157 + 11)] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_158 = 0; i_2_1_s_158 < 4; ++i_2_1_s_158) {
    Y_local[((i_2_1_s_158 * 4) + 3)] = (Y_local[((i_2_1_s_158 * 4) + 3)] + (A_shared_dyn_local[(i_2_1_s_158 + 7)] * B_shared_dyn_local[7]));
  }
  for (int i_2_1_s_159 = 0; i_2_1_s_159 < 4; ++i_2_1_s_159) {
    if (i_2_1_s_159 < 3) {
      Y_local[((i_2_1_s_159 * 4) + 19)] = (Y_local[((i_2_1_s_159 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_159 + 11)] * B_shared_dyn_local[7]));
    }
  }
  for (int ax0_0_21 = 0; ax0_0_21 < 2; ++ax0_0_21) {
    for (int ax0_1_s_21 = 0; ax0_1_s_21 < 4; ++ax0_1_s_21) {
      if (((ax0_0_21 * 4) + ax0_1_s_21) < 7) {
        A_shared_dyn_local[(((ax0_0_21 * 4) + ax0_1_s_21) + 7)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_21 * 80)) + (ax0_1_s_21 * 20)) + 14097)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 4) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 4736));
  for (int i_2_1_s_160 = 0; i_2_1_s_160 < 4; ++i_2_1_s_160) {
    Y_local[(i_2_1_s_160 * 4)] = (Y_local[(i_2_1_s_160 * 4)] + (A_shared_dyn_local[i_2_1_s_160] * B_shared_dyn_local[0]));
  }
  for (int i_2_1_s_161 = 0; i_2_1_s_161 < 4; ++i_2_1_s_161) {
    if (i_2_1_s_161 < 3) {
      Y_local[((i_2_1_s_161 * 4) + 16)] = (Y_local[((i_2_1_s_161 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_161 + 4)] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_162 = 0; i_2_1_s_162 < 4; ++i_2_1_s_162) {
    Y_local[((i_2_1_s_162 * 4) + 1)] = (Y_local[((i_2_1_s_162 * 4) + 1)] + (A_shared_dyn_local[i_2_1_s_162] * B_shared_dyn_local[1]));
  }
  for (int i_2_1_s_163 = 0; i_2_1_s_163 < 4; ++i_2_1_s_163) {
    if (i_2_1_s_163 < 3) {
      Y_local[((i_2_1_s_163 * 4) + 17)] = (Y_local[((i_2_1_s_163 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_163 + 4)] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_164 = 0; i_2_1_s_164 < 4; ++i_2_1_s_164) {
    Y_local[((i_2_1_s_164 * 4) + 2)] = (Y_local[((i_2_1_s_164 * 4) + 2)] + (A_shared_dyn_local[i_2_1_s_164] * B_shared_dyn_local[2]));
  }
  for (int i_2_1_s_165 = 0; i_2_1_s_165 < 4; ++i_2_1_s_165) {
    if (i_2_1_s_165 < 3) {
      Y_local[((i_2_1_s_165 * 4) + 18)] = (Y_local[((i_2_1_s_165 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_165 + 4)] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_166 = 0; i_2_1_s_166 < 4; ++i_2_1_s_166) {
    Y_local[((i_2_1_s_166 * 4) + 3)] = (Y_local[((i_2_1_s_166 * 4) + 3)] + (A_shared_dyn_local[i_2_1_s_166] * B_shared_dyn_local[3]));
  }
  for (int i_2_1_s_167 = 0; i_2_1_s_167 < 4; ++i_2_1_s_167) {
    if (i_2_1_s_167 < 3) {
      Y_local[((i_2_1_s_167 * 4) + 19)] = (Y_local[((i_2_1_s_167 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_167 + 4)] * B_shared_dyn_local[3]));
    }
  }
  for (int ax0_0_22 = 0; ax0_0_22 < 2; ++ax0_0_22) {
    for (int ax0_1_s_22 = 0; ax0_1_s_22 < 4; ++ax0_1_s_22) {
      if (((ax0_0_22 * 4) + ax0_1_s_22) < 7) {
        A_shared_dyn_local[((ax0_0_22 * 4) + ax0_1_s_22)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_22 * 80)) + (ax0_1_s_22 * 20)) + 14098)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 0) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 4864));
  for (int i_2_1_s_168 = 0; i_2_1_s_168 < 4; ++i_2_1_s_168) {
    Y_local[(i_2_1_s_168 * 4)] = (Y_local[(i_2_1_s_168 * 4)] + (A_shared_dyn_local[(i_2_1_s_168 + 7)] * B_shared_dyn_local[4]));
  }
  for (int i_2_1_s_169 = 0; i_2_1_s_169 < 4; ++i_2_1_s_169) {
    if (i_2_1_s_169 < 3) {
      Y_local[((i_2_1_s_169 * 4) + 16)] = (Y_local[((i_2_1_s_169 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_169 + 11)] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_170 = 0; i_2_1_s_170 < 4; ++i_2_1_s_170) {
    Y_local[((i_2_1_s_170 * 4) + 1)] = (Y_local[((i_2_1_s_170 * 4) + 1)] + (A_shared_dyn_local[(i_2_1_s_170 + 7)] * B_shared_dyn_local[5]));
  }
  for (int i_2_1_s_171 = 0; i_2_1_s_171 < 4; ++i_2_1_s_171) {
    if (i_2_1_s_171 < 3) {
      Y_local[((i_2_1_s_171 * 4) + 17)] = (Y_local[((i_2_1_s_171 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_171 + 11)] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_172 = 0; i_2_1_s_172 < 4; ++i_2_1_s_172) {
    Y_local[((i_2_1_s_172 * 4) + 2)] = (Y_local[((i_2_1_s_172 * 4) + 2)] + (A_shared_dyn_local[(i_2_1_s_172 + 7)] * B_shared_dyn_local[6]));
  }
  for (int i_2_1_s_173 = 0; i_2_1_s_173 < 4; ++i_2_1_s_173) {
    if (i_2_1_s_173 < 3) {
      Y_local[((i_2_1_s_173 * 4) + 18)] = (Y_local[((i_2_1_s_173 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_173 + 11)] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_174 = 0; i_2_1_s_174 < 4; ++i_2_1_s_174) {
    Y_local[((i_2_1_s_174 * 4) + 3)] = (Y_local[((i_2_1_s_174 * 4) + 3)] + (A_shared_dyn_local[(i_2_1_s_174 + 7)] * B_shared_dyn_local[7]));
  }
  for (int i_2_1_s_175 = 0; i_2_1_s_175 < 4; ++i_2_1_s_175) {
    if (i_2_1_s_175 < 3) {
      Y_local[((i_2_1_s_175 * 4) + 19)] = (Y_local[((i_2_1_s_175 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_175 + 11)] * B_shared_dyn_local[7]));
    }
  }
  for (int ax0_0_23 = 0; ax0_0_23 < 2; ++ax0_0_23) {
    for (int ax0_1_s_23 = 0; ax0_1_s_23 < 4; ++ax0_1_s_23) {
      if (((ax0_0_23 * 4) + ax0_1_s_23) < 7) {
        A_shared_dyn_local[(((ax0_0_23 * 4) + ax0_1_s_23) + 7)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_23 * 80)) + (ax0_1_s_23 * 20)) + 14099)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 4) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 4992));
  for (int i_2_1_s_176 = 0; i_2_1_s_176 < 4; ++i_2_1_s_176) {
    Y_local[(i_2_1_s_176 * 4)] = (Y_local[(i_2_1_s_176 * 4)] + (A_shared_dyn_local[i_2_1_s_176] * B_shared_dyn_local[0]));
  }
  for (int i_2_1_s_177 = 0; i_2_1_s_177 < 4; ++i_2_1_s_177) {
    if (i_2_1_s_177 < 3) {
      Y_local[((i_2_1_s_177 * 4) + 16)] = (Y_local[((i_2_1_s_177 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_177 + 4)] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_178 = 0; i_2_1_s_178 < 4; ++i_2_1_s_178) {
    Y_local[((i_2_1_s_178 * 4) + 1)] = (Y_local[((i_2_1_s_178 * 4) + 1)] + (A_shared_dyn_local[i_2_1_s_178] * B_shared_dyn_local[1]));
  }
  for (int i_2_1_s_179 = 0; i_2_1_s_179 < 4; ++i_2_1_s_179) {
    if (i_2_1_s_179 < 3) {
      Y_local[((i_2_1_s_179 * 4) + 17)] = (Y_local[((i_2_1_s_179 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_179 + 4)] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_180 = 0; i_2_1_s_180 < 4; ++i_2_1_s_180) {
    Y_local[((i_2_1_s_180 * 4) + 2)] = (Y_local[((i_2_1_s_180 * 4) + 2)] + (A_shared_dyn_local[i_2_1_s_180] * B_shared_dyn_local[2]));
  }
  for (int i_2_1_s_181 = 0; i_2_1_s_181 < 4; ++i_2_1_s_181) {
    if (i_2_1_s_181 < 3) {
      Y_local[((i_2_1_s_181 * 4) + 18)] = (Y_local[((i_2_1_s_181 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_181 + 4)] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_182 = 0; i_2_1_s_182 < 4; ++i_2_1_s_182) {
    Y_local[((i_2_1_s_182 * 4) + 3)] = (Y_local[((i_2_1_s_182 * 4) + 3)] + (A_shared_dyn_local[i_2_1_s_182] * B_shared_dyn_local[3]));
  }
  for (int i_2_1_s_183 = 0; i_2_1_s_183 < 4; ++i_2_1_s_183) {
    if (i_2_1_s_183 < 3) {
      Y_local[((i_2_1_s_183 * 4) + 19)] = (Y_local[((i_2_1_s_183 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_183 + 4)] * B_shared_dyn_local[3]));
    }
  }
  for (int ax0_0_24 = 0; ax0_0_24 < 2; ++ax0_0_24) {
    for (int ax0_1_s_24 = 0; ax0_1_s_24 < 4; ++ax0_1_s_24) {
      if (((ax0_0_24 * 4) + ax0_1_s_24) < 7) {
        A_shared_dyn_local[((ax0_0_24 * 4) + ax0_1_s_24)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_24 * 80)) + (ax0_1_s_24 * 20)) + 5120)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 0) = *(float4*)(((float*)buf_dyn_shmem) + (((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)));
  for (int i_2_1_s_184 = 0; i_2_1_s_184 < 4; ++i_2_1_s_184) {
    Y_local[(i_2_1_s_184 * 4)] = (Y_local[(i_2_1_s_184 * 4)] + (A_shared_dyn_local[(i_2_1_s_184 + 7)] * B_shared_dyn_local[4]));
  }
  for (int i_2_1_s_185 = 0; i_2_1_s_185 < 4; ++i_2_1_s_185) {
    if (i_2_1_s_185 < 3) {
      Y_local[((i_2_1_s_185 * 4) + 16)] = (Y_local[((i_2_1_s_185 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_185 + 11)] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_186 = 0; i_2_1_s_186 < 4; ++i_2_1_s_186) {
    Y_local[((i_2_1_s_186 * 4) + 1)] = (Y_local[((i_2_1_s_186 * 4) + 1)] + (A_shared_dyn_local[(i_2_1_s_186 + 7)] * B_shared_dyn_local[5]));
  }
  for (int i_2_1_s_187 = 0; i_2_1_s_187 < 4; ++i_2_1_s_187) {
    if (i_2_1_s_187 < 3) {
      Y_local[((i_2_1_s_187 * 4) + 17)] = (Y_local[((i_2_1_s_187 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_187 + 11)] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_188 = 0; i_2_1_s_188 < 4; ++i_2_1_s_188) {
    Y_local[((i_2_1_s_188 * 4) + 2)] = (Y_local[((i_2_1_s_188 * 4) + 2)] + (A_shared_dyn_local[(i_2_1_s_188 + 7)] * B_shared_dyn_local[6]));
  }
  for (int i_2_1_s_189 = 0; i_2_1_s_189 < 4; ++i_2_1_s_189) {
    if (i_2_1_s_189 < 3) {
      Y_local[((i_2_1_s_189 * 4) + 18)] = (Y_local[((i_2_1_s_189 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_189 + 11)] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_190 = 0; i_2_1_s_190 < 4; ++i_2_1_s_190) {
    Y_local[((i_2_1_s_190 * 4) + 3)] = (Y_local[((i_2_1_s_190 * 4) + 3)] + (A_shared_dyn_local[(i_2_1_s_190 + 7)] * B_shared_dyn_local[7]));
  }
  for (int i_2_1_s_191 = 0; i_2_1_s_191 < 4; ++i_2_1_s_191) {
    if (i_2_1_s_191 < 3) {
      Y_local[((i_2_1_s_191 * 4) + 19)] = (Y_local[((i_2_1_s_191 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_191 + 11)] * B_shared_dyn_local[7]));
    }
  }
__asm__ __volatile__("cp.async.wait_group 0;");

  __syncthreads();
  for (int ax0_0_25 = 0; ax0_0_25 < 2; ++ax0_0_25) {
    for (int ax0_1_s_25 = 0; ax0_1_s_25 < 4; ++ax0_1_s_25) {
      if (((ax0_0_25 * 4) + ax0_1_s_25) < 7) {
        A_shared_dyn_local[(((ax0_0_25 * 4) + ax0_1_s_25) + 7)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_25 * 80)) + (ax0_1_s_25 * 20)) + 5121)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 4) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 128));
  for (int i_2_1_s_192 = 0; i_2_1_s_192 < 4; ++i_2_1_s_192) {
    Y_local[(i_2_1_s_192 * 4)] = (Y_local[(i_2_1_s_192 * 4)] + (A_shared_dyn_local[i_2_1_s_192] * B_shared_dyn_local[0]));
  }
  for (int i_2_1_s_193 = 0; i_2_1_s_193 < 4; ++i_2_1_s_193) {
    if (i_2_1_s_193 < 3) {
      Y_local[((i_2_1_s_193 * 4) + 16)] = (Y_local[((i_2_1_s_193 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_193 + 4)] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_194 = 0; i_2_1_s_194 < 4; ++i_2_1_s_194) {
    Y_local[((i_2_1_s_194 * 4) + 1)] = (Y_local[((i_2_1_s_194 * 4) + 1)] + (A_shared_dyn_local[i_2_1_s_194] * B_shared_dyn_local[1]));
  }
  for (int i_2_1_s_195 = 0; i_2_1_s_195 < 4; ++i_2_1_s_195) {
    if (i_2_1_s_195 < 3) {
      Y_local[((i_2_1_s_195 * 4) + 17)] = (Y_local[((i_2_1_s_195 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_195 + 4)] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_196 = 0; i_2_1_s_196 < 4; ++i_2_1_s_196) {
    Y_local[((i_2_1_s_196 * 4) + 2)] = (Y_local[((i_2_1_s_196 * 4) + 2)] + (A_shared_dyn_local[i_2_1_s_196] * B_shared_dyn_local[2]));
  }
  for (int i_2_1_s_197 = 0; i_2_1_s_197 < 4; ++i_2_1_s_197) {
    if (i_2_1_s_197 < 3) {
      Y_local[((i_2_1_s_197 * 4) + 18)] = (Y_local[((i_2_1_s_197 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_197 + 4)] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_198 = 0; i_2_1_s_198 < 4; ++i_2_1_s_198) {
    Y_local[((i_2_1_s_198 * 4) + 3)] = (Y_local[((i_2_1_s_198 * 4) + 3)] + (A_shared_dyn_local[i_2_1_s_198] * B_shared_dyn_local[3]));
  }
  for (int i_2_1_s_199 = 0; i_2_1_s_199 < 4; ++i_2_1_s_199) {
    if (i_2_1_s_199 < 3) {
      Y_local[((i_2_1_s_199 * 4) + 19)] = (Y_local[((i_2_1_s_199 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_199 + 4)] * B_shared_dyn_local[3]));
    }
  }
  for (int ax0_0_26 = 0; ax0_0_26 < 2; ++ax0_0_26) {
    for (int ax0_1_s_26 = 0; ax0_1_s_26 < 4; ++ax0_1_s_26) {
      if (((ax0_0_26 * 4) + ax0_1_s_26) < 7) {
        A_shared_dyn_local[((ax0_0_26 * 4) + ax0_1_s_26)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_26 * 80)) + (ax0_1_s_26 * 20)) + 5122)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 0) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 256));
  for (int i_2_1_s_200 = 0; i_2_1_s_200 < 4; ++i_2_1_s_200) {
    Y_local[(i_2_1_s_200 * 4)] = (Y_local[(i_2_1_s_200 * 4)] + (A_shared_dyn_local[(i_2_1_s_200 + 7)] * B_shared_dyn_local[4]));
  }
  for (int i_2_1_s_201 = 0; i_2_1_s_201 < 4; ++i_2_1_s_201) {
    if (i_2_1_s_201 < 3) {
      Y_local[((i_2_1_s_201 * 4) + 16)] = (Y_local[((i_2_1_s_201 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_201 + 11)] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_202 = 0; i_2_1_s_202 < 4; ++i_2_1_s_202) {
    Y_local[((i_2_1_s_202 * 4) + 1)] = (Y_local[((i_2_1_s_202 * 4) + 1)] + (A_shared_dyn_local[(i_2_1_s_202 + 7)] * B_shared_dyn_local[5]));
  }
  for (int i_2_1_s_203 = 0; i_2_1_s_203 < 4; ++i_2_1_s_203) {
    if (i_2_1_s_203 < 3) {
      Y_local[((i_2_1_s_203 * 4) + 17)] = (Y_local[((i_2_1_s_203 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_203 + 11)] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_204 = 0; i_2_1_s_204 < 4; ++i_2_1_s_204) {
    Y_local[((i_2_1_s_204 * 4) + 2)] = (Y_local[((i_2_1_s_204 * 4) + 2)] + (A_shared_dyn_local[(i_2_1_s_204 + 7)] * B_shared_dyn_local[6]));
  }
  for (int i_2_1_s_205 = 0; i_2_1_s_205 < 4; ++i_2_1_s_205) {
    if (i_2_1_s_205 < 3) {
      Y_local[((i_2_1_s_205 * 4) + 18)] = (Y_local[((i_2_1_s_205 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_205 + 11)] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_206 = 0; i_2_1_s_206 < 4; ++i_2_1_s_206) {
    Y_local[((i_2_1_s_206 * 4) + 3)] = (Y_local[((i_2_1_s_206 * 4) + 3)] + (A_shared_dyn_local[(i_2_1_s_206 + 7)] * B_shared_dyn_local[7]));
  }
  for (int i_2_1_s_207 = 0; i_2_1_s_207 < 4; ++i_2_1_s_207) {
    if (i_2_1_s_207 < 3) {
      Y_local[((i_2_1_s_207 * 4) + 19)] = (Y_local[((i_2_1_s_207 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_207 + 11)] * B_shared_dyn_local[7]));
    }
  }
  for (int ax0_0_27 = 0; ax0_0_27 < 2; ++ax0_0_27) {
    for (int ax0_1_s_27 = 0; ax0_1_s_27 < 4; ++ax0_1_s_27) {
      if (((ax0_0_27 * 4) + ax0_1_s_27) < 7) {
        A_shared_dyn_local[(((ax0_0_27 * 4) + ax0_1_s_27) + 7)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_27 * 80)) + (ax0_1_s_27 * 20)) + 5123)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 4) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 384));
  for (int i_2_1_s_208 = 0; i_2_1_s_208 < 4; ++i_2_1_s_208) {
    Y_local[(i_2_1_s_208 * 4)] = (Y_local[(i_2_1_s_208 * 4)] + (A_shared_dyn_local[i_2_1_s_208] * B_shared_dyn_local[0]));
  }
  for (int i_2_1_s_209 = 0; i_2_1_s_209 < 4; ++i_2_1_s_209) {
    if (i_2_1_s_209 < 3) {
      Y_local[((i_2_1_s_209 * 4) + 16)] = (Y_local[((i_2_1_s_209 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_209 + 4)] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_210 = 0; i_2_1_s_210 < 4; ++i_2_1_s_210) {
    Y_local[((i_2_1_s_210 * 4) + 1)] = (Y_local[((i_2_1_s_210 * 4) + 1)] + (A_shared_dyn_local[i_2_1_s_210] * B_shared_dyn_local[1]));
  }
  for (int i_2_1_s_211 = 0; i_2_1_s_211 < 4; ++i_2_1_s_211) {
    if (i_2_1_s_211 < 3) {
      Y_local[((i_2_1_s_211 * 4) + 17)] = (Y_local[((i_2_1_s_211 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_211 + 4)] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_212 = 0; i_2_1_s_212 < 4; ++i_2_1_s_212) {
    Y_local[((i_2_1_s_212 * 4) + 2)] = (Y_local[((i_2_1_s_212 * 4) + 2)] + (A_shared_dyn_local[i_2_1_s_212] * B_shared_dyn_local[2]));
  }
  for (int i_2_1_s_213 = 0; i_2_1_s_213 < 4; ++i_2_1_s_213) {
    if (i_2_1_s_213 < 3) {
      Y_local[((i_2_1_s_213 * 4) + 18)] = (Y_local[((i_2_1_s_213 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_213 + 4)] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_214 = 0; i_2_1_s_214 < 4; ++i_2_1_s_214) {
    Y_local[((i_2_1_s_214 * 4) + 3)] = (Y_local[((i_2_1_s_214 * 4) + 3)] + (A_shared_dyn_local[i_2_1_s_214] * B_shared_dyn_local[3]));
  }
  for (int i_2_1_s_215 = 0; i_2_1_s_215 < 4; ++i_2_1_s_215) {
    if (i_2_1_s_215 < 3) {
      Y_local[((i_2_1_s_215 * 4) + 19)] = (Y_local[((i_2_1_s_215 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_215 + 4)] * B_shared_dyn_local[3]));
    }
  }
  for (int ax0_0_28 = 0; ax0_0_28 < 2; ++ax0_0_28) {
    for (int ax0_1_s_28 = 0; ax0_1_s_28 < 4; ++ax0_1_s_28) {
      if (((ax0_0_28 * 4) + ax0_1_s_28) < 7) {
        A_shared_dyn_local[((ax0_0_28 * 4) + ax0_1_s_28)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_28 * 80)) + (ax0_1_s_28 * 20)) + 5136)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 0) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 512));
  for (int i_2_1_s_216 = 0; i_2_1_s_216 < 4; ++i_2_1_s_216) {
    Y_local[(i_2_1_s_216 * 4)] = (Y_local[(i_2_1_s_216 * 4)] + (A_shared_dyn_local[(i_2_1_s_216 + 7)] * B_shared_dyn_local[4]));
  }
  for (int i_2_1_s_217 = 0; i_2_1_s_217 < 4; ++i_2_1_s_217) {
    if (i_2_1_s_217 < 3) {
      Y_local[((i_2_1_s_217 * 4) + 16)] = (Y_local[((i_2_1_s_217 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_217 + 11)] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_218 = 0; i_2_1_s_218 < 4; ++i_2_1_s_218) {
    Y_local[((i_2_1_s_218 * 4) + 1)] = (Y_local[((i_2_1_s_218 * 4) + 1)] + (A_shared_dyn_local[(i_2_1_s_218 + 7)] * B_shared_dyn_local[5]));
  }
  for (int i_2_1_s_219 = 0; i_2_1_s_219 < 4; ++i_2_1_s_219) {
    if (i_2_1_s_219 < 3) {
      Y_local[((i_2_1_s_219 * 4) + 17)] = (Y_local[((i_2_1_s_219 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_219 + 11)] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_220 = 0; i_2_1_s_220 < 4; ++i_2_1_s_220) {
    Y_local[((i_2_1_s_220 * 4) + 2)] = (Y_local[((i_2_1_s_220 * 4) + 2)] + (A_shared_dyn_local[(i_2_1_s_220 + 7)] * B_shared_dyn_local[6]));
  }
  for (int i_2_1_s_221 = 0; i_2_1_s_221 < 4; ++i_2_1_s_221) {
    if (i_2_1_s_221 < 3) {
      Y_local[((i_2_1_s_221 * 4) + 18)] = (Y_local[((i_2_1_s_221 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_221 + 11)] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_222 = 0; i_2_1_s_222 < 4; ++i_2_1_s_222) {
    Y_local[((i_2_1_s_222 * 4) + 3)] = (Y_local[((i_2_1_s_222 * 4) + 3)] + (A_shared_dyn_local[(i_2_1_s_222 + 7)] * B_shared_dyn_local[7]));
  }
  for (int i_2_1_s_223 = 0; i_2_1_s_223 < 4; ++i_2_1_s_223) {
    if (i_2_1_s_223 < 3) {
      Y_local[((i_2_1_s_223 * 4) + 19)] = (Y_local[((i_2_1_s_223 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_223 + 11)] * B_shared_dyn_local[7]));
    }
  }
  for (int ax0_0_29 = 0; ax0_0_29 < 2; ++ax0_0_29) {
    for (int ax0_1_s_29 = 0; ax0_1_s_29 < 4; ++ax0_1_s_29) {
      if (((ax0_0_29 * 4) + ax0_1_s_29) < 7) {
        A_shared_dyn_local[(((ax0_0_29 * 4) + ax0_1_s_29) + 7)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_29 * 80)) + (ax0_1_s_29 * 20)) + 5137)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 4) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 640));
  for (int i_2_1_s_224 = 0; i_2_1_s_224 < 4; ++i_2_1_s_224) {
    Y_local[(i_2_1_s_224 * 4)] = (Y_local[(i_2_1_s_224 * 4)] + (A_shared_dyn_local[i_2_1_s_224] * B_shared_dyn_local[0]));
  }
  for (int i_2_1_s_225 = 0; i_2_1_s_225 < 4; ++i_2_1_s_225) {
    if (i_2_1_s_225 < 3) {
      Y_local[((i_2_1_s_225 * 4) + 16)] = (Y_local[((i_2_1_s_225 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_225 + 4)] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_226 = 0; i_2_1_s_226 < 4; ++i_2_1_s_226) {
    Y_local[((i_2_1_s_226 * 4) + 1)] = (Y_local[((i_2_1_s_226 * 4) + 1)] + (A_shared_dyn_local[i_2_1_s_226] * B_shared_dyn_local[1]));
  }
  for (int i_2_1_s_227 = 0; i_2_1_s_227 < 4; ++i_2_1_s_227) {
    if (i_2_1_s_227 < 3) {
      Y_local[((i_2_1_s_227 * 4) + 17)] = (Y_local[((i_2_1_s_227 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_227 + 4)] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_228 = 0; i_2_1_s_228 < 4; ++i_2_1_s_228) {
    Y_local[((i_2_1_s_228 * 4) + 2)] = (Y_local[((i_2_1_s_228 * 4) + 2)] + (A_shared_dyn_local[i_2_1_s_228] * B_shared_dyn_local[2]));
  }
  for (int i_2_1_s_229 = 0; i_2_1_s_229 < 4; ++i_2_1_s_229) {
    if (i_2_1_s_229 < 3) {
      Y_local[((i_2_1_s_229 * 4) + 18)] = (Y_local[((i_2_1_s_229 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_229 + 4)] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_230 = 0; i_2_1_s_230 < 4; ++i_2_1_s_230) {
    Y_local[((i_2_1_s_230 * 4) + 3)] = (Y_local[((i_2_1_s_230 * 4) + 3)] + (A_shared_dyn_local[i_2_1_s_230] * B_shared_dyn_local[3]));
  }
  for (int i_2_1_s_231 = 0; i_2_1_s_231 < 4; ++i_2_1_s_231) {
    if (i_2_1_s_231 < 3) {
      Y_local[((i_2_1_s_231 * 4) + 19)] = (Y_local[((i_2_1_s_231 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_231 + 4)] * B_shared_dyn_local[3]));
    }
  }
  for (int ax0_0_30 = 0; ax0_0_30 < 2; ++ax0_0_30) {
    for (int ax0_1_s_30 = 0; ax0_1_s_30 < 4; ++ax0_1_s_30) {
      if (((ax0_0_30 * 4) + ax0_1_s_30) < 7) {
        A_shared_dyn_local[((ax0_0_30 * 4) + ax0_1_s_30)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_30 * 80)) + (ax0_1_s_30 * 20)) + 5138)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 0) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 768));
  for (int i_2_1_s_232 = 0; i_2_1_s_232 < 4; ++i_2_1_s_232) {
    Y_local[(i_2_1_s_232 * 4)] = (Y_local[(i_2_1_s_232 * 4)] + (A_shared_dyn_local[(i_2_1_s_232 + 7)] * B_shared_dyn_local[4]));
  }
  for (int i_2_1_s_233 = 0; i_2_1_s_233 < 4; ++i_2_1_s_233) {
    if (i_2_1_s_233 < 3) {
      Y_local[((i_2_1_s_233 * 4) + 16)] = (Y_local[((i_2_1_s_233 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_233 + 11)] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_234 = 0; i_2_1_s_234 < 4; ++i_2_1_s_234) {
    Y_local[((i_2_1_s_234 * 4) + 1)] = (Y_local[((i_2_1_s_234 * 4) + 1)] + (A_shared_dyn_local[(i_2_1_s_234 + 7)] * B_shared_dyn_local[5]));
  }
  for (int i_2_1_s_235 = 0; i_2_1_s_235 < 4; ++i_2_1_s_235) {
    if (i_2_1_s_235 < 3) {
      Y_local[((i_2_1_s_235 * 4) + 17)] = (Y_local[((i_2_1_s_235 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_235 + 11)] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_236 = 0; i_2_1_s_236 < 4; ++i_2_1_s_236) {
    Y_local[((i_2_1_s_236 * 4) + 2)] = (Y_local[((i_2_1_s_236 * 4) + 2)] + (A_shared_dyn_local[(i_2_1_s_236 + 7)] * B_shared_dyn_local[6]));
  }
  for (int i_2_1_s_237 = 0; i_2_1_s_237 < 4; ++i_2_1_s_237) {
    if (i_2_1_s_237 < 3) {
      Y_local[((i_2_1_s_237 * 4) + 18)] = (Y_local[((i_2_1_s_237 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_237 + 11)] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_238 = 0; i_2_1_s_238 < 4; ++i_2_1_s_238) {
    Y_local[((i_2_1_s_238 * 4) + 3)] = (Y_local[((i_2_1_s_238 * 4) + 3)] + (A_shared_dyn_local[(i_2_1_s_238 + 7)] * B_shared_dyn_local[7]));
  }
  for (int i_2_1_s_239 = 0; i_2_1_s_239 < 4; ++i_2_1_s_239) {
    if (i_2_1_s_239 < 3) {
      Y_local[((i_2_1_s_239 * 4) + 19)] = (Y_local[((i_2_1_s_239 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_239 + 11)] * B_shared_dyn_local[7]));
    }
  }
  for (int ax0_0_31 = 0; ax0_0_31 < 2; ++ax0_0_31) {
    for (int ax0_1_s_31 = 0; ax0_1_s_31 < 4; ++ax0_1_s_31) {
      if (((ax0_0_31 * 4) + ax0_1_s_31) < 7) {
        A_shared_dyn_local[(((ax0_0_31 * 4) + ax0_1_s_31) + 7)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_31 * 80)) + (ax0_1_s_31 * 20)) + 5139)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 4) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 896));
  for (int i_2_1_s_240 = 0; i_2_1_s_240 < 4; ++i_2_1_s_240) {
    Y_local[(i_2_1_s_240 * 4)] = (Y_local[(i_2_1_s_240 * 4)] + (A_shared_dyn_local[i_2_1_s_240] * B_shared_dyn_local[0]));
  }
  for (int i_2_1_s_241 = 0; i_2_1_s_241 < 4; ++i_2_1_s_241) {
    if (i_2_1_s_241 < 3) {
      Y_local[((i_2_1_s_241 * 4) + 16)] = (Y_local[((i_2_1_s_241 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_241 + 4)] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_242 = 0; i_2_1_s_242 < 4; ++i_2_1_s_242) {
    Y_local[((i_2_1_s_242 * 4) + 1)] = (Y_local[((i_2_1_s_242 * 4) + 1)] + (A_shared_dyn_local[i_2_1_s_242] * B_shared_dyn_local[1]));
  }
  for (int i_2_1_s_243 = 0; i_2_1_s_243 < 4; ++i_2_1_s_243) {
    if (i_2_1_s_243 < 3) {
      Y_local[((i_2_1_s_243 * 4) + 17)] = (Y_local[((i_2_1_s_243 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_243 + 4)] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_244 = 0; i_2_1_s_244 < 4; ++i_2_1_s_244) {
    Y_local[((i_2_1_s_244 * 4) + 2)] = (Y_local[((i_2_1_s_244 * 4) + 2)] + (A_shared_dyn_local[i_2_1_s_244] * B_shared_dyn_local[2]));
  }
  for (int i_2_1_s_245 = 0; i_2_1_s_245 < 4; ++i_2_1_s_245) {
    if (i_2_1_s_245 < 3) {
      Y_local[((i_2_1_s_245 * 4) + 18)] = (Y_local[((i_2_1_s_245 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_245 + 4)] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_246 = 0; i_2_1_s_246 < 4; ++i_2_1_s_246) {
    Y_local[((i_2_1_s_246 * 4) + 3)] = (Y_local[((i_2_1_s_246 * 4) + 3)] + (A_shared_dyn_local[i_2_1_s_246] * B_shared_dyn_local[3]));
  }
  for (int i_2_1_s_247 = 0; i_2_1_s_247 < 4; ++i_2_1_s_247) {
    if (i_2_1_s_247 < 3) {
      Y_local[((i_2_1_s_247 * 4) + 19)] = (Y_local[((i_2_1_s_247 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_247 + 4)] * B_shared_dyn_local[3]));
    }
  }
  for (int ax0_0_32 = 0; ax0_0_32 < 2; ++ax0_0_32) {
    for (int ax0_1_s_32 = 0; ax0_1_s_32 < 4; ++ax0_1_s_32) {
      if (((ax0_0_32 * 4) + ax0_1_s_32) < 7) {
        A_shared_dyn_local[((ax0_0_32 * 4) + ax0_1_s_32)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_32 * 80)) + (ax0_1_s_32 * 20)) + 7360)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 0) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 1024));
  for (int i_2_1_s_248 = 0; i_2_1_s_248 < 4; ++i_2_1_s_248) {
    Y_local[(i_2_1_s_248 * 4)] = (Y_local[(i_2_1_s_248 * 4)] + (A_shared_dyn_local[(i_2_1_s_248 + 7)] * B_shared_dyn_local[4]));
  }
  for (int i_2_1_s_249 = 0; i_2_1_s_249 < 4; ++i_2_1_s_249) {
    if (i_2_1_s_249 < 3) {
      Y_local[((i_2_1_s_249 * 4) + 16)] = (Y_local[((i_2_1_s_249 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_249 + 11)] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_250 = 0; i_2_1_s_250 < 4; ++i_2_1_s_250) {
    Y_local[((i_2_1_s_250 * 4) + 1)] = (Y_local[((i_2_1_s_250 * 4) + 1)] + (A_shared_dyn_local[(i_2_1_s_250 + 7)] * B_shared_dyn_local[5]));
  }
  for (int i_2_1_s_251 = 0; i_2_1_s_251 < 4; ++i_2_1_s_251) {
    if (i_2_1_s_251 < 3) {
      Y_local[((i_2_1_s_251 * 4) + 17)] = (Y_local[((i_2_1_s_251 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_251 + 11)] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_252 = 0; i_2_1_s_252 < 4; ++i_2_1_s_252) {
    Y_local[((i_2_1_s_252 * 4) + 2)] = (Y_local[((i_2_1_s_252 * 4) + 2)] + (A_shared_dyn_local[(i_2_1_s_252 + 7)] * B_shared_dyn_local[6]));
  }
  for (int i_2_1_s_253 = 0; i_2_1_s_253 < 4; ++i_2_1_s_253) {
    if (i_2_1_s_253 < 3) {
      Y_local[((i_2_1_s_253 * 4) + 18)] = (Y_local[((i_2_1_s_253 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_253 + 11)] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_254 = 0; i_2_1_s_254 < 4; ++i_2_1_s_254) {
    Y_local[((i_2_1_s_254 * 4) + 3)] = (Y_local[((i_2_1_s_254 * 4) + 3)] + (A_shared_dyn_local[(i_2_1_s_254 + 7)] * B_shared_dyn_local[7]));
  }
  for (int i_2_1_s_255 = 0; i_2_1_s_255 < 4; ++i_2_1_s_255) {
    if (i_2_1_s_255 < 3) {
      Y_local[((i_2_1_s_255 * 4) + 19)] = (Y_local[((i_2_1_s_255 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_255 + 11)] * B_shared_dyn_local[7]));
    }
  }
  for (int ax0_0_33 = 0; ax0_0_33 < 2; ++ax0_0_33) {
    for (int ax0_1_s_33 = 0; ax0_1_s_33 < 4; ++ax0_1_s_33) {
      if (((ax0_0_33 * 4) + ax0_1_s_33) < 7) {
        A_shared_dyn_local[(((ax0_0_33 * 4) + ax0_1_s_33) + 7)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_33 * 80)) + (ax0_1_s_33 * 20)) + 7361)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 4) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 1152));
  for (int i_2_1_s_256 = 0; i_2_1_s_256 < 4; ++i_2_1_s_256) {
    Y_local[(i_2_1_s_256 * 4)] = (Y_local[(i_2_1_s_256 * 4)] + (A_shared_dyn_local[i_2_1_s_256] * B_shared_dyn_local[0]));
  }
  for (int i_2_1_s_257 = 0; i_2_1_s_257 < 4; ++i_2_1_s_257) {
    if (i_2_1_s_257 < 3) {
      Y_local[((i_2_1_s_257 * 4) + 16)] = (Y_local[((i_2_1_s_257 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_257 + 4)] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_258 = 0; i_2_1_s_258 < 4; ++i_2_1_s_258) {
    Y_local[((i_2_1_s_258 * 4) + 1)] = (Y_local[((i_2_1_s_258 * 4) + 1)] + (A_shared_dyn_local[i_2_1_s_258] * B_shared_dyn_local[1]));
  }
  for (int i_2_1_s_259 = 0; i_2_1_s_259 < 4; ++i_2_1_s_259) {
    if (i_2_1_s_259 < 3) {
      Y_local[((i_2_1_s_259 * 4) + 17)] = (Y_local[((i_2_1_s_259 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_259 + 4)] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_260 = 0; i_2_1_s_260 < 4; ++i_2_1_s_260) {
    Y_local[((i_2_1_s_260 * 4) + 2)] = (Y_local[((i_2_1_s_260 * 4) + 2)] + (A_shared_dyn_local[i_2_1_s_260] * B_shared_dyn_local[2]));
  }
  for (int i_2_1_s_261 = 0; i_2_1_s_261 < 4; ++i_2_1_s_261) {
    if (i_2_1_s_261 < 3) {
      Y_local[((i_2_1_s_261 * 4) + 18)] = (Y_local[((i_2_1_s_261 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_261 + 4)] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_262 = 0; i_2_1_s_262 < 4; ++i_2_1_s_262) {
    Y_local[((i_2_1_s_262 * 4) + 3)] = (Y_local[((i_2_1_s_262 * 4) + 3)] + (A_shared_dyn_local[i_2_1_s_262] * B_shared_dyn_local[3]));
  }
  for (int i_2_1_s_263 = 0; i_2_1_s_263 < 4; ++i_2_1_s_263) {
    if (i_2_1_s_263 < 3) {
      Y_local[((i_2_1_s_263 * 4) + 19)] = (Y_local[((i_2_1_s_263 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_263 + 4)] * B_shared_dyn_local[3]));
    }
  }
  for (int ax0_0_34 = 0; ax0_0_34 < 2; ++ax0_0_34) {
    for (int ax0_1_s_34 = 0; ax0_1_s_34 < 4; ++ax0_1_s_34) {
      if (((ax0_0_34 * 4) + ax0_1_s_34) < 7) {
        A_shared_dyn_local[((ax0_0_34 * 4) + ax0_1_s_34)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_34 * 80)) + (ax0_1_s_34 * 20)) + 7362)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 0) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 1280));
  for (int i_2_1_s_264 = 0; i_2_1_s_264 < 4; ++i_2_1_s_264) {
    Y_local[(i_2_1_s_264 * 4)] = (Y_local[(i_2_1_s_264 * 4)] + (A_shared_dyn_local[(i_2_1_s_264 + 7)] * B_shared_dyn_local[4]));
  }
  for (int i_2_1_s_265 = 0; i_2_1_s_265 < 4; ++i_2_1_s_265) {
    if (i_2_1_s_265 < 3) {
      Y_local[((i_2_1_s_265 * 4) + 16)] = (Y_local[((i_2_1_s_265 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_265 + 11)] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_266 = 0; i_2_1_s_266 < 4; ++i_2_1_s_266) {
    Y_local[((i_2_1_s_266 * 4) + 1)] = (Y_local[((i_2_1_s_266 * 4) + 1)] + (A_shared_dyn_local[(i_2_1_s_266 + 7)] * B_shared_dyn_local[5]));
  }
  for (int i_2_1_s_267 = 0; i_2_1_s_267 < 4; ++i_2_1_s_267) {
    if (i_2_1_s_267 < 3) {
      Y_local[((i_2_1_s_267 * 4) + 17)] = (Y_local[((i_2_1_s_267 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_267 + 11)] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_268 = 0; i_2_1_s_268 < 4; ++i_2_1_s_268) {
    Y_local[((i_2_1_s_268 * 4) + 2)] = (Y_local[((i_2_1_s_268 * 4) + 2)] + (A_shared_dyn_local[(i_2_1_s_268 + 7)] * B_shared_dyn_local[6]));
  }
  for (int i_2_1_s_269 = 0; i_2_1_s_269 < 4; ++i_2_1_s_269) {
    if (i_2_1_s_269 < 3) {
      Y_local[((i_2_1_s_269 * 4) + 18)] = (Y_local[((i_2_1_s_269 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_269 + 11)] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_270 = 0; i_2_1_s_270 < 4; ++i_2_1_s_270) {
    Y_local[((i_2_1_s_270 * 4) + 3)] = (Y_local[((i_2_1_s_270 * 4) + 3)] + (A_shared_dyn_local[(i_2_1_s_270 + 7)] * B_shared_dyn_local[7]));
  }
  for (int i_2_1_s_271 = 0; i_2_1_s_271 < 4; ++i_2_1_s_271) {
    if (i_2_1_s_271 < 3) {
      Y_local[((i_2_1_s_271 * 4) + 19)] = (Y_local[((i_2_1_s_271 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_271 + 11)] * B_shared_dyn_local[7]));
    }
  }
  for (int ax0_0_35 = 0; ax0_0_35 < 2; ++ax0_0_35) {
    for (int ax0_1_s_35 = 0; ax0_1_s_35 < 4; ++ax0_1_s_35) {
      if (((ax0_0_35 * 4) + ax0_1_s_35) < 7) {
        A_shared_dyn_local[(((ax0_0_35 * 4) + ax0_1_s_35) + 7)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_35 * 80)) + (ax0_1_s_35 * 20)) + 7363)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 4) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 1408));
  for (int i_2_1_s_272 = 0; i_2_1_s_272 < 4; ++i_2_1_s_272) {
    Y_local[(i_2_1_s_272 * 4)] = (Y_local[(i_2_1_s_272 * 4)] + (A_shared_dyn_local[i_2_1_s_272] * B_shared_dyn_local[0]));
  }
  for (int i_2_1_s_273 = 0; i_2_1_s_273 < 4; ++i_2_1_s_273) {
    if (i_2_1_s_273 < 3) {
      Y_local[((i_2_1_s_273 * 4) + 16)] = (Y_local[((i_2_1_s_273 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_273 + 4)] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_274 = 0; i_2_1_s_274 < 4; ++i_2_1_s_274) {
    Y_local[((i_2_1_s_274 * 4) + 1)] = (Y_local[((i_2_1_s_274 * 4) + 1)] + (A_shared_dyn_local[i_2_1_s_274] * B_shared_dyn_local[1]));
  }
  for (int i_2_1_s_275 = 0; i_2_1_s_275 < 4; ++i_2_1_s_275) {
    if (i_2_1_s_275 < 3) {
      Y_local[((i_2_1_s_275 * 4) + 17)] = (Y_local[((i_2_1_s_275 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_275 + 4)] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_276 = 0; i_2_1_s_276 < 4; ++i_2_1_s_276) {
    Y_local[((i_2_1_s_276 * 4) + 2)] = (Y_local[((i_2_1_s_276 * 4) + 2)] + (A_shared_dyn_local[i_2_1_s_276] * B_shared_dyn_local[2]));
  }
  for (int i_2_1_s_277 = 0; i_2_1_s_277 < 4; ++i_2_1_s_277) {
    if (i_2_1_s_277 < 3) {
      Y_local[((i_2_1_s_277 * 4) + 18)] = (Y_local[((i_2_1_s_277 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_277 + 4)] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_278 = 0; i_2_1_s_278 < 4; ++i_2_1_s_278) {
    Y_local[((i_2_1_s_278 * 4) + 3)] = (Y_local[((i_2_1_s_278 * 4) + 3)] + (A_shared_dyn_local[i_2_1_s_278] * B_shared_dyn_local[3]));
  }
  for (int i_2_1_s_279 = 0; i_2_1_s_279 < 4; ++i_2_1_s_279) {
    if (i_2_1_s_279 < 3) {
      Y_local[((i_2_1_s_279 * 4) + 19)] = (Y_local[((i_2_1_s_279 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_279 + 4)] * B_shared_dyn_local[3]));
    }
  }
  for (int ax0_0_36 = 0; ax0_0_36 < 2; ++ax0_0_36) {
    for (int ax0_1_s_36 = 0; ax0_1_s_36 < 4; ++ax0_1_s_36) {
      if (((ax0_0_36 * 4) + ax0_1_s_36) < 7) {
        A_shared_dyn_local[((ax0_0_36 * 4) + ax0_1_s_36)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_36 * 80)) + (ax0_1_s_36 * 20)) + 7376)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 0) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 1536));
  for (int i_2_1_s_280 = 0; i_2_1_s_280 < 4; ++i_2_1_s_280) {
    Y_local[(i_2_1_s_280 * 4)] = (Y_local[(i_2_1_s_280 * 4)] + (A_shared_dyn_local[(i_2_1_s_280 + 7)] * B_shared_dyn_local[4]));
  }
  for (int i_2_1_s_281 = 0; i_2_1_s_281 < 4; ++i_2_1_s_281) {
    if (i_2_1_s_281 < 3) {
      Y_local[((i_2_1_s_281 * 4) + 16)] = (Y_local[((i_2_1_s_281 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_281 + 11)] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_282 = 0; i_2_1_s_282 < 4; ++i_2_1_s_282) {
    Y_local[((i_2_1_s_282 * 4) + 1)] = (Y_local[((i_2_1_s_282 * 4) + 1)] + (A_shared_dyn_local[(i_2_1_s_282 + 7)] * B_shared_dyn_local[5]));
  }
  for (int i_2_1_s_283 = 0; i_2_1_s_283 < 4; ++i_2_1_s_283) {
    if (i_2_1_s_283 < 3) {
      Y_local[((i_2_1_s_283 * 4) + 17)] = (Y_local[((i_2_1_s_283 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_283 + 11)] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_284 = 0; i_2_1_s_284 < 4; ++i_2_1_s_284) {
    Y_local[((i_2_1_s_284 * 4) + 2)] = (Y_local[((i_2_1_s_284 * 4) + 2)] + (A_shared_dyn_local[(i_2_1_s_284 + 7)] * B_shared_dyn_local[6]));
  }
  for (int i_2_1_s_285 = 0; i_2_1_s_285 < 4; ++i_2_1_s_285) {
    if (i_2_1_s_285 < 3) {
      Y_local[((i_2_1_s_285 * 4) + 18)] = (Y_local[((i_2_1_s_285 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_285 + 11)] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_286 = 0; i_2_1_s_286 < 4; ++i_2_1_s_286) {
    Y_local[((i_2_1_s_286 * 4) + 3)] = (Y_local[((i_2_1_s_286 * 4) + 3)] + (A_shared_dyn_local[(i_2_1_s_286 + 7)] * B_shared_dyn_local[7]));
  }
  for (int i_2_1_s_287 = 0; i_2_1_s_287 < 4; ++i_2_1_s_287) {
    if (i_2_1_s_287 < 3) {
      Y_local[((i_2_1_s_287 * 4) + 19)] = (Y_local[((i_2_1_s_287 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_287 + 11)] * B_shared_dyn_local[7]));
    }
  }
  for (int ax0_0_37 = 0; ax0_0_37 < 2; ++ax0_0_37) {
    for (int ax0_1_s_37 = 0; ax0_1_s_37 < 4; ++ax0_1_s_37) {
      if (((ax0_0_37 * 4) + ax0_1_s_37) < 7) {
        A_shared_dyn_local[(((ax0_0_37 * 4) + ax0_1_s_37) + 7)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_37 * 80)) + (ax0_1_s_37 * 20)) + 7377)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 4) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 1664));
  for (int i_2_1_s_288 = 0; i_2_1_s_288 < 4; ++i_2_1_s_288) {
    Y_local[(i_2_1_s_288 * 4)] = (Y_local[(i_2_1_s_288 * 4)] + (A_shared_dyn_local[i_2_1_s_288] * B_shared_dyn_local[0]));
  }
  for (int i_2_1_s_289 = 0; i_2_1_s_289 < 4; ++i_2_1_s_289) {
    if (i_2_1_s_289 < 3) {
      Y_local[((i_2_1_s_289 * 4) + 16)] = (Y_local[((i_2_1_s_289 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_289 + 4)] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_290 = 0; i_2_1_s_290 < 4; ++i_2_1_s_290) {
    Y_local[((i_2_1_s_290 * 4) + 1)] = (Y_local[((i_2_1_s_290 * 4) + 1)] + (A_shared_dyn_local[i_2_1_s_290] * B_shared_dyn_local[1]));
  }
  for (int i_2_1_s_291 = 0; i_2_1_s_291 < 4; ++i_2_1_s_291) {
    if (i_2_1_s_291 < 3) {
      Y_local[((i_2_1_s_291 * 4) + 17)] = (Y_local[((i_2_1_s_291 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_291 + 4)] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_292 = 0; i_2_1_s_292 < 4; ++i_2_1_s_292) {
    Y_local[((i_2_1_s_292 * 4) + 2)] = (Y_local[((i_2_1_s_292 * 4) + 2)] + (A_shared_dyn_local[i_2_1_s_292] * B_shared_dyn_local[2]));
  }
  for (int i_2_1_s_293 = 0; i_2_1_s_293 < 4; ++i_2_1_s_293) {
    if (i_2_1_s_293 < 3) {
      Y_local[((i_2_1_s_293 * 4) + 18)] = (Y_local[((i_2_1_s_293 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_293 + 4)] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_294 = 0; i_2_1_s_294 < 4; ++i_2_1_s_294) {
    Y_local[((i_2_1_s_294 * 4) + 3)] = (Y_local[((i_2_1_s_294 * 4) + 3)] + (A_shared_dyn_local[i_2_1_s_294] * B_shared_dyn_local[3]));
  }
  for (int i_2_1_s_295 = 0; i_2_1_s_295 < 4; ++i_2_1_s_295) {
    if (i_2_1_s_295 < 3) {
      Y_local[((i_2_1_s_295 * 4) + 19)] = (Y_local[((i_2_1_s_295 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_295 + 4)] * B_shared_dyn_local[3]));
    }
  }
  for (int ax0_0_38 = 0; ax0_0_38 < 2; ++ax0_0_38) {
    for (int ax0_1_s_38 = 0; ax0_1_s_38 < 4; ++ax0_1_s_38) {
      if (((ax0_0_38 * 4) + ax0_1_s_38) < 7) {
        A_shared_dyn_local[((ax0_0_38 * 4) + ax0_1_s_38)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_38 * 80)) + (ax0_1_s_38 * 20)) + 7378)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 0) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 1792));
  for (int i_2_1_s_296 = 0; i_2_1_s_296 < 4; ++i_2_1_s_296) {
    Y_local[(i_2_1_s_296 * 4)] = (Y_local[(i_2_1_s_296 * 4)] + (A_shared_dyn_local[(i_2_1_s_296 + 7)] * B_shared_dyn_local[4]));
  }
  for (int i_2_1_s_297 = 0; i_2_1_s_297 < 4; ++i_2_1_s_297) {
    if (i_2_1_s_297 < 3) {
      Y_local[((i_2_1_s_297 * 4) + 16)] = (Y_local[((i_2_1_s_297 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_297 + 11)] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_298 = 0; i_2_1_s_298 < 4; ++i_2_1_s_298) {
    Y_local[((i_2_1_s_298 * 4) + 1)] = (Y_local[((i_2_1_s_298 * 4) + 1)] + (A_shared_dyn_local[(i_2_1_s_298 + 7)] * B_shared_dyn_local[5]));
  }
  for (int i_2_1_s_299 = 0; i_2_1_s_299 < 4; ++i_2_1_s_299) {
    if (i_2_1_s_299 < 3) {
      Y_local[((i_2_1_s_299 * 4) + 17)] = (Y_local[((i_2_1_s_299 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_299 + 11)] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_300 = 0; i_2_1_s_300 < 4; ++i_2_1_s_300) {
    Y_local[((i_2_1_s_300 * 4) + 2)] = (Y_local[((i_2_1_s_300 * 4) + 2)] + (A_shared_dyn_local[(i_2_1_s_300 + 7)] * B_shared_dyn_local[6]));
  }
  for (int i_2_1_s_301 = 0; i_2_1_s_301 < 4; ++i_2_1_s_301) {
    if (i_2_1_s_301 < 3) {
      Y_local[((i_2_1_s_301 * 4) + 18)] = (Y_local[((i_2_1_s_301 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_301 + 11)] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_302 = 0; i_2_1_s_302 < 4; ++i_2_1_s_302) {
    Y_local[((i_2_1_s_302 * 4) + 3)] = (Y_local[((i_2_1_s_302 * 4) + 3)] + (A_shared_dyn_local[(i_2_1_s_302 + 7)] * B_shared_dyn_local[7]));
  }
  for (int i_2_1_s_303 = 0; i_2_1_s_303 < 4; ++i_2_1_s_303) {
    if (i_2_1_s_303 < 3) {
      Y_local[((i_2_1_s_303 * 4) + 19)] = (Y_local[((i_2_1_s_303 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_303 + 11)] * B_shared_dyn_local[7]));
    }
  }
  for (int ax0_0_39 = 0; ax0_0_39 < 2; ++ax0_0_39) {
    for (int ax0_1_s_39 = 0; ax0_1_s_39 < 4; ++ax0_1_s_39) {
      if (((ax0_0_39 * 4) + ax0_1_s_39) < 7) {
        A_shared_dyn_local[(((ax0_0_39 * 4) + ax0_1_s_39) + 7)] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 3) * 280) + ((((int)threadIdx.x) & 1) * 140)) + (ax0_0_39 * 80)) + (ax0_1_s_39 * 20)) + 7379)];
      }
    }
  }
  *(float4*)(B_shared_dyn_local + 4) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((int)threadIdx.x) >> 8) * 64) + (((((int)threadIdx.x) & 3) >> 1) * 32)) + (((((int)threadIdx.x) & 255) >> 6) * 8)) + (((((int)threadIdx.x) & 7) >> 2) * 4)) + 1920));
  for (int i_2_1_s_304 = 0; i_2_1_s_304 < 4; ++i_2_1_s_304) {
    Y_local[(i_2_1_s_304 * 4)] = (Y_local[(i_2_1_s_304 * 4)] + (A_shared_dyn_local[i_2_1_s_304] * B_shared_dyn_local[0]));
  }
  for (int i_2_1_s_305 = 0; i_2_1_s_305 < 4; ++i_2_1_s_305) {
    if (i_2_1_s_305 < 3) {
      Y_local[((i_2_1_s_305 * 4) + 16)] = (Y_local[((i_2_1_s_305 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_305 + 4)] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_306 = 0; i_2_1_s_306 < 4; ++i_2_1_s_306) {
    Y_local[((i_2_1_s_306 * 4) + 1)] = (Y_local[((i_2_1_s_306 * 4) + 1)] + (A_shared_dyn_local[i_2_1_s_306] * B_shared_dyn_local[1]));
  }
  for (int i_2_1_s_307 = 0; i_2_1_s_307 < 4; ++i_2_1_s_307) {
    if (i_2_1_s_307 < 3) {
      Y_local[((i_2_1_s_307 * 4) + 17)] = (Y_local[((i_2_1_s_307 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_307 + 4)] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_308 = 0; i_2_1_s_308 < 4; ++i_2_1_s_308) {
    Y_local[((i_2_1_s_308 * 4) + 2)] = (Y_local[((i_2_1_s_308 * 4) + 2)] + (A_shared_dyn_local[i_2_1_s_308] * B_shared_dyn_local[2]));
  }
  for (int i_2_1_s_309 = 0; i_2_1_s_309 < 4; ++i_2_1_s_309) {
    if (i_2_1_s_309 < 3) {
      Y_local[((i_2_1_s_309 * 4) + 18)] = (Y_local[((i_2_1_s_309 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_309 + 4)] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_310 = 0; i_2_1_s_310 < 4; ++i_2_1_s_310) {
    Y_local[((i_2_1_s_310 * 4) + 3)] = (Y_local[((i_2_1_s_310 * 4) + 3)] + (A_shared_dyn_local[i_2_1_s_310] * B_shared_dyn_local[3]));
  }
  for (int i_2_1_s_311 = 0; i_2_1_s_311 < 4; ++i_2_1_s_311) {
    if (i_2_1_s_311 < 3) {
      Y_local[((i_2_1_s_311 * 4) + 19)] = (Y_local[((i_2_1_s_311 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_311 + 4)] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_312 = 0; i_2_1_s_312 < 4; ++i_2_1_s_312) {
    Y_local[(i_2_1_s_312 * 4)] = (Y_local[(i_2_1_s_312 * 4)] + (A_shared_dyn_local[(i_2_1_s_312 + 7)] * B_shared_dyn_local[4]));
  }
  for (int i_2_1_s_313 = 0; i_2_1_s_313 < 4; ++i_2_1_s_313) {
    if (i_2_1_s_313 < 3) {
      Y_local[((i_2_1_s_313 * 4) + 16)] = (Y_local[((i_2_1_s_313 * 4) + 16)] + (A_shared_dyn_local[(i_2_1_s_313 + 11)] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_314 = 0; i_2_1_s_314 < 4; ++i_2_1_s_314) {
    Y_local[((i_2_1_s_314 * 4) + 1)] = (Y_local[((i_2_1_s_314 * 4) + 1)] + (A_shared_dyn_local[(i_2_1_s_314 + 7)] * B_shared_dyn_local[5]));
  }
  for (int i_2_1_s_315 = 0; i_2_1_s_315 < 4; ++i_2_1_s_315) {
    if (i_2_1_s_315 < 3) {
      Y_local[((i_2_1_s_315 * 4) + 17)] = (Y_local[((i_2_1_s_315 * 4) + 17)] + (A_shared_dyn_local[(i_2_1_s_315 + 11)] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_316 = 0; i_2_1_s_316 < 4; ++i_2_1_s_316) {
    Y_local[((i_2_1_s_316 * 4) + 2)] = (Y_local[((i_2_1_s_316 * 4) + 2)] + (A_shared_dyn_local[(i_2_1_s_316 + 7)] * B_shared_dyn_local[6]));
  }
  for (int i_2_1_s_317 = 0; i_2_1_s_317 < 4; ++i_2_1_s_317) {
    if (i_2_1_s_317 < 3) {
      Y_local[((i_2_1_s_317 * 4) + 18)] = (Y_local[((i_2_1_s_317 * 4) + 18)] + (A_shared_dyn_local[(i_2_1_s_317 + 11)] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_318 = 0; i_2_1_s_318 < 4; ++i_2_1_s_318) {
    Y_local[((i_2_1_s_318 * 4) + 3)] = (Y_local[((i_2_1_s_318 * 4) + 3)] + (A_shared_dyn_local[(i_2_1_s_318 + 7)] * B_shared_dyn_local[7]));
  }
  for (int i_2_1_s_319 = 0; i_2_1_s_319 < 4; ++i_2_1_s_319) {
    if (i_2_1_s_319 < 3) {
      Y_local[((i_2_1_s_319 * 4) + 19)] = (Y_local[((i_2_1_s_319 * 4) + 19)] + (A_shared_dyn_local[(i_2_1_s_319 + 11)] * B_shared_dyn_local[7]));
    }
  }
  *(float4*)(Y + (((((((((int)blockIdx.x) / 7) * 100352) + (((((int)threadIdx.x) & 63) >> 3) * 12544)) + ((((int)threadIdx.x) & 1) * 6272)) + ((((int)blockIdx.x) % 7) * 128)) + ((((int)threadIdx.x) >> 6) * 16)) + (((((int)threadIdx.x) & 7) >> 1) * 4))) = *(float4*)(Y_local + 0);
  *(float4*)(Y + ((((((((((int)blockIdx.x) / 7) * 100352) + (((((int)threadIdx.x) & 63) >> 3) * 12544)) + ((((int)threadIdx.x) & 1) * 6272)) + ((((int)blockIdx.x) % 7) * 128)) + ((((int)threadIdx.x) >> 6) * 16)) + (((((int)threadIdx.x) & 7) >> 1) * 4)) + 896)) = *(float4*)(Y_local + 4);
  *(float4*)(Y + ((((((((((int)blockIdx.x) / 7) * 100352) + (((((int)threadIdx.x) & 63) >> 3) * 12544)) + ((((int)threadIdx.x) & 1) * 6272)) + ((((int)blockIdx.x) % 7) * 128)) + ((((int)threadIdx.x) >> 6) * 16)) + (((((int)threadIdx.x) & 7) >> 1) * 4)) + 1792)) = *(float4*)(Y_local + 8);
  *(float4*)(Y + ((((((((((int)blockIdx.x) / 7) * 100352) + (((((int)threadIdx.x) & 63) >> 3) * 12544)) + ((((int)threadIdx.x) & 1) * 6272)) + ((((int)blockIdx.x) % 7) * 128)) + ((((int)threadIdx.x) >> 6) * 16)) + (((((int)threadIdx.x) & 7) >> 1) * 4)) + 2688)) = *(float4*)(Y_local + 12);
  *(float4*)(Y + ((((((((((int)blockIdx.x) / 7) * 100352) + (((((int)threadIdx.x) & 63) >> 3) * 12544)) + ((((int)threadIdx.x) & 1) * 6272)) + ((((int)blockIdx.x) % 7) * 128)) + ((((int)threadIdx.x) >> 6) * 16)) + (((((int)threadIdx.x) & 7) >> 1) * 4)) + 3584)) = *(float4*)(Y_local + 16);
  *(float4*)(Y + ((((((((((int)blockIdx.x) / 7) * 100352) + (((((int)threadIdx.x) & 63) >> 3) * 12544)) + ((((int)threadIdx.x) & 1) * 6272)) + ((((int)blockIdx.x) % 7) * 128)) + ((((int)threadIdx.x) >> 6) * 16)) + (((((int)threadIdx.x) & 7) >> 1) * 4)) + 4480)) = *(float4*)(Y_local + 20);
  *(float4*)(Y + ((((((((((int)blockIdx.x) / 7) * 100352) + (((((int)threadIdx.x) & 63) >> 3) * 12544)) + ((((int)threadIdx.x) & 1) * 6272)) + ((((int)blockIdx.x) % 7) * 128)) + ((((int)threadIdx.x) >> 6) * 16)) + (((((int)threadIdx.x) & 7) >> 1) * 4)) + 5376)) = *(float4*)(Y_local + 24);
}


