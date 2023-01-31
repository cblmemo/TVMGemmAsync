#include "cutlass/gemm/device/gemm.h"
#include "cutlass/layout/tensor.h"
#include "cutlass/conv/kernel/default_conv2d_fprop.h"
#include "cutlass/conv/device/implicit_gemm_convolution.h"
#include "cutlass/util/device_memory.h"
#include "include/inc.h"
#include <unistd.h>
#include <vector>

// using CutlassBestPerf = cutlass::gemm::device::Gemm<
//     float, cutlass::layout::ColumnMajor,
//     float, cutlass::layout::RowMajor,
//     float, cutlass::layout::RowMajor,
//     float,
//     cutlass::arch::OpClassSimt,
//     cutlass::arch::Sm80,
//     cutlass::gemm::GemmShape<64, 128, 8>,
//     cutlass::gemm::GemmShape<32, 64, 8>,
//     cutlass::gemm::GemmShape<1, 1, 1>,
//     cutlass::epilogue::thread::LinearCombination<
//         float,
//         1,
//         float,
//         float
//     >,
//     cutlass::gemm::threadblock::GemmIdentityThreadblockSwizzle<8>,
//     5,
//     1,
//     1,
//     true,
//     cutlass::arch::OpMultiplyAdd
//     >;

// void run_bestPerf(float *IT, float *WT, float *OT) {
// #ifdef NT_LAYOUT
//     int lda = M;
//     int ldb = N;
//     int ldc = N;
// #elif defined(NN_LAYOUT)
//     int lda = M;
//     int ldb = N;
//     int ldc = M;
// #endif
//     CutlassBestPerf gemm_operator;
//     CutlassBestPerf::Arguments args(
//         {M, N, K},
//         {A, lda},
//         {B, ldb},
//         {C, ldc},
//         {C, ldc},
//         {1, 0}
//     );
//     gemm_operator(args);
// }

/// Conv operation element types for the Gemm equivalent (ImplicitGemm)
using ElementA           = float;
using ElementB           = float;
using ElementC           = float;
using ElementAccumulator = float;
using ElementCompute     = float;


/// Device-level Conv2d instance
using Conv2dFpropKernel = typename cutlass::conv::kernel::DefaultConv2dFprop<
    ElementA, 
    cutlass::layout::TensorNHWC,
    ElementB, 
    cutlass::layout::TensorNHWC,
    ElementC, 
    cutlass::layout::TensorNHWC,
    ElementAccumulator,
    cutlass::arch::OpClassSimt,
    cutlass::arch::Sm80,
    cutlass::gemm::GemmShape<64, 64, 8>,
    cutlass::gemm::GemmShape<32, 64, 8>, 
    cutlass::gemm::GemmShape<1, 1, 1>,
    cutlass::epilogue::thread::LinearCombination<
        ElementC,
        1,
        ElementAccumulator,
        ElementCompute
    >,
    cutlass::gemm::threadblock::GemmIdentityThreadblockSwizzle<4>,
    5,
    cutlass::arch::OpMultiplyAdd,
    cutlass::conv::IteratorAlgorithm::kOptimized,
    cutlass::conv::StrideSupport::kStrided,
    1,
    1
>::Kernel;

using Conv2dFprop = cutlass::conv::device::ImplicitGemmConvolution<Conv2dFpropKernel>;

cutlass::conv::Conv2dProblemSize problem_size(      
    cutlass::Tensor4DCoord(N, H, W, C),
    cutlass::Tensor4DCoord(R, S, C, K),
    cutlass::Tensor4DCoord(1, 1, 1, 1),
    cutlass::MatrixCoord(1, 1),
    cutlass::MatrixCoord(1, 1),
    cutlass::Tensor4DCoord(N, P, Q, K),
    cutlass::conv::Mode::kCrossCorrelation,
    1
);

size_t workspace_size;
cutlass::device_memory::allocation<uint8_t> workspace;

void preprocess() {
    Conv2dFprop::Arguments arguments {
        problem_size,
        {nullptr, cutlass::layout::TensorNHWC::packed({N, H, W, C})},
        {nullptr, cutlass::layout::TensorNHWC::packed({R, S, C, K})},
        {nullptr, cutlass::layout::TensorNHWC::packed({N, P, Q, K})},
        {nullptr, cutlass::layout::TensorNHWC::packed({N, P, Q, K})},
        {1, 0}
    };
    Conv2dFprop implicit_gemm_op;
    workspace_size = implicit_gemm_op.get_workspace_size(arguments);
    workspace.reset(workspace_size);
}

void run_cutlass(float *IT, float *WT, float *OT) {
    Conv2dFprop::Arguments arguments {
        problem_size,
        {IT, cutlass::layout::TensorNHWC::packed({N, H, W, C})},
        {WT, cutlass::layout::TensorNHWC::packed({R, S, C, K})},
        {OT, cutlass::layout::TensorNHWC::packed({N, P, Q, K})},
        {OT, cutlass::layout::TensorNHWC::packed({N, P, Q, K})},
        {1, 0}
    };
    Conv2dFprop implicit_gemm_op;
    implicit_gemm_op(arguments, workspace.get());
}

void run_tune(float *IT, float *WT, float *OT) {
    main_kernel0<<<BLOCK_NUM, THREAD_NUM>>>(IT, WT, OT);
}

class CUDATensor {
private:
    float *tensor_, *dev_tensor_;
    std::vector<int> shape_;
    size_t size_;

public:
    CUDATensor(std::vector<int> shape) {
        size_ = 1;
        for (int i = 0; i < shape.size(); i++) {
            shape_.push_back(shape[i]);
            size_ *= shape[i];
        }
        tensor_ = (float *) malloc(size_ * sizeof(float));
        cudaMalloc((void **) &dev_tensor_, size_ * sizeof(float));
    }
    ~CUDATensor() { free(tensor_), cudaFree(dev_tensor_); }
    float *devPtr() { return dev_tensor_; }
    void cpyToDevice() { cudaMemcpy(dev_tensor_, tensor_, size_, cudaMemcpyHostToDevice); }
    void cpyToHost() { cudaMemcpy(tensor_, dev_tensor_, size_, cudaMemcpyDeviceToHost); }
    void fillRand() { for (int i = 0; i < size_; i++) tensor_[i] = rand() % 100; }
    void fill(float val) { for (int i = 0; i < size_; i++) tensor_[i] = val; }
};

float multiTest(void (*calc)(float *, float *, float *), int round = 100) {
    srand(time(nullptr));
    // fprintf(stderr, "srand seed: %ld\n", time(nullptr));
    // srand(1666362747);
    static const int warmupGoal = round / 10;
    CUDATensor IT({N, H, W, C}), WT({R, S, C, K}), OT({N, P, Q, K});
    double totTime = 0;
    IT.fillRand(), WT.fillRand();
    IT.cpyToDevice(), WT.cpyToDevice();
    for (int i = 0; i < warmupGoal; i++) calc(IT.devPtr(), WT.devPtr(), OT.devPtr());
    for (int i = 0; i < round; i++) {
        // A.fillRand(), B.fillRand();
        // A.cpyToDevice(), B.cpyToDevice();
        cudaEvent_t start, stop;
        cudaEventCreate(&start);
        cudaEventCreate(&stop);
        cudaEventRecord(start, 0);
        
        calc(IT.devPtr(), WT.devPtr(), OT.devPtr());

        cudaEventRecord(stop, 0);
        cudaEventSynchronize(stop);
        float ti;
        cudaEventElapsedTime(&ti, start, stop);
        cudaEventDestroy(start);
        cudaEventDestroy(stop);
        totTime += ti;
        // C.cpyToHost();
        // printf("%f\n", ti);
    }
    // printf("%f\n", totTime);
    OT.cpyToHost();
    int gemmM = N * P * Q, gemmN = K, gemmK = R * S * C;
    double FLOPs = (((long long int) (gemmM)) * gemmN * gemmK + gemmM * gemmN) * 2;
    double runtime = totTime / round;
    float ret = double(FLOPs) / runtime / 1.0e6;
    if (ret > 25000) fprintf(stderr, "Cuda Error: %s\n", cudaGetErrorString(cudaGetLastError()));
    return ret;
}

int main() {
    preprocess();
    float cutlass = multiTest(run_cutlass, 100);
    float tune = multiTest(run_tune, 100);
    printf("tune: %f, cutlass: %f\n", tune, cutlass);
    return 0;
}