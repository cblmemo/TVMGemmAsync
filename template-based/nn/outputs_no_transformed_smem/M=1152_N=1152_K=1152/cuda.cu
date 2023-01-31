
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
extern "C" __global__ void __launch_bounds__(216) main_kernel0(float* __restrict__ A, float* __restrict__ B, float* __restrict__ Y) {
  extern __shared__ uchar buf_dyn_shmem[];
  float Y_local[96];
  float A_shared_dyn_local[12];
  float B_shared_dyn_local[32];
  Y_local[0] = 0.000000e+00f;
  Y_local[16] = 0.000000e+00f;
  Y_local[32] = 0.000000e+00f;
  Y_local[48] = 0.000000e+00f;
  Y_local[64] = 0.000000e+00f;
  Y_local[80] = 0.000000e+00f;
  Y_local[1] = 0.000000e+00f;
  Y_local[17] = 0.000000e+00f;
  Y_local[33] = 0.000000e+00f;
  Y_local[49] = 0.000000e+00f;
  Y_local[65] = 0.000000e+00f;
  Y_local[81] = 0.000000e+00f;
  Y_local[2] = 0.000000e+00f;
  Y_local[18] = 0.000000e+00f;
  Y_local[34] = 0.000000e+00f;
  Y_local[50] = 0.000000e+00f;
  Y_local[66] = 0.000000e+00f;
  Y_local[82] = 0.000000e+00f;
  Y_local[3] = 0.000000e+00f;
  Y_local[19] = 0.000000e+00f;
  Y_local[35] = 0.000000e+00f;
  Y_local[51] = 0.000000e+00f;
  Y_local[67] = 0.000000e+00f;
  Y_local[83] = 0.000000e+00f;
  Y_local[4] = 0.000000e+00f;
  Y_local[20] = 0.000000e+00f;
  Y_local[36] = 0.000000e+00f;
  Y_local[52] = 0.000000e+00f;
  Y_local[68] = 0.000000e+00f;
  Y_local[84] = 0.000000e+00f;
  Y_local[5] = 0.000000e+00f;
  Y_local[21] = 0.000000e+00f;
  Y_local[37] = 0.000000e+00f;
  Y_local[53] = 0.000000e+00f;
  Y_local[69] = 0.000000e+00f;
  Y_local[85] = 0.000000e+00f;
  Y_local[6] = 0.000000e+00f;
  Y_local[22] = 0.000000e+00f;
  Y_local[38] = 0.000000e+00f;
  Y_local[54] = 0.000000e+00f;
  Y_local[70] = 0.000000e+00f;
  Y_local[86] = 0.000000e+00f;
  Y_local[7] = 0.000000e+00f;
  Y_local[23] = 0.000000e+00f;
  Y_local[39] = 0.000000e+00f;
  Y_local[55] = 0.000000e+00f;
  Y_local[71] = 0.000000e+00f;
  Y_local[87] = 0.000000e+00f;
  Y_local[8] = 0.000000e+00f;
  Y_local[24] = 0.000000e+00f;
  Y_local[40] = 0.000000e+00f;
  Y_local[56] = 0.000000e+00f;
  Y_local[72] = 0.000000e+00f;
  Y_local[88] = 0.000000e+00f;
  Y_local[9] = 0.000000e+00f;
  Y_local[25] = 0.000000e+00f;
  Y_local[41] = 0.000000e+00f;
  Y_local[57] = 0.000000e+00f;
  Y_local[73] = 0.000000e+00f;
  Y_local[89] = 0.000000e+00f;
  Y_local[10] = 0.000000e+00f;
  Y_local[26] = 0.000000e+00f;
  Y_local[42] = 0.000000e+00f;
  Y_local[58] = 0.000000e+00f;
  Y_local[74] = 0.000000e+00f;
  Y_local[90] = 0.000000e+00f;
  Y_local[11] = 0.000000e+00f;
  Y_local[27] = 0.000000e+00f;
  Y_local[43] = 0.000000e+00f;
  Y_local[59] = 0.000000e+00f;
  Y_local[75] = 0.000000e+00f;
  Y_local[91] = 0.000000e+00f;
  Y_local[12] = 0.000000e+00f;
  Y_local[28] = 0.000000e+00f;
  Y_local[44] = 0.000000e+00f;
  Y_local[60] = 0.000000e+00f;
  Y_local[76] = 0.000000e+00f;
  Y_local[92] = 0.000000e+00f;
  Y_local[13] = 0.000000e+00f;
  Y_local[29] = 0.000000e+00f;
  Y_local[45] = 0.000000e+00f;
  Y_local[61] = 0.000000e+00f;
  Y_local[77] = 0.000000e+00f;
  Y_local[93] = 0.000000e+00f;
  Y_local[14] = 0.000000e+00f;
  Y_local[30] = 0.000000e+00f;
  Y_local[46] = 0.000000e+00f;
  Y_local[62] = 0.000000e+00f;
  Y_local[78] = 0.000000e+00f;
  Y_local[94] = 0.000000e+00f;
  Y_local[15] = 0.000000e+00f;
  Y_local[31] = 0.000000e+00f;
  Y_local[47] = 0.000000e+00f;
  Y_local[63] = 0.000000e+00f;
  Y_local[79] = 0.000000e+00f;
  Y_local[95] = 0.000000e+00f;
  for (int ax0_ax1_fused_2_s = 0; ax0_ax1_fused_2_s < 3; ++ax0_ax1_fused_2_s) {
    if (((int)threadIdx.x) < 192) {

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + ((((int)threadIdx.x) * 12) + (ax0_ax1_fused_2_s * 4))))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(A + ((((((int)blockIdx.x) >> 3) * 165888) + ((((((int)threadIdx.x) * 3) + ax0_ax1_fused_2_s) >> 2) * 1152)) + (((((int)threadIdx.x) * 3) + ax0_ax1_fused_2_s) & 3)))), "n"(4)
    );
  }
    }
  }
  for (int ax0_ax1_fused_2_s_1 = 0; ax0_ax1_fused_2_s_1 < 3; ++ax0_ax1_fused_2_s_1) {
    if (((int)threadIdx.x) < 192) {

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + ((((((((((int)threadIdx.x) / 48) * 768) + (((((((int)blockIdx.x) & 7) * 9) + ((((((int)threadIdx.x) % 48) * 3) + ax0_ax1_fused_2_s_1) >> 4)) >> 2) * 256)) + (((((((int)threadIdx.x) * 3) + ax0_ax1_fused_2_s_1) & 7) >> 2) * 128)) + (((((((int)blockIdx.x) & 7) * 2) + ((((((int)threadIdx.x) % 48) * 3) + ax0_ax1_fused_2_s_1) >> 3)) & 7) * 16)) + ((((((int)threadIdx.x) * 3) + ax0_ax1_fused_2_s_1) & 3) * 4)) + 11520) - ((((((int)blockIdx.x) & 7) * 144) >> 6) * 256))))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(B + (((((((int)threadIdx.x) / 48) * 1152) + ((((int)blockIdx.x) & 7) * 144)) + ((((int)threadIdx.x) % 48) * 3)) + ax0_ax1_fused_2_s_1))), "n"(4)
    );
  }
    }
  }
__asm__ __volatile__("cp.async.commit_group;");

  for (int ax0_ax1_fused_2_s_2 = 0; ax0_ax1_fused_2_s_2 < 3; ++ax0_ax1_fused_2_s_2) {
    if (((int)threadIdx.x) < 192) {

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + (((((int)threadIdx.x) * 12) + (ax0_ax1_fused_2_s_2 * 4)) + 2304)))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(A + (((((((int)blockIdx.x) >> 3) * 165888) + ((((((int)threadIdx.x) * 3) + ax0_ax1_fused_2_s_2) >> 2) * 1152)) + (((((int)threadIdx.x) * 3) + ax0_ax1_fused_2_s_2) & 3)) + 4))), "n"(4)
    );
  }
    }
  }
  for (int ax0_ax1_fused_2_s_3 = 0; ax0_ax1_fused_2_s_3 < 3; ++ax0_ax1_fused_2_s_3) {
    if (((int)threadIdx.x) < 192) {

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + ((((((((((int)threadIdx.x) / 48) * 768) + (((((((int)blockIdx.x) & 7) * 9) + ((((((int)threadIdx.x) % 48) * 3) + ax0_ax1_fused_2_s_3) >> 4)) >> 2) * 256)) + (((((((int)threadIdx.x) * 3) + ax0_ax1_fused_2_s_3) & 7) >> 2) * 128)) + (((((((int)blockIdx.x) & 7) * 2) + ((((((int)threadIdx.x) % 48) * 3) + ax0_ax1_fused_2_s_3) >> 3)) & 7) * 16)) + ((((((int)threadIdx.x) * 3) + ax0_ax1_fused_2_s_3) & 3) * 4)) + 14592) - ((((((int)blockIdx.x) & 7) * 144) >> 6) * 256))))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(B + ((((((((int)threadIdx.x) / 48) * 1152) + ((((int)blockIdx.x) & 7) * 144)) + ((((int)threadIdx.x) % 48) * 3)) + ax0_ax1_fused_2_s_3) + 4608))), "n"(4)
    );
  }
    }
  }
__asm__ __volatile__("cp.async.commit_group;");

  for (int ax0_ax1_fused_2_s_4 = 0; ax0_ax1_fused_2_s_4 < 3; ++ax0_ax1_fused_2_s_4) {
    if (((int)threadIdx.x) < 192) {

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + (((((int)threadIdx.x) * 12) + (ax0_ax1_fused_2_s_4 * 4)) + 4608)))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(A + (((((((int)blockIdx.x) >> 3) * 165888) + ((((((int)threadIdx.x) * 3) + ax0_ax1_fused_2_s_4) >> 2) * 1152)) + (((((int)threadIdx.x) * 3) + ax0_ax1_fused_2_s_4) & 3)) + 8))), "n"(4)
    );
  }
    }
  }
  for (int ax0_ax1_fused_2_s_5 = 0; ax0_ax1_fused_2_s_5 < 3; ++ax0_ax1_fused_2_s_5) {
    if (((int)threadIdx.x) < 192) {

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + ((((((((((int)threadIdx.x) / 48) * 768) + (((((((int)blockIdx.x) & 7) * 9) + ((((((int)threadIdx.x) % 48) * 3) + ax0_ax1_fused_2_s_5) >> 4)) >> 2) * 256)) + (((((((int)threadIdx.x) * 3) + ax0_ax1_fused_2_s_5) & 7) >> 2) * 128)) + (((((((int)blockIdx.x) & 7) * 2) + ((((((int)threadIdx.x) % 48) * 3) + ax0_ax1_fused_2_s_5) >> 3)) & 7) * 16)) + ((((((int)threadIdx.x) * 3) + ax0_ax1_fused_2_s_5) & 3) * 4)) + 17664) - ((((((int)blockIdx.x) & 7) * 144) >> 6) * 256))))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(B + ((((((((int)threadIdx.x) / 48) * 1152) + ((((int)blockIdx.x) & 7) * 144)) + ((((int)threadIdx.x) % 48) * 3)) + ax0_ax1_fused_2_s_5) + 9216))), "n"(4)
    );
  }
    }
  }
__asm__ __volatile__("cp.async.commit_group;");

  for (int ax0_ax1_fused_2_s_6 = 0; ax0_ax1_fused_2_s_6 < 3; ++ax0_ax1_fused_2_s_6) {
    if (((int)threadIdx.x) < 192) {

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + (((((int)threadIdx.x) * 12) + (ax0_ax1_fused_2_s_6 * 4)) + 6912)))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(A + (((((((int)blockIdx.x) >> 3) * 165888) + ((((((int)threadIdx.x) * 3) + ax0_ax1_fused_2_s_6) >> 2) * 1152)) + (((((int)threadIdx.x) * 3) + ax0_ax1_fused_2_s_6) & 3)) + 12))), "n"(4)
    );
  }
    }
  }
  for (int ax0_ax1_fused_2_s_7 = 0; ax0_ax1_fused_2_s_7 < 3; ++ax0_ax1_fused_2_s_7) {
    if (((int)threadIdx.x) < 192) {

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + ((((((((((int)threadIdx.x) / 48) * 768) + (((((((int)blockIdx.x) & 7) * 9) + ((((((int)threadIdx.x) % 48) * 3) + ax0_ax1_fused_2_s_7) >> 4)) >> 2) * 256)) + (((((((int)threadIdx.x) * 3) + ax0_ax1_fused_2_s_7) & 7) >> 2) * 128)) + (((((((int)blockIdx.x) & 7) * 2) + ((((((int)threadIdx.x) % 48) * 3) + ax0_ax1_fused_2_s_7) >> 3)) & 7) * 16)) + ((((((int)threadIdx.x) * 3) + ax0_ax1_fused_2_s_7) & 3) * 4)) + 20736) - ((((((int)blockIdx.x) & 7) * 144) >> 6) * 256))))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(B + ((((((((int)threadIdx.x) / 48) * 1152) + ((((int)blockIdx.x) & 7) * 144)) + ((((int)threadIdx.x) % 48) * 3)) + ax0_ax1_fused_2_s_7) + 13824))), "n"(4)
    );
  }
    }
  }
__asm__ __volatile__("cp.async.commit_group;");

__asm__ __volatile__("cp.async.wait_group 3;");

  __syncthreads();
  for (int ax0_0 = 0; ax0_0 < 2; ++ax0_0) {
    for (int ax0_1_s = 0; ax0_1_s < 4; ++ax0_1_s) {
      if (((ax0_0 * 2) + (ax0_1_s >> 1)) < 3) {
        A_shared_dyn_local[((ax0_0 * 4) + ax0_1_s)] = ((float*)buf_dyn_shmem)[(((((((int)threadIdx.x) / 27) * 72) + ((((int)threadIdx.x) % 3) * 24)) + (ax0_0 * 16)) + (ax0_1_s * 4))];
      }
    }
  }
  for (int ax1_0 = 0; ax1_0 < 4; ++ax1_0) {
    *(float4*)(B_shared_dyn_local + (ax1_0 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((int)blockIdx.x) & 7) * 144) + (((((int)threadIdx.x) % 27) / 3) * 16)) + (ax1_0 * 4)) >> 6) * 64) + ((ax1_0 & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 18) + (((((int)threadIdx.x) % 27) / 3) * 2)) + (ax1_0 >> 1)) & 7) * 4)) + 2880) - ((((((int)blockIdx.x) & 7) * 144) >> 6) * 64)));
  }
  for (int k_0 = 0; k_0 < 284; ++k_0) {
    __syncthreads();
    for (int ax0_ax1_fused_2_s_8 = 0; ax0_ax1_fused_2_s_8 < 3; ++ax0_ax1_fused_2_s_8) {
      if (((int)threadIdx.x) < 192) {

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + (((((k_0 + 4) % 5) * 2304) + (((int)threadIdx.x) * 12)) + (ax0_ax1_fused_2_s_8 * 4))))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(A + ((((((((int)blockIdx.x) >> 3) * 165888) + ((((((int)threadIdx.x) * 3) + ax0_ax1_fused_2_s_8) >> 2) * 1152)) + (k_0 * 4)) + (((((int)threadIdx.x) * 3) + ax0_ax1_fused_2_s_8) & 3)) + 16))), "n"(4)
    );
  }
      }
    }
    for (int ax0_ax1_fused_2_s_9 = 0; ax0_ax1_fused_2_s_9 < 3; ++ax0_ax1_fused_2_s_9) {
      if (((int)threadIdx.x) < 192) {

  {
    unsigned int addr;
    __asm__ __volatile__(
      "{ .reg .u64 addr; cvta.to.shared.u64 addr, %1; cvt.u32.u64 %0, addr; }\n"
      : "=r"(addr)
      : "l"((void *)(buf_dyn_shmem + ((((((((((k_0 + 4) % 5) * 3072) + ((((int)threadIdx.x) / 48) * 768)) + (((((((int)blockIdx.x) & 7) * 9) + ((((((int)threadIdx.x) % 48) * 3) + ax0_ax1_fused_2_s_9) >> 4)) >> 2) * 256)) + (((((((int)threadIdx.x) * 3) + ax0_ax1_fused_2_s_9) & 7) >> 2) * 128)) + (((((((int)blockIdx.x) & 7) * 2) + ((((((int)threadIdx.x) % 48) * 3) + ax0_ax1_fused_2_s_9) >> 3)) & 7) * 16)) + ((((((int)threadIdx.x) * 3) + ax0_ax1_fused_2_s_9) & 3) * 4)) + 11520) - ((((((int)blockIdx.x) & 7) * 144) >> 6) * 256))))
    );
    __asm__ __volatile__(
      "cp.async.ca.shared.global [%0], [%1], %2;"
       :: "r"(addr), "l"((void*)(B + ((((((k_0 * 4608) + ((((int)threadIdx.x) / 48) * 1152)) + ((((int)blockIdx.x) & 7) * 144)) + ((((int)threadIdx.x) % 48) * 3)) + ax0_ax1_fused_2_s_9) + 18432))), "n"(4)
    );
  }
      }
    }
__asm__ __volatile__("cp.async.commit_group;");

__asm__ __volatile__("cp.async.wait_group 3;");

    __syncthreads();
    for (int ax0_0_1 = 0; ax0_0_1 < 2; ++ax0_0_1) {
      for (int ax0_1_s_1 = 0; ax0_1_s_1 < 4; ++ax0_1_s_1) {
        if (((ax0_0_1 * 2) + (ax0_1_s_1 >> 1)) < 3) {
          A_shared_dyn_local[(((ax0_0_1 * 4) + ax0_1_s_1) + 6)] = ((float*)buf_dyn_shmem)[(((((((k_0 % 5) * 576) + ((((int)threadIdx.x) / 27) * 72)) + ((((int)threadIdx.x) % 3) * 24)) + (ax0_0_1 * 16)) + (ax0_1_s_1 * 4)) + 1)];
        }
      }
    }
    for (int ax1_0_1 = 0; ax1_0_1 < 4; ++ax1_0_1) {
      *(float4*)(B_shared_dyn_local + ((ax1_0_1 * 4) + 16)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((k_0 % 5) * 768) + ((((((((int)blockIdx.x) & 7) * 144) + (((((int)threadIdx.x) % 27) / 3) * 16)) + (ax1_0_1 * 4)) >> 6) * 64)) + ((ax1_0_1 & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 18) + (((((int)threadIdx.x) % 27) / 3) * 2)) + (ax1_0_1 >> 1)) & 7) * 4)) + 3072) - ((((((int)blockIdx.x) & 7) * 144) >> 6) * 64)));
    }
    for (int i_2_1_s = 0; i_2_1_s < 4; ++i_2_1_s) {
      Y_local[(i_2_1_s * 16)] = (Y_local[(i_2_1_s * 16)] + (A_shared_dyn_local[i_2_1_s] * B_shared_dyn_local[0]));
    }
    for (int i_2_1_s_1 = 0; i_2_1_s_1 < 4; ++i_2_1_s_1) {
      if (i_2_1_s_1 < 2) {
        Y_local[((i_2_1_s_1 * 16) + 64)] = (Y_local[((i_2_1_s_1 * 16) + 64)] + (A_shared_dyn_local[(i_2_1_s_1 + 4)] * B_shared_dyn_local[0]));
      }
    }
    for (int i_2_1_s_2 = 0; i_2_1_s_2 < 4; ++i_2_1_s_2) {
      Y_local[((i_2_1_s_2 * 16) + 1)] = (Y_local[((i_2_1_s_2 * 16) + 1)] + (A_shared_dyn_local[i_2_1_s_2] * B_shared_dyn_local[1]));
    }
    for (int i_2_1_s_3 = 0; i_2_1_s_3 < 4; ++i_2_1_s_3) {
      if (i_2_1_s_3 < 2) {
        Y_local[((i_2_1_s_3 * 16) + 65)] = (Y_local[((i_2_1_s_3 * 16) + 65)] + (A_shared_dyn_local[(i_2_1_s_3 + 4)] * B_shared_dyn_local[1]));
      }
    }
    for (int i_2_1_s_4 = 0; i_2_1_s_4 < 4; ++i_2_1_s_4) {
      Y_local[((i_2_1_s_4 * 16) + 2)] = (Y_local[((i_2_1_s_4 * 16) + 2)] + (A_shared_dyn_local[i_2_1_s_4] * B_shared_dyn_local[2]));
    }
    for (int i_2_1_s_5 = 0; i_2_1_s_5 < 4; ++i_2_1_s_5) {
      if (i_2_1_s_5 < 2) {
        Y_local[((i_2_1_s_5 * 16) + 66)] = (Y_local[((i_2_1_s_5 * 16) + 66)] + (A_shared_dyn_local[(i_2_1_s_5 + 4)] * B_shared_dyn_local[2]));
      }
    }
    for (int i_2_1_s_6 = 0; i_2_1_s_6 < 4; ++i_2_1_s_6) {
      Y_local[((i_2_1_s_6 * 16) + 3)] = (Y_local[((i_2_1_s_6 * 16) + 3)] + (A_shared_dyn_local[i_2_1_s_6] * B_shared_dyn_local[3]));
    }
    for (int i_2_1_s_7 = 0; i_2_1_s_7 < 4; ++i_2_1_s_7) {
      if (i_2_1_s_7 < 2) {
        Y_local[((i_2_1_s_7 * 16) + 67)] = (Y_local[((i_2_1_s_7 * 16) + 67)] + (A_shared_dyn_local[(i_2_1_s_7 + 4)] * B_shared_dyn_local[3]));
      }
    }
    for (int i_2_1_s_8 = 0; i_2_1_s_8 < 4; ++i_2_1_s_8) {
      Y_local[((i_2_1_s_8 * 16) + 4)] = (Y_local[((i_2_1_s_8 * 16) + 4)] + (A_shared_dyn_local[i_2_1_s_8] * B_shared_dyn_local[4]));
    }
    for (int i_2_1_s_9 = 0; i_2_1_s_9 < 4; ++i_2_1_s_9) {
      if (i_2_1_s_9 < 2) {
        Y_local[((i_2_1_s_9 * 16) + 68)] = (Y_local[((i_2_1_s_9 * 16) + 68)] + (A_shared_dyn_local[(i_2_1_s_9 + 4)] * B_shared_dyn_local[4]));
      }
    }
    for (int i_2_1_s_10 = 0; i_2_1_s_10 < 4; ++i_2_1_s_10) {
      Y_local[((i_2_1_s_10 * 16) + 5)] = (Y_local[((i_2_1_s_10 * 16) + 5)] + (A_shared_dyn_local[i_2_1_s_10] * B_shared_dyn_local[5]));
    }
    for (int i_2_1_s_11 = 0; i_2_1_s_11 < 4; ++i_2_1_s_11) {
      if (i_2_1_s_11 < 2) {
        Y_local[((i_2_1_s_11 * 16) + 69)] = (Y_local[((i_2_1_s_11 * 16) + 69)] + (A_shared_dyn_local[(i_2_1_s_11 + 4)] * B_shared_dyn_local[5]));
      }
    }
    for (int i_2_1_s_12 = 0; i_2_1_s_12 < 4; ++i_2_1_s_12) {
      Y_local[((i_2_1_s_12 * 16) + 6)] = (Y_local[((i_2_1_s_12 * 16) + 6)] + (A_shared_dyn_local[i_2_1_s_12] * B_shared_dyn_local[6]));
    }
    for (int i_2_1_s_13 = 0; i_2_1_s_13 < 4; ++i_2_1_s_13) {
      if (i_2_1_s_13 < 2) {
        Y_local[((i_2_1_s_13 * 16) + 70)] = (Y_local[((i_2_1_s_13 * 16) + 70)] + (A_shared_dyn_local[(i_2_1_s_13 + 4)] * B_shared_dyn_local[6]));
      }
    }
    for (int i_2_1_s_14 = 0; i_2_1_s_14 < 4; ++i_2_1_s_14) {
      Y_local[((i_2_1_s_14 * 16) + 7)] = (Y_local[((i_2_1_s_14 * 16) + 7)] + (A_shared_dyn_local[i_2_1_s_14] * B_shared_dyn_local[7]));
    }
    for (int i_2_1_s_15 = 0; i_2_1_s_15 < 4; ++i_2_1_s_15) {
      if (i_2_1_s_15 < 2) {
        Y_local[((i_2_1_s_15 * 16) + 71)] = (Y_local[((i_2_1_s_15 * 16) + 71)] + (A_shared_dyn_local[(i_2_1_s_15 + 4)] * B_shared_dyn_local[7]));
      }
    }
    for (int i_2_1_s_16 = 0; i_2_1_s_16 < 4; ++i_2_1_s_16) {
      Y_local[((i_2_1_s_16 * 16) + 8)] = (Y_local[((i_2_1_s_16 * 16) + 8)] + (A_shared_dyn_local[i_2_1_s_16] * B_shared_dyn_local[8]));
    }
    for (int i_2_1_s_17 = 0; i_2_1_s_17 < 4; ++i_2_1_s_17) {
      if (i_2_1_s_17 < 2) {
        Y_local[((i_2_1_s_17 * 16) + 72)] = (Y_local[((i_2_1_s_17 * 16) + 72)] + (A_shared_dyn_local[(i_2_1_s_17 + 4)] * B_shared_dyn_local[8]));
      }
    }
    for (int i_2_1_s_18 = 0; i_2_1_s_18 < 4; ++i_2_1_s_18) {
      Y_local[((i_2_1_s_18 * 16) + 9)] = (Y_local[((i_2_1_s_18 * 16) + 9)] + (A_shared_dyn_local[i_2_1_s_18] * B_shared_dyn_local[9]));
    }
    for (int i_2_1_s_19 = 0; i_2_1_s_19 < 4; ++i_2_1_s_19) {
      if (i_2_1_s_19 < 2) {
        Y_local[((i_2_1_s_19 * 16) + 73)] = (Y_local[((i_2_1_s_19 * 16) + 73)] + (A_shared_dyn_local[(i_2_1_s_19 + 4)] * B_shared_dyn_local[9]));
      }
    }
    for (int i_2_1_s_20 = 0; i_2_1_s_20 < 4; ++i_2_1_s_20) {
      Y_local[((i_2_1_s_20 * 16) + 10)] = (Y_local[((i_2_1_s_20 * 16) + 10)] + (A_shared_dyn_local[i_2_1_s_20] * B_shared_dyn_local[10]));
    }
    for (int i_2_1_s_21 = 0; i_2_1_s_21 < 4; ++i_2_1_s_21) {
      if (i_2_1_s_21 < 2) {
        Y_local[((i_2_1_s_21 * 16) + 74)] = (Y_local[((i_2_1_s_21 * 16) + 74)] + (A_shared_dyn_local[(i_2_1_s_21 + 4)] * B_shared_dyn_local[10]));
      }
    }
    for (int i_2_1_s_22 = 0; i_2_1_s_22 < 4; ++i_2_1_s_22) {
      Y_local[((i_2_1_s_22 * 16) + 11)] = (Y_local[((i_2_1_s_22 * 16) + 11)] + (A_shared_dyn_local[i_2_1_s_22] * B_shared_dyn_local[11]));
    }
    for (int i_2_1_s_23 = 0; i_2_1_s_23 < 4; ++i_2_1_s_23) {
      if (i_2_1_s_23 < 2) {
        Y_local[((i_2_1_s_23 * 16) + 75)] = (Y_local[((i_2_1_s_23 * 16) + 75)] + (A_shared_dyn_local[(i_2_1_s_23 + 4)] * B_shared_dyn_local[11]));
      }
    }
    for (int i_2_1_s_24 = 0; i_2_1_s_24 < 4; ++i_2_1_s_24) {
      Y_local[((i_2_1_s_24 * 16) + 12)] = (Y_local[((i_2_1_s_24 * 16) + 12)] + (A_shared_dyn_local[i_2_1_s_24] * B_shared_dyn_local[12]));
    }
    for (int i_2_1_s_25 = 0; i_2_1_s_25 < 4; ++i_2_1_s_25) {
      if (i_2_1_s_25 < 2) {
        Y_local[((i_2_1_s_25 * 16) + 76)] = (Y_local[((i_2_1_s_25 * 16) + 76)] + (A_shared_dyn_local[(i_2_1_s_25 + 4)] * B_shared_dyn_local[12]));
      }
    }
    for (int i_2_1_s_26 = 0; i_2_1_s_26 < 4; ++i_2_1_s_26) {
      Y_local[((i_2_1_s_26 * 16) + 13)] = (Y_local[((i_2_1_s_26 * 16) + 13)] + (A_shared_dyn_local[i_2_1_s_26] * B_shared_dyn_local[13]));
    }
    for (int i_2_1_s_27 = 0; i_2_1_s_27 < 4; ++i_2_1_s_27) {
      if (i_2_1_s_27 < 2) {
        Y_local[((i_2_1_s_27 * 16) + 77)] = (Y_local[((i_2_1_s_27 * 16) + 77)] + (A_shared_dyn_local[(i_2_1_s_27 + 4)] * B_shared_dyn_local[13]));
      }
    }
    for (int i_2_1_s_28 = 0; i_2_1_s_28 < 4; ++i_2_1_s_28) {
      Y_local[((i_2_1_s_28 * 16) + 14)] = (Y_local[((i_2_1_s_28 * 16) + 14)] + (A_shared_dyn_local[i_2_1_s_28] * B_shared_dyn_local[14]));
    }
    for (int i_2_1_s_29 = 0; i_2_1_s_29 < 4; ++i_2_1_s_29) {
      if (i_2_1_s_29 < 2) {
        Y_local[((i_2_1_s_29 * 16) + 78)] = (Y_local[((i_2_1_s_29 * 16) + 78)] + (A_shared_dyn_local[(i_2_1_s_29 + 4)] * B_shared_dyn_local[14]));
      }
    }
    for (int i_2_1_s_30 = 0; i_2_1_s_30 < 4; ++i_2_1_s_30) {
      Y_local[((i_2_1_s_30 * 16) + 15)] = (Y_local[((i_2_1_s_30 * 16) + 15)] + (A_shared_dyn_local[i_2_1_s_30] * B_shared_dyn_local[15]));
    }
    for (int i_2_1_s_31 = 0; i_2_1_s_31 < 4; ++i_2_1_s_31) {
      if (i_2_1_s_31 < 2) {
        Y_local[((i_2_1_s_31 * 16) + 79)] = (Y_local[((i_2_1_s_31 * 16) + 79)] + (A_shared_dyn_local[(i_2_1_s_31 + 4)] * B_shared_dyn_local[15]));
      }
    }
    for (int ax0_0_2 = 0; ax0_0_2 < 2; ++ax0_0_2) {
      for (int ax0_1_s_2 = 0; ax0_1_s_2 < 4; ++ax0_1_s_2) {
        if (((ax0_0_2 * 2) + (ax0_1_s_2 >> 1)) < 3) {
          A_shared_dyn_local[((ax0_0_2 * 4) + ax0_1_s_2)] = ((float*)buf_dyn_shmem)[(((((((k_0 % 5) * 576) + ((((int)threadIdx.x) / 27) * 72)) + ((((int)threadIdx.x) % 3) * 24)) + (ax0_0_2 * 16)) + (ax0_1_s_2 * 4)) + 2)];
        }
      }
    }
    for (int ax1_0_2 = 0; ax1_0_2 < 4; ++ax1_0_2) {
      *(float4*)(B_shared_dyn_local + (ax1_0_2 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((k_0 % 5) * 768) + ((((((((int)blockIdx.x) & 7) * 144) + (((((int)threadIdx.x) % 27) / 3) * 16)) + (ax1_0_2 * 4)) >> 6) * 64)) + ((ax1_0_2 & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 18) + (((((int)threadIdx.x) % 27) / 3) * 2)) + (ax1_0_2 >> 1)) & 7) * 4)) + 3264) - ((((((int)blockIdx.x) & 7) * 144) >> 6) * 64)));
    }
    for (int i_2_1_s_32 = 0; i_2_1_s_32 < 4; ++i_2_1_s_32) {
      Y_local[(i_2_1_s_32 * 16)] = (Y_local[(i_2_1_s_32 * 16)] + (A_shared_dyn_local[(i_2_1_s_32 + 6)] * B_shared_dyn_local[16]));
    }
    for (int i_2_1_s_33 = 0; i_2_1_s_33 < 4; ++i_2_1_s_33) {
      if (i_2_1_s_33 < 2) {
        Y_local[((i_2_1_s_33 * 16) + 64)] = (Y_local[((i_2_1_s_33 * 16) + 64)] + (A_shared_dyn_local[(i_2_1_s_33 + 10)] * B_shared_dyn_local[16]));
      }
    }
    for (int i_2_1_s_34 = 0; i_2_1_s_34 < 4; ++i_2_1_s_34) {
      Y_local[((i_2_1_s_34 * 16) + 1)] = (Y_local[((i_2_1_s_34 * 16) + 1)] + (A_shared_dyn_local[(i_2_1_s_34 + 6)] * B_shared_dyn_local[17]));
    }
    for (int i_2_1_s_35 = 0; i_2_1_s_35 < 4; ++i_2_1_s_35) {
      if (i_2_1_s_35 < 2) {
        Y_local[((i_2_1_s_35 * 16) + 65)] = (Y_local[((i_2_1_s_35 * 16) + 65)] + (A_shared_dyn_local[(i_2_1_s_35 + 10)] * B_shared_dyn_local[17]));
      }
    }
    for (int i_2_1_s_36 = 0; i_2_1_s_36 < 4; ++i_2_1_s_36) {
      Y_local[((i_2_1_s_36 * 16) + 2)] = (Y_local[((i_2_1_s_36 * 16) + 2)] + (A_shared_dyn_local[(i_2_1_s_36 + 6)] * B_shared_dyn_local[18]));
    }
    for (int i_2_1_s_37 = 0; i_2_1_s_37 < 4; ++i_2_1_s_37) {
      if (i_2_1_s_37 < 2) {
        Y_local[((i_2_1_s_37 * 16) + 66)] = (Y_local[((i_2_1_s_37 * 16) + 66)] + (A_shared_dyn_local[(i_2_1_s_37 + 10)] * B_shared_dyn_local[18]));
      }
    }
    for (int i_2_1_s_38 = 0; i_2_1_s_38 < 4; ++i_2_1_s_38) {
      Y_local[((i_2_1_s_38 * 16) + 3)] = (Y_local[((i_2_1_s_38 * 16) + 3)] + (A_shared_dyn_local[(i_2_1_s_38 + 6)] * B_shared_dyn_local[19]));
    }
    for (int i_2_1_s_39 = 0; i_2_1_s_39 < 4; ++i_2_1_s_39) {
      if (i_2_1_s_39 < 2) {
        Y_local[((i_2_1_s_39 * 16) + 67)] = (Y_local[((i_2_1_s_39 * 16) + 67)] + (A_shared_dyn_local[(i_2_1_s_39 + 10)] * B_shared_dyn_local[19]));
      }
    }
    for (int i_2_1_s_40 = 0; i_2_1_s_40 < 4; ++i_2_1_s_40) {
      Y_local[((i_2_1_s_40 * 16) + 4)] = (Y_local[((i_2_1_s_40 * 16) + 4)] + (A_shared_dyn_local[(i_2_1_s_40 + 6)] * B_shared_dyn_local[20]));
    }
    for (int i_2_1_s_41 = 0; i_2_1_s_41 < 4; ++i_2_1_s_41) {
      if (i_2_1_s_41 < 2) {
        Y_local[((i_2_1_s_41 * 16) + 68)] = (Y_local[((i_2_1_s_41 * 16) + 68)] + (A_shared_dyn_local[(i_2_1_s_41 + 10)] * B_shared_dyn_local[20]));
      }
    }
    for (int i_2_1_s_42 = 0; i_2_1_s_42 < 4; ++i_2_1_s_42) {
      Y_local[((i_2_1_s_42 * 16) + 5)] = (Y_local[((i_2_1_s_42 * 16) + 5)] + (A_shared_dyn_local[(i_2_1_s_42 + 6)] * B_shared_dyn_local[21]));
    }
    for (int i_2_1_s_43 = 0; i_2_1_s_43 < 4; ++i_2_1_s_43) {
      if (i_2_1_s_43 < 2) {
        Y_local[((i_2_1_s_43 * 16) + 69)] = (Y_local[((i_2_1_s_43 * 16) + 69)] + (A_shared_dyn_local[(i_2_1_s_43 + 10)] * B_shared_dyn_local[21]));
      }
    }
    for (int i_2_1_s_44 = 0; i_2_1_s_44 < 4; ++i_2_1_s_44) {
      Y_local[((i_2_1_s_44 * 16) + 6)] = (Y_local[((i_2_1_s_44 * 16) + 6)] + (A_shared_dyn_local[(i_2_1_s_44 + 6)] * B_shared_dyn_local[22]));
    }
    for (int i_2_1_s_45 = 0; i_2_1_s_45 < 4; ++i_2_1_s_45) {
      if (i_2_1_s_45 < 2) {
        Y_local[((i_2_1_s_45 * 16) + 70)] = (Y_local[((i_2_1_s_45 * 16) + 70)] + (A_shared_dyn_local[(i_2_1_s_45 + 10)] * B_shared_dyn_local[22]));
      }
    }
    for (int i_2_1_s_46 = 0; i_2_1_s_46 < 4; ++i_2_1_s_46) {
      Y_local[((i_2_1_s_46 * 16) + 7)] = (Y_local[((i_2_1_s_46 * 16) + 7)] + (A_shared_dyn_local[(i_2_1_s_46 + 6)] * B_shared_dyn_local[23]));
    }
    for (int i_2_1_s_47 = 0; i_2_1_s_47 < 4; ++i_2_1_s_47) {
      if (i_2_1_s_47 < 2) {
        Y_local[((i_2_1_s_47 * 16) + 71)] = (Y_local[((i_2_1_s_47 * 16) + 71)] + (A_shared_dyn_local[(i_2_1_s_47 + 10)] * B_shared_dyn_local[23]));
      }
    }
    for (int i_2_1_s_48 = 0; i_2_1_s_48 < 4; ++i_2_1_s_48) {
      Y_local[((i_2_1_s_48 * 16) + 8)] = (Y_local[((i_2_1_s_48 * 16) + 8)] + (A_shared_dyn_local[(i_2_1_s_48 + 6)] * B_shared_dyn_local[24]));
    }
    for (int i_2_1_s_49 = 0; i_2_1_s_49 < 4; ++i_2_1_s_49) {
      if (i_2_1_s_49 < 2) {
        Y_local[((i_2_1_s_49 * 16) + 72)] = (Y_local[((i_2_1_s_49 * 16) + 72)] + (A_shared_dyn_local[(i_2_1_s_49 + 10)] * B_shared_dyn_local[24]));
      }
    }
    for (int i_2_1_s_50 = 0; i_2_1_s_50 < 4; ++i_2_1_s_50) {
      Y_local[((i_2_1_s_50 * 16) + 9)] = (Y_local[((i_2_1_s_50 * 16) + 9)] + (A_shared_dyn_local[(i_2_1_s_50 + 6)] * B_shared_dyn_local[25]));
    }
    for (int i_2_1_s_51 = 0; i_2_1_s_51 < 4; ++i_2_1_s_51) {
      if (i_2_1_s_51 < 2) {
        Y_local[((i_2_1_s_51 * 16) + 73)] = (Y_local[((i_2_1_s_51 * 16) + 73)] + (A_shared_dyn_local[(i_2_1_s_51 + 10)] * B_shared_dyn_local[25]));
      }
    }
    for (int i_2_1_s_52 = 0; i_2_1_s_52 < 4; ++i_2_1_s_52) {
      Y_local[((i_2_1_s_52 * 16) + 10)] = (Y_local[((i_2_1_s_52 * 16) + 10)] + (A_shared_dyn_local[(i_2_1_s_52 + 6)] * B_shared_dyn_local[26]));
    }
    for (int i_2_1_s_53 = 0; i_2_1_s_53 < 4; ++i_2_1_s_53) {
      if (i_2_1_s_53 < 2) {
        Y_local[((i_2_1_s_53 * 16) + 74)] = (Y_local[((i_2_1_s_53 * 16) + 74)] + (A_shared_dyn_local[(i_2_1_s_53 + 10)] * B_shared_dyn_local[26]));
      }
    }
    for (int i_2_1_s_54 = 0; i_2_1_s_54 < 4; ++i_2_1_s_54) {
      Y_local[((i_2_1_s_54 * 16) + 11)] = (Y_local[((i_2_1_s_54 * 16) + 11)] + (A_shared_dyn_local[(i_2_1_s_54 + 6)] * B_shared_dyn_local[27]));
    }
    for (int i_2_1_s_55 = 0; i_2_1_s_55 < 4; ++i_2_1_s_55) {
      if (i_2_1_s_55 < 2) {
        Y_local[((i_2_1_s_55 * 16) + 75)] = (Y_local[((i_2_1_s_55 * 16) + 75)] + (A_shared_dyn_local[(i_2_1_s_55 + 10)] * B_shared_dyn_local[27]));
      }
    }
    for (int i_2_1_s_56 = 0; i_2_1_s_56 < 4; ++i_2_1_s_56) {
      Y_local[((i_2_1_s_56 * 16) + 12)] = (Y_local[((i_2_1_s_56 * 16) + 12)] + (A_shared_dyn_local[(i_2_1_s_56 + 6)] * B_shared_dyn_local[28]));
    }
    for (int i_2_1_s_57 = 0; i_2_1_s_57 < 4; ++i_2_1_s_57) {
      if (i_2_1_s_57 < 2) {
        Y_local[((i_2_1_s_57 * 16) + 76)] = (Y_local[((i_2_1_s_57 * 16) + 76)] + (A_shared_dyn_local[(i_2_1_s_57 + 10)] * B_shared_dyn_local[28]));
      }
    }
    for (int i_2_1_s_58 = 0; i_2_1_s_58 < 4; ++i_2_1_s_58) {
      Y_local[((i_2_1_s_58 * 16) + 13)] = (Y_local[((i_2_1_s_58 * 16) + 13)] + (A_shared_dyn_local[(i_2_1_s_58 + 6)] * B_shared_dyn_local[29]));
    }
    for (int i_2_1_s_59 = 0; i_2_1_s_59 < 4; ++i_2_1_s_59) {
      if (i_2_1_s_59 < 2) {
        Y_local[((i_2_1_s_59 * 16) + 77)] = (Y_local[((i_2_1_s_59 * 16) + 77)] + (A_shared_dyn_local[(i_2_1_s_59 + 10)] * B_shared_dyn_local[29]));
      }
    }
    for (int i_2_1_s_60 = 0; i_2_1_s_60 < 4; ++i_2_1_s_60) {
      Y_local[((i_2_1_s_60 * 16) + 14)] = (Y_local[((i_2_1_s_60 * 16) + 14)] + (A_shared_dyn_local[(i_2_1_s_60 + 6)] * B_shared_dyn_local[30]));
    }
    for (int i_2_1_s_61 = 0; i_2_1_s_61 < 4; ++i_2_1_s_61) {
      if (i_2_1_s_61 < 2) {
        Y_local[((i_2_1_s_61 * 16) + 78)] = (Y_local[((i_2_1_s_61 * 16) + 78)] + (A_shared_dyn_local[(i_2_1_s_61 + 10)] * B_shared_dyn_local[30]));
      }
    }
    for (int i_2_1_s_62 = 0; i_2_1_s_62 < 4; ++i_2_1_s_62) {
      Y_local[((i_2_1_s_62 * 16) + 15)] = (Y_local[((i_2_1_s_62 * 16) + 15)] + (A_shared_dyn_local[(i_2_1_s_62 + 6)] * B_shared_dyn_local[31]));
    }
    for (int i_2_1_s_63 = 0; i_2_1_s_63 < 4; ++i_2_1_s_63) {
      if (i_2_1_s_63 < 2) {
        Y_local[((i_2_1_s_63 * 16) + 79)] = (Y_local[((i_2_1_s_63 * 16) + 79)] + (A_shared_dyn_local[(i_2_1_s_63 + 10)] * B_shared_dyn_local[31]));
      }
    }
    for (int ax0_0_3 = 0; ax0_0_3 < 2; ++ax0_0_3) {
      for (int ax0_1_s_3 = 0; ax0_1_s_3 < 4; ++ax0_1_s_3) {
        if (((ax0_0_3 * 2) + (ax0_1_s_3 >> 1)) < 3) {
          A_shared_dyn_local[(((ax0_0_3 * 4) + ax0_1_s_3) + 6)] = ((float*)buf_dyn_shmem)[(((((((k_0 % 5) * 576) + ((((int)threadIdx.x) / 27) * 72)) + ((((int)threadIdx.x) % 3) * 24)) + (ax0_0_3 * 16)) + (ax0_1_s_3 * 4)) + 3)];
        }
      }
    }
    for (int ax1_0_3 = 0; ax1_0_3 < 4; ++ax1_0_3) {
      *(float4*)(B_shared_dyn_local + ((ax1_0_3 * 4) + 16)) = *(float4*)(((float*)buf_dyn_shmem) + (((((((k_0 % 5) * 768) + ((((((((int)blockIdx.x) & 7) * 144) + (((((int)threadIdx.x) % 27) / 3) * 16)) + (ax1_0_3 * 4)) >> 6) * 64)) + ((ax1_0_3 & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 18) + (((((int)threadIdx.x) % 27) / 3) * 2)) + (ax1_0_3 >> 1)) & 7) * 4)) + 3456) - ((((((int)blockIdx.x) & 7) * 144) >> 6) * 64)));
    }
    for (int i_2_1_s_64 = 0; i_2_1_s_64 < 4; ++i_2_1_s_64) {
      Y_local[(i_2_1_s_64 * 16)] = (Y_local[(i_2_1_s_64 * 16)] + (A_shared_dyn_local[i_2_1_s_64] * B_shared_dyn_local[0]));
    }
    for (int i_2_1_s_65 = 0; i_2_1_s_65 < 4; ++i_2_1_s_65) {
      if (i_2_1_s_65 < 2) {
        Y_local[((i_2_1_s_65 * 16) + 64)] = (Y_local[((i_2_1_s_65 * 16) + 64)] + (A_shared_dyn_local[(i_2_1_s_65 + 4)] * B_shared_dyn_local[0]));
      }
    }
    for (int i_2_1_s_66 = 0; i_2_1_s_66 < 4; ++i_2_1_s_66) {
      Y_local[((i_2_1_s_66 * 16) + 1)] = (Y_local[((i_2_1_s_66 * 16) + 1)] + (A_shared_dyn_local[i_2_1_s_66] * B_shared_dyn_local[1]));
    }
    for (int i_2_1_s_67 = 0; i_2_1_s_67 < 4; ++i_2_1_s_67) {
      if (i_2_1_s_67 < 2) {
        Y_local[((i_2_1_s_67 * 16) + 65)] = (Y_local[((i_2_1_s_67 * 16) + 65)] + (A_shared_dyn_local[(i_2_1_s_67 + 4)] * B_shared_dyn_local[1]));
      }
    }
    for (int i_2_1_s_68 = 0; i_2_1_s_68 < 4; ++i_2_1_s_68) {
      Y_local[((i_2_1_s_68 * 16) + 2)] = (Y_local[((i_2_1_s_68 * 16) + 2)] + (A_shared_dyn_local[i_2_1_s_68] * B_shared_dyn_local[2]));
    }
    for (int i_2_1_s_69 = 0; i_2_1_s_69 < 4; ++i_2_1_s_69) {
      if (i_2_1_s_69 < 2) {
        Y_local[((i_2_1_s_69 * 16) + 66)] = (Y_local[((i_2_1_s_69 * 16) + 66)] + (A_shared_dyn_local[(i_2_1_s_69 + 4)] * B_shared_dyn_local[2]));
      }
    }
    for (int i_2_1_s_70 = 0; i_2_1_s_70 < 4; ++i_2_1_s_70) {
      Y_local[((i_2_1_s_70 * 16) + 3)] = (Y_local[((i_2_1_s_70 * 16) + 3)] + (A_shared_dyn_local[i_2_1_s_70] * B_shared_dyn_local[3]));
    }
    for (int i_2_1_s_71 = 0; i_2_1_s_71 < 4; ++i_2_1_s_71) {
      if (i_2_1_s_71 < 2) {
        Y_local[((i_2_1_s_71 * 16) + 67)] = (Y_local[((i_2_1_s_71 * 16) + 67)] + (A_shared_dyn_local[(i_2_1_s_71 + 4)] * B_shared_dyn_local[3]));
      }
    }
    for (int i_2_1_s_72 = 0; i_2_1_s_72 < 4; ++i_2_1_s_72) {
      Y_local[((i_2_1_s_72 * 16) + 4)] = (Y_local[((i_2_1_s_72 * 16) + 4)] + (A_shared_dyn_local[i_2_1_s_72] * B_shared_dyn_local[4]));
    }
    for (int i_2_1_s_73 = 0; i_2_1_s_73 < 4; ++i_2_1_s_73) {
      if (i_2_1_s_73 < 2) {
        Y_local[((i_2_1_s_73 * 16) + 68)] = (Y_local[((i_2_1_s_73 * 16) + 68)] + (A_shared_dyn_local[(i_2_1_s_73 + 4)] * B_shared_dyn_local[4]));
      }
    }
    for (int i_2_1_s_74 = 0; i_2_1_s_74 < 4; ++i_2_1_s_74) {
      Y_local[((i_2_1_s_74 * 16) + 5)] = (Y_local[((i_2_1_s_74 * 16) + 5)] + (A_shared_dyn_local[i_2_1_s_74] * B_shared_dyn_local[5]));
    }
    for (int i_2_1_s_75 = 0; i_2_1_s_75 < 4; ++i_2_1_s_75) {
      if (i_2_1_s_75 < 2) {
        Y_local[((i_2_1_s_75 * 16) + 69)] = (Y_local[((i_2_1_s_75 * 16) + 69)] + (A_shared_dyn_local[(i_2_1_s_75 + 4)] * B_shared_dyn_local[5]));
      }
    }
    for (int i_2_1_s_76 = 0; i_2_1_s_76 < 4; ++i_2_1_s_76) {
      Y_local[((i_2_1_s_76 * 16) + 6)] = (Y_local[((i_2_1_s_76 * 16) + 6)] + (A_shared_dyn_local[i_2_1_s_76] * B_shared_dyn_local[6]));
    }
    for (int i_2_1_s_77 = 0; i_2_1_s_77 < 4; ++i_2_1_s_77) {
      if (i_2_1_s_77 < 2) {
        Y_local[((i_2_1_s_77 * 16) + 70)] = (Y_local[((i_2_1_s_77 * 16) + 70)] + (A_shared_dyn_local[(i_2_1_s_77 + 4)] * B_shared_dyn_local[6]));
      }
    }
    for (int i_2_1_s_78 = 0; i_2_1_s_78 < 4; ++i_2_1_s_78) {
      Y_local[((i_2_1_s_78 * 16) + 7)] = (Y_local[((i_2_1_s_78 * 16) + 7)] + (A_shared_dyn_local[i_2_1_s_78] * B_shared_dyn_local[7]));
    }
    for (int i_2_1_s_79 = 0; i_2_1_s_79 < 4; ++i_2_1_s_79) {
      if (i_2_1_s_79 < 2) {
        Y_local[((i_2_1_s_79 * 16) + 71)] = (Y_local[((i_2_1_s_79 * 16) + 71)] + (A_shared_dyn_local[(i_2_1_s_79 + 4)] * B_shared_dyn_local[7]));
      }
    }
    for (int i_2_1_s_80 = 0; i_2_1_s_80 < 4; ++i_2_1_s_80) {
      Y_local[((i_2_1_s_80 * 16) + 8)] = (Y_local[((i_2_1_s_80 * 16) + 8)] + (A_shared_dyn_local[i_2_1_s_80] * B_shared_dyn_local[8]));
    }
    for (int i_2_1_s_81 = 0; i_2_1_s_81 < 4; ++i_2_1_s_81) {
      if (i_2_1_s_81 < 2) {
        Y_local[((i_2_1_s_81 * 16) + 72)] = (Y_local[((i_2_1_s_81 * 16) + 72)] + (A_shared_dyn_local[(i_2_1_s_81 + 4)] * B_shared_dyn_local[8]));
      }
    }
    for (int i_2_1_s_82 = 0; i_2_1_s_82 < 4; ++i_2_1_s_82) {
      Y_local[((i_2_1_s_82 * 16) + 9)] = (Y_local[((i_2_1_s_82 * 16) + 9)] + (A_shared_dyn_local[i_2_1_s_82] * B_shared_dyn_local[9]));
    }
    for (int i_2_1_s_83 = 0; i_2_1_s_83 < 4; ++i_2_1_s_83) {
      if (i_2_1_s_83 < 2) {
        Y_local[((i_2_1_s_83 * 16) + 73)] = (Y_local[((i_2_1_s_83 * 16) + 73)] + (A_shared_dyn_local[(i_2_1_s_83 + 4)] * B_shared_dyn_local[9]));
      }
    }
    for (int i_2_1_s_84 = 0; i_2_1_s_84 < 4; ++i_2_1_s_84) {
      Y_local[((i_2_1_s_84 * 16) + 10)] = (Y_local[((i_2_1_s_84 * 16) + 10)] + (A_shared_dyn_local[i_2_1_s_84] * B_shared_dyn_local[10]));
    }
    for (int i_2_1_s_85 = 0; i_2_1_s_85 < 4; ++i_2_1_s_85) {
      if (i_2_1_s_85 < 2) {
        Y_local[((i_2_1_s_85 * 16) + 74)] = (Y_local[((i_2_1_s_85 * 16) + 74)] + (A_shared_dyn_local[(i_2_1_s_85 + 4)] * B_shared_dyn_local[10]));
      }
    }
    for (int i_2_1_s_86 = 0; i_2_1_s_86 < 4; ++i_2_1_s_86) {
      Y_local[((i_2_1_s_86 * 16) + 11)] = (Y_local[((i_2_1_s_86 * 16) + 11)] + (A_shared_dyn_local[i_2_1_s_86] * B_shared_dyn_local[11]));
    }
    for (int i_2_1_s_87 = 0; i_2_1_s_87 < 4; ++i_2_1_s_87) {
      if (i_2_1_s_87 < 2) {
        Y_local[((i_2_1_s_87 * 16) + 75)] = (Y_local[((i_2_1_s_87 * 16) + 75)] + (A_shared_dyn_local[(i_2_1_s_87 + 4)] * B_shared_dyn_local[11]));
      }
    }
    for (int i_2_1_s_88 = 0; i_2_1_s_88 < 4; ++i_2_1_s_88) {
      Y_local[((i_2_1_s_88 * 16) + 12)] = (Y_local[((i_2_1_s_88 * 16) + 12)] + (A_shared_dyn_local[i_2_1_s_88] * B_shared_dyn_local[12]));
    }
    for (int i_2_1_s_89 = 0; i_2_1_s_89 < 4; ++i_2_1_s_89) {
      if (i_2_1_s_89 < 2) {
        Y_local[((i_2_1_s_89 * 16) + 76)] = (Y_local[((i_2_1_s_89 * 16) + 76)] + (A_shared_dyn_local[(i_2_1_s_89 + 4)] * B_shared_dyn_local[12]));
      }
    }
    for (int i_2_1_s_90 = 0; i_2_1_s_90 < 4; ++i_2_1_s_90) {
      Y_local[((i_2_1_s_90 * 16) + 13)] = (Y_local[((i_2_1_s_90 * 16) + 13)] + (A_shared_dyn_local[i_2_1_s_90] * B_shared_dyn_local[13]));
    }
    for (int i_2_1_s_91 = 0; i_2_1_s_91 < 4; ++i_2_1_s_91) {
      if (i_2_1_s_91 < 2) {
        Y_local[((i_2_1_s_91 * 16) + 77)] = (Y_local[((i_2_1_s_91 * 16) + 77)] + (A_shared_dyn_local[(i_2_1_s_91 + 4)] * B_shared_dyn_local[13]));
      }
    }
    for (int i_2_1_s_92 = 0; i_2_1_s_92 < 4; ++i_2_1_s_92) {
      Y_local[((i_2_1_s_92 * 16) + 14)] = (Y_local[((i_2_1_s_92 * 16) + 14)] + (A_shared_dyn_local[i_2_1_s_92] * B_shared_dyn_local[14]));
    }
    for (int i_2_1_s_93 = 0; i_2_1_s_93 < 4; ++i_2_1_s_93) {
      if (i_2_1_s_93 < 2) {
        Y_local[((i_2_1_s_93 * 16) + 78)] = (Y_local[((i_2_1_s_93 * 16) + 78)] + (A_shared_dyn_local[(i_2_1_s_93 + 4)] * B_shared_dyn_local[14]));
      }
    }
    for (int i_2_1_s_94 = 0; i_2_1_s_94 < 4; ++i_2_1_s_94) {
      Y_local[((i_2_1_s_94 * 16) + 15)] = (Y_local[((i_2_1_s_94 * 16) + 15)] + (A_shared_dyn_local[i_2_1_s_94] * B_shared_dyn_local[15]));
    }
    for (int i_2_1_s_95 = 0; i_2_1_s_95 < 4; ++i_2_1_s_95) {
      if (i_2_1_s_95 < 2) {
        Y_local[((i_2_1_s_95 * 16) + 79)] = (Y_local[((i_2_1_s_95 * 16) + 79)] + (A_shared_dyn_local[(i_2_1_s_95 + 4)] * B_shared_dyn_local[15]));
      }
    }
    for (int ax0_0_4 = 0; ax0_0_4 < 2; ++ax0_0_4) {
      for (int ax0_1_s_4 = 0; ax0_1_s_4 < 4; ++ax0_1_s_4) {
        if (((ax0_0_4 * 2) + (ax0_1_s_4 >> 1)) < 3) {
          A_shared_dyn_local[((ax0_0_4 * 4) + ax0_1_s_4)] = ((float*)buf_dyn_shmem)[(((((((k_0 + 1) % 5) * 576) + ((((int)threadIdx.x) / 27) * 72)) + ((((int)threadIdx.x) % 3) * 24)) + (ax0_0_4 * 16)) + (ax0_1_s_4 * 4))];
        }
      }
    }
    for (int ax1_0_4 = 0; ax1_0_4 < 4; ++ax1_0_4) {
      *(float4*)(B_shared_dyn_local + (ax1_0_4 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((k_0 + 1) % 5) * 768) + ((((((((int)blockIdx.x) & 7) * 144) + (((((int)threadIdx.x) % 27) / 3) * 16)) + (ax1_0_4 * 4)) >> 6) * 64)) + ((ax1_0_4 & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 18) + (((((int)threadIdx.x) % 27) / 3) * 2)) + (ax1_0_4 >> 1)) & 7) * 4)) + 2880) - ((((((int)blockIdx.x) & 7) * 144) >> 6) * 64)));
    }
    for (int i_2_1_s_96 = 0; i_2_1_s_96 < 4; ++i_2_1_s_96) {
      Y_local[(i_2_1_s_96 * 16)] = (Y_local[(i_2_1_s_96 * 16)] + (A_shared_dyn_local[(i_2_1_s_96 + 6)] * B_shared_dyn_local[16]));
    }
    for (int i_2_1_s_97 = 0; i_2_1_s_97 < 4; ++i_2_1_s_97) {
      if (i_2_1_s_97 < 2) {
        Y_local[((i_2_1_s_97 * 16) + 64)] = (Y_local[((i_2_1_s_97 * 16) + 64)] + (A_shared_dyn_local[(i_2_1_s_97 + 10)] * B_shared_dyn_local[16]));
      }
    }
    for (int i_2_1_s_98 = 0; i_2_1_s_98 < 4; ++i_2_1_s_98) {
      Y_local[((i_2_1_s_98 * 16) + 1)] = (Y_local[((i_2_1_s_98 * 16) + 1)] + (A_shared_dyn_local[(i_2_1_s_98 + 6)] * B_shared_dyn_local[17]));
    }
    for (int i_2_1_s_99 = 0; i_2_1_s_99 < 4; ++i_2_1_s_99) {
      if (i_2_1_s_99 < 2) {
        Y_local[((i_2_1_s_99 * 16) + 65)] = (Y_local[((i_2_1_s_99 * 16) + 65)] + (A_shared_dyn_local[(i_2_1_s_99 + 10)] * B_shared_dyn_local[17]));
      }
    }
    for (int i_2_1_s_100 = 0; i_2_1_s_100 < 4; ++i_2_1_s_100) {
      Y_local[((i_2_1_s_100 * 16) + 2)] = (Y_local[((i_2_1_s_100 * 16) + 2)] + (A_shared_dyn_local[(i_2_1_s_100 + 6)] * B_shared_dyn_local[18]));
    }
    for (int i_2_1_s_101 = 0; i_2_1_s_101 < 4; ++i_2_1_s_101) {
      if (i_2_1_s_101 < 2) {
        Y_local[((i_2_1_s_101 * 16) + 66)] = (Y_local[((i_2_1_s_101 * 16) + 66)] + (A_shared_dyn_local[(i_2_1_s_101 + 10)] * B_shared_dyn_local[18]));
      }
    }
    for (int i_2_1_s_102 = 0; i_2_1_s_102 < 4; ++i_2_1_s_102) {
      Y_local[((i_2_1_s_102 * 16) + 3)] = (Y_local[((i_2_1_s_102 * 16) + 3)] + (A_shared_dyn_local[(i_2_1_s_102 + 6)] * B_shared_dyn_local[19]));
    }
    for (int i_2_1_s_103 = 0; i_2_1_s_103 < 4; ++i_2_1_s_103) {
      if (i_2_1_s_103 < 2) {
        Y_local[((i_2_1_s_103 * 16) + 67)] = (Y_local[((i_2_1_s_103 * 16) + 67)] + (A_shared_dyn_local[(i_2_1_s_103 + 10)] * B_shared_dyn_local[19]));
      }
    }
    for (int i_2_1_s_104 = 0; i_2_1_s_104 < 4; ++i_2_1_s_104) {
      Y_local[((i_2_1_s_104 * 16) + 4)] = (Y_local[((i_2_1_s_104 * 16) + 4)] + (A_shared_dyn_local[(i_2_1_s_104 + 6)] * B_shared_dyn_local[20]));
    }
    for (int i_2_1_s_105 = 0; i_2_1_s_105 < 4; ++i_2_1_s_105) {
      if (i_2_1_s_105 < 2) {
        Y_local[((i_2_1_s_105 * 16) + 68)] = (Y_local[((i_2_1_s_105 * 16) + 68)] + (A_shared_dyn_local[(i_2_1_s_105 + 10)] * B_shared_dyn_local[20]));
      }
    }
    for (int i_2_1_s_106 = 0; i_2_1_s_106 < 4; ++i_2_1_s_106) {
      Y_local[((i_2_1_s_106 * 16) + 5)] = (Y_local[((i_2_1_s_106 * 16) + 5)] + (A_shared_dyn_local[(i_2_1_s_106 + 6)] * B_shared_dyn_local[21]));
    }
    for (int i_2_1_s_107 = 0; i_2_1_s_107 < 4; ++i_2_1_s_107) {
      if (i_2_1_s_107 < 2) {
        Y_local[((i_2_1_s_107 * 16) + 69)] = (Y_local[((i_2_1_s_107 * 16) + 69)] + (A_shared_dyn_local[(i_2_1_s_107 + 10)] * B_shared_dyn_local[21]));
      }
    }
    for (int i_2_1_s_108 = 0; i_2_1_s_108 < 4; ++i_2_1_s_108) {
      Y_local[((i_2_1_s_108 * 16) + 6)] = (Y_local[((i_2_1_s_108 * 16) + 6)] + (A_shared_dyn_local[(i_2_1_s_108 + 6)] * B_shared_dyn_local[22]));
    }
    for (int i_2_1_s_109 = 0; i_2_1_s_109 < 4; ++i_2_1_s_109) {
      if (i_2_1_s_109 < 2) {
        Y_local[((i_2_1_s_109 * 16) + 70)] = (Y_local[((i_2_1_s_109 * 16) + 70)] + (A_shared_dyn_local[(i_2_1_s_109 + 10)] * B_shared_dyn_local[22]));
      }
    }
    for (int i_2_1_s_110 = 0; i_2_1_s_110 < 4; ++i_2_1_s_110) {
      Y_local[((i_2_1_s_110 * 16) + 7)] = (Y_local[((i_2_1_s_110 * 16) + 7)] + (A_shared_dyn_local[(i_2_1_s_110 + 6)] * B_shared_dyn_local[23]));
    }
    for (int i_2_1_s_111 = 0; i_2_1_s_111 < 4; ++i_2_1_s_111) {
      if (i_2_1_s_111 < 2) {
        Y_local[((i_2_1_s_111 * 16) + 71)] = (Y_local[((i_2_1_s_111 * 16) + 71)] + (A_shared_dyn_local[(i_2_1_s_111 + 10)] * B_shared_dyn_local[23]));
      }
    }
    for (int i_2_1_s_112 = 0; i_2_1_s_112 < 4; ++i_2_1_s_112) {
      Y_local[((i_2_1_s_112 * 16) + 8)] = (Y_local[((i_2_1_s_112 * 16) + 8)] + (A_shared_dyn_local[(i_2_1_s_112 + 6)] * B_shared_dyn_local[24]));
    }
    for (int i_2_1_s_113 = 0; i_2_1_s_113 < 4; ++i_2_1_s_113) {
      if (i_2_1_s_113 < 2) {
        Y_local[((i_2_1_s_113 * 16) + 72)] = (Y_local[((i_2_1_s_113 * 16) + 72)] + (A_shared_dyn_local[(i_2_1_s_113 + 10)] * B_shared_dyn_local[24]));
      }
    }
    for (int i_2_1_s_114 = 0; i_2_1_s_114 < 4; ++i_2_1_s_114) {
      Y_local[((i_2_1_s_114 * 16) + 9)] = (Y_local[((i_2_1_s_114 * 16) + 9)] + (A_shared_dyn_local[(i_2_1_s_114 + 6)] * B_shared_dyn_local[25]));
    }
    for (int i_2_1_s_115 = 0; i_2_1_s_115 < 4; ++i_2_1_s_115) {
      if (i_2_1_s_115 < 2) {
        Y_local[((i_2_1_s_115 * 16) + 73)] = (Y_local[((i_2_1_s_115 * 16) + 73)] + (A_shared_dyn_local[(i_2_1_s_115 + 10)] * B_shared_dyn_local[25]));
      }
    }
    for (int i_2_1_s_116 = 0; i_2_1_s_116 < 4; ++i_2_1_s_116) {
      Y_local[((i_2_1_s_116 * 16) + 10)] = (Y_local[((i_2_1_s_116 * 16) + 10)] + (A_shared_dyn_local[(i_2_1_s_116 + 6)] * B_shared_dyn_local[26]));
    }
    for (int i_2_1_s_117 = 0; i_2_1_s_117 < 4; ++i_2_1_s_117) {
      if (i_2_1_s_117 < 2) {
        Y_local[((i_2_1_s_117 * 16) + 74)] = (Y_local[((i_2_1_s_117 * 16) + 74)] + (A_shared_dyn_local[(i_2_1_s_117 + 10)] * B_shared_dyn_local[26]));
      }
    }
    for (int i_2_1_s_118 = 0; i_2_1_s_118 < 4; ++i_2_1_s_118) {
      Y_local[((i_2_1_s_118 * 16) + 11)] = (Y_local[((i_2_1_s_118 * 16) + 11)] + (A_shared_dyn_local[(i_2_1_s_118 + 6)] * B_shared_dyn_local[27]));
    }
    for (int i_2_1_s_119 = 0; i_2_1_s_119 < 4; ++i_2_1_s_119) {
      if (i_2_1_s_119 < 2) {
        Y_local[((i_2_1_s_119 * 16) + 75)] = (Y_local[((i_2_1_s_119 * 16) + 75)] + (A_shared_dyn_local[(i_2_1_s_119 + 10)] * B_shared_dyn_local[27]));
      }
    }
    for (int i_2_1_s_120 = 0; i_2_1_s_120 < 4; ++i_2_1_s_120) {
      Y_local[((i_2_1_s_120 * 16) + 12)] = (Y_local[((i_2_1_s_120 * 16) + 12)] + (A_shared_dyn_local[(i_2_1_s_120 + 6)] * B_shared_dyn_local[28]));
    }
    for (int i_2_1_s_121 = 0; i_2_1_s_121 < 4; ++i_2_1_s_121) {
      if (i_2_1_s_121 < 2) {
        Y_local[((i_2_1_s_121 * 16) + 76)] = (Y_local[((i_2_1_s_121 * 16) + 76)] + (A_shared_dyn_local[(i_2_1_s_121 + 10)] * B_shared_dyn_local[28]));
      }
    }
    for (int i_2_1_s_122 = 0; i_2_1_s_122 < 4; ++i_2_1_s_122) {
      Y_local[((i_2_1_s_122 * 16) + 13)] = (Y_local[((i_2_1_s_122 * 16) + 13)] + (A_shared_dyn_local[(i_2_1_s_122 + 6)] * B_shared_dyn_local[29]));
    }
    for (int i_2_1_s_123 = 0; i_2_1_s_123 < 4; ++i_2_1_s_123) {
      if (i_2_1_s_123 < 2) {
        Y_local[((i_2_1_s_123 * 16) + 77)] = (Y_local[((i_2_1_s_123 * 16) + 77)] + (A_shared_dyn_local[(i_2_1_s_123 + 10)] * B_shared_dyn_local[29]));
      }
    }
    for (int i_2_1_s_124 = 0; i_2_1_s_124 < 4; ++i_2_1_s_124) {
      Y_local[((i_2_1_s_124 * 16) + 14)] = (Y_local[((i_2_1_s_124 * 16) + 14)] + (A_shared_dyn_local[(i_2_1_s_124 + 6)] * B_shared_dyn_local[30]));
    }
    for (int i_2_1_s_125 = 0; i_2_1_s_125 < 4; ++i_2_1_s_125) {
      if (i_2_1_s_125 < 2) {
        Y_local[((i_2_1_s_125 * 16) + 78)] = (Y_local[((i_2_1_s_125 * 16) + 78)] + (A_shared_dyn_local[(i_2_1_s_125 + 10)] * B_shared_dyn_local[30]));
      }
    }
    for (int i_2_1_s_126 = 0; i_2_1_s_126 < 4; ++i_2_1_s_126) {
      Y_local[((i_2_1_s_126 * 16) + 15)] = (Y_local[((i_2_1_s_126 * 16) + 15)] + (A_shared_dyn_local[(i_2_1_s_126 + 6)] * B_shared_dyn_local[31]));
    }
    for (int i_2_1_s_127 = 0; i_2_1_s_127 < 4; ++i_2_1_s_127) {
      if (i_2_1_s_127 < 2) {
        Y_local[((i_2_1_s_127 * 16) + 79)] = (Y_local[((i_2_1_s_127 * 16) + 79)] + (A_shared_dyn_local[(i_2_1_s_127 + 10)] * B_shared_dyn_local[31]));
      }
    }
  }
__asm__ __volatile__("cp.async.wait_group 2;");

  __syncthreads();
  for (int ax0_0_5 = 0; ax0_0_5 < 2; ++ax0_0_5) {
    for (int ax0_1_s_5 = 0; ax0_1_s_5 < 4; ++ax0_1_s_5) {
      if (((ax0_0_5 * 2) + (ax0_1_s_5 >> 1)) < 3) {
        A_shared_dyn_local[(((ax0_0_5 * 4) + ax0_1_s_5) + 6)] = ((float*)buf_dyn_shmem)[((((((((int)threadIdx.x) / 27) * 72) + ((((int)threadIdx.x) % 3) * 24)) + (ax0_0_5 * 16)) + (ax0_1_s_5 * 4)) + 2305)];
      }
    }
  }
  for (int ax1_0_5 = 0; ax1_0_5 < 4; ++ax1_0_5) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_5 * 4) + 16)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((int)blockIdx.x) & 7) * 144) + (((((int)threadIdx.x) % 27) / 3) * 16)) + (ax1_0_5 * 4)) >> 6) * 64) + ((ax1_0_5 & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 18) + (((((int)threadIdx.x) % 27) / 3) * 2)) + (ax1_0_5 >> 1)) & 7) * 4)) + 6144) - ((((((int)blockIdx.x) & 7) * 144) >> 6) * 64)));
  }
  for (int i_2_1_s_128 = 0; i_2_1_s_128 < 4; ++i_2_1_s_128) {
    Y_local[(i_2_1_s_128 * 16)] = (Y_local[(i_2_1_s_128 * 16)] + (A_shared_dyn_local[i_2_1_s_128] * B_shared_dyn_local[0]));
  }
  for (int i_2_1_s_129 = 0; i_2_1_s_129 < 4; ++i_2_1_s_129) {
    if (i_2_1_s_129 < 2) {
      Y_local[((i_2_1_s_129 * 16) + 64)] = (Y_local[((i_2_1_s_129 * 16) + 64)] + (A_shared_dyn_local[(i_2_1_s_129 + 4)] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_130 = 0; i_2_1_s_130 < 4; ++i_2_1_s_130) {
    Y_local[((i_2_1_s_130 * 16) + 1)] = (Y_local[((i_2_1_s_130 * 16) + 1)] + (A_shared_dyn_local[i_2_1_s_130] * B_shared_dyn_local[1]));
  }
  for (int i_2_1_s_131 = 0; i_2_1_s_131 < 4; ++i_2_1_s_131) {
    if (i_2_1_s_131 < 2) {
      Y_local[((i_2_1_s_131 * 16) + 65)] = (Y_local[((i_2_1_s_131 * 16) + 65)] + (A_shared_dyn_local[(i_2_1_s_131 + 4)] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_132 = 0; i_2_1_s_132 < 4; ++i_2_1_s_132) {
    Y_local[((i_2_1_s_132 * 16) + 2)] = (Y_local[((i_2_1_s_132 * 16) + 2)] + (A_shared_dyn_local[i_2_1_s_132] * B_shared_dyn_local[2]));
  }
  for (int i_2_1_s_133 = 0; i_2_1_s_133 < 4; ++i_2_1_s_133) {
    if (i_2_1_s_133 < 2) {
      Y_local[((i_2_1_s_133 * 16) + 66)] = (Y_local[((i_2_1_s_133 * 16) + 66)] + (A_shared_dyn_local[(i_2_1_s_133 + 4)] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_134 = 0; i_2_1_s_134 < 4; ++i_2_1_s_134) {
    Y_local[((i_2_1_s_134 * 16) + 3)] = (Y_local[((i_2_1_s_134 * 16) + 3)] + (A_shared_dyn_local[i_2_1_s_134] * B_shared_dyn_local[3]));
  }
  for (int i_2_1_s_135 = 0; i_2_1_s_135 < 4; ++i_2_1_s_135) {
    if (i_2_1_s_135 < 2) {
      Y_local[((i_2_1_s_135 * 16) + 67)] = (Y_local[((i_2_1_s_135 * 16) + 67)] + (A_shared_dyn_local[(i_2_1_s_135 + 4)] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_136 = 0; i_2_1_s_136 < 4; ++i_2_1_s_136) {
    Y_local[((i_2_1_s_136 * 16) + 4)] = (Y_local[((i_2_1_s_136 * 16) + 4)] + (A_shared_dyn_local[i_2_1_s_136] * B_shared_dyn_local[4]));
  }
  for (int i_2_1_s_137 = 0; i_2_1_s_137 < 4; ++i_2_1_s_137) {
    if (i_2_1_s_137 < 2) {
      Y_local[((i_2_1_s_137 * 16) + 68)] = (Y_local[((i_2_1_s_137 * 16) + 68)] + (A_shared_dyn_local[(i_2_1_s_137 + 4)] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_138 = 0; i_2_1_s_138 < 4; ++i_2_1_s_138) {
    Y_local[((i_2_1_s_138 * 16) + 5)] = (Y_local[((i_2_1_s_138 * 16) + 5)] + (A_shared_dyn_local[i_2_1_s_138] * B_shared_dyn_local[5]));
  }
  for (int i_2_1_s_139 = 0; i_2_1_s_139 < 4; ++i_2_1_s_139) {
    if (i_2_1_s_139 < 2) {
      Y_local[((i_2_1_s_139 * 16) + 69)] = (Y_local[((i_2_1_s_139 * 16) + 69)] + (A_shared_dyn_local[(i_2_1_s_139 + 4)] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_140 = 0; i_2_1_s_140 < 4; ++i_2_1_s_140) {
    Y_local[((i_2_1_s_140 * 16) + 6)] = (Y_local[((i_2_1_s_140 * 16) + 6)] + (A_shared_dyn_local[i_2_1_s_140] * B_shared_dyn_local[6]));
  }
  for (int i_2_1_s_141 = 0; i_2_1_s_141 < 4; ++i_2_1_s_141) {
    if (i_2_1_s_141 < 2) {
      Y_local[((i_2_1_s_141 * 16) + 70)] = (Y_local[((i_2_1_s_141 * 16) + 70)] + (A_shared_dyn_local[(i_2_1_s_141 + 4)] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_142 = 0; i_2_1_s_142 < 4; ++i_2_1_s_142) {
    Y_local[((i_2_1_s_142 * 16) + 7)] = (Y_local[((i_2_1_s_142 * 16) + 7)] + (A_shared_dyn_local[i_2_1_s_142] * B_shared_dyn_local[7]));
  }
  for (int i_2_1_s_143 = 0; i_2_1_s_143 < 4; ++i_2_1_s_143) {
    if (i_2_1_s_143 < 2) {
      Y_local[((i_2_1_s_143 * 16) + 71)] = (Y_local[((i_2_1_s_143 * 16) + 71)] + (A_shared_dyn_local[(i_2_1_s_143 + 4)] * B_shared_dyn_local[7]));
    }
  }
  for (int i_2_1_s_144 = 0; i_2_1_s_144 < 4; ++i_2_1_s_144) {
    Y_local[((i_2_1_s_144 * 16) + 8)] = (Y_local[((i_2_1_s_144 * 16) + 8)] + (A_shared_dyn_local[i_2_1_s_144] * B_shared_dyn_local[8]));
  }
  for (int i_2_1_s_145 = 0; i_2_1_s_145 < 4; ++i_2_1_s_145) {
    if (i_2_1_s_145 < 2) {
      Y_local[((i_2_1_s_145 * 16) + 72)] = (Y_local[((i_2_1_s_145 * 16) + 72)] + (A_shared_dyn_local[(i_2_1_s_145 + 4)] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_146 = 0; i_2_1_s_146 < 4; ++i_2_1_s_146) {
    Y_local[((i_2_1_s_146 * 16) + 9)] = (Y_local[((i_2_1_s_146 * 16) + 9)] + (A_shared_dyn_local[i_2_1_s_146] * B_shared_dyn_local[9]));
  }
  for (int i_2_1_s_147 = 0; i_2_1_s_147 < 4; ++i_2_1_s_147) {
    if (i_2_1_s_147 < 2) {
      Y_local[((i_2_1_s_147 * 16) + 73)] = (Y_local[((i_2_1_s_147 * 16) + 73)] + (A_shared_dyn_local[(i_2_1_s_147 + 4)] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_148 = 0; i_2_1_s_148 < 4; ++i_2_1_s_148) {
    Y_local[((i_2_1_s_148 * 16) + 10)] = (Y_local[((i_2_1_s_148 * 16) + 10)] + (A_shared_dyn_local[i_2_1_s_148] * B_shared_dyn_local[10]));
  }
  for (int i_2_1_s_149 = 0; i_2_1_s_149 < 4; ++i_2_1_s_149) {
    if (i_2_1_s_149 < 2) {
      Y_local[((i_2_1_s_149 * 16) + 74)] = (Y_local[((i_2_1_s_149 * 16) + 74)] + (A_shared_dyn_local[(i_2_1_s_149 + 4)] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_150 = 0; i_2_1_s_150 < 4; ++i_2_1_s_150) {
    Y_local[((i_2_1_s_150 * 16) + 11)] = (Y_local[((i_2_1_s_150 * 16) + 11)] + (A_shared_dyn_local[i_2_1_s_150] * B_shared_dyn_local[11]));
  }
  for (int i_2_1_s_151 = 0; i_2_1_s_151 < 4; ++i_2_1_s_151) {
    if (i_2_1_s_151 < 2) {
      Y_local[((i_2_1_s_151 * 16) + 75)] = (Y_local[((i_2_1_s_151 * 16) + 75)] + (A_shared_dyn_local[(i_2_1_s_151 + 4)] * B_shared_dyn_local[11]));
    }
  }
  for (int i_2_1_s_152 = 0; i_2_1_s_152 < 4; ++i_2_1_s_152) {
    Y_local[((i_2_1_s_152 * 16) + 12)] = (Y_local[((i_2_1_s_152 * 16) + 12)] + (A_shared_dyn_local[i_2_1_s_152] * B_shared_dyn_local[12]));
  }
  for (int i_2_1_s_153 = 0; i_2_1_s_153 < 4; ++i_2_1_s_153) {
    if (i_2_1_s_153 < 2) {
      Y_local[((i_2_1_s_153 * 16) + 76)] = (Y_local[((i_2_1_s_153 * 16) + 76)] + (A_shared_dyn_local[(i_2_1_s_153 + 4)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_154 = 0; i_2_1_s_154 < 4; ++i_2_1_s_154) {
    Y_local[((i_2_1_s_154 * 16) + 13)] = (Y_local[((i_2_1_s_154 * 16) + 13)] + (A_shared_dyn_local[i_2_1_s_154] * B_shared_dyn_local[13]));
  }
  for (int i_2_1_s_155 = 0; i_2_1_s_155 < 4; ++i_2_1_s_155) {
    if (i_2_1_s_155 < 2) {
      Y_local[((i_2_1_s_155 * 16) + 77)] = (Y_local[((i_2_1_s_155 * 16) + 77)] + (A_shared_dyn_local[(i_2_1_s_155 + 4)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_156 = 0; i_2_1_s_156 < 4; ++i_2_1_s_156) {
    Y_local[((i_2_1_s_156 * 16) + 14)] = (Y_local[((i_2_1_s_156 * 16) + 14)] + (A_shared_dyn_local[i_2_1_s_156] * B_shared_dyn_local[14]));
  }
  for (int i_2_1_s_157 = 0; i_2_1_s_157 < 4; ++i_2_1_s_157) {
    if (i_2_1_s_157 < 2) {
      Y_local[((i_2_1_s_157 * 16) + 78)] = (Y_local[((i_2_1_s_157 * 16) + 78)] + (A_shared_dyn_local[(i_2_1_s_157 + 4)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_158 = 0; i_2_1_s_158 < 4; ++i_2_1_s_158) {
    Y_local[((i_2_1_s_158 * 16) + 15)] = (Y_local[((i_2_1_s_158 * 16) + 15)] + (A_shared_dyn_local[i_2_1_s_158] * B_shared_dyn_local[15]));
  }
  for (int i_2_1_s_159 = 0; i_2_1_s_159 < 4; ++i_2_1_s_159) {
    if (i_2_1_s_159 < 2) {
      Y_local[((i_2_1_s_159 * 16) + 79)] = (Y_local[((i_2_1_s_159 * 16) + 79)] + (A_shared_dyn_local[(i_2_1_s_159 + 4)] * B_shared_dyn_local[15]));
    }
  }
  for (int ax0_0_6 = 0; ax0_0_6 < 2; ++ax0_0_6) {
    for (int ax0_1_s_6 = 0; ax0_1_s_6 < 4; ++ax0_1_s_6) {
      if (((ax0_0_6 * 2) + (ax0_1_s_6 >> 1)) < 3) {
        A_shared_dyn_local[((ax0_0_6 * 4) + ax0_1_s_6)] = ((float*)buf_dyn_shmem)[((((((((int)threadIdx.x) / 27) * 72) + ((((int)threadIdx.x) % 3) * 24)) + (ax0_0_6 * 16)) + (ax0_1_s_6 * 4)) + 2306)];
      }
    }
  }
  for (int ax1_0_6 = 0; ax1_0_6 < 4; ++ax1_0_6) {
    *(float4*)(B_shared_dyn_local + (ax1_0_6 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((int)blockIdx.x) & 7) * 144) + (((((int)threadIdx.x) % 27) / 3) * 16)) + (ax1_0_6 * 4)) >> 6) * 64) + ((ax1_0_6 & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 18) + (((((int)threadIdx.x) % 27) / 3) * 2)) + (ax1_0_6 >> 1)) & 7) * 4)) + 6336) - ((((((int)blockIdx.x) & 7) * 144) >> 6) * 64)));
  }
  for (int i_2_1_s_160 = 0; i_2_1_s_160 < 4; ++i_2_1_s_160) {
    Y_local[(i_2_1_s_160 * 16)] = (Y_local[(i_2_1_s_160 * 16)] + (A_shared_dyn_local[(i_2_1_s_160 + 6)] * B_shared_dyn_local[16]));
  }
  for (int i_2_1_s_161 = 0; i_2_1_s_161 < 4; ++i_2_1_s_161) {
    if (i_2_1_s_161 < 2) {
      Y_local[((i_2_1_s_161 * 16) + 64)] = (Y_local[((i_2_1_s_161 * 16) + 64)] + (A_shared_dyn_local[(i_2_1_s_161 + 10)] * B_shared_dyn_local[16]));
    }
  }
  for (int i_2_1_s_162 = 0; i_2_1_s_162 < 4; ++i_2_1_s_162) {
    Y_local[((i_2_1_s_162 * 16) + 1)] = (Y_local[((i_2_1_s_162 * 16) + 1)] + (A_shared_dyn_local[(i_2_1_s_162 + 6)] * B_shared_dyn_local[17]));
  }
  for (int i_2_1_s_163 = 0; i_2_1_s_163 < 4; ++i_2_1_s_163) {
    if (i_2_1_s_163 < 2) {
      Y_local[((i_2_1_s_163 * 16) + 65)] = (Y_local[((i_2_1_s_163 * 16) + 65)] + (A_shared_dyn_local[(i_2_1_s_163 + 10)] * B_shared_dyn_local[17]));
    }
  }
  for (int i_2_1_s_164 = 0; i_2_1_s_164 < 4; ++i_2_1_s_164) {
    Y_local[((i_2_1_s_164 * 16) + 2)] = (Y_local[((i_2_1_s_164 * 16) + 2)] + (A_shared_dyn_local[(i_2_1_s_164 + 6)] * B_shared_dyn_local[18]));
  }
  for (int i_2_1_s_165 = 0; i_2_1_s_165 < 4; ++i_2_1_s_165) {
    if (i_2_1_s_165 < 2) {
      Y_local[((i_2_1_s_165 * 16) + 66)] = (Y_local[((i_2_1_s_165 * 16) + 66)] + (A_shared_dyn_local[(i_2_1_s_165 + 10)] * B_shared_dyn_local[18]));
    }
  }
  for (int i_2_1_s_166 = 0; i_2_1_s_166 < 4; ++i_2_1_s_166) {
    Y_local[((i_2_1_s_166 * 16) + 3)] = (Y_local[((i_2_1_s_166 * 16) + 3)] + (A_shared_dyn_local[(i_2_1_s_166 + 6)] * B_shared_dyn_local[19]));
  }
  for (int i_2_1_s_167 = 0; i_2_1_s_167 < 4; ++i_2_1_s_167) {
    if (i_2_1_s_167 < 2) {
      Y_local[((i_2_1_s_167 * 16) + 67)] = (Y_local[((i_2_1_s_167 * 16) + 67)] + (A_shared_dyn_local[(i_2_1_s_167 + 10)] * B_shared_dyn_local[19]));
    }
  }
  for (int i_2_1_s_168 = 0; i_2_1_s_168 < 4; ++i_2_1_s_168) {
    Y_local[((i_2_1_s_168 * 16) + 4)] = (Y_local[((i_2_1_s_168 * 16) + 4)] + (A_shared_dyn_local[(i_2_1_s_168 + 6)] * B_shared_dyn_local[20]));
  }
  for (int i_2_1_s_169 = 0; i_2_1_s_169 < 4; ++i_2_1_s_169) {
    if (i_2_1_s_169 < 2) {
      Y_local[((i_2_1_s_169 * 16) + 68)] = (Y_local[((i_2_1_s_169 * 16) + 68)] + (A_shared_dyn_local[(i_2_1_s_169 + 10)] * B_shared_dyn_local[20]));
    }
  }
  for (int i_2_1_s_170 = 0; i_2_1_s_170 < 4; ++i_2_1_s_170) {
    Y_local[((i_2_1_s_170 * 16) + 5)] = (Y_local[((i_2_1_s_170 * 16) + 5)] + (A_shared_dyn_local[(i_2_1_s_170 + 6)] * B_shared_dyn_local[21]));
  }
  for (int i_2_1_s_171 = 0; i_2_1_s_171 < 4; ++i_2_1_s_171) {
    if (i_2_1_s_171 < 2) {
      Y_local[((i_2_1_s_171 * 16) + 69)] = (Y_local[((i_2_1_s_171 * 16) + 69)] + (A_shared_dyn_local[(i_2_1_s_171 + 10)] * B_shared_dyn_local[21]));
    }
  }
  for (int i_2_1_s_172 = 0; i_2_1_s_172 < 4; ++i_2_1_s_172) {
    Y_local[((i_2_1_s_172 * 16) + 6)] = (Y_local[((i_2_1_s_172 * 16) + 6)] + (A_shared_dyn_local[(i_2_1_s_172 + 6)] * B_shared_dyn_local[22]));
  }
  for (int i_2_1_s_173 = 0; i_2_1_s_173 < 4; ++i_2_1_s_173) {
    if (i_2_1_s_173 < 2) {
      Y_local[((i_2_1_s_173 * 16) + 70)] = (Y_local[((i_2_1_s_173 * 16) + 70)] + (A_shared_dyn_local[(i_2_1_s_173 + 10)] * B_shared_dyn_local[22]));
    }
  }
  for (int i_2_1_s_174 = 0; i_2_1_s_174 < 4; ++i_2_1_s_174) {
    Y_local[((i_2_1_s_174 * 16) + 7)] = (Y_local[((i_2_1_s_174 * 16) + 7)] + (A_shared_dyn_local[(i_2_1_s_174 + 6)] * B_shared_dyn_local[23]));
  }
  for (int i_2_1_s_175 = 0; i_2_1_s_175 < 4; ++i_2_1_s_175) {
    if (i_2_1_s_175 < 2) {
      Y_local[((i_2_1_s_175 * 16) + 71)] = (Y_local[((i_2_1_s_175 * 16) + 71)] + (A_shared_dyn_local[(i_2_1_s_175 + 10)] * B_shared_dyn_local[23]));
    }
  }
  for (int i_2_1_s_176 = 0; i_2_1_s_176 < 4; ++i_2_1_s_176) {
    Y_local[((i_2_1_s_176 * 16) + 8)] = (Y_local[((i_2_1_s_176 * 16) + 8)] + (A_shared_dyn_local[(i_2_1_s_176 + 6)] * B_shared_dyn_local[24]));
  }
  for (int i_2_1_s_177 = 0; i_2_1_s_177 < 4; ++i_2_1_s_177) {
    if (i_2_1_s_177 < 2) {
      Y_local[((i_2_1_s_177 * 16) + 72)] = (Y_local[((i_2_1_s_177 * 16) + 72)] + (A_shared_dyn_local[(i_2_1_s_177 + 10)] * B_shared_dyn_local[24]));
    }
  }
  for (int i_2_1_s_178 = 0; i_2_1_s_178 < 4; ++i_2_1_s_178) {
    Y_local[((i_2_1_s_178 * 16) + 9)] = (Y_local[((i_2_1_s_178 * 16) + 9)] + (A_shared_dyn_local[(i_2_1_s_178 + 6)] * B_shared_dyn_local[25]));
  }
  for (int i_2_1_s_179 = 0; i_2_1_s_179 < 4; ++i_2_1_s_179) {
    if (i_2_1_s_179 < 2) {
      Y_local[((i_2_1_s_179 * 16) + 73)] = (Y_local[((i_2_1_s_179 * 16) + 73)] + (A_shared_dyn_local[(i_2_1_s_179 + 10)] * B_shared_dyn_local[25]));
    }
  }
  for (int i_2_1_s_180 = 0; i_2_1_s_180 < 4; ++i_2_1_s_180) {
    Y_local[((i_2_1_s_180 * 16) + 10)] = (Y_local[((i_2_1_s_180 * 16) + 10)] + (A_shared_dyn_local[(i_2_1_s_180 + 6)] * B_shared_dyn_local[26]));
  }
  for (int i_2_1_s_181 = 0; i_2_1_s_181 < 4; ++i_2_1_s_181) {
    if (i_2_1_s_181 < 2) {
      Y_local[((i_2_1_s_181 * 16) + 74)] = (Y_local[((i_2_1_s_181 * 16) + 74)] + (A_shared_dyn_local[(i_2_1_s_181 + 10)] * B_shared_dyn_local[26]));
    }
  }
  for (int i_2_1_s_182 = 0; i_2_1_s_182 < 4; ++i_2_1_s_182) {
    Y_local[((i_2_1_s_182 * 16) + 11)] = (Y_local[((i_2_1_s_182 * 16) + 11)] + (A_shared_dyn_local[(i_2_1_s_182 + 6)] * B_shared_dyn_local[27]));
  }
  for (int i_2_1_s_183 = 0; i_2_1_s_183 < 4; ++i_2_1_s_183) {
    if (i_2_1_s_183 < 2) {
      Y_local[((i_2_1_s_183 * 16) + 75)] = (Y_local[((i_2_1_s_183 * 16) + 75)] + (A_shared_dyn_local[(i_2_1_s_183 + 10)] * B_shared_dyn_local[27]));
    }
  }
  for (int i_2_1_s_184 = 0; i_2_1_s_184 < 4; ++i_2_1_s_184) {
    Y_local[((i_2_1_s_184 * 16) + 12)] = (Y_local[((i_2_1_s_184 * 16) + 12)] + (A_shared_dyn_local[(i_2_1_s_184 + 6)] * B_shared_dyn_local[28]));
  }
  for (int i_2_1_s_185 = 0; i_2_1_s_185 < 4; ++i_2_1_s_185) {
    if (i_2_1_s_185 < 2) {
      Y_local[((i_2_1_s_185 * 16) + 76)] = (Y_local[((i_2_1_s_185 * 16) + 76)] + (A_shared_dyn_local[(i_2_1_s_185 + 10)] * B_shared_dyn_local[28]));
    }
  }
  for (int i_2_1_s_186 = 0; i_2_1_s_186 < 4; ++i_2_1_s_186) {
    Y_local[((i_2_1_s_186 * 16) + 13)] = (Y_local[((i_2_1_s_186 * 16) + 13)] + (A_shared_dyn_local[(i_2_1_s_186 + 6)] * B_shared_dyn_local[29]));
  }
  for (int i_2_1_s_187 = 0; i_2_1_s_187 < 4; ++i_2_1_s_187) {
    if (i_2_1_s_187 < 2) {
      Y_local[((i_2_1_s_187 * 16) + 77)] = (Y_local[((i_2_1_s_187 * 16) + 77)] + (A_shared_dyn_local[(i_2_1_s_187 + 10)] * B_shared_dyn_local[29]));
    }
  }
  for (int i_2_1_s_188 = 0; i_2_1_s_188 < 4; ++i_2_1_s_188) {
    Y_local[((i_2_1_s_188 * 16) + 14)] = (Y_local[((i_2_1_s_188 * 16) + 14)] + (A_shared_dyn_local[(i_2_1_s_188 + 6)] * B_shared_dyn_local[30]));
  }
  for (int i_2_1_s_189 = 0; i_2_1_s_189 < 4; ++i_2_1_s_189) {
    if (i_2_1_s_189 < 2) {
      Y_local[((i_2_1_s_189 * 16) + 78)] = (Y_local[((i_2_1_s_189 * 16) + 78)] + (A_shared_dyn_local[(i_2_1_s_189 + 10)] * B_shared_dyn_local[30]));
    }
  }
  for (int i_2_1_s_190 = 0; i_2_1_s_190 < 4; ++i_2_1_s_190) {
    Y_local[((i_2_1_s_190 * 16) + 15)] = (Y_local[((i_2_1_s_190 * 16) + 15)] + (A_shared_dyn_local[(i_2_1_s_190 + 6)] * B_shared_dyn_local[31]));
  }
  for (int i_2_1_s_191 = 0; i_2_1_s_191 < 4; ++i_2_1_s_191) {
    if (i_2_1_s_191 < 2) {
      Y_local[((i_2_1_s_191 * 16) + 79)] = (Y_local[((i_2_1_s_191 * 16) + 79)] + (A_shared_dyn_local[(i_2_1_s_191 + 10)] * B_shared_dyn_local[31]));
    }
  }
  for (int ax0_0_7 = 0; ax0_0_7 < 2; ++ax0_0_7) {
    for (int ax0_1_s_7 = 0; ax0_1_s_7 < 4; ++ax0_1_s_7) {
      if (((ax0_0_7 * 2) + (ax0_1_s_7 >> 1)) < 3) {
        A_shared_dyn_local[(((ax0_0_7 * 4) + ax0_1_s_7) + 6)] = ((float*)buf_dyn_shmem)[((((((((int)threadIdx.x) / 27) * 72) + ((((int)threadIdx.x) % 3) * 24)) + (ax0_0_7 * 16)) + (ax0_1_s_7 * 4)) + 2307)];
      }
    }
  }
  for (int ax1_0_7 = 0; ax1_0_7 < 4; ++ax1_0_7) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_7 * 4) + 16)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((int)blockIdx.x) & 7) * 144) + (((((int)threadIdx.x) % 27) / 3) * 16)) + (ax1_0_7 * 4)) >> 6) * 64) + ((ax1_0_7 & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 18) + (((((int)threadIdx.x) % 27) / 3) * 2)) + (ax1_0_7 >> 1)) & 7) * 4)) + 6528) - ((((((int)blockIdx.x) & 7) * 144) >> 6) * 64)));
  }
  for (int i_2_1_s_192 = 0; i_2_1_s_192 < 4; ++i_2_1_s_192) {
    Y_local[(i_2_1_s_192 * 16)] = (Y_local[(i_2_1_s_192 * 16)] + (A_shared_dyn_local[i_2_1_s_192] * B_shared_dyn_local[0]));
  }
  for (int i_2_1_s_193 = 0; i_2_1_s_193 < 4; ++i_2_1_s_193) {
    if (i_2_1_s_193 < 2) {
      Y_local[((i_2_1_s_193 * 16) + 64)] = (Y_local[((i_2_1_s_193 * 16) + 64)] + (A_shared_dyn_local[(i_2_1_s_193 + 4)] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_194 = 0; i_2_1_s_194 < 4; ++i_2_1_s_194) {
    Y_local[((i_2_1_s_194 * 16) + 1)] = (Y_local[((i_2_1_s_194 * 16) + 1)] + (A_shared_dyn_local[i_2_1_s_194] * B_shared_dyn_local[1]));
  }
  for (int i_2_1_s_195 = 0; i_2_1_s_195 < 4; ++i_2_1_s_195) {
    if (i_2_1_s_195 < 2) {
      Y_local[((i_2_1_s_195 * 16) + 65)] = (Y_local[((i_2_1_s_195 * 16) + 65)] + (A_shared_dyn_local[(i_2_1_s_195 + 4)] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_196 = 0; i_2_1_s_196 < 4; ++i_2_1_s_196) {
    Y_local[((i_2_1_s_196 * 16) + 2)] = (Y_local[((i_2_1_s_196 * 16) + 2)] + (A_shared_dyn_local[i_2_1_s_196] * B_shared_dyn_local[2]));
  }
  for (int i_2_1_s_197 = 0; i_2_1_s_197 < 4; ++i_2_1_s_197) {
    if (i_2_1_s_197 < 2) {
      Y_local[((i_2_1_s_197 * 16) + 66)] = (Y_local[((i_2_1_s_197 * 16) + 66)] + (A_shared_dyn_local[(i_2_1_s_197 + 4)] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_198 = 0; i_2_1_s_198 < 4; ++i_2_1_s_198) {
    Y_local[((i_2_1_s_198 * 16) + 3)] = (Y_local[((i_2_1_s_198 * 16) + 3)] + (A_shared_dyn_local[i_2_1_s_198] * B_shared_dyn_local[3]));
  }
  for (int i_2_1_s_199 = 0; i_2_1_s_199 < 4; ++i_2_1_s_199) {
    if (i_2_1_s_199 < 2) {
      Y_local[((i_2_1_s_199 * 16) + 67)] = (Y_local[((i_2_1_s_199 * 16) + 67)] + (A_shared_dyn_local[(i_2_1_s_199 + 4)] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_200 = 0; i_2_1_s_200 < 4; ++i_2_1_s_200) {
    Y_local[((i_2_1_s_200 * 16) + 4)] = (Y_local[((i_2_1_s_200 * 16) + 4)] + (A_shared_dyn_local[i_2_1_s_200] * B_shared_dyn_local[4]));
  }
  for (int i_2_1_s_201 = 0; i_2_1_s_201 < 4; ++i_2_1_s_201) {
    if (i_2_1_s_201 < 2) {
      Y_local[((i_2_1_s_201 * 16) + 68)] = (Y_local[((i_2_1_s_201 * 16) + 68)] + (A_shared_dyn_local[(i_2_1_s_201 + 4)] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_202 = 0; i_2_1_s_202 < 4; ++i_2_1_s_202) {
    Y_local[((i_2_1_s_202 * 16) + 5)] = (Y_local[((i_2_1_s_202 * 16) + 5)] + (A_shared_dyn_local[i_2_1_s_202] * B_shared_dyn_local[5]));
  }
  for (int i_2_1_s_203 = 0; i_2_1_s_203 < 4; ++i_2_1_s_203) {
    if (i_2_1_s_203 < 2) {
      Y_local[((i_2_1_s_203 * 16) + 69)] = (Y_local[((i_2_1_s_203 * 16) + 69)] + (A_shared_dyn_local[(i_2_1_s_203 + 4)] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_204 = 0; i_2_1_s_204 < 4; ++i_2_1_s_204) {
    Y_local[((i_2_1_s_204 * 16) + 6)] = (Y_local[((i_2_1_s_204 * 16) + 6)] + (A_shared_dyn_local[i_2_1_s_204] * B_shared_dyn_local[6]));
  }
  for (int i_2_1_s_205 = 0; i_2_1_s_205 < 4; ++i_2_1_s_205) {
    if (i_2_1_s_205 < 2) {
      Y_local[((i_2_1_s_205 * 16) + 70)] = (Y_local[((i_2_1_s_205 * 16) + 70)] + (A_shared_dyn_local[(i_2_1_s_205 + 4)] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_206 = 0; i_2_1_s_206 < 4; ++i_2_1_s_206) {
    Y_local[((i_2_1_s_206 * 16) + 7)] = (Y_local[((i_2_1_s_206 * 16) + 7)] + (A_shared_dyn_local[i_2_1_s_206] * B_shared_dyn_local[7]));
  }
  for (int i_2_1_s_207 = 0; i_2_1_s_207 < 4; ++i_2_1_s_207) {
    if (i_2_1_s_207 < 2) {
      Y_local[((i_2_1_s_207 * 16) + 71)] = (Y_local[((i_2_1_s_207 * 16) + 71)] + (A_shared_dyn_local[(i_2_1_s_207 + 4)] * B_shared_dyn_local[7]));
    }
  }
  for (int i_2_1_s_208 = 0; i_2_1_s_208 < 4; ++i_2_1_s_208) {
    Y_local[((i_2_1_s_208 * 16) + 8)] = (Y_local[((i_2_1_s_208 * 16) + 8)] + (A_shared_dyn_local[i_2_1_s_208] * B_shared_dyn_local[8]));
  }
  for (int i_2_1_s_209 = 0; i_2_1_s_209 < 4; ++i_2_1_s_209) {
    if (i_2_1_s_209 < 2) {
      Y_local[((i_2_1_s_209 * 16) + 72)] = (Y_local[((i_2_1_s_209 * 16) + 72)] + (A_shared_dyn_local[(i_2_1_s_209 + 4)] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_210 = 0; i_2_1_s_210 < 4; ++i_2_1_s_210) {
    Y_local[((i_2_1_s_210 * 16) + 9)] = (Y_local[((i_2_1_s_210 * 16) + 9)] + (A_shared_dyn_local[i_2_1_s_210] * B_shared_dyn_local[9]));
  }
  for (int i_2_1_s_211 = 0; i_2_1_s_211 < 4; ++i_2_1_s_211) {
    if (i_2_1_s_211 < 2) {
      Y_local[((i_2_1_s_211 * 16) + 73)] = (Y_local[((i_2_1_s_211 * 16) + 73)] + (A_shared_dyn_local[(i_2_1_s_211 + 4)] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_212 = 0; i_2_1_s_212 < 4; ++i_2_1_s_212) {
    Y_local[((i_2_1_s_212 * 16) + 10)] = (Y_local[((i_2_1_s_212 * 16) + 10)] + (A_shared_dyn_local[i_2_1_s_212] * B_shared_dyn_local[10]));
  }
  for (int i_2_1_s_213 = 0; i_2_1_s_213 < 4; ++i_2_1_s_213) {
    if (i_2_1_s_213 < 2) {
      Y_local[((i_2_1_s_213 * 16) + 74)] = (Y_local[((i_2_1_s_213 * 16) + 74)] + (A_shared_dyn_local[(i_2_1_s_213 + 4)] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_214 = 0; i_2_1_s_214 < 4; ++i_2_1_s_214) {
    Y_local[((i_2_1_s_214 * 16) + 11)] = (Y_local[((i_2_1_s_214 * 16) + 11)] + (A_shared_dyn_local[i_2_1_s_214] * B_shared_dyn_local[11]));
  }
  for (int i_2_1_s_215 = 0; i_2_1_s_215 < 4; ++i_2_1_s_215) {
    if (i_2_1_s_215 < 2) {
      Y_local[((i_2_1_s_215 * 16) + 75)] = (Y_local[((i_2_1_s_215 * 16) + 75)] + (A_shared_dyn_local[(i_2_1_s_215 + 4)] * B_shared_dyn_local[11]));
    }
  }
  for (int i_2_1_s_216 = 0; i_2_1_s_216 < 4; ++i_2_1_s_216) {
    Y_local[((i_2_1_s_216 * 16) + 12)] = (Y_local[((i_2_1_s_216 * 16) + 12)] + (A_shared_dyn_local[i_2_1_s_216] * B_shared_dyn_local[12]));
  }
  for (int i_2_1_s_217 = 0; i_2_1_s_217 < 4; ++i_2_1_s_217) {
    if (i_2_1_s_217 < 2) {
      Y_local[((i_2_1_s_217 * 16) + 76)] = (Y_local[((i_2_1_s_217 * 16) + 76)] + (A_shared_dyn_local[(i_2_1_s_217 + 4)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_218 = 0; i_2_1_s_218 < 4; ++i_2_1_s_218) {
    Y_local[((i_2_1_s_218 * 16) + 13)] = (Y_local[((i_2_1_s_218 * 16) + 13)] + (A_shared_dyn_local[i_2_1_s_218] * B_shared_dyn_local[13]));
  }
  for (int i_2_1_s_219 = 0; i_2_1_s_219 < 4; ++i_2_1_s_219) {
    if (i_2_1_s_219 < 2) {
      Y_local[((i_2_1_s_219 * 16) + 77)] = (Y_local[((i_2_1_s_219 * 16) + 77)] + (A_shared_dyn_local[(i_2_1_s_219 + 4)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_220 = 0; i_2_1_s_220 < 4; ++i_2_1_s_220) {
    Y_local[((i_2_1_s_220 * 16) + 14)] = (Y_local[((i_2_1_s_220 * 16) + 14)] + (A_shared_dyn_local[i_2_1_s_220] * B_shared_dyn_local[14]));
  }
  for (int i_2_1_s_221 = 0; i_2_1_s_221 < 4; ++i_2_1_s_221) {
    if (i_2_1_s_221 < 2) {
      Y_local[((i_2_1_s_221 * 16) + 78)] = (Y_local[((i_2_1_s_221 * 16) + 78)] + (A_shared_dyn_local[(i_2_1_s_221 + 4)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_222 = 0; i_2_1_s_222 < 4; ++i_2_1_s_222) {
    Y_local[((i_2_1_s_222 * 16) + 15)] = (Y_local[((i_2_1_s_222 * 16) + 15)] + (A_shared_dyn_local[i_2_1_s_222] * B_shared_dyn_local[15]));
  }
  for (int i_2_1_s_223 = 0; i_2_1_s_223 < 4; ++i_2_1_s_223) {
    if (i_2_1_s_223 < 2) {
      Y_local[((i_2_1_s_223 * 16) + 79)] = (Y_local[((i_2_1_s_223 * 16) + 79)] + (A_shared_dyn_local[(i_2_1_s_223 + 4)] * B_shared_dyn_local[15]));
    }
  }
  for (int ax0_0_8 = 0; ax0_0_8 < 2; ++ax0_0_8) {
    for (int ax0_1_s_8 = 0; ax0_1_s_8 < 4; ++ax0_1_s_8) {
      if (((ax0_0_8 * 2) + (ax0_1_s_8 >> 1)) < 3) {
        A_shared_dyn_local[((ax0_0_8 * 4) + ax0_1_s_8)] = ((float*)buf_dyn_shmem)[(((((((int)threadIdx.x) / 27) * 72) + ((((int)threadIdx.x) % 3) * 24)) + (ax0_0_8 * 16)) + (ax0_1_s_8 * 4))];
      }
    }
  }
  for (int ax1_0_8 = 0; ax1_0_8 < 4; ++ax1_0_8) {
    *(float4*)(B_shared_dyn_local + (ax1_0_8 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((int)blockIdx.x) & 7) * 144) + (((((int)threadIdx.x) % 27) / 3) * 16)) + (ax1_0_8 * 4)) >> 6) * 64) + ((ax1_0_8 & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 18) + (((((int)threadIdx.x) % 27) / 3) * 2)) + (ax1_0_8 >> 1)) & 7) * 4)) + 2880) - ((((((int)blockIdx.x) & 7) * 144) >> 6) * 64)));
  }
  for (int i_2_1_s_224 = 0; i_2_1_s_224 < 4; ++i_2_1_s_224) {
    Y_local[(i_2_1_s_224 * 16)] = (Y_local[(i_2_1_s_224 * 16)] + (A_shared_dyn_local[(i_2_1_s_224 + 6)] * B_shared_dyn_local[16]));
  }
  for (int i_2_1_s_225 = 0; i_2_1_s_225 < 4; ++i_2_1_s_225) {
    if (i_2_1_s_225 < 2) {
      Y_local[((i_2_1_s_225 * 16) + 64)] = (Y_local[((i_2_1_s_225 * 16) + 64)] + (A_shared_dyn_local[(i_2_1_s_225 + 10)] * B_shared_dyn_local[16]));
    }
  }
  for (int i_2_1_s_226 = 0; i_2_1_s_226 < 4; ++i_2_1_s_226) {
    Y_local[((i_2_1_s_226 * 16) + 1)] = (Y_local[((i_2_1_s_226 * 16) + 1)] + (A_shared_dyn_local[(i_2_1_s_226 + 6)] * B_shared_dyn_local[17]));
  }
  for (int i_2_1_s_227 = 0; i_2_1_s_227 < 4; ++i_2_1_s_227) {
    if (i_2_1_s_227 < 2) {
      Y_local[((i_2_1_s_227 * 16) + 65)] = (Y_local[((i_2_1_s_227 * 16) + 65)] + (A_shared_dyn_local[(i_2_1_s_227 + 10)] * B_shared_dyn_local[17]));
    }
  }
  for (int i_2_1_s_228 = 0; i_2_1_s_228 < 4; ++i_2_1_s_228) {
    Y_local[((i_2_1_s_228 * 16) + 2)] = (Y_local[((i_2_1_s_228 * 16) + 2)] + (A_shared_dyn_local[(i_2_1_s_228 + 6)] * B_shared_dyn_local[18]));
  }
  for (int i_2_1_s_229 = 0; i_2_1_s_229 < 4; ++i_2_1_s_229) {
    if (i_2_1_s_229 < 2) {
      Y_local[((i_2_1_s_229 * 16) + 66)] = (Y_local[((i_2_1_s_229 * 16) + 66)] + (A_shared_dyn_local[(i_2_1_s_229 + 10)] * B_shared_dyn_local[18]));
    }
  }
  for (int i_2_1_s_230 = 0; i_2_1_s_230 < 4; ++i_2_1_s_230) {
    Y_local[((i_2_1_s_230 * 16) + 3)] = (Y_local[((i_2_1_s_230 * 16) + 3)] + (A_shared_dyn_local[(i_2_1_s_230 + 6)] * B_shared_dyn_local[19]));
  }
  for (int i_2_1_s_231 = 0; i_2_1_s_231 < 4; ++i_2_1_s_231) {
    if (i_2_1_s_231 < 2) {
      Y_local[((i_2_1_s_231 * 16) + 67)] = (Y_local[((i_2_1_s_231 * 16) + 67)] + (A_shared_dyn_local[(i_2_1_s_231 + 10)] * B_shared_dyn_local[19]));
    }
  }
  for (int i_2_1_s_232 = 0; i_2_1_s_232 < 4; ++i_2_1_s_232) {
    Y_local[((i_2_1_s_232 * 16) + 4)] = (Y_local[((i_2_1_s_232 * 16) + 4)] + (A_shared_dyn_local[(i_2_1_s_232 + 6)] * B_shared_dyn_local[20]));
  }
  for (int i_2_1_s_233 = 0; i_2_1_s_233 < 4; ++i_2_1_s_233) {
    if (i_2_1_s_233 < 2) {
      Y_local[((i_2_1_s_233 * 16) + 68)] = (Y_local[((i_2_1_s_233 * 16) + 68)] + (A_shared_dyn_local[(i_2_1_s_233 + 10)] * B_shared_dyn_local[20]));
    }
  }
  for (int i_2_1_s_234 = 0; i_2_1_s_234 < 4; ++i_2_1_s_234) {
    Y_local[((i_2_1_s_234 * 16) + 5)] = (Y_local[((i_2_1_s_234 * 16) + 5)] + (A_shared_dyn_local[(i_2_1_s_234 + 6)] * B_shared_dyn_local[21]));
  }
  for (int i_2_1_s_235 = 0; i_2_1_s_235 < 4; ++i_2_1_s_235) {
    if (i_2_1_s_235 < 2) {
      Y_local[((i_2_1_s_235 * 16) + 69)] = (Y_local[((i_2_1_s_235 * 16) + 69)] + (A_shared_dyn_local[(i_2_1_s_235 + 10)] * B_shared_dyn_local[21]));
    }
  }
  for (int i_2_1_s_236 = 0; i_2_1_s_236 < 4; ++i_2_1_s_236) {
    Y_local[((i_2_1_s_236 * 16) + 6)] = (Y_local[((i_2_1_s_236 * 16) + 6)] + (A_shared_dyn_local[(i_2_1_s_236 + 6)] * B_shared_dyn_local[22]));
  }
  for (int i_2_1_s_237 = 0; i_2_1_s_237 < 4; ++i_2_1_s_237) {
    if (i_2_1_s_237 < 2) {
      Y_local[((i_2_1_s_237 * 16) + 70)] = (Y_local[((i_2_1_s_237 * 16) + 70)] + (A_shared_dyn_local[(i_2_1_s_237 + 10)] * B_shared_dyn_local[22]));
    }
  }
  for (int i_2_1_s_238 = 0; i_2_1_s_238 < 4; ++i_2_1_s_238) {
    Y_local[((i_2_1_s_238 * 16) + 7)] = (Y_local[((i_2_1_s_238 * 16) + 7)] + (A_shared_dyn_local[(i_2_1_s_238 + 6)] * B_shared_dyn_local[23]));
  }
  for (int i_2_1_s_239 = 0; i_2_1_s_239 < 4; ++i_2_1_s_239) {
    if (i_2_1_s_239 < 2) {
      Y_local[((i_2_1_s_239 * 16) + 71)] = (Y_local[((i_2_1_s_239 * 16) + 71)] + (A_shared_dyn_local[(i_2_1_s_239 + 10)] * B_shared_dyn_local[23]));
    }
  }
  for (int i_2_1_s_240 = 0; i_2_1_s_240 < 4; ++i_2_1_s_240) {
    Y_local[((i_2_1_s_240 * 16) + 8)] = (Y_local[((i_2_1_s_240 * 16) + 8)] + (A_shared_dyn_local[(i_2_1_s_240 + 6)] * B_shared_dyn_local[24]));
  }
  for (int i_2_1_s_241 = 0; i_2_1_s_241 < 4; ++i_2_1_s_241) {
    if (i_2_1_s_241 < 2) {
      Y_local[((i_2_1_s_241 * 16) + 72)] = (Y_local[((i_2_1_s_241 * 16) + 72)] + (A_shared_dyn_local[(i_2_1_s_241 + 10)] * B_shared_dyn_local[24]));
    }
  }
  for (int i_2_1_s_242 = 0; i_2_1_s_242 < 4; ++i_2_1_s_242) {
    Y_local[((i_2_1_s_242 * 16) + 9)] = (Y_local[((i_2_1_s_242 * 16) + 9)] + (A_shared_dyn_local[(i_2_1_s_242 + 6)] * B_shared_dyn_local[25]));
  }
  for (int i_2_1_s_243 = 0; i_2_1_s_243 < 4; ++i_2_1_s_243) {
    if (i_2_1_s_243 < 2) {
      Y_local[((i_2_1_s_243 * 16) + 73)] = (Y_local[((i_2_1_s_243 * 16) + 73)] + (A_shared_dyn_local[(i_2_1_s_243 + 10)] * B_shared_dyn_local[25]));
    }
  }
  for (int i_2_1_s_244 = 0; i_2_1_s_244 < 4; ++i_2_1_s_244) {
    Y_local[((i_2_1_s_244 * 16) + 10)] = (Y_local[((i_2_1_s_244 * 16) + 10)] + (A_shared_dyn_local[(i_2_1_s_244 + 6)] * B_shared_dyn_local[26]));
  }
  for (int i_2_1_s_245 = 0; i_2_1_s_245 < 4; ++i_2_1_s_245) {
    if (i_2_1_s_245 < 2) {
      Y_local[((i_2_1_s_245 * 16) + 74)] = (Y_local[((i_2_1_s_245 * 16) + 74)] + (A_shared_dyn_local[(i_2_1_s_245 + 10)] * B_shared_dyn_local[26]));
    }
  }
  for (int i_2_1_s_246 = 0; i_2_1_s_246 < 4; ++i_2_1_s_246) {
    Y_local[((i_2_1_s_246 * 16) + 11)] = (Y_local[((i_2_1_s_246 * 16) + 11)] + (A_shared_dyn_local[(i_2_1_s_246 + 6)] * B_shared_dyn_local[27]));
  }
  for (int i_2_1_s_247 = 0; i_2_1_s_247 < 4; ++i_2_1_s_247) {
    if (i_2_1_s_247 < 2) {
      Y_local[((i_2_1_s_247 * 16) + 75)] = (Y_local[((i_2_1_s_247 * 16) + 75)] + (A_shared_dyn_local[(i_2_1_s_247 + 10)] * B_shared_dyn_local[27]));
    }
  }
  for (int i_2_1_s_248 = 0; i_2_1_s_248 < 4; ++i_2_1_s_248) {
    Y_local[((i_2_1_s_248 * 16) + 12)] = (Y_local[((i_2_1_s_248 * 16) + 12)] + (A_shared_dyn_local[(i_2_1_s_248 + 6)] * B_shared_dyn_local[28]));
  }
  for (int i_2_1_s_249 = 0; i_2_1_s_249 < 4; ++i_2_1_s_249) {
    if (i_2_1_s_249 < 2) {
      Y_local[((i_2_1_s_249 * 16) + 76)] = (Y_local[((i_2_1_s_249 * 16) + 76)] + (A_shared_dyn_local[(i_2_1_s_249 + 10)] * B_shared_dyn_local[28]));
    }
  }
  for (int i_2_1_s_250 = 0; i_2_1_s_250 < 4; ++i_2_1_s_250) {
    Y_local[((i_2_1_s_250 * 16) + 13)] = (Y_local[((i_2_1_s_250 * 16) + 13)] + (A_shared_dyn_local[(i_2_1_s_250 + 6)] * B_shared_dyn_local[29]));
  }
  for (int i_2_1_s_251 = 0; i_2_1_s_251 < 4; ++i_2_1_s_251) {
    if (i_2_1_s_251 < 2) {
      Y_local[((i_2_1_s_251 * 16) + 77)] = (Y_local[((i_2_1_s_251 * 16) + 77)] + (A_shared_dyn_local[(i_2_1_s_251 + 10)] * B_shared_dyn_local[29]));
    }
  }
  for (int i_2_1_s_252 = 0; i_2_1_s_252 < 4; ++i_2_1_s_252) {
    Y_local[((i_2_1_s_252 * 16) + 14)] = (Y_local[((i_2_1_s_252 * 16) + 14)] + (A_shared_dyn_local[(i_2_1_s_252 + 6)] * B_shared_dyn_local[30]));
  }
  for (int i_2_1_s_253 = 0; i_2_1_s_253 < 4; ++i_2_1_s_253) {
    if (i_2_1_s_253 < 2) {
      Y_local[((i_2_1_s_253 * 16) + 78)] = (Y_local[((i_2_1_s_253 * 16) + 78)] + (A_shared_dyn_local[(i_2_1_s_253 + 10)] * B_shared_dyn_local[30]));
    }
  }
  for (int i_2_1_s_254 = 0; i_2_1_s_254 < 4; ++i_2_1_s_254) {
    Y_local[((i_2_1_s_254 * 16) + 15)] = (Y_local[((i_2_1_s_254 * 16) + 15)] + (A_shared_dyn_local[(i_2_1_s_254 + 6)] * B_shared_dyn_local[31]));
  }
  for (int i_2_1_s_255 = 0; i_2_1_s_255 < 4; ++i_2_1_s_255) {
    if (i_2_1_s_255 < 2) {
      Y_local[((i_2_1_s_255 * 16) + 79)] = (Y_local[((i_2_1_s_255 * 16) + 79)] + (A_shared_dyn_local[(i_2_1_s_255 + 10)] * B_shared_dyn_local[31]));
    }
  }
__asm__ __volatile__("cp.async.wait_group 1;");

  __syncthreads();
  for (int ax0_0_9 = 0; ax0_0_9 < 2; ++ax0_0_9) {
    for (int ax0_1_s_9 = 0; ax0_1_s_9 < 4; ++ax0_1_s_9) {
      if (((ax0_0_9 * 2) + (ax0_1_s_9 >> 1)) < 3) {
        A_shared_dyn_local[(((ax0_0_9 * 4) + ax0_1_s_9) + 6)] = ((float*)buf_dyn_shmem)[((((((((int)threadIdx.x) / 27) * 72) + ((((int)threadIdx.x) % 3) * 24)) + (ax0_0_9 * 16)) + (ax0_1_s_9 * 4)) + 1)];
      }
    }
  }
  for (int ax1_0_9 = 0; ax1_0_9 < 4; ++ax1_0_9) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_9 * 4) + 16)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((int)blockIdx.x) & 7) * 144) + (((((int)threadIdx.x) % 27) / 3) * 16)) + (ax1_0_9 * 4)) >> 6) * 64) + ((ax1_0_9 & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 18) + (((((int)threadIdx.x) % 27) / 3) * 2)) + (ax1_0_9 >> 1)) & 7) * 4)) + 3072) - ((((((int)blockIdx.x) & 7) * 144) >> 6) * 64)));
  }
  for (int i_2_1_s_256 = 0; i_2_1_s_256 < 4; ++i_2_1_s_256) {
    Y_local[(i_2_1_s_256 * 16)] = (Y_local[(i_2_1_s_256 * 16)] + (A_shared_dyn_local[i_2_1_s_256] * B_shared_dyn_local[0]));
  }
  for (int i_2_1_s_257 = 0; i_2_1_s_257 < 4; ++i_2_1_s_257) {
    if (i_2_1_s_257 < 2) {
      Y_local[((i_2_1_s_257 * 16) + 64)] = (Y_local[((i_2_1_s_257 * 16) + 64)] + (A_shared_dyn_local[(i_2_1_s_257 + 4)] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_258 = 0; i_2_1_s_258 < 4; ++i_2_1_s_258) {
    Y_local[((i_2_1_s_258 * 16) + 1)] = (Y_local[((i_2_1_s_258 * 16) + 1)] + (A_shared_dyn_local[i_2_1_s_258] * B_shared_dyn_local[1]));
  }
  for (int i_2_1_s_259 = 0; i_2_1_s_259 < 4; ++i_2_1_s_259) {
    if (i_2_1_s_259 < 2) {
      Y_local[((i_2_1_s_259 * 16) + 65)] = (Y_local[((i_2_1_s_259 * 16) + 65)] + (A_shared_dyn_local[(i_2_1_s_259 + 4)] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_260 = 0; i_2_1_s_260 < 4; ++i_2_1_s_260) {
    Y_local[((i_2_1_s_260 * 16) + 2)] = (Y_local[((i_2_1_s_260 * 16) + 2)] + (A_shared_dyn_local[i_2_1_s_260] * B_shared_dyn_local[2]));
  }
  for (int i_2_1_s_261 = 0; i_2_1_s_261 < 4; ++i_2_1_s_261) {
    if (i_2_1_s_261 < 2) {
      Y_local[((i_2_1_s_261 * 16) + 66)] = (Y_local[((i_2_1_s_261 * 16) + 66)] + (A_shared_dyn_local[(i_2_1_s_261 + 4)] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_262 = 0; i_2_1_s_262 < 4; ++i_2_1_s_262) {
    Y_local[((i_2_1_s_262 * 16) + 3)] = (Y_local[((i_2_1_s_262 * 16) + 3)] + (A_shared_dyn_local[i_2_1_s_262] * B_shared_dyn_local[3]));
  }
  for (int i_2_1_s_263 = 0; i_2_1_s_263 < 4; ++i_2_1_s_263) {
    if (i_2_1_s_263 < 2) {
      Y_local[((i_2_1_s_263 * 16) + 67)] = (Y_local[((i_2_1_s_263 * 16) + 67)] + (A_shared_dyn_local[(i_2_1_s_263 + 4)] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_264 = 0; i_2_1_s_264 < 4; ++i_2_1_s_264) {
    Y_local[((i_2_1_s_264 * 16) + 4)] = (Y_local[((i_2_1_s_264 * 16) + 4)] + (A_shared_dyn_local[i_2_1_s_264] * B_shared_dyn_local[4]));
  }
  for (int i_2_1_s_265 = 0; i_2_1_s_265 < 4; ++i_2_1_s_265) {
    if (i_2_1_s_265 < 2) {
      Y_local[((i_2_1_s_265 * 16) + 68)] = (Y_local[((i_2_1_s_265 * 16) + 68)] + (A_shared_dyn_local[(i_2_1_s_265 + 4)] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_266 = 0; i_2_1_s_266 < 4; ++i_2_1_s_266) {
    Y_local[((i_2_1_s_266 * 16) + 5)] = (Y_local[((i_2_1_s_266 * 16) + 5)] + (A_shared_dyn_local[i_2_1_s_266] * B_shared_dyn_local[5]));
  }
  for (int i_2_1_s_267 = 0; i_2_1_s_267 < 4; ++i_2_1_s_267) {
    if (i_2_1_s_267 < 2) {
      Y_local[((i_2_1_s_267 * 16) + 69)] = (Y_local[((i_2_1_s_267 * 16) + 69)] + (A_shared_dyn_local[(i_2_1_s_267 + 4)] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_268 = 0; i_2_1_s_268 < 4; ++i_2_1_s_268) {
    Y_local[((i_2_1_s_268 * 16) + 6)] = (Y_local[((i_2_1_s_268 * 16) + 6)] + (A_shared_dyn_local[i_2_1_s_268] * B_shared_dyn_local[6]));
  }
  for (int i_2_1_s_269 = 0; i_2_1_s_269 < 4; ++i_2_1_s_269) {
    if (i_2_1_s_269 < 2) {
      Y_local[((i_2_1_s_269 * 16) + 70)] = (Y_local[((i_2_1_s_269 * 16) + 70)] + (A_shared_dyn_local[(i_2_1_s_269 + 4)] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_270 = 0; i_2_1_s_270 < 4; ++i_2_1_s_270) {
    Y_local[((i_2_1_s_270 * 16) + 7)] = (Y_local[((i_2_1_s_270 * 16) + 7)] + (A_shared_dyn_local[i_2_1_s_270] * B_shared_dyn_local[7]));
  }
  for (int i_2_1_s_271 = 0; i_2_1_s_271 < 4; ++i_2_1_s_271) {
    if (i_2_1_s_271 < 2) {
      Y_local[((i_2_1_s_271 * 16) + 71)] = (Y_local[((i_2_1_s_271 * 16) + 71)] + (A_shared_dyn_local[(i_2_1_s_271 + 4)] * B_shared_dyn_local[7]));
    }
  }
  for (int i_2_1_s_272 = 0; i_2_1_s_272 < 4; ++i_2_1_s_272) {
    Y_local[((i_2_1_s_272 * 16) + 8)] = (Y_local[((i_2_1_s_272 * 16) + 8)] + (A_shared_dyn_local[i_2_1_s_272] * B_shared_dyn_local[8]));
  }
  for (int i_2_1_s_273 = 0; i_2_1_s_273 < 4; ++i_2_1_s_273) {
    if (i_2_1_s_273 < 2) {
      Y_local[((i_2_1_s_273 * 16) + 72)] = (Y_local[((i_2_1_s_273 * 16) + 72)] + (A_shared_dyn_local[(i_2_1_s_273 + 4)] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_274 = 0; i_2_1_s_274 < 4; ++i_2_1_s_274) {
    Y_local[((i_2_1_s_274 * 16) + 9)] = (Y_local[((i_2_1_s_274 * 16) + 9)] + (A_shared_dyn_local[i_2_1_s_274] * B_shared_dyn_local[9]));
  }
  for (int i_2_1_s_275 = 0; i_2_1_s_275 < 4; ++i_2_1_s_275) {
    if (i_2_1_s_275 < 2) {
      Y_local[((i_2_1_s_275 * 16) + 73)] = (Y_local[((i_2_1_s_275 * 16) + 73)] + (A_shared_dyn_local[(i_2_1_s_275 + 4)] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_276 = 0; i_2_1_s_276 < 4; ++i_2_1_s_276) {
    Y_local[((i_2_1_s_276 * 16) + 10)] = (Y_local[((i_2_1_s_276 * 16) + 10)] + (A_shared_dyn_local[i_2_1_s_276] * B_shared_dyn_local[10]));
  }
  for (int i_2_1_s_277 = 0; i_2_1_s_277 < 4; ++i_2_1_s_277) {
    if (i_2_1_s_277 < 2) {
      Y_local[((i_2_1_s_277 * 16) + 74)] = (Y_local[((i_2_1_s_277 * 16) + 74)] + (A_shared_dyn_local[(i_2_1_s_277 + 4)] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_278 = 0; i_2_1_s_278 < 4; ++i_2_1_s_278) {
    Y_local[((i_2_1_s_278 * 16) + 11)] = (Y_local[((i_2_1_s_278 * 16) + 11)] + (A_shared_dyn_local[i_2_1_s_278] * B_shared_dyn_local[11]));
  }
  for (int i_2_1_s_279 = 0; i_2_1_s_279 < 4; ++i_2_1_s_279) {
    if (i_2_1_s_279 < 2) {
      Y_local[((i_2_1_s_279 * 16) + 75)] = (Y_local[((i_2_1_s_279 * 16) + 75)] + (A_shared_dyn_local[(i_2_1_s_279 + 4)] * B_shared_dyn_local[11]));
    }
  }
  for (int i_2_1_s_280 = 0; i_2_1_s_280 < 4; ++i_2_1_s_280) {
    Y_local[((i_2_1_s_280 * 16) + 12)] = (Y_local[((i_2_1_s_280 * 16) + 12)] + (A_shared_dyn_local[i_2_1_s_280] * B_shared_dyn_local[12]));
  }
  for (int i_2_1_s_281 = 0; i_2_1_s_281 < 4; ++i_2_1_s_281) {
    if (i_2_1_s_281 < 2) {
      Y_local[((i_2_1_s_281 * 16) + 76)] = (Y_local[((i_2_1_s_281 * 16) + 76)] + (A_shared_dyn_local[(i_2_1_s_281 + 4)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_282 = 0; i_2_1_s_282 < 4; ++i_2_1_s_282) {
    Y_local[((i_2_1_s_282 * 16) + 13)] = (Y_local[((i_2_1_s_282 * 16) + 13)] + (A_shared_dyn_local[i_2_1_s_282] * B_shared_dyn_local[13]));
  }
  for (int i_2_1_s_283 = 0; i_2_1_s_283 < 4; ++i_2_1_s_283) {
    if (i_2_1_s_283 < 2) {
      Y_local[((i_2_1_s_283 * 16) + 77)] = (Y_local[((i_2_1_s_283 * 16) + 77)] + (A_shared_dyn_local[(i_2_1_s_283 + 4)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_284 = 0; i_2_1_s_284 < 4; ++i_2_1_s_284) {
    Y_local[((i_2_1_s_284 * 16) + 14)] = (Y_local[((i_2_1_s_284 * 16) + 14)] + (A_shared_dyn_local[i_2_1_s_284] * B_shared_dyn_local[14]));
  }
  for (int i_2_1_s_285 = 0; i_2_1_s_285 < 4; ++i_2_1_s_285) {
    if (i_2_1_s_285 < 2) {
      Y_local[((i_2_1_s_285 * 16) + 78)] = (Y_local[((i_2_1_s_285 * 16) + 78)] + (A_shared_dyn_local[(i_2_1_s_285 + 4)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_286 = 0; i_2_1_s_286 < 4; ++i_2_1_s_286) {
    Y_local[((i_2_1_s_286 * 16) + 15)] = (Y_local[((i_2_1_s_286 * 16) + 15)] + (A_shared_dyn_local[i_2_1_s_286] * B_shared_dyn_local[15]));
  }
  for (int i_2_1_s_287 = 0; i_2_1_s_287 < 4; ++i_2_1_s_287) {
    if (i_2_1_s_287 < 2) {
      Y_local[((i_2_1_s_287 * 16) + 79)] = (Y_local[((i_2_1_s_287 * 16) + 79)] + (A_shared_dyn_local[(i_2_1_s_287 + 4)] * B_shared_dyn_local[15]));
    }
  }
  for (int ax0_0_10 = 0; ax0_0_10 < 2; ++ax0_0_10) {
    for (int ax0_1_s_10 = 0; ax0_1_s_10 < 4; ++ax0_1_s_10) {
      if (((ax0_0_10 * 2) + (ax0_1_s_10 >> 1)) < 3) {
        A_shared_dyn_local[((ax0_0_10 * 4) + ax0_1_s_10)] = ((float*)buf_dyn_shmem)[((((((((int)threadIdx.x) / 27) * 72) + ((((int)threadIdx.x) % 3) * 24)) + (ax0_0_10 * 16)) + (ax0_1_s_10 * 4)) + 2)];
      }
    }
  }
  for (int ax1_0_10 = 0; ax1_0_10 < 4; ++ax1_0_10) {
    *(float4*)(B_shared_dyn_local + (ax1_0_10 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((int)blockIdx.x) & 7) * 144) + (((((int)threadIdx.x) % 27) / 3) * 16)) + (ax1_0_10 * 4)) >> 6) * 64) + ((ax1_0_10 & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 18) + (((((int)threadIdx.x) % 27) / 3) * 2)) + (ax1_0_10 >> 1)) & 7) * 4)) + 3264) - ((((((int)blockIdx.x) & 7) * 144) >> 6) * 64)));
  }
  for (int i_2_1_s_288 = 0; i_2_1_s_288 < 4; ++i_2_1_s_288) {
    Y_local[(i_2_1_s_288 * 16)] = (Y_local[(i_2_1_s_288 * 16)] + (A_shared_dyn_local[(i_2_1_s_288 + 6)] * B_shared_dyn_local[16]));
  }
  for (int i_2_1_s_289 = 0; i_2_1_s_289 < 4; ++i_2_1_s_289) {
    if (i_2_1_s_289 < 2) {
      Y_local[((i_2_1_s_289 * 16) + 64)] = (Y_local[((i_2_1_s_289 * 16) + 64)] + (A_shared_dyn_local[(i_2_1_s_289 + 10)] * B_shared_dyn_local[16]));
    }
  }
  for (int i_2_1_s_290 = 0; i_2_1_s_290 < 4; ++i_2_1_s_290) {
    Y_local[((i_2_1_s_290 * 16) + 1)] = (Y_local[((i_2_1_s_290 * 16) + 1)] + (A_shared_dyn_local[(i_2_1_s_290 + 6)] * B_shared_dyn_local[17]));
  }
  for (int i_2_1_s_291 = 0; i_2_1_s_291 < 4; ++i_2_1_s_291) {
    if (i_2_1_s_291 < 2) {
      Y_local[((i_2_1_s_291 * 16) + 65)] = (Y_local[((i_2_1_s_291 * 16) + 65)] + (A_shared_dyn_local[(i_2_1_s_291 + 10)] * B_shared_dyn_local[17]));
    }
  }
  for (int i_2_1_s_292 = 0; i_2_1_s_292 < 4; ++i_2_1_s_292) {
    Y_local[((i_2_1_s_292 * 16) + 2)] = (Y_local[((i_2_1_s_292 * 16) + 2)] + (A_shared_dyn_local[(i_2_1_s_292 + 6)] * B_shared_dyn_local[18]));
  }
  for (int i_2_1_s_293 = 0; i_2_1_s_293 < 4; ++i_2_1_s_293) {
    if (i_2_1_s_293 < 2) {
      Y_local[((i_2_1_s_293 * 16) + 66)] = (Y_local[((i_2_1_s_293 * 16) + 66)] + (A_shared_dyn_local[(i_2_1_s_293 + 10)] * B_shared_dyn_local[18]));
    }
  }
  for (int i_2_1_s_294 = 0; i_2_1_s_294 < 4; ++i_2_1_s_294) {
    Y_local[((i_2_1_s_294 * 16) + 3)] = (Y_local[((i_2_1_s_294 * 16) + 3)] + (A_shared_dyn_local[(i_2_1_s_294 + 6)] * B_shared_dyn_local[19]));
  }
  for (int i_2_1_s_295 = 0; i_2_1_s_295 < 4; ++i_2_1_s_295) {
    if (i_2_1_s_295 < 2) {
      Y_local[((i_2_1_s_295 * 16) + 67)] = (Y_local[((i_2_1_s_295 * 16) + 67)] + (A_shared_dyn_local[(i_2_1_s_295 + 10)] * B_shared_dyn_local[19]));
    }
  }
  for (int i_2_1_s_296 = 0; i_2_1_s_296 < 4; ++i_2_1_s_296) {
    Y_local[((i_2_1_s_296 * 16) + 4)] = (Y_local[((i_2_1_s_296 * 16) + 4)] + (A_shared_dyn_local[(i_2_1_s_296 + 6)] * B_shared_dyn_local[20]));
  }
  for (int i_2_1_s_297 = 0; i_2_1_s_297 < 4; ++i_2_1_s_297) {
    if (i_2_1_s_297 < 2) {
      Y_local[((i_2_1_s_297 * 16) + 68)] = (Y_local[((i_2_1_s_297 * 16) + 68)] + (A_shared_dyn_local[(i_2_1_s_297 + 10)] * B_shared_dyn_local[20]));
    }
  }
  for (int i_2_1_s_298 = 0; i_2_1_s_298 < 4; ++i_2_1_s_298) {
    Y_local[((i_2_1_s_298 * 16) + 5)] = (Y_local[((i_2_1_s_298 * 16) + 5)] + (A_shared_dyn_local[(i_2_1_s_298 + 6)] * B_shared_dyn_local[21]));
  }
  for (int i_2_1_s_299 = 0; i_2_1_s_299 < 4; ++i_2_1_s_299) {
    if (i_2_1_s_299 < 2) {
      Y_local[((i_2_1_s_299 * 16) + 69)] = (Y_local[((i_2_1_s_299 * 16) + 69)] + (A_shared_dyn_local[(i_2_1_s_299 + 10)] * B_shared_dyn_local[21]));
    }
  }
  for (int i_2_1_s_300 = 0; i_2_1_s_300 < 4; ++i_2_1_s_300) {
    Y_local[((i_2_1_s_300 * 16) + 6)] = (Y_local[((i_2_1_s_300 * 16) + 6)] + (A_shared_dyn_local[(i_2_1_s_300 + 6)] * B_shared_dyn_local[22]));
  }
  for (int i_2_1_s_301 = 0; i_2_1_s_301 < 4; ++i_2_1_s_301) {
    if (i_2_1_s_301 < 2) {
      Y_local[((i_2_1_s_301 * 16) + 70)] = (Y_local[((i_2_1_s_301 * 16) + 70)] + (A_shared_dyn_local[(i_2_1_s_301 + 10)] * B_shared_dyn_local[22]));
    }
  }
  for (int i_2_1_s_302 = 0; i_2_1_s_302 < 4; ++i_2_1_s_302) {
    Y_local[((i_2_1_s_302 * 16) + 7)] = (Y_local[((i_2_1_s_302 * 16) + 7)] + (A_shared_dyn_local[(i_2_1_s_302 + 6)] * B_shared_dyn_local[23]));
  }
  for (int i_2_1_s_303 = 0; i_2_1_s_303 < 4; ++i_2_1_s_303) {
    if (i_2_1_s_303 < 2) {
      Y_local[((i_2_1_s_303 * 16) + 71)] = (Y_local[((i_2_1_s_303 * 16) + 71)] + (A_shared_dyn_local[(i_2_1_s_303 + 10)] * B_shared_dyn_local[23]));
    }
  }
  for (int i_2_1_s_304 = 0; i_2_1_s_304 < 4; ++i_2_1_s_304) {
    Y_local[((i_2_1_s_304 * 16) + 8)] = (Y_local[((i_2_1_s_304 * 16) + 8)] + (A_shared_dyn_local[(i_2_1_s_304 + 6)] * B_shared_dyn_local[24]));
  }
  for (int i_2_1_s_305 = 0; i_2_1_s_305 < 4; ++i_2_1_s_305) {
    if (i_2_1_s_305 < 2) {
      Y_local[((i_2_1_s_305 * 16) + 72)] = (Y_local[((i_2_1_s_305 * 16) + 72)] + (A_shared_dyn_local[(i_2_1_s_305 + 10)] * B_shared_dyn_local[24]));
    }
  }
  for (int i_2_1_s_306 = 0; i_2_1_s_306 < 4; ++i_2_1_s_306) {
    Y_local[((i_2_1_s_306 * 16) + 9)] = (Y_local[((i_2_1_s_306 * 16) + 9)] + (A_shared_dyn_local[(i_2_1_s_306 + 6)] * B_shared_dyn_local[25]));
  }
  for (int i_2_1_s_307 = 0; i_2_1_s_307 < 4; ++i_2_1_s_307) {
    if (i_2_1_s_307 < 2) {
      Y_local[((i_2_1_s_307 * 16) + 73)] = (Y_local[((i_2_1_s_307 * 16) + 73)] + (A_shared_dyn_local[(i_2_1_s_307 + 10)] * B_shared_dyn_local[25]));
    }
  }
  for (int i_2_1_s_308 = 0; i_2_1_s_308 < 4; ++i_2_1_s_308) {
    Y_local[((i_2_1_s_308 * 16) + 10)] = (Y_local[((i_2_1_s_308 * 16) + 10)] + (A_shared_dyn_local[(i_2_1_s_308 + 6)] * B_shared_dyn_local[26]));
  }
  for (int i_2_1_s_309 = 0; i_2_1_s_309 < 4; ++i_2_1_s_309) {
    if (i_2_1_s_309 < 2) {
      Y_local[((i_2_1_s_309 * 16) + 74)] = (Y_local[((i_2_1_s_309 * 16) + 74)] + (A_shared_dyn_local[(i_2_1_s_309 + 10)] * B_shared_dyn_local[26]));
    }
  }
  for (int i_2_1_s_310 = 0; i_2_1_s_310 < 4; ++i_2_1_s_310) {
    Y_local[((i_2_1_s_310 * 16) + 11)] = (Y_local[((i_2_1_s_310 * 16) + 11)] + (A_shared_dyn_local[(i_2_1_s_310 + 6)] * B_shared_dyn_local[27]));
  }
  for (int i_2_1_s_311 = 0; i_2_1_s_311 < 4; ++i_2_1_s_311) {
    if (i_2_1_s_311 < 2) {
      Y_local[((i_2_1_s_311 * 16) + 75)] = (Y_local[((i_2_1_s_311 * 16) + 75)] + (A_shared_dyn_local[(i_2_1_s_311 + 10)] * B_shared_dyn_local[27]));
    }
  }
  for (int i_2_1_s_312 = 0; i_2_1_s_312 < 4; ++i_2_1_s_312) {
    Y_local[((i_2_1_s_312 * 16) + 12)] = (Y_local[((i_2_1_s_312 * 16) + 12)] + (A_shared_dyn_local[(i_2_1_s_312 + 6)] * B_shared_dyn_local[28]));
  }
  for (int i_2_1_s_313 = 0; i_2_1_s_313 < 4; ++i_2_1_s_313) {
    if (i_2_1_s_313 < 2) {
      Y_local[((i_2_1_s_313 * 16) + 76)] = (Y_local[((i_2_1_s_313 * 16) + 76)] + (A_shared_dyn_local[(i_2_1_s_313 + 10)] * B_shared_dyn_local[28]));
    }
  }
  for (int i_2_1_s_314 = 0; i_2_1_s_314 < 4; ++i_2_1_s_314) {
    Y_local[((i_2_1_s_314 * 16) + 13)] = (Y_local[((i_2_1_s_314 * 16) + 13)] + (A_shared_dyn_local[(i_2_1_s_314 + 6)] * B_shared_dyn_local[29]));
  }
  for (int i_2_1_s_315 = 0; i_2_1_s_315 < 4; ++i_2_1_s_315) {
    if (i_2_1_s_315 < 2) {
      Y_local[((i_2_1_s_315 * 16) + 77)] = (Y_local[((i_2_1_s_315 * 16) + 77)] + (A_shared_dyn_local[(i_2_1_s_315 + 10)] * B_shared_dyn_local[29]));
    }
  }
  for (int i_2_1_s_316 = 0; i_2_1_s_316 < 4; ++i_2_1_s_316) {
    Y_local[((i_2_1_s_316 * 16) + 14)] = (Y_local[((i_2_1_s_316 * 16) + 14)] + (A_shared_dyn_local[(i_2_1_s_316 + 6)] * B_shared_dyn_local[30]));
  }
  for (int i_2_1_s_317 = 0; i_2_1_s_317 < 4; ++i_2_1_s_317) {
    if (i_2_1_s_317 < 2) {
      Y_local[((i_2_1_s_317 * 16) + 78)] = (Y_local[((i_2_1_s_317 * 16) + 78)] + (A_shared_dyn_local[(i_2_1_s_317 + 10)] * B_shared_dyn_local[30]));
    }
  }
  for (int i_2_1_s_318 = 0; i_2_1_s_318 < 4; ++i_2_1_s_318) {
    Y_local[((i_2_1_s_318 * 16) + 15)] = (Y_local[((i_2_1_s_318 * 16) + 15)] + (A_shared_dyn_local[(i_2_1_s_318 + 6)] * B_shared_dyn_local[31]));
  }
  for (int i_2_1_s_319 = 0; i_2_1_s_319 < 4; ++i_2_1_s_319) {
    if (i_2_1_s_319 < 2) {
      Y_local[((i_2_1_s_319 * 16) + 79)] = (Y_local[((i_2_1_s_319 * 16) + 79)] + (A_shared_dyn_local[(i_2_1_s_319 + 10)] * B_shared_dyn_local[31]));
    }
  }
  for (int ax0_0_11 = 0; ax0_0_11 < 2; ++ax0_0_11) {
    for (int ax0_1_s_11 = 0; ax0_1_s_11 < 4; ++ax0_1_s_11) {
      if (((ax0_0_11 * 2) + (ax0_1_s_11 >> 1)) < 3) {
        A_shared_dyn_local[(((ax0_0_11 * 4) + ax0_1_s_11) + 6)] = ((float*)buf_dyn_shmem)[((((((((int)threadIdx.x) / 27) * 72) + ((((int)threadIdx.x) % 3) * 24)) + (ax0_0_11 * 16)) + (ax0_1_s_11 * 4)) + 3)];
      }
    }
  }
  for (int ax1_0_11 = 0; ax1_0_11 < 4; ++ax1_0_11) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_11 * 4) + 16)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((int)blockIdx.x) & 7) * 144) + (((((int)threadIdx.x) % 27) / 3) * 16)) + (ax1_0_11 * 4)) >> 6) * 64) + ((ax1_0_11 & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 18) + (((((int)threadIdx.x) % 27) / 3) * 2)) + (ax1_0_11 >> 1)) & 7) * 4)) + 3456) - ((((((int)blockIdx.x) & 7) * 144) >> 6) * 64)));
  }
  for (int i_2_1_s_320 = 0; i_2_1_s_320 < 4; ++i_2_1_s_320) {
    Y_local[(i_2_1_s_320 * 16)] = (Y_local[(i_2_1_s_320 * 16)] + (A_shared_dyn_local[i_2_1_s_320] * B_shared_dyn_local[0]));
  }
  for (int i_2_1_s_321 = 0; i_2_1_s_321 < 4; ++i_2_1_s_321) {
    if (i_2_1_s_321 < 2) {
      Y_local[((i_2_1_s_321 * 16) + 64)] = (Y_local[((i_2_1_s_321 * 16) + 64)] + (A_shared_dyn_local[(i_2_1_s_321 + 4)] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_322 = 0; i_2_1_s_322 < 4; ++i_2_1_s_322) {
    Y_local[((i_2_1_s_322 * 16) + 1)] = (Y_local[((i_2_1_s_322 * 16) + 1)] + (A_shared_dyn_local[i_2_1_s_322] * B_shared_dyn_local[1]));
  }
  for (int i_2_1_s_323 = 0; i_2_1_s_323 < 4; ++i_2_1_s_323) {
    if (i_2_1_s_323 < 2) {
      Y_local[((i_2_1_s_323 * 16) + 65)] = (Y_local[((i_2_1_s_323 * 16) + 65)] + (A_shared_dyn_local[(i_2_1_s_323 + 4)] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_324 = 0; i_2_1_s_324 < 4; ++i_2_1_s_324) {
    Y_local[((i_2_1_s_324 * 16) + 2)] = (Y_local[((i_2_1_s_324 * 16) + 2)] + (A_shared_dyn_local[i_2_1_s_324] * B_shared_dyn_local[2]));
  }
  for (int i_2_1_s_325 = 0; i_2_1_s_325 < 4; ++i_2_1_s_325) {
    if (i_2_1_s_325 < 2) {
      Y_local[((i_2_1_s_325 * 16) + 66)] = (Y_local[((i_2_1_s_325 * 16) + 66)] + (A_shared_dyn_local[(i_2_1_s_325 + 4)] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_326 = 0; i_2_1_s_326 < 4; ++i_2_1_s_326) {
    Y_local[((i_2_1_s_326 * 16) + 3)] = (Y_local[((i_2_1_s_326 * 16) + 3)] + (A_shared_dyn_local[i_2_1_s_326] * B_shared_dyn_local[3]));
  }
  for (int i_2_1_s_327 = 0; i_2_1_s_327 < 4; ++i_2_1_s_327) {
    if (i_2_1_s_327 < 2) {
      Y_local[((i_2_1_s_327 * 16) + 67)] = (Y_local[((i_2_1_s_327 * 16) + 67)] + (A_shared_dyn_local[(i_2_1_s_327 + 4)] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_328 = 0; i_2_1_s_328 < 4; ++i_2_1_s_328) {
    Y_local[((i_2_1_s_328 * 16) + 4)] = (Y_local[((i_2_1_s_328 * 16) + 4)] + (A_shared_dyn_local[i_2_1_s_328] * B_shared_dyn_local[4]));
  }
  for (int i_2_1_s_329 = 0; i_2_1_s_329 < 4; ++i_2_1_s_329) {
    if (i_2_1_s_329 < 2) {
      Y_local[((i_2_1_s_329 * 16) + 68)] = (Y_local[((i_2_1_s_329 * 16) + 68)] + (A_shared_dyn_local[(i_2_1_s_329 + 4)] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_330 = 0; i_2_1_s_330 < 4; ++i_2_1_s_330) {
    Y_local[((i_2_1_s_330 * 16) + 5)] = (Y_local[((i_2_1_s_330 * 16) + 5)] + (A_shared_dyn_local[i_2_1_s_330] * B_shared_dyn_local[5]));
  }
  for (int i_2_1_s_331 = 0; i_2_1_s_331 < 4; ++i_2_1_s_331) {
    if (i_2_1_s_331 < 2) {
      Y_local[((i_2_1_s_331 * 16) + 69)] = (Y_local[((i_2_1_s_331 * 16) + 69)] + (A_shared_dyn_local[(i_2_1_s_331 + 4)] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_332 = 0; i_2_1_s_332 < 4; ++i_2_1_s_332) {
    Y_local[((i_2_1_s_332 * 16) + 6)] = (Y_local[((i_2_1_s_332 * 16) + 6)] + (A_shared_dyn_local[i_2_1_s_332] * B_shared_dyn_local[6]));
  }
  for (int i_2_1_s_333 = 0; i_2_1_s_333 < 4; ++i_2_1_s_333) {
    if (i_2_1_s_333 < 2) {
      Y_local[((i_2_1_s_333 * 16) + 70)] = (Y_local[((i_2_1_s_333 * 16) + 70)] + (A_shared_dyn_local[(i_2_1_s_333 + 4)] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_334 = 0; i_2_1_s_334 < 4; ++i_2_1_s_334) {
    Y_local[((i_2_1_s_334 * 16) + 7)] = (Y_local[((i_2_1_s_334 * 16) + 7)] + (A_shared_dyn_local[i_2_1_s_334] * B_shared_dyn_local[7]));
  }
  for (int i_2_1_s_335 = 0; i_2_1_s_335 < 4; ++i_2_1_s_335) {
    if (i_2_1_s_335 < 2) {
      Y_local[((i_2_1_s_335 * 16) + 71)] = (Y_local[((i_2_1_s_335 * 16) + 71)] + (A_shared_dyn_local[(i_2_1_s_335 + 4)] * B_shared_dyn_local[7]));
    }
  }
  for (int i_2_1_s_336 = 0; i_2_1_s_336 < 4; ++i_2_1_s_336) {
    Y_local[((i_2_1_s_336 * 16) + 8)] = (Y_local[((i_2_1_s_336 * 16) + 8)] + (A_shared_dyn_local[i_2_1_s_336] * B_shared_dyn_local[8]));
  }
  for (int i_2_1_s_337 = 0; i_2_1_s_337 < 4; ++i_2_1_s_337) {
    if (i_2_1_s_337 < 2) {
      Y_local[((i_2_1_s_337 * 16) + 72)] = (Y_local[((i_2_1_s_337 * 16) + 72)] + (A_shared_dyn_local[(i_2_1_s_337 + 4)] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_338 = 0; i_2_1_s_338 < 4; ++i_2_1_s_338) {
    Y_local[((i_2_1_s_338 * 16) + 9)] = (Y_local[((i_2_1_s_338 * 16) + 9)] + (A_shared_dyn_local[i_2_1_s_338] * B_shared_dyn_local[9]));
  }
  for (int i_2_1_s_339 = 0; i_2_1_s_339 < 4; ++i_2_1_s_339) {
    if (i_2_1_s_339 < 2) {
      Y_local[((i_2_1_s_339 * 16) + 73)] = (Y_local[((i_2_1_s_339 * 16) + 73)] + (A_shared_dyn_local[(i_2_1_s_339 + 4)] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_340 = 0; i_2_1_s_340 < 4; ++i_2_1_s_340) {
    Y_local[((i_2_1_s_340 * 16) + 10)] = (Y_local[((i_2_1_s_340 * 16) + 10)] + (A_shared_dyn_local[i_2_1_s_340] * B_shared_dyn_local[10]));
  }
  for (int i_2_1_s_341 = 0; i_2_1_s_341 < 4; ++i_2_1_s_341) {
    if (i_2_1_s_341 < 2) {
      Y_local[((i_2_1_s_341 * 16) + 74)] = (Y_local[((i_2_1_s_341 * 16) + 74)] + (A_shared_dyn_local[(i_2_1_s_341 + 4)] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_342 = 0; i_2_1_s_342 < 4; ++i_2_1_s_342) {
    Y_local[((i_2_1_s_342 * 16) + 11)] = (Y_local[((i_2_1_s_342 * 16) + 11)] + (A_shared_dyn_local[i_2_1_s_342] * B_shared_dyn_local[11]));
  }
  for (int i_2_1_s_343 = 0; i_2_1_s_343 < 4; ++i_2_1_s_343) {
    if (i_2_1_s_343 < 2) {
      Y_local[((i_2_1_s_343 * 16) + 75)] = (Y_local[((i_2_1_s_343 * 16) + 75)] + (A_shared_dyn_local[(i_2_1_s_343 + 4)] * B_shared_dyn_local[11]));
    }
  }
  for (int i_2_1_s_344 = 0; i_2_1_s_344 < 4; ++i_2_1_s_344) {
    Y_local[((i_2_1_s_344 * 16) + 12)] = (Y_local[((i_2_1_s_344 * 16) + 12)] + (A_shared_dyn_local[i_2_1_s_344] * B_shared_dyn_local[12]));
  }
  for (int i_2_1_s_345 = 0; i_2_1_s_345 < 4; ++i_2_1_s_345) {
    if (i_2_1_s_345 < 2) {
      Y_local[((i_2_1_s_345 * 16) + 76)] = (Y_local[((i_2_1_s_345 * 16) + 76)] + (A_shared_dyn_local[(i_2_1_s_345 + 4)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_346 = 0; i_2_1_s_346 < 4; ++i_2_1_s_346) {
    Y_local[((i_2_1_s_346 * 16) + 13)] = (Y_local[((i_2_1_s_346 * 16) + 13)] + (A_shared_dyn_local[i_2_1_s_346] * B_shared_dyn_local[13]));
  }
  for (int i_2_1_s_347 = 0; i_2_1_s_347 < 4; ++i_2_1_s_347) {
    if (i_2_1_s_347 < 2) {
      Y_local[((i_2_1_s_347 * 16) + 77)] = (Y_local[((i_2_1_s_347 * 16) + 77)] + (A_shared_dyn_local[(i_2_1_s_347 + 4)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_348 = 0; i_2_1_s_348 < 4; ++i_2_1_s_348) {
    Y_local[((i_2_1_s_348 * 16) + 14)] = (Y_local[((i_2_1_s_348 * 16) + 14)] + (A_shared_dyn_local[i_2_1_s_348] * B_shared_dyn_local[14]));
  }
  for (int i_2_1_s_349 = 0; i_2_1_s_349 < 4; ++i_2_1_s_349) {
    if (i_2_1_s_349 < 2) {
      Y_local[((i_2_1_s_349 * 16) + 78)] = (Y_local[((i_2_1_s_349 * 16) + 78)] + (A_shared_dyn_local[(i_2_1_s_349 + 4)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_350 = 0; i_2_1_s_350 < 4; ++i_2_1_s_350) {
    Y_local[((i_2_1_s_350 * 16) + 15)] = (Y_local[((i_2_1_s_350 * 16) + 15)] + (A_shared_dyn_local[i_2_1_s_350] * B_shared_dyn_local[15]));
  }
  for (int i_2_1_s_351 = 0; i_2_1_s_351 < 4; ++i_2_1_s_351) {
    if (i_2_1_s_351 < 2) {
      Y_local[((i_2_1_s_351 * 16) + 79)] = (Y_local[((i_2_1_s_351 * 16) + 79)] + (A_shared_dyn_local[(i_2_1_s_351 + 4)] * B_shared_dyn_local[15]));
    }
  }
  for (int ax0_0_12 = 0; ax0_0_12 < 2; ++ax0_0_12) {
    for (int ax0_1_s_12 = 0; ax0_1_s_12 < 4; ++ax0_1_s_12) {
      if (((ax0_0_12 * 2) + (ax0_1_s_12 >> 1)) < 3) {
        A_shared_dyn_local[((ax0_0_12 * 4) + ax0_1_s_12)] = ((float*)buf_dyn_shmem)[((((((((int)threadIdx.x) / 27) * 72) + ((((int)threadIdx.x) % 3) * 24)) + (ax0_0_12 * 16)) + (ax0_1_s_12 * 4)) + 576)];
      }
    }
  }
  for (int ax1_0_12 = 0; ax1_0_12 < 4; ++ax1_0_12) {
    *(float4*)(B_shared_dyn_local + (ax1_0_12 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((int)blockIdx.x) & 7) * 144) + (((((int)threadIdx.x) % 27) / 3) * 16)) + (ax1_0_12 * 4)) >> 6) * 64) + ((ax1_0_12 & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 18) + (((((int)threadIdx.x) % 27) / 3) * 2)) + (ax1_0_12 >> 1)) & 7) * 4)) + 3648) - ((((((int)blockIdx.x) & 7) * 144) >> 6) * 64)));
  }
  for (int i_2_1_s_352 = 0; i_2_1_s_352 < 4; ++i_2_1_s_352) {
    Y_local[(i_2_1_s_352 * 16)] = (Y_local[(i_2_1_s_352 * 16)] + (A_shared_dyn_local[(i_2_1_s_352 + 6)] * B_shared_dyn_local[16]));
  }
  for (int i_2_1_s_353 = 0; i_2_1_s_353 < 4; ++i_2_1_s_353) {
    if (i_2_1_s_353 < 2) {
      Y_local[((i_2_1_s_353 * 16) + 64)] = (Y_local[((i_2_1_s_353 * 16) + 64)] + (A_shared_dyn_local[(i_2_1_s_353 + 10)] * B_shared_dyn_local[16]));
    }
  }
  for (int i_2_1_s_354 = 0; i_2_1_s_354 < 4; ++i_2_1_s_354) {
    Y_local[((i_2_1_s_354 * 16) + 1)] = (Y_local[((i_2_1_s_354 * 16) + 1)] + (A_shared_dyn_local[(i_2_1_s_354 + 6)] * B_shared_dyn_local[17]));
  }
  for (int i_2_1_s_355 = 0; i_2_1_s_355 < 4; ++i_2_1_s_355) {
    if (i_2_1_s_355 < 2) {
      Y_local[((i_2_1_s_355 * 16) + 65)] = (Y_local[((i_2_1_s_355 * 16) + 65)] + (A_shared_dyn_local[(i_2_1_s_355 + 10)] * B_shared_dyn_local[17]));
    }
  }
  for (int i_2_1_s_356 = 0; i_2_1_s_356 < 4; ++i_2_1_s_356) {
    Y_local[((i_2_1_s_356 * 16) + 2)] = (Y_local[((i_2_1_s_356 * 16) + 2)] + (A_shared_dyn_local[(i_2_1_s_356 + 6)] * B_shared_dyn_local[18]));
  }
  for (int i_2_1_s_357 = 0; i_2_1_s_357 < 4; ++i_2_1_s_357) {
    if (i_2_1_s_357 < 2) {
      Y_local[((i_2_1_s_357 * 16) + 66)] = (Y_local[((i_2_1_s_357 * 16) + 66)] + (A_shared_dyn_local[(i_2_1_s_357 + 10)] * B_shared_dyn_local[18]));
    }
  }
  for (int i_2_1_s_358 = 0; i_2_1_s_358 < 4; ++i_2_1_s_358) {
    Y_local[((i_2_1_s_358 * 16) + 3)] = (Y_local[((i_2_1_s_358 * 16) + 3)] + (A_shared_dyn_local[(i_2_1_s_358 + 6)] * B_shared_dyn_local[19]));
  }
  for (int i_2_1_s_359 = 0; i_2_1_s_359 < 4; ++i_2_1_s_359) {
    if (i_2_1_s_359 < 2) {
      Y_local[((i_2_1_s_359 * 16) + 67)] = (Y_local[((i_2_1_s_359 * 16) + 67)] + (A_shared_dyn_local[(i_2_1_s_359 + 10)] * B_shared_dyn_local[19]));
    }
  }
  for (int i_2_1_s_360 = 0; i_2_1_s_360 < 4; ++i_2_1_s_360) {
    Y_local[((i_2_1_s_360 * 16) + 4)] = (Y_local[((i_2_1_s_360 * 16) + 4)] + (A_shared_dyn_local[(i_2_1_s_360 + 6)] * B_shared_dyn_local[20]));
  }
  for (int i_2_1_s_361 = 0; i_2_1_s_361 < 4; ++i_2_1_s_361) {
    if (i_2_1_s_361 < 2) {
      Y_local[((i_2_1_s_361 * 16) + 68)] = (Y_local[((i_2_1_s_361 * 16) + 68)] + (A_shared_dyn_local[(i_2_1_s_361 + 10)] * B_shared_dyn_local[20]));
    }
  }
  for (int i_2_1_s_362 = 0; i_2_1_s_362 < 4; ++i_2_1_s_362) {
    Y_local[((i_2_1_s_362 * 16) + 5)] = (Y_local[((i_2_1_s_362 * 16) + 5)] + (A_shared_dyn_local[(i_2_1_s_362 + 6)] * B_shared_dyn_local[21]));
  }
  for (int i_2_1_s_363 = 0; i_2_1_s_363 < 4; ++i_2_1_s_363) {
    if (i_2_1_s_363 < 2) {
      Y_local[((i_2_1_s_363 * 16) + 69)] = (Y_local[((i_2_1_s_363 * 16) + 69)] + (A_shared_dyn_local[(i_2_1_s_363 + 10)] * B_shared_dyn_local[21]));
    }
  }
  for (int i_2_1_s_364 = 0; i_2_1_s_364 < 4; ++i_2_1_s_364) {
    Y_local[((i_2_1_s_364 * 16) + 6)] = (Y_local[((i_2_1_s_364 * 16) + 6)] + (A_shared_dyn_local[(i_2_1_s_364 + 6)] * B_shared_dyn_local[22]));
  }
  for (int i_2_1_s_365 = 0; i_2_1_s_365 < 4; ++i_2_1_s_365) {
    if (i_2_1_s_365 < 2) {
      Y_local[((i_2_1_s_365 * 16) + 70)] = (Y_local[((i_2_1_s_365 * 16) + 70)] + (A_shared_dyn_local[(i_2_1_s_365 + 10)] * B_shared_dyn_local[22]));
    }
  }
  for (int i_2_1_s_366 = 0; i_2_1_s_366 < 4; ++i_2_1_s_366) {
    Y_local[((i_2_1_s_366 * 16) + 7)] = (Y_local[((i_2_1_s_366 * 16) + 7)] + (A_shared_dyn_local[(i_2_1_s_366 + 6)] * B_shared_dyn_local[23]));
  }
  for (int i_2_1_s_367 = 0; i_2_1_s_367 < 4; ++i_2_1_s_367) {
    if (i_2_1_s_367 < 2) {
      Y_local[((i_2_1_s_367 * 16) + 71)] = (Y_local[((i_2_1_s_367 * 16) + 71)] + (A_shared_dyn_local[(i_2_1_s_367 + 10)] * B_shared_dyn_local[23]));
    }
  }
  for (int i_2_1_s_368 = 0; i_2_1_s_368 < 4; ++i_2_1_s_368) {
    Y_local[((i_2_1_s_368 * 16) + 8)] = (Y_local[((i_2_1_s_368 * 16) + 8)] + (A_shared_dyn_local[(i_2_1_s_368 + 6)] * B_shared_dyn_local[24]));
  }
  for (int i_2_1_s_369 = 0; i_2_1_s_369 < 4; ++i_2_1_s_369) {
    if (i_2_1_s_369 < 2) {
      Y_local[((i_2_1_s_369 * 16) + 72)] = (Y_local[((i_2_1_s_369 * 16) + 72)] + (A_shared_dyn_local[(i_2_1_s_369 + 10)] * B_shared_dyn_local[24]));
    }
  }
  for (int i_2_1_s_370 = 0; i_2_1_s_370 < 4; ++i_2_1_s_370) {
    Y_local[((i_2_1_s_370 * 16) + 9)] = (Y_local[((i_2_1_s_370 * 16) + 9)] + (A_shared_dyn_local[(i_2_1_s_370 + 6)] * B_shared_dyn_local[25]));
  }
  for (int i_2_1_s_371 = 0; i_2_1_s_371 < 4; ++i_2_1_s_371) {
    if (i_2_1_s_371 < 2) {
      Y_local[((i_2_1_s_371 * 16) + 73)] = (Y_local[((i_2_1_s_371 * 16) + 73)] + (A_shared_dyn_local[(i_2_1_s_371 + 10)] * B_shared_dyn_local[25]));
    }
  }
  for (int i_2_1_s_372 = 0; i_2_1_s_372 < 4; ++i_2_1_s_372) {
    Y_local[((i_2_1_s_372 * 16) + 10)] = (Y_local[((i_2_1_s_372 * 16) + 10)] + (A_shared_dyn_local[(i_2_1_s_372 + 6)] * B_shared_dyn_local[26]));
  }
  for (int i_2_1_s_373 = 0; i_2_1_s_373 < 4; ++i_2_1_s_373) {
    if (i_2_1_s_373 < 2) {
      Y_local[((i_2_1_s_373 * 16) + 74)] = (Y_local[((i_2_1_s_373 * 16) + 74)] + (A_shared_dyn_local[(i_2_1_s_373 + 10)] * B_shared_dyn_local[26]));
    }
  }
  for (int i_2_1_s_374 = 0; i_2_1_s_374 < 4; ++i_2_1_s_374) {
    Y_local[((i_2_1_s_374 * 16) + 11)] = (Y_local[((i_2_1_s_374 * 16) + 11)] + (A_shared_dyn_local[(i_2_1_s_374 + 6)] * B_shared_dyn_local[27]));
  }
  for (int i_2_1_s_375 = 0; i_2_1_s_375 < 4; ++i_2_1_s_375) {
    if (i_2_1_s_375 < 2) {
      Y_local[((i_2_1_s_375 * 16) + 75)] = (Y_local[((i_2_1_s_375 * 16) + 75)] + (A_shared_dyn_local[(i_2_1_s_375 + 10)] * B_shared_dyn_local[27]));
    }
  }
  for (int i_2_1_s_376 = 0; i_2_1_s_376 < 4; ++i_2_1_s_376) {
    Y_local[((i_2_1_s_376 * 16) + 12)] = (Y_local[((i_2_1_s_376 * 16) + 12)] + (A_shared_dyn_local[(i_2_1_s_376 + 6)] * B_shared_dyn_local[28]));
  }
  for (int i_2_1_s_377 = 0; i_2_1_s_377 < 4; ++i_2_1_s_377) {
    if (i_2_1_s_377 < 2) {
      Y_local[((i_2_1_s_377 * 16) + 76)] = (Y_local[((i_2_1_s_377 * 16) + 76)] + (A_shared_dyn_local[(i_2_1_s_377 + 10)] * B_shared_dyn_local[28]));
    }
  }
  for (int i_2_1_s_378 = 0; i_2_1_s_378 < 4; ++i_2_1_s_378) {
    Y_local[((i_2_1_s_378 * 16) + 13)] = (Y_local[((i_2_1_s_378 * 16) + 13)] + (A_shared_dyn_local[(i_2_1_s_378 + 6)] * B_shared_dyn_local[29]));
  }
  for (int i_2_1_s_379 = 0; i_2_1_s_379 < 4; ++i_2_1_s_379) {
    if (i_2_1_s_379 < 2) {
      Y_local[((i_2_1_s_379 * 16) + 77)] = (Y_local[((i_2_1_s_379 * 16) + 77)] + (A_shared_dyn_local[(i_2_1_s_379 + 10)] * B_shared_dyn_local[29]));
    }
  }
  for (int i_2_1_s_380 = 0; i_2_1_s_380 < 4; ++i_2_1_s_380) {
    Y_local[((i_2_1_s_380 * 16) + 14)] = (Y_local[((i_2_1_s_380 * 16) + 14)] + (A_shared_dyn_local[(i_2_1_s_380 + 6)] * B_shared_dyn_local[30]));
  }
  for (int i_2_1_s_381 = 0; i_2_1_s_381 < 4; ++i_2_1_s_381) {
    if (i_2_1_s_381 < 2) {
      Y_local[((i_2_1_s_381 * 16) + 78)] = (Y_local[((i_2_1_s_381 * 16) + 78)] + (A_shared_dyn_local[(i_2_1_s_381 + 10)] * B_shared_dyn_local[30]));
    }
  }
  for (int i_2_1_s_382 = 0; i_2_1_s_382 < 4; ++i_2_1_s_382) {
    Y_local[((i_2_1_s_382 * 16) + 15)] = (Y_local[((i_2_1_s_382 * 16) + 15)] + (A_shared_dyn_local[(i_2_1_s_382 + 6)] * B_shared_dyn_local[31]));
  }
  for (int i_2_1_s_383 = 0; i_2_1_s_383 < 4; ++i_2_1_s_383) {
    if (i_2_1_s_383 < 2) {
      Y_local[((i_2_1_s_383 * 16) + 79)] = (Y_local[((i_2_1_s_383 * 16) + 79)] + (A_shared_dyn_local[(i_2_1_s_383 + 10)] * B_shared_dyn_local[31]));
    }
  }
__asm__ __volatile__("cp.async.wait_group 0;");

  __syncthreads();
  for (int ax0_0_13 = 0; ax0_0_13 < 2; ++ax0_0_13) {
    for (int ax0_1_s_13 = 0; ax0_1_s_13 < 4; ++ax0_1_s_13) {
      if (((ax0_0_13 * 2) + (ax0_1_s_13 >> 1)) < 3) {
        A_shared_dyn_local[(((ax0_0_13 * 4) + ax0_1_s_13) + 6)] = ((float*)buf_dyn_shmem)[((((((((int)threadIdx.x) / 27) * 72) + ((((int)threadIdx.x) % 3) * 24)) + (ax0_0_13 * 16)) + (ax0_1_s_13 * 4)) + 577)];
      }
    }
  }
  for (int ax1_0_13 = 0; ax1_0_13 < 4; ++ax1_0_13) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_13 * 4) + 16)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((int)blockIdx.x) & 7) * 144) + (((((int)threadIdx.x) % 27) / 3) * 16)) + (ax1_0_13 * 4)) >> 6) * 64) + ((ax1_0_13 & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 18) + (((((int)threadIdx.x) % 27) / 3) * 2)) + (ax1_0_13 >> 1)) & 7) * 4)) + 3840) - ((((((int)blockIdx.x) & 7) * 144) >> 6) * 64)));
  }
  for (int i_2_1_s_384 = 0; i_2_1_s_384 < 4; ++i_2_1_s_384) {
    Y_local[(i_2_1_s_384 * 16)] = (Y_local[(i_2_1_s_384 * 16)] + (A_shared_dyn_local[i_2_1_s_384] * B_shared_dyn_local[0]));
  }
  for (int i_2_1_s_385 = 0; i_2_1_s_385 < 4; ++i_2_1_s_385) {
    if (i_2_1_s_385 < 2) {
      Y_local[((i_2_1_s_385 * 16) + 64)] = (Y_local[((i_2_1_s_385 * 16) + 64)] + (A_shared_dyn_local[(i_2_1_s_385 + 4)] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_386 = 0; i_2_1_s_386 < 4; ++i_2_1_s_386) {
    Y_local[((i_2_1_s_386 * 16) + 1)] = (Y_local[((i_2_1_s_386 * 16) + 1)] + (A_shared_dyn_local[i_2_1_s_386] * B_shared_dyn_local[1]));
  }
  for (int i_2_1_s_387 = 0; i_2_1_s_387 < 4; ++i_2_1_s_387) {
    if (i_2_1_s_387 < 2) {
      Y_local[((i_2_1_s_387 * 16) + 65)] = (Y_local[((i_2_1_s_387 * 16) + 65)] + (A_shared_dyn_local[(i_2_1_s_387 + 4)] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_388 = 0; i_2_1_s_388 < 4; ++i_2_1_s_388) {
    Y_local[((i_2_1_s_388 * 16) + 2)] = (Y_local[((i_2_1_s_388 * 16) + 2)] + (A_shared_dyn_local[i_2_1_s_388] * B_shared_dyn_local[2]));
  }
  for (int i_2_1_s_389 = 0; i_2_1_s_389 < 4; ++i_2_1_s_389) {
    if (i_2_1_s_389 < 2) {
      Y_local[((i_2_1_s_389 * 16) + 66)] = (Y_local[((i_2_1_s_389 * 16) + 66)] + (A_shared_dyn_local[(i_2_1_s_389 + 4)] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_390 = 0; i_2_1_s_390 < 4; ++i_2_1_s_390) {
    Y_local[((i_2_1_s_390 * 16) + 3)] = (Y_local[((i_2_1_s_390 * 16) + 3)] + (A_shared_dyn_local[i_2_1_s_390] * B_shared_dyn_local[3]));
  }
  for (int i_2_1_s_391 = 0; i_2_1_s_391 < 4; ++i_2_1_s_391) {
    if (i_2_1_s_391 < 2) {
      Y_local[((i_2_1_s_391 * 16) + 67)] = (Y_local[((i_2_1_s_391 * 16) + 67)] + (A_shared_dyn_local[(i_2_1_s_391 + 4)] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_392 = 0; i_2_1_s_392 < 4; ++i_2_1_s_392) {
    Y_local[((i_2_1_s_392 * 16) + 4)] = (Y_local[((i_2_1_s_392 * 16) + 4)] + (A_shared_dyn_local[i_2_1_s_392] * B_shared_dyn_local[4]));
  }
  for (int i_2_1_s_393 = 0; i_2_1_s_393 < 4; ++i_2_1_s_393) {
    if (i_2_1_s_393 < 2) {
      Y_local[((i_2_1_s_393 * 16) + 68)] = (Y_local[((i_2_1_s_393 * 16) + 68)] + (A_shared_dyn_local[(i_2_1_s_393 + 4)] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_394 = 0; i_2_1_s_394 < 4; ++i_2_1_s_394) {
    Y_local[((i_2_1_s_394 * 16) + 5)] = (Y_local[((i_2_1_s_394 * 16) + 5)] + (A_shared_dyn_local[i_2_1_s_394] * B_shared_dyn_local[5]));
  }
  for (int i_2_1_s_395 = 0; i_2_1_s_395 < 4; ++i_2_1_s_395) {
    if (i_2_1_s_395 < 2) {
      Y_local[((i_2_1_s_395 * 16) + 69)] = (Y_local[((i_2_1_s_395 * 16) + 69)] + (A_shared_dyn_local[(i_2_1_s_395 + 4)] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_396 = 0; i_2_1_s_396 < 4; ++i_2_1_s_396) {
    Y_local[((i_2_1_s_396 * 16) + 6)] = (Y_local[((i_2_1_s_396 * 16) + 6)] + (A_shared_dyn_local[i_2_1_s_396] * B_shared_dyn_local[6]));
  }
  for (int i_2_1_s_397 = 0; i_2_1_s_397 < 4; ++i_2_1_s_397) {
    if (i_2_1_s_397 < 2) {
      Y_local[((i_2_1_s_397 * 16) + 70)] = (Y_local[((i_2_1_s_397 * 16) + 70)] + (A_shared_dyn_local[(i_2_1_s_397 + 4)] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_398 = 0; i_2_1_s_398 < 4; ++i_2_1_s_398) {
    Y_local[((i_2_1_s_398 * 16) + 7)] = (Y_local[((i_2_1_s_398 * 16) + 7)] + (A_shared_dyn_local[i_2_1_s_398] * B_shared_dyn_local[7]));
  }
  for (int i_2_1_s_399 = 0; i_2_1_s_399 < 4; ++i_2_1_s_399) {
    if (i_2_1_s_399 < 2) {
      Y_local[((i_2_1_s_399 * 16) + 71)] = (Y_local[((i_2_1_s_399 * 16) + 71)] + (A_shared_dyn_local[(i_2_1_s_399 + 4)] * B_shared_dyn_local[7]));
    }
  }
  for (int i_2_1_s_400 = 0; i_2_1_s_400 < 4; ++i_2_1_s_400) {
    Y_local[((i_2_1_s_400 * 16) + 8)] = (Y_local[((i_2_1_s_400 * 16) + 8)] + (A_shared_dyn_local[i_2_1_s_400] * B_shared_dyn_local[8]));
  }
  for (int i_2_1_s_401 = 0; i_2_1_s_401 < 4; ++i_2_1_s_401) {
    if (i_2_1_s_401 < 2) {
      Y_local[((i_2_1_s_401 * 16) + 72)] = (Y_local[((i_2_1_s_401 * 16) + 72)] + (A_shared_dyn_local[(i_2_1_s_401 + 4)] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_402 = 0; i_2_1_s_402 < 4; ++i_2_1_s_402) {
    Y_local[((i_2_1_s_402 * 16) + 9)] = (Y_local[((i_2_1_s_402 * 16) + 9)] + (A_shared_dyn_local[i_2_1_s_402] * B_shared_dyn_local[9]));
  }
  for (int i_2_1_s_403 = 0; i_2_1_s_403 < 4; ++i_2_1_s_403) {
    if (i_2_1_s_403 < 2) {
      Y_local[((i_2_1_s_403 * 16) + 73)] = (Y_local[((i_2_1_s_403 * 16) + 73)] + (A_shared_dyn_local[(i_2_1_s_403 + 4)] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_404 = 0; i_2_1_s_404 < 4; ++i_2_1_s_404) {
    Y_local[((i_2_1_s_404 * 16) + 10)] = (Y_local[((i_2_1_s_404 * 16) + 10)] + (A_shared_dyn_local[i_2_1_s_404] * B_shared_dyn_local[10]));
  }
  for (int i_2_1_s_405 = 0; i_2_1_s_405 < 4; ++i_2_1_s_405) {
    if (i_2_1_s_405 < 2) {
      Y_local[((i_2_1_s_405 * 16) + 74)] = (Y_local[((i_2_1_s_405 * 16) + 74)] + (A_shared_dyn_local[(i_2_1_s_405 + 4)] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_406 = 0; i_2_1_s_406 < 4; ++i_2_1_s_406) {
    Y_local[((i_2_1_s_406 * 16) + 11)] = (Y_local[((i_2_1_s_406 * 16) + 11)] + (A_shared_dyn_local[i_2_1_s_406] * B_shared_dyn_local[11]));
  }
  for (int i_2_1_s_407 = 0; i_2_1_s_407 < 4; ++i_2_1_s_407) {
    if (i_2_1_s_407 < 2) {
      Y_local[((i_2_1_s_407 * 16) + 75)] = (Y_local[((i_2_1_s_407 * 16) + 75)] + (A_shared_dyn_local[(i_2_1_s_407 + 4)] * B_shared_dyn_local[11]));
    }
  }
  for (int i_2_1_s_408 = 0; i_2_1_s_408 < 4; ++i_2_1_s_408) {
    Y_local[((i_2_1_s_408 * 16) + 12)] = (Y_local[((i_2_1_s_408 * 16) + 12)] + (A_shared_dyn_local[i_2_1_s_408] * B_shared_dyn_local[12]));
  }
  for (int i_2_1_s_409 = 0; i_2_1_s_409 < 4; ++i_2_1_s_409) {
    if (i_2_1_s_409 < 2) {
      Y_local[((i_2_1_s_409 * 16) + 76)] = (Y_local[((i_2_1_s_409 * 16) + 76)] + (A_shared_dyn_local[(i_2_1_s_409 + 4)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_410 = 0; i_2_1_s_410 < 4; ++i_2_1_s_410) {
    Y_local[((i_2_1_s_410 * 16) + 13)] = (Y_local[((i_2_1_s_410 * 16) + 13)] + (A_shared_dyn_local[i_2_1_s_410] * B_shared_dyn_local[13]));
  }
  for (int i_2_1_s_411 = 0; i_2_1_s_411 < 4; ++i_2_1_s_411) {
    if (i_2_1_s_411 < 2) {
      Y_local[((i_2_1_s_411 * 16) + 77)] = (Y_local[((i_2_1_s_411 * 16) + 77)] + (A_shared_dyn_local[(i_2_1_s_411 + 4)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_412 = 0; i_2_1_s_412 < 4; ++i_2_1_s_412) {
    Y_local[((i_2_1_s_412 * 16) + 14)] = (Y_local[((i_2_1_s_412 * 16) + 14)] + (A_shared_dyn_local[i_2_1_s_412] * B_shared_dyn_local[14]));
  }
  for (int i_2_1_s_413 = 0; i_2_1_s_413 < 4; ++i_2_1_s_413) {
    if (i_2_1_s_413 < 2) {
      Y_local[((i_2_1_s_413 * 16) + 78)] = (Y_local[((i_2_1_s_413 * 16) + 78)] + (A_shared_dyn_local[(i_2_1_s_413 + 4)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_414 = 0; i_2_1_s_414 < 4; ++i_2_1_s_414) {
    Y_local[((i_2_1_s_414 * 16) + 15)] = (Y_local[((i_2_1_s_414 * 16) + 15)] + (A_shared_dyn_local[i_2_1_s_414] * B_shared_dyn_local[15]));
  }
  for (int i_2_1_s_415 = 0; i_2_1_s_415 < 4; ++i_2_1_s_415) {
    if (i_2_1_s_415 < 2) {
      Y_local[((i_2_1_s_415 * 16) + 79)] = (Y_local[((i_2_1_s_415 * 16) + 79)] + (A_shared_dyn_local[(i_2_1_s_415 + 4)] * B_shared_dyn_local[15]));
    }
  }
  for (int ax0_0_14 = 0; ax0_0_14 < 2; ++ax0_0_14) {
    for (int ax0_1_s_14 = 0; ax0_1_s_14 < 4; ++ax0_1_s_14) {
      if (((ax0_0_14 * 2) + (ax0_1_s_14 >> 1)) < 3) {
        A_shared_dyn_local[((ax0_0_14 * 4) + ax0_1_s_14)] = ((float*)buf_dyn_shmem)[((((((((int)threadIdx.x) / 27) * 72) + ((((int)threadIdx.x) % 3) * 24)) + (ax0_0_14 * 16)) + (ax0_1_s_14 * 4)) + 578)];
      }
    }
  }
  for (int ax1_0_14 = 0; ax1_0_14 < 4; ++ax1_0_14) {
    *(float4*)(B_shared_dyn_local + (ax1_0_14 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((int)blockIdx.x) & 7) * 144) + (((((int)threadIdx.x) % 27) / 3) * 16)) + (ax1_0_14 * 4)) >> 6) * 64) + ((ax1_0_14 & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 18) + (((((int)threadIdx.x) % 27) / 3) * 2)) + (ax1_0_14 >> 1)) & 7) * 4)) + 4032) - ((((((int)blockIdx.x) & 7) * 144) >> 6) * 64)));
  }
  for (int i_2_1_s_416 = 0; i_2_1_s_416 < 4; ++i_2_1_s_416) {
    Y_local[(i_2_1_s_416 * 16)] = (Y_local[(i_2_1_s_416 * 16)] + (A_shared_dyn_local[(i_2_1_s_416 + 6)] * B_shared_dyn_local[16]));
  }
  for (int i_2_1_s_417 = 0; i_2_1_s_417 < 4; ++i_2_1_s_417) {
    if (i_2_1_s_417 < 2) {
      Y_local[((i_2_1_s_417 * 16) + 64)] = (Y_local[((i_2_1_s_417 * 16) + 64)] + (A_shared_dyn_local[(i_2_1_s_417 + 10)] * B_shared_dyn_local[16]));
    }
  }
  for (int i_2_1_s_418 = 0; i_2_1_s_418 < 4; ++i_2_1_s_418) {
    Y_local[((i_2_1_s_418 * 16) + 1)] = (Y_local[((i_2_1_s_418 * 16) + 1)] + (A_shared_dyn_local[(i_2_1_s_418 + 6)] * B_shared_dyn_local[17]));
  }
  for (int i_2_1_s_419 = 0; i_2_1_s_419 < 4; ++i_2_1_s_419) {
    if (i_2_1_s_419 < 2) {
      Y_local[((i_2_1_s_419 * 16) + 65)] = (Y_local[((i_2_1_s_419 * 16) + 65)] + (A_shared_dyn_local[(i_2_1_s_419 + 10)] * B_shared_dyn_local[17]));
    }
  }
  for (int i_2_1_s_420 = 0; i_2_1_s_420 < 4; ++i_2_1_s_420) {
    Y_local[((i_2_1_s_420 * 16) + 2)] = (Y_local[((i_2_1_s_420 * 16) + 2)] + (A_shared_dyn_local[(i_2_1_s_420 + 6)] * B_shared_dyn_local[18]));
  }
  for (int i_2_1_s_421 = 0; i_2_1_s_421 < 4; ++i_2_1_s_421) {
    if (i_2_1_s_421 < 2) {
      Y_local[((i_2_1_s_421 * 16) + 66)] = (Y_local[((i_2_1_s_421 * 16) + 66)] + (A_shared_dyn_local[(i_2_1_s_421 + 10)] * B_shared_dyn_local[18]));
    }
  }
  for (int i_2_1_s_422 = 0; i_2_1_s_422 < 4; ++i_2_1_s_422) {
    Y_local[((i_2_1_s_422 * 16) + 3)] = (Y_local[((i_2_1_s_422 * 16) + 3)] + (A_shared_dyn_local[(i_2_1_s_422 + 6)] * B_shared_dyn_local[19]));
  }
  for (int i_2_1_s_423 = 0; i_2_1_s_423 < 4; ++i_2_1_s_423) {
    if (i_2_1_s_423 < 2) {
      Y_local[((i_2_1_s_423 * 16) + 67)] = (Y_local[((i_2_1_s_423 * 16) + 67)] + (A_shared_dyn_local[(i_2_1_s_423 + 10)] * B_shared_dyn_local[19]));
    }
  }
  for (int i_2_1_s_424 = 0; i_2_1_s_424 < 4; ++i_2_1_s_424) {
    Y_local[((i_2_1_s_424 * 16) + 4)] = (Y_local[((i_2_1_s_424 * 16) + 4)] + (A_shared_dyn_local[(i_2_1_s_424 + 6)] * B_shared_dyn_local[20]));
  }
  for (int i_2_1_s_425 = 0; i_2_1_s_425 < 4; ++i_2_1_s_425) {
    if (i_2_1_s_425 < 2) {
      Y_local[((i_2_1_s_425 * 16) + 68)] = (Y_local[((i_2_1_s_425 * 16) + 68)] + (A_shared_dyn_local[(i_2_1_s_425 + 10)] * B_shared_dyn_local[20]));
    }
  }
  for (int i_2_1_s_426 = 0; i_2_1_s_426 < 4; ++i_2_1_s_426) {
    Y_local[((i_2_1_s_426 * 16) + 5)] = (Y_local[((i_2_1_s_426 * 16) + 5)] + (A_shared_dyn_local[(i_2_1_s_426 + 6)] * B_shared_dyn_local[21]));
  }
  for (int i_2_1_s_427 = 0; i_2_1_s_427 < 4; ++i_2_1_s_427) {
    if (i_2_1_s_427 < 2) {
      Y_local[((i_2_1_s_427 * 16) + 69)] = (Y_local[((i_2_1_s_427 * 16) + 69)] + (A_shared_dyn_local[(i_2_1_s_427 + 10)] * B_shared_dyn_local[21]));
    }
  }
  for (int i_2_1_s_428 = 0; i_2_1_s_428 < 4; ++i_2_1_s_428) {
    Y_local[((i_2_1_s_428 * 16) + 6)] = (Y_local[((i_2_1_s_428 * 16) + 6)] + (A_shared_dyn_local[(i_2_1_s_428 + 6)] * B_shared_dyn_local[22]));
  }
  for (int i_2_1_s_429 = 0; i_2_1_s_429 < 4; ++i_2_1_s_429) {
    if (i_2_1_s_429 < 2) {
      Y_local[((i_2_1_s_429 * 16) + 70)] = (Y_local[((i_2_1_s_429 * 16) + 70)] + (A_shared_dyn_local[(i_2_1_s_429 + 10)] * B_shared_dyn_local[22]));
    }
  }
  for (int i_2_1_s_430 = 0; i_2_1_s_430 < 4; ++i_2_1_s_430) {
    Y_local[((i_2_1_s_430 * 16) + 7)] = (Y_local[((i_2_1_s_430 * 16) + 7)] + (A_shared_dyn_local[(i_2_1_s_430 + 6)] * B_shared_dyn_local[23]));
  }
  for (int i_2_1_s_431 = 0; i_2_1_s_431 < 4; ++i_2_1_s_431) {
    if (i_2_1_s_431 < 2) {
      Y_local[((i_2_1_s_431 * 16) + 71)] = (Y_local[((i_2_1_s_431 * 16) + 71)] + (A_shared_dyn_local[(i_2_1_s_431 + 10)] * B_shared_dyn_local[23]));
    }
  }
  for (int i_2_1_s_432 = 0; i_2_1_s_432 < 4; ++i_2_1_s_432) {
    Y_local[((i_2_1_s_432 * 16) + 8)] = (Y_local[((i_2_1_s_432 * 16) + 8)] + (A_shared_dyn_local[(i_2_1_s_432 + 6)] * B_shared_dyn_local[24]));
  }
  for (int i_2_1_s_433 = 0; i_2_1_s_433 < 4; ++i_2_1_s_433) {
    if (i_2_1_s_433 < 2) {
      Y_local[((i_2_1_s_433 * 16) + 72)] = (Y_local[((i_2_1_s_433 * 16) + 72)] + (A_shared_dyn_local[(i_2_1_s_433 + 10)] * B_shared_dyn_local[24]));
    }
  }
  for (int i_2_1_s_434 = 0; i_2_1_s_434 < 4; ++i_2_1_s_434) {
    Y_local[((i_2_1_s_434 * 16) + 9)] = (Y_local[((i_2_1_s_434 * 16) + 9)] + (A_shared_dyn_local[(i_2_1_s_434 + 6)] * B_shared_dyn_local[25]));
  }
  for (int i_2_1_s_435 = 0; i_2_1_s_435 < 4; ++i_2_1_s_435) {
    if (i_2_1_s_435 < 2) {
      Y_local[((i_2_1_s_435 * 16) + 73)] = (Y_local[((i_2_1_s_435 * 16) + 73)] + (A_shared_dyn_local[(i_2_1_s_435 + 10)] * B_shared_dyn_local[25]));
    }
  }
  for (int i_2_1_s_436 = 0; i_2_1_s_436 < 4; ++i_2_1_s_436) {
    Y_local[((i_2_1_s_436 * 16) + 10)] = (Y_local[((i_2_1_s_436 * 16) + 10)] + (A_shared_dyn_local[(i_2_1_s_436 + 6)] * B_shared_dyn_local[26]));
  }
  for (int i_2_1_s_437 = 0; i_2_1_s_437 < 4; ++i_2_1_s_437) {
    if (i_2_1_s_437 < 2) {
      Y_local[((i_2_1_s_437 * 16) + 74)] = (Y_local[((i_2_1_s_437 * 16) + 74)] + (A_shared_dyn_local[(i_2_1_s_437 + 10)] * B_shared_dyn_local[26]));
    }
  }
  for (int i_2_1_s_438 = 0; i_2_1_s_438 < 4; ++i_2_1_s_438) {
    Y_local[((i_2_1_s_438 * 16) + 11)] = (Y_local[((i_2_1_s_438 * 16) + 11)] + (A_shared_dyn_local[(i_2_1_s_438 + 6)] * B_shared_dyn_local[27]));
  }
  for (int i_2_1_s_439 = 0; i_2_1_s_439 < 4; ++i_2_1_s_439) {
    if (i_2_1_s_439 < 2) {
      Y_local[((i_2_1_s_439 * 16) + 75)] = (Y_local[((i_2_1_s_439 * 16) + 75)] + (A_shared_dyn_local[(i_2_1_s_439 + 10)] * B_shared_dyn_local[27]));
    }
  }
  for (int i_2_1_s_440 = 0; i_2_1_s_440 < 4; ++i_2_1_s_440) {
    Y_local[((i_2_1_s_440 * 16) + 12)] = (Y_local[((i_2_1_s_440 * 16) + 12)] + (A_shared_dyn_local[(i_2_1_s_440 + 6)] * B_shared_dyn_local[28]));
  }
  for (int i_2_1_s_441 = 0; i_2_1_s_441 < 4; ++i_2_1_s_441) {
    if (i_2_1_s_441 < 2) {
      Y_local[((i_2_1_s_441 * 16) + 76)] = (Y_local[((i_2_1_s_441 * 16) + 76)] + (A_shared_dyn_local[(i_2_1_s_441 + 10)] * B_shared_dyn_local[28]));
    }
  }
  for (int i_2_1_s_442 = 0; i_2_1_s_442 < 4; ++i_2_1_s_442) {
    Y_local[((i_2_1_s_442 * 16) + 13)] = (Y_local[((i_2_1_s_442 * 16) + 13)] + (A_shared_dyn_local[(i_2_1_s_442 + 6)] * B_shared_dyn_local[29]));
  }
  for (int i_2_1_s_443 = 0; i_2_1_s_443 < 4; ++i_2_1_s_443) {
    if (i_2_1_s_443 < 2) {
      Y_local[((i_2_1_s_443 * 16) + 77)] = (Y_local[((i_2_1_s_443 * 16) + 77)] + (A_shared_dyn_local[(i_2_1_s_443 + 10)] * B_shared_dyn_local[29]));
    }
  }
  for (int i_2_1_s_444 = 0; i_2_1_s_444 < 4; ++i_2_1_s_444) {
    Y_local[((i_2_1_s_444 * 16) + 14)] = (Y_local[((i_2_1_s_444 * 16) + 14)] + (A_shared_dyn_local[(i_2_1_s_444 + 6)] * B_shared_dyn_local[30]));
  }
  for (int i_2_1_s_445 = 0; i_2_1_s_445 < 4; ++i_2_1_s_445) {
    if (i_2_1_s_445 < 2) {
      Y_local[((i_2_1_s_445 * 16) + 78)] = (Y_local[((i_2_1_s_445 * 16) + 78)] + (A_shared_dyn_local[(i_2_1_s_445 + 10)] * B_shared_dyn_local[30]));
    }
  }
  for (int i_2_1_s_446 = 0; i_2_1_s_446 < 4; ++i_2_1_s_446) {
    Y_local[((i_2_1_s_446 * 16) + 15)] = (Y_local[((i_2_1_s_446 * 16) + 15)] + (A_shared_dyn_local[(i_2_1_s_446 + 6)] * B_shared_dyn_local[31]));
  }
  for (int i_2_1_s_447 = 0; i_2_1_s_447 < 4; ++i_2_1_s_447) {
    if (i_2_1_s_447 < 2) {
      Y_local[((i_2_1_s_447 * 16) + 79)] = (Y_local[((i_2_1_s_447 * 16) + 79)] + (A_shared_dyn_local[(i_2_1_s_447 + 10)] * B_shared_dyn_local[31]));
    }
  }
  for (int ax0_0_15 = 0; ax0_0_15 < 2; ++ax0_0_15) {
    for (int ax0_1_s_15 = 0; ax0_1_s_15 < 4; ++ax0_1_s_15) {
      if (((ax0_0_15 * 2) + (ax0_1_s_15 >> 1)) < 3) {
        A_shared_dyn_local[(((ax0_0_15 * 4) + ax0_1_s_15) + 6)] = ((float*)buf_dyn_shmem)[((((((((int)threadIdx.x) / 27) * 72) + ((((int)threadIdx.x) % 3) * 24)) + (ax0_0_15 * 16)) + (ax0_1_s_15 * 4)) + 579)];
      }
    }
  }
  for (int ax1_0_15 = 0; ax1_0_15 < 4; ++ax1_0_15) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_15 * 4) + 16)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((int)blockIdx.x) & 7) * 144) + (((((int)threadIdx.x) % 27) / 3) * 16)) + (ax1_0_15 * 4)) >> 6) * 64) + ((ax1_0_15 & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 18) + (((((int)threadIdx.x) % 27) / 3) * 2)) + (ax1_0_15 >> 1)) & 7) * 4)) + 4224) - ((((((int)blockIdx.x) & 7) * 144) >> 6) * 64)));
  }
  for (int i_2_1_s_448 = 0; i_2_1_s_448 < 4; ++i_2_1_s_448) {
    Y_local[(i_2_1_s_448 * 16)] = (Y_local[(i_2_1_s_448 * 16)] + (A_shared_dyn_local[i_2_1_s_448] * B_shared_dyn_local[0]));
  }
  for (int i_2_1_s_449 = 0; i_2_1_s_449 < 4; ++i_2_1_s_449) {
    if (i_2_1_s_449 < 2) {
      Y_local[((i_2_1_s_449 * 16) + 64)] = (Y_local[((i_2_1_s_449 * 16) + 64)] + (A_shared_dyn_local[(i_2_1_s_449 + 4)] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_450 = 0; i_2_1_s_450 < 4; ++i_2_1_s_450) {
    Y_local[((i_2_1_s_450 * 16) + 1)] = (Y_local[((i_2_1_s_450 * 16) + 1)] + (A_shared_dyn_local[i_2_1_s_450] * B_shared_dyn_local[1]));
  }
  for (int i_2_1_s_451 = 0; i_2_1_s_451 < 4; ++i_2_1_s_451) {
    if (i_2_1_s_451 < 2) {
      Y_local[((i_2_1_s_451 * 16) + 65)] = (Y_local[((i_2_1_s_451 * 16) + 65)] + (A_shared_dyn_local[(i_2_1_s_451 + 4)] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_452 = 0; i_2_1_s_452 < 4; ++i_2_1_s_452) {
    Y_local[((i_2_1_s_452 * 16) + 2)] = (Y_local[((i_2_1_s_452 * 16) + 2)] + (A_shared_dyn_local[i_2_1_s_452] * B_shared_dyn_local[2]));
  }
  for (int i_2_1_s_453 = 0; i_2_1_s_453 < 4; ++i_2_1_s_453) {
    if (i_2_1_s_453 < 2) {
      Y_local[((i_2_1_s_453 * 16) + 66)] = (Y_local[((i_2_1_s_453 * 16) + 66)] + (A_shared_dyn_local[(i_2_1_s_453 + 4)] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_454 = 0; i_2_1_s_454 < 4; ++i_2_1_s_454) {
    Y_local[((i_2_1_s_454 * 16) + 3)] = (Y_local[((i_2_1_s_454 * 16) + 3)] + (A_shared_dyn_local[i_2_1_s_454] * B_shared_dyn_local[3]));
  }
  for (int i_2_1_s_455 = 0; i_2_1_s_455 < 4; ++i_2_1_s_455) {
    if (i_2_1_s_455 < 2) {
      Y_local[((i_2_1_s_455 * 16) + 67)] = (Y_local[((i_2_1_s_455 * 16) + 67)] + (A_shared_dyn_local[(i_2_1_s_455 + 4)] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_456 = 0; i_2_1_s_456 < 4; ++i_2_1_s_456) {
    Y_local[((i_2_1_s_456 * 16) + 4)] = (Y_local[((i_2_1_s_456 * 16) + 4)] + (A_shared_dyn_local[i_2_1_s_456] * B_shared_dyn_local[4]));
  }
  for (int i_2_1_s_457 = 0; i_2_1_s_457 < 4; ++i_2_1_s_457) {
    if (i_2_1_s_457 < 2) {
      Y_local[((i_2_1_s_457 * 16) + 68)] = (Y_local[((i_2_1_s_457 * 16) + 68)] + (A_shared_dyn_local[(i_2_1_s_457 + 4)] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_458 = 0; i_2_1_s_458 < 4; ++i_2_1_s_458) {
    Y_local[((i_2_1_s_458 * 16) + 5)] = (Y_local[((i_2_1_s_458 * 16) + 5)] + (A_shared_dyn_local[i_2_1_s_458] * B_shared_dyn_local[5]));
  }
  for (int i_2_1_s_459 = 0; i_2_1_s_459 < 4; ++i_2_1_s_459) {
    if (i_2_1_s_459 < 2) {
      Y_local[((i_2_1_s_459 * 16) + 69)] = (Y_local[((i_2_1_s_459 * 16) + 69)] + (A_shared_dyn_local[(i_2_1_s_459 + 4)] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_460 = 0; i_2_1_s_460 < 4; ++i_2_1_s_460) {
    Y_local[((i_2_1_s_460 * 16) + 6)] = (Y_local[((i_2_1_s_460 * 16) + 6)] + (A_shared_dyn_local[i_2_1_s_460] * B_shared_dyn_local[6]));
  }
  for (int i_2_1_s_461 = 0; i_2_1_s_461 < 4; ++i_2_1_s_461) {
    if (i_2_1_s_461 < 2) {
      Y_local[((i_2_1_s_461 * 16) + 70)] = (Y_local[((i_2_1_s_461 * 16) + 70)] + (A_shared_dyn_local[(i_2_1_s_461 + 4)] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_462 = 0; i_2_1_s_462 < 4; ++i_2_1_s_462) {
    Y_local[((i_2_1_s_462 * 16) + 7)] = (Y_local[((i_2_1_s_462 * 16) + 7)] + (A_shared_dyn_local[i_2_1_s_462] * B_shared_dyn_local[7]));
  }
  for (int i_2_1_s_463 = 0; i_2_1_s_463 < 4; ++i_2_1_s_463) {
    if (i_2_1_s_463 < 2) {
      Y_local[((i_2_1_s_463 * 16) + 71)] = (Y_local[((i_2_1_s_463 * 16) + 71)] + (A_shared_dyn_local[(i_2_1_s_463 + 4)] * B_shared_dyn_local[7]));
    }
  }
  for (int i_2_1_s_464 = 0; i_2_1_s_464 < 4; ++i_2_1_s_464) {
    Y_local[((i_2_1_s_464 * 16) + 8)] = (Y_local[((i_2_1_s_464 * 16) + 8)] + (A_shared_dyn_local[i_2_1_s_464] * B_shared_dyn_local[8]));
  }
  for (int i_2_1_s_465 = 0; i_2_1_s_465 < 4; ++i_2_1_s_465) {
    if (i_2_1_s_465 < 2) {
      Y_local[((i_2_1_s_465 * 16) + 72)] = (Y_local[((i_2_1_s_465 * 16) + 72)] + (A_shared_dyn_local[(i_2_1_s_465 + 4)] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_466 = 0; i_2_1_s_466 < 4; ++i_2_1_s_466) {
    Y_local[((i_2_1_s_466 * 16) + 9)] = (Y_local[((i_2_1_s_466 * 16) + 9)] + (A_shared_dyn_local[i_2_1_s_466] * B_shared_dyn_local[9]));
  }
  for (int i_2_1_s_467 = 0; i_2_1_s_467 < 4; ++i_2_1_s_467) {
    if (i_2_1_s_467 < 2) {
      Y_local[((i_2_1_s_467 * 16) + 73)] = (Y_local[((i_2_1_s_467 * 16) + 73)] + (A_shared_dyn_local[(i_2_1_s_467 + 4)] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_468 = 0; i_2_1_s_468 < 4; ++i_2_1_s_468) {
    Y_local[((i_2_1_s_468 * 16) + 10)] = (Y_local[((i_2_1_s_468 * 16) + 10)] + (A_shared_dyn_local[i_2_1_s_468] * B_shared_dyn_local[10]));
  }
  for (int i_2_1_s_469 = 0; i_2_1_s_469 < 4; ++i_2_1_s_469) {
    if (i_2_1_s_469 < 2) {
      Y_local[((i_2_1_s_469 * 16) + 74)] = (Y_local[((i_2_1_s_469 * 16) + 74)] + (A_shared_dyn_local[(i_2_1_s_469 + 4)] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_470 = 0; i_2_1_s_470 < 4; ++i_2_1_s_470) {
    Y_local[((i_2_1_s_470 * 16) + 11)] = (Y_local[((i_2_1_s_470 * 16) + 11)] + (A_shared_dyn_local[i_2_1_s_470] * B_shared_dyn_local[11]));
  }
  for (int i_2_1_s_471 = 0; i_2_1_s_471 < 4; ++i_2_1_s_471) {
    if (i_2_1_s_471 < 2) {
      Y_local[((i_2_1_s_471 * 16) + 75)] = (Y_local[((i_2_1_s_471 * 16) + 75)] + (A_shared_dyn_local[(i_2_1_s_471 + 4)] * B_shared_dyn_local[11]));
    }
  }
  for (int i_2_1_s_472 = 0; i_2_1_s_472 < 4; ++i_2_1_s_472) {
    Y_local[((i_2_1_s_472 * 16) + 12)] = (Y_local[((i_2_1_s_472 * 16) + 12)] + (A_shared_dyn_local[i_2_1_s_472] * B_shared_dyn_local[12]));
  }
  for (int i_2_1_s_473 = 0; i_2_1_s_473 < 4; ++i_2_1_s_473) {
    if (i_2_1_s_473 < 2) {
      Y_local[((i_2_1_s_473 * 16) + 76)] = (Y_local[((i_2_1_s_473 * 16) + 76)] + (A_shared_dyn_local[(i_2_1_s_473 + 4)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_474 = 0; i_2_1_s_474 < 4; ++i_2_1_s_474) {
    Y_local[((i_2_1_s_474 * 16) + 13)] = (Y_local[((i_2_1_s_474 * 16) + 13)] + (A_shared_dyn_local[i_2_1_s_474] * B_shared_dyn_local[13]));
  }
  for (int i_2_1_s_475 = 0; i_2_1_s_475 < 4; ++i_2_1_s_475) {
    if (i_2_1_s_475 < 2) {
      Y_local[((i_2_1_s_475 * 16) + 77)] = (Y_local[((i_2_1_s_475 * 16) + 77)] + (A_shared_dyn_local[(i_2_1_s_475 + 4)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_476 = 0; i_2_1_s_476 < 4; ++i_2_1_s_476) {
    Y_local[((i_2_1_s_476 * 16) + 14)] = (Y_local[((i_2_1_s_476 * 16) + 14)] + (A_shared_dyn_local[i_2_1_s_476] * B_shared_dyn_local[14]));
  }
  for (int i_2_1_s_477 = 0; i_2_1_s_477 < 4; ++i_2_1_s_477) {
    if (i_2_1_s_477 < 2) {
      Y_local[((i_2_1_s_477 * 16) + 78)] = (Y_local[((i_2_1_s_477 * 16) + 78)] + (A_shared_dyn_local[(i_2_1_s_477 + 4)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_478 = 0; i_2_1_s_478 < 4; ++i_2_1_s_478) {
    Y_local[((i_2_1_s_478 * 16) + 15)] = (Y_local[((i_2_1_s_478 * 16) + 15)] + (A_shared_dyn_local[i_2_1_s_478] * B_shared_dyn_local[15]));
  }
  for (int i_2_1_s_479 = 0; i_2_1_s_479 < 4; ++i_2_1_s_479) {
    if (i_2_1_s_479 < 2) {
      Y_local[((i_2_1_s_479 * 16) + 79)] = (Y_local[((i_2_1_s_479 * 16) + 79)] + (A_shared_dyn_local[(i_2_1_s_479 + 4)] * B_shared_dyn_local[15]));
    }
  }
  for (int ax0_0_16 = 0; ax0_0_16 < 2; ++ax0_0_16) {
    for (int ax0_1_s_16 = 0; ax0_1_s_16 < 4; ++ax0_1_s_16) {
      if (((ax0_0_16 * 2) + (ax0_1_s_16 >> 1)) < 3) {
        A_shared_dyn_local[((ax0_0_16 * 4) + ax0_1_s_16)] = ((float*)buf_dyn_shmem)[((((((((int)threadIdx.x) / 27) * 72) + ((((int)threadIdx.x) % 3) * 24)) + (ax0_0_16 * 16)) + (ax0_1_s_16 * 4)) + 1152)];
      }
    }
  }
  for (int ax1_0_16 = 0; ax1_0_16 < 4; ++ax1_0_16) {
    *(float4*)(B_shared_dyn_local + (ax1_0_16 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((int)blockIdx.x) & 7) * 144) + (((((int)threadIdx.x) % 27) / 3) * 16)) + (ax1_0_16 * 4)) >> 6) * 64) + ((ax1_0_16 & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 18) + (((((int)threadIdx.x) % 27) / 3) * 2)) + (ax1_0_16 >> 1)) & 7) * 4)) + 4416) - ((((((int)blockIdx.x) & 7) * 144) >> 6) * 64)));
  }
  for (int i_2_1_s_480 = 0; i_2_1_s_480 < 4; ++i_2_1_s_480) {
    Y_local[(i_2_1_s_480 * 16)] = (Y_local[(i_2_1_s_480 * 16)] + (A_shared_dyn_local[(i_2_1_s_480 + 6)] * B_shared_dyn_local[16]));
  }
  for (int i_2_1_s_481 = 0; i_2_1_s_481 < 4; ++i_2_1_s_481) {
    if (i_2_1_s_481 < 2) {
      Y_local[((i_2_1_s_481 * 16) + 64)] = (Y_local[((i_2_1_s_481 * 16) + 64)] + (A_shared_dyn_local[(i_2_1_s_481 + 10)] * B_shared_dyn_local[16]));
    }
  }
  for (int i_2_1_s_482 = 0; i_2_1_s_482 < 4; ++i_2_1_s_482) {
    Y_local[((i_2_1_s_482 * 16) + 1)] = (Y_local[((i_2_1_s_482 * 16) + 1)] + (A_shared_dyn_local[(i_2_1_s_482 + 6)] * B_shared_dyn_local[17]));
  }
  for (int i_2_1_s_483 = 0; i_2_1_s_483 < 4; ++i_2_1_s_483) {
    if (i_2_1_s_483 < 2) {
      Y_local[((i_2_1_s_483 * 16) + 65)] = (Y_local[((i_2_1_s_483 * 16) + 65)] + (A_shared_dyn_local[(i_2_1_s_483 + 10)] * B_shared_dyn_local[17]));
    }
  }
  for (int i_2_1_s_484 = 0; i_2_1_s_484 < 4; ++i_2_1_s_484) {
    Y_local[((i_2_1_s_484 * 16) + 2)] = (Y_local[((i_2_1_s_484 * 16) + 2)] + (A_shared_dyn_local[(i_2_1_s_484 + 6)] * B_shared_dyn_local[18]));
  }
  for (int i_2_1_s_485 = 0; i_2_1_s_485 < 4; ++i_2_1_s_485) {
    if (i_2_1_s_485 < 2) {
      Y_local[((i_2_1_s_485 * 16) + 66)] = (Y_local[((i_2_1_s_485 * 16) + 66)] + (A_shared_dyn_local[(i_2_1_s_485 + 10)] * B_shared_dyn_local[18]));
    }
  }
  for (int i_2_1_s_486 = 0; i_2_1_s_486 < 4; ++i_2_1_s_486) {
    Y_local[((i_2_1_s_486 * 16) + 3)] = (Y_local[((i_2_1_s_486 * 16) + 3)] + (A_shared_dyn_local[(i_2_1_s_486 + 6)] * B_shared_dyn_local[19]));
  }
  for (int i_2_1_s_487 = 0; i_2_1_s_487 < 4; ++i_2_1_s_487) {
    if (i_2_1_s_487 < 2) {
      Y_local[((i_2_1_s_487 * 16) + 67)] = (Y_local[((i_2_1_s_487 * 16) + 67)] + (A_shared_dyn_local[(i_2_1_s_487 + 10)] * B_shared_dyn_local[19]));
    }
  }
  for (int i_2_1_s_488 = 0; i_2_1_s_488 < 4; ++i_2_1_s_488) {
    Y_local[((i_2_1_s_488 * 16) + 4)] = (Y_local[((i_2_1_s_488 * 16) + 4)] + (A_shared_dyn_local[(i_2_1_s_488 + 6)] * B_shared_dyn_local[20]));
  }
  for (int i_2_1_s_489 = 0; i_2_1_s_489 < 4; ++i_2_1_s_489) {
    if (i_2_1_s_489 < 2) {
      Y_local[((i_2_1_s_489 * 16) + 68)] = (Y_local[((i_2_1_s_489 * 16) + 68)] + (A_shared_dyn_local[(i_2_1_s_489 + 10)] * B_shared_dyn_local[20]));
    }
  }
  for (int i_2_1_s_490 = 0; i_2_1_s_490 < 4; ++i_2_1_s_490) {
    Y_local[((i_2_1_s_490 * 16) + 5)] = (Y_local[((i_2_1_s_490 * 16) + 5)] + (A_shared_dyn_local[(i_2_1_s_490 + 6)] * B_shared_dyn_local[21]));
  }
  for (int i_2_1_s_491 = 0; i_2_1_s_491 < 4; ++i_2_1_s_491) {
    if (i_2_1_s_491 < 2) {
      Y_local[((i_2_1_s_491 * 16) + 69)] = (Y_local[((i_2_1_s_491 * 16) + 69)] + (A_shared_dyn_local[(i_2_1_s_491 + 10)] * B_shared_dyn_local[21]));
    }
  }
  for (int i_2_1_s_492 = 0; i_2_1_s_492 < 4; ++i_2_1_s_492) {
    Y_local[((i_2_1_s_492 * 16) + 6)] = (Y_local[((i_2_1_s_492 * 16) + 6)] + (A_shared_dyn_local[(i_2_1_s_492 + 6)] * B_shared_dyn_local[22]));
  }
  for (int i_2_1_s_493 = 0; i_2_1_s_493 < 4; ++i_2_1_s_493) {
    if (i_2_1_s_493 < 2) {
      Y_local[((i_2_1_s_493 * 16) + 70)] = (Y_local[((i_2_1_s_493 * 16) + 70)] + (A_shared_dyn_local[(i_2_1_s_493 + 10)] * B_shared_dyn_local[22]));
    }
  }
  for (int i_2_1_s_494 = 0; i_2_1_s_494 < 4; ++i_2_1_s_494) {
    Y_local[((i_2_1_s_494 * 16) + 7)] = (Y_local[((i_2_1_s_494 * 16) + 7)] + (A_shared_dyn_local[(i_2_1_s_494 + 6)] * B_shared_dyn_local[23]));
  }
  for (int i_2_1_s_495 = 0; i_2_1_s_495 < 4; ++i_2_1_s_495) {
    if (i_2_1_s_495 < 2) {
      Y_local[((i_2_1_s_495 * 16) + 71)] = (Y_local[((i_2_1_s_495 * 16) + 71)] + (A_shared_dyn_local[(i_2_1_s_495 + 10)] * B_shared_dyn_local[23]));
    }
  }
  for (int i_2_1_s_496 = 0; i_2_1_s_496 < 4; ++i_2_1_s_496) {
    Y_local[((i_2_1_s_496 * 16) + 8)] = (Y_local[((i_2_1_s_496 * 16) + 8)] + (A_shared_dyn_local[(i_2_1_s_496 + 6)] * B_shared_dyn_local[24]));
  }
  for (int i_2_1_s_497 = 0; i_2_1_s_497 < 4; ++i_2_1_s_497) {
    if (i_2_1_s_497 < 2) {
      Y_local[((i_2_1_s_497 * 16) + 72)] = (Y_local[((i_2_1_s_497 * 16) + 72)] + (A_shared_dyn_local[(i_2_1_s_497 + 10)] * B_shared_dyn_local[24]));
    }
  }
  for (int i_2_1_s_498 = 0; i_2_1_s_498 < 4; ++i_2_1_s_498) {
    Y_local[((i_2_1_s_498 * 16) + 9)] = (Y_local[((i_2_1_s_498 * 16) + 9)] + (A_shared_dyn_local[(i_2_1_s_498 + 6)] * B_shared_dyn_local[25]));
  }
  for (int i_2_1_s_499 = 0; i_2_1_s_499 < 4; ++i_2_1_s_499) {
    if (i_2_1_s_499 < 2) {
      Y_local[((i_2_1_s_499 * 16) + 73)] = (Y_local[((i_2_1_s_499 * 16) + 73)] + (A_shared_dyn_local[(i_2_1_s_499 + 10)] * B_shared_dyn_local[25]));
    }
  }
  for (int i_2_1_s_500 = 0; i_2_1_s_500 < 4; ++i_2_1_s_500) {
    Y_local[((i_2_1_s_500 * 16) + 10)] = (Y_local[((i_2_1_s_500 * 16) + 10)] + (A_shared_dyn_local[(i_2_1_s_500 + 6)] * B_shared_dyn_local[26]));
  }
  for (int i_2_1_s_501 = 0; i_2_1_s_501 < 4; ++i_2_1_s_501) {
    if (i_2_1_s_501 < 2) {
      Y_local[((i_2_1_s_501 * 16) + 74)] = (Y_local[((i_2_1_s_501 * 16) + 74)] + (A_shared_dyn_local[(i_2_1_s_501 + 10)] * B_shared_dyn_local[26]));
    }
  }
  for (int i_2_1_s_502 = 0; i_2_1_s_502 < 4; ++i_2_1_s_502) {
    Y_local[((i_2_1_s_502 * 16) + 11)] = (Y_local[((i_2_1_s_502 * 16) + 11)] + (A_shared_dyn_local[(i_2_1_s_502 + 6)] * B_shared_dyn_local[27]));
  }
  for (int i_2_1_s_503 = 0; i_2_1_s_503 < 4; ++i_2_1_s_503) {
    if (i_2_1_s_503 < 2) {
      Y_local[((i_2_1_s_503 * 16) + 75)] = (Y_local[((i_2_1_s_503 * 16) + 75)] + (A_shared_dyn_local[(i_2_1_s_503 + 10)] * B_shared_dyn_local[27]));
    }
  }
  for (int i_2_1_s_504 = 0; i_2_1_s_504 < 4; ++i_2_1_s_504) {
    Y_local[((i_2_1_s_504 * 16) + 12)] = (Y_local[((i_2_1_s_504 * 16) + 12)] + (A_shared_dyn_local[(i_2_1_s_504 + 6)] * B_shared_dyn_local[28]));
  }
  for (int i_2_1_s_505 = 0; i_2_1_s_505 < 4; ++i_2_1_s_505) {
    if (i_2_1_s_505 < 2) {
      Y_local[((i_2_1_s_505 * 16) + 76)] = (Y_local[((i_2_1_s_505 * 16) + 76)] + (A_shared_dyn_local[(i_2_1_s_505 + 10)] * B_shared_dyn_local[28]));
    }
  }
  for (int i_2_1_s_506 = 0; i_2_1_s_506 < 4; ++i_2_1_s_506) {
    Y_local[((i_2_1_s_506 * 16) + 13)] = (Y_local[((i_2_1_s_506 * 16) + 13)] + (A_shared_dyn_local[(i_2_1_s_506 + 6)] * B_shared_dyn_local[29]));
  }
  for (int i_2_1_s_507 = 0; i_2_1_s_507 < 4; ++i_2_1_s_507) {
    if (i_2_1_s_507 < 2) {
      Y_local[((i_2_1_s_507 * 16) + 77)] = (Y_local[((i_2_1_s_507 * 16) + 77)] + (A_shared_dyn_local[(i_2_1_s_507 + 10)] * B_shared_dyn_local[29]));
    }
  }
  for (int i_2_1_s_508 = 0; i_2_1_s_508 < 4; ++i_2_1_s_508) {
    Y_local[((i_2_1_s_508 * 16) + 14)] = (Y_local[((i_2_1_s_508 * 16) + 14)] + (A_shared_dyn_local[(i_2_1_s_508 + 6)] * B_shared_dyn_local[30]));
  }
  for (int i_2_1_s_509 = 0; i_2_1_s_509 < 4; ++i_2_1_s_509) {
    if (i_2_1_s_509 < 2) {
      Y_local[((i_2_1_s_509 * 16) + 78)] = (Y_local[((i_2_1_s_509 * 16) + 78)] + (A_shared_dyn_local[(i_2_1_s_509 + 10)] * B_shared_dyn_local[30]));
    }
  }
  for (int i_2_1_s_510 = 0; i_2_1_s_510 < 4; ++i_2_1_s_510) {
    Y_local[((i_2_1_s_510 * 16) + 15)] = (Y_local[((i_2_1_s_510 * 16) + 15)] + (A_shared_dyn_local[(i_2_1_s_510 + 6)] * B_shared_dyn_local[31]));
  }
  for (int i_2_1_s_511 = 0; i_2_1_s_511 < 4; ++i_2_1_s_511) {
    if (i_2_1_s_511 < 2) {
      Y_local[((i_2_1_s_511 * 16) + 79)] = (Y_local[((i_2_1_s_511 * 16) + 79)] + (A_shared_dyn_local[(i_2_1_s_511 + 10)] * B_shared_dyn_local[31]));
    }
  }
  for (int ax0_0_17 = 0; ax0_0_17 < 2; ++ax0_0_17) {
    for (int ax0_1_s_17 = 0; ax0_1_s_17 < 4; ++ax0_1_s_17) {
      if (((ax0_0_17 * 2) + (ax0_1_s_17 >> 1)) < 3) {
        A_shared_dyn_local[(((ax0_0_17 * 4) + ax0_1_s_17) + 6)] = ((float*)buf_dyn_shmem)[((((((((int)threadIdx.x) / 27) * 72) + ((((int)threadIdx.x) % 3) * 24)) + (ax0_0_17 * 16)) + (ax0_1_s_17 * 4)) + 1153)];
      }
    }
  }
  for (int ax1_0_17 = 0; ax1_0_17 < 4; ++ax1_0_17) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_17 * 4) + 16)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((int)blockIdx.x) & 7) * 144) + (((((int)threadIdx.x) % 27) / 3) * 16)) + (ax1_0_17 * 4)) >> 6) * 64) + ((ax1_0_17 & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 18) + (((((int)threadIdx.x) % 27) / 3) * 2)) + (ax1_0_17 >> 1)) & 7) * 4)) + 4608) - ((((((int)blockIdx.x) & 7) * 144) >> 6) * 64)));
  }
  for (int i_2_1_s_512 = 0; i_2_1_s_512 < 4; ++i_2_1_s_512) {
    Y_local[(i_2_1_s_512 * 16)] = (Y_local[(i_2_1_s_512 * 16)] + (A_shared_dyn_local[i_2_1_s_512] * B_shared_dyn_local[0]));
  }
  for (int i_2_1_s_513 = 0; i_2_1_s_513 < 4; ++i_2_1_s_513) {
    if (i_2_1_s_513 < 2) {
      Y_local[((i_2_1_s_513 * 16) + 64)] = (Y_local[((i_2_1_s_513 * 16) + 64)] + (A_shared_dyn_local[(i_2_1_s_513 + 4)] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_514 = 0; i_2_1_s_514 < 4; ++i_2_1_s_514) {
    Y_local[((i_2_1_s_514 * 16) + 1)] = (Y_local[((i_2_1_s_514 * 16) + 1)] + (A_shared_dyn_local[i_2_1_s_514] * B_shared_dyn_local[1]));
  }
  for (int i_2_1_s_515 = 0; i_2_1_s_515 < 4; ++i_2_1_s_515) {
    if (i_2_1_s_515 < 2) {
      Y_local[((i_2_1_s_515 * 16) + 65)] = (Y_local[((i_2_1_s_515 * 16) + 65)] + (A_shared_dyn_local[(i_2_1_s_515 + 4)] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_516 = 0; i_2_1_s_516 < 4; ++i_2_1_s_516) {
    Y_local[((i_2_1_s_516 * 16) + 2)] = (Y_local[((i_2_1_s_516 * 16) + 2)] + (A_shared_dyn_local[i_2_1_s_516] * B_shared_dyn_local[2]));
  }
  for (int i_2_1_s_517 = 0; i_2_1_s_517 < 4; ++i_2_1_s_517) {
    if (i_2_1_s_517 < 2) {
      Y_local[((i_2_1_s_517 * 16) + 66)] = (Y_local[((i_2_1_s_517 * 16) + 66)] + (A_shared_dyn_local[(i_2_1_s_517 + 4)] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_518 = 0; i_2_1_s_518 < 4; ++i_2_1_s_518) {
    Y_local[((i_2_1_s_518 * 16) + 3)] = (Y_local[((i_2_1_s_518 * 16) + 3)] + (A_shared_dyn_local[i_2_1_s_518] * B_shared_dyn_local[3]));
  }
  for (int i_2_1_s_519 = 0; i_2_1_s_519 < 4; ++i_2_1_s_519) {
    if (i_2_1_s_519 < 2) {
      Y_local[((i_2_1_s_519 * 16) + 67)] = (Y_local[((i_2_1_s_519 * 16) + 67)] + (A_shared_dyn_local[(i_2_1_s_519 + 4)] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_520 = 0; i_2_1_s_520 < 4; ++i_2_1_s_520) {
    Y_local[((i_2_1_s_520 * 16) + 4)] = (Y_local[((i_2_1_s_520 * 16) + 4)] + (A_shared_dyn_local[i_2_1_s_520] * B_shared_dyn_local[4]));
  }
  for (int i_2_1_s_521 = 0; i_2_1_s_521 < 4; ++i_2_1_s_521) {
    if (i_2_1_s_521 < 2) {
      Y_local[((i_2_1_s_521 * 16) + 68)] = (Y_local[((i_2_1_s_521 * 16) + 68)] + (A_shared_dyn_local[(i_2_1_s_521 + 4)] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_522 = 0; i_2_1_s_522 < 4; ++i_2_1_s_522) {
    Y_local[((i_2_1_s_522 * 16) + 5)] = (Y_local[((i_2_1_s_522 * 16) + 5)] + (A_shared_dyn_local[i_2_1_s_522] * B_shared_dyn_local[5]));
  }
  for (int i_2_1_s_523 = 0; i_2_1_s_523 < 4; ++i_2_1_s_523) {
    if (i_2_1_s_523 < 2) {
      Y_local[((i_2_1_s_523 * 16) + 69)] = (Y_local[((i_2_1_s_523 * 16) + 69)] + (A_shared_dyn_local[(i_2_1_s_523 + 4)] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_524 = 0; i_2_1_s_524 < 4; ++i_2_1_s_524) {
    Y_local[((i_2_1_s_524 * 16) + 6)] = (Y_local[((i_2_1_s_524 * 16) + 6)] + (A_shared_dyn_local[i_2_1_s_524] * B_shared_dyn_local[6]));
  }
  for (int i_2_1_s_525 = 0; i_2_1_s_525 < 4; ++i_2_1_s_525) {
    if (i_2_1_s_525 < 2) {
      Y_local[((i_2_1_s_525 * 16) + 70)] = (Y_local[((i_2_1_s_525 * 16) + 70)] + (A_shared_dyn_local[(i_2_1_s_525 + 4)] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_526 = 0; i_2_1_s_526 < 4; ++i_2_1_s_526) {
    Y_local[((i_2_1_s_526 * 16) + 7)] = (Y_local[((i_2_1_s_526 * 16) + 7)] + (A_shared_dyn_local[i_2_1_s_526] * B_shared_dyn_local[7]));
  }
  for (int i_2_1_s_527 = 0; i_2_1_s_527 < 4; ++i_2_1_s_527) {
    if (i_2_1_s_527 < 2) {
      Y_local[((i_2_1_s_527 * 16) + 71)] = (Y_local[((i_2_1_s_527 * 16) + 71)] + (A_shared_dyn_local[(i_2_1_s_527 + 4)] * B_shared_dyn_local[7]));
    }
  }
  for (int i_2_1_s_528 = 0; i_2_1_s_528 < 4; ++i_2_1_s_528) {
    Y_local[((i_2_1_s_528 * 16) + 8)] = (Y_local[((i_2_1_s_528 * 16) + 8)] + (A_shared_dyn_local[i_2_1_s_528] * B_shared_dyn_local[8]));
  }
  for (int i_2_1_s_529 = 0; i_2_1_s_529 < 4; ++i_2_1_s_529) {
    if (i_2_1_s_529 < 2) {
      Y_local[((i_2_1_s_529 * 16) + 72)] = (Y_local[((i_2_1_s_529 * 16) + 72)] + (A_shared_dyn_local[(i_2_1_s_529 + 4)] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_530 = 0; i_2_1_s_530 < 4; ++i_2_1_s_530) {
    Y_local[((i_2_1_s_530 * 16) + 9)] = (Y_local[((i_2_1_s_530 * 16) + 9)] + (A_shared_dyn_local[i_2_1_s_530] * B_shared_dyn_local[9]));
  }
  for (int i_2_1_s_531 = 0; i_2_1_s_531 < 4; ++i_2_1_s_531) {
    if (i_2_1_s_531 < 2) {
      Y_local[((i_2_1_s_531 * 16) + 73)] = (Y_local[((i_2_1_s_531 * 16) + 73)] + (A_shared_dyn_local[(i_2_1_s_531 + 4)] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_532 = 0; i_2_1_s_532 < 4; ++i_2_1_s_532) {
    Y_local[((i_2_1_s_532 * 16) + 10)] = (Y_local[((i_2_1_s_532 * 16) + 10)] + (A_shared_dyn_local[i_2_1_s_532] * B_shared_dyn_local[10]));
  }
  for (int i_2_1_s_533 = 0; i_2_1_s_533 < 4; ++i_2_1_s_533) {
    if (i_2_1_s_533 < 2) {
      Y_local[((i_2_1_s_533 * 16) + 74)] = (Y_local[((i_2_1_s_533 * 16) + 74)] + (A_shared_dyn_local[(i_2_1_s_533 + 4)] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_534 = 0; i_2_1_s_534 < 4; ++i_2_1_s_534) {
    Y_local[((i_2_1_s_534 * 16) + 11)] = (Y_local[((i_2_1_s_534 * 16) + 11)] + (A_shared_dyn_local[i_2_1_s_534] * B_shared_dyn_local[11]));
  }
  for (int i_2_1_s_535 = 0; i_2_1_s_535 < 4; ++i_2_1_s_535) {
    if (i_2_1_s_535 < 2) {
      Y_local[((i_2_1_s_535 * 16) + 75)] = (Y_local[((i_2_1_s_535 * 16) + 75)] + (A_shared_dyn_local[(i_2_1_s_535 + 4)] * B_shared_dyn_local[11]));
    }
  }
  for (int i_2_1_s_536 = 0; i_2_1_s_536 < 4; ++i_2_1_s_536) {
    Y_local[((i_2_1_s_536 * 16) + 12)] = (Y_local[((i_2_1_s_536 * 16) + 12)] + (A_shared_dyn_local[i_2_1_s_536] * B_shared_dyn_local[12]));
  }
  for (int i_2_1_s_537 = 0; i_2_1_s_537 < 4; ++i_2_1_s_537) {
    if (i_2_1_s_537 < 2) {
      Y_local[((i_2_1_s_537 * 16) + 76)] = (Y_local[((i_2_1_s_537 * 16) + 76)] + (A_shared_dyn_local[(i_2_1_s_537 + 4)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_538 = 0; i_2_1_s_538 < 4; ++i_2_1_s_538) {
    Y_local[((i_2_1_s_538 * 16) + 13)] = (Y_local[((i_2_1_s_538 * 16) + 13)] + (A_shared_dyn_local[i_2_1_s_538] * B_shared_dyn_local[13]));
  }
  for (int i_2_1_s_539 = 0; i_2_1_s_539 < 4; ++i_2_1_s_539) {
    if (i_2_1_s_539 < 2) {
      Y_local[((i_2_1_s_539 * 16) + 77)] = (Y_local[((i_2_1_s_539 * 16) + 77)] + (A_shared_dyn_local[(i_2_1_s_539 + 4)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_540 = 0; i_2_1_s_540 < 4; ++i_2_1_s_540) {
    Y_local[((i_2_1_s_540 * 16) + 14)] = (Y_local[((i_2_1_s_540 * 16) + 14)] + (A_shared_dyn_local[i_2_1_s_540] * B_shared_dyn_local[14]));
  }
  for (int i_2_1_s_541 = 0; i_2_1_s_541 < 4; ++i_2_1_s_541) {
    if (i_2_1_s_541 < 2) {
      Y_local[((i_2_1_s_541 * 16) + 78)] = (Y_local[((i_2_1_s_541 * 16) + 78)] + (A_shared_dyn_local[(i_2_1_s_541 + 4)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_542 = 0; i_2_1_s_542 < 4; ++i_2_1_s_542) {
    Y_local[((i_2_1_s_542 * 16) + 15)] = (Y_local[((i_2_1_s_542 * 16) + 15)] + (A_shared_dyn_local[i_2_1_s_542] * B_shared_dyn_local[15]));
  }
  for (int i_2_1_s_543 = 0; i_2_1_s_543 < 4; ++i_2_1_s_543) {
    if (i_2_1_s_543 < 2) {
      Y_local[((i_2_1_s_543 * 16) + 79)] = (Y_local[((i_2_1_s_543 * 16) + 79)] + (A_shared_dyn_local[(i_2_1_s_543 + 4)] * B_shared_dyn_local[15]));
    }
  }
  for (int ax0_0_18 = 0; ax0_0_18 < 2; ++ax0_0_18) {
    for (int ax0_1_s_18 = 0; ax0_1_s_18 < 4; ++ax0_1_s_18) {
      if (((ax0_0_18 * 2) + (ax0_1_s_18 >> 1)) < 3) {
        A_shared_dyn_local[((ax0_0_18 * 4) + ax0_1_s_18)] = ((float*)buf_dyn_shmem)[((((((((int)threadIdx.x) / 27) * 72) + ((((int)threadIdx.x) % 3) * 24)) + (ax0_0_18 * 16)) + (ax0_1_s_18 * 4)) + 1154)];
      }
    }
  }
  for (int ax1_0_18 = 0; ax1_0_18 < 4; ++ax1_0_18) {
    *(float4*)(B_shared_dyn_local + (ax1_0_18 * 4)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((int)blockIdx.x) & 7) * 144) + (((((int)threadIdx.x) % 27) / 3) * 16)) + (ax1_0_18 * 4)) >> 6) * 64) + ((ax1_0_18 & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 18) + (((((int)threadIdx.x) % 27) / 3) * 2)) + (ax1_0_18 >> 1)) & 7) * 4)) + 4800) - ((((((int)blockIdx.x) & 7) * 144) >> 6) * 64)));
  }
  for (int i_2_1_s_544 = 0; i_2_1_s_544 < 4; ++i_2_1_s_544) {
    Y_local[(i_2_1_s_544 * 16)] = (Y_local[(i_2_1_s_544 * 16)] + (A_shared_dyn_local[(i_2_1_s_544 + 6)] * B_shared_dyn_local[16]));
  }
  for (int i_2_1_s_545 = 0; i_2_1_s_545 < 4; ++i_2_1_s_545) {
    if (i_2_1_s_545 < 2) {
      Y_local[((i_2_1_s_545 * 16) + 64)] = (Y_local[((i_2_1_s_545 * 16) + 64)] + (A_shared_dyn_local[(i_2_1_s_545 + 10)] * B_shared_dyn_local[16]));
    }
  }
  for (int i_2_1_s_546 = 0; i_2_1_s_546 < 4; ++i_2_1_s_546) {
    Y_local[((i_2_1_s_546 * 16) + 1)] = (Y_local[((i_2_1_s_546 * 16) + 1)] + (A_shared_dyn_local[(i_2_1_s_546 + 6)] * B_shared_dyn_local[17]));
  }
  for (int i_2_1_s_547 = 0; i_2_1_s_547 < 4; ++i_2_1_s_547) {
    if (i_2_1_s_547 < 2) {
      Y_local[((i_2_1_s_547 * 16) + 65)] = (Y_local[((i_2_1_s_547 * 16) + 65)] + (A_shared_dyn_local[(i_2_1_s_547 + 10)] * B_shared_dyn_local[17]));
    }
  }
  for (int i_2_1_s_548 = 0; i_2_1_s_548 < 4; ++i_2_1_s_548) {
    Y_local[((i_2_1_s_548 * 16) + 2)] = (Y_local[((i_2_1_s_548 * 16) + 2)] + (A_shared_dyn_local[(i_2_1_s_548 + 6)] * B_shared_dyn_local[18]));
  }
  for (int i_2_1_s_549 = 0; i_2_1_s_549 < 4; ++i_2_1_s_549) {
    if (i_2_1_s_549 < 2) {
      Y_local[((i_2_1_s_549 * 16) + 66)] = (Y_local[((i_2_1_s_549 * 16) + 66)] + (A_shared_dyn_local[(i_2_1_s_549 + 10)] * B_shared_dyn_local[18]));
    }
  }
  for (int i_2_1_s_550 = 0; i_2_1_s_550 < 4; ++i_2_1_s_550) {
    Y_local[((i_2_1_s_550 * 16) + 3)] = (Y_local[((i_2_1_s_550 * 16) + 3)] + (A_shared_dyn_local[(i_2_1_s_550 + 6)] * B_shared_dyn_local[19]));
  }
  for (int i_2_1_s_551 = 0; i_2_1_s_551 < 4; ++i_2_1_s_551) {
    if (i_2_1_s_551 < 2) {
      Y_local[((i_2_1_s_551 * 16) + 67)] = (Y_local[((i_2_1_s_551 * 16) + 67)] + (A_shared_dyn_local[(i_2_1_s_551 + 10)] * B_shared_dyn_local[19]));
    }
  }
  for (int i_2_1_s_552 = 0; i_2_1_s_552 < 4; ++i_2_1_s_552) {
    Y_local[((i_2_1_s_552 * 16) + 4)] = (Y_local[((i_2_1_s_552 * 16) + 4)] + (A_shared_dyn_local[(i_2_1_s_552 + 6)] * B_shared_dyn_local[20]));
  }
  for (int i_2_1_s_553 = 0; i_2_1_s_553 < 4; ++i_2_1_s_553) {
    if (i_2_1_s_553 < 2) {
      Y_local[((i_2_1_s_553 * 16) + 68)] = (Y_local[((i_2_1_s_553 * 16) + 68)] + (A_shared_dyn_local[(i_2_1_s_553 + 10)] * B_shared_dyn_local[20]));
    }
  }
  for (int i_2_1_s_554 = 0; i_2_1_s_554 < 4; ++i_2_1_s_554) {
    Y_local[((i_2_1_s_554 * 16) + 5)] = (Y_local[((i_2_1_s_554 * 16) + 5)] + (A_shared_dyn_local[(i_2_1_s_554 + 6)] * B_shared_dyn_local[21]));
  }
  for (int i_2_1_s_555 = 0; i_2_1_s_555 < 4; ++i_2_1_s_555) {
    if (i_2_1_s_555 < 2) {
      Y_local[((i_2_1_s_555 * 16) + 69)] = (Y_local[((i_2_1_s_555 * 16) + 69)] + (A_shared_dyn_local[(i_2_1_s_555 + 10)] * B_shared_dyn_local[21]));
    }
  }
  for (int i_2_1_s_556 = 0; i_2_1_s_556 < 4; ++i_2_1_s_556) {
    Y_local[((i_2_1_s_556 * 16) + 6)] = (Y_local[((i_2_1_s_556 * 16) + 6)] + (A_shared_dyn_local[(i_2_1_s_556 + 6)] * B_shared_dyn_local[22]));
  }
  for (int i_2_1_s_557 = 0; i_2_1_s_557 < 4; ++i_2_1_s_557) {
    if (i_2_1_s_557 < 2) {
      Y_local[((i_2_1_s_557 * 16) + 70)] = (Y_local[((i_2_1_s_557 * 16) + 70)] + (A_shared_dyn_local[(i_2_1_s_557 + 10)] * B_shared_dyn_local[22]));
    }
  }
  for (int i_2_1_s_558 = 0; i_2_1_s_558 < 4; ++i_2_1_s_558) {
    Y_local[((i_2_1_s_558 * 16) + 7)] = (Y_local[((i_2_1_s_558 * 16) + 7)] + (A_shared_dyn_local[(i_2_1_s_558 + 6)] * B_shared_dyn_local[23]));
  }
  for (int i_2_1_s_559 = 0; i_2_1_s_559 < 4; ++i_2_1_s_559) {
    if (i_2_1_s_559 < 2) {
      Y_local[((i_2_1_s_559 * 16) + 71)] = (Y_local[((i_2_1_s_559 * 16) + 71)] + (A_shared_dyn_local[(i_2_1_s_559 + 10)] * B_shared_dyn_local[23]));
    }
  }
  for (int i_2_1_s_560 = 0; i_2_1_s_560 < 4; ++i_2_1_s_560) {
    Y_local[((i_2_1_s_560 * 16) + 8)] = (Y_local[((i_2_1_s_560 * 16) + 8)] + (A_shared_dyn_local[(i_2_1_s_560 + 6)] * B_shared_dyn_local[24]));
  }
  for (int i_2_1_s_561 = 0; i_2_1_s_561 < 4; ++i_2_1_s_561) {
    if (i_2_1_s_561 < 2) {
      Y_local[((i_2_1_s_561 * 16) + 72)] = (Y_local[((i_2_1_s_561 * 16) + 72)] + (A_shared_dyn_local[(i_2_1_s_561 + 10)] * B_shared_dyn_local[24]));
    }
  }
  for (int i_2_1_s_562 = 0; i_2_1_s_562 < 4; ++i_2_1_s_562) {
    Y_local[((i_2_1_s_562 * 16) + 9)] = (Y_local[((i_2_1_s_562 * 16) + 9)] + (A_shared_dyn_local[(i_2_1_s_562 + 6)] * B_shared_dyn_local[25]));
  }
  for (int i_2_1_s_563 = 0; i_2_1_s_563 < 4; ++i_2_1_s_563) {
    if (i_2_1_s_563 < 2) {
      Y_local[((i_2_1_s_563 * 16) + 73)] = (Y_local[((i_2_1_s_563 * 16) + 73)] + (A_shared_dyn_local[(i_2_1_s_563 + 10)] * B_shared_dyn_local[25]));
    }
  }
  for (int i_2_1_s_564 = 0; i_2_1_s_564 < 4; ++i_2_1_s_564) {
    Y_local[((i_2_1_s_564 * 16) + 10)] = (Y_local[((i_2_1_s_564 * 16) + 10)] + (A_shared_dyn_local[(i_2_1_s_564 + 6)] * B_shared_dyn_local[26]));
  }
  for (int i_2_1_s_565 = 0; i_2_1_s_565 < 4; ++i_2_1_s_565) {
    if (i_2_1_s_565 < 2) {
      Y_local[((i_2_1_s_565 * 16) + 74)] = (Y_local[((i_2_1_s_565 * 16) + 74)] + (A_shared_dyn_local[(i_2_1_s_565 + 10)] * B_shared_dyn_local[26]));
    }
  }
  for (int i_2_1_s_566 = 0; i_2_1_s_566 < 4; ++i_2_1_s_566) {
    Y_local[((i_2_1_s_566 * 16) + 11)] = (Y_local[((i_2_1_s_566 * 16) + 11)] + (A_shared_dyn_local[(i_2_1_s_566 + 6)] * B_shared_dyn_local[27]));
  }
  for (int i_2_1_s_567 = 0; i_2_1_s_567 < 4; ++i_2_1_s_567) {
    if (i_2_1_s_567 < 2) {
      Y_local[((i_2_1_s_567 * 16) + 75)] = (Y_local[((i_2_1_s_567 * 16) + 75)] + (A_shared_dyn_local[(i_2_1_s_567 + 10)] * B_shared_dyn_local[27]));
    }
  }
  for (int i_2_1_s_568 = 0; i_2_1_s_568 < 4; ++i_2_1_s_568) {
    Y_local[((i_2_1_s_568 * 16) + 12)] = (Y_local[((i_2_1_s_568 * 16) + 12)] + (A_shared_dyn_local[(i_2_1_s_568 + 6)] * B_shared_dyn_local[28]));
  }
  for (int i_2_1_s_569 = 0; i_2_1_s_569 < 4; ++i_2_1_s_569) {
    if (i_2_1_s_569 < 2) {
      Y_local[((i_2_1_s_569 * 16) + 76)] = (Y_local[((i_2_1_s_569 * 16) + 76)] + (A_shared_dyn_local[(i_2_1_s_569 + 10)] * B_shared_dyn_local[28]));
    }
  }
  for (int i_2_1_s_570 = 0; i_2_1_s_570 < 4; ++i_2_1_s_570) {
    Y_local[((i_2_1_s_570 * 16) + 13)] = (Y_local[((i_2_1_s_570 * 16) + 13)] + (A_shared_dyn_local[(i_2_1_s_570 + 6)] * B_shared_dyn_local[29]));
  }
  for (int i_2_1_s_571 = 0; i_2_1_s_571 < 4; ++i_2_1_s_571) {
    if (i_2_1_s_571 < 2) {
      Y_local[((i_2_1_s_571 * 16) + 77)] = (Y_local[((i_2_1_s_571 * 16) + 77)] + (A_shared_dyn_local[(i_2_1_s_571 + 10)] * B_shared_dyn_local[29]));
    }
  }
  for (int i_2_1_s_572 = 0; i_2_1_s_572 < 4; ++i_2_1_s_572) {
    Y_local[((i_2_1_s_572 * 16) + 14)] = (Y_local[((i_2_1_s_572 * 16) + 14)] + (A_shared_dyn_local[(i_2_1_s_572 + 6)] * B_shared_dyn_local[30]));
  }
  for (int i_2_1_s_573 = 0; i_2_1_s_573 < 4; ++i_2_1_s_573) {
    if (i_2_1_s_573 < 2) {
      Y_local[((i_2_1_s_573 * 16) + 78)] = (Y_local[((i_2_1_s_573 * 16) + 78)] + (A_shared_dyn_local[(i_2_1_s_573 + 10)] * B_shared_dyn_local[30]));
    }
  }
  for (int i_2_1_s_574 = 0; i_2_1_s_574 < 4; ++i_2_1_s_574) {
    Y_local[((i_2_1_s_574 * 16) + 15)] = (Y_local[((i_2_1_s_574 * 16) + 15)] + (A_shared_dyn_local[(i_2_1_s_574 + 6)] * B_shared_dyn_local[31]));
  }
  for (int i_2_1_s_575 = 0; i_2_1_s_575 < 4; ++i_2_1_s_575) {
    if (i_2_1_s_575 < 2) {
      Y_local[((i_2_1_s_575 * 16) + 79)] = (Y_local[((i_2_1_s_575 * 16) + 79)] + (A_shared_dyn_local[(i_2_1_s_575 + 10)] * B_shared_dyn_local[31]));
    }
  }
  for (int ax0_0_19 = 0; ax0_0_19 < 2; ++ax0_0_19) {
    for (int ax0_1_s_19 = 0; ax0_1_s_19 < 4; ++ax0_1_s_19) {
      if (((ax0_0_19 * 2) + (ax0_1_s_19 >> 1)) < 3) {
        A_shared_dyn_local[(((ax0_0_19 * 4) + ax0_1_s_19) + 6)] = ((float*)buf_dyn_shmem)[((((((((int)threadIdx.x) / 27) * 72) + ((((int)threadIdx.x) % 3) * 24)) + (ax0_0_19 * 16)) + (ax0_1_s_19 * 4)) + 1155)];
      }
    }
  }
  for (int ax1_0_19 = 0; ax1_0_19 < 4; ++ax1_0_19) {
    *(float4*)(B_shared_dyn_local + ((ax1_0_19 * 4) + 16)) = *(float4*)(((float*)buf_dyn_shmem) + ((((((((((((int)blockIdx.x) & 7) * 144) + (((((int)threadIdx.x) % 27) / 3) * 16)) + (ax1_0_19 * 4)) >> 6) * 64) + ((ax1_0_19 & 1) * 32)) + ((((((((int)blockIdx.x) & 7) * 18) + (((((int)threadIdx.x) % 27) / 3) * 2)) + (ax1_0_19 >> 1)) & 7) * 4)) + 4992) - ((((((int)blockIdx.x) & 7) * 144) >> 6) * 64)));
  }
  for (int i_2_1_s_576 = 0; i_2_1_s_576 < 4; ++i_2_1_s_576) {
    Y_local[(i_2_1_s_576 * 16)] = (Y_local[(i_2_1_s_576 * 16)] + (A_shared_dyn_local[i_2_1_s_576] * B_shared_dyn_local[0]));
  }
  for (int i_2_1_s_577 = 0; i_2_1_s_577 < 4; ++i_2_1_s_577) {
    if (i_2_1_s_577 < 2) {
      Y_local[((i_2_1_s_577 * 16) + 64)] = (Y_local[((i_2_1_s_577 * 16) + 64)] + (A_shared_dyn_local[(i_2_1_s_577 + 4)] * B_shared_dyn_local[0]));
    }
  }
  for (int i_2_1_s_578 = 0; i_2_1_s_578 < 4; ++i_2_1_s_578) {
    Y_local[((i_2_1_s_578 * 16) + 1)] = (Y_local[((i_2_1_s_578 * 16) + 1)] + (A_shared_dyn_local[i_2_1_s_578] * B_shared_dyn_local[1]));
  }
  for (int i_2_1_s_579 = 0; i_2_1_s_579 < 4; ++i_2_1_s_579) {
    if (i_2_1_s_579 < 2) {
      Y_local[((i_2_1_s_579 * 16) + 65)] = (Y_local[((i_2_1_s_579 * 16) + 65)] + (A_shared_dyn_local[(i_2_1_s_579 + 4)] * B_shared_dyn_local[1]));
    }
  }
  for (int i_2_1_s_580 = 0; i_2_1_s_580 < 4; ++i_2_1_s_580) {
    Y_local[((i_2_1_s_580 * 16) + 2)] = (Y_local[((i_2_1_s_580 * 16) + 2)] + (A_shared_dyn_local[i_2_1_s_580] * B_shared_dyn_local[2]));
  }
  for (int i_2_1_s_581 = 0; i_2_1_s_581 < 4; ++i_2_1_s_581) {
    if (i_2_1_s_581 < 2) {
      Y_local[((i_2_1_s_581 * 16) + 66)] = (Y_local[((i_2_1_s_581 * 16) + 66)] + (A_shared_dyn_local[(i_2_1_s_581 + 4)] * B_shared_dyn_local[2]));
    }
  }
  for (int i_2_1_s_582 = 0; i_2_1_s_582 < 4; ++i_2_1_s_582) {
    Y_local[((i_2_1_s_582 * 16) + 3)] = (Y_local[((i_2_1_s_582 * 16) + 3)] + (A_shared_dyn_local[i_2_1_s_582] * B_shared_dyn_local[3]));
  }
  for (int i_2_1_s_583 = 0; i_2_1_s_583 < 4; ++i_2_1_s_583) {
    if (i_2_1_s_583 < 2) {
      Y_local[((i_2_1_s_583 * 16) + 67)] = (Y_local[((i_2_1_s_583 * 16) + 67)] + (A_shared_dyn_local[(i_2_1_s_583 + 4)] * B_shared_dyn_local[3]));
    }
  }
  for (int i_2_1_s_584 = 0; i_2_1_s_584 < 4; ++i_2_1_s_584) {
    Y_local[((i_2_1_s_584 * 16) + 4)] = (Y_local[((i_2_1_s_584 * 16) + 4)] + (A_shared_dyn_local[i_2_1_s_584] * B_shared_dyn_local[4]));
  }
  for (int i_2_1_s_585 = 0; i_2_1_s_585 < 4; ++i_2_1_s_585) {
    if (i_2_1_s_585 < 2) {
      Y_local[((i_2_1_s_585 * 16) + 68)] = (Y_local[((i_2_1_s_585 * 16) + 68)] + (A_shared_dyn_local[(i_2_1_s_585 + 4)] * B_shared_dyn_local[4]));
    }
  }
  for (int i_2_1_s_586 = 0; i_2_1_s_586 < 4; ++i_2_1_s_586) {
    Y_local[((i_2_1_s_586 * 16) + 5)] = (Y_local[((i_2_1_s_586 * 16) + 5)] + (A_shared_dyn_local[i_2_1_s_586] * B_shared_dyn_local[5]));
  }
  for (int i_2_1_s_587 = 0; i_2_1_s_587 < 4; ++i_2_1_s_587) {
    if (i_2_1_s_587 < 2) {
      Y_local[((i_2_1_s_587 * 16) + 69)] = (Y_local[((i_2_1_s_587 * 16) + 69)] + (A_shared_dyn_local[(i_2_1_s_587 + 4)] * B_shared_dyn_local[5]));
    }
  }
  for (int i_2_1_s_588 = 0; i_2_1_s_588 < 4; ++i_2_1_s_588) {
    Y_local[((i_2_1_s_588 * 16) + 6)] = (Y_local[((i_2_1_s_588 * 16) + 6)] + (A_shared_dyn_local[i_2_1_s_588] * B_shared_dyn_local[6]));
  }
  for (int i_2_1_s_589 = 0; i_2_1_s_589 < 4; ++i_2_1_s_589) {
    if (i_2_1_s_589 < 2) {
      Y_local[((i_2_1_s_589 * 16) + 70)] = (Y_local[((i_2_1_s_589 * 16) + 70)] + (A_shared_dyn_local[(i_2_1_s_589 + 4)] * B_shared_dyn_local[6]));
    }
  }
  for (int i_2_1_s_590 = 0; i_2_1_s_590 < 4; ++i_2_1_s_590) {
    Y_local[((i_2_1_s_590 * 16) + 7)] = (Y_local[((i_2_1_s_590 * 16) + 7)] + (A_shared_dyn_local[i_2_1_s_590] * B_shared_dyn_local[7]));
  }
  for (int i_2_1_s_591 = 0; i_2_1_s_591 < 4; ++i_2_1_s_591) {
    if (i_2_1_s_591 < 2) {
      Y_local[((i_2_1_s_591 * 16) + 71)] = (Y_local[((i_2_1_s_591 * 16) + 71)] + (A_shared_dyn_local[(i_2_1_s_591 + 4)] * B_shared_dyn_local[7]));
    }
  }
  for (int i_2_1_s_592 = 0; i_2_1_s_592 < 4; ++i_2_1_s_592) {
    Y_local[((i_2_1_s_592 * 16) + 8)] = (Y_local[((i_2_1_s_592 * 16) + 8)] + (A_shared_dyn_local[i_2_1_s_592] * B_shared_dyn_local[8]));
  }
  for (int i_2_1_s_593 = 0; i_2_1_s_593 < 4; ++i_2_1_s_593) {
    if (i_2_1_s_593 < 2) {
      Y_local[((i_2_1_s_593 * 16) + 72)] = (Y_local[((i_2_1_s_593 * 16) + 72)] + (A_shared_dyn_local[(i_2_1_s_593 + 4)] * B_shared_dyn_local[8]));
    }
  }
  for (int i_2_1_s_594 = 0; i_2_1_s_594 < 4; ++i_2_1_s_594) {
    Y_local[((i_2_1_s_594 * 16) + 9)] = (Y_local[((i_2_1_s_594 * 16) + 9)] + (A_shared_dyn_local[i_2_1_s_594] * B_shared_dyn_local[9]));
  }
  for (int i_2_1_s_595 = 0; i_2_1_s_595 < 4; ++i_2_1_s_595) {
    if (i_2_1_s_595 < 2) {
      Y_local[((i_2_1_s_595 * 16) + 73)] = (Y_local[((i_2_1_s_595 * 16) + 73)] + (A_shared_dyn_local[(i_2_1_s_595 + 4)] * B_shared_dyn_local[9]));
    }
  }
  for (int i_2_1_s_596 = 0; i_2_1_s_596 < 4; ++i_2_1_s_596) {
    Y_local[((i_2_1_s_596 * 16) + 10)] = (Y_local[((i_2_1_s_596 * 16) + 10)] + (A_shared_dyn_local[i_2_1_s_596] * B_shared_dyn_local[10]));
  }
  for (int i_2_1_s_597 = 0; i_2_1_s_597 < 4; ++i_2_1_s_597) {
    if (i_2_1_s_597 < 2) {
      Y_local[((i_2_1_s_597 * 16) + 74)] = (Y_local[((i_2_1_s_597 * 16) + 74)] + (A_shared_dyn_local[(i_2_1_s_597 + 4)] * B_shared_dyn_local[10]));
    }
  }
  for (int i_2_1_s_598 = 0; i_2_1_s_598 < 4; ++i_2_1_s_598) {
    Y_local[((i_2_1_s_598 * 16) + 11)] = (Y_local[((i_2_1_s_598 * 16) + 11)] + (A_shared_dyn_local[i_2_1_s_598] * B_shared_dyn_local[11]));
  }
  for (int i_2_1_s_599 = 0; i_2_1_s_599 < 4; ++i_2_1_s_599) {
    if (i_2_1_s_599 < 2) {
      Y_local[((i_2_1_s_599 * 16) + 75)] = (Y_local[((i_2_1_s_599 * 16) + 75)] + (A_shared_dyn_local[(i_2_1_s_599 + 4)] * B_shared_dyn_local[11]));
    }
  }
  for (int i_2_1_s_600 = 0; i_2_1_s_600 < 4; ++i_2_1_s_600) {
    Y_local[((i_2_1_s_600 * 16) + 12)] = (Y_local[((i_2_1_s_600 * 16) + 12)] + (A_shared_dyn_local[i_2_1_s_600] * B_shared_dyn_local[12]));
  }
  for (int i_2_1_s_601 = 0; i_2_1_s_601 < 4; ++i_2_1_s_601) {
    if (i_2_1_s_601 < 2) {
      Y_local[((i_2_1_s_601 * 16) + 76)] = (Y_local[((i_2_1_s_601 * 16) + 76)] + (A_shared_dyn_local[(i_2_1_s_601 + 4)] * B_shared_dyn_local[12]));
    }
  }
  for (int i_2_1_s_602 = 0; i_2_1_s_602 < 4; ++i_2_1_s_602) {
    Y_local[((i_2_1_s_602 * 16) + 13)] = (Y_local[((i_2_1_s_602 * 16) + 13)] + (A_shared_dyn_local[i_2_1_s_602] * B_shared_dyn_local[13]));
  }
  for (int i_2_1_s_603 = 0; i_2_1_s_603 < 4; ++i_2_1_s_603) {
    if (i_2_1_s_603 < 2) {
      Y_local[((i_2_1_s_603 * 16) + 77)] = (Y_local[((i_2_1_s_603 * 16) + 77)] + (A_shared_dyn_local[(i_2_1_s_603 + 4)] * B_shared_dyn_local[13]));
    }
  }
  for (int i_2_1_s_604 = 0; i_2_1_s_604 < 4; ++i_2_1_s_604) {
    Y_local[((i_2_1_s_604 * 16) + 14)] = (Y_local[((i_2_1_s_604 * 16) + 14)] + (A_shared_dyn_local[i_2_1_s_604] * B_shared_dyn_local[14]));
  }
  for (int i_2_1_s_605 = 0; i_2_1_s_605 < 4; ++i_2_1_s_605) {
    if (i_2_1_s_605 < 2) {
      Y_local[((i_2_1_s_605 * 16) + 78)] = (Y_local[((i_2_1_s_605 * 16) + 78)] + (A_shared_dyn_local[(i_2_1_s_605 + 4)] * B_shared_dyn_local[14]));
    }
  }
  for (int i_2_1_s_606 = 0; i_2_1_s_606 < 4; ++i_2_1_s_606) {
    Y_local[((i_2_1_s_606 * 16) + 15)] = (Y_local[((i_2_1_s_606 * 16) + 15)] + (A_shared_dyn_local[i_2_1_s_606] * B_shared_dyn_local[15]));
  }
  for (int i_2_1_s_607 = 0; i_2_1_s_607 < 4; ++i_2_1_s_607) {
    if (i_2_1_s_607 < 2) {
      Y_local[((i_2_1_s_607 * 16) + 79)] = (Y_local[((i_2_1_s_607 * 16) + 79)] + (A_shared_dyn_local[(i_2_1_s_607 + 4)] * B_shared_dyn_local[15]));
    }
  }
  for (int i_2_1_s_608 = 0; i_2_1_s_608 < 4; ++i_2_1_s_608) {
    Y_local[(i_2_1_s_608 * 16)] = (Y_local[(i_2_1_s_608 * 16)] + (A_shared_dyn_local[(i_2_1_s_608 + 6)] * B_shared_dyn_local[16]));
  }
  for (int i_2_1_s_609 = 0; i_2_1_s_609 < 4; ++i_2_1_s_609) {
    if (i_2_1_s_609 < 2) {
      Y_local[((i_2_1_s_609 * 16) + 64)] = (Y_local[((i_2_1_s_609 * 16) + 64)] + (A_shared_dyn_local[(i_2_1_s_609 + 10)] * B_shared_dyn_local[16]));
    }
  }
  for (int i_2_1_s_610 = 0; i_2_1_s_610 < 4; ++i_2_1_s_610) {
    Y_local[((i_2_1_s_610 * 16) + 1)] = (Y_local[((i_2_1_s_610 * 16) + 1)] + (A_shared_dyn_local[(i_2_1_s_610 + 6)] * B_shared_dyn_local[17]));
  }
  for (int i_2_1_s_611 = 0; i_2_1_s_611 < 4; ++i_2_1_s_611) {
    if (i_2_1_s_611 < 2) {
      Y_local[((i_2_1_s_611 * 16) + 65)] = (Y_local[((i_2_1_s_611 * 16) + 65)] + (A_shared_dyn_local[(i_2_1_s_611 + 10)] * B_shared_dyn_local[17]));
    }
  }
  for (int i_2_1_s_612 = 0; i_2_1_s_612 < 4; ++i_2_1_s_612) {
    Y_local[((i_2_1_s_612 * 16) + 2)] = (Y_local[((i_2_1_s_612 * 16) + 2)] + (A_shared_dyn_local[(i_2_1_s_612 + 6)] * B_shared_dyn_local[18]));
  }
  for (int i_2_1_s_613 = 0; i_2_1_s_613 < 4; ++i_2_1_s_613) {
    if (i_2_1_s_613 < 2) {
      Y_local[((i_2_1_s_613 * 16) + 66)] = (Y_local[((i_2_1_s_613 * 16) + 66)] + (A_shared_dyn_local[(i_2_1_s_613 + 10)] * B_shared_dyn_local[18]));
    }
  }
  for (int i_2_1_s_614 = 0; i_2_1_s_614 < 4; ++i_2_1_s_614) {
    Y_local[((i_2_1_s_614 * 16) + 3)] = (Y_local[((i_2_1_s_614 * 16) + 3)] + (A_shared_dyn_local[(i_2_1_s_614 + 6)] * B_shared_dyn_local[19]));
  }
  for (int i_2_1_s_615 = 0; i_2_1_s_615 < 4; ++i_2_1_s_615) {
    if (i_2_1_s_615 < 2) {
      Y_local[((i_2_1_s_615 * 16) + 67)] = (Y_local[((i_2_1_s_615 * 16) + 67)] + (A_shared_dyn_local[(i_2_1_s_615 + 10)] * B_shared_dyn_local[19]));
    }
  }
  for (int i_2_1_s_616 = 0; i_2_1_s_616 < 4; ++i_2_1_s_616) {
    Y_local[((i_2_1_s_616 * 16) + 4)] = (Y_local[((i_2_1_s_616 * 16) + 4)] + (A_shared_dyn_local[(i_2_1_s_616 + 6)] * B_shared_dyn_local[20]));
  }
  for (int i_2_1_s_617 = 0; i_2_1_s_617 < 4; ++i_2_1_s_617) {
    if (i_2_1_s_617 < 2) {
      Y_local[((i_2_1_s_617 * 16) + 68)] = (Y_local[((i_2_1_s_617 * 16) + 68)] + (A_shared_dyn_local[(i_2_1_s_617 + 10)] * B_shared_dyn_local[20]));
    }
  }
  for (int i_2_1_s_618 = 0; i_2_1_s_618 < 4; ++i_2_1_s_618) {
    Y_local[((i_2_1_s_618 * 16) + 5)] = (Y_local[((i_2_1_s_618 * 16) + 5)] + (A_shared_dyn_local[(i_2_1_s_618 + 6)] * B_shared_dyn_local[21]));
  }
  for (int i_2_1_s_619 = 0; i_2_1_s_619 < 4; ++i_2_1_s_619) {
    if (i_2_1_s_619 < 2) {
      Y_local[((i_2_1_s_619 * 16) + 69)] = (Y_local[((i_2_1_s_619 * 16) + 69)] + (A_shared_dyn_local[(i_2_1_s_619 + 10)] * B_shared_dyn_local[21]));
    }
  }
  for (int i_2_1_s_620 = 0; i_2_1_s_620 < 4; ++i_2_1_s_620) {
    Y_local[((i_2_1_s_620 * 16) + 6)] = (Y_local[((i_2_1_s_620 * 16) + 6)] + (A_shared_dyn_local[(i_2_1_s_620 + 6)] * B_shared_dyn_local[22]));
  }
  for (int i_2_1_s_621 = 0; i_2_1_s_621 < 4; ++i_2_1_s_621) {
    if (i_2_1_s_621 < 2) {
      Y_local[((i_2_1_s_621 * 16) + 70)] = (Y_local[((i_2_1_s_621 * 16) + 70)] + (A_shared_dyn_local[(i_2_1_s_621 + 10)] * B_shared_dyn_local[22]));
    }
  }
  for (int i_2_1_s_622 = 0; i_2_1_s_622 < 4; ++i_2_1_s_622) {
    Y_local[((i_2_1_s_622 * 16) + 7)] = (Y_local[((i_2_1_s_622 * 16) + 7)] + (A_shared_dyn_local[(i_2_1_s_622 + 6)] * B_shared_dyn_local[23]));
  }
  for (int i_2_1_s_623 = 0; i_2_1_s_623 < 4; ++i_2_1_s_623) {
    if (i_2_1_s_623 < 2) {
      Y_local[((i_2_1_s_623 * 16) + 71)] = (Y_local[((i_2_1_s_623 * 16) + 71)] + (A_shared_dyn_local[(i_2_1_s_623 + 10)] * B_shared_dyn_local[23]));
    }
  }
  for (int i_2_1_s_624 = 0; i_2_1_s_624 < 4; ++i_2_1_s_624) {
    Y_local[((i_2_1_s_624 * 16) + 8)] = (Y_local[((i_2_1_s_624 * 16) + 8)] + (A_shared_dyn_local[(i_2_1_s_624 + 6)] * B_shared_dyn_local[24]));
  }
  for (int i_2_1_s_625 = 0; i_2_1_s_625 < 4; ++i_2_1_s_625) {
    if (i_2_1_s_625 < 2) {
      Y_local[((i_2_1_s_625 * 16) + 72)] = (Y_local[((i_2_1_s_625 * 16) + 72)] + (A_shared_dyn_local[(i_2_1_s_625 + 10)] * B_shared_dyn_local[24]));
    }
  }
  for (int i_2_1_s_626 = 0; i_2_1_s_626 < 4; ++i_2_1_s_626) {
    Y_local[((i_2_1_s_626 * 16) + 9)] = (Y_local[((i_2_1_s_626 * 16) + 9)] + (A_shared_dyn_local[(i_2_1_s_626 + 6)] * B_shared_dyn_local[25]));
  }
  for (int i_2_1_s_627 = 0; i_2_1_s_627 < 4; ++i_2_1_s_627) {
    if (i_2_1_s_627 < 2) {
      Y_local[((i_2_1_s_627 * 16) + 73)] = (Y_local[((i_2_1_s_627 * 16) + 73)] + (A_shared_dyn_local[(i_2_1_s_627 + 10)] * B_shared_dyn_local[25]));
    }
  }
  for (int i_2_1_s_628 = 0; i_2_1_s_628 < 4; ++i_2_1_s_628) {
    Y_local[((i_2_1_s_628 * 16) + 10)] = (Y_local[((i_2_1_s_628 * 16) + 10)] + (A_shared_dyn_local[(i_2_1_s_628 + 6)] * B_shared_dyn_local[26]));
  }
  for (int i_2_1_s_629 = 0; i_2_1_s_629 < 4; ++i_2_1_s_629) {
    if (i_2_1_s_629 < 2) {
      Y_local[((i_2_1_s_629 * 16) + 74)] = (Y_local[((i_2_1_s_629 * 16) + 74)] + (A_shared_dyn_local[(i_2_1_s_629 + 10)] * B_shared_dyn_local[26]));
    }
  }
  for (int i_2_1_s_630 = 0; i_2_1_s_630 < 4; ++i_2_1_s_630) {
    Y_local[((i_2_1_s_630 * 16) + 11)] = (Y_local[((i_2_1_s_630 * 16) + 11)] + (A_shared_dyn_local[(i_2_1_s_630 + 6)] * B_shared_dyn_local[27]));
  }
  for (int i_2_1_s_631 = 0; i_2_1_s_631 < 4; ++i_2_1_s_631) {
    if (i_2_1_s_631 < 2) {
      Y_local[((i_2_1_s_631 * 16) + 75)] = (Y_local[((i_2_1_s_631 * 16) + 75)] + (A_shared_dyn_local[(i_2_1_s_631 + 10)] * B_shared_dyn_local[27]));
    }
  }
  for (int i_2_1_s_632 = 0; i_2_1_s_632 < 4; ++i_2_1_s_632) {
    Y_local[((i_2_1_s_632 * 16) + 12)] = (Y_local[((i_2_1_s_632 * 16) + 12)] + (A_shared_dyn_local[(i_2_1_s_632 + 6)] * B_shared_dyn_local[28]));
  }
  for (int i_2_1_s_633 = 0; i_2_1_s_633 < 4; ++i_2_1_s_633) {
    if (i_2_1_s_633 < 2) {
      Y_local[((i_2_1_s_633 * 16) + 76)] = (Y_local[((i_2_1_s_633 * 16) + 76)] + (A_shared_dyn_local[(i_2_1_s_633 + 10)] * B_shared_dyn_local[28]));
    }
  }
  for (int i_2_1_s_634 = 0; i_2_1_s_634 < 4; ++i_2_1_s_634) {
    Y_local[((i_2_1_s_634 * 16) + 13)] = (Y_local[((i_2_1_s_634 * 16) + 13)] + (A_shared_dyn_local[(i_2_1_s_634 + 6)] * B_shared_dyn_local[29]));
  }
  for (int i_2_1_s_635 = 0; i_2_1_s_635 < 4; ++i_2_1_s_635) {
    if (i_2_1_s_635 < 2) {
      Y_local[((i_2_1_s_635 * 16) + 77)] = (Y_local[((i_2_1_s_635 * 16) + 77)] + (A_shared_dyn_local[(i_2_1_s_635 + 10)] * B_shared_dyn_local[29]));
    }
  }
  for (int i_2_1_s_636 = 0; i_2_1_s_636 < 4; ++i_2_1_s_636) {
    Y_local[((i_2_1_s_636 * 16) + 14)] = (Y_local[((i_2_1_s_636 * 16) + 14)] + (A_shared_dyn_local[(i_2_1_s_636 + 6)] * B_shared_dyn_local[30]));
  }
  for (int i_2_1_s_637 = 0; i_2_1_s_637 < 4; ++i_2_1_s_637) {
    if (i_2_1_s_637 < 2) {
      Y_local[((i_2_1_s_637 * 16) + 78)] = (Y_local[((i_2_1_s_637 * 16) + 78)] + (A_shared_dyn_local[(i_2_1_s_637 + 10)] * B_shared_dyn_local[30]));
    }
  }
  for (int i_2_1_s_638 = 0; i_2_1_s_638 < 4; ++i_2_1_s_638) {
    Y_local[((i_2_1_s_638 * 16) + 15)] = (Y_local[((i_2_1_s_638 * 16) + 15)] + (A_shared_dyn_local[(i_2_1_s_638 + 6)] * B_shared_dyn_local[31]));
  }
  for (int i_2_1_s_639 = 0; i_2_1_s_639 < 4; ++i_2_1_s_639) {
    if (i_2_1_s_639 < 2) {
      Y_local[((i_2_1_s_639 * 16) + 79)] = (Y_local[((i_2_1_s_639 * 16) + 79)] + (A_shared_dyn_local[(i_2_1_s_639 + 10)] * B_shared_dyn_local[31]));
    }
  }
  for (int ax1_0_20 = 0; ax1_0_20 < 4; ++ax1_0_20) {
    *(float4*)(Y + (((((((((int)blockIdx.x) >> 3) * 165888) + ((((int)threadIdx.x) / 27) * 20736)) + ((((int)threadIdx.x) % 3) * 6912)) + ((((int)blockIdx.x) & 7) * 144)) + (((((int)threadIdx.x) % 27) / 3) * 16)) + (ax1_0_20 * 4))) = *(float4*)(Y_local + (ax1_0_20 * 4));
  }
  for (int ax1_0_21 = 0; ax1_0_21 < 4; ++ax1_0_21) {
    *(float4*)(Y + ((((((((((int)blockIdx.x) >> 3) * 165888) + ((((int)threadIdx.x) / 27) * 20736)) + ((((int)threadIdx.x) % 3) * 6912)) + ((((int)blockIdx.x) & 7) * 144)) + (((((int)threadIdx.x) % 27) / 3) * 16)) + (ax1_0_21 * 4)) + 1152)) = *(float4*)(Y_local + ((ax1_0_21 * 4) + 16));
  }
  for (int ax1_0_22 = 0; ax1_0_22 < 4; ++ax1_0_22) {
    *(float4*)(Y + ((((((((((int)blockIdx.x) >> 3) * 165888) + ((((int)threadIdx.x) / 27) * 20736)) + ((((int)threadIdx.x) % 3) * 6912)) + ((((int)blockIdx.x) & 7) * 144)) + (((((int)threadIdx.x) % 27) / 3) * 16)) + (ax1_0_22 * 4)) + 2304)) = *(float4*)(Y_local + ((ax1_0_22 * 4) + 32));
  }
  for (int ax1_0_23 = 0; ax1_0_23 < 4; ++ax1_0_23) {
    *(float4*)(Y + ((((((((((int)blockIdx.x) >> 3) * 165888) + ((((int)threadIdx.x) / 27) * 20736)) + ((((int)threadIdx.x) % 3) * 6912)) + ((((int)blockIdx.x) & 7) * 144)) + (((((int)threadIdx.x) % 27) / 3) * 16)) + (ax1_0_23 * 4)) + 3456)) = *(float4*)(Y_local + ((ax1_0_23 * 4) + 48));
  }
  for (int ax1_0_24 = 0; ax1_0_24 < 4; ++ax1_0_24) {
    *(float4*)(Y + ((((((((((int)blockIdx.x) >> 3) * 165888) + ((((int)threadIdx.x) / 27) * 20736)) + ((((int)threadIdx.x) % 3) * 6912)) + ((((int)blockIdx.x) & 7) * 144)) + (((((int)threadIdx.x) % 27) / 3) * 16)) + (ax1_0_24 * 4)) + 4608)) = *(float4*)(Y_local + ((ax1_0_24 * 4) + 64));
  }
  for (int ax1_0_25 = 0; ax1_0_25 < 4; ++ax1_0_25) {
    *(float4*)(Y + ((((((((((int)blockIdx.x) >> 3) * 165888) + ((((int)threadIdx.x) / 27) * 20736)) + ((((int)threadIdx.x) % 3) * 6912)) + ((((int)blockIdx.x) & 7) * 144)) + (((((int)threadIdx.x) % 27) / 3) * 16)) + (ax1_0_25 * 4)) + 5760)) = *(float4*)(Y_local + ((ax1_0_25 * 4) + 80));
  }
}


