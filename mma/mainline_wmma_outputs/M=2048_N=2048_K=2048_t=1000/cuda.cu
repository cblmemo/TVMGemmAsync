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
  nvcuda::wmma::fragment<nvcuda::wmma::matrix_a, 16, 16, 16, half, nvcuda::wmma::row_major> A_reindex_shared_dyn_wmma_matrix_a[16];
  nvcuda::wmma::fragment<nvcuda::wmma::matrix_b, 16, 16, 16, half, nvcuda::wmma::row_major> B_reindex_shared_dyn_wmma_matrix_b[8];
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[0], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[4], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[1], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[5], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[2], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[6], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[3], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[7], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[8], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[12], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[9], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[13], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[10], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[14], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[11], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[15], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[16], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[20], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[17], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[21], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[18], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[22], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[19], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[23], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[24], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[28], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[25], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[29], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[26], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[30], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[27], 0.000000e+00f);
  nvcuda::wmma::fill_fragment(Y_reindex_shared_dyn_wmma_accumulator[31], 0.000000e+00f);
  for (int ax2_0_0 = 0; ax2_0_0 < 64; ++ax2_0_0) {
    __syncthreads();
    *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 160) + ((((int)threadIdx.x) >> 3) * 40)) + ((((int)threadIdx.x) & 7) * 4))) = *(uint2*)(A + (((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + (((int)threadIdx.y) * 8192)) + ((((int)threadIdx.x) >> 3) * 2048)) + (ax2_0_0 * 32)) + ((((int)threadIdx.x) & 7) * 4)));
    *(uint2*)(((half*)buf_dyn_shmem) + ((((((int)threadIdx.y) * 160) + ((((int)threadIdx.x) >> 3) * 40)) + ((((int)threadIdx.x) & 7) * 4)) + 640)) = *(uint2*)(A + ((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + (((int)threadIdx.y) * 8192)) + ((((int)threadIdx.x) >> 3) * 2048)) + (ax2_0_0 * 32)) + ((((int)threadIdx.x) & 7) * 4)) + 32768));
    *(uint2*)(((half*)buf_dyn_shmem) + ((((((int)threadIdx.y) * 160) + ((((int)threadIdx.x) >> 3) * 40)) + ((((int)threadIdx.x) & 7) * 4)) + 1280)) = *(uint2*)(A + ((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + (((int)threadIdx.y) * 8192)) + ((((int)threadIdx.x) >> 3) * 2048)) + (ax2_0_0 * 32)) + ((((int)threadIdx.x) & 7) * 4)) + 65536));
    *(uint2*)(((half*)buf_dyn_shmem) + ((((((int)threadIdx.y) * 160) + ((((int)threadIdx.x) >> 3) * 40)) + ((((int)threadIdx.x) & 7) * 4)) + 1920)) = *(uint2*)(A + ((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + (((int)threadIdx.y) * 8192)) + ((((int)threadIdx.x) >> 3) * 2048)) + (ax2_0_0 * 32)) + ((((int)threadIdx.x) & 7) * 4)) + 98304));
    *(uint2*)(((half*)buf_dyn_shmem) + ((((((int)threadIdx.y) * 160) + ((((int)threadIdx.x) >> 3) * 40)) + ((((int)threadIdx.x) & 7) * 4)) + 2560)) = *(uint2*)(A + ((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + (((int)threadIdx.y) * 8192)) + ((((int)threadIdx.x) >> 3) * 2048)) + (ax2_0_0 * 32)) + ((((int)threadIdx.x) & 7) * 4)) + 131072));
    *(uint2*)(((half*)buf_dyn_shmem) + ((((((int)threadIdx.y) * 160) + ((((int)threadIdx.x) >> 3) * 40)) + ((((int)threadIdx.x) & 7) * 4)) + 3200)) = *(uint2*)(A + ((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + (((int)threadIdx.y) * 8192)) + ((((int)threadIdx.x) >> 3) * 2048)) + (ax2_0_0 * 32)) + ((((int)threadIdx.x) & 7) * 4)) + 163840));
    *(uint2*)(((half*)buf_dyn_shmem) + ((((((int)threadIdx.y) * 160) + ((((int)threadIdx.x) >> 3) * 40)) + ((((int)threadIdx.x) & 7) * 4)) + 3840)) = *(uint2*)(A + ((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + (((int)threadIdx.y) * 8192)) + ((((int)threadIdx.x) >> 3) * 2048)) + (ax2_0_0 * 32)) + ((((int)threadIdx.x) & 7) * 4)) + 196608));
    *(uint2*)(((half*)buf_dyn_shmem) + ((((((int)threadIdx.y) * 160) + ((((int)threadIdx.x) >> 3) * 40)) + ((((int)threadIdx.x) & 7) * 4)) + 4480)) = *(uint2*)(A + ((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + (((int)threadIdx.y) * 8192)) + ((((int)threadIdx.x) >> 3) * 2048)) + (ax2_0_0 * 32)) + ((((int)threadIdx.x) & 7) * 4)) + 229376));
    *(uint4*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 264) + (((int)threadIdx.x) * 8)) + 5120)) = *(uint4*)(B + ((((ax2_0_0 * 65536) + (((int)threadIdx.y) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + (((int)threadIdx.x) * 8)));
    *(uint4*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 264) + (((int)threadIdx.x) * 8)) + 6176)) = *(uint4*)(B + (((((ax2_0_0 * 65536) + (((int)threadIdx.y) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + (((int)threadIdx.x) * 8)) + 8192));
    *(uint4*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 264) + (((int)threadIdx.x) * 8)) + 7232)) = *(uint4*)(B + (((((ax2_0_0 * 65536) + (((int)threadIdx.y) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + (((int)threadIdx.x) * 8)) + 16384));
    *(uint4*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 264) + (((int)threadIdx.x) * 8)) + 8288)) = *(uint4*)(B + (((((ax2_0_0 * 65536) + (((int)threadIdx.y) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + (((int)threadIdx.x) * 8)) + 24576));
    *(uint4*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 264) + (((int)threadIdx.x) * 8)) + 9344)) = *(uint4*)(B + (((((ax2_0_0 * 65536) + (((int)threadIdx.y) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + (((int)threadIdx.x) * 8)) + 32768));
    *(uint4*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 264) + (((int)threadIdx.x) * 8)) + 10400)) = *(uint4*)(B + (((((ax2_0_0 * 65536) + (((int)threadIdx.y) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + (((int)threadIdx.x) * 8)) + 40960));
    *(uint4*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 264) + (((int)threadIdx.x) * 8)) + 11456)) = *(uint4*)(B + (((((ax2_0_0 * 65536) + (((int)threadIdx.y) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + (((int)threadIdx.x) * 8)) + 49152));
    *(uint4*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 264) + (((int)threadIdx.x) * 8)) + 12512)) = *(uint4*)(B + (((((ax2_0_0 * 65536) + (((int)threadIdx.y) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + (((int)threadIdx.x) * 8)) + 57344));
    __syncthreads();
    nvcuda::wmma::load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a[0], (&(((half*)buf_dyn_shmem)[0])), 40);
    nvcuda::wmma::load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a[1], (&(((half*)buf_dyn_shmem)[16])), 40);
    nvcuda::wmma::load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a[2], (&(((half*)buf_dyn_shmem)[640])), 40);
    nvcuda::wmma::load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a[3], (&(((half*)buf_dyn_shmem)[656])), 40);
    nvcuda::wmma::load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a[4], (&(((half*)buf_dyn_shmem)[1280])), 40);
    nvcuda::wmma::load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a[5], (&(((half*)buf_dyn_shmem)[1296])), 40);
    nvcuda::wmma::load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a[6], (&(((half*)buf_dyn_shmem)[1920])), 40);
    nvcuda::wmma::load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a[7], (&(((half*)buf_dyn_shmem)[1936])), 40);
    nvcuda::wmma::load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a[8], (&(((half*)buf_dyn_shmem)[2560])), 40);
    nvcuda::wmma::load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a[9], (&(((half*)buf_dyn_shmem)[2576])), 40);
    nvcuda::wmma::load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a[10], (&(((half*)buf_dyn_shmem)[3200])), 40);
    nvcuda::wmma::load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a[11], (&(((half*)buf_dyn_shmem)[3216])), 40);
    nvcuda::wmma::load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a[12], (&(((half*)buf_dyn_shmem)[3840])), 40);
    nvcuda::wmma::load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a[13], (&(((half*)buf_dyn_shmem)[3856])), 40);
    nvcuda::wmma::load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a[14], (&(((half*)buf_dyn_shmem)[4480])), 40);
    nvcuda::wmma::load_matrix_sync(A_reindex_shared_dyn_wmma_matrix_a[15], (&(((half*)buf_dyn_shmem)[4496])), 40);
    nvcuda::wmma::load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b[0], (&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 64) + 5120)])), 264);
    nvcuda::wmma::load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b[1], (&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 64) + 5136)])), 264);
    nvcuda::wmma::load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b[2], (&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 64) + 5152)])), 264);
    nvcuda::wmma::load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b[3], (&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 64) + 5168)])), 264);
    nvcuda::wmma::load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b[4], (&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 64) + 9344)])), 264);
    nvcuda::wmma::load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b[5], (&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 64) + 9360)])), 264);
    nvcuda::wmma::load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b[6], (&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 64) + 9376)])), 264);
    nvcuda::wmma::load_matrix_sync(B_reindex_shared_dyn_wmma_matrix_b[7], (&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 64) + 9392)])), 264);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[0], A_reindex_shared_dyn_wmma_matrix_a[0], B_reindex_shared_dyn_wmma_matrix_b[0], Y_reindex_shared_dyn_wmma_accumulator[0]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[4], A_reindex_shared_dyn_wmma_matrix_a[2], B_reindex_shared_dyn_wmma_matrix_b[0], Y_reindex_shared_dyn_wmma_accumulator[4]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[0], A_reindex_shared_dyn_wmma_matrix_a[1], B_reindex_shared_dyn_wmma_matrix_b[4], Y_reindex_shared_dyn_wmma_accumulator[0]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[4], A_reindex_shared_dyn_wmma_matrix_a[3], B_reindex_shared_dyn_wmma_matrix_b[4], Y_reindex_shared_dyn_wmma_accumulator[4]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[1], A_reindex_shared_dyn_wmma_matrix_a[0], B_reindex_shared_dyn_wmma_matrix_b[1], Y_reindex_shared_dyn_wmma_accumulator[1]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[5], A_reindex_shared_dyn_wmma_matrix_a[2], B_reindex_shared_dyn_wmma_matrix_b[1], Y_reindex_shared_dyn_wmma_accumulator[5]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[1], A_reindex_shared_dyn_wmma_matrix_a[1], B_reindex_shared_dyn_wmma_matrix_b[5], Y_reindex_shared_dyn_wmma_accumulator[1]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[5], A_reindex_shared_dyn_wmma_matrix_a[3], B_reindex_shared_dyn_wmma_matrix_b[5], Y_reindex_shared_dyn_wmma_accumulator[5]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[2], A_reindex_shared_dyn_wmma_matrix_a[0], B_reindex_shared_dyn_wmma_matrix_b[2], Y_reindex_shared_dyn_wmma_accumulator[2]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[6], A_reindex_shared_dyn_wmma_matrix_a[2], B_reindex_shared_dyn_wmma_matrix_b[2], Y_reindex_shared_dyn_wmma_accumulator[6]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[2], A_reindex_shared_dyn_wmma_matrix_a[1], B_reindex_shared_dyn_wmma_matrix_b[6], Y_reindex_shared_dyn_wmma_accumulator[2]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[6], A_reindex_shared_dyn_wmma_matrix_a[3], B_reindex_shared_dyn_wmma_matrix_b[6], Y_reindex_shared_dyn_wmma_accumulator[6]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[3], A_reindex_shared_dyn_wmma_matrix_a[0], B_reindex_shared_dyn_wmma_matrix_b[3], Y_reindex_shared_dyn_wmma_accumulator[3]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[7], A_reindex_shared_dyn_wmma_matrix_a[2], B_reindex_shared_dyn_wmma_matrix_b[3], Y_reindex_shared_dyn_wmma_accumulator[7]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[3], A_reindex_shared_dyn_wmma_matrix_a[1], B_reindex_shared_dyn_wmma_matrix_b[7], Y_reindex_shared_dyn_wmma_accumulator[3]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[7], A_reindex_shared_dyn_wmma_matrix_a[3], B_reindex_shared_dyn_wmma_matrix_b[7], Y_reindex_shared_dyn_wmma_accumulator[7]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[8], A_reindex_shared_dyn_wmma_matrix_a[4], B_reindex_shared_dyn_wmma_matrix_b[0], Y_reindex_shared_dyn_wmma_accumulator[8]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[12], A_reindex_shared_dyn_wmma_matrix_a[6], B_reindex_shared_dyn_wmma_matrix_b[0], Y_reindex_shared_dyn_wmma_accumulator[12]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[8], A_reindex_shared_dyn_wmma_matrix_a[5], B_reindex_shared_dyn_wmma_matrix_b[4], Y_reindex_shared_dyn_wmma_accumulator[8]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[12], A_reindex_shared_dyn_wmma_matrix_a[7], B_reindex_shared_dyn_wmma_matrix_b[4], Y_reindex_shared_dyn_wmma_accumulator[12]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[9], A_reindex_shared_dyn_wmma_matrix_a[4], B_reindex_shared_dyn_wmma_matrix_b[1], Y_reindex_shared_dyn_wmma_accumulator[9]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[13], A_reindex_shared_dyn_wmma_matrix_a[6], B_reindex_shared_dyn_wmma_matrix_b[1], Y_reindex_shared_dyn_wmma_accumulator[13]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[9], A_reindex_shared_dyn_wmma_matrix_a[5], B_reindex_shared_dyn_wmma_matrix_b[5], Y_reindex_shared_dyn_wmma_accumulator[9]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[13], A_reindex_shared_dyn_wmma_matrix_a[7], B_reindex_shared_dyn_wmma_matrix_b[5], Y_reindex_shared_dyn_wmma_accumulator[13]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[10], A_reindex_shared_dyn_wmma_matrix_a[4], B_reindex_shared_dyn_wmma_matrix_b[2], Y_reindex_shared_dyn_wmma_accumulator[10]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[14], A_reindex_shared_dyn_wmma_matrix_a[6], B_reindex_shared_dyn_wmma_matrix_b[2], Y_reindex_shared_dyn_wmma_accumulator[14]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[10], A_reindex_shared_dyn_wmma_matrix_a[5], B_reindex_shared_dyn_wmma_matrix_b[6], Y_reindex_shared_dyn_wmma_accumulator[10]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[14], A_reindex_shared_dyn_wmma_matrix_a[7], B_reindex_shared_dyn_wmma_matrix_b[6], Y_reindex_shared_dyn_wmma_accumulator[14]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[11], A_reindex_shared_dyn_wmma_matrix_a[4], B_reindex_shared_dyn_wmma_matrix_b[3], Y_reindex_shared_dyn_wmma_accumulator[11]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[15], A_reindex_shared_dyn_wmma_matrix_a[6], B_reindex_shared_dyn_wmma_matrix_b[3], Y_reindex_shared_dyn_wmma_accumulator[15]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[11], A_reindex_shared_dyn_wmma_matrix_a[5], B_reindex_shared_dyn_wmma_matrix_b[7], Y_reindex_shared_dyn_wmma_accumulator[11]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[15], A_reindex_shared_dyn_wmma_matrix_a[7], B_reindex_shared_dyn_wmma_matrix_b[7], Y_reindex_shared_dyn_wmma_accumulator[15]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[16], A_reindex_shared_dyn_wmma_matrix_a[8], B_reindex_shared_dyn_wmma_matrix_b[0], Y_reindex_shared_dyn_wmma_accumulator[16]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[20], A_reindex_shared_dyn_wmma_matrix_a[10], B_reindex_shared_dyn_wmma_matrix_b[0], Y_reindex_shared_dyn_wmma_accumulator[20]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[16], A_reindex_shared_dyn_wmma_matrix_a[9], B_reindex_shared_dyn_wmma_matrix_b[4], Y_reindex_shared_dyn_wmma_accumulator[16]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[20], A_reindex_shared_dyn_wmma_matrix_a[11], B_reindex_shared_dyn_wmma_matrix_b[4], Y_reindex_shared_dyn_wmma_accumulator[20]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[17], A_reindex_shared_dyn_wmma_matrix_a[8], B_reindex_shared_dyn_wmma_matrix_b[1], Y_reindex_shared_dyn_wmma_accumulator[17]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[21], A_reindex_shared_dyn_wmma_matrix_a[10], B_reindex_shared_dyn_wmma_matrix_b[1], Y_reindex_shared_dyn_wmma_accumulator[21]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[17], A_reindex_shared_dyn_wmma_matrix_a[9], B_reindex_shared_dyn_wmma_matrix_b[5], Y_reindex_shared_dyn_wmma_accumulator[17]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[21], A_reindex_shared_dyn_wmma_matrix_a[11], B_reindex_shared_dyn_wmma_matrix_b[5], Y_reindex_shared_dyn_wmma_accumulator[21]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[18], A_reindex_shared_dyn_wmma_matrix_a[8], B_reindex_shared_dyn_wmma_matrix_b[2], Y_reindex_shared_dyn_wmma_accumulator[18]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[22], A_reindex_shared_dyn_wmma_matrix_a[10], B_reindex_shared_dyn_wmma_matrix_b[2], Y_reindex_shared_dyn_wmma_accumulator[22]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[18], A_reindex_shared_dyn_wmma_matrix_a[9], B_reindex_shared_dyn_wmma_matrix_b[6], Y_reindex_shared_dyn_wmma_accumulator[18]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[22], A_reindex_shared_dyn_wmma_matrix_a[11], B_reindex_shared_dyn_wmma_matrix_b[6], Y_reindex_shared_dyn_wmma_accumulator[22]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[19], A_reindex_shared_dyn_wmma_matrix_a[8], B_reindex_shared_dyn_wmma_matrix_b[3], Y_reindex_shared_dyn_wmma_accumulator[19]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[23], A_reindex_shared_dyn_wmma_matrix_a[10], B_reindex_shared_dyn_wmma_matrix_b[3], Y_reindex_shared_dyn_wmma_accumulator[23]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[19], A_reindex_shared_dyn_wmma_matrix_a[9], B_reindex_shared_dyn_wmma_matrix_b[7], Y_reindex_shared_dyn_wmma_accumulator[19]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[23], A_reindex_shared_dyn_wmma_matrix_a[11], B_reindex_shared_dyn_wmma_matrix_b[7], Y_reindex_shared_dyn_wmma_accumulator[23]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[24], A_reindex_shared_dyn_wmma_matrix_a[12], B_reindex_shared_dyn_wmma_matrix_b[0], Y_reindex_shared_dyn_wmma_accumulator[24]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[28], A_reindex_shared_dyn_wmma_matrix_a[14], B_reindex_shared_dyn_wmma_matrix_b[0], Y_reindex_shared_dyn_wmma_accumulator[28]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[24], A_reindex_shared_dyn_wmma_matrix_a[13], B_reindex_shared_dyn_wmma_matrix_b[4], Y_reindex_shared_dyn_wmma_accumulator[24]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[28], A_reindex_shared_dyn_wmma_matrix_a[15], B_reindex_shared_dyn_wmma_matrix_b[4], Y_reindex_shared_dyn_wmma_accumulator[28]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[25], A_reindex_shared_dyn_wmma_matrix_a[12], B_reindex_shared_dyn_wmma_matrix_b[1], Y_reindex_shared_dyn_wmma_accumulator[25]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[29], A_reindex_shared_dyn_wmma_matrix_a[14], B_reindex_shared_dyn_wmma_matrix_b[1], Y_reindex_shared_dyn_wmma_accumulator[29]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[25], A_reindex_shared_dyn_wmma_matrix_a[13], B_reindex_shared_dyn_wmma_matrix_b[5], Y_reindex_shared_dyn_wmma_accumulator[25]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[29], A_reindex_shared_dyn_wmma_matrix_a[15], B_reindex_shared_dyn_wmma_matrix_b[5], Y_reindex_shared_dyn_wmma_accumulator[29]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[26], A_reindex_shared_dyn_wmma_matrix_a[12], B_reindex_shared_dyn_wmma_matrix_b[2], Y_reindex_shared_dyn_wmma_accumulator[26]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[30], A_reindex_shared_dyn_wmma_matrix_a[14], B_reindex_shared_dyn_wmma_matrix_b[2], Y_reindex_shared_dyn_wmma_accumulator[30]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[26], A_reindex_shared_dyn_wmma_matrix_a[13], B_reindex_shared_dyn_wmma_matrix_b[6], Y_reindex_shared_dyn_wmma_accumulator[26]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[30], A_reindex_shared_dyn_wmma_matrix_a[15], B_reindex_shared_dyn_wmma_matrix_b[6], Y_reindex_shared_dyn_wmma_accumulator[30]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[27], A_reindex_shared_dyn_wmma_matrix_a[12], B_reindex_shared_dyn_wmma_matrix_b[3], Y_reindex_shared_dyn_wmma_accumulator[27]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[31], A_reindex_shared_dyn_wmma_matrix_a[14], B_reindex_shared_dyn_wmma_matrix_b[3], Y_reindex_shared_dyn_wmma_accumulator[31]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[27], A_reindex_shared_dyn_wmma_matrix_a[13], B_reindex_shared_dyn_wmma_matrix_b[7], Y_reindex_shared_dyn_wmma_accumulator[27]);
    nvcuda::wmma::mma_sync(Y_reindex_shared_dyn_wmma_accumulator[31], A_reindex_shared_dyn_wmma_matrix_a[15], B_reindex_shared_dyn_wmma_matrix_b[7], Y_reindex_shared_dyn_wmma_accumulator[31]);
  }
  __syncthreads();
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[(((int)threadIdx.y) * 1024)])), Y_reindex_shared_dyn_wmma_accumulator[0], 16, nvcuda::wmma::mem_row_major);
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 1024) + 256)])), Y_reindex_shared_dyn_wmma_accumulator[1], 16, nvcuda::wmma::mem_row_major);
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 1024) + 512)])), Y_reindex_shared_dyn_wmma_accumulator[2], 16, nvcuda::wmma::mem_row_major);
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 1024) + 768)])), Y_reindex_shared_dyn_wmma_accumulator[3], 16, nvcuda::wmma::mem_row_major);
  __syncthreads();
  *(uint2*)(Y + ((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4))) = *(uint2*)(((half*)buf_dyn_shmem) + ((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 32)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 512));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 64)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 1024));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 96)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 1536));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 128)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 2048));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 160)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 2560));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 192)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 3072));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 224)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 3584));
  __syncthreads();
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[(((int)threadIdx.y) * 1024)])), Y_reindex_shared_dyn_wmma_accumulator[4], 16, nvcuda::wmma::mem_row_major);
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 1024) + 256)])), Y_reindex_shared_dyn_wmma_accumulator[5], 16, nvcuda::wmma::mem_row_major);
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 1024) + 512)])), Y_reindex_shared_dyn_wmma_accumulator[6], 16, nvcuda::wmma::mem_row_major);
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 1024) + 768)])), Y_reindex_shared_dyn_wmma_accumulator[7], 16, nvcuda::wmma::mem_row_major);
  __syncthreads();
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 32768)) = *(uint2*)(((half*)buf_dyn_shmem) + ((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 32800)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 512));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 32832)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 1024));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 32864)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 1536));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 32896)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 2048));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 32928)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 2560));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 32960)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 3072));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 32992)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 3584));
  __syncthreads();
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[(((int)threadIdx.y) * 1024)])), Y_reindex_shared_dyn_wmma_accumulator[8], 16, nvcuda::wmma::mem_row_major);
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 1024) + 256)])), Y_reindex_shared_dyn_wmma_accumulator[9], 16, nvcuda::wmma::mem_row_major);
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 1024) + 512)])), Y_reindex_shared_dyn_wmma_accumulator[10], 16, nvcuda::wmma::mem_row_major);
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 1024) + 768)])), Y_reindex_shared_dyn_wmma_accumulator[11], 16, nvcuda::wmma::mem_row_major);
  __syncthreads();
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 65536)) = *(uint2*)(((half*)buf_dyn_shmem) + ((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 65568)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 512));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 65600)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 1024));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 65632)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 1536));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 65664)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 2048));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 65696)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 2560));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 65728)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 3072));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 65760)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 3584));
  __syncthreads();
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[(((int)threadIdx.y) * 1024)])), Y_reindex_shared_dyn_wmma_accumulator[12], 16, nvcuda::wmma::mem_row_major);
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 1024) + 256)])), Y_reindex_shared_dyn_wmma_accumulator[13], 16, nvcuda::wmma::mem_row_major);
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 1024) + 512)])), Y_reindex_shared_dyn_wmma_accumulator[14], 16, nvcuda::wmma::mem_row_major);
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 1024) + 768)])), Y_reindex_shared_dyn_wmma_accumulator[15], 16, nvcuda::wmma::mem_row_major);
  __syncthreads();
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 98304)) = *(uint2*)(((half*)buf_dyn_shmem) + ((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 98336)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 512));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 98368)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 1024));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 98400)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 1536));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 98432)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 2048));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 98464)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 2560));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 98496)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 3072));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 98528)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 3584));
  __syncthreads();
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[(((int)threadIdx.y) * 1024)])), Y_reindex_shared_dyn_wmma_accumulator[16], 16, nvcuda::wmma::mem_row_major);
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 1024) + 256)])), Y_reindex_shared_dyn_wmma_accumulator[17], 16, nvcuda::wmma::mem_row_major);
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 1024) + 512)])), Y_reindex_shared_dyn_wmma_accumulator[18], 16, nvcuda::wmma::mem_row_major);
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 1024) + 768)])), Y_reindex_shared_dyn_wmma_accumulator[19], 16, nvcuda::wmma::mem_row_major);
  __syncthreads();
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 131072)) = *(uint2*)(((half*)buf_dyn_shmem) + ((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 131104)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 512));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 131136)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 1024));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 131168)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 1536));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 131200)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 2048));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 131232)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 2560));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 131264)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 3072));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 131296)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 3584));
  __syncthreads();
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[(((int)threadIdx.y) * 1024)])), Y_reindex_shared_dyn_wmma_accumulator[20], 16, nvcuda::wmma::mem_row_major);
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 1024) + 256)])), Y_reindex_shared_dyn_wmma_accumulator[21], 16, nvcuda::wmma::mem_row_major);
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 1024) + 512)])), Y_reindex_shared_dyn_wmma_accumulator[22], 16, nvcuda::wmma::mem_row_major);
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 1024) + 768)])), Y_reindex_shared_dyn_wmma_accumulator[23], 16, nvcuda::wmma::mem_row_major);
  __syncthreads();
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 163840)) = *(uint2*)(((half*)buf_dyn_shmem) + ((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 163872)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 512));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 163904)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 1024));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 163936)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 1536));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 163968)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 2048));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 164000)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 2560));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 164032)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 3072));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 164064)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 3584));
  __syncthreads();
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[(((int)threadIdx.y) * 1024)])), Y_reindex_shared_dyn_wmma_accumulator[24], 16, nvcuda::wmma::mem_row_major);
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 1024) + 256)])), Y_reindex_shared_dyn_wmma_accumulator[25], 16, nvcuda::wmma::mem_row_major);
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 1024) + 512)])), Y_reindex_shared_dyn_wmma_accumulator[26], 16, nvcuda::wmma::mem_row_major);
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 1024) + 768)])), Y_reindex_shared_dyn_wmma_accumulator[27], 16, nvcuda::wmma::mem_row_major);
  __syncthreads();
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 196608)) = *(uint2*)(((half*)buf_dyn_shmem) + ((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 196640)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 512));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 196672)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 1024));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 196704)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 1536));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 196736)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 2048));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 196768)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 2560));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 196800)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 3072));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 196832)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 3584));
  __syncthreads();
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[(((int)threadIdx.y) * 1024)])), Y_reindex_shared_dyn_wmma_accumulator[28], 16, nvcuda::wmma::mem_row_major);
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 1024) + 256)])), Y_reindex_shared_dyn_wmma_accumulator[29], 16, nvcuda::wmma::mem_row_major);
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 1024) + 512)])), Y_reindex_shared_dyn_wmma_accumulator[30], 16, nvcuda::wmma::mem_row_major);
  nvcuda::wmma::store_matrix_sync((&(((half*)buf_dyn_shmem)[((((int)threadIdx.y) * 1024) + 768)])), Y_reindex_shared_dyn_wmma_accumulator[31], 16, nvcuda::wmma::mem_row_major);
  __syncthreads();
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 229376)) = *(uint2*)(((half*)buf_dyn_shmem) + ((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 229408)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 512));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 229440)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 1024));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 229472)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 1536));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 229504)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 2048));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 229536)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 2560));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 229568)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 3072));
  *(uint2*)(Y + (((((((((((int)blockIdx.y) >> 3) * 1048576) + (((int)blockIdx.x) * 262144)) + ((((int)threadIdx.y) & 1) * 16384)) + ((((int)threadIdx.x) >> 2) * 2048)) + ((((int)blockIdx.y) & 7) * 256)) + ((((int)threadIdx.y) >> 1) * 16)) + ((((int)threadIdx.x) & 3) * 4)) + 229600)) = *(uint2*)(((half*)buf_dyn_shmem) + (((((int)threadIdx.y) * 128) + (((int)threadIdx.x) * 4)) + 3584));
}


