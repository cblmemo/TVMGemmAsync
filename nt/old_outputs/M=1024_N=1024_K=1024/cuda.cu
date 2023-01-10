
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
  float Y_local[64];
  __shared__ float A_shared[4096];
  __shared__ float B_shared[2048];
  Y_local[0] = 0.000000e+00f;
  Y_local[32] = 0.000000e+00f;
  Y_local[1] = 0.000000e+00f;
  Y_local[33] = 0.000000e+00f;
  Y_local[2] = 0.000000e+00f;
  Y_local[34] = 0.000000e+00f;
  Y_local[3] = 0.000000e+00f;
  Y_local[35] = 0.000000e+00f;
  Y_local[4] = 0.000000e+00f;
  Y_local[36] = 0.000000e+00f;
  Y_local[5] = 0.000000e+00f;
  Y_local[37] = 0.000000e+00f;
  Y_local[6] = 0.000000e+00f;
  Y_local[38] = 0.000000e+00f;
  Y_local[7] = 0.000000e+00f;
  Y_local[39] = 0.000000e+00f;
  Y_local[8] = 0.000000e+00f;
  Y_local[40] = 0.000000e+00f;
  Y_local[9] = 0.000000e+00f;
  Y_local[41] = 0.000000e+00f;
  Y_local[10] = 0.000000e+00f;
  Y_local[42] = 0.000000e+00f;
  Y_local[11] = 0.000000e+00f;
  Y_local[43] = 0.000000e+00f;
  Y_local[12] = 0.000000e+00f;
  Y_local[44] = 0.000000e+00f;
  Y_local[13] = 0.000000e+00f;
  Y_local[45] = 0.000000e+00f;
  Y_local[14] = 0.000000e+00f;
  Y_local[46] = 0.000000e+00f;
  Y_local[15] = 0.000000e+00f;
  Y_local[47] = 0.000000e+00f;
  Y_local[16] = 0.000000e+00f;
  Y_local[48] = 0.000000e+00f;
  Y_local[17] = 0.000000e+00f;
  Y_local[49] = 0.000000e+00f;
  Y_local[18] = 0.000000e+00f;
  Y_local[50] = 0.000000e+00f;
  Y_local[19] = 0.000000e+00f;
  Y_local[51] = 0.000000e+00f;
  Y_local[20] = 0.000000e+00f;
  Y_local[52] = 0.000000e+00f;
  Y_local[21] = 0.000000e+00f;
  Y_local[53] = 0.000000e+00f;
  Y_local[22] = 0.000000e+00f;
  Y_local[54] = 0.000000e+00f;
  Y_local[23] = 0.000000e+00f;
  Y_local[55] = 0.000000e+00f;
  Y_local[24] = 0.000000e+00f;
  Y_local[56] = 0.000000e+00f;
  Y_local[25] = 0.000000e+00f;
  Y_local[57] = 0.000000e+00f;
  Y_local[26] = 0.000000e+00f;
  Y_local[58] = 0.000000e+00f;
  Y_local[27] = 0.000000e+00f;
  Y_local[59] = 0.000000e+00f;
  Y_local[28] = 0.000000e+00f;
  Y_local[60] = 0.000000e+00f;
  Y_local[29] = 0.000000e+00f;
  Y_local[61] = 0.000000e+00f;
  Y_local[30] = 0.000000e+00f;
  Y_local[62] = 0.000000e+00f;
  Y_local[31] = 0.000000e+00f;
  Y_local[63] = 0.000000e+00f;
  for (int k_0 = 0; k_0 < 32; ++k_0) {
    __syncthreads();
    *(float2*)(A_shared + (((int)threadIdx.x) * 2)) = *(float2*)(A + ((((k_0 * 32768) + ((((int)threadIdx.x) >> 6) * 1024)) + ((((int)blockIdx.x) >> 4) * 128)) + ((((int)threadIdx.x) & 63) * 2)));
    *(float2*)(A_shared + ((((int)threadIdx.x) * 2) + 256)) = *(float2*)(A + (((((k_0 * 32768) + ((((int)threadIdx.x) >> 6) * 1024)) + ((((int)blockIdx.x) >> 4) * 128)) + ((((int)threadIdx.x) & 63) * 2)) + 2048));
    *(float2*)(A_shared + ((((int)threadIdx.x) * 2) + 512)) = *(float2*)(A + (((((k_0 * 32768) + ((((int)threadIdx.x) >> 6) * 1024)) + ((((int)blockIdx.x) >> 4) * 128)) + ((((int)threadIdx.x) & 63) * 2)) + 4096));
    *(float2*)(A_shared + ((((int)threadIdx.x) * 2) + 768)) = *(float2*)(A + (((((k_0 * 32768) + ((((int)threadIdx.x) >> 6) * 1024)) + ((((int)blockIdx.x) >> 4) * 128)) + ((((int)threadIdx.x) & 63) * 2)) + 6144));
    *(float2*)(A_shared + ((((int)threadIdx.x) * 2) + 1024)) = *(float2*)(A + (((((k_0 * 32768) + ((((int)threadIdx.x) >> 6) * 1024)) + ((((int)blockIdx.x) >> 4) * 128)) + ((((int)threadIdx.x) & 63) * 2)) + 8192));
    *(float2*)(A_shared + ((((int)threadIdx.x) * 2) + 1280)) = *(float2*)(A + (((((k_0 * 32768) + ((((int)threadIdx.x) >> 6) * 1024)) + ((((int)blockIdx.x) >> 4) * 128)) + ((((int)threadIdx.x) & 63) * 2)) + 10240));
    *(float2*)(A_shared + ((((int)threadIdx.x) * 2) + 1536)) = *(float2*)(A + (((((k_0 * 32768) + ((((int)threadIdx.x) >> 6) * 1024)) + ((((int)blockIdx.x) >> 4) * 128)) + ((((int)threadIdx.x) & 63) * 2)) + 12288));
    *(float2*)(A_shared + ((((int)threadIdx.x) * 2) + 1792)) = *(float2*)(A + (((((k_0 * 32768) + ((((int)threadIdx.x) >> 6) * 1024)) + ((((int)blockIdx.x) >> 4) * 128)) + ((((int)threadIdx.x) & 63) * 2)) + 14336));
    *(float2*)(A_shared + ((((int)threadIdx.x) * 2) + 2048)) = *(float2*)(A + (((((k_0 * 32768) + ((((int)threadIdx.x) >> 6) * 1024)) + ((((int)blockIdx.x) >> 4) * 128)) + ((((int)threadIdx.x) & 63) * 2)) + 16384));
    *(float2*)(A_shared + ((((int)threadIdx.x) * 2) + 2304)) = *(float2*)(A + (((((k_0 * 32768) + ((((int)threadIdx.x) >> 6) * 1024)) + ((((int)blockIdx.x) >> 4) * 128)) + ((((int)threadIdx.x) & 63) * 2)) + 18432));
    *(float2*)(A_shared + ((((int)threadIdx.x) * 2) + 2560)) = *(float2*)(A + (((((k_0 * 32768) + ((((int)threadIdx.x) >> 6) * 1024)) + ((((int)blockIdx.x) >> 4) * 128)) + ((((int)threadIdx.x) & 63) * 2)) + 20480));
    *(float2*)(A_shared + ((((int)threadIdx.x) * 2) + 2816)) = *(float2*)(A + (((((k_0 * 32768) + ((((int)threadIdx.x) >> 6) * 1024)) + ((((int)blockIdx.x) >> 4) * 128)) + ((((int)threadIdx.x) & 63) * 2)) + 22528));
    *(float2*)(A_shared + ((((int)threadIdx.x) * 2) + 3072)) = *(float2*)(A + (((((k_0 * 32768) + ((((int)threadIdx.x) >> 6) * 1024)) + ((((int)blockIdx.x) >> 4) * 128)) + ((((int)threadIdx.x) & 63) * 2)) + 24576));
    *(float2*)(A_shared + ((((int)threadIdx.x) * 2) + 3328)) = *(float2*)(A + (((((k_0 * 32768) + ((((int)threadIdx.x) >> 6) * 1024)) + ((((int)blockIdx.x) >> 4) * 128)) + ((((int)threadIdx.x) & 63) * 2)) + 26624));
    *(float2*)(A_shared + ((((int)threadIdx.x) * 2) + 3584)) = *(float2*)(A + (((((k_0 * 32768) + ((((int)threadIdx.x) >> 6) * 1024)) + ((((int)blockIdx.x) >> 4) * 128)) + ((((int)threadIdx.x) & 63) * 2)) + 28672));
    *(float2*)(A_shared + ((((int)threadIdx.x) * 2) + 3840)) = *(float2*)(A + (((((k_0 * 32768) + ((((int)threadIdx.x) >> 6) * 1024)) + ((((int)blockIdx.x) >> 4) * 128)) + ((((int)threadIdx.x) & 63) * 2)) + 30720));
    *(float2*)(B_shared + (((int)threadIdx.x) * 2)) = *(float2*)(B + ((((k_0 * 32768) + ((((int)threadIdx.x) >> 5) * 1024)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 31) * 2)));
    *(float2*)(B_shared + ((((int)threadIdx.x) * 2) + 256)) = *(float2*)(B + (((((k_0 * 32768) + ((((int)threadIdx.x) >> 5) * 1024)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 31) * 2)) + 4096));
    *(float2*)(B_shared + ((((int)threadIdx.x) * 2) + 512)) = *(float2*)(B + (((((k_0 * 32768) + ((((int)threadIdx.x) >> 5) * 1024)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 31) * 2)) + 8192));
    *(float2*)(B_shared + ((((int)threadIdx.x) * 2) + 768)) = *(float2*)(B + (((((k_0 * 32768) + ((((int)threadIdx.x) >> 5) * 1024)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 31) * 2)) + 12288));
    *(float2*)(B_shared + ((((int)threadIdx.x) * 2) + 1024)) = *(float2*)(B + (((((k_0 * 32768) + ((((int)threadIdx.x) >> 5) * 1024)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 31) * 2)) + 16384));
    *(float2*)(B_shared + ((((int)threadIdx.x) * 2) + 1280)) = *(float2*)(B + (((((k_0 * 32768) + ((((int)threadIdx.x) >> 5) * 1024)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 31) * 2)) + 20480));
    *(float2*)(B_shared + ((((int)threadIdx.x) * 2) + 1536)) = *(float2*)(B + (((((k_0 * 32768) + ((((int)threadIdx.x) >> 5) * 1024)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 31) * 2)) + 24576));
    *(float2*)(B_shared + ((((int)threadIdx.x) * 2) + 1792)) = *(float2*)(B + (((((k_0 * 32768) + ((((int)threadIdx.x) >> 5) * 1024)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 31) * 2)) + 28672));
    __syncthreads();
    for (int k_1 = 0; k_1 < 2; ++k_1) {
      for (int k_2 = 0; k_2 < 16; ++k_2) {
        Y_local[0] = (Y_local[0] + (A_shared[(((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16))] * B_shared[(((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2))]));
        Y_local[32] = (Y_local[32] + (A_shared[(((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16))] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 32)]));
        Y_local[1] = (Y_local[1] + (A_shared[(((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16))] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 1)]));
        Y_local[33] = (Y_local[33] + (A_shared[(((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16))] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 33)]));
        Y_local[2] = (Y_local[2] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 1)] * B_shared[(((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2))]));
        Y_local[34] = (Y_local[34] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 1)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 32)]));
        Y_local[3] = (Y_local[3] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 1)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 1)]));
        Y_local[35] = (Y_local[35] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 1)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 33)]));
        Y_local[4] = (Y_local[4] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 2)] * B_shared[(((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2))]));
        Y_local[36] = (Y_local[36] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 2)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 32)]));
        Y_local[5] = (Y_local[5] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 2)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 1)]));
        Y_local[37] = (Y_local[37] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 2)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 33)]));
        Y_local[6] = (Y_local[6] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 3)] * B_shared[(((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2))]));
        Y_local[38] = (Y_local[38] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 3)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 32)]));
        Y_local[7] = (Y_local[7] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 3)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 1)]));
        Y_local[39] = (Y_local[39] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 3)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 33)]));
        Y_local[8] = (Y_local[8] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 4)] * B_shared[(((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2))]));
        Y_local[40] = (Y_local[40] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 4)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 32)]));
        Y_local[9] = (Y_local[9] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 4)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 1)]));
        Y_local[41] = (Y_local[41] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 4)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 33)]));
        Y_local[10] = (Y_local[10] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 5)] * B_shared[(((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2))]));
        Y_local[42] = (Y_local[42] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 5)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 32)]));
        Y_local[11] = (Y_local[11] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 5)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 1)]));
        Y_local[43] = (Y_local[43] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 5)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 33)]));
        Y_local[12] = (Y_local[12] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 6)] * B_shared[(((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2))]));
        Y_local[44] = (Y_local[44] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 6)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 32)]));
        Y_local[13] = (Y_local[13] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 6)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 1)]));
        Y_local[45] = (Y_local[45] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 6)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 33)]));
        Y_local[14] = (Y_local[14] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 7)] * B_shared[(((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2))]));
        Y_local[46] = (Y_local[46] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 7)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 32)]));
        Y_local[15] = (Y_local[15] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 7)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 1)]));
        Y_local[47] = (Y_local[47] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 7)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 33)]));
        Y_local[16] = (Y_local[16] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 8)] * B_shared[(((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2))]));
        Y_local[48] = (Y_local[48] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 8)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 32)]));
        Y_local[17] = (Y_local[17] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 8)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 1)]));
        Y_local[49] = (Y_local[49] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 8)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 33)]));
        Y_local[18] = (Y_local[18] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 9)] * B_shared[(((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2))]));
        Y_local[50] = (Y_local[50] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 9)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 32)]));
        Y_local[19] = (Y_local[19] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 9)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 1)]));
        Y_local[51] = (Y_local[51] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 9)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 33)]));
        Y_local[20] = (Y_local[20] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 10)] * B_shared[(((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2))]));
        Y_local[52] = (Y_local[52] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 10)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 32)]));
        Y_local[21] = (Y_local[21] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 10)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 1)]));
        Y_local[53] = (Y_local[53] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 10)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 33)]));
        Y_local[22] = (Y_local[22] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 11)] * B_shared[(((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2))]));
        Y_local[54] = (Y_local[54] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 11)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 32)]));
        Y_local[23] = (Y_local[23] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 11)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 1)]));
        Y_local[55] = (Y_local[55] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 11)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 33)]));
        Y_local[24] = (Y_local[24] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 12)] * B_shared[(((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2))]));
        Y_local[56] = (Y_local[56] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 12)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 32)]));
        Y_local[25] = (Y_local[25] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 12)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 1)]));
        Y_local[57] = (Y_local[57] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 12)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 33)]));
        Y_local[26] = (Y_local[26] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 13)] * B_shared[(((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2))]));
        Y_local[58] = (Y_local[58] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 13)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 32)]));
        Y_local[27] = (Y_local[27] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 13)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 1)]));
        Y_local[59] = (Y_local[59] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 13)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 33)]));
        Y_local[28] = (Y_local[28] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 14)] * B_shared[(((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2))]));
        Y_local[60] = (Y_local[60] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 14)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 32)]));
        Y_local[29] = (Y_local[29] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 14)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 1)]));
        Y_local[61] = (Y_local[61] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 14)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 33)]));
        Y_local[30] = (Y_local[30] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 15)] * B_shared[(((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2))]));
        Y_local[62] = (Y_local[62] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 15)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 32)]));
        Y_local[31] = (Y_local[31] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 15)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 1)]));
        Y_local[63] = (Y_local[63] + (A_shared[((((k_1 * 2048) + (k_2 * 128)) + ((((int)threadIdx.x) >> 4) * 16)) + 15)] * B_shared[((((k_1 * 1024) + (k_2 * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 33)]));
      }
    }
  }
  Y[(((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2))] = Y_local[0];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 32)] = Y_local[32];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 1)] = Y_local[1];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 33)] = Y_local[33];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 1024)] = Y_local[2];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 1056)] = Y_local[34];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 1025)] = Y_local[3];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 1057)] = Y_local[35];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 2048)] = Y_local[4];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 2080)] = Y_local[36];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 2049)] = Y_local[5];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 2081)] = Y_local[37];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 3072)] = Y_local[6];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 3104)] = Y_local[38];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 3073)] = Y_local[7];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 3105)] = Y_local[39];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 4096)] = Y_local[8];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 4128)] = Y_local[40];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 4097)] = Y_local[9];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 4129)] = Y_local[41];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 5120)] = Y_local[10];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 5152)] = Y_local[42];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 5121)] = Y_local[11];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 5153)] = Y_local[43];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 6144)] = Y_local[12];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 6176)] = Y_local[44];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 6145)] = Y_local[13];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 6177)] = Y_local[45];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 7168)] = Y_local[14];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 7200)] = Y_local[46];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 7169)] = Y_local[15];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 7201)] = Y_local[47];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 8192)] = Y_local[16];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 8224)] = Y_local[48];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 8193)] = Y_local[17];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 8225)] = Y_local[49];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 9216)] = Y_local[18];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 9248)] = Y_local[50];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 9217)] = Y_local[19];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 9249)] = Y_local[51];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 10240)] = Y_local[20];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 10272)] = Y_local[52];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 10241)] = Y_local[21];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 10273)] = Y_local[53];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 11264)] = Y_local[22];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 11296)] = Y_local[54];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 11265)] = Y_local[23];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 11297)] = Y_local[55];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 12288)] = Y_local[24];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 12320)] = Y_local[56];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 12289)] = Y_local[25];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 12321)] = Y_local[57];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 13312)] = Y_local[26];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 13344)] = Y_local[58];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 13313)] = Y_local[27];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 13345)] = Y_local[59];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 14336)] = Y_local[28];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 14368)] = Y_local[60];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 14337)] = Y_local[29];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 14369)] = Y_local[61];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 15360)] = Y_local[30];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 15392)] = Y_local[62];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 15361)] = Y_local[31];
  Y[((((((((int)blockIdx.x) >> 4) * 131072) + ((((int)threadIdx.x) >> 4) * 16384)) + ((((int)blockIdx.x) & 15) * 64)) + ((((int)threadIdx.x) & 15) * 2)) + 15393)] = Y_local[63];
}


