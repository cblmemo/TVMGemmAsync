
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
  float Y_local[96];
  __shared__ float A_shared[768];
  __shared__ float B_shared[4096];
  for (int i_3_init = 0; i_3_init < 12; ++i_3_init) {
    Y_local[(i_3_init * 4)] = 0.000000e+00f;
    Y_local[((i_3_init * 4) + 48)] = 0.000000e+00f;
    Y_local[((i_3_init * 4) + 1)] = 0.000000e+00f;
    Y_local[((i_3_init * 4) + 49)] = 0.000000e+00f;
    Y_local[((i_3_init * 4) + 2)] = 0.000000e+00f;
    Y_local[((i_3_init * 4) + 50)] = 0.000000e+00f;
    Y_local[((i_3_init * 4) + 3)] = 0.000000e+00f;
    Y_local[((i_3_init * 4) + 51)] = 0.000000e+00f;
  }
  for (int k_0 = 0; k_0 < 96; ++k_0) {
    __syncthreads();
    *(float2*)(A_shared + (((int)threadIdx.x) * 2)) = *(float2*)(A + ((((k_0 * 24576) + ((((int)threadIdx.x) / 24) * 1536)) + ((((int)blockIdx.x) / 6) * 48)) + ((((int)threadIdx.x) % 24) * 2)));
    *(float2*)(A_shared + ((((int)threadIdx.x) * 2) + 256)) = *(float2*)(A + ((((k_0 * 24576) + ((((((int)threadIdx.x) * 2) + 256) / 48) * 1536)) + ((((int)blockIdx.x) / 6) * 48)) + (((((int)threadIdx.x) * 2) + 16) % 48)));
    *(float2*)(A_shared + ((((int)threadIdx.x) * 2) + 512)) = *(float2*)(A + ((((k_0 * 24576) + ((((((int)threadIdx.x) * 2) + 512) / 48) * 1536)) + ((((int)blockIdx.x) / 6) * 48)) + (((((int)threadIdx.x) * 2) + 32) % 48)));
    *(float4*)(B_shared + (((int)threadIdx.x) * 4)) = *(float4*)(B + ((((k_0 * 24576) + ((((int)threadIdx.x) >> 6) * 1536)) + ((((int)blockIdx.x) % 6) * 256)) + ((((int)threadIdx.x) & 63) * 4)));
    *(float4*)(B_shared + ((((int)threadIdx.x) * 4) + 512)) = *(float4*)(B + (((((k_0 * 24576) + ((((int)threadIdx.x) >> 6) * 1536)) + ((((int)blockIdx.x) % 6) * 256)) + ((((int)threadIdx.x) & 63) * 4)) + 3072));
    *(float4*)(B_shared + ((((int)threadIdx.x) * 4) + 1024)) = *(float4*)(B + (((((k_0 * 24576) + ((((int)threadIdx.x) >> 6) * 1536)) + ((((int)blockIdx.x) % 6) * 256)) + ((((int)threadIdx.x) & 63) * 4)) + 6144));
    *(float4*)(B_shared + ((((int)threadIdx.x) * 4) + 1536)) = *(float4*)(B + (((((k_0 * 24576) + ((((int)threadIdx.x) >> 6) * 1536)) + ((((int)blockIdx.x) % 6) * 256)) + ((((int)threadIdx.x) & 63) * 4)) + 9216));
    *(float4*)(B_shared + ((((int)threadIdx.x) * 4) + 2048)) = *(float4*)(B + (((((k_0 * 24576) + ((((int)threadIdx.x) >> 6) * 1536)) + ((((int)blockIdx.x) % 6) * 256)) + ((((int)threadIdx.x) & 63) * 4)) + 12288));
    *(float4*)(B_shared + ((((int)threadIdx.x) * 4) + 2560)) = *(float4*)(B + (((((k_0 * 24576) + ((((int)threadIdx.x) >> 6) * 1536)) + ((((int)blockIdx.x) % 6) * 256)) + ((((int)threadIdx.x) & 63) * 4)) + 15360));
    *(float4*)(B_shared + ((((int)threadIdx.x) * 4) + 3072)) = *(float4*)(B + (((((k_0 * 24576) + ((((int)threadIdx.x) >> 6) * 1536)) + ((((int)blockIdx.x) % 6) * 256)) + ((((int)threadIdx.x) & 63) * 4)) + 18432));
    *(float4*)(B_shared + ((((int)threadIdx.x) * 4) + 3584)) = *(float4*)(B + (((((k_0 * 24576) + ((((int)threadIdx.x) >> 6) * 1536)) + ((((int)blockIdx.x) % 6) * 256)) + ((((int)threadIdx.x) & 63) * 4)) + 21504));
    __syncthreads();
    for (int k_1 = 0; k_1 < 16; ++k_1) {
      for (int i_3 = 0; i_3 < 12; ++i_3) {
        Y_local[(i_3 * 4)] = (Y_local[(i_3 * 4)] + (A_shared[(((k_1 * 48) + ((((int)threadIdx.x) >> 5) * 12)) + i_3)] * B_shared[((k_1 * 256) + ((((int)threadIdx.x) & 31) * 4))]));
        Y_local[((i_3 * 4) + 48)] = (Y_local[((i_3 * 4) + 48)] + (A_shared[(((k_1 * 48) + ((((int)threadIdx.x) >> 5) * 12)) + i_3)] * B_shared[(((k_1 * 256) + ((((int)threadIdx.x) & 31) * 4)) + 128)]));
        Y_local[((i_3 * 4) + 1)] = (Y_local[((i_3 * 4) + 1)] + (A_shared[(((k_1 * 48) + ((((int)threadIdx.x) >> 5) * 12)) + i_3)] * B_shared[(((k_1 * 256) + ((((int)threadIdx.x) & 31) * 4)) + 1)]));
        Y_local[((i_3 * 4) + 49)] = (Y_local[((i_3 * 4) + 49)] + (A_shared[(((k_1 * 48) + ((((int)threadIdx.x) >> 5) * 12)) + i_3)] * B_shared[(((k_1 * 256) + ((((int)threadIdx.x) & 31) * 4)) + 129)]));
        Y_local[((i_3 * 4) + 2)] = (Y_local[((i_3 * 4) + 2)] + (A_shared[(((k_1 * 48) + ((((int)threadIdx.x) >> 5) * 12)) + i_3)] * B_shared[(((k_1 * 256) + ((((int)threadIdx.x) & 31) * 4)) + 2)]));
        Y_local[((i_3 * 4) + 50)] = (Y_local[((i_3 * 4) + 50)] + (A_shared[(((k_1 * 48) + ((((int)threadIdx.x) >> 5) * 12)) + i_3)] * B_shared[(((k_1 * 256) + ((((int)threadIdx.x) & 31) * 4)) + 130)]));
        Y_local[((i_3 * 4) + 3)] = (Y_local[((i_3 * 4) + 3)] + (A_shared[(((k_1 * 48) + ((((int)threadIdx.x) >> 5) * 12)) + i_3)] * B_shared[(((k_1 * 256) + ((((int)threadIdx.x) & 31) * 4)) + 3)]));
        Y_local[((i_3 * 4) + 51)] = (Y_local[((i_3 * 4) + 51)] + (A_shared[(((k_1 * 48) + ((((int)threadIdx.x) >> 5) * 12)) + i_3)] * B_shared[(((k_1 * 256) + ((((int)threadIdx.x) & 31) * 4)) + 131)]));
      }
    }
  }
  for (int ax0 = 0; ax0 < 12; ++ax0) {
    Y[((((((((int)blockIdx.x) / 6) * 73728) + ((((int)threadIdx.x) >> 5) * 18432)) + (ax0 * 1536)) + ((((int)blockIdx.x) % 6) * 256)) + ((((int)threadIdx.x) & 31) * 4))] = Y_local[(ax0 * 4)];
    Y[(((((((((int)blockIdx.x) / 6) * 73728) + ((((int)threadIdx.x) >> 5) * 18432)) + (ax0 * 1536)) + ((((int)blockIdx.x) % 6) * 256)) + ((((int)threadIdx.x) & 31) * 4)) + 128)] = Y_local[((ax0 * 4) + 48)];
    Y[(((((((((int)blockIdx.x) / 6) * 73728) + ((((int)threadIdx.x) >> 5) * 18432)) + (ax0 * 1536)) + ((((int)blockIdx.x) % 6) * 256)) + ((((int)threadIdx.x) & 31) * 4)) + 1)] = Y_local[((ax0 * 4) + 1)];
    Y[(((((((((int)blockIdx.x) / 6) * 73728) + ((((int)threadIdx.x) >> 5) * 18432)) + (ax0 * 1536)) + ((((int)blockIdx.x) % 6) * 256)) + ((((int)threadIdx.x) & 31) * 4)) + 129)] = Y_local[((ax0 * 4) + 49)];
    Y[(((((((((int)blockIdx.x) / 6) * 73728) + ((((int)threadIdx.x) >> 5) * 18432)) + (ax0 * 1536)) + ((((int)blockIdx.x) % 6) * 256)) + ((((int)threadIdx.x) & 31) * 4)) + 2)] = Y_local[((ax0 * 4) + 2)];
    Y[(((((((((int)blockIdx.x) / 6) * 73728) + ((((int)threadIdx.x) >> 5) * 18432)) + (ax0 * 1536)) + ((((int)blockIdx.x) % 6) * 256)) + ((((int)threadIdx.x) & 31) * 4)) + 130)] = Y_local[((ax0 * 4) + 50)];
    Y[(((((((((int)blockIdx.x) / 6) * 73728) + ((((int)threadIdx.x) >> 5) * 18432)) + (ax0 * 1536)) + ((((int)blockIdx.x) % 6) * 256)) + ((((int)threadIdx.x) & 31) * 4)) + 3)] = Y_local[((ax0 * 4) + 3)];
    Y[(((((((((int)blockIdx.x) / 6) * 73728) + ((((int)threadIdx.x) >> 5) * 18432)) + (ax0 * 1536)) + ((((int)blockIdx.x) % 6) * 256)) + ((((int)threadIdx.x) & 31) * 4)) + 131)] = Y_local[((ax0 * 4) + 51)];
  }
}


