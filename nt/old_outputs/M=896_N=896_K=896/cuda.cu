
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
extern "C" __global__ void __launch_bounds__(112) main_kernel0(float* __restrict__ A, float* __restrict__ B, float* __restrict__ Y) {
  float Y_local[56];
  __shared__ float A_shared[1568];
  __shared__ float B_shared[3136];
  for (int i_3_init = 0; i_3_init < 4; ++i_3_init) {
    for (int j_3_init = 0; j_3_init < 2; ++j_3_init) {
      Y_local[((i_3_init * 2) + j_3_init)] = 0.000000e+00f;
      Y_local[(((i_3_init * 2) + j_3_init) + 8)] = 0.000000e+00f;
      Y_local[(((i_3_init * 2) + j_3_init) + 16)] = 0.000000e+00f;
      Y_local[(((i_3_init * 2) + j_3_init) + 24)] = 0.000000e+00f;
      Y_local[(((i_3_init * 2) + j_3_init) + 32)] = 0.000000e+00f;
      Y_local[(((i_3_init * 2) + j_3_init) + 40)] = 0.000000e+00f;
      Y_local[(((i_3_init * 2) + j_3_init) + 48)] = 0.000000e+00f;
    }
  }
  for (int k_0 = 0; k_0 < 32; ++k_0) {
    __syncthreads();
    for (int ax0_ax1_fused_0 = 0; ax0_ax1_fused_0 < 14; ++ax0_ax1_fused_0) {
      A_shared[((ax0_ax1_fused_0 * 112) + ((int)threadIdx.x))] = A[(((((k_0 * 25088) + (ax0_ax1_fused_0 * 1792)) + ((((int)threadIdx.x) / 56) * 896)) + ((((int)blockIdx.x) >> 3) * 56)) + (((int)threadIdx.x) % 56))];
    }
    for (int ax0_ax1_fused_0_1 = 0; ax0_ax1_fused_0_1 < 7; ++ax0_ax1_fused_0_1) {
      *(float4*)(B_shared + ((ax0_ax1_fused_0_1 * 448) + (((int)threadIdx.x) * 4))) = *(float4*)(B + (((((k_0 * 25088) + (ax0_ax1_fused_0_1 * 3584)) + ((((int)threadIdx.x) / 28) * 896)) + ((((int)blockIdx.x) & 7) * 112)) + ((((int)threadIdx.x) % 28) * 4)));
    }
    __syncthreads();
    for (int k_1 = 0; k_1 < 4; ++k_1) {
      for (int i_3 = 0; i_3 < 4; ++i_3) {
        for (int j_3 = 0; j_3 < 2; ++j_3) {
          for (int k_2 = 0; k_2 < 7; ++k_2) {
            Y_local[((i_3 * 2) + j_3)] = (Y_local[((i_3 * 2) + j_3)] + (A_shared[((((k_1 * 392) + (k_2 * 56)) + ((((int)threadIdx.x) >> 3) * 4)) + i_3)] * B_shared[((((k_1 * 784) + (k_2 * 112)) + ((((int)threadIdx.x) & 7) * 2)) + j_3)]));
            Y_local[(((i_3 * 2) + j_3) + 8)] = (Y_local[(((i_3 * 2) + j_3) + 8)] + (A_shared[((((k_1 * 392) + (k_2 * 56)) + ((((int)threadIdx.x) >> 3) * 4)) + i_3)] * B_shared[(((((k_1 * 784) + (k_2 * 112)) + ((((int)threadIdx.x) & 7) * 2)) + j_3) + 16)]));
            Y_local[(((i_3 * 2) + j_3) + 16)] = (Y_local[(((i_3 * 2) + j_3) + 16)] + (A_shared[((((k_1 * 392) + (k_2 * 56)) + ((((int)threadIdx.x) >> 3) * 4)) + i_3)] * B_shared[(((((k_1 * 784) + (k_2 * 112)) + ((((int)threadIdx.x) & 7) * 2)) + j_3) + 32)]));
            Y_local[(((i_3 * 2) + j_3) + 24)] = (Y_local[(((i_3 * 2) + j_3) + 24)] + (A_shared[((((k_1 * 392) + (k_2 * 56)) + ((((int)threadIdx.x) >> 3) * 4)) + i_3)] * B_shared[(((((k_1 * 784) + (k_2 * 112)) + ((((int)threadIdx.x) & 7) * 2)) + j_3) + 48)]));
            Y_local[(((i_3 * 2) + j_3) + 32)] = (Y_local[(((i_3 * 2) + j_3) + 32)] + (A_shared[((((k_1 * 392) + (k_2 * 56)) + ((((int)threadIdx.x) >> 3) * 4)) + i_3)] * B_shared[(((((k_1 * 784) + (k_2 * 112)) + ((((int)threadIdx.x) & 7) * 2)) + j_3) + 64)]));
            Y_local[(((i_3 * 2) + j_3) + 40)] = (Y_local[(((i_3 * 2) + j_3) + 40)] + (A_shared[((((k_1 * 392) + (k_2 * 56)) + ((((int)threadIdx.x) >> 3) * 4)) + i_3)] * B_shared[(((((k_1 * 784) + (k_2 * 112)) + ((((int)threadIdx.x) & 7) * 2)) + j_3) + 80)]));
            Y_local[(((i_3 * 2) + j_3) + 48)] = (Y_local[(((i_3 * 2) + j_3) + 48)] + (A_shared[((((k_1 * 392) + (k_2 * 56)) + ((((int)threadIdx.x) >> 3) * 4)) + i_3)] * B_shared[(((((k_1 * 784) + (k_2 * 112)) + ((((int)threadIdx.x) & 7) * 2)) + j_3) + 96)]));
          }
        }
      }
    }
  }
  for (int ax0 = 0; ax0 < 4; ++ax0) {
    for (int ax1 = 0; ax1 < 2; ++ax1) {
      Y[(((((((((int)blockIdx.x) >> 3) * 50176) + ((((int)threadIdx.x) >> 3) * 3584)) + (ax0 * 896)) + ((((int)blockIdx.x) & 7) * 112)) + ((((int)threadIdx.x) & 7) * 2)) + ax1)] = Y_local[((ax0 * 2) + ax1)];
      Y[((((((((((int)blockIdx.x) >> 3) * 50176) + ((((int)threadIdx.x) >> 3) * 3584)) + (ax0 * 896)) + ((((int)blockIdx.x) & 7) * 112)) + ((((int)threadIdx.x) & 7) * 2)) + ax1) + 16)] = Y_local[(((ax0 * 2) + ax1) + 8)];
      Y[((((((((((int)blockIdx.x) >> 3) * 50176) + ((((int)threadIdx.x) >> 3) * 3584)) + (ax0 * 896)) + ((((int)blockIdx.x) & 7) * 112)) + ((((int)threadIdx.x) & 7) * 2)) + ax1) + 32)] = Y_local[(((ax0 * 2) + ax1) + 16)];
      Y[((((((((((int)blockIdx.x) >> 3) * 50176) + ((((int)threadIdx.x) >> 3) * 3584)) + (ax0 * 896)) + ((((int)blockIdx.x) & 7) * 112)) + ((((int)threadIdx.x) & 7) * 2)) + ax1) + 48)] = Y_local[(((ax0 * 2) + ax1) + 24)];
      Y[((((((((((int)blockIdx.x) >> 3) * 50176) + ((((int)threadIdx.x) >> 3) * 3584)) + (ax0 * 896)) + ((((int)blockIdx.x) & 7) * 112)) + ((((int)threadIdx.x) & 7) * 2)) + ax1) + 64)] = Y_local[(((ax0 * 2) + ax1) + 32)];
      Y[((((((((((int)blockIdx.x) >> 3) * 50176) + ((((int)threadIdx.x) >> 3) * 3584)) + (ax0 * 896)) + ((((int)blockIdx.x) & 7) * 112)) + ((((int)threadIdx.x) & 7) * 2)) + ax1) + 80)] = Y_local[(((ax0 * 2) + ax1) + 40)];
      Y[((((((((((int)blockIdx.x) >> 3) * 50176) + ((((int)threadIdx.x) >> 3) * 3584)) + (ax0 * 896)) + ((((int)blockIdx.x) & 7) * 112)) + ((((int)threadIdx.x) & 7) * 2)) + ax1) + 96)] = Y_local[(((ax0 * 2) + ax1) + 48)];
    }
  }
}


