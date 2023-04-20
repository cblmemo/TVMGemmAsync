#if defined(__CUDA_ARCH__) && (__CUDA_ARCH__ >= 530)
#include <cuda_fp16.h>
__device__ half max(half a, half b)
{
  return __hgt(__half(a), __half(b)) ? a : b;
}
__device__ half min(half a, half b)
{
  return __hlt(__half(a), __half(b)) ? a : b;
}
#else

typedef unsigned short uint16_t;
typedef unsigned char uint8_t;
typedef signed char int8_t;
typedef int int32_t;
typedef unsigned long long uint64_t;
typedef unsigned int uint32_t;

#define TVM_FORCE_INLINE inline __attribute__((always_inline))
#define TVM_XINLINE TVM_FORCE_INLINE __device__ __host__
#define TVM_ALIGNED(x) __attribute__ ((aligned(x)))
#define TVM_HALF_OPERATOR(RTYPE, OP)                              \
  TVM_XINLINE RTYPE operator OP (half a, half b) {                \
    return RTYPE(float(a) OP float(b));                           \
  }                                                               \
  template<typename T>                                            \
  TVM_XINLINE RTYPE operator OP (half a, T b) {                   \
    return RTYPE(float(a) OP float(b));                           \
  }                                                               \
  template<typename T>                                            \
  TVM_XINLINE RTYPE operator OP (T a, half b) {                   \
    return RTYPE(float(a) OP float(b));                           \
  }

#define TVM_HALF_ASSIGNOP(AOP, OP)                                \
  template<typename T>                                            \
  TVM_XINLINE half operator AOP (const T& a) {                    \
    return *this = half(float(*this) OP float(a));                \
  }                                                               \
  template<typename T>                                            \
  TVM_XINLINE half operator AOP (const volatile T& a) volatile {  \
    return *this = half(float(*this) OP float(a));                \
  }

class TVM_ALIGNED(2) half {
 public:
  uint16_t half_;

  static TVM_XINLINE half Binary(uint16_t value) {
    half res;
    res.half_ = value;
    return res;
  }

  TVM_XINLINE half() {}

  TVM_XINLINE half(const float& value) { constructor(value); }
  TVM_XINLINE explicit half(const double& value) { constructor(value); }
  TVM_XINLINE explicit half(const int8_t& value) { constructor(value); }
  TVM_XINLINE explicit half(const uint8_t& value) { constructor(value); }
  TVM_XINLINE explicit half(const int32_t& value) { constructor(value); }
  TVM_XINLINE explicit half(const uint32_t& value) { constructor(value); }
  TVM_XINLINE explicit half(const long long& value) { constructor(value); }
  TVM_XINLINE explicit half(const uint64_t& value) { constructor(value); }

  TVM_XINLINE operator float() const {                          \
    return float(half2float(half_));                            \
  }                                                             \
  TVM_XINLINE operator float() const volatile {                 \
    return float(half2float(half_));                            \
  }


  TVM_HALF_ASSIGNOP(+=, +)
  TVM_HALF_ASSIGNOP(-=, -)
  TVM_HALF_ASSIGNOP(*=, *)
  TVM_HALF_ASSIGNOP(/=, /)

  TVM_XINLINE half operator+() {
    return *this;
  }

  TVM_XINLINE half operator-() {
    return half(-float(*this));
  }

  TVM_XINLINE half operator=(const half& a) {
    half_ = a.half_;
    return a;
  }

  template<typename T>
  TVM_XINLINE half operator=(const T& a) {
    return *this = half(a);
  }

  TVM_XINLINE half operator=(const half& a) volatile {
    half_ = a.half_;
    return a;
  }

  template<typename T>
  TVM_XINLINE half operator=(const T& a) volatile {
    return *this = half(a);
  }

 private:
  union Bits {
    float f;
    int32_t si;
    uint32_t ui;
  };

  static int const fp16FractionBits = 10;
  static int const fp32FractionBits = 23;
  static int32_t const fp32FractionMask = ~(~0u << fp32FractionBits);   // == 0x7fffff
  static int32_t const fp32HiddenBit = 1 << fp32FractionBits;   // == 0x800000
  static int const shift = fp32FractionBits - fp16FractionBits;   // == 13
  static int const shiftSign = 16;
  static int32_t const expAdjust = 127 - 15;   // exp32-127 = exp16-15, so exp16 = exp32 - (127-15)

  static int32_t const infN = 0x7F800000;   // flt32 infinity
  static int32_t const maxN = 0x477FFFFF;   // max flt32 that's a flt16 normal after >> by shift
  static int32_t const minN = 0x38800000;   // min flt16 normal as a flt32
  static int32_t const maxZ = 0x33000000;   // max fp32 number that's still rounded to zero in fp16
  static int32_t const signN = 0x80000000;  // flt32 sign bit

  static int32_t const infC = infN >> shift;
  static int32_t const nanN = (infC + 1) << shift;   // minimum flt16 nan as a flt32
  static int32_t const maxC = maxN >> shift;
  static int32_t const minC = minN >> shift;
  static int32_t const signC = signN >> shiftSign;  // flt16 sign bit

  static int32_t const mulN = 0x52000000;  // (1 << 23) / minN
  static int32_t const mulC = 0x33800000;  // minN / (1 << (23 - shift))

  static int32_t const subC = 0x003FF;  // max flt32 subnormal down shifted
  static int32_t const norC = 0x00400;  // min flt32 normal down shifted

  static int32_t const maxD = infC - maxC - 1;
  static int32_t const minD = minC - subC - 1;

  TVM_XINLINE uint16_t float2half(const float& value) const {
    Bits v;
    v.f = value;
    uint32_t sign = v.si & signN;    // grab sign bit
    v.si ^= sign;                    // clear sign bit from v
    sign >>= shiftSign;              // logical shift sign to fp16 position

    if (v.si <= maxZ) {
      // Handle eventual zeros here to ensure
      // vshift will not exceed 32 below.
      v.ui = 0;
    } else if (v.si < minN) {
      // Handle denorms
      uint32_t exp32 = v.ui >> fp32FractionBits;
      int32_t exp16 = exp32 - expAdjust;
      // If exp16 == 0 (just into the denorm range), then significant should be shifted right 1.
      // Smaller (so negative) exp16 values should result in greater right shifts.
      uint32_t vshift = 1 - exp16;
      uint32_t significand = fp32HiddenBit | (v.ui & fp32FractionMask);
      v.ui = significand >> vshift;
      v.ui += (v.ui & 0x3fff) != 0x1000 || (significand & 0x7ff) ? 0x1000 : 0;
    } else if (v.si <= maxN) {
      // Handle norms
      v.ui += (v.ui & 0x3fff) != 0x1000 ? 0x1000 : 0;
      v.ui -= expAdjust << fp32FractionBits;
    } else if (v.si <= infN) {
      v.si = infN;
    } else if (v.si < nanN) {
      v.si = nanN;
    }

    v.ui >>= shift;
    return sign | (v.ui & 0x7fff);
  }

  // Same as above routine, except for addition of volatile keyword
  TVM_XINLINE uint16_t float2half(
    const volatile float& value) const volatile {
    Bits v;
    v.f = value;
    uint32_t sign = v.si & signN;    // grab sign bit
    v.si ^= sign;                    // clear sign bit from v
    sign >>= shiftSign;              // logical shift sign to fp16 position

    if (v.si <= maxZ) {
      // Handle eventual zeros here to ensure
      // vshift will not exceed 32 below.
      v.ui = 0;
    } else if (v.si < minN) {
      // Handle denorms
      uint32_t exp32 = v.ui >> fp32FractionBits;
      int32_t exp16 = exp32 - expAdjust;
      // If exp16 == 0 (just into the denorm range), then significant should be shifted right 1.
      // Smaller (so negative) exp16 values should result in greater right shifts.
      uint32_t vshift = 1 - exp16;
      uint32_t significand = fp32HiddenBit | (v.ui & fp32FractionMask);
      v.ui = significand >> vshift;
      v.ui += (v.ui & 0x3fff) != 0x1000 || (significand & 0x7ff) ? 0x1000 : 0;
    } else if (v.si <= maxN) {
      // Handle norms
      v.ui += (v.ui & 0x3fff) != 0x1000 ? 0x1000 : 0;
      v.ui -= expAdjust << fp32FractionBits;
    } else if (v.si <= infN) {
      v.si = infN;
    } else if (v.si < nanN) {
      v.si = nanN;
    }

    v.ui >>= shift;
    return sign | (v.ui & 0x7fff);
  }

  TVM_XINLINE float half2float(const uint16_t& value) const {
    Bits v;
    v.ui = value;
    int32_t sign = v.si & signC;
    v.si ^= sign;
    sign <<= shiftSign;
    v.si ^= ((v.si + minD) ^ v.si) & -(v.si > subC);
    v.si ^= ((v.si + maxD) ^ v.si) & -(v.si > maxC);
    Bits s;
    s.si = mulC;
    s.f *= v.si;
    int32_t mask = -(norC > v.si);
    v.si <<= shift;
    v.si ^= (s.si ^ v.si) & mask;
    v.si |= sign;
    return v.f;
  }

  TVM_XINLINE float half2float(
    const volatile uint16_t& value) const volatile {
    Bits v;
    v.ui = value;
    int32_t sign = v.si & signC;
    v.si ^= sign;
    sign <<= shiftSign;
    v.si ^= ((v.si + minD) ^ v.si) & -(v.si > subC);
    v.si ^= ((v.si + maxD) ^ v.si) & -(v.si > maxC);
    Bits s;
    s.si = mulC;
    s.f *= v.si;
    int32_t mask = -(norC > v.si);
    v.si <<= shift;
    v.si ^= (s.si ^ v.si) & mask;
    v.si |= sign;
    return v.f;
  }

  template<typename T>
  TVM_XINLINE void constructor(const T& value) {
    half_ = float2half(float(value));
  }
};

TVM_HALF_OPERATOR(half, +)
TVM_HALF_OPERATOR(half, -)
TVM_HALF_OPERATOR(half, *)
TVM_HALF_OPERATOR(half, /)
TVM_HALF_OPERATOR(bool, >)
TVM_HALF_OPERATOR(bool, <)
TVM_HALF_OPERATOR(bool, >=)
TVM_HALF_OPERATOR(bool, <=)

TVM_XINLINE half __float2half_rn(const float a) {
  return half(a);
}
#endif


// Pack two half values.
static inline __device__ __host__ unsigned
__pack_half2(const half x, const half y) {
  unsigned v0 = *((unsigned short *)&x);
  unsigned v1 = *((unsigned short *)&y);
  return (v1 << 16) | v0;
}

// Some fp16 math functions are not supported in cuda_fp16.h,
// so we define them here to make sure the generated CUDA code
// is valid.
#if defined(__CUDA_ARCH__) && (__CUDA_ARCH__ >= 530)
#define CUDA_UNSUPPORTED_HALF_MATH_BINARY(HALF_MATH_NAME, FP32_MATH_NAME) \
static inline __device__ __host__ half HALF_MATH_NAME(half x, half y) {   \
  float tmp_x = __half2float(x);                                          \
  float tmp_y = __half2float(y);                                          \
  float result = FP32_MATH_NAME(tmp_x, tmp_y);                            \
  return __float2half(result);                                            \
}

#define CUDA_UNSUPPORTED_HALF_MATH_UNARY(HALF_MATH_NAME, FP32_MATH_NAME) \
static inline __device__ __host__ half HALF_MATH_NAME(half x) {          \
  float tmp_x = __half2float(x);                                         \
  float result = FP32_MATH_NAME(tmp_x);                                  \
  return __float2half(result);                                           \
}

CUDA_UNSUPPORTED_HALF_MATH_BINARY(hpow, powf)
CUDA_UNSUPPORTED_HALF_MATH_UNARY(htanh, tanhf)
CUDA_UNSUPPORTED_HALF_MATH_UNARY(htan, tanf)
CUDA_UNSUPPORTED_HALF_MATH_UNARY(hatan, atanf)
CUDA_UNSUPPORTED_HALF_MATH_UNARY(herf, erf)

#undef CUDA_UNSUPPORTED_HALF_MATH_BINARY
#undef CUDA_UNSUPPORTED_HALF_MATH_UNARY

#endif
#include <mma.h>

#if (((__CUDACC_VER_MAJOR__ == 11) && (__CUDACC_VER_MINOR__ >= 4)) || \
     (__CUDACC_VER_MAJOR__ > 11))
#define TVM_ENABLE_L2_PREFETCH 1
#else
#define TVM_ENABLE_L2_PREFETCH 0
#endif

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
extern "C" __global__ void __launch_bounds__(128) main_kernel0(half* __restrict__ A, half* __restrict__ B, half* __restrict__ Y) {
  extern __shared__ uchar buf_dyn_shmem[];
  nvcuda::wmma::fragment<nvcuda::wmma::accumulator, 16, 16, 16, half> Y_reindex_shared_dyn_wmma_accumulator[32];
  nvcuda::wmma::fragment<nvcuda::wmma::matrix_a, 16, 16, 16, half, nvcuda::wmma::row_major> A_reindex_shared_dyn_wmma_matrix_a[4];
  nvcuda::wmma::fragment<nvcuda::wmma::matrix_b, 16, 16, 16, half, nvcuda::wmma::row_major> B_reindex_shared_dyn_wmma_matrix_b[8];
  for (int ax0_0_3_init = 0; ax0_0_3_init < 4; ++ax0_0_3_init) {
    nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[(ax0_0_3_init * 8)], 0.000000e+00f);
    nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[((ax0_0_3_init * 8) + 1)], 0.000000e+00f);
    nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[((ax0_0_3_init * 8) + 2)], 0.000000e+00f);
    nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[((ax0_0_3_init * 8) + 3)], 0.000000e+00f);
    nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[((ax0_0_3_init * 8) + 4)], 0.000000e+00f);
    nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[((ax0_0_3_init * 8) + 5)], 0.000000e+00f);
    nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[((ax0_0_3_init * 8) + 6)], 0.000000e+00f);
    nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[((ax0_0_3_init * 8) + 7)], 0.000000e+00f);
  }
  for (int ax2_0_0 = 0; ax2_0_0 < 256; ++ax2_0_0) {
    __syncthreads();
    *(uint4*)(((half*)buf_dyn_shmem) + ((((((int)threadIdx.y) * 320) + ((((int)threadIdx.x) >> 2) * 40)) + ((((int)threadIdx.x) & 3) * 8)) + 4352)) = *(uint4*)(A + (((((((((int)blockIdx.y) >> 6) * 8388608) + (((int)blockIdx.x) * 2097152)) + (((int)threadIdx.y) * 65536)) + ((((int)threadIdx.x) >> 2) * 8192)) + (ax2_0_0 * 32)) + ((((int)threadIdx.x) & 3) * 8)));
    *(uint4*)(((half*)buf_dyn_shmem) + ((((((int)threadIdx.y) * 320) + ((((int)threadIdx.x) >> 2) * 40)) + ((((int)threadIdx.x) & 3) * 8)) + 5632)) = *(uint4*)(A + ((((((((((int)blockIdx.y) >> 6) * 8388608) + (((int)blockIdx.x) * 2097152)) + (((int)threadIdx.y) * 65536)) + ((((int)threadIdx.x) >> 2) * 8192)) + (ax2_0_0 * 32)) + ((((int)threadIdx.x) & 3) * 8)) + 262144));
    *(uint4*)(((half*)buf_dyn_shmem) + ((((((int)threadIdx.y) * 320) + ((((int)threadIdx.x) >> 2) * 40)) + ((((int)threadIdx.x) & 3) * 8)) + 6912)) = *(uint4*)(A + ((((((((((int)blockIdx.y) >> 6) * 8388608) + (((int)blockIdx.x) * 2097152)) + (((int)threadIdx.y) * 65536)) + ((((int)threadIdx.x) >> 2) * 8192)) + (ax2_0_0 * 32)) + ((((int)threadIdx.x) & 3) * 8)) + 524288));
    *(uint4*)(((half*)buf_dyn_shmem) + ((((((int)threadIdx.y) * 320) + ((((int)threadIdx.x) >> 2) * 40)) + ((((int)threadIdx.x) & 3) * 8)) + 8192)) = *(uint4*)(A + ((((((((((int)blockIdx.y) >> 6) * 8388608) + (((int)blockIdx.x) * 2097152)) + (((int)threadIdx.y) * 65536)) + ((((int)threadIdx.x) >> 2) * 8192)) + (ax2_0_0 * 32)) + ((((int)threadIdx.x) & 3) * 8)) + 786432));
    *(uint4*)(((half*)buf_dyn_shmem) + ((((((int)threadIdx.y) * 320) + ((((int)threadIdx.x) >> 2) * 40)) + ((((int)threadIdx.x) & 3) * 8)) + 9472)) = *(uint4*)(A + ((((((((((int)blockIdx.y) >> 6) * 8388608) + (((int)blockIdx.x) * 2097152)) + (((int)threadIdx.y) * 65536)) + ((((int)threadIdx.x) >> 2) * 8192)) + (ax2_0_0 * 32)) + ((((int)threadIdx.x) & 3) * 8)) + 1048576));
    *(uint4*)(((half*)buf_dyn_shmem) + ((((((int)threadIdx.y) * 320) + ((((int)threadIdx.x) >> 2) * 40)) + ((((int)threadIdx.x) & 3) * 8)) + 10752)) = *(uint4*)(A + ((((((((((int)blockIdx.y) >> 6) * 8388608) + (((int)blockIdx.x) * 2097152)) + (((int)threadIdx.y) * 65536)) + ((((int)threadIdx.x) >> 2) * 8192)) + (ax2_0_0 * 32)) + ((((int)threadIdx.x) & 3) * 8)) + 1310720));
    *(uint4*)(((half*)buf_dyn_shmem) + ((((((int)threadIdx.y) * 320) + ((((int)threadIdx.x) >> 2) * 40)) + ((((int)threadIdx.x) & 3) * 8)) + 12032)) = *(uint4*)(A + ((((((((((int)blockIdx.y) >> 6) * 8388608) + (((int)blockIdx.x) * 2097152)) + (((int)threadIdx.y) * 65536)) + ((((int)threadIdx.x) >> 2) * 8192)) + (ax2_0_0 * 32)) + ((((int)threadIdx.x) & 3) * 8)) + 1572864));
    *(uint4*)(((half*)buf_dyn_shmem) + ((((((int)threadIdx.y) * 320) + ((((int)threadIdx.x) >> 2) * 40)) + ((((int)threadIdx.x) & 3) * 8)) + 13312)) = *(uint4*)(A + ((((((((((int)blockIdx.y) >> 6) * 8388608) + (((int)blockIdx.x) * 2097152)) + (((int)threadIdx.y) * 65536)) + ((((int)threadIdx.x) >> 2) * 8192)) + (ax2_0_0 * 32)) + ((((int)threadIdx.x) & 3) * 8)) + 1835008));
    *(uint2*)(((half*)buf_dyn_shmem) + ((((int)threadIdx.y) * 136) + (((int)threadIdx.x) * 4))) = *(uint2*)(B + ((((ax2_0_0 * 262144) + (((int)threadIdx.y) * 8192)) + ((((int)blockIdx.y) & 63) * 128)) + (((int)threadIdx.x) * 4)));
    *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 136) + (((int)threadIdx.x) * 4)) + 544)) = *(uint2*)(B + (((((ax2_0_0 * 262144) + (((int)threadIdx.y) * 8192)) + ((((int)blockIdx.y) & 63) * 128)) + (((int)threadIdx.x) * 4)) + 32768));
    *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 136) + (((int)threadIdx.x) * 4)) + 1088)) = *(uint2*)(B + (((((ax2_0_0 * 262144) + (((int)threadIdx.y) * 8192)) + ((((int)blockIdx.y) & 63) * 128)) + (((int)threadIdx.x) * 4)) + 65536));
    *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 136) + (((int)threadIdx.x) * 4)) + 1632)) = *(uint2*)(B + (((((ax2_0_0 * 262144) + (((int)threadIdx.y) * 8192)) + ((((int)blockIdx.y) & 63) * 128)) + (((int)threadIdx.x) * 4)) + 98304));
    *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 136) + (((int)threadIdx.x) * 4)) + 2176)) = *(uint2*)(B + (((((ax2_0_0 * 262144) + (((int)threadIdx.y) * 8192)) + ((((int)blockIdx.y) & 63) * 128)) + (((int)threadIdx.x) * 4)) + 131072));
    *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 136) + (((int)threadIdx.x) * 4)) + 2720)) = *(uint2*)(B + (((((ax2_0_0 * 262144) + (((int)threadIdx.y) * 8192)) + ((((int)blockIdx.y) & 63) * 128)) + (((int)threadIdx.x) * 4)) + 163840));
    *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 136) + (((int)threadIdx.x) * 4)) + 3264)) = *(uint2*)(B + (((((ax2_0_0 * 262144) + (((int)threadIdx.y) * 8192)) + ((((int)blockIdx.y) & 63) * 128)) + (((int)threadIdx.x) * 4)) + 196608));
    *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 136) + (((int)threadIdx.x) * 4)) + 3808)) = *(uint2*)(B + (((((ax2_0_0 * 262144) + (((int)threadIdx.y) * 8192)) + ((((int)blockIdx.y) & 63) * 128)) + (((int)threadIdx.x) * 4)) + 229376));
    __syncthreads();
    for (int ax2_0_1 = 0; ax2_0_1 < 2; ++ax2_0_1) {
      nvcuda::wmma::load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a[0], (&(((half*)buf_dyn_shmem)[(((((int)threadIdx.y) * 2560) + (ax2_0_1 * 16)) + 4352)])), 40);
      nvcuda::wmma::load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a[1], (&(((half*)buf_dyn_shmem)[(((((int)threadIdx.y) * 2560) + (ax2_0_1 * 16)) + 4992)])), 40);
      nvcuda::wmma::load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a[2], (&(((half*)buf_dyn_shmem)[(((((int)threadIdx.y) * 2560) + (ax2_0_1 * 16)) + 5632)])), 40);
      nvcuda::wmma::load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a[3], (&(((half*)buf_dyn_shmem)[(((((int)threadIdx.y) * 2560) + (ax2_0_1 * 16)) + 6272)])), 40);
      nvcuda::wmma::load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b[0], (&(((half*)buf_dyn_shmem)[(ax2_0_1 * 2176)])), 136);
      nvcuda::wmma::load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b[1], (&(((half*)buf_dyn_shmem)[((ax2_0_1 * 2176) + 16)])), 136);
      nvcuda::wmma::load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b[2], (&(((half*)buf_dyn_shmem)[((ax2_0_1 * 2176) + 32)])), 136);
      nvcuda::wmma::load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b[3], (&(((half*)buf_dyn_shmem)[((ax2_0_1 * 2176) + 48)])), 136);
      nvcuda::wmma::load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b[4], (&(((half*)buf_dyn_shmem)[((ax2_0_1 * 2176) + 64)])), 136);
      nvcuda::wmma::load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b[5], (&(((half*)buf_dyn_shmem)[((ax2_0_1 * 2176) + 80)])), 136);
      nvcuda::wmma::load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b[6], (&(((half*)buf_dyn_shmem)[((ax2_0_1 * 2176) + 96)])), 136);
      nvcuda::wmma::load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b[7], (&(((half*)buf_dyn_shmem)[((ax2_0_1 * 2176) + 112)])), 136);
      for (int ax0_0_3 = 0; ax0_0_3 < 4; ++ax0_0_3) {
        nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[(ax0_0_3 * 8)], A_reindex_shared_dyn_wmma_matrix_a[ax0_0_3], B_reindex_shared_dyn_wmma_matrix_b[0], Y_reindex_shared_dyn_wmma_accumulator[(ax0_0_3 * 8)]);
        nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[((ax0_0_3 * 8) + 1)], A_reindex_shared_dyn_wmma_matrix_a[ax0_0_3], B_reindex_shared_dyn_wmma_matrix_b[1], Y_reindex_shared_dyn_wmma_accumulator[((ax0_0_3 * 8) + 1)]);
        nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[((ax0_0_3 * 8) + 2)], A_reindex_shared_dyn_wmma_matrix_a[ax0_0_3], B_reindex_shared_dyn_wmma_matrix_b[2], Y_reindex_shared_dyn_wmma_accumulator[((ax0_0_3 * 8) + 2)]);
        nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[((ax0_0_3 * 8) + 3)], A_reindex_shared_dyn_wmma_matrix_a[ax0_0_3], B_reindex_shared_dyn_wmma_matrix_b[3], Y_reindex_shared_dyn_wmma_accumulator[((ax0_0_3 * 8) + 3)]);
        nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[((ax0_0_3 * 8) + 4)], A_reindex_shared_dyn_wmma_matrix_a[ax0_0_3], B_reindex_shared_dyn_wmma_matrix_b[4], Y_reindex_shared_dyn_wmma_accumulator[((ax0_0_3 * 8) + 4)]);
        nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[((ax0_0_3 * 8) + 5)], A_reindex_shared_dyn_wmma_matrix_a[ax0_0_3], B_reindex_shared_dyn_wmma_matrix_b[5], Y_reindex_shared_dyn_wmma_accumulator[((ax0_0_3 * 8) + 5)]);
        nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[((ax0_0_3 * 8) + 6)], A_reindex_shared_dyn_wmma_matrix_a[ax0_0_3], B_reindex_shared_dyn_wmma_matrix_b[6], Y_reindex_shared_dyn_wmma_accumulator[((ax0_0_3 * 8) + 6)]);
        nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[((ax0_0_3 * 8) + 7)], A_reindex_shared_dyn_wmma_matrix_a[ax0_0_3], B_reindex_shared_dyn_wmma_matrix_b[7], Y_reindex_shared_dyn_wmma_accumulator[((ax0_0_3 * 8) + 7)]);
      }
    }
  }
  for (int ax2 = 0; ax2 < 4; ++ax2) {
    __syncthreads();
    nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 2048) + 4352)])), Y_reindex_shared_dyn_wmma_accumulator[(ax2 * 8)], 16, nvcuda::wmma::mem_row_major);
    nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 2048) + 4608)])), Y_reindex_shared_dyn_wmma_accumulator[((ax2 * 8) + 1)], 16, nvcuda::wmma::mem_row_major);
    nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 2048) + 4864)])), Y_reindex_shared_dyn_wmma_accumulator[((ax2 * 8) + 2)], 16, nvcuda::wmma::mem_row_major);
    nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 2048) + 5120)])), Y_reindex_shared_dyn_wmma_accumulator[((ax2 * 8) + 3)], 16, nvcuda::wmma::mem_row_major);
    nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 2048) + 5376)])), Y_reindex_shared_dyn_wmma_accumulator[((ax2 * 8) + 4)], 16, nvcuda::wmma::mem_row_major);
    nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 2048) + 5632)])), Y_reindex_shared_dyn_wmma_accumulator[((ax2 * 8) + 5)], 16, nvcuda::wmma::mem_row_major);
    nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 2048) + 5888)])), Y_reindex_shared_dyn_wmma_accumulator[((ax2 * 8) + 6)], 16, nvcuda::wmma::mem_row_major);
    nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 2048) + 6144)])), Y_reindex_shared_dyn_wmma_accumulator[((ax2 * 8) + 7)], 16, nvcuda::wmma::mem_row_major);
    __syncthreads();
    for (int ax0_ax1_ax3_ax4_ax5_fused_0 = 0; ax0_ax1_ax3_ax4_ax5_fused_0 < 32; ++ax0_ax1_ax3_ax4_ax5_fused_0) {
      *(uint1*)(Y + ((((((((((((int)blockIdx.y) >> 6) * 8388608) + (((int)blockIdx.x) * 2097152)) + ((ax0_ax1_ax3_ax4_ax5_fused_0 >> 3) * 524288)) + (ax2 * 131072)) + (((int)threadIdx.y) * 32768)) + ((((int)threadIdx.x) >> 3) * 8192)) + ((((int)blockIdx.y) & 63) * 128)) + ((ax0_ax1_ax3_ax4_ax5_fused_0 & 7) * 16)) + ((((int)threadIdx.x) & 7) * 2))) = *(uint1*)(((half*)buf_dyn_shmem) + ((((ax0_ax1_ax3_ax4_ax5_fused_0 * 256) + (((int)threadIdx.y) * 64)) + (((int)threadIdx.x) * 2)) + 4352));
    }
  }
}


