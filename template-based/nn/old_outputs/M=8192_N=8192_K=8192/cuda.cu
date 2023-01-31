
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
  float Y_local[128];
  __shared__ float A_shared[2048];
  __shared__ float B_shared[2048];
  for (int i_3_init = 0; i_3_init < 2; ++i_3_init) {
    for (int j_3_init = 0; j_3_init < 2; ++j_3_init) {
      for (int i_4_init = 0; i_4_init < 4; ++i_4_init) {
        Y_local[(((i_3_init * 8) + (i_4_init * 2)) + j_3_init)] = 0.000000e+00f;
        Y_local[((((i_3_init * 8) + (i_4_init * 2)) + j_3_init) + 16)] = 0.000000e+00f;
        Y_local[((((i_3_init * 8) + (i_4_init * 2)) + j_3_init) + 32)] = 0.000000e+00f;
        Y_local[((((i_3_init * 8) + (i_4_init * 2)) + j_3_init) + 48)] = 0.000000e+00f;
        Y_local[((((i_3_init * 8) + (i_4_init * 2)) + j_3_init) + 64)] = 0.000000e+00f;
        Y_local[((((i_3_init * 8) + (i_4_init * 2)) + j_3_init) + 80)] = 0.000000e+00f;
        Y_local[((((i_3_init * 8) + (i_4_init * 2)) + j_3_init) + 96)] = 0.000000e+00f;
        Y_local[((((i_3_init * 8) + (i_4_init * 2)) + j_3_init) + 112)] = 0.000000e+00f;
      }
    }
  }
  for (int k_0 = 0; k_0 < 512; ++k_0) {
    __syncthreads();
    *(float4*)(A_shared + (((int)threadIdx.x) * 4)) = *(float4*)(A + (((((((int)blockIdx.x) >> 6) * 1048576) + ((((int)threadIdx.x) >> 2) * 8192)) + (k_0 * 16)) + ((((int)threadIdx.x) & 3) * 4)));
    *(float4*)(A_shared + ((((int)threadIdx.x) * 4) + 512)) = *(float4*)(A + ((((((((int)blockIdx.x) >> 6) * 1048576) + ((((int)threadIdx.x) >> 2) * 8192)) + (k_0 * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 262144));
    *(float4*)(A_shared + ((((int)threadIdx.x) * 4) + 1024)) = *(float4*)(A + ((((((((int)blockIdx.x) >> 6) * 1048576) + ((((int)threadIdx.x) >> 2) * 8192)) + (k_0 * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 524288));
    *(float4*)(A_shared + ((((int)threadIdx.x) * 4) + 1536)) = *(float4*)(A + ((((((((int)blockIdx.x) >> 6) * 1048576) + ((((int)threadIdx.x) >> 2) * 8192)) + (k_0 * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 786432));
    *(float4*)(B_shared + (((int)threadIdx.x) * 4)) = *(float4*)(B + ((((k_0 * 131072) + ((((int)threadIdx.x) >> 5) * 8192)) + ((((int)blockIdx.x) & 63) * 128)) + ((((int)threadIdx.x) & 31) * 4)));
    *(float4*)(B_shared + ((((int)threadIdx.x) * 4) + 512)) = *(float4*)(B + (((((k_0 * 131072) + ((((int)threadIdx.x) >> 5) * 8192)) + ((((int)blockIdx.x) & 63) * 128)) + ((((int)threadIdx.x) & 31) * 4)) + 32768));
    *(float4*)(B_shared + ((((int)threadIdx.x) * 4) + 1024)) = *(float4*)(B + (((((k_0 * 131072) + ((((int)threadIdx.x) >> 5) * 8192)) + ((((int)blockIdx.x) & 63) * 128)) + ((((int)threadIdx.x) & 31) * 4)) + 65536));
    *(float4*)(B_shared + ((((int)threadIdx.x) * 4) + 1536)) = *(float4*)(B + (((((k_0 * 131072) + ((((int)threadIdx.x) >> 5) * 8192)) + ((((int)blockIdx.x) & 63) * 128)) + ((((int)threadIdx.x) & 31) * 4)) + 98304));
    __syncthreads();
    for (int k_1 = 0; k_1 < 4; ++k_1) {
      for (int i_3 = 0; i_3 < 2; ++i_3) {
        for (int j_3 = 0; j_3 < 2; ++j_3) {
          for (int k_2 = 0; k_2 < 4; ++k_2) {
            for (int i_4 = 0; i_4 < 4; ++i_4) {
              Y_local[(((i_3 * 8) + (i_4 * 2)) + j_3)] = (Y_local[(((i_3 * 8) + (i_4 * 2)) + j_3)] + (A_shared[((((((((int)threadIdx.x) >> 4) * 128) + (i_3 * 64)) + (i_4 * 16)) + (k_1 * 4)) + k_2)] * B_shared[((((k_1 * 512) + (k_2 * 128)) + ((((int)threadIdx.x) & 15) * 2)) + j_3)]));
              Y_local[((((i_3 * 8) + (i_4 * 2)) + j_3) + 16)] = (Y_local[((((i_3 * 8) + (i_4 * 2)) + j_3) + 16)] + (A_shared[((((((((int)threadIdx.x) >> 4) * 128) + (i_3 * 64)) + (i_4 * 16)) + (k_1 * 4)) + k_2)] * B_shared[(((((k_1 * 512) + (k_2 * 128)) + ((((int)threadIdx.x) & 15) * 2)) + j_3) + 32)]));
              Y_local[((((i_3 * 8) + (i_4 * 2)) + j_3) + 32)] = (Y_local[((((i_3 * 8) + (i_4 * 2)) + j_3) + 32)] + (A_shared[((((((((int)threadIdx.x) >> 4) * 128) + (i_3 * 64)) + (i_4 * 16)) + (k_1 * 4)) + k_2)] * B_shared[(((((k_1 * 512) + (k_2 * 128)) + ((((int)threadIdx.x) & 15) * 2)) + j_3) + 64)]));
              Y_local[((((i_3 * 8) + (i_4 * 2)) + j_3) + 48)] = (Y_local[((((i_3 * 8) + (i_4 * 2)) + j_3) + 48)] + (A_shared[((((((((int)threadIdx.x) >> 4) * 128) + (i_3 * 64)) + (i_4 * 16)) + (k_1 * 4)) + k_2)] * B_shared[(((((k_1 * 512) + (k_2 * 128)) + ((((int)threadIdx.x) & 15) * 2)) + j_3) + 96)]));
              Y_local[((((i_3 * 8) + (i_4 * 2)) + j_3) + 64)] = (Y_local[((((i_3 * 8) + (i_4 * 2)) + j_3) + 64)] + (A_shared[(((((((((int)threadIdx.x) >> 4) * 128) + (i_3 * 64)) + (i_4 * 16)) + (k_1 * 4)) + k_2) + 1024)] * B_shared[((((k_1 * 512) + (k_2 * 128)) + ((((int)threadIdx.x) & 15) * 2)) + j_3)]));
              Y_local[((((i_3 * 8) + (i_4 * 2)) + j_3) + 80)] = (Y_local[((((i_3 * 8) + (i_4 * 2)) + j_3) + 80)] + (A_shared[(((((((((int)threadIdx.x) >> 4) * 128) + (i_3 * 64)) + (i_4 * 16)) + (k_1 * 4)) + k_2) + 1024)] * B_shared[(((((k_1 * 512) + (k_2 * 128)) + ((((int)threadIdx.x) & 15) * 2)) + j_3) + 32)]));
              Y_local[((((i_3 * 8) + (i_4 * 2)) + j_3) + 96)] = (Y_local[((((i_3 * 8) + (i_4 * 2)) + j_3) + 96)] + (A_shared[(((((((((int)threadIdx.x) >> 4) * 128) + (i_3 * 64)) + (i_4 * 16)) + (k_1 * 4)) + k_2) + 1024)] * B_shared[(((((k_1 * 512) + (k_2 * 128)) + ((((int)threadIdx.x) & 15) * 2)) + j_3) + 64)]));
              Y_local[((((i_3 * 8) + (i_4 * 2)) + j_3) + 112)] = (Y_local[((((i_3 * 8) + (i_4 * 2)) + j_3) + 112)] + (A_shared[(((((((((int)threadIdx.x) >> 4) * 128) + (i_3 * 64)) + (i_4 * 16)) + (k_1 * 4)) + k_2) + 1024)] * B_shared[(((((k_1 * 512) + (k_2 * 128)) + ((((int)threadIdx.x) & 15) * 2)) + j_3) + 96)]));
            }
          }
        }
      }
    }
  }
  for (int ax0 = 0; ax0 < 8; ++ax0) {
    Y[((((((((int)blockIdx.x) >> 6) * 1048576) + ((((int)threadIdx.x) >> 4) * 65536)) + (ax0 * 8192)) + ((((int)blockIdx.x) & 63) * 128)) + ((((int)threadIdx.x) & 15) * 2))] = Y_local[(ax0 * 2)];
    Y[(((((((((int)blockIdx.x) >> 6) * 1048576) + ((((int)threadIdx.x) >> 4) * 65536)) + (ax0 * 8192)) + ((((int)blockIdx.x) & 63) * 128)) + ((((int)threadIdx.x) & 15) * 2)) + 32)] = Y_local[((ax0 * 2) + 16)];
    Y[(((((((((int)blockIdx.x) >> 6) * 1048576) + ((((int)threadIdx.x) >> 4) * 65536)) + (ax0 * 8192)) + ((((int)blockIdx.x) & 63) * 128)) + ((((int)threadIdx.x) & 15) * 2)) + 64)] = Y_local[((ax0 * 2) + 32)];
    Y[(((((((((int)blockIdx.x) >> 6) * 1048576) + ((((int)threadIdx.x) >> 4) * 65536)) + (ax0 * 8192)) + ((((int)blockIdx.x) & 63) * 128)) + ((((int)threadIdx.x) & 15) * 2)) + 96)] = Y_local[((ax0 * 2) + 48)];
    Y[(((((((((int)blockIdx.x) >> 6) * 1048576) + ((((int)threadIdx.x) >> 4) * 65536)) + (ax0 * 8192)) + ((((int)blockIdx.x) & 63) * 128)) + ((((int)threadIdx.x) & 15) * 2)) + 524288)] = Y_local[((ax0 * 2) + 64)];
    Y[(((((((((int)blockIdx.x) >> 6) * 1048576) + ((((int)threadIdx.x) >> 4) * 65536)) + (ax0 * 8192)) + ((((int)blockIdx.x) & 63) * 128)) + ((((int)threadIdx.x) & 15) * 2)) + 524320)] = Y_local[((ax0 * 2) + 80)];
    Y[(((((((((int)blockIdx.x) >> 6) * 1048576) + ((((int)threadIdx.x) >> 4) * 65536)) + (ax0 * 8192)) + ((((int)blockIdx.x) & 63) * 128)) + ((((int)threadIdx.x) & 15) * 2)) + 524352)] = Y_local[((ax0 * 2) + 96)];
    Y[(((((((((int)blockIdx.x) >> 6) * 1048576) + ((((int)threadIdx.x) >> 4) * 65536)) + (ax0 * 8192)) + ((((int)blockIdx.x) & 63) * 128)) + ((((int)threadIdx.x) & 15) * 2)) + 524384)] = Y_local[((ax0 * 2) + 112)];
    Y[(((((((((int)blockIdx.x) >> 6) * 1048576) + ((((int)threadIdx.x) >> 4) * 65536)) + (ax0 * 8192)) + ((((int)blockIdx.x) & 63) * 128)) + ((((int)threadIdx.x) & 15) * 2)) + 1)] = Y_local[((ax0 * 2) + 1)];
    Y[(((((((((int)blockIdx.x) >> 6) * 1048576) + ((((int)threadIdx.x) >> 4) * 65536)) + (ax0 * 8192)) + ((((int)blockIdx.x) & 63) * 128)) + ((((int)threadIdx.x) & 15) * 2)) + 33)] = Y_local[((ax0 * 2) + 17)];
    Y[(((((((((int)blockIdx.x) >> 6) * 1048576) + ((((int)threadIdx.x) >> 4) * 65536)) + (ax0 * 8192)) + ((((int)blockIdx.x) & 63) * 128)) + ((((int)threadIdx.x) & 15) * 2)) + 65)] = Y_local[((ax0 * 2) + 33)];
    Y[(((((((((int)blockIdx.x) >> 6) * 1048576) + ((((int)threadIdx.x) >> 4) * 65536)) + (ax0 * 8192)) + ((((int)blockIdx.x) & 63) * 128)) + ((((int)threadIdx.x) & 15) * 2)) + 97)] = Y_local[((ax0 * 2) + 49)];
    Y[(((((((((int)blockIdx.x) >> 6) * 1048576) + ((((int)threadIdx.x) >> 4) * 65536)) + (ax0 * 8192)) + ((((int)blockIdx.x) & 63) * 128)) + ((((int)threadIdx.x) & 15) * 2)) + 524289)] = Y_local[((ax0 * 2) + 65)];
    Y[(((((((((int)blockIdx.x) >> 6) * 1048576) + ((((int)threadIdx.x) >> 4) * 65536)) + (ax0 * 8192)) + ((((int)blockIdx.x) & 63) * 128)) + ((((int)threadIdx.x) & 15) * 2)) + 524321)] = Y_local[((ax0 * 2) + 81)];
    Y[(((((((((int)blockIdx.x) >> 6) * 1048576) + ((((int)threadIdx.x) >> 4) * 65536)) + (ax0 * 8192)) + ((((int)blockIdx.x) & 63) * 128)) + ((((int)threadIdx.x) & 15) * 2)) + 524353)] = Y_local[((ax0 * 2) + 97)];
    Y[(((((((((int)blockIdx.x) >> 6) * 1048576) + ((((int)threadIdx.x) >> 4) * 65536)) + (ax0 * 8192)) + ((((int)blockIdx.x) & 63) * 128)) + ((((int)threadIdx.x) & 15) * 2)) + 524385)] = Y_local[((ax0 * 2) + 113)];
  }
}


