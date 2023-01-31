
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
extern "C" __global__ void __launch_bounds__(128) main_kernel0(float* __restrict__ A, float* __restrict__ B, float* __restrict__ Y) {
  extern __shared__ uchar buf_dyn_shmem[];
  float Y_local[24];
  float A_shared_dyn_local[4];
  float B_shared_dyn_local[24];
  Y_local[0] = 0.000000e+00f;
  Y_local[12] = 0.000000e+00f;
  Y_local[1] = 0.000000e+00f;
  Y_local[13] = 0.000000e+00f;
  Y_local[2] = 0.000000e+00f;
  Y_local[14] = 0.000000e+00f;
  Y_local[3] = 0.000000e+00f;
  Y_local[15] = 0.000000e+00f;
  Y_local[4] = 0.000000e+00f;
  Y_local[16] = 0.000000e+00f;
  Y_local[5] = 0.000000e+00f;
  Y_local[17] = 0.000000e+00f;
  Y_local[6] = 0.000000e+00f;
  Y_local[18] = 0.000000e+00f;
  Y_local[7] = 0.000000e+00f;
  Y_local[19] = 0.000000e+00f;
  Y_local[8] = 0.000000e+00f;
  Y_local[20] = 0.000000e+00f;
  Y_local[9] = 0.000000e+00f;
  Y_local[21] = 0.000000e+00f;
  Y_local[10] = 0.000000e+00f;
  Y_local[22] = 0.000000e+00f;
  Y_local[11] = 0.000000e+00f;
  Y_local[23] = 0.000000e+00f;

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + ((((((int)threadIdx.x) >> 3) * 128) + ((((int)threadIdx.x) & 1) * 64)) + (((((int)threadIdx.x) & 7) >> 1) * 16))))
    );
    __asm__ __volatile__(
      "cp.async.cg.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(A + ((((((int)threadIdx.x) >> 4) * 512) + ((((int)blockIdx.x) >> 3) * 64)) + ((((int)threadIdx.x) & 15) * 4)))), "n"(16)
    );
  }
  for (int ax0_ax1_fused_2 = 0; ax0_ax1_fused_2 < 3; ++ax0_ax1_fused_2) {

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + ((((((((((int)threadIdx.x) >> 4) * 512) + (((((((int)blockIdx.x) & 7) * 3) + ((((((int)threadIdx.x) & 15) * 3) + ax0_ax1_fused_2) >> 4)) >> 2) * 256)) + (((((((int)threadIdx.x) * 3) + ax0_ax1_fused_2) & 7) >> 2) * 128)) + (((((((int)blockIdx.x) & 7) * 6) + ((((((int)threadIdx.x) & 15) * 3) + ax0_ax1_fused_2) >> 3)) & 7) * 16)) + ((((((int)threadIdx.x) * 3) + ax0_ax1_fused_2) & 3) * 4)) + 8192) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 256))))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(B + (((((((int)threadIdx.x) >> 4) * 384) + ((((int)blockIdx.x) & 7) * 48)) + ((((int)threadIdx.x) & 15) * 3)) + ax0_ax1_fused_2))), "n"(4)
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
       :: "r"(addr), "l"((void*)(A + (((((((int)threadIdx.x) >> 4) * 512) + ((((int)blockIdx.x) >> 3) * 64)) + ((((int)threadIdx.x) & 15) * 4)) + 4096))), "n"(16)
    );
  }
  for (int ax0_ax1_fused_2_1 = 0; ax0_ax1_fused_2_1 < 3; ++ax0_ax1_fused_2_1) {

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + ((((((((((int)threadIdx.x) >> 4) * 512) + (((((((int)blockIdx.x) & 7) * 3) + ((((((int)threadIdx.x) & 15) * 3) + ax0_ax1_fused_2_1) >> 4)) >> 2) * 256)) + (((((((int)threadIdx.x) * 3) + ax0_ax1_fused_2_1) & 7) >> 2) * 128)) + (((((((int)blockIdx.x) & 7) * 6) + ((((((int)threadIdx.x) & 15) * 3) + ax0_ax1_fused_2_1) >> 3)) & 7) * 16)) + ((((((int)threadIdx.x) * 3) + ax0_ax1_fused_2_1) & 3) * 4)) + 12288) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 256))))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(B + ((((((((int)threadIdx.x) >> 4) * 384) + ((((int)blockIdx.x) & 7) * 48)) + ((((int)threadIdx.x) & 15) * 3)) + ax0_ax1_fused_2_1) + 3072))), "n"(4)
    );
  }
  }
__asm__ __volatile__("cp.async.commit_group;");


  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + (((((((int)threadIdx.x) >> 3) * 128) + ((((int)threadIdx.x) & 1) * 64)) + (((((int)threadIdx.x) & 7) >> 1) * 16)) + 4096)))
    );
    __asm__ __volatile__(
      "cp.async.cg.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(A + (((((((int)threadIdx.x) >> 4) * 512) + ((((int)blockIdx.x) >> 3) * 64)) + ((((int)threadIdx.x) & 15) * 4)) + 8192))), "n"(16)
    );
  }
  for (int ax0_ax1_fused_2_2 = 0; ax0_ax1_fused_2_2 < 3; ++ax0_ax1_fused_2_2) {

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + ((((((((((int)threadIdx.x) >> 4) * 512) + (((((((int)blockIdx.x) & 7) * 3) + ((((((int)threadIdx.x) & 15) * 3) + ax0_ax1_fused_2_2) >> 4)) >> 2) * 256)) + (((((((int)threadIdx.x) * 3) + ax0_ax1_fused_2_2) & 7) >> 2) * 128)) + (((((((int)blockIdx.x) & 7) * 6) + ((((((int)threadIdx.x) & 15) * 3) + ax0_ax1_fused_2_2) >> 3)) & 7) * 16)) + ((((((int)threadIdx.x) * 3) + ax0_ax1_fused_2_2) & 3) * 4)) + 16384) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 256))))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(B + ((((((((int)threadIdx.x) >> 4) * 384) + ((((int)blockIdx.x) & 7) * 48)) + ((((int)threadIdx.x) & 15) * 3)) + ax0_ax1_fused_2_2) + 6144))), "n"(4)
    );
  }
  }
__asm__ __volatile__("cp.async.commit_group;");

__asm__ __volatile__("cp.async.wait_group 2;");

  __syncthreads();
  for (int ax1_1_s = 0; ax1_1_s < 4; ++ax1_1_s) {
    if (ax1_1_s < 2) {
      A_shared_dyn_local[ax1_1_s] = ((float*)buf_dyn_shmem)[(((((((((int)threadIdx.x) & 63) >> 5) * 32) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s)];
    }
  }
  for (int ax1_0 = 0; ax1_0 < 3; ++ax1_0) {
    *(float4*)(B_shared_dyn_local + (ax1_0 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0 * 4)) >> 6) * 64) + (((ax1_0 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0 * 4)) >> 3)) & 7) * 4)) + 2048) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
  }
  for (int k_0 = 0; k_0 < 29; ++k_0) {
    __syncthreads();

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + ((((((k_0 + 3) & 3) * 2048) + ((((int)threadIdx.x) >> 3) * 128)) + ((((int)threadIdx.x) & 1) * 64)) + (((((int)threadIdx.x) & 7) >> 1) * 16))))
    );
    __asm__ __volatile__(
      "cp.async.cg.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(A + (((((k_0 * 4096) + ((((int)threadIdx.x) >> 4) * 512)) + ((((int)blockIdx.x) >> 3) * 64)) + ((((int)threadIdx.x) & 15) * 4)) + 12288))), "n"(16)
    );
  }
    for (int ax0_ax1_fused_2_3 = 0; ax0_ax1_fused_2_3 < 3; ++ax0_ax1_fused_2_3) {

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + ((((((((((k_0 + 3) & 3) * 4096) + ((((int)threadIdx.x) >> 4) * 512)) + (((((((int)blockIdx.x) & 7) * 3) + ((((((int)threadIdx.x) & 15) * 3) + ax0_ax1_fused_2_3) >> 4)) >> 2) * 256)) + (((((((int)threadIdx.x) * 3) + ax0_ax1_fused_2_3) & 7) >> 2) * 128)) + (((((((int)blockIdx.x) & 7) * 6) + ((((((int)threadIdx.x) & 15) * 3) + ax0_ax1_fused_2_3) >> 3)) & 7) * 16)) + ((((((int)threadIdx.x) * 3) + ax0_ax1_fused_2_3) & 3) * 4)) + 8192) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 256))))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(B + ((((((k_0 * 3072) + ((((int)threadIdx.x) >> 4) * 384)) + ((((int)blockIdx.x) & 7) * 48)) + ((((int)threadIdx.x) & 15) * 3)) + ax0_ax1_fused_2_3) + 9216))), "n"(4)
    );
  }
    }
__asm__ __volatile__("cp.async.commit_group;");

__asm__ __volatile__("cp.async.wait_group 2;");

    __syncthreads();
    for (int ax1_1_s_1 = 0; ax1_1_s_1 < 4; ++ax1_1_s_1) {
      if (ax1_1_s_1 < 2) {
        A_shared_dyn_local[(ax1_1_s_1 + 2)] = ((float*)buf_dyn_shmem)[((((((((k_0 & 3) * 512) + (((((int)threadIdx.x) & 63) >> 5) * 32)) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_1) + 64)];
      }
    }
    for (int ax1_0_1 = 0; ax1_0_1 < 3; ++ax1_0_1) {
      *(float4*)(B_shared_dyn_local + ((ax1_0_1 * 4) + 12)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((k_0 & 3) * 1024) + (((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_1 * 4)) >> 6) * 64)) + (((ax1_0_1 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_1 * 4)) >> 3)) & 7) * 4)) + 2176) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
    }
    for (int i_2_1_s = 0; i_2_1_s < 4; ++i_2_1_s) {
      if (i_2_1_s < 2) {
        Y_local[(i_2_1_s * 12)] = (Y_local[(i_2_1_s * 12)] + (A_shared_dyn_local[i_2_1_s] * B_shared_dyn_local[0]));
      }
    }
    for (int i_2_1_s_1 = 0; i_2_1_s_1 < 4; ++i_2_1_s_1) {
      if (i_2_1_s_1 < 2) {
        Y_local[((i_2_1_s_1 * 12) + 1)] = (Y_local[((i_2_1_s_1 * 12) + 1)] + (A_shared_dyn_local[i_2_1_s_1] * B_shared_dyn_local[1]));
      }
    }
    for (int i_2_1_s_2 = 0; i_2_1_s_2 < 4; ++i_2_1_s_2) {
      if (i_2_1_s_2 < 2) {
        Y_local[((i_2_1_s_2 * 12) + 2)] = (Y_local[((i_2_1_s_2 * 12) + 2)] + (A_shared_dyn_local[i_2_1_s_2] * B_shared_dyn_local[2]));
      }
    }
    for (int i_2_1_s_3 = 0; i_2_1_s_3 < 4; ++i_2_1_s_3) {
      if (i_2_1_s_3 < 2) {
        Y_local[((i_2_1_s_3 * 12) + 3)] = (Y_local[((i_2_1_s_3 * 12) + 3)] + (A_shared_dyn_local[i_2_1_s_3] * B_shared_dyn_local[3]));
      }
    }
    for (int i_2_1_s_4 = 0; i_2_1_s_4 < 4; ++i_2_1_s_4) {
      if (i_2_1_s_4 < 2) {
        Y_local[((i_2_1_s_4 * 12) + 4)] = (Y_local[((i_2_1_s_4 * 12) + 4)] + (A_shared_dyn_local[i_2_1_s_4] * B_shared_dyn_local[4]));
      }
    }
    for (int i_2_1_s_5 = 0; i_2_1_s_5 < 4; ++i_2_1_s_5) {
      if (i_2_1_s_5 < 2) {
        Y_local[((i_2_1_s_5 * 12) + 5)] = (Y_local[((i_2_1_s_5 * 12) + 5)] + (A_shared_dyn_local[i_2_1_s_5] * B_shared_dyn_local[5]));
      }
    }
    for (int i_2_1_s_6 = 0; i_2_1_s_6 < 4; ++i_2_1_s_6) {
      if (i_2_1_s_6 < 2) {
        Y_local[((i_2_1_s_6 * 12) + 6)] = (Y_local[((i_2_1_s_6 * 12) + 6)] + (A_shared_dyn_local[i_2_1_s_6] * B_shared_dyn_local[6]));
      }
    }
    for (int i_2_1_s_7 = 0; i_2_1_s_7 < 4; ++i_2_1_s_7) {
      if (i_2_1_s_7 < 2) {
        Y_local[((i_2_1_s_7 * 12) + 7)] = (Y_local[((i_2_1_s_7 * 12) + 7)] + (A_shared_dyn_local[i_2_1_s_7] * B_shared_dyn_local[7]));
      }
    }
    for (int i_2_1_s_8 = 0; i_2_1_s_8 < 4; ++i_2_1_s_8) {
      if (i_2_1_s_8 < 2) {
        Y_local[((i_2_1_s_8 * 12) + 8)] = (Y_local[((i_2_1_s_8 * 12) + 8)] + (A_shared_dyn_local[i_2_1_s_8] * B_shared_dyn_local[8]));
      }
    }
    for (int i_2_1_s_9 = 0; i_2_1_s_9 < 4; ++i_2_1_s_9) {
      if (i_2_1_s_9 < 2) {
        Y_local[((i_2_1_s_9 * 12) + 9)] = (Y_local[((i_2_1_s_9 * 12) + 9)] + (A_shared_dyn_local[i_2_1_s_9] * B_shared_dyn_local[9]));
      }
    }
    for (int i_2_1_s_10 = 0; i_2_1_s_10 < 4; ++i_2_1_s_10) {
      if (i_2_1_s_10 < 2) {
        Y_local[((i_2_1_s_10 * 12) + 10)] = (Y_local[((i_2_1_s_10 * 12) + 10)] + (A_shared_dyn_local[i_2_1_s_10] * B_shared_dyn_local[10]));
      }
    }
    for (int i_2_1_s_11 = 0; i_2_1_s_11 < 4; ++i_2_1_s_11) {
      if (i_2_1_s_11 < 2) {
        Y_local[((i_2_1_s_11 * 12) + 11)] = (Y_local[((i_2_1_s_11 * 12) + 11)] + (A_shared_dyn_local[i_2_1_s_11] * B_shared_dyn_local[11]));
      }
    }
    for (int ax1_1_s_2 = 0; ax1_1_s_2 < 4; ++ax1_1_s_2) {
      if (ax1_1_s_2 < 2) {
        A_shared_dyn_local[ax1_1_s_2] = ((float*)buf_dyn_shmem)[((((((((k_0 & 3) * 512) + (((((int)threadIdx.x) & 63) >> 5) * 32)) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_2) + 128)];
      }
    }
    for (int ax1_0_2 = 0; ax1_0_2 < 3; ++ax1_0_2) {
      *(float4*)(B_shared_dyn_local + (ax1_0_2 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((k_0 & 3) * 1024) + (((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_2 * 4)) >> 6) * 64)) + (((ax1_0_2 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_2 * 4)) >> 3)) & 7) * 4)) + 2304) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
    }
    for (int i_2_1_s_12 = 0; i_2_1_s_12 < 4; ++i_2_1_s_12) {
      if (i_2_1_s_12 < 2) {
        Y_local[(i_2_1_s_12 * 12)] = (Y_local[(i_2_1_s_12 * 12)] + (A_shared_dyn_local[(i_2_1_s_12 + 2)] * B_shared_dyn_local[12]));
      }
    }
    for (int i_2_1_s_13 = 0; i_2_1_s_13 < 4; ++i_2_1_s_13) {
      if (i_2_1_s_13 < 2) {
        Y_local[((i_2_1_s_13 * 12) + 1)] = (Y_local[((i_2_1_s_13 * 12) + 1)] + (A_shared_dyn_local[(i_2_1_s_13 + 2)] * B_shared_dyn_local[13]));
      }
    }
    for (int i_2_1_s_14 = 0; i_2_1_s_14 < 4; ++i_2_1_s_14) {
      if (i_2_1_s_14 < 2) {
        Y_local[((i_2_1_s_14 * 12) + 2)] = (Y_local[((i_2_1_s_14 * 12) + 2)] + (A_shared_dyn_local[(i_2_1_s_14 + 2)] * B_shared_dyn_local[14]));
      }
    }
    for (int i_2_1_s_15 = 0; i_2_1_s_15 < 4; ++i_2_1_s_15) {
      if (i_2_1_s_15 < 2) {
        Y_local[((i_2_1_s_15 * 12) + 3)] = (Y_local[((i_2_1_s_15 * 12) + 3)] + (A_shared_dyn_local[(i_2_1_s_15 + 2)] * B_shared_dyn_local[15]));
      }
    }
    for (int i_2_1_s_16 = 0; i_2_1_s_16 < 4; ++i_2_1_s_16) {
      if (i_2_1_s_16 < 2) {
        Y_local[((i_2_1_s_16 * 12) + 4)] = (Y_local[((i_2_1_s_16 * 12) + 4)] + (A_shared_dyn_local[(i_2_1_s_16 + 2)] * B_shared_dyn_local[16]));
      }
    }
    for (int i_2_1_s_17 = 0; i_2_1_s_17 < 4; ++i_2_1_s_17) {
      if (i_2_1_s_17 < 2) {
        Y_local[((i_2_1_s_17 * 12) + 5)] = (Y_local[((i_2_1_s_17 * 12) + 5)] + (A_shared_dyn_local[(i_2_1_s_17 + 2)] * B_shared_dyn_local[17]));
      }
    }
    for (int i_2_1_s_18 = 0; i_2_1_s_18 < 4; ++i_2_1_s_18) {
      if (i_2_1_s_18 < 2) {
        Y_local[((i_2_1_s_18 * 12) + 6)] = (Y_local[((i_2_1_s_18 * 12) + 6)] + (A_shared_dyn_local[(i_2_1_s_18 + 2)] * B_shared_dyn_local[18]));
      }
    }
    for (int i_2_1_s_19 = 0; i_2_1_s_19 < 4; ++i_2_1_s_19) {
      if (i_2_1_s_19 < 2) {
        Y_local[((i_2_1_s_19 * 12) + 7)] = (Y_local[((i_2_1_s_19 * 12) + 7)] + (A_shared_dyn_local[(i_2_1_s_19 + 2)] * B_shared_dyn_local[19]));
      }
    }
    for (int i_2_1_s_20 = 0; i_2_1_s_20 < 4; ++i_2_1_s_20) {
      if (i_2_1_s_20 < 2) {
        Y_local[((i_2_1_s_20 * 12) + 8)] = (Y_local[((i_2_1_s_20 * 12) + 8)] + (A_shared_dyn_local[(i_2_1_s_20 + 2)] * B_shared_dyn_local[20]));
      }
    }
    for (int i_2_1_s_21 = 0; i_2_1_s_21 < 4; ++i_2_1_s_21) {
      if (i_2_1_s_21 < 2) {
        Y_local[((i_2_1_s_21 * 12) + 9)] = (Y_local[((i_2_1_s_21 * 12) + 9)] + (A_shared_dyn_local[(i_2_1_s_21 + 2)] * B_shared_dyn_local[21]));
      }
    }
    for (int i_2_1_s_22 = 0; i_2_1_s_22 < 4; ++i_2_1_s_22) {
      if (i_2_1_s_22 < 2) {
        Y_local[((i_2_1_s_22 * 12) + 10)] = (Y_local[((i_2_1_s_22 * 12) + 10)] + (A_shared_dyn_local[(i_2_1_s_22 + 2)] * B_shared_dyn_local[22]));
      }
    }
    for (int i_2_1_s_23 = 0; i_2_1_s_23 < 4; ++i_2_1_s_23) {
      if (i_2_1_s_23 < 2) {
        Y_local[((i_2_1_s_23 * 12) + 11)] = (Y_local[((i_2_1_s_23 * 12) + 11)] + (A_shared_dyn_local[(i_2_1_s_23 + 2)] * B_shared_dyn_local[23]));
      }
    }
    for (int ax1_1_s_3 = 0; ax1_1_s_3 < 4; ++ax1_1_s_3) {
      if (ax1_1_s_3 < 2) {
        A_shared_dyn_local[(ax1_1_s_3 + 2)] = ((float*)buf_dyn_shmem)[((((((((k_0 & 3) * 512) + (((((int)threadIdx.x) & 63) >> 5) * 32)) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_3) + 192)];
      }
    }
    for (int ax1_0_3 = 0; ax1_0_3 < 3; ++ax1_0_3) {
      *(float4*)(B_shared_dyn_local + ((ax1_0_3 * 4) + 12)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((k_0 & 3) * 1024) + (((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_3 * 4)) >> 6) * 64)) + (((ax1_0_3 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_3 * 4)) >> 3)) & 7) * 4)) + 2432) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
    }
    for (int i_2_1_s_24 = 0; i_2_1_s_24 < 4; ++i_2_1_s_24) {
      if (i_2_1_s_24 < 2) {
        Y_local[(i_2_1_s_24 * 12)] = (Y_local[(i_2_1_s_24 * 12)] + (A_shared_dyn_local[i_2_1_s_24] * B_shared_dyn_local[0]));
      }
    }
    for (int i_2_1_s_25 = 0; i_2_1_s_25 < 4; ++i_2_1_s_25) {
      if (i_2_1_s_25 < 2) {
        Y_local[((i_2_1_s_25 * 12) + 1)] = (Y_local[((i_2_1_s_25 * 12) + 1)] + (A_shared_dyn_local[i_2_1_s_25] * B_shared_dyn_local[1]));
      }
    }
    for (int i_2_1_s_26 = 0; i_2_1_s_26 < 4; ++i_2_1_s_26) {
      if (i_2_1_s_26 < 2) {
        Y_local[((i_2_1_s_26 * 12) + 2)] = (Y_local[((i_2_1_s_26 * 12) + 2)] + (A_shared_dyn_local[i_2_1_s_26] * B_shared_dyn_local[2]));
      }
    }
    for (int i_2_1_s_27 = 0; i_2_1_s_27 < 4; ++i_2_1_s_27) {
      if (i_2_1_s_27 < 2) {
        Y_local[((i_2_1_s_27 * 12) + 3)] = (Y_local[((i_2_1_s_27 * 12) + 3)] + (A_shared_dyn_local[i_2_1_s_27] * B_shared_dyn_local[3]));
      }
    }
    for (int i_2_1_s_28 = 0; i_2_1_s_28 < 4; ++i_2_1_s_28) {
      if (i_2_1_s_28 < 2) {
        Y_local[((i_2_1_s_28 * 12) + 4)] = (Y_local[((i_2_1_s_28 * 12) + 4)] + (A_shared_dyn_local[i_2_1_s_28] * B_shared_dyn_local[4]));
      }
    }
    for (int i_2_1_s_29 = 0; i_2_1_s_29 < 4; ++i_2_1_s_29) {
      if (i_2_1_s_29 < 2) {
        Y_local[((i_2_1_s_29 * 12) + 5)] = (Y_local[((i_2_1_s_29 * 12) + 5)] + (A_shared_dyn_local[i_2_1_s_29] * B_shared_dyn_local[5]));
      }
    }
    for (int i_2_1_s_30 = 0; i_2_1_s_30 < 4; ++i_2_1_s_30) {
      if (i_2_1_s_30 < 2) {
        Y_local[((i_2_1_s_30 * 12) + 6)] = (Y_local[((i_2_1_s_30 * 12) + 6)] + (A_shared_dyn_local[i_2_1_s_30] * B_shared_dyn_local[6]));
      }
    }
    for (int i_2_1_s_31 = 0; i_2_1_s_31 < 4; ++i_2_1_s_31) {
      if (i_2_1_s_31 < 2) {
        Y_local[((i_2_1_s_31 * 12) + 7)] = (Y_local[((i_2_1_s_31 * 12) + 7)] + (A_shared_dyn_local[i_2_1_s_31] * B_shared_dyn_local[7]));
      }
    }
    for (int i_2_1_s_32 = 0; i_2_1_s_32 < 4; ++i_2_1_s_32) {
      if (i_2_1_s_32 < 2) {
        Y_local[((i_2_1_s_32 * 12) + 8)] = (Y_local[((i_2_1_s_32 * 12) + 8)] + (A_shared_dyn_local[i_2_1_s_32] * B_shared_dyn_local[8]));
      }
    }
    for (int i_2_1_s_33 = 0; i_2_1_s_33 < 4; ++i_2_1_s_33) {
      if (i_2_1_s_33 < 2) {
        Y_local[((i_2_1_s_33 * 12) + 9)] = (Y_local[((i_2_1_s_33 * 12) + 9)] + (A_shared_dyn_local[i_2_1_s_33] * B_shared_dyn_local[9]));
      }
    }
    for (int i_2_1_s_34 = 0; i_2_1_s_34 < 4; ++i_2_1_s_34) {
      if (i_2_1_s_34 < 2) {
        Y_local[((i_2_1_s_34 * 12) + 10)] = (Y_local[((i_2_1_s_34 * 12) + 10)] + (A_shared_dyn_local[i_2_1_s_34] * B_shared_dyn_local[10]));
      }
    }
    for (int i_2_1_s_35 = 0; i_2_1_s_35 < 4; ++i_2_1_s_35) {
      if (i_2_1_s_35 < 2) {
        Y_local[((i_2_1_s_35 * 12) + 11)] = (Y_local[((i_2_1_s_35 * 12) + 11)] + (A_shared_dyn_local[i_2_1_s_35] * B_shared_dyn_local[11]));
      }
    }
    for (int ax1_1_s_4 = 0; ax1_1_s_4 < 4; ++ax1_1_s_4) {
      if (ax1_1_s_4 < 2) {
        A_shared_dyn_local[ax1_1_s_4] = ((float*)buf_dyn_shmem)[((((((((k_0 & 3) * 512) + (((((int)threadIdx.x) & 63) >> 5) * 32)) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_4) + 256)];
      }
    }
    for (int ax1_0_4 = 0; ax1_0_4 < 3; ++ax1_0_4) {
      *(float4*)(B_shared_dyn_local + (ax1_0_4 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((k_0 & 3) * 1024) + (((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_4 * 4)) >> 6) * 64)) + (((ax1_0_4 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_4 * 4)) >> 3)) & 7) * 4)) + 2560) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
    }
    for (int i_2_1_s_36 = 0; i_2_1_s_36 < 4; ++i_2_1_s_36) {
      if (i_2_1_s_36 < 2) {
        Y_local[(i_2_1_s_36 * 12)] = (Y_local[(i_2_1_s_36 * 12)] + (A_shared_dyn_local[(i_2_1_s_36 + 2)] * B_shared_dyn_local[12]));
      }
    }
    for (int i_2_1_s_37 = 0; i_2_1_s_37 < 4; ++i_2_1_s_37) {
      if (i_2_1_s_37 < 2) {
        Y_local[((i_2_1_s_37 * 12) + 1)] = (Y_local[((i_2_1_s_37 * 12) + 1)] + (A_shared_dyn_local[(i_2_1_s_37 + 2)] * B_shared_dyn_local[13]));
      }
    }
    for (int i_2_1_s_38 = 0; i_2_1_s_38 < 4; ++i_2_1_s_38) {
      if (i_2_1_s_38 < 2) {
        Y_local[((i_2_1_s_38 * 12) + 2)] = (Y_local[((i_2_1_s_38 * 12) + 2)] + (A_shared_dyn_local[(i_2_1_s_38 + 2)] * B_shared_dyn_local[14]));
      }
    }
    for (int i_2_1_s_39 = 0; i_2_1_s_39 < 4; ++i_2_1_s_39) {
      if (i_2_1_s_39 < 2) {
        Y_local[((i_2_1_s_39 * 12) + 3)] = (Y_local[((i_2_1_s_39 * 12) + 3)] + (A_shared_dyn_local[(i_2_1_s_39 + 2)] * B_shared_dyn_local[15]));
      }
    }
    for (int i_2_1_s_40 = 0; i_2_1_s_40 < 4; ++i_2_1_s_40) {
      if (i_2_1_s_40 < 2) {
        Y_local[((i_2_1_s_40 * 12) + 4)] = (Y_local[((i_2_1_s_40 * 12) + 4)] + (A_shared_dyn_local[(i_2_1_s_40 + 2)] * B_shared_dyn_local[16]));
      }
    }
    for (int i_2_1_s_41 = 0; i_2_1_s_41 < 4; ++i_2_1_s_41) {
      if (i_2_1_s_41 < 2) {
        Y_local[((i_2_1_s_41 * 12) + 5)] = (Y_local[((i_2_1_s_41 * 12) + 5)] + (A_shared_dyn_local[(i_2_1_s_41 + 2)] * B_shared_dyn_local[17]));
      }
    }
    for (int i_2_1_s_42 = 0; i_2_1_s_42 < 4; ++i_2_1_s_42) {
      if (i_2_1_s_42 < 2) {
        Y_local[((i_2_1_s_42 * 12) + 6)] = (Y_local[((i_2_1_s_42 * 12) + 6)] + (A_shared_dyn_local[(i_2_1_s_42 + 2)] * B_shared_dyn_local[18]));
      }
    }
    for (int i_2_1_s_43 = 0; i_2_1_s_43 < 4; ++i_2_1_s_43) {
      if (i_2_1_s_43 < 2) {
        Y_local[((i_2_1_s_43 * 12) + 7)] = (Y_local[((i_2_1_s_43 * 12) + 7)] + (A_shared_dyn_local[(i_2_1_s_43 + 2)] * B_shared_dyn_local[19]));
      }
    }
    for (int i_2_1_s_44 = 0; i_2_1_s_44 < 4; ++i_2_1_s_44) {
      if (i_2_1_s_44 < 2) {
        Y_local[((i_2_1_s_44 * 12) + 8)] = (Y_local[((i_2_1_s_44 * 12) + 8)] + (A_shared_dyn_local[(i_2_1_s_44 + 2)] * B_shared_dyn_local[20]));
      }
    }
    for (int i_2_1_s_45 = 0; i_2_1_s_45 < 4; ++i_2_1_s_45) {
      if (i_2_1_s_45 < 2) {
        Y_local[((i_2_1_s_45 * 12) + 9)] = (Y_local[((i_2_1_s_45 * 12) + 9)] + (A_shared_dyn_local[(i_2_1_s_45 + 2)] * B_shared_dyn_local[21]));
      }
    }
    for (int i_2_1_s_46 = 0; i_2_1_s_46 < 4; ++i_2_1_s_46) {
      if (i_2_1_s_46 < 2) {
        Y_local[((i_2_1_s_46 * 12) + 10)] = (Y_local[((i_2_1_s_46 * 12) + 10)] + (A_shared_dyn_local[(i_2_1_s_46 + 2)] * B_shared_dyn_local[22]));
      }
    }
    for (int i_2_1_s_47 = 0; i_2_1_s_47 < 4; ++i_2_1_s_47) {
      if (i_2_1_s_47 < 2) {
        Y_local[((i_2_1_s_47 * 12) + 11)] = (Y_local[((i_2_1_s_47 * 12) + 11)] + (A_shared_dyn_local[(i_2_1_s_47 + 2)] * B_shared_dyn_local[23]));
      }
    }
    for (int ax1_1_s_5 = 0; ax1_1_s_5 < 4; ++ax1_1_s_5) {
      if (ax1_1_s_5 < 2) {
        A_shared_dyn_local[(ax1_1_s_5 + 2)] = ((float*)buf_dyn_shmem)[((((((((k_0 & 3) * 512) + (((((int)threadIdx.x) & 63) >> 5) * 32)) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_5) + 320)];
      }
    }
    for (int ax1_0_5 = 0; ax1_0_5 < 3; ++ax1_0_5) {
      *(float4*)(B_shared_dyn_local + ((ax1_0_5 * 4) + 12)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((k_0 & 3) * 1024) + (((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_5 * 4)) >> 6) * 64)) + (((ax1_0_5 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_5 * 4)) >> 3)) & 7) * 4)) + 2688) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
    }
    for (int i_2_1_s_48 = 0; i_2_1_s_48 < 4; ++i_2_1_s_48) {
      if (i_2_1_s_48 < 2) {
        Y_local[(i_2_1_s_48 * 12)] = (Y_local[(i_2_1_s_48 * 12)] + (A_shared_dyn_local[i_2_1_s_48] * B_shared_dyn_local[0]));
      }
    }
    for (int i_2_1_s_49 = 0; i_2_1_s_49 < 4; ++i_2_1_s_49) {
      if (i_2_1_s_49 < 2) {
        Y_local[((i_2_1_s_49 * 12) + 1)] = (Y_local[((i_2_1_s_49 * 12) + 1)] + (A_shared_dyn_local[i_2_1_s_49] * B_shared_dyn_local[1]));
      }
    }
    for (int i_2_1_s_50 = 0; i_2_1_s_50 < 4; ++i_2_1_s_50) {
      if (i_2_1_s_50 < 2) {
        Y_local[((i_2_1_s_50 * 12) + 2)] = (Y_local[((i_2_1_s_50 * 12) + 2)] + (A_shared_dyn_local[i_2_1_s_50] * B_shared_dyn_local[2]));
      }
    }
    for (int i_2_1_s_51 = 0; i_2_1_s_51 < 4; ++i_2_1_s_51) {
      if (i_2_1_s_51 < 2) {
        Y_local[((i_2_1_s_51 * 12) + 3)] = (Y_local[((i_2_1_s_51 * 12) + 3)] + (A_shared_dyn_local[i_2_1_s_51] * B_shared_dyn_local[3]));
      }
    }
    for (int i_2_1_s_52 = 0; i_2_1_s_52 < 4; ++i_2_1_s_52) {
      if (i_2_1_s_52 < 2) {
        Y_local[((i_2_1_s_52 * 12) + 4)] = (Y_local[((i_2_1_s_52 * 12) + 4)] + (A_shared_dyn_local[i_2_1_s_52] * B_shared_dyn_local[4]));
      }
    }
    for (int i_2_1_s_53 = 0; i_2_1_s_53 < 4; ++i_2_1_s_53) {
      if (i_2_1_s_53 < 2) {
        Y_local[((i_2_1_s_53 * 12) + 5)] = (Y_local[((i_2_1_s_53 * 12) + 5)] + (A_shared_dyn_local[i_2_1_s_53] * B_shared_dyn_local[5]));
      }
    }
    for (int i_2_1_s_54 = 0; i_2_1_s_54 < 4; ++i_2_1_s_54) {
      if (i_2_1_s_54 < 2) {
        Y_local[((i_2_1_s_54 * 12) + 6)] = (Y_local[((i_2_1_s_54 * 12) + 6)] + (A_shared_dyn_local[i_2_1_s_54] * B_shared_dyn_local[6]));
      }
    }
    for (int i_2_1_s_55 = 0; i_2_1_s_55 < 4; ++i_2_1_s_55) {
      if (i_2_1_s_55 < 2) {
        Y_local[((i_2_1_s_55 * 12) + 7)] = (Y_local[((i_2_1_s_55 * 12) + 7)] + (A_shared_dyn_local[i_2_1_s_55] * B_shared_dyn_local[7]));
      }
    }
    for (int i_2_1_s_56 = 0; i_2_1_s_56 < 4; ++i_2_1_s_56) {
      if (i_2_1_s_56 < 2) {
        Y_local[((i_2_1_s_56 * 12) + 8)] = (Y_local[((i_2_1_s_56 * 12) + 8)] + (A_shared_dyn_local[i_2_1_s_56] * B_shared_dyn_local[8]));
      }
    }
    for (int i_2_1_s_57 = 0; i_2_1_s_57 < 4; ++i_2_1_s_57) {
      if (i_2_1_s_57 < 2) {
        Y_local[((i_2_1_s_57 * 12) + 9)] = (Y_local[((i_2_1_s_57 * 12) + 9)] + (A_shared_dyn_local[i_2_1_s_57] * B_shared_dyn_local[9]));
      }
    }
    for (int i_2_1_s_58 = 0; i_2_1_s_58 < 4; ++i_2_1_s_58) {
      if (i_2_1_s_58 < 2) {
        Y_local[((i_2_1_s_58 * 12) + 10)] = (Y_local[((i_2_1_s_58 * 12) + 10)] + (A_shared_dyn_local[i_2_1_s_58] * B_shared_dyn_local[10]));
      }
    }
    for (int i_2_1_s_59 = 0; i_2_1_s_59 < 4; ++i_2_1_s_59) {
      if (i_2_1_s_59 < 2) {
        Y_local[((i_2_1_s_59 * 12) + 11)] = (Y_local[((i_2_1_s_59 * 12) + 11)] + (A_shared_dyn_local[i_2_1_s_59] * B_shared_dyn_local[11]));
      }
    }
    for (int ax1_1_s_6 = 0; ax1_1_s_6 < 4; ++ax1_1_s_6) {
      if (ax1_1_s_6 < 2) {
        A_shared_dyn_local[ax1_1_s_6] = ((float*)buf_dyn_shmem)[((((((((k_0 & 3) * 512) + (((((int)threadIdx.x) & 63) >> 5) * 32)) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_6) + 384)];
      }
    }
    for (int ax1_0_6 = 0; ax1_0_6 < 3; ++ax1_0_6) {
      *(float4*)(B_shared_dyn_local + (ax1_0_6 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((k_0 & 3) * 1024) + (((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_6 * 4)) >> 6) * 64)) + (((ax1_0_6 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_6 * 4)) >> 3)) & 7) * 4)) + 2816) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
    }
    for (int i_2_1_s_60 = 0; i_2_1_s_60 < 4; ++i_2_1_s_60) {
      if (i_2_1_s_60 < 2) {
        Y_local[(i_2_1_s_60 * 12)] = (Y_local[(i_2_1_s_60 * 12)] + (A_shared_dyn_local[(i_2_1_s_60 + 2)] * B_shared_dyn_local[12]));
      }
    }
    for (int i_2_1_s_61 = 0; i_2_1_s_61 < 4; ++i_2_1_s_61) {
      if (i_2_1_s_61 < 2) {
        Y_local[((i_2_1_s_61 * 12) + 1)] = (Y_local[((i_2_1_s_61 * 12) + 1)] + (A_shared_dyn_local[(i_2_1_s_61 + 2)] * B_shared_dyn_local[13]));
      }
    }
    for (int i_2_1_s_62 = 0; i_2_1_s_62 < 4; ++i_2_1_s_62) {
      if (i_2_1_s_62 < 2) {
        Y_local[((i_2_1_s_62 * 12) + 2)] = (Y_local[((i_2_1_s_62 * 12) + 2)] + (A_shared_dyn_local[(i_2_1_s_62 + 2)] * B_shared_dyn_local[14]));
      }
    }
    for (int i_2_1_s_63 = 0; i_2_1_s_63 < 4; ++i_2_1_s_63) {
      if (i_2_1_s_63 < 2) {
        Y_local[((i_2_1_s_63 * 12) + 3)] = (Y_local[((i_2_1_s_63 * 12) + 3)] + (A_shared_dyn_local[(i_2_1_s_63 + 2)] * B_shared_dyn_local[15]));
      }
    }
    for (int i_2_1_s_64 = 0; i_2_1_s_64 < 4; ++i_2_1_s_64) {
      if (i_2_1_s_64 < 2) {
        Y_local[((i_2_1_s_64 * 12) + 4)] = (Y_local[((i_2_1_s_64 * 12) + 4)] + (A_shared_dyn_local[(i_2_1_s_64 + 2)] * B_shared_dyn_local[16]));
      }
    }
    for (int i_2_1_s_65 = 0; i_2_1_s_65 < 4; ++i_2_1_s_65) {
      if (i_2_1_s_65 < 2) {
        Y_local[((i_2_1_s_65 * 12) + 5)] = (Y_local[((i_2_1_s_65 * 12) + 5)] + (A_shared_dyn_local[(i_2_1_s_65 + 2)] * B_shared_dyn_local[17]));
      }
    }
    for (int i_2_1_s_66 = 0; i_2_1_s_66 < 4; ++i_2_1_s_66) {
      if (i_2_1_s_66 < 2) {
        Y_local[((i_2_1_s_66 * 12) + 6)] = (Y_local[((i_2_1_s_66 * 12) + 6)] + (A_shared_dyn_local[(i_2_1_s_66 + 2)] * B_shared_dyn_local[18]));
      }
    }
    for (int i_2_1_s_67 = 0; i_2_1_s_67 < 4; ++i_2_1_s_67) {
      if (i_2_1_s_67 < 2) {
        Y_local[((i_2_1_s_67 * 12) + 7)] = (Y_local[((i_2_1_s_67 * 12) + 7)] + (A_shared_dyn_local[(i_2_1_s_67 + 2)] * B_shared_dyn_local[19]));
      }
    }
    for (int i_2_1_s_68 = 0; i_2_1_s_68 < 4; ++i_2_1_s_68) {
      if (i_2_1_s_68 < 2) {
        Y_local[((i_2_1_s_68 * 12) + 8)] = (Y_local[((i_2_1_s_68 * 12) + 8)] + (A_shared_dyn_local[(i_2_1_s_68 + 2)] * B_shared_dyn_local[20]));
      }
    }
    for (int i_2_1_s_69 = 0; i_2_1_s_69 < 4; ++i_2_1_s_69) {
      if (i_2_1_s_69 < 2) {
        Y_local[((i_2_1_s_69 * 12) + 9)] = (Y_local[((i_2_1_s_69 * 12) + 9)] + (A_shared_dyn_local[(i_2_1_s_69 + 2)] * B_shared_dyn_local[21]));
      }
    }
    for (int i_2_1_s_70 = 0; i_2_1_s_70 < 4; ++i_2_1_s_70) {
      if (i_2_1_s_70 < 2) {
        Y_local[((i_2_1_s_70 * 12) + 10)] = (Y_local[((i_2_1_s_70 * 12) + 10)] + (A_shared_dyn_local[(i_2_1_s_70 + 2)] * B_shared_dyn_local[22]));
      }
    }
    for (int i_2_1_s_71 = 0; i_2_1_s_71 < 4; ++i_2_1_s_71) {
      if (i_2_1_s_71 < 2) {
        Y_local[((i_2_1_s_71 * 12) + 11)] = (Y_local[((i_2_1_s_71 * 12) + 11)] + (A_shared_dyn_local[(i_2_1_s_71 + 2)] * B_shared_dyn_local[23]));
      }
    }
    for (int ax1_1_s_7 = 0; ax1_1_s_7 < 4; ++ax1_1_s_7) {
      if (ax1_1_s_7 < 2) {
        A_shared_dyn_local[(ax1_1_s_7 + 2)] = ((float*)buf_dyn_shmem)[((((((((k_0 & 3) * 512) + (((((int)threadIdx.x) & 63) >> 5) * 32)) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_7) + 448)];
      }
    }
    for (int ax1_0_7 = 0; ax1_0_7 < 3; ++ax1_0_7) {
      *(float4*)(B_shared_dyn_local + ((ax1_0_7 * 4) + 12)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((k_0 & 3) * 1024) + (((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_7 * 4)) >> 6) * 64)) + (((ax1_0_7 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_7 * 4)) >> 3)) & 7) * 4)) + 2944) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
    }
    for (int i_2_1_s_72 = 0; i_2_1_s_72 < 4; ++i_2_1_s_72) {
      if (i_2_1_s_72 < 2) {
        Y_local[(i_2_1_s_72 * 12)] = (Y_local[(i_2_1_s_72 * 12)] + (A_shared_dyn_local[i_2_1_s_72] * B_shared_dyn_local[0]));
      }
    }
    for (int i_2_1_s_73 = 0; i_2_1_s_73 < 4; ++i_2_1_s_73) {
      if (i_2_1_s_73 < 2) {
        Y_local[((i_2_1_s_73 * 12) + 1)] = (Y_local[((i_2_1_s_73 * 12) + 1)] + (A_shared_dyn_local[i_2_1_s_73] * B_shared_dyn_local[1]));
      }
    }
    for (int i_2_1_s_74 = 0; i_2_1_s_74 < 4; ++i_2_1_s_74) {
      if (i_2_1_s_74 < 2) {
        Y_local[((i_2_1_s_74 * 12) + 2)] = (Y_local[((i_2_1_s_74 * 12) + 2)] + (A_shared_dyn_local[i_2_1_s_74] * B_shared_dyn_local[2]));
      }
    }
    for (int i_2_1_s_75 = 0; i_2_1_s_75 < 4; ++i_2_1_s_75) {
      if (i_2_1_s_75 < 2) {
        Y_local[((i_2_1_s_75 * 12) + 3)] = (Y_local[((i_2_1_s_75 * 12) + 3)] + (A_shared_dyn_local[i_2_1_s_75] * B_shared_dyn_local[3]));
      }
    }
    for (int i_2_1_s_76 = 0; i_2_1_s_76 < 4; ++i_2_1_s_76) {
      if (i_2_1_s_76 < 2) {
        Y_local[((i_2_1_s_76 * 12) + 4)] = (Y_local[((i_2_1_s_76 * 12) + 4)] + (A_shared_dyn_local[i_2_1_s_76] * B_shared_dyn_local[4]));
      }
    }
    for (int i_2_1_s_77 = 0; i_2_1_s_77 < 4; ++i_2_1_s_77) {
      if (i_2_1_s_77 < 2) {
        Y_local[((i_2_1_s_77 * 12) + 5)] = (Y_local[((i_2_1_s_77 * 12) + 5)] + (A_shared_dyn_local[i_2_1_s_77] * B_shared_dyn_local[5]));
      }
    }
    for (int i_2_1_s_78 = 0; i_2_1_s_78 < 4; ++i_2_1_s_78) {
      if (i_2_1_s_78 < 2) {
        Y_local[((i_2_1_s_78 * 12) + 6)] = (Y_local[((i_2_1_s_78 * 12) + 6)] + (A_shared_dyn_local[i_2_1_s_78] * B_shared_dyn_local[6]));
      }
    }
    for (int i_2_1_s_79 = 0; i_2_1_s_79 < 4; ++i_2_1_s_79) {
      if (i_2_1_s_79 < 2) {
        Y_local[((i_2_1_s_79 * 12) + 7)] = (Y_local[((i_2_1_s_79 * 12) + 7)] + (A_shared_dyn_local[i_2_1_s_79] * B_shared_dyn_local[7]));
      }
    }
    for (int i_2_1_s_80 = 0; i_2_1_s_80 < 4; ++i_2_1_s_80) {
      if (i_2_1_s_80 < 2) {
        Y_local[((i_2_1_s_80 * 12) + 8)] = (Y_local[((i_2_1_s_80 * 12) + 8)] + (A_shared_dyn_local[i_2_1_s_80] * B_shared_dyn_local[8]));
      }
    }
    for (int i_2_1_s_81 = 0; i_2_1_s_81 < 4; ++i_2_1_s_81) {
      if (i_2_1_s_81 < 2) {
        Y_local[((i_2_1_s_81 * 12) + 9)] = (Y_local[((i_2_1_s_81 * 12) + 9)] + (A_shared_dyn_local[i_2_1_s_81] * B_shared_dyn_local[9]));
      }
    }
    for (int i_2_1_s_82 = 0; i_2_1_s_82 < 4; ++i_2_1_s_82) {
      if (i_2_1_s_82 < 2) {
        Y_local[((i_2_1_s_82 * 12) + 10)] = (Y_local[((i_2_1_s_82 * 12) + 10)] + (A_shared_dyn_local[i_2_1_s_82] * B_shared_dyn_local[10]));
      }
    }
    for (int i_2_1_s_83 = 0; i_2_1_s_83 < 4; ++i_2_1_s_83) {
      if (i_2_1_s_83 < 2) {
        Y_local[((i_2_1_s_83 * 12) + 11)] = (Y_local[((i_2_1_s_83 * 12) + 11)] + (A_shared_dyn_local[i_2_1_s_83] * B_shared_dyn_local[11]));
      }
    }
    for (int ax1_1_s_8 = 0; ax1_1_s_8 < 4; ++ax1_1_s_8) {
      if (ax1_1_s_8 < 2) {
        A_shared_dyn_local[ax1_1_s_8] = ((float*)buf_dyn_shmem)[((((((((k_0 + 1) & 3) * 512) + (((((int)threadIdx.x) & 63) >> 5) * 32)) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_8)];
      }
    }
    for (int ax1_0_8 = 0; ax1_0_8 < 3; ++ax1_0_8) {
      *(float4*)(B_shared_dyn_local + (ax1_0_8 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((k_0 + 1) & 3) * 1024) + (((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_8 * 4)) >> 6) * 64)) + (((ax1_0_8 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_8 * 4)) >> 3)) & 7) * 4)) + 2048) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
    }
    for (int i_2_1_s_84 = 0; i_2_1_s_84 < 4; ++i_2_1_s_84) {
      if (i_2_1_s_84 < 2) {
        Y_local[(i_2_1_s_84 * 12)] = (Y_local[(i_2_1_s_84 * 12)] + (A_shared_dyn_local[(i_2_1_s_84 + 2)] * B_shared_dyn_local[12]));
      }
    }
    for (int i_2_1_s_85 = 0; i_2_1_s_85 < 4; ++i_2_1_s_85) {
      if (i_2_1_s_85 < 2) {
        Y_local[((i_2_1_s_85 * 12) + 1)] = (Y_local[((i_2_1_s_85 * 12) + 1)] + (A_shared_dyn_local[(i_2_1_s_85 + 2)] * B_shared_dyn_local[13]));
      }
    }
    for (int i_2_1_s_86 = 0; i_2_1_s_86 < 4; ++i_2_1_s_86) {
      if (i_2_1_s_86 < 2) {
        Y_local[((i_2_1_s_86 * 12) + 2)] = (Y_local[((i_2_1_s_86 * 12) + 2)] + (A_shared_dyn_local[(i_2_1_s_86 + 2)] * B_shared_dyn_local[14]));
      }
    }
    for (int i_2_1_s_87 = 0; i_2_1_s_87 < 4; ++i_2_1_s_87) {
      if (i_2_1_s_87 < 2) {
        Y_local[((i_2_1_s_87 * 12) + 3)] = (Y_local[((i_2_1_s_87 * 12) + 3)] + (A_shared_dyn_local[(i_2_1_s_87 + 2)] * B_shared_dyn_local[15]));
      }
    }
    for (int i_2_1_s_88 = 0; i_2_1_s_88 < 4; ++i_2_1_s_88) {
      if (i_2_1_s_88 < 2) {
        Y_local[((i_2_1_s_88 * 12) + 4)] = (Y_local[((i_2_1_s_88 * 12) + 4)] + (A_shared_dyn_local[(i_2_1_s_88 + 2)] * B_shared_dyn_local[16]));
      }
    }
    for (int i_2_1_s_89 = 0; i_2_1_s_89 < 4; ++i_2_1_s_89) {
      if (i_2_1_s_89 < 2) {
        Y_local[((i_2_1_s_89 * 12) + 5)] = (Y_local[((i_2_1_s_89 * 12) + 5)] + (A_shared_dyn_local[(i_2_1_s_89 + 2)] * B_shared_dyn_local[17]));
      }
    }
    for (int i_2_1_s_90 = 0; i_2_1_s_90 < 4; ++i_2_1_s_90) {
      if (i_2_1_s_90 < 2) {
        Y_local[((i_2_1_s_90 * 12) + 6)] = (Y_local[((i_2_1_s_90 * 12) + 6)] + (A_shared_dyn_local[(i_2_1_s_90 + 2)] * B_shared_dyn_local[18]));
      }
    }
    for (int i_2_1_s_91 = 0; i_2_1_s_91 < 4; ++i_2_1_s_91) {
      if (i_2_1_s_91 < 2) {
        Y_local[((i_2_1_s_91 * 12) + 7)] = (Y_local[((i_2_1_s_91 * 12) + 7)] + (A_shared_dyn_local[(i_2_1_s_91 + 2)] * B_shared_dyn_local[19]));
      }
    }
    for (int i_2_1_s_92 = 0; i_2_1_s_92 < 4; ++i_2_1_s_92) {
      if (i_2_1_s_92 < 2) {
        Y_local[((i_2_1_s_92 * 12) + 8)] = (Y_local[((i_2_1_s_92 * 12) + 8)] + (A_shared_dyn_local[(i_2_1_s_92 + 2)] * B_shared_dyn_local[20]));
      }
    }
    for (int i_2_1_s_93 = 0; i_2_1_s_93 < 4; ++i_2_1_s_93) {
      if (i_2_1_s_93 < 2) {
        Y_local[((i_2_1_s_93 * 12) + 9)] = (Y_local[((i_2_1_s_93 * 12) + 9)] + (A_shared_dyn_local[(i_2_1_s_93 + 2)] * B_shared_dyn_local[21]));
      }
    }
    for (int i_2_1_s_94 = 0; i_2_1_s_94 < 4; ++i_2_1_s_94) {
      if (i_2_1_s_94 < 2) {
        Y_local[((i_2_1_s_94 * 12) + 10)] = (Y_local[((i_2_1_s_94 * 12) + 10)] + (A_shared_dyn_local[(i_2_1_s_94 + 2)] * B_shared_dyn_local[22]));
      }
    }
    for (int i_2_1_s_95 = 0; i_2_1_s_95 < 4; ++i_2_1_s_95) {
      if (i_2_1_s_95 < 2) {
        Y_local[((i_2_1_s_95 * 12) + 11)] = (Y_local[((i_2_1_s_95 * 12) + 11)] + (A_shared_dyn_local[(i_2_1_s_95 + 2)] * B_shared_dyn_local[23]));
      }
    }
  }
__asm__ __volatile__("cp.async.wait_group 1;");

  __syncthreads();
  for (int ax1_1_s_9 = 0; ax1_1_s_9 < 4; ++ax1_1_s_9) {
    if (ax1_1_s_9 < 2) {
      A_shared_dyn_local[(ax1_1_s_9 + 2)] = ((float*)buf_dyn_shmem)[((((((((((int)threadIdx.x) & 63) >> 5) * 32) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_9) + 576)];
    }
  }
  for (int ax1_0_9 = 0; ax1_0_9 < 3; ++ax1_0_9) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_9 * 4) + 12)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_9 * 4)) >> 6) * 64) + (((ax1_0_9 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_9 * 4)) >> 3)) & 7) * 4)) + 3200) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
  }
  for (int i_2_1_s_96 = 0; i_2_1_s_96 < 4; ++i_2_1_s_96) {
    if (i_2_1_s_96 < 2) {
      Y_local[(i_2_1_s_96 * 12)] = (Y_local[(i_2_1_s_96 * 12)] + (A_shared_dyn_local[i_2_1_s_96] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_97 = 0; i_2_1_s_97 < 4; ++i_2_1_s_97) {
    if (i_2_1_s_97 < 2) {
      Y_local[((i_2_1_s_97 * 12) + 1)] = (Y_local[((i_2_1_s_97 * 12) + 1)] + (A_shared_dyn_local[i_2_1_s_97] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_98 = 0; i_2_1_s_98 < 4; ++i_2_1_s_98) {
    if (i_2_1_s_98 < 2) {
      Y_local[((i_2_1_s_98 * 12) + 2)] = (Y_local[((i_2_1_s_98 * 12) + 2)] + (A_shared_dyn_local[i_2_1_s_98] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_99 = 0; i_2_1_s_99 < 4; ++i_2_1_s_99) {
    if (i_2_1_s_99 < 2) {
      Y_local[((i_2_1_s_99 * 12) + 3)] = (Y_local[((i_2_1_s_99 * 12) + 3)] + (A_shared_dyn_local[i_2_1_s_99] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_100 = 0; i_2_1_s_100 < 4; ++i_2_1_s_100) {
    if (i_2_1_s_100 < 2) {
      Y_local[((i_2_1_s_100 * 12) + 4)] = (Y_local[((i_2_1_s_100 * 12) + 4)] + (A_shared_dyn_local[i_2_1_s_100] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_101 = 0; i_2_1_s_101 < 4; ++i_2_1_s_101) {
    if (i_2_1_s_101 < 2) {
      Y_local[((i_2_1_s_101 * 12) + 5)] = (Y_local[((i_2_1_s_101 * 12) + 5)] + (A_shared_dyn_local[i_2_1_s_101] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_102 = 0; i_2_1_s_102 < 4; ++i_2_1_s_102) {
    if (i_2_1_s_102 < 2) {
      Y_local[((i_2_1_s_102 * 12) + 6)] = (Y_local[((i_2_1_s_102 * 12) + 6)] + (A_shared_dyn_local[i_2_1_s_102] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_103 = 0; i_2_1_s_103 < 4; ++i_2_1_s_103) {
    if (i_2_1_s_103 < 2) {
      Y_local[((i_2_1_s_103 * 12) + 7)] = (Y_local[((i_2_1_s_103 * 12) + 7)] + (A_shared_dyn_local[i_2_1_s_103] * B_shared_dyn_local[7]));
    }
  }
  for (int i_2_1_s_104 = 0; i_2_1_s_104 < 4; ++i_2_1_s_104) {
    if (i_2_1_s_104 < 2) {
      Y_local[((i_2_1_s_104 * 12) + 8)] = (Y_local[((i_2_1_s_104 * 12) + 8)] + (A_shared_dyn_local[i_2_1_s_104] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_105 = 0; i_2_1_s_105 < 4; ++i_2_1_s_105) {
    if (i_2_1_s_105 < 2) {
      Y_local[((i_2_1_s_105 * 12) + 9)] = (Y_local[((i_2_1_s_105 * 12) + 9)] + (A_shared_dyn_local[i_2_1_s_105] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_106 = 0; i_2_1_s_106 < 4; ++i_2_1_s_106) {
    if (i_2_1_s_106 < 2) {
      Y_local[((i_2_1_s_106 * 12) + 10)] = (Y_local[((i_2_1_s_106 * 12) + 10)] + (A_shared_dyn_local[i_2_1_s_106] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_107 = 0; i_2_1_s_107 < 4; ++i_2_1_s_107) {
    if (i_2_1_s_107 < 2) {
      Y_local[((i_2_1_s_107 * 12) + 11)] = (Y_local[((i_2_1_s_107 * 12) + 11)] + (A_shared_dyn_local[i_2_1_s_107] * B_shared_dyn_local[11]));
    }
  }
  for (int ax1_1_s_10 = 0; ax1_1_s_10 < 4; ++ax1_1_s_10) {
    if (ax1_1_s_10 < 2) {
      A_shared_dyn_local[ax1_1_s_10] = ((float*)buf_dyn_shmem)[((((((((((int)threadIdx.x) & 63) >> 5) * 32) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_10) + 640)];
    }
  }
  for (int ax1_0_10 = 0; ax1_0_10 < 3; ++ax1_0_10) {
    *(float4*)(B_shared_dyn_local + (ax1_0_10 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_10 * 4)) >> 6) * 64) + (((ax1_0_10 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_10 * 4)) >> 3)) & 7) * 4)) + 3328) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
  }
  for (int i_2_1_s_108 = 0; i_2_1_s_108 < 4; ++i_2_1_s_108) {
    if (i_2_1_s_108 < 2) {
      Y_local[(i_2_1_s_108 * 12)] = (Y_local[(i_2_1_s_108 * 12)] + (A_shared_dyn_local[(i_2_1_s_108 + 2)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_109 = 0; i_2_1_s_109 < 4; ++i_2_1_s_109) {
    if (i_2_1_s_109 < 2) {
      Y_local[((i_2_1_s_109 * 12) + 1)] = (Y_local[((i_2_1_s_109 * 12) + 1)] + (A_shared_dyn_local[(i_2_1_s_109 + 2)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_110 = 0; i_2_1_s_110 < 4; ++i_2_1_s_110) {
    if (i_2_1_s_110 < 2) {
      Y_local[((i_2_1_s_110 * 12) + 2)] = (Y_local[((i_2_1_s_110 * 12) + 2)] + (A_shared_dyn_local[(i_2_1_s_110 + 2)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_111 = 0; i_2_1_s_111 < 4; ++i_2_1_s_111) {
    if (i_2_1_s_111 < 2) {
      Y_local[((i_2_1_s_111 * 12) + 3)] = (Y_local[((i_2_1_s_111 * 12) + 3)] + (A_shared_dyn_local[(i_2_1_s_111 + 2)] * B_shared_dyn_local[15]));
    }
  }
  for (int i_2_1_s_112 = 0; i_2_1_s_112 < 4; ++i_2_1_s_112) {
    if (i_2_1_s_112 < 2) {
      Y_local[((i_2_1_s_112 * 12) + 4)] = (Y_local[((i_2_1_s_112 * 12) + 4)] + (A_shared_dyn_local[(i_2_1_s_112 + 2)] * B_shared_dyn_local[16]));
    }
  }
  for (int i_2_1_s_113 = 0; i_2_1_s_113 < 4; ++i_2_1_s_113) {
    if (i_2_1_s_113 < 2) {
      Y_local[((i_2_1_s_113 * 12) + 5)] = (Y_local[((i_2_1_s_113 * 12) + 5)] + (A_shared_dyn_local[(i_2_1_s_113 + 2)] * B_shared_dyn_local[17]));
    }
  }
  for (int i_2_1_s_114 = 0; i_2_1_s_114 < 4; ++i_2_1_s_114) {
    if (i_2_1_s_114 < 2) {
      Y_local[((i_2_1_s_114 * 12) + 6)] = (Y_local[((i_2_1_s_114 * 12) + 6)] + (A_shared_dyn_local[(i_2_1_s_114 + 2)] * B_shared_dyn_local[18]));
    }
  }
  for (int i_2_1_s_115 = 0; i_2_1_s_115 < 4; ++i_2_1_s_115) {
    if (i_2_1_s_115 < 2) {
      Y_local[((i_2_1_s_115 * 12) + 7)] = (Y_local[((i_2_1_s_115 * 12) + 7)] + (A_shared_dyn_local[(i_2_1_s_115 + 2)] * B_shared_dyn_local[19]));
    }
  }
  for (int i_2_1_s_116 = 0; i_2_1_s_116 < 4; ++i_2_1_s_116) {
    if (i_2_1_s_116 < 2) {
      Y_local[((i_2_1_s_116 * 12) + 8)] = (Y_local[((i_2_1_s_116 * 12) + 8)] + (A_shared_dyn_local[(i_2_1_s_116 + 2)] * B_shared_dyn_local[20]));
    }
  }
  for (int i_2_1_s_117 = 0; i_2_1_s_117 < 4; ++i_2_1_s_117) {
    if (i_2_1_s_117 < 2) {
      Y_local[((i_2_1_s_117 * 12) + 9)] = (Y_local[((i_2_1_s_117 * 12) + 9)] + (A_shared_dyn_local[(i_2_1_s_117 + 2)] * B_shared_dyn_local[21]));
    }
  }
  for (int i_2_1_s_118 = 0; i_2_1_s_118 < 4; ++i_2_1_s_118) {
    if (i_2_1_s_118 < 2) {
      Y_local[((i_2_1_s_118 * 12) + 10)] = (Y_local[((i_2_1_s_118 * 12) + 10)] + (A_shared_dyn_local[(i_2_1_s_118 + 2)] * B_shared_dyn_local[22]));
    }
  }
  for (int i_2_1_s_119 = 0; i_2_1_s_119 < 4; ++i_2_1_s_119) {
    if (i_2_1_s_119 < 2) {
      Y_local[((i_2_1_s_119 * 12) + 11)] = (Y_local[((i_2_1_s_119 * 12) + 11)] + (A_shared_dyn_local[(i_2_1_s_119 + 2)] * B_shared_dyn_local[23]));
    }
  }
  for (int ax1_1_s_11 = 0; ax1_1_s_11 < 4; ++ax1_1_s_11) {
    if (ax1_1_s_11 < 2) {
      A_shared_dyn_local[(ax1_1_s_11 + 2)] = ((float*)buf_dyn_shmem)[((((((((((int)threadIdx.x) & 63) >> 5) * 32) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_11) + 704)];
    }
  }
  for (int ax1_0_11 = 0; ax1_0_11 < 3; ++ax1_0_11) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_11 * 4) + 12)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_11 * 4)) >> 6) * 64) + (((ax1_0_11 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_11 * 4)) >> 3)) & 7) * 4)) + 3456) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
  }
  for (int i_2_1_s_120 = 0; i_2_1_s_120 < 4; ++i_2_1_s_120) {
    if (i_2_1_s_120 < 2) {
      Y_local[(i_2_1_s_120 * 12)] = (Y_local[(i_2_1_s_120 * 12)] + (A_shared_dyn_local[i_2_1_s_120] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_121 = 0; i_2_1_s_121 < 4; ++i_2_1_s_121) {
    if (i_2_1_s_121 < 2) {
      Y_local[((i_2_1_s_121 * 12) + 1)] = (Y_local[((i_2_1_s_121 * 12) + 1)] + (A_shared_dyn_local[i_2_1_s_121] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_122 = 0; i_2_1_s_122 < 4; ++i_2_1_s_122) {
    if (i_2_1_s_122 < 2) {
      Y_local[((i_2_1_s_122 * 12) + 2)] = (Y_local[((i_2_1_s_122 * 12) + 2)] + (A_shared_dyn_local[i_2_1_s_122] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_123 = 0; i_2_1_s_123 < 4; ++i_2_1_s_123) {
    if (i_2_1_s_123 < 2) {
      Y_local[((i_2_1_s_123 * 12) + 3)] = (Y_local[((i_2_1_s_123 * 12) + 3)] + (A_shared_dyn_local[i_2_1_s_123] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_124 = 0; i_2_1_s_124 < 4; ++i_2_1_s_124) {
    if (i_2_1_s_124 < 2) {
      Y_local[((i_2_1_s_124 * 12) + 4)] = (Y_local[((i_2_1_s_124 * 12) + 4)] + (A_shared_dyn_local[i_2_1_s_124] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_125 = 0; i_2_1_s_125 < 4; ++i_2_1_s_125) {
    if (i_2_1_s_125 < 2) {
      Y_local[((i_2_1_s_125 * 12) + 5)] = (Y_local[((i_2_1_s_125 * 12) + 5)] + (A_shared_dyn_local[i_2_1_s_125] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_126 = 0; i_2_1_s_126 < 4; ++i_2_1_s_126) {
    if (i_2_1_s_126 < 2) {
      Y_local[((i_2_1_s_126 * 12) + 6)] = (Y_local[((i_2_1_s_126 * 12) + 6)] + (A_shared_dyn_local[i_2_1_s_126] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_127 = 0; i_2_1_s_127 < 4; ++i_2_1_s_127) {
    if (i_2_1_s_127 < 2) {
      Y_local[((i_2_1_s_127 * 12) + 7)] = (Y_local[((i_2_1_s_127 * 12) + 7)] + (A_shared_dyn_local[i_2_1_s_127] * B_shared_dyn_local[7]));
    }
  }
  for (int i_2_1_s_128 = 0; i_2_1_s_128 < 4; ++i_2_1_s_128) {
    if (i_2_1_s_128 < 2) {
      Y_local[((i_2_1_s_128 * 12) + 8)] = (Y_local[((i_2_1_s_128 * 12) + 8)] + (A_shared_dyn_local[i_2_1_s_128] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_129 = 0; i_2_1_s_129 < 4; ++i_2_1_s_129) {
    if (i_2_1_s_129 < 2) {
      Y_local[((i_2_1_s_129 * 12) + 9)] = (Y_local[((i_2_1_s_129 * 12) + 9)] + (A_shared_dyn_local[i_2_1_s_129] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_130 = 0; i_2_1_s_130 < 4; ++i_2_1_s_130) {
    if (i_2_1_s_130 < 2) {
      Y_local[((i_2_1_s_130 * 12) + 10)] = (Y_local[((i_2_1_s_130 * 12) + 10)] + (A_shared_dyn_local[i_2_1_s_130] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_131 = 0; i_2_1_s_131 < 4; ++i_2_1_s_131) {
    if (i_2_1_s_131 < 2) {
      Y_local[((i_2_1_s_131 * 12) + 11)] = (Y_local[((i_2_1_s_131 * 12) + 11)] + (A_shared_dyn_local[i_2_1_s_131] * B_shared_dyn_local[11]));
    }
  }
  for (int ax1_1_s_12 = 0; ax1_1_s_12 < 4; ++ax1_1_s_12) {
    if (ax1_1_s_12 < 2) {
      A_shared_dyn_local[ax1_1_s_12] = ((float*)buf_dyn_shmem)[((((((((((int)threadIdx.x) & 63) >> 5) * 32) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_12) + 768)];
    }
  }
  for (int ax1_0_12 = 0; ax1_0_12 < 3; ++ax1_0_12) {
    *(float4*)(B_shared_dyn_local + (ax1_0_12 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_12 * 4)) >> 6) * 64) + (((ax1_0_12 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_12 * 4)) >> 3)) & 7) * 4)) + 3584) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
  }
  for (int i_2_1_s_132 = 0; i_2_1_s_132 < 4; ++i_2_1_s_132) {
    if (i_2_1_s_132 < 2) {
      Y_local[(i_2_1_s_132 * 12)] = (Y_local[(i_2_1_s_132 * 12)] + (A_shared_dyn_local[(i_2_1_s_132 + 2)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_133 = 0; i_2_1_s_133 < 4; ++i_2_1_s_133) {
    if (i_2_1_s_133 < 2) {
      Y_local[((i_2_1_s_133 * 12) + 1)] = (Y_local[((i_2_1_s_133 * 12) + 1)] + (A_shared_dyn_local[(i_2_1_s_133 + 2)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_134 = 0; i_2_1_s_134 < 4; ++i_2_1_s_134) {
    if (i_2_1_s_134 < 2) {
      Y_local[((i_2_1_s_134 * 12) + 2)] = (Y_local[((i_2_1_s_134 * 12) + 2)] + (A_shared_dyn_local[(i_2_1_s_134 + 2)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_135 = 0; i_2_1_s_135 < 4; ++i_2_1_s_135) {
    if (i_2_1_s_135 < 2) {
      Y_local[((i_2_1_s_135 * 12) + 3)] = (Y_local[((i_2_1_s_135 * 12) + 3)] + (A_shared_dyn_local[(i_2_1_s_135 + 2)] * B_shared_dyn_local[15]));
    }
  }
  for (int i_2_1_s_136 = 0; i_2_1_s_136 < 4; ++i_2_1_s_136) {
    if (i_2_1_s_136 < 2) {
      Y_local[((i_2_1_s_136 * 12) + 4)] = (Y_local[((i_2_1_s_136 * 12) + 4)] + (A_shared_dyn_local[(i_2_1_s_136 + 2)] * B_shared_dyn_local[16]));
    }
  }
  for (int i_2_1_s_137 = 0; i_2_1_s_137 < 4; ++i_2_1_s_137) {
    if (i_2_1_s_137 < 2) {
      Y_local[((i_2_1_s_137 * 12) + 5)] = (Y_local[((i_2_1_s_137 * 12) + 5)] + (A_shared_dyn_local[(i_2_1_s_137 + 2)] * B_shared_dyn_local[17]));
    }
  }
  for (int i_2_1_s_138 = 0; i_2_1_s_138 < 4; ++i_2_1_s_138) {
    if (i_2_1_s_138 < 2) {
      Y_local[((i_2_1_s_138 * 12) + 6)] = (Y_local[((i_2_1_s_138 * 12) + 6)] + (A_shared_dyn_local[(i_2_1_s_138 + 2)] * B_shared_dyn_local[18]));
    }
  }
  for (int i_2_1_s_139 = 0; i_2_1_s_139 < 4; ++i_2_1_s_139) {
    if (i_2_1_s_139 < 2) {
      Y_local[((i_2_1_s_139 * 12) + 7)] = (Y_local[((i_2_1_s_139 * 12) + 7)] + (A_shared_dyn_local[(i_2_1_s_139 + 2)] * B_shared_dyn_local[19]));
    }
  }
  for (int i_2_1_s_140 = 0; i_2_1_s_140 < 4; ++i_2_1_s_140) {
    if (i_2_1_s_140 < 2) {
      Y_local[((i_2_1_s_140 * 12) + 8)] = (Y_local[((i_2_1_s_140 * 12) + 8)] + (A_shared_dyn_local[(i_2_1_s_140 + 2)] * B_shared_dyn_local[20]));
    }
  }
  for (int i_2_1_s_141 = 0; i_2_1_s_141 < 4; ++i_2_1_s_141) {
    if (i_2_1_s_141 < 2) {
      Y_local[((i_2_1_s_141 * 12) + 9)] = (Y_local[((i_2_1_s_141 * 12) + 9)] + (A_shared_dyn_local[(i_2_1_s_141 + 2)] * B_shared_dyn_local[21]));
    }
  }
  for (int i_2_1_s_142 = 0; i_2_1_s_142 < 4; ++i_2_1_s_142) {
    if (i_2_1_s_142 < 2) {
      Y_local[((i_2_1_s_142 * 12) + 10)] = (Y_local[((i_2_1_s_142 * 12) + 10)] + (A_shared_dyn_local[(i_2_1_s_142 + 2)] * B_shared_dyn_local[22]));
    }
  }
  for (int i_2_1_s_143 = 0; i_2_1_s_143 < 4; ++i_2_1_s_143) {
    if (i_2_1_s_143 < 2) {
      Y_local[((i_2_1_s_143 * 12) + 11)] = (Y_local[((i_2_1_s_143 * 12) + 11)] + (A_shared_dyn_local[(i_2_1_s_143 + 2)] * B_shared_dyn_local[23]));
    }
  }
  for (int ax1_1_s_13 = 0; ax1_1_s_13 < 4; ++ax1_1_s_13) {
    if (ax1_1_s_13 < 2) {
      A_shared_dyn_local[(ax1_1_s_13 + 2)] = ((float*)buf_dyn_shmem)[((((((((((int)threadIdx.x) & 63) >> 5) * 32) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_13) + 832)];
    }
  }
  for (int ax1_0_13 = 0; ax1_0_13 < 3; ++ax1_0_13) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_13 * 4) + 12)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_13 * 4)) >> 6) * 64) + (((ax1_0_13 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_13 * 4)) >> 3)) & 7) * 4)) + 3712) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
  }
  for (int i_2_1_s_144 = 0; i_2_1_s_144 < 4; ++i_2_1_s_144) {
    if (i_2_1_s_144 < 2) {
      Y_local[(i_2_1_s_144 * 12)] = (Y_local[(i_2_1_s_144 * 12)] + (A_shared_dyn_local[i_2_1_s_144] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_145 = 0; i_2_1_s_145 < 4; ++i_2_1_s_145) {
    if (i_2_1_s_145 < 2) {
      Y_local[((i_2_1_s_145 * 12) + 1)] = (Y_local[((i_2_1_s_145 * 12) + 1)] + (A_shared_dyn_local[i_2_1_s_145] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_146 = 0; i_2_1_s_146 < 4; ++i_2_1_s_146) {
    if (i_2_1_s_146 < 2) {
      Y_local[((i_2_1_s_146 * 12) + 2)] = (Y_local[((i_2_1_s_146 * 12) + 2)] + (A_shared_dyn_local[i_2_1_s_146] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_147 = 0; i_2_1_s_147 < 4; ++i_2_1_s_147) {
    if (i_2_1_s_147 < 2) {
      Y_local[((i_2_1_s_147 * 12) + 3)] = (Y_local[((i_2_1_s_147 * 12) + 3)] + (A_shared_dyn_local[i_2_1_s_147] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_148 = 0; i_2_1_s_148 < 4; ++i_2_1_s_148) {
    if (i_2_1_s_148 < 2) {
      Y_local[((i_2_1_s_148 * 12) + 4)] = (Y_local[((i_2_1_s_148 * 12) + 4)] + (A_shared_dyn_local[i_2_1_s_148] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_149 = 0; i_2_1_s_149 < 4; ++i_2_1_s_149) {
    if (i_2_1_s_149 < 2) {
      Y_local[((i_2_1_s_149 * 12) + 5)] = (Y_local[((i_2_1_s_149 * 12) + 5)] + (A_shared_dyn_local[i_2_1_s_149] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_150 = 0; i_2_1_s_150 < 4; ++i_2_1_s_150) {
    if (i_2_1_s_150 < 2) {
      Y_local[((i_2_1_s_150 * 12) + 6)] = (Y_local[((i_2_1_s_150 * 12) + 6)] + (A_shared_dyn_local[i_2_1_s_150] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_151 = 0; i_2_1_s_151 < 4; ++i_2_1_s_151) {
    if (i_2_1_s_151 < 2) {
      Y_local[((i_2_1_s_151 * 12) + 7)] = (Y_local[((i_2_1_s_151 * 12) + 7)] + (A_shared_dyn_local[i_2_1_s_151] * B_shared_dyn_local[7]));
    }
  }
  for (int i_2_1_s_152 = 0; i_2_1_s_152 < 4; ++i_2_1_s_152) {
    if (i_2_1_s_152 < 2) {
      Y_local[((i_2_1_s_152 * 12) + 8)] = (Y_local[((i_2_1_s_152 * 12) + 8)] + (A_shared_dyn_local[i_2_1_s_152] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_153 = 0; i_2_1_s_153 < 4; ++i_2_1_s_153) {
    if (i_2_1_s_153 < 2) {
      Y_local[((i_2_1_s_153 * 12) + 9)] = (Y_local[((i_2_1_s_153 * 12) + 9)] + (A_shared_dyn_local[i_2_1_s_153] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_154 = 0; i_2_1_s_154 < 4; ++i_2_1_s_154) {
    if (i_2_1_s_154 < 2) {
      Y_local[((i_2_1_s_154 * 12) + 10)] = (Y_local[((i_2_1_s_154 * 12) + 10)] + (A_shared_dyn_local[i_2_1_s_154] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_155 = 0; i_2_1_s_155 < 4; ++i_2_1_s_155) {
    if (i_2_1_s_155 < 2) {
      Y_local[((i_2_1_s_155 * 12) + 11)] = (Y_local[((i_2_1_s_155 * 12) + 11)] + (A_shared_dyn_local[i_2_1_s_155] * B_shared_dyn_local[11]));
    }
  }
  for (int ax1_1_s_14 = 0; ax1_1_s_14 < 4; ++ax1_1_s_14) {
    if (ax1_1_s_14 < 2) {
      A_shared_dyn_local[ax1_1_s_14] = ((float*)buf_dyn_shmem)[((((((((((int)threadIdx.x) & 63) >> 5) * 32) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_14) + 896)];
    }
  }
  for (int ax1_0_14 = 0; ax1_0_14 < 3; ++ax1_0_14) {
    *(float4*)(B_shared_dyn_local + (ax1_0_14 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_14 * 4)) >> 6) * 64) + (((ax1_0_14 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_14 * 4)) >> 3)) & 7) * 4)) + 3840) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
  }
  for (int i_2_1_s_156 = 0; i_2_1_s_156 < 4; ++i_2_1_s_156) {
    if (i_2_1_s_156 < 2) {
      Y_local[(i_2_1_s_156 * 12)] = (Y_local[(i_2_1_s_156 * 12)] + (A_shared_dyn_local[(i_2_1_s_156 + 2)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_157 = 0; i_2_1_s_157 < 4; ++i_2_1_s_157) {
    if (i_2_1_s_157 < 2) {
      Y_local[((i_2_1_s_157 * 12) + 1)] = (Y_local[((i_2_1_s_157 * 12) + 1)] + (A_shared_dyn_local[(i_2_1_s_157 + 2)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_158 = 0; i_2_1_s_158 < 4; ++i_2_1_s_158) {
    if (i_2_1_s_158 < 2) {
      Y_local[((i_2_1_s_158 * 12) + 2)] = (Y_local[((i_2_1_s_158 * 12) + 2)] + (A_shared_dyn_local[(i_2_1_s_158 + 2)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_159 = 0; i_2_1_s_159 < 4; ++i_2_1_s_159) {
    if (i_2_1_s_159 < 2) {
      Y_local[((i_2_1_s_159 * 12) + 3)] = (Y_local[((i_2_1_s_159 * 12) + 3)] + (A_shared_dyn_local[(i_2_1_s_159 + 2)] * B_shared_dyn_local[15]));
    }
  }
  for (int i_2_1_s_160 = 0; i_2_1_s_160 < 4; ++i_2_1_s_160) {
    if (i_2_1_s_160 < 2) {
      Y_local[((i_2_1_s_160 * 12) + 4)] = (Y_local[((i_2_1_s_160 * 12) + 4)] + (A_shared_dyn_local[(i_2_1_s_160 + 2)] * B_shared_dyn_local[16]));
    }
  }
  for (int i_2_1_s_161 = 0; i_2_1_s_161 < 4; ++i_2_1_s_161) {
    if (i_2_1_s_161 < 2) {
      Y_local[((i_2_1_s_161 * 12) + 5)] = (Y_local[((i_2_1_s_161 * 12) + 5)] + (A_shared_dyn_local[(i_2_1_s_161 + 2)] * B_shared_dyn_local[17]));
    }
  }
  for (int i_2_1_s_162 = 0; i_2_1_s_162 < 4; ++i_2_1_s_162) {
    if (i_2_1_s_162 < 2) {
      Y_local[((i_2_1_s_162 * 12) + 6)] = (Y_local[((i_2_1_s_162 * 12) + 6)] + (A_shared_dyn_local[(i_2_1_s_162 + 2)] * B_shared_dyn_local[18]));
    }
  }
  for (int i_2_1_s_163 = 0; i_2_1_s_163 < 4; ++i_2_1_s_163) {
    if (i_2_1_s_163 < 2) {
      Y_local[((i_2_1_s_163 * 12) + 7)] = (Y_local[((i_2_1_s_163 * 12) + 7)] + (A_shared_dyn_local[(i_2_1_s_163 + 2)] * B_shared_dyn_local[19]));
    }
  }
  for (int i_2_1_s_164 = 0; i_2_1_s_164 < 4; ++i_2_1_s_164) {
    if (i_2_1_s_164 < 2) {
      Y_local[((i_2_1_s_164 * 12) + 8)] = (Y_local[((i_2_1_s_164 * 12) + 8)] + (A_shared_dyn_local[(i_2_1_s_164 + 2)] * B_shared_dyn_local[20]));
    }
  }
  for (int i_2_1_s_165 = 0; i_2_1_s_165 < 4; ++i_2_1_s_165) {
    if (i_2_1_s_165 < 2) {
      Y_local[((i_2_1_s_165 * 12) + 9)] = (Y_local[((i_2_1_s_165 * 12) + 9)] + (A_shared_dyn_local[(i_2_1_s_165 + 2)] * B_shared_dyn_local[21]));
    }
  }
  for (int i_2_1_s_166 = 0; i_2_1_s_166 < 4; ++i_2_1_s_166) {
    if (i_2_1_s_166 < 2) {
      Y_local[((i_2_1_s_166 * 12) + 10)] = (Y_local[((i_2_1_s_166 * 12) + 10)] + (A_shared_dyn_local[(i_2_1_s_166 + 2)] * B_shared_dyn_local[22]));
    }
  }
  for (int i_2_1_s_167 = 0; i_2_1_s_167 < 4; ++i_2_1_s_167) {
    if (i_2_1_s_167 < 2) {
      Y_local[((i_2_1_s_167 * 12) + 11)] = (Y_local[((i_2_1_s_167 * 12) + 11)] + (A_shared_dyn_local[(i_2_1_s_167 + 2)] * B_shared_dyn_local[23]));
    }
  }
  for (int ax1_1_s_15 = 0; ax1_1_s_15 < 4; ++ax1_1_s_15) {
    if (ax1_1_s_15 < 2) {
      A_shared_dyn_local[(ax1_1_s_15 + 2)] = ((float*)buf_dyn_shmem)[((((((((((int)threadIdx.x) & 63) >> 5) * 32) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_15) + 960)];
    }
  }
  for (int ax1_0_15 = 0; ax1_0_15 < 3; ++ax1_0_15) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_15 * 4) + 12)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_15 * 4)) >> 6) * 64) + (((ax1_0_15 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_15 * 4)) >> 3)) & 7) * 4)) + 3968) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
  }
  for (int i_2_1_s_168 = 0; i_2_1_s_168 < 4; ++i_2_1_s_168) {
    if (i_2_1_s_168 < 2) {
      Y_local[(i_2_1_s_168 * 12)] = (Y_local[(i_2_1_s_168 * 12)] + (A_shared_dyn_local[i_2_1_s_168] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_169 = 0; i_2_1_s_169 < 4; ++i_2_1_s_169) {
    if (i_2_1_s_169 < 2) {
      Y_local[((i_2_1_s_169 * 12) + 1)] = (Y_local[((i_2_1_s_169 * 12) + 1)] + (A_shared_dyn_local[i_2_1_s_169] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_170 = 0; i_2_1_s_170 < 4; ++i_2_1_s_170) {
    if (i_2_1_s_170 < 2) {
      Y_local[((i_2_1_s_170 * 12) + 2)] = (Y_local[((i_2_1_s_170 * 12) + 2)] + (A_shared_dyn_local[i_2_1_s_170] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_171 = 0; i_2_1_s_171 < 4; ++i_2_1_s_171) {
    if (i_2_1_s_171 < 2) {
      Y_local[((i_2_1_s_171 * 12) + 3)] = (Y_local[((i_2_1_s_171 * 12) + 3)] + (A_shared_dyn_local[i_2_1_s_171] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_172 = 0; i_2_1_s_172 < 4; ++i_2_1_s_172) {
    if (i_2_1_s_172 < 2) {
      Y_local[((i_2_1_s_172 * 12) + 4)] = (Y_local[((i_2_1_s_172 * 12) + 4)] + (A_shared_dyn_local[i_2_1_s_172] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_173 = 0; i_2_1_s_173 < 4; ++i_2_1_s_173) {
    if (i_2_1_s_173 < 2) {
      Y_local[((i_2_1_s_173 * 12) + 5)] = (Y_local[((i_2_1_s_173 * 12) + 5)] + (A_shared_dyn_local[i_2_1_s_173] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_174 = 0; i_2_1_s_174 < 4; ++i_2_1_s_174) {
    if (i_2_1_s_174 < 2) {
      Y_local[((i_2_1_s_174 * 12) + 6)] = (Y_local[((i_2_1_s_174 * 12) + 6)] + (A_shared_dyn_local[i_2_1_s_174] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_175 = 0; i_2_1_s_175 < 4; ++i_2_1_s_175) {
    if (i_2_1_s_175 < 2) {
      Y_local[((i_2_1_s_175 * 12) + 7)] = (Y_local[((i_2_1_s_175 * 12) + 7)] + (A_shared_dyn_local[i_2_1_s_175] * B_shared_dyn_local[7]));
    }
  }
  for (int i_2_1_s_176 = 0; i_2_1_s_176 < 4; ++i_2_1_s_176) {
    if (i_2_1_s_176 < 2) {
      Y_local[((i_2_1_s_176 * 12) + 8)] = (Y_local[((i_2_1_s_176 * 12) + 8)] + (A_shared_dyn_local[i_2_1_s_176] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_177 = 0; i_2_1_s_177 < 4; ++i_2_1_s_177) {
    if (i_2_1_s_177 < 2) {
      Y_local[((i_2_1_s_177 * 12) + 9)] = (Y_local[((i_2_1_s_177 * 12) + 9)] + (A_shared_dyn_local[i_2_1_s_177] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_178 = 0; i_2_1_s_178 < 4; ++i_2_1_s_178) {
    if (i_2_1_s_178 < 2) {
      Y_local[((i_2_1_s_178 * 12) + 10)] = (Y_local[((i_2_1_s_178 * 12) + 10)] + (A_shared_dyn_local[i_2_1_s_178] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_179 = 0; i_2_1_s_179 < 4; ++i_2_1_s_179) {
    if (i_2_1_s_179 < 2) {
      Y_local[((i_2_1_s_179 * 12) + 11)] = (Y_local[((i_2_1_s_179 * 12) + 11)] + (A_shared_dyn_local[i_2_1_s_179] * B_shared_dyn_local[11]));
    }
  }
  for (int ax1_1_s_16 = 0; ax1_1_s_16 < 4; ++ax1_1_s_16) {
    if (ax1_1_s_16 < 2) {
      A_shared_dyn_local[ax1_1_s_16] = ((float*)buf_dyn_shmem)[((((((((((int)threadIdx.x) & 63) >> 5) * 32) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_16) + 1024)];
    }
  }
  for (int ax1_0_16 = 0; ax1_0_16 < 3; ++ax1_0_16) {
    *(float4*)(B_shared_dyn_local + (ax1_0_16 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_16 * 4)) >> 6) * 64) + (((ax1_0_16 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_16 * 4)) >> 3)) & 7) * 4)) + 4096) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
  }
  for (int i_2_1_s_180 = 0; i_2_1_s_180 < 4; ++i_2_1_s_180) {
    if (i_2_1_s_180 < 2) {
      Y_local[(i_2_1_s_180 * 12)] = (Y_local[(i_2_1_s_180 * 12)] + (A_shared_dyn_local[(i_2_1_s_180 + 2)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_181 = 0; i_2_1_s_181 < 4; ++i_2_1_s_181) {
    if (i_2_1_s_181 < 2) {
      Y_local[((i_2_1_s_181 * 12) + 1)] = (Y_local[((i_2_1_s_181 * 12) + 1)] + (A_shared_dyn_local[(i_2_1_s_181 + 2)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_182 = 0; i_2_1_s_182 < 4; ++i_2_1_s_182) {
    if (i_2_1_s_182 < 2) {
      Y_local[((i_2_1_s_182 * 12) + 2)] = (Y_local[((i_2_1_s_182 * 12) + 2)] + (A_shared_dyn_local[(i_2_1_s_182 + 2)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_183 = 0; i_2_1_s_183 < 4; ++i_2_1_s_183) {
    if (i_2_1_s_183 < 2) {
      Y_local[((i_2_1_s_183 * 12) + 3)] = (Y_local[((i_2_1_s_183 * 12) + 3)] + (A_shared_dyn_local[(i_2_1_s_183 + 2)] * B_shared_dyn_local[15]));
    }
  }
  for (int i_2_1_s_184 = 0; i_2_1_s_184 < 4; ++i_2_1_s_184) {
    if (i_2_1_s_184 < 2) {
      Y_local[((i_2_1_s_184 * 12) + 4)] = (Y_local[((i_2_1_s_184 * 12) + 4)] + (A_shared_dyn_local[(i_2_1_s_184 + 2)] * B_shared_dyn_local[16]));
    }
  }
  for (int i_2_1_s_185 = 0; i_2_1_s_185 < 4; ++i_2_1_s_185) {
    if (i_2_1_s_185 < 2) {
      Y_local[((i_2_1_s_185 * 12) + 5)] = (Y_local[((i_2_1_s_185 * 12) + 5)] + (A_shared_dyn_local[(i_2_1_s_185 + 2)] * B_shared_dyn_local[17]));
    }
  }
  for (int i_2_1_s_186 = 0; i_2_1_s_186 < 4; ++i_2_1_s_186) {
    if (i_2_1_s_186 < 2) {
      Y_local[((i_2_1_s_186 * 12) + 6)] = (Y_local[((i_2_1_s_186 * 12) + 6)] + (A_shared_dyn_local[(i_2_1_s_186 + 2)] * B_shared_dyn_local[18]));
    }
  }
  for (int i_2_1_s_187 = 0; i_2_1_s_187 < 4; ++i_2_1_s_187) {
    if (i_2_1_s_187 < 2) {
      Y_local[((i_2_1_s_187 * 12) + 7)] = (Y_local[((i_2_1_s_187 * 12) + 7)] + (A_shared_dyn_local[(i_2_1_s_187 + 2)] * B_shared_dyn_local[19]));
    }
  }
  for (int i_2_1_s_188 = 0; i_2_1_s_188 < 4; ++i_2_1_s_188) {
    if (i_2_1_s_188 < 2) {
      Y_local[((i_2_1_s_188 * 12) + 8)] = (Y_local[((i_2_1_s_188 * 12) + 8)] + (A_shared_dyn_local[(i_2_1_s_188 + 2)] * B_shared_dyn_local[20]));
    }
  }
  for (int i_2_1_s_189 = 0; i_2_1_s_189 < 4; ++i_2_1_s_189) {
    if (i_2_1_s_189 < 2) {
      Y_local[((i_2_1_s_189 * 12) + 9)] = (Y_local[((i_2_1_s_189 * 12) + 9)] + (A_shared_dyn_local[(i_2_1_s_189 + 2)] * B_shared_dyn_local[21]));
    }
  }
  for (int i_2_1_s_190 = 0; i_2_1_s_190 < 4; ++i_2_1_s_190) {
    if (i_2_1_s_190 < 2) {
      Y_local[((i_2_1_s_190 * 12) + 10)] = (Y_local[((i_2_1_s_190 * 12) + 10)] + (A_shared_dyn_local[(i_2_1_s_190 + 2)] * B_shared_dyn_local[22]));
    }
  }
  for (int i_2_1_s_191 = 0; i_2_1_s_191 < 4; ++i_2_1_s_191) {
    if (i_2_1_s_191 < 2) {
      Y_local[((i_2_1_s_191 * 12) + 11)] = (Y_local[((i_2_1_s_191 * 12) + 11)] + (A_shared_dyn_local[(i_2_1_s_191 + 2)] * B_shared_dyn_local[23]));
    }
  }
__asm__ __volatile__("cp.async.wait_group 0;");

  __syncthreads();
  for (int ax1_1_s_17 = 0; ax1_1_s_17 < 4; ++ax1_1_s_17) {
    if (ax1_1_s_17 < 2) {
      A_shared_dyn_local[(ax1_1_s_17 + 2)] = ((float*)buf_dyn_shmem)[((((((((((int)threadIdx.x) & 63) >> 5) * 32) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_17) + 1088)];
    }
  }
  for (int ax1_0_17 = 0; ax1_0_17 < 3; ++ax1_0_17) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_17 * 4) + 12)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_17 * 4)) >> 6) * 64) + (((ax1_0_17 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_17 * 4)) >> 3)) & 7) * 4)) + 4224) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
  }
  for (int i_2_1_s_192 = 0; i_2_1_s_192 < 4; ++i_2_1_s_192) {
    if (i_2_1_s_192 < 2) {
      Y_local[(i_2_1_s_192 * 12)] = (Y_local[(i_2_1_s_192 * 12)] + (A_shared_dyn_local[i_2_1_s_192] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_193 = 0; i_2_1_s_193 < 4; ++i_2_1_s_193) {
    if (i_2_1_s_193 < 2) {
      Y_local[((i_2_1_s_193 * 12) + 1)] = (Y_local[((i_2_1_s_193 * 12) + 1)] + (A_shared_dyn_local[i_2_1_s_193] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_194 = 0; i_2_1_s_194 < 4; ++i_2_1_s_194) {
    if (i_2_1_s_194 < 2) {
      Y_local[((i_2_1_s_194 * 12) + 2)] = (Y_local[((i_2_1_s_194 * 12) + 2)] + (A_shared_dyn_local[i_2_1_s_194] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_195 = 0; i_2_1_s_195 < 4; ++i_2_1_s_195) {
    if (i_2_1_s_195 < 2) {
      Y_local[((i_2_1_s_195 * 12) + 3)] = (Y_local[((i_2_1_s_195 * 12) + 3)] + (A_shared_dyn_local[i_2_1_s_195] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_196 = 0; i_2_1_s_196 < 4; ++i_2_1_s_196) {
    if (i_2_1_s_196 < 2) {
      Y_local[((i_2_1_s_196 * 12) + 4)] = (Y_local[((i_2_1_s_196 * 12) + 4)] + (A_shared_dyn_local[i_2_1_s_196] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_197 = 0; i_2_1_s_197 < 4; ++i_2_1_s_197) {
    if (i_2_1_s_197 < 2) {
      Y_local[((i_2_1_s_197 * 12) + 5)] = (Y_local[((i_2_1_s_197 * 12) + 5)] + (A_shared_dyn_local[i_2_1_s_197] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_198 = 0; i_2_1_s_198 < 4; ++i_2_1_s_198) {
    if (i_2_1_s_198 < 2) {
      Y_local[((i_2_1_s_198 * 12) + 6)] = (Y_local[((i_2_1_s_198 * 12) + 6)] + (A_shared_dyn_local[i_2_1_s_198] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_199 = 0; i_2_1_s_199 < 4; ++i_2_1_s_199) {
    if (i_2_1_s_199 < 2) {
      Y_local[((i_2_1_s_199 * 12) + 7)] = (Y_local[((i_2_1_s_199 * 12) + 7)] + (A_shared_dyn_local[i_2_1_s_199] * B_shared_dyn_local[7]));
    }
  }
  for (int i_2_1_s_200 = 0; i_2_1_s_200 < 4; ++i_2_1_s_200) {
    if (i_2_1_s_200 < 2) {
      Y_local[((i_2_1_s_200 * 12) + 8)] = (Y_local[((i_2_1_s_200 * 12) + 8)] + (A_shared_dyn_local[i_2_1_s_200] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_201 = 0; i_2_1_s_201 < 4; ++i_2_1_s_201) {
    if (i_2_1_s_201 < 2) {
      Y_local[((i_2_1_s_201 * 12) + 9)] = (Y_local[((i_2_1_s_201 * 12) + 9)] + (A_shared_dyn_local[i_2_1_s_201] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_202 = 0; i_2_1_s_202 < 4; ++i_2_1_s_202) {
    if (i_2_1_s_202 < 2) {
      Y_local[((i_2_1_s_202 * 12) + 10)] = (Y_local[((i_2_1_s_202 * 12) + 10)] + (A_shared_dyn_local[i_2_1_s_202] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_203 = 0; i_2_1_s_203 < 4; ++i_2_1_s_203) {
    if (i_2_1_s_203 < 2) {
      Y_local[((i_2_1_s_203 * 12) + 11)] = (Y_local[((i_2_1_s_203 * 12) + 11)] + (A_shared_dyn_local[i_2_1_s_203] * B_shared_dyn_local[11]));
    }
  }
  for (int ax1_1_s_18 = 0; ax1_1_s_18 < 4; ++ax1_1_s_18) {
    if (ax1_1_s_18 < 2) {
      A_shared_dyn_local[ax1_1_s_18] = ((float*)buf_dyn_shmem)[((((((((((int)threadIdx.x) & 63) >> 5) * 32) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_18) + 1152)];
    }
  }
  for (int ax1_0_18 = 0; ax1_0_18 < 3; ++ax1_0_18) {
    *(float4*)(B_shared_dyn_local + (ax1_0_18 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_18 * 4)) >> 6) * 64) + (((ax1_0_18 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_18 * 4)) >> 3)) & 7) * 4)) + 4352) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
  }
  for (int i_2_1_s_204 = 0; i_2_1_s_204 < 4; ++i_2_1_s_204) {
    if (i_2_1_s_204 < 2) {
      Y_local[(i_2_1_s_204 * 12)] = (Y_local[(i_2_1_s_204 * 12)] + (A_shared_dyn_local[(i_2_1_s_204 + 2)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_205 = 0; i_2_1_s_205 < 4; ++i_2_1_s_205) {
    if (i_2_1_s_205 < 2) {
      Y_local[((i_2_1_s_205 * 12) + 1)] = (Y_local[((i_2_1_s_205 * 12) + 1)] + (A_shared_dyn_local[(i_2_1_s_205 + 2)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_206 = 0; i_2_1_s_206 < 4; ++i_2_1_s_206) {
    if (i_2_1_s_206 < 2) {
      Y_local[((i_2_1_s_206 * 12) + 2)] = (Y_local[((i_2_1_s_206 * 12) + 2)] + (A_shared_dyn_local[(i_2_1_s_206 + 2)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_207 = 0; i_2_1_s_207 < 4; ++i_2_1_s_207) {
    if (i_2_1_s_207 < 2) {
      Y_local[((i_2_1_s_207 * 12) + 3)] = (Y_local[((i_2_1_s_207 * 12) + 3)] + (A_shared_dyn_local[(i_2_1_s_207 + 2)] * B_shared_dyn_local[15]));
    }
  }
  for (int i_2_1_s_208 = 0; i_2_1_s_208 < 4; ++i_2_1_s_208) {
    if (i_2_1_s_208 < 2) {
      Y_local[((i_2_1_s_208 * 12) + 4)] = (Y_local[((i_2_1_s_208 * 12) + 4)] + (A_shared_dyn_local[(i_2_1_s_208 + 2)] * B_shared_dyn_local[16]));
    }
  }
  for (int i_2_1_s_209 = 0; i_2_1_s_209 < 4; ++i_2_1_s_209) {
    if (i_2_1_s_209 < 2) {
      Y_local[((i_2_1_s_209 * 12) + 5)] = (Y_local[((i_2_1_s_209 * 12) + 5)] + (A_shared_dyn_local[(i_2_1_s_209 + 2)] * B_shared_dyn_local[17]));
    }
  }
  for (int i_2_1_s_210 = 0; i_2_1_s_210 < 4; ++i_2_1_s_210) {
    if (i_2_1_s_210 < 2) {
      Y_local[((i_2_1_s_210 * 12) + 6)] = (Y_local[((i_2_1_s_210 * 12) + 6)] + (A_shared_dyn_local[(i_2_1_s_210 + 2)] * B_shared_dyn_local[18]));
    }
  }
  for (int i_2_1_s_211 = 0; i_2_1_s_211 < 4; ++i_2_1_s_211) {
    if (i_2_1_s_211 < 2) {
      Y_local[((i_2_1_s_211 * 12) + 7)] = (Y_local[((i_2_1_s_211 * 12) + 7)] + (A_shared_dyn_local[(i_2_1_s_211 + 2)] * B_shared_dyn_local[19]));
    }
  }
  for (int i_2_1_s_212 = 0; i_2_1_s_212 < 4; ++i_2_1_s_212) {
    if (i_2_1_s_212 < 2) {
      Y_local[((i_2_1_s_212 * 12) + 8)] = (Y_local[((i_2_1_s_212 * 12) + 8)] + (A_shared_dyn_local[(i_2_1_s_212 + 2)] * B_shared_dyn_local[20]));
    }
  }
  for (int i_2_1_s_213 = 0; i_2_1_s_213 < 4; ++i_2_1_s_213) {
    if (i_2_1_s_213 < 2) {
      Y_local[((i_2_1_s_213 * 12) + 9)] = (Y_local[((i_2_1_s_213 * 12) + 9)] + (A_shared_dyn_local[(i_2_1_s_213 + 2)] * B_shared_dyn_local[21]));
    }
  }
  for (int i_2_1_s_214 = 0; i_2_1_s_214 < 4; ++i_2_1_s_214) {
    if (i_2_1_s_214 < 2) {
      Y_local[((i_2_1_s_214 * 12) + 10)] = (Y_local[((i_2_1_s_214 * 12) + 10)] + (A_shared_dyn_local[(i_2_1_s_214 + 2)] * B_shared_dyn_local[22]));
    }
  }
  for (int i_2_1_s_215 = 0; i_2_1_s_215 < 4; ++i_2_1_s_215) {
    if (i_2_1_s_215 < 2) {
      Y_local[((i_2_1_s_215 * 12) + 11)] = (Y_local[((i_2_1_s_215 * 12) + 11)] + (A_shared_dyn_local[(i_2_1_s_215 + 2)] * B_shared_dyn_local[23]));
    }
  }
  for (int ax1_1_s_19 = 0; ax1_1_s_19 < 4; ++ax1_1_s_19) {
    if (ax1_1_s_19 < 2) {
      A_shared_dyn_local[(ax1_1_s_19 + 2)] = ((float*)buf_dyn_shmem)[((((((((((int)threadIdx.x) & 63) >> 5) * 32) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_19) + 1216)];
    }
  }
  for (int ax1_0_19 = 0; ax1_0_19 < 3; ++ax1_0_19) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_19 * 4) + 12)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_19 * 4)) >> 6) * 64) + (((ax1_0_19 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_19 * 4)) >> 3)) & 7) * 4)) + 4480) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
  }
  for (int i_2_1_s_216 = 0; i_2_1_s_216 < 4; ++i_2_1_s_216) {
    if (i_2_1_s_216 < 2) {
      Y_local[(i_2_1_s_216 * 12)] = (Y_local[(i_2_1_s_216 * 12)] + (A_shared_dyn_local[i_2_1_s_216] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_217 = 0; i_2_1_s_217 < 4; ++i_2_1_s_217) {
    if (i_2_1_s_217 < 2) {
      Y_local[((i_2_1_s_217 * 12) + 1)] = (Y_local[((i_2_1_s_217 * 12) + 1)] + (A_shared_dyn_local[i_2_1_s_217] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_218 = 0; i_2_1_s_218 < 4; ++i_2_1_s_218) {
    if (i_2_1_s_218 < 2) {
      Y_local[((i_2_1_s_218 * 12) + 2)] = (Y_local[((i_2_1_s_218 * 12) + 2)] + (A_shared_dyn_local[i_2_1_s_218] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_219 = 0; i_2_1_s_219 < 4; ++i_2_1_s_219) {
    if (i_2_1_s_219 < 2) {
      Y_local[((i_2_1_s_219 * 12) + 3)] = (Y_local[((i_2_1_s_219 * 12) + 3)] + (A_shared_dyn_local[i_2_1_s_219] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_220 = 0; i_2_1_s_220 < 4; ++i_2_1_s_220) {
    if (i_2_1_s_220 < 2) {
      Y_local[((i_2_1_s_220 * 12) + 4)] = (Y_local[((i_2_1_s_220 * 12) + 4)] + (A_shared_dyn_local[i_2_1_s_220] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_221 = 0; i_2_1_s_221 < 4; ++i_2_1_s_221) {
    if (i_2_1_s_221 < 2) {
      Y_local[((i_2_1_s_221 * 12) + 5)] = (Y_local[((i_2_1_s_221 * 12) + 5)] + (A_shared_dyn_local[i_2_1_s_221] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_222 = 0; i_2_1_s_222 < 4; ++i_2_1_s_222) {
    if (i_2_1_s_222 < 2) {
      Y_local[((i_2_1_s_222 * 12) + 6)] = (Y_local[((i_2_1_s_222 * 12) + 6)] + (A_shared_dyn_local[i_2_1_s_222] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_223 = 0; i_2_1_s_223 < 4; ++i_2_1_s_223) {
    if (i_2_1_s_223 < 2) {
      Y_local[((i_2_1_s_223 * 12) + 7)] = (Y_local[((i_2_1_s_223 * 12) + 7)] + (A_shared_dyn_local[i_2_1_s_223] * B_shared_dyn_local[7]));
    }
  }
  for (int i_2_1_s_224 = 0; i_2_1_s_224 < 4; ++i_2_1_s_224) {
    if (i_2_1_s_224 < 2) {
      Y_local[((i_2_1_s_224 * 12) + 8)] = (Y_local[((i_2_1_s_224 * 12) + 8)] + (A_shared_dyn_local[i_2_1_s_224] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_225 = 0; i_2_1_s_225 < 4; ++i_2_1_s_225) {
    if (i_2_1_s_225 < 2) {
      Y_local[((i_2_1_s_225 * 12) + 9)] = (Y_local[((i_2_1_s_225 * 12) + 9)] + (A_shared_dyn_local[i_2_1_s_225] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_226 = 0; i_2_1_s_226 < 4; ++i_2_1_s_226) {
    if (i_2_1_s_226 < 2) {
      Y_local[((i_2_1_s_226 * 12) + 10)] = (Y_local[((i_2_1_s_226 * 12) + 10)] + (A_shared_dyn_local[i_2_1_s_226] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_227 = 0; i_2_1_s_227 < 4; ++i_2_1_s_227) {
    if (i_2_1_s_227 < 2) {
      Y_local[((i_2_1_s_227 * 12) + 11)] = (Y_local[((i_2_1_s_227 * 12) + 11)] + (A_shared_dyn_local[i_2_1_s_227] * B_shared_dyn_local[11]));
    }
  }
  for (int ax1_1_s_20 = 0; ax1_1_s_20 < 4; ++ax1_1_s_20) {
    if (ax1_1_s_20 < 2) {
      A_shared_dyn_local[ax1_1_s_20] = ((float*)buf_dyn_shmem)[((((((((((int)threadIdx.x) & 63) >> 5) * 32) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_20) + 1280)];
    }
  }
  for (int ax1_0_20 = 0; ax1_0_20 < 3; ++ax1_0_20) {
    *(float4*)(B_shared_dyn_local + (ax1_0_20 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_20 * 4)) >> 6) * 64) + (((ax1_0_20 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_20 * 4)) >> 3)) & 7) * 4)) + 4608) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
  }
  for (int i_2_1_s_228 = 0; i_2_1_s_228 < 4; ++i_2_1_s_228) {
    if (i_2_1_s_228 < 2) {
      Y_local[(i_2_1_s_228 * 12)] = (Y_local[(i_2_1_s_228 * 12)] + (A_shared_dyn_local[(i_2_1_s_228 + 2)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_229 = 0; i_2_1_s_229 < 4; ++i_2_1_s_229) {
    if (i_2_1_s_229 < 2) {
      Y_local[((i_2_1_s_229 * 12) + 1)] = (Y_local[((i_2_1_s_229 * 12) + 1)] + (A_shared_dyn_local[(i_2_1_s_229 + 2)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_230 = 0; i_2_1_s_230 < 4; ++i_2_1_s_230) {
    if (i_2_1_s_230 < 2) {
      Y_local[((i_2_1_s_230 * 12) + 2)] = (Y_local[((i_2_1_s_230 * 12) + 2)] + (A_shared_dyn_local[(i_2_1_s_230 + 2)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_231 = 0; i_2_1_s_231 < 4; ++i_2_1_s_231) {
    if (i_2_1_s_231 < 2) {
      Y_local[((i_2_1_s_231 * 12) + 3)] = (Y_local[((i_2_1_s_231 * 12) + 3)] + (A_shared_dyn_local[(i_2_1_s_231 + 2)] * B_shared_dyn_local[15]));
    }
  }
  for (int i_2_1_s_232 = 0; i_2_1_s_232 < 4; ++i_2_1_s_232) {
    if (i_2_1_s_232 < 2) {
      Y_local[((i_2_1_s_232 * 12) + 4)] = (Y_local[((i_2_1_s_232 * 12) + 4)] + (A_shared_dyn_local[(i_2_1_s_232 + 2)] * B_shared_dyn_local[16]));
    }
  }
  for (int i_2_1_s_233 = 0; i_2_1_s_233 < 4; ++i_2_1_s_233) {
    if (i_2_1_s_233 < 2) {
      Y_local[((i_2_1_s_233 * 12) + 5)] = (Y_local[((i_2_1_s_233 * 12) + 5)] + (A_shared_dyn_local[(i_2_1_s_233 + 2)] * B_shared_dyn_local[17]));
    }
  }
  for (int i_2_1_s_234 = 0; i_2_1_s_234 < 4; ++i_2_1_s_234) {
    if (i_2_1_s_234 < 2) {
      Y_local[((i_2_1_s_234 * 12) + 6)] = (Y_local[((i_2_1_s_234 * 12) + 6)] + (A_shared_dyn_local[(i_2_1_s_234 + 2)] * B_shared_dyn_local[18]));
    }
  }
  for (int i_2_1_s_235 = 0; i_2_1_s_235 < 4; ++i_2_1_s_235) {
    if (i_2_1_s_235 < 2) {
      Y_local[((i_2_1_s_235 * 12) + 7)] = (Y_local[((i_2_1_s_235 * 12) + 7)] + (A_shared_dyn_local[(i_2_1_s_235 + 2)] * B_shared_dyn_local[19]));
    }
  }
  for (int i_2_1_s_236 = 0; i_2_1_s_236 < 4; ++i_2_1_s_236) {
    if (i_2_1_s_236 < 2) {
      Y_local[((i_2_1_s_236 * 12) + 8)] = (Y_local[((i_2_1_s_236 * 12) + 8)] + (A_shared_dyn_local[(i_2_1_s_236 + 2)] * B_shared_dyn_local[20]));
    }
  }
  for (int i_2_1_s_237 = 0; i_2_1_s_237 < 4; ++i_2_1_s_237) {
    if (i_2_1_s_237 < 2) {
      Y_local[((i_2_1_s_237 * 12) + 9)] = (Y_local[((i_2_1_s_237 * 12) + 9)] + (A_shared_dyn_local[(i_2_1_s_237 + 2)] * B_shared_dyn_local[21]));
    }
  }
  for (int i_2_1_s_238 = 0; i_2_1_s_238 < 4; ++i_2_1_s_238) {
    if (i_2_1_s_238 < 2) {
      Y_local[((i_2_1_s_238 * 12) + 10)] = (Y_local[((i_2_1_s_238 * 12) + 10)] + (A_shared_dyn_local[(i_2_1_s_238 + 2)] * B_shared_dyn_local[22]));
    }
  }
  for (int i_2_1_s_239 = 0; i_2_1_s_239 < 4; ++i_2_1_s_239) {
    if (i_2_1_s_239 < 2) {
      Y_local[((i_2_1_s_239 * 12) + 11)] = (Y_local[((i_2_1_s_239 * 12) + 11)] + (A_shared_dyn_local[(i_2_1_s_239 + 2)] * B_shared_dyn_local[23]));
    }
  }
  for (int ax1_1_s_21 = 0; ax1_1_s_21 < 4; ++ax1_1_s_21) {
    if (ax1_1_s_21 < 2) {
      A_shared_dyn_local[(ax1_1_s_21 + 2)] = ((float*)buf_dyn_shmem)[((((((((((int)threadIdx.x) & 63) >> 5) * 32) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_21) + 1344)];
    }
  }
  for (int ax1_0_21 = 0; ax1_0_21 < 3; ++ax1_0_21) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_21 * 4) + 12)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_21 * 4)) >> 6) * 64) + (((ax1_0_21 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_21 * 4)) >> 3)) & 7) * 4)) + 4736) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
  }
  for (int i_2_1_s_240 = 0; i_2_1_s_240 < 4; ++i_2_1_s_240) {
    if (i_2_1_s_240 < 2) {
      Y_local[(i_2_1_s_240 * 12)] = (Y_local[(i_2_1_s_240 * 12)] + (A_shared_dyn_local[i_2_1_s_240] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_241 = 0; i_2_1_s_241 < 4; ++i_2_1_s_241) {
    if (i_2_1_s_241 < 2) {
      Y_local[((i_2_1_s_241 * 12) + 1)] = (Y_local[((i_2_1_s_241 * 12) + 1)] + (A_shared_dyn_local[i_2_1_s_241] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_242 = 0; i_2_1_s_242 < 4; ++i_2_1_s_242) {
    if (i_2_1_s_242 < 2) {
      Y_local[((i_2_1_s_242 * 12) + 2)] = (Y_local[((i_2_1_s_242 * 12) + 2)] + (A_shared_dyn_local[i_2_1_s_242] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_243 = 0; i_2_1_s_243 < 4; ++i_2_1_s_243) {
    if (i_2_1_s_243 < 2) {
      Y_local[((i_2_1_s_243 * 12) + 3)] = (Y_local[((i_2_1_s_243 * 12) + 3)] + (A_shared_dyn_local[i_2_1_s_243] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_244 = 0; i_2_1_s_244 < 4; ++i_2_1_s_244) {
    if (i_2_1_s_244 < 2) {
      Y_local[((i_2_1_s_244 * 12) + 4)] = (Y_local[((i_2_1_s_244 * 12) + 4)] + (A_shared_dyn_local[i_2_1_s_244] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_245 = 0; i_2_1_s_245 < 4; ++i_2_1_s_245) {
    if (i_2_1_s_245 < 2) {
      Y_local[((i_2_1_s_245 * 12) + 5)] = (Y_local[((i_2_1_s_245 * 12) + 5)] + (A_shared_dyn_local[i_2_1_s_245] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_246 = 0; i_2_1_s_246 < 4; ++i_2_1_s_246) {
    if (i_2_1_s_246 < 2) {
      Y_local[((i_2_1_s_246 * 12) + 6)] = (Y_local[((i_2_1_s_246 * 12) + 6)] + (A_shared_dyn_local[i_2_1_s_246] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_247 = 0; i_2_1_s_247 < 4; ++i_2_1_s_247) {
    if (i_2_1_s_247 < 2) {
      Y_local[((i_2_1_s_247 * 12) + 7)] = (Y_local[((i_2_1_s_247 * 12) + 7)] + (A_shared_dyn_local[i_2_1_s_247] * B_shared_dyn_local[7]));
    }
  }
  for (int i_2_1_s_248 = 0; i_2_1_s_248 < 4; ++i_2_1_s_248) {
    if (i_2_1_s_248 < 2) {
      Y_local[((i_2_1_s_248 * 12) + 8)] = (Y_local[((i_2_1_s_248 * 12) + 8)] + (A_shared_dyn_local[i_2_1_s_248] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_249 = 0; i_2_1_s_249 < 4; ++i_2_1_s_249) {
    if (i_2_1_s_249 < 2) {
      Y_local[((i_2_1_s_249 * 12) + 9)] = (Y_local[((i_2_1_s_249 * 12) + 9)] + (A_shared_dyn_local[i_2_1_s_249] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_250 = 0; i_2_1_s_250 < 4; ++i_2_1_s_250) {
    if (i_2_1_s_250 < 2) {
      Y_local[((i_2_1_s_250 * 12) + 10)] = (Y_local[((i_2_1_s_250 * 12) + 10)] + (A_shared_dyn_local[i_2_1_s_250] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_251 = 0; i_2_1_s_251 < 4; ++i_2_1_s_251) {
    if (i_2_1_s_251 < 2) {
      Y_local[((i_2_1_s_251 * 12) + 11)] = (Y_local[((i_2_1_s_251 * 12) + 11)] + (A_shared_dyn_local[i_2_1_s_251] * B_shared_dyn_local[11]));
    }
  }
  for (int ax1_1_s_22 = 0; ax1_1_s_22 < 4; ++ax1_1_s_22) {
    if (ax1_1_s_22 < 2) {
      A_shared_dyn_local[ax1_1_s_22] = ((float*)buf_dyn_shmem)[((((((((((int)threadIdx.x) & 63) >> 5) * 32) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_22) + 1408)];
    }
  }
  for (int ax1_0_22 = 0; ax1_0_22 < 3; ++ax1_0_22) {
    *(float4*)(B_shared_dyn_local + (ax1_0_22 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_22 * 4)) >> 6) * 64) + (((ax1_0_22 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_22 * 4)) >> 3)) & 7) * 4)) + 4864) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
  }
  for (int i_2_1_s_252 = 0; i_2_1_s_252 < 4; ++i_2_1_s_252) {
    if (i_2_1_s_252 < 2) {
      Y_local[(i_2_1_s_252 * 12)] = (Y_local[(i_2_1_s_252 * 12)] + (A_shared_dyn_local[(i_2_1_s_252 + 2)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_253 = 0; i_2_1_s_253 < 4; ++i_2_1_s_253) {
    if (i_2_1_s_253 < 2) {
      Y_local[((i_2_1_s_253 * 12) + 1)] = (Y_local[((i_2_1_s_253 * 12) + 1)] + (A_shared_dyn_local[(i_2_1_s_253 + 2)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_254 = 0; i_2_1_s_254 < 4; ++i_2_1_s_254) {
    if (i_2_1_s_254 < 2) {
      Y_local[((i_2_1_s_254 * 12) + 2)] = (Y_local[((i_2_1_s_254 * 12) + 2)] + (A_shared_dyn_local[(i_2_1_s_254 + 2)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_255 = 0; i_2_1_s_255 < 4; ++i_2_1_s_255) {
    if (i_2_1_s_255 < 2) {
      Y_local[((i_2_1_s_255 * 12) + 3)] = (Y_local[((i_2_1_s_255 * 12) + 3)] + (A_shared_dyn_local[(i_2_1_s_255 + 2)] * B_shared_dyn_local[15]));
    }
  }
  for (int i_2_1_s_256 = 0; i_2_1_s_256 < 4; ++i_2_1_s_256) {
    if (i_2_1_s_256 < 2) {
      Y_local[((i_2_1_s_256 * 12) + 4)] = (Y_local[((i_2_1_s_256 * 12) + 4)] + (A_shared_dyn_local[(i_2_1_s_256 + 2)] * B_shared_dyn_local[16]));
    }
  }
  for (int i_2_1_s_257 = 0; i_2_1_s_257 < 4; ++i_2_1_s_257) {
    if (i_2_1_s_257 < 2) {
      Y_local[((i_2_1_s_257 * 12) + 5)] = (Y_local[((i_2_1_s_257 * 12) + 5)] + (A_shared_dyn_local[(i_2_1_s_257 + 2)] * B_shared_dyn_local[17]));
    }
  }
  for (int i_2_1_s_258 = 0; i_2_1_s_258 < 4; ++i_2_1_s_258) {
    if (i_2_1_s_258 < 2) {
      Y_local[((i_2_1_s_258 * 12) + 6)] = (Y_local[((i_2_1_s_258 * 12) + 6)] + (A_shared_dyn_local[(i_2_1_s_258 + 2)] * B_shared_dyn_local[18]));
    }
  }
  for (int i_2_1_s_259 = 0; i_2_1_s_259 < 4; ++i_2_1_s_259) {
    if (i_2_1_s_259 < 2) {
      Y_local[((i_2_1_s_259 * 12) + 7)] = (Y_local[((i_2_1_s_259 * 12) + 7)] + (A_shared_dyn_local[(i_2_1_s_259 + 2)] * B_shared_dyn_local[19]));
    }
  }
  for (int i_2_1_s_260 = 0; i_2_1_s_260 < 4; ++i_2_1_s_260) {
    if (i_2_1_s_260 < 2) {
      Y_local[((i_2_1_s_260 * 12) + 8)] = (Y_local[((i_2_1_s_260 * 12) + 8)] + (A_shared_dyn_local[(i_2_1_s_260 + 2)] * B_shared_dyn_local[20]));
    }
  }
  for (int i_2_1_s_261 = 0; i_2_1_s_261 < 4; ++i_2_1_s_261) {
    if (i_2_1_s_261 < 2) {
      Y_local[((i_2_1_s_261 * 12) + 9)] = (Y_local[((i_2_1_s_261 * 12) + 9)] + (A_shared_dyn_local[(i_2_1_s_261 + 2)] * B_shared_dyn_local[21]));
    }
  }
  for (int i_2_1_s_262 = 0; i_2_1_s_262 < 4; ++i_2_1_s_262) {
    if (i_2_1_s_262 < 2) {
      Y_local[((i_2_1_s_262 * 12) + 10)] = (Y_local[((i_2_1_s_262 * 12) + 10)] + (A_shared_dyn_local[(i_2_1_s_262 + 2)] * B_shared_dyn_local[22]));
    }
  }
  for (int i_2_1_s_263 = 0; i_2_1_s_263 < 4; ++i_2_1_s_263) {
    if (i_2_1_s_263 < 2) {
      Y_local[((i_2_1_s_263 * 12) + 11)] = (Y_local[((i_2_1_s_263 * 12) + 11)] + (A_shared_dyn_local[(i_2_1_s_263 + 2)] * B_shared_dyn_local[23]));
    }
  }
  for (int ax1_1_s_23 = 0; ax1_1_s_23 < 4; ++ax1_1_s_23) {
    if (ax1_1_s_23 < 2) {
      A_shared_dyn_local[(ax1_1_s_23 + 2)] = ((float*)buf_dyn_shmem)[((((((((((int)threadIdx.x) & 63) >> 5) * 32) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_23) + 1472)];
    }
  }
  for (int ax1_0_23 = 0; ax1_0_23 < 3; ++ax1_0_23) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_23 * 4) + 12)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_23 * 4)) >> 6) * 64) + (((ax1_0_23 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_23 * 4)) >> 3)) & 7) * 4)) + 4992) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
  }
  for (int i_2_1_s_264 = 0; i_2_1_s_264 < 4; ++i_2_1_s_264) {
    if (i_2_1_s_264 < 2) {
      Y_local[(i_2_1_s_264 * 12)] = (Y_local[(i_2_1_s_264 * 12)] + (A_shared_dyn_local[i_2_1_s_264] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_265 = 0; i_2_1_s_265 < 4; ++i_2_1_s_265) {
    if (i_2_1_s_265 < 2) {
      Y_local[((i_2_1_s_265 * 12) + 1)] = (Y_local[((i_2_1_s_265 * 12) + 1)] + (A_shared_dyn_local[i_2_1_s_265] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_266 = 0; i_2_1_s_266 < 4; ++i_2_1_s_266) {
    if (i_2_1_s_266 < 2) {
      Y_local[((i_2_1_s_266 * 12) + 2)] = (Y_local[((i_2_1_s_266 * 12) + 2)] + (A_shared_dyn_local[i_2_1_s_266] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_267 = 0; i_2_1_s_267 < 4; ++i_2_1_s_267) {
    if (i_2_1_s_267 < 2) {
      Y_local[((i_2_1_s_267 * 12) + 3)] = (Y_local[((i_2_1_s_267 * 12) + 3)] + (A_shared_dyn_local[i_2_1_s_267] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_268 = 0; i_2_1_s_268 < 4; ++i_2_1_s_268) {
    if (i_2_1_s_268 < 2) {
      Y_local[((i_2_1_s_268 * 12) + 4)] = (Y_local[((i_2_1_s_268 * 12) + 4)] + (A_shared_dyn_local[i_2_1_s_268] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_269 = 0; i_2_1_s_269 < 4; ++i_2_1_s_269) {
    if (i_2_1_s_269 < 2) {
      Y_local[((i_2_1_s_269 * 12) + 5)] = (Y_local[((i_2_1_s_269 * 12) + 5)] + (A_shared_dyn_local[i_2_1_s_269] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_270 = 0; i_2_1_s_270 < 4; ++i_2_1_s_270) {
    if (i_2_1_s_270 < 2) {
      Y_local[((i_2_1_s_270 * 12) + 6)] = (Y_local[((i_2_1_s_270 * 12) + 6)] + (A_shared_dyn_local[i_2_1_s_270] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_271 = 0; i_2_1_s_271 < 4; ++i_2_1_s_271) {
    if (i_2_1_s_271 < 2) {
      Y_local[((i_2_1_s_271 * 12) + 7)] = (Y_local[((i_2_1_s_271 * 12) + 7)] + (A_shared_dyn_local[i_2_1_s_271] * B_shared_dyn_local[7]));
    }
  }
  for (int i_2_1_s_272 = 0; i_2_1_s_272 < 4; ++i_2_1_s_272) {
    if (i_2_1_s_272 < 2) {
      Y_local[((i_2_1_s_272 * 12) + 8)] = (Y_local[((i_2_1_s_272 * 12) + 8)] + (A_shared_dyn_local[i_2_1_s_272] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_273 = 0; i_2_1_s_273 < 4; ++i_2_1_s_273) {
    if (i_2_1_s_273 < 2) {
      Y_local[((i_2_1_s_273 * 12) + 9)] = (Y_local[((i_2_1_s_273 * 12) + 9)] + (A_shared_dyn_local[i_2_1_s_273] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_274 = 0; i_2_1_s_274 < 4; ++i_2_1_s_274) {
    if (i_2_1_s_274 < 2) {
      Y_local[((i_2_1_s_274 * 12) + 10)] = (Y_local[((i_2_1_s_274 * 12) + 10)] + (A_shared_dyn_local[i_2_1_s_274] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_275 = 0; i_2_1_s_275 < 4; ++i_2_1_s_275) {
    if (i_2_1_s_275 < 2) {
      Y_local[((i_2_1_s_275 * 12) + 11)] = (Y_local[((i_2_1_s_275 * 12) + 11)] + (A_shared_dyn_local[i_2_1_s_275] * B_shared_dyn_local[11]));
    }
  }
  for (int ax1_1_s_24 = 0; ax1_1_s_24 < 4; ++ax1_1_s_24) {
    if (ax1_1_s_24 < 2) {
      A_shared_dyn_local[ax1_1_s_24] = ((float*)buf_dyn_shmem)[((((((((((int)threadIdx.x) & 63) >> 5) * 32) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_24) + 1536)];
    }
  }
  for (int ax1_0_24 = 0; ax1_0_24 < 3; ++ax1_0_24) {
    *(float4*)(B_shared_dyn_local + (ax1_0_24 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_24 * 4)) >> 6) * 64) + (((ax1_0_24 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_24 * 4)) >> 3)) & 7) * 4)) + 5120) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
  }
  for (int i_2_1_s_276 = 0; i_2_1_s_276 < 4; ++i_2_1_s_276) {
    if (i_2_1_s_276 < 2) {
      Y_local[(i_2_1_s_276 * 12)] = (Y_local[(i_2_1_s_276 * 12)] + (A_shared_dyn_local[(i_2_1_s_276 + 2)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_277 = 0; i_2_1_s_277 < 4; ++i_2_1_s_277) {
    if (i_2_1_s_277 < 2) {
      Y_local[((i_2_1_s_277 * 12) + 1)] = (Y_local[((i_2_1_s_277 * 12) + 1)] + (A_shared_dyn_local[(i_2_1_s_277 + 2)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_278 = 0; i_2_1_s_278 < 4; ++i_2_1_s_278) {
    if (i_2_1_s_278 < 2) {
      Y_local[((i_2_1_s_278 * 12) + 2)] = (Y_local[((i_2_1_s_278 * 12) + 2)] + (A_shared_dyn_local[(i_2_1_s_278 + 2)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_279 = 0; i_2_1_s_279 < 4; ++i_2_1_s_279) {
    if (i_2_1_s_279 < 2) {
      Y_local[((i_2_1_s_279 * 12) + 3)] = (Y_local[((i_2_1_s_279 * 12) + 3)] + (A_shared_dyn_local[(i_2_1_s_279 + 2)] * B_shared_dyn_local[15]));
    }
  }
  for (int i_2_1_s_280 = 0; i_2_1_s_280 < 4; ++i_2_1_s_280) {
    if (i_2_1_s_280 < 2) {
      Y_local[((i_2_1_s_280 * 12) + 4)] = (Y_local[((i_2_1_s_280 * 12) + 4)] + (A_shared_dyn_local[(i_2_1_s_280 + 2)] * B_shared_dyn_local[16]));
    }
  }
  for (int i_2_1_s_281 = 0; i_2_1_s_281 < 4; ++i_2_1_s_281) {
    if (i_2_1_s_281 < 2) {
      Y_local[((i_2_1_s_281 * 12) + 5)] = (Y_local[((i_2_1_s_281 * 12) + 5)] + (A_shared_dyn_local[(i_2_1_s_281 + 2)] * B_shared_dyn_local[17]));
    }
  }
  for (int i_2_1_s_282 = 0; i_2_1_s_282 < 4; ++i_2_1_s_282) {
    if (i_2_1_s_282 < 2) {
      Y_local[((i_2_1_s_282 * 12) + 6)] = (Y_local[((i_2_1_s_282 * 12) + 6)] + (A_shared_dyn_local[(i_2_1_s_282 + 2)] * B_shared_dyn_local[18]));
    }
  }
  for (int i_2_1_s_283 = 0; i_2_1_s_283 < 4; ++i_2_1_s_283) {
    if (i_2_1_s_283 < 2) {
      Y_local[((i_2_1_s_283 * 12) + 7)] = (Y_local[((i_2_1_s_283 * 12) + 7)] + (A_shared_dyn_local[(i_2_1_s_283 + 2)] * B_shared_dyn_local[19]));
    }
  }
  for (int i_2_1_s_284 = 0; i_2_1_s_284 < 4; ++i_2_1_s_284) {
    if (i_2_1_s_284 < 2) {
      Y_local[((i_2_1_s_284 * 12) + 8)] = (Y_local[((i_2_1_s_284 * 12) + 8)] + (A_shared_dyn_local[(i_2_1_s_284 + 2)] * B_shared_dyn_local[20]));
    }
  }
  for (int i_2_1_s_285 = 0; i_2_1_s_285 < 4; ++i_2_1_s_285) {
    if (i_2_1_s_285 < 2) {
      Y_local[((i_2_1_s_285 * 12) + 9)] = (Y_local[((i_2_1_s_285 * 12) + 9)] + (A_shared_dyn_local[(i_2_1_s_285 + 2)] * B_shared_dyn_local[21]));
    }
  }
  for (int i_2_1_s_286 = 0; i_2_1_s_286 < 4; ++i_2_1_s_286) {
    if (i_2_1_s_286 < 2) {
      Y_local[((i_2_1_s_286 * 12) + 10)] = (Y_local[((i_2_1_s_286 * 12) + 10)] + (A_shared_dyn_local[(i_2_1_s_286 + 2)] * B_shared_dyn_local[22]));
    }
  }
  for (int i_2_1_s_287 = 0; i_2_1_s_287 < 4; ++i_2_1_s_287) {
    if (i_2_1_s_287 < 2) {
      Y_local[((i_2_1_s_287 * 12) + 11)] = (Y_local[((i_2_1_s_287 * 12) + 11)] + (A_shared_dyn_local[(i_2_1_s_287 + 2)] * B_shared_dyn_local[23]));
    }
  }
  for (int ax1_1_s_25 = 0; ax1_1_s_25 < 4; ++ax1_1_s_25) {
    if (ax1_1_s_25 < 2) {
      A_shared_dyn_local[(ax1_1_s_25 + 2)] = ((float*)buf_dyn_shmem)[((((((((((int)threadIdx.x) & 63) >> 5) * 32) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_25) + 1600)];
    }
  }
  for (int ax1_0_25 = 0; ax1_0_25 < 3; ++ax1_0_25) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_25 * 4) + 12)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_25 * 4)) >> 6) * 64) + (((ax1_0_25 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_25 * 4)) >> 3)) & 7) * 4)) + 5248) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
  }
  for (int i_2_1_s_288 = 0; i_2_1_s_288 < 4; ++i_2_1_s_288) {
    if (i_2_1_s_288 < 2) {
      Y_local[(i_2_1_s_288 * 12)] = (Y_local[(i_2_1_s_288 * 12)] + (A_shared_dyn_local[i_2_1_s_288] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_289 = 0; i_2_1_s_289 < 4; ++i_2_1_s_289) {
    if (i_2_1_s_289 < 2) {
      Y_local[((i_2_1_s_289 * 12) + 1)] = (Y_local[((i_2_1_s_289 * 12) + 1)] + (A_shared_dyn_local[i_2_1_s_289] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_290 = 0; i_2_1_s_290 < 4; ++i_2_1_s_290) {
    if (i_2_1_s_290 < 2) {
      Y_local[((i_2_1_s_290 * 12) + 2)] = (Y_local[((i_2_1_s_290 * 12) + 2)] + (A_shared_dyn_local[i_2_1_s_290] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_291 = 0; i_2_1_s_291 < 4; ++i_2_1_s_291) {
    if (i_2_1_s_291 < 2) {
      Y_local[((i_2_1_s_291 * 12) + 3)] = (Y_local[((i_2_1_s_291 * 12) + 3)] + (A_shared_dyn_local[i_2_1_s_291] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_292 = 0; i_2_1_s_292 < 4; ++i_2_1_s_292) {
    if (i_2_1_s_292 < 2) {
      Y_local[((i_2_1_s_292 * 12) + 4)] = (Y_local[((i_2_1_s_292 * 12) + 4)] + (A_shared_dyn_local[i_2_1_s_292] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_293 = 0; i_2_1_s_293 < 4; ++i_2_1_s_293) {
    if (i_2_1_s_293 < 2) {
      Y_local[((i_2_1_s_293 * 12) + 5)] = (Y_local[((i_2_1_s_293 * 12) + 5)] + (A_shared_dyn_local[i_2_1_s_293] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_294 = 0; i_2_1_s_294 < 4; ++i_2_1_s_294) {
    if (i_2_1_s_294 < 2) {
      Y_local[((i_2_1_s_294 * 12) + 6)] = (Y_local[((i_2_1_s_294 * 12) + 6)] + (A_shared_dyn_local[i_2_1_s_294] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_295 = 0; i_2_1_s_295 < 4; ++i_2_1_s_295) {
    if (i_2_1_s_295 < 2) {
      Y_local[((i_2_1_s_295 * 12) + 7)] = (Y_local[((i_2_1_s_295 * 12) + 7)] + (A_shared_dyn_local[i_2_1_s_295] * B_shared_dyn_local[7]));
    }
  }
  for (int i_2_1_s_296 = 0; i_2_1_s_296 < 4; ++i_2_1_s_296) {
    if (i_2_1_s_296 < 2) {
      Y_local[((i_2_1_s_296 * 12) + 8)] = (Y_local[((i_2_1_s_296 * 12) + 8)] + (A_shared_dyn_local[i_2_1_s_296] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_297 = 0; i_2_1_s_297 < 4; ++i_2_1_s_297) {
    if (i_2_1_s_297 < 2) {
      Y_local[((i_2_1_s_297 * 12) + 9)] = (Y_local[((i_2_1_s_297 * 12) + 9)] + (A_shared_dyn_local[i_2_1_s_297] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_298 = 0; i_2_1_s_298 < 4; ++i_2_1_s_298) {
    if (i_2_1_s_298 < 2) {
      Y_local[((i_2_1_s_298 * 12) + 10)] = (Y_local[((i_2_1_s_298 * 12) + 10)] + (A_shared_dyn_local[i_2_1_s_298] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_299 = 0; i_2_1_s_299 < 4; ++i_2_1_s_299) {
    if (i_2_1_s_299 < 2) {
      Y_local[((i_2_1_s_299 * 12) + 11)] = (Y_local[((i_2_1_s_299 * 12) + 11)] + (A_shared_dyn_local[i_2_1_s_299] * B_shared_dyn_local[11]));
    }
  }
  for (int ax1_1_s_26 = 0; ax1_1_s_26 < 4; ++ax1_1_s_26) {
    if (ax1_1_s_26 < 2) {
      A_shared_dyn_local[ax1_1_s_26] = ((float*)buf_dyn_shmem)[((((((((((int)threadIdx.x) & 63) >> 5) * 32) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_26) + 1664)];
    }
  }
  for (int ax1_0_26 = 0; ax1_0_26 < 3; ++ax1_0_26) {
    *(float4*)(B_shared_dyn_local + (ax1_0_26 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_26 * 4)) >> 6) * 64) + (((ax1_0_26 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_26 * 4)) >> 3)) & 7) * 4)) + 5376) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
  }
  for (int i_2_1_s_300 = 0; i_2_1_s_300 < 4; ++i_2_1_s_300) {
    if (i_2_1_s_300 < 2) {
      Y_local[(i_2_1_s_300 * 12)] = (Y_local[(i_2_1_s_300 * 12)] + (A_shared_dyn_local[(i_2_1_s_300 + 2)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_301 = 0; i_2_1_s_301 < 4; ++i_2_1_s_301) {
    if (i_2_1_s_301 < 2) {
      Y_local[((i_2_1_s_301 * 12) + 1)] = (Y_local[((i_2_1_s_301 * 12) + 1)] + (A_shared_dyn_local[(i_2_1_s_301 + 2)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_302 = 0; i_2_1_s_302 < 4; ++i_2_1_s_302) {
    if (i_2_1_s_302 < 2) {
      Y_local[((i_2_1_s_302 * 12) + 2)] = (Y_local[((i_2_1_s_302 * 12) + 2)] + (A_shared_dyn_local[(i_2_1_s_302 + 2)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_303 = 0; i_2_1_s_303 < 4; ++i_2_1_s_303) {
    if (i_2_1_s_303 < 2) {
      Y_local[((i_2_1_s_303 * 12) + 3)] = (Y_local[((i_2_1_s_303 * 12) + 3)] + (A_shared_dyn_local[(i_2_1_s_303 + 2)] * B_shared_dyn_local[15]));
    }
  }
  for (int i_2_1_s_304 = 0; i_2_1_s_304 < 4; ++i_2_1_s_304) {
    if (i_2_1_s_304 < 2) {
      Y_local[((i_2_1_s_304 * 12) + 4)] = (Y_local[((i_2_1_s_304 * 12) + 4)] + (A_shared_dyn_local[(i_2_1_s_304 + 2)] * B_shared_dyn_local[16]));
    }
  }
  for (int i_2_1_s_305 = 0; i_2_1_s_305 < 4; ++i_2_1_s_305) {
    if (i_2_1_s_305 < 2) {
      Y_local[((i_2_1_s_305 * 12) + 5)] = (Y_local[((i_2_1_s_305 * 12) + 5)] + (A_shared_dyn_local[(i_2_1_s_305 + 2)] * B_shared_dyn_local[17]));
    }
  }
  for (int i_2_1_s_306 = 0; i_2_1_s_306 < 4; ++i_2_1_s_306) {
    if (i_2_1_s_306 < 2) {
      Y_local[((i_2_1_s_306 * 12) + 6)] = (Y_local[((i_2_1_s_306 * 12) + 6)] + (A_shared_dyn_local[(i_2_1_s_306 + 2)] * B_shared_dyn_local[18]));
    }
  }
  for (int i_2_1_s_307 = 0; i_2_1_s_307 < 4; ++i_2_1_s_307) {
    if (i_2_1_s_307 < 2) {
      Y_local[((i_2_1_s_307 * 12) + 7)] = (Y_local[((i_2_1_s_307 * 12) + 7)] + (A_shared_dyn_local[(i_2_1_s_307 + 2)] * B_shared_dyn_local[19]));
    }
  }
  for (int i_2_1_s_308 = 0; i_2_1_s_308 < 4; ++i_2_1_s_308) {
    if (i_2_1_s_308 < 2) {
      Y_local[((i_2_1_s_308 * 12) + 8)] = (Y_local[((i_2_1_s_308 * 12) + 8)] + (A_shared_dyn_local[(i_2_1_s_308 + 2)] * B_shared_dyn_local[20]));
    }
  }
  for (int i_2_1_s_309 = 0; i_2_1_s_309 < 4; ++i_2_1_s_309) {
    if (i_2_1_s_309 < 2) {
      Y_local[((i_2_1_s_309 * 12) + 9)] = (Y_local[((i_2_1_s_309 * 12) + 9)] + (A_shared_dyn_local[(i_2_1_s_309 + 2)] * B_shared_dyn_local[21]));
    }
  }
  for (int i_2_1_s_310 = 0; i_2_1_s_310 < 4; ++i_2_1_s_310) {
    if (i_2_1_s_310 < 2) {
      Y_local[((i_2_1_s_310 * 12) + 10)] = (Y_local[((i_2_1_s_310 * 12) + 10)] + (A_shared_dyn_local[(i_2_1_s_310 + 2)] * B_shared_dyn_local[22]));
    }
  }
  for (int i_2_1_s_311 = 0; i_2_1_s_311 < 4; ++i_2_1_s_311) {
    if (i_2_1_s_311 < 2) {
      Y_local[((i_2_1_s_311 * 12) + 11)] = (Y_local[((i_2_1_s_311 * 12) + 11)] + (A_shared_dyn_local[(i_2_1_s_311 + 2)] * B_shared_dyn_local[23]));
    }
  }
  for (int ax1_1_s_27 = 0; ax1_1_s_27 < 4; ++ax1_1_s_27) {
    if (ax1_1_s_27 < 2) {
      A_shared_dyn_local[(ax1_1_s_27 + 2)] = ((float*)buf_dyn_shmem)[((((((((((int)threadIdx.x) & 63) >> 5) * 32) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_27) + 1728)];
    }
  }
  for (int ax1_0_27 = 0; ax1_0_27 < 3; ++ax1_0_27) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_27 * 4) + 12)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_27 * 4)) >> 6) * 64) + (((ax1_0_27 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_27 * 4)) >> 3)) & 7) * 4)) + 5504) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
  }
  for (int i_2_1_s_312 = 0; i_2_1_s_312 < 4; ++i_2_1_s_312) {
    if (i_2_1_s_312 < 2) {
      Y_local[(i_2_1_s_312 * 12)] = (Y_local[(i_2_1_s_312 * 12)] + (A_shared_dyn_local[i_2_1_s_312] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_313 = 0; i_2_1_s_313 < 4; ++i_2_1_s_313) {
    if (i_2_1_s_313 < 2) {
      Y_local[((i_2_1_s_313 * 12) + 1)] = (Y_local[((i_2_1_s_313 * 12) + 1)] + (A_shared_dyn_local[i_2_1_s_313] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_314 = 0; i_2_1_s_314 < 4; ++i_2_1_s_314) {
    if (i_2_1_s_314 < 2) {
      Y_local[((i_2_1_s_314 * 12) + 2)] = (Y_local[((i_2_1_s_314 * 12) + 2)] + (A_shared_dyn_local[i_2_1_s_314] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_315 = 0; i_2_1_s_315 < 4; ++i_2_1_s_315) {
    if (i_2_1_s_315 < 2) {
      Y_local[((i_2_1_s_315 * 12) + 3)] = (Y_local[((i_2_1_s_315 * 12) + 3)] + (A_shared_dyn_local[i_2_1_s_315] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_316 = 0; i_2_1_s_316 < 4; ++i_2_1_s_316) {
    if (i_2_1_s_316 < 2) {
      Y_local[((i_2_1_s_316 * 12) + 4)] = (Y_local[((i_2_1_s_316 * 12) + 4)] + (A_shared_dyn_local[i_2_1_s_316] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_317 = 0; i_2_1_s_317 < 4; ++i_2_1_s_317) {
    if (i_2_1_s_317 < 2) {
      Y_local[((i_2_1_s_317 * 12) + 5)] = (Y_local[((i_2_1_s_317 * 12) + 5)] + (A_shared_dyn_local[i_2_1_s_317] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_318 = 0; i_2_1_s_318 < 4; ++i_2_1_s_318) {
    if (i_2_1_s_318 < 2) {
      Y_local[((i_2_1_s_318 * 12) + 6)] = (Y_local[((i_2_1_s_318 * 12) + 6)] + (A_shared_dyn_local[i_2_1_s_318] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_319 = 0; i_2_1_s_319 < 4; ++i_2_1_s_319) {
    if (i_2_1_s_319 < 2) {
      Y_local[((i_2_1_s_319 * 12) + 7)] = (Y_local[((i_2_1_s_319 * 12) + 7)] + (A_shared_dyn_local[i_2_1_s_319] * B_shared_dyn_local[7]));
    }
  }
  for (int i_2_1_s_320 = 0; i_2_1_s_320 < 4; ++i_2_1_s_320) {
    if (i_2_1_s_320 < 2) {
      Y_local[((i_2_1_s_320 * 12) + 8)] = (Y_local[((i_2_1_s_320 * 12) + 8)] + (A_shared_dyn_local[i_2_1_s_320] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_321 = 0; i_2_1_s_321 < 4; ++i_2_1_s_321) {
    if (i_2_1_s_321 < 2) {
      Y_local[((i_2_1_s_321 * 12) + 9)] = (Y_local[((i_2_1_s_321 * 12) + 9)] + (A_shared_dyn_local[i_2_1_s_321] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_322 = 0; i_2_1_s_322 < 4; ++i_2_1_s_322) {
    if (i_2_1_s_322 < 2) {
      Y_local[((i_2_1_s_322 * 12) + 10)] = (Y_local[((i_2_1_s_322 * 12) + 10)] + (A_shared_dyn_local[i_2_1_s_322] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_323 = 0; i_2_1_s_323 < 4; ++i_2_1_s_323) {
    if (i_2_1_s_323 < 2) {
      Y_local[((i_2_1_s_323 * 12) + 11)] = (Y_local[((i_2_1_s_323 * 12) + 11)] + (A_shared_dyn_local[i_2_1_s_323] * B_shared_dyn_local[11]));
    }
  }
  for (int ax1_1_s_28 = 0; ax1_1_s_28 < 4; ++ax1_1_s_28) {
    if (ax1_1_s_28 < 2) {
      A_shared_dyn_local[ax1_1_s_28] = ((float*)buf_dyn_shmem)[((((((((((int)threadIdx.x) & 63) >> 5) * 32) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_28) + 1792)];
    }
  }
  for (int ax1_0_28 = 0; ax1_0_28 < 3; ++ax1_0_28) {
    *(float4*)(B_shared_dyn_local + (ax1_0_28 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_28 * 4)) >> 6) * 64) + (((ax1_0_28 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_28 * 4)) >> 3)) & 7) * 4)) + 5632) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
  }
  for (int i_2_1_s_324 = 0; i_2_1_s_324 < 4; ++i_2_1_s_324) {
    if (i_2_1_s_324 < 2) {
      Y_local[(i_2_1_s_324 * 12)] = (Y_local[(i_2_1_s_324 * 12)] + (A_shared_dyn_local[(i_2_1_s_324 + 2)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_325 = 0; i_2_1_s_325 < 4; ++i_2_1_s_325) {
    if (i_2_1_s_325 < 2) {
      Y_local[((i_2_1_s_325 * 12) + 1)] = (Y_local[((i_2_1_s_325 * 12) + 1)] + (A_shared_dyn_local[(i_2_1_s_325 + 2)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_326 = 0; i_2_1_s_326 < 4; ++i_2_1_s_326) {
    if (i_2_1_s_326 < 2) {
      Y_local[((i_2_1_s_326 * 12) + 2)] = (Y_local[((i_2_1_s_326 * 12) + 2)] + (A_shared_dyn_local[(i_2_1_s_326 + 2)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_327 = 0; i_2_1_s_327 < 4; ++i_2_1_s_327) {
    if (i_2_1_s_327 < 2) {
      Y_local[((i_2_1_s_327 * 12) + 3)] = (Y_local[((i_2_1_s_327 * 12) + 3)] + (A_shared_dyn_local[(i_2_1_s_327 + 2)] * B_shared_dyn_local[15]));
    }
  }
  for (int i_2_1_s_328 = 0; i_2_1_s_328 < 4; ++i_2_1_s_328) {
    if (i_2_1_s_328 < 2) {
      Y_local[((i_2_1_s_328 * 12) + 4)] = (Y_local[((i_2_1_s_328 * 12) + 4)] + (A_shared_dyn_local[(i_2_1_s_328 + 2)] * B_shared_dyn_local[16]));
    }
  }
  for (int i_2_1_s_329 = 0; i_2_1_s_329 < 4; ++i_2_1_s_329) {
    if (i_2_1_s_329 < 2) {
      Y_local[((i_2_1_s_329 * 12) + 5)] = (Y_local[((i_2_1_s_329 * 12) + 5)] + (A_shared_dyn_local[(i_2_1_s_329 + 2)] * B_shared_dyn_local[17]));
    }
  }
  for (int i_2_1_s_330 = 0; i_2_1_s_330 < 4; ++i_2_1_s_330) {
    if (i_2_1_s_330 < 2) {
      Y_local[((i_2_1_s_330 * 12) + 6)] = (Y_local[((i_2_1_s_330 * 12) + 6)] + (A_shared_dyn_local[(i_2_1_s_330 + 2)] * B_shared_dyn_local[18]));
    }
  }
  for (int i_2_1_s_331 = 0; i_2_1_s_331 < 4; ++i_2_1_s_331) {
    if (i_2_1_s_331 < 2) {
      Y_local[((i_2_1_s_331 * 12) + 7)] = (Y_local[((i_2_1_s_331 * 12) + 7)] + (A_shared_dyn_local[(i_2_1_s_331 + 2)] * B_shared_dyn_local[19]));
    }
  }
  for (int i_2_1_s_332 = 0; i_2_1_s_332 < 4; ++i_2_1_s_332) {
    if (i_2_1_s_332 < 2) {
      Y_local[((i_2_1_s_332 * 12) + 8)] = (Y_local[((i_2_1_s_332 * 12) + 8)] + (A_shared_dyn_local[(i_2_1_s_332 + 2)] * B_shared_dyn_local[20]));
    }
  }
  for (int i_2_1_s_333 = 0; i_2_1_s_333 < 4; ++i_2_1_s_333) {
    if (i_2_1_s_333 < 2) {
      Y_local[((i_2_1_s_333 * 12) + 9)] = (Y_local[((i_2_1_s_333 * 12) + 9)] + (A_shared_dyn_local[(i_2_1_s_333 + 2)] * B_shared_dyn_local[21]));
    }
  }
  for (int i_2_1_s_334 = 0; i_2_1_s_334 < 4; ++i_2_1_s_334) {
    if (i_2_1_s_334 < 2) {
      Y_local[((i_2_1_s_334 * 12) + 10)] = (Y_local[((i_2_1_s_334 * 12) + 10)] + (A_shared_dyn_local[(i_2_1_s_334 + 2)] * B_shared_dyn_local[22]));
    }
  }
  for (int i_2_1_s_335 = 0; i_2_1_s_335 < 4; ++i_2_1_s_335) {
    if (i_2_1_s_335 < 2) {
      Y_local[((i_2_1_s_335 * 12) + 11)] = (Y_local[((i_2_1_s_335 * 12) + 11)] + (A_shared_dyn_local[(i_2_1_s_335 + 2)] * B_shared_dyn_local[23]));
    }
  }
  for (int ax1_1_s_29 = 0; ax1_1_s_29 < 4; ++ax1_1_s_29) {
    if (ax1_1_s_29 < 2) {
      A_shared_dyn_local[(ax1_1_s_29 + 2)] = ((float*)buf_dyn_shmem)[((((((((((int)threadIdx.x) & 63) >> 5) * 32) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_29) + 1856)];
    }
  }
  for (int ax1_0_29 = 0; ax1_0_29 < 3; ++ax1_0_29) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_29 * 4) + 12)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_29 * 4)) >> 6) * 64) + (((ax1_0_29 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_29 * 4)) >> 3)) & 7) * 4)) + 5760) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
  }
  for (int i_2_1_s_336 = 0; i_2_1_s_336 < 4; ++i_2_1_s_336) {
    if (i_2_1_s_336 < 2) {
      Y_local[(i_2_1_s_336 * 12)] = (Y_local[(i_2_1_s_336 * 12)] + (A_shared_dyn_local[i_2_1_s_336] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_337 = 0; i_2_1_s_337 < 4; ++i_2_1_s_337) {
    if (i_2_1_s_337 < 2) {
      Y_local[((i_2_1_s_337 * 12) + 1)] = (Y_local[((i_2_1_s_337 * 12) + 1)] + (A_shared_dyn_local[i_2_1_s_337] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_338 = 0; i_2_1_s_338 < 4; ++i_2_1_s_338) {
    if (i_2_1_s_338 < 2) {
      Y_local[((i_2_1_s_338 * 12) + 2)] = (Y_local[((i_2_1_s_338 * 12) + 2)] + (A_shared_dyn_local[i_2_1_s_338] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_339 = 0; i_2_1_s_339 < 4; ++i_2_1_s_339) {
    if (i_2_1_s_339 < 2) {
      Y_local[((i_2_1_s_339 * 12) + 3)] = (Y_local[((i_2_1_s_339 * 12) + 3)] + (A_shared_dyn_local[i_2_1_s_339] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_340 = 0; i_2_1_s_340 < 4; ++i_2_1_s_340) {
    if (i_2_1_s_340 < 2) {
      Y_local[((i_2_1_s_340 * 12) + 4)] = (Y_local[((i_2_1_s_340 * 12) + 4)] + (A_shared_dyn_local[i_2_1_s_340] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_341 = 0; i_2_1_s_341 < 4; ++i_2_1_s_341) {
    if (i_2_1_s_341 < 2) {
      Y_local[((i_2_1_s_341 * 12) + 5)] = (Y_local[((i_2_1_s_341 * 12) + 5)] + (A_shared_dyn_local[i_2_1_s_341] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_342 = 0; i_2_1_s_342 < 4; ++i_2_1_s_342) {
    if (i_2_1_s_342 < 2) {
      Y_local[((i_2_1_s_342 * 12) + 6)] = (Y_local[((i_2_1_s_342 * 12) + 6)] + (A_shared_dyn_local[i_2_1_s_342] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_343 = 0; i_2_1_s_343 < 4; ++i_2_1_s_343) {
    if (i_2_1_s_343 < 2) {
      Y_local[((i_2_1_s_343 * 12) + 7)] = (Y_local[((i_2_1_s_343 * 12) + 7)] + (A_shared_dyn_local[i_2_1_s_343] * B_shared_dyn_local[7]));
    }
  }
  for (int i_2_1_s_344 = 0; i_2_1_s_344 < 4; ++i_2_1_s_344) {
    if (i_2_1_s_344 < 2) {
      Y_local[((i_2_1_s_344 * 12) + 8)] = (Y_local[((i_2_1_s_344 * 12) + 8)] + (A_shared_dyn_local[i_2_1_s_344] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_345 = 0; i_2_1_s_345 < 4; ++i_2_1_s_345) {
    if (i_2_1_s_345 < 2) {
      Y_local[((i_2_1_s_345 * 12) + 9)] = (Y_local[((i_2_1_s_345 * 12) + 9)] + (A_shared_dyn_local[i_2_1_s_345] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_346 = 0; i_2_1_s_346 < 4; ++i_2_1_s_346) {
    if (i_2_1_s_346 < 2) {
      Y_local[((i_2_1_s_346 * 12) + 10)] = (Y_local[((i_2_1_s_346 * 12) + 10)] + (A_shared_dyn_local[i_2_1_s_346] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_347 = 0; i_2_1_s_347 < 4; ++i_2_1_s_347) {
    if (i_2_1_s_347 < 2) {
      Y_local[((i_2_1_s_347 * 12) + 11)] = (Y_local[((i_2_1_s_347 * 12) + 11)] + (A_shared_dyn_local[i_2_1_s_347] * B_shared_dyn_local[11]));
    }
  }
  for (int ax1_1_s_30 = 0; ax1_1_s_30 < 4; ++ax1_1_s_30) {
    if (ax1_1_s_30 < 2) {
      A_shared_dyn_local[ax1_1_s_30] = ((float*)buf_dyn_shmem)[((((((((((int)threadIdx.x) & 63) >> 5) * 32) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_30) + 1920)];
    }
  }
  for (int ax1_0_30 = 0; ax1_0_30 < 3; ++ax1_0_30) {
    *(float4*)(B_shared_dyn_local + (ax1_0_30 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_30 * 4)) >> 6) * 64) + (((ax1_0_30 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_30 * 4)) >> 3)) & 7) * 4)) + 5888) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
  }
  for (int i_2_1_s_348 = 0; i_2_1_s_348 < 4; ++i_2_1_s_348) {
    if (i_2_1_s_348 < 2) {
      Y_local[(i_2_1_s_348 * 12)] = (Y_local[(i_2_1_s_348 * 12)] + (A_shared_dyn_local[(i_2_1_s_348 + 2)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_349 = 0; i_2_1_s_349 < 4; ++i_2_1_s_349) {
    if (i_2_1_s_349 < 2) {
      Y_local[((i_2_1_s_349 * 12) + 1)] = (Y_local[((i_2_1_s_349 * 12) + 1)] + (A_shared_dyn_local[(i_2_1_s_349 + 2)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_350 = 0; i_2_1_s_350 < 4; ++i_2_1_s_350) {
    if (i_2_1_s_350 < 2) {
      Y_local[((i_2_1_s_350 * 12) + 2)] = (Y_local[((i_2_1_s_350 * 12) + 2)] + (A_shared_dyn_local[(i_2_1_s_350 + 2)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_351 = 0; i_2_1_s_351 < 4; ++i_2_1_s_351) {
    if (i_2_1_s_351 < 2) {
      Y_local[((i_2_1_s_351 * 12) + 3)] = (Y_local[((i_2_1_s_351 * 12) + 3)] + (A_shared_dyn_local[(i_2_1_s_351 + 2)] * B_shared_dyn_local[15]));
    }
  }
  for (int i_2_1_s_352 = 0; i_2_1_s_352 < 4; ++i_2_1_s_352) {
    if (i_2_1_s_352 < 2) {
      Y_local[((i_2_1_s_352 * 12) + 4)] = (Y_local[((i_2_1_s_352 * 12) + 4)] + (A_shared_dyn_local[(i_2_1_s_352 + 2)] * B_shared_dyn_local[16]));
    }
  }
  for (int i_2_1_s_353 = 0; i_2_1_s_353 < 4; ++i_2_1_s_353) {
    if (i_2_1_s_353 < 2) {
      Y_local[((i_2_1_s_353 * 12) + 5)] = (Y_local[((i_2_1_s_353 * 12) + 5)] + (A_shared_dyn_local[(i_2_1_s_353 + 2)] * B_shared_dyn_local[17]));
    }
  }
  for (int i_2_1_s_354 = 0; i_2_1_s_354 < 4; ++i_2_1_s_354) {
    if (i_2_1_s_354 < 2) {
      Y_local[((i_2_1_s_354 * 12) + 6)] = (Y_local[((i_2_1_s_354 * 12) + 6)] + (A_shared_dyn_local[(i_2_1_s_354 + 2)] * B_shared_dyn_local[18]));
    }
  }
  for (int i_2_1_s_355 = 0; i_2_1_s_355 < 4; ++i_2_1_s_355) {
    if (i_2_1_s_355 < 2) {
      Y_local[((i_2_1_s_355 * 12) + 7)] = (Y_local[((i_2_1_s_355 * 12) + 7)] + (A_shared_dyn_local[(i_2_1_s_355 + 2)] * B_shared_dyn_local[19]));
    }
  }
  for (int i_2_1_s_356 = 0; i_2_1_s_356 < 4; ++i_2_1_s_356) {
    if (i_2_1_s_356 < 2) {
      Y_local[((i_2_1_s_356 * 12) + 8)] = (Y_local[((i_2_1_s_356 * 12) + 8)] + (A_shared_dyn_local[(i_2_1_s_356 + 2)] * B_shared_dyn_local[20]));
    }
  }
  for (int i_2_1_s_357 = 0; i_2_1_s_357 < 4; ++i_2_1_s_357) {
    if (i_2_1_s_357 < 2) {
      Y_local[((i_2_1_s_357 * 12) + 9)] = (Y_local[((i_2_1_s_357 * 12) + 9)] + (A_shared_dyn_local[(i_2_1_s_357 + 2)] * B_shared_dyn_local[21]));
    }
  }
  for (int i_2_1_s_358 = 0; i_2_1_s_358 < 4; ++i_2_1_s_358) {
    if (i_2_1_s_358 < 2) {
      Y_local[((i_2_1_s_358 * 12) + 10)] = (Y_local[((i_2_1_s_358 * 12) + 10)] + (A_shared_dyn_local[(i_2_1_s_358 + 2)] * B_shared_dyn_local[22]));
    }
  }
  for (int i_2_1_s_359 = 0; i_2_1_s_359 < 4; ++i_2_1_s_359) {
    if (i_2_1_s_359 < 2) {
      Y_local[((i_2_1_s_359 * 12) + 11)] = (Y_local[((i_2_1_s_359 * 12) + 11)] + (A_shared_dyn_local[(i_2_1_s_359 + 2)] * B_shared_dyn_local[23]));
    }
  }
  for (int ax1_1_s_31 = 0; ax1_1_s_31 < 4; ++ax1_1_s_31) {
    if (ax1_1_s_31 < 2) {
      A_shared_dyn_local[(ax1_1_s_31 + 2)] = ((float*)buf_dyn_shmem)[((((((((((int)threadIdx.x) & 63) >> 5) * 32) + (((((int)threadIdx.x) & 7) >> 2) * 16)) + (((((int)threadIdx.x) & 31) >> 3) * 4)) + (((((int)threadIdx.x) & 3) >> 1) * 2)) + ax1_1_s_31) + 1984)];
    }
  }
  for (int ax1_0_31 = 0; ax1_0_31 < 3; ++ax1_0_31) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_31 * 4) + 12)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((((((((int)blockIdx.x) & 7) * 48) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_31 * 4)) >> 6) * 64) + (((ax1_0_31 + (((int)threadIdx.x) & 1)) & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 6) + ((((int)threadIdx.x) >> 6) * 3)) + ((((((int)threadIdx.x) & 1) * 12) + (ax1_0_31 * 4)) >> 3)) & 7) * 4)) + 6016) - ((((((int)blockIdx.x) & 7) * 48) >> 6) * 64)));
  }
  for (int i_2_1_s_360 = 0; i_2_1_s_360 < 4; ++i_2_1_s_360) {
    if (i_2_1_s_360 < 2) {
      Y_local[(i_2_1_s_360 * 12)] = (Y_local[(i_2_1_s_360 * 12)] + (A_shared_dyn_local[i_2_1_s_360] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_361 = 0; i_2_1_s_361 < 4; ++i_2_1_s_361) {
    if (i_2_1_s_361 < 2) {
      Y_local[((i_2_1_s_361 * 12) + 1)] = (Y_local[((i_2_1_s_361 * 12) + 1)] + (A_shared_dyn_local[i_2_1_s_361] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_362 = 0; i_2_1_s_362 < 4; ++i_2_1_s_362) {
    if (i_2_1_s_362 < 2) {
      Y_local[((i_2_1_s_362 * 12) + 2)] = (Y_local[((i_2_1_s_362 * 12) + 2)] + (A_shared_dyn_local[i_2_1_s_362] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_363 = 0; i_2_1_s_363 < 4; ++i_2_1_s_363) {
    if (i_2_1_s_363 < 2) {
      Y_local[((i_2_1_s_363 * 12) + 3)] = (Y_local[((i_2_1_s_363 * 12) + 3)] + (A_shared_dyn_local[i_2_1_s_363] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_364 = 0; i_2_1_s_364 < 4; ++i_2_1_s_364) {
    if (i_2_1_s_364 < 2) {
      Y_local[((i_2_1_s_364 * 12) + 4)] = (Y_local[((i_2_1_s_364 * 12) + 4)] + (A_shared_dyn_local[i_2_1_s_364] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_365 = 0; i_2_1_s_365 < 4; ++i_2_1_s_365) {
    if (i_2_1_s_365 < 2) {
      Y_local[((i_2_1_s_365 * 12) + 5)] = (Y_local[((i_2_1_s_365 * 12) + 5)] + (A_shared_dyn_local[i_2_1_s_365] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_366 = 0; i_2_1_s_366 < 4; ++i_2_1_s_366) {
    if (i_2_1_s_366 < 2) {
      Y_local[((i_2_1_s_366 * 12) + 6)] = (Y_local[((i_2_1_s_366 * 12) + 6)] + (A_shared_dyn_local[i_2_1_s_366] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_367 = 0; i_2_1_s_367 < 4; ++i_2_1_s_367) {
    if (i_2_1_s_367 < 2) {
      Y_local[((i_2_1_s_367 * 12) + 7)] = (Y_local[((i_2_1_s_367 * 12) + 7)] + (A_shared_dyn_local[i_2_1_s_367] * B_shared_dyn_local[7]));
    }
  }
  for (int i_2_1_s_368 = 0; i_2_1_s_368 < 4; ++i_2_1_s_368) {
    if (i_2_1_s_368 < 2) {
      Y_local[((i_2_1_s_368 * 12) + 8)] = (Y_local[((i_2_1_s_368 * 12) + 8)] + (A_shared_dyn_local[i_2_1_s_368] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_369 = 0; i_2_1_s_369 < 4; ++i_2_1_s_369) {
    if (i_2_1_s_369 < 2) {
      Y_local[((i_2_1_s_369 * 12) + 9)] = (Y_local[((i_2_1_s_369 * 12) + 9)] + (A_shared_dyn_local[i_2_1_s_369] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_370 = 0; i_2_1_s_370 < 4; ++i_2_1_s_370) {
    if (i_2_1_s_370 < 2) {
      Y_local[((i_2_1_s_370 * 12) + 10)] = (Y_local[((i_2_1_s_370 * 12) + 10)] + (A_shared_dyn_local[i_2_1_s_370] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_371 = 0; i_2_1_s_371 < 4; ++i_2_1_s_371) {
    if (i_2_1_s_371 < 2) {
      Y_local[((i_2_1_s_371 * 12) + 11)] = (Y_local[((i_2_1_s_371 * 12) + 11)] + (A_shared_dyn_local[i_2_1_s_371] * B_shared_dyn_local[11]));
    }
  }
  for (int i_2_1_s_372 = 0; i_2_1_s_372 < 4; ++i_2_1_s_372) {
    if (i_2_1_s_372 < 2) {
      Y_local[(i_2_1_s_372 * 12)] = (Y_local[(i_2_1_s_372 * 12)] + (A_shared_dyn_local[(i_2_1_s_372 + 2)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_373 = 0; i_2_1_s_373 < 4; ++i_2_1_s_373) {
    if (i_2_1_s_373 < 2) {
      Y_local[((i_2_1_s_373 * 12) + 1)] = (Y_local[((i_2_1_s_373 * 12) + 1)] + (A_shared_dyn_local[(i_2_1_s_373 + 2)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_374 = 0; i_2_1_s_374 < 4; ++i_2_1_s_374) {
    if (i_2_1_s_374 < 2) {
      Y_local[((i_2_1_s_374 * 12) + 2)] = (Y_local[((i_2_1_s_374 * 12) + 2)] + (A_shared_dyn_local[(i_2_1_s_374 + 2)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_375 = 0; i_2_1_s_375 < 4; ++i_2_1_s_375) {
    if (i_2_1_s_375 < 2) {
      Y_local[((i_2_1_s_375 * 12) + 3)] = (Y_local[((i_2_1_s_375 * 12) + 3)] + (A_shared_dyn_local[(i_2_1_s_375 + 2)] * B_shared_dyn_local[15]));
    }
  }
  for (int i_2_1_s_376 = 0; i_2_1_s_376 < 4; ++i_2_1_s_376) {
    if (i_2_1_s_376 < 2) {
      Y_local[((i_2_1_s_376 * 12) + 4)] = (Y_local[((i_2_1_s_376 * 12) + 4)] + (A_shared_dyn_local[(i_2_1_s_376 + 2)] * B_shared_dyn_local[16]));
    }
  }
  for (int i_2_1_s_377 = 0; i_2_1_s_377 < 4; ++i_2_1_s_377) {
    if (i_2_1_s_377 < 2) {
      Y_local[((i_2_1_s_377 * 12) + 5)] = (Y_local[((i_2_1_s_377 * 12) + 5)] + (A_shared_dyn_local[(i_2_1_s_377 + 2)] * B_shared_dyn_local[17]));
    }
  }
  for (int i_2_1_s_378 = 0; i_2_1_s_378 < 4; ++i_2_1_s_378) {
    if (i_2_1_s_378 < 2) {
      Y_local[((i_2_1_s_378 * 12) + 6)] = (Y_local[((i_2_1_s_378 * 12) + 6)] + (A_shared_dyn_local[(i_2_1_s_378 + 2)] * B_shared_dyn_local[18]));
    }
  }
  for (int i_2_1_s_379 = 0; i_2_1_s_379 < 4; ++i_2_1_s_379) {
    if (i_2_1_s_379 < 2) {
      Y_local[((i_2_1_s_379 * 12) + 7)] = (Y_local[((i_2_1_s_379 * 12) + 7)] + (A_shared_dyn_local[(i_2_1_s_379 + 2)] * B_shared_dyn_local[19]));
    }
  }
  for (int i_2_1_s_380 = 0; i_2_1_s_380 < 4; ++i_2_1_s_380) {
    if (i_2_1_s_380 < 2) {
      Y_local[((i_2_1_s_380 * 12) + 8)] = (Y_local[((i_2_1_s_380 * 12) + 8)] + (A_shared_dyn_local[(i_2_1_s_380 + 2)] * B_shared_dyn_local[20]));
    }
  }
  for (int i_2_1_s_381 = 0; i_2_1_s_381 < 4; ++i_2_1_s_381) {
    if (i_2_1_s_381 < 2) {
      Y_local[((i_2_1_s_381 * 12) + 9)] = (Y_local[((i_2_1_s_381 * 12) + 9)] + (A_shared_dyn_local[(i_2_1_s_381 + 2)] * B_shared_dyn_local[21]));
    }
  }
  for (int i_2_1_s_382 = 0; i_2_1_s_382 < 4; ++i_2_1_s_382) {
    if (i_2_1_s_382 < 2) {
      Y_local[((i_2_1_s_382 * 12) + 10)] = (Y_local[((i_2_1_s_382 * 12) + 10)] + (A_shared_dyn_local[(i_2_1_s_382 + 2)] * B_shared_dyn_local[22]));
    }
  }
  for (int i_2_1_s_383 = 0; i_2_1_s_383 < 4; ++i_2_1_s_383) {
    if (i_2_1_s_383 < 2) {
      Y_local[((i_2_1_s_383 * 12) + 11)] = (Y_local[((i_2_1_s_383 * 12) + 11)] + (A_shared_dyn_local[(i_2_1_s_383 + 2)] * B_shared_dyn_local[23]));
    }
  }
  for (int ax1_0_32 = 0; ax1_0_32 < 3; ++ax1_0_32) {
    *(float4*)(Y + (((((((((int)blockIdx.x) >> 3) * 24576) + (((((int)threadIdx.x) & 63) >> 1) * 768)) + ((((int)blockIdx.x) & 7) * 48)) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_32 * 4))) = *(float4*)(Y_local + (ax1_0_32 * 4));
  }
  for (int ax1_0_33 = 0; ax1_0_33 < 3; ++ax1_0_33) {
    *(float4*)(Y + ((((((((((int)blockIdx.x) >> 3) * 24576) + (((((int)threadIdx.x) & 63) >> 1) * 768)) + ((((int)blockIdx.x) & 7) * 48)) + ((((int)threadIdx.x) >> 6) * 24)) + ((((int)threadIdx.x) & 1) * 12)) + (ax1_0_33 * 4)) + 384)) = *(float4*)(Y_local + ((ax1_0_33 * 4) + 12));
  }
}


