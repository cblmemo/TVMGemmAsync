#include "cutlass/gemm/device/gemm.h"
#include "include/inc.h"
#include <unistd.h>

#define NT_LAYOUT
// #define NN_LAYOUT

using CutlassBestPerf = cutlass::gemm::device::Gemm<
    float, cutlass::layout::ColumnMajor,
    float, cutlass::layout::RowMajor,
    float, cutlass::layout::RowMajor,
    float,
    cutlass::arch::OpClassSimt,
    cutlass::arch::Sm80,
    cutlass::gemm::GemmShape<256, 128, 8>, // MODIFY THIS LINE
    cutlass::gemm::GemmShape<64, 64, 8>,   // MODIFY THIS LINE
    cutlass::gemm::GemmShape<1, 1, 1>,
    cutlass::epilogue::thread::LinearCombination<
        float,
        1,
        float,
        float
    >,
    cutlass::gemm::threadblock::GemmIdentityThreadblockSwizzle<8>,
    5,                                     // MODIFY THIS LINE
    1,
    1,
    true,
    cutlass::arch::OpMultiplyAdd
    >;

void run_bestPerf(float *A, float *B, float *C) {
#ifdef NT_LAYOUT
    int lda = M;
    int ldb = N;
    int ldc = N;
#elif defined(NN_LAYOUT)
    int lda = M;
    int ldb = N;
    int ldc = M;
#endif
    CutlassBestPerf gemm_operator;
    CutlassBestPerf::Arguments args(
        {M, N, K},
        {A, lda},
        {B, ldb},
        {C, ldc},
        {C, ldc},
        {1, 0}
    );
    gemm_operator(args);
}

class CUDAMatrix {
private:
    float *mat, *dev_mat;
    int row, col;
    size_t size;

public:
    CUDAMatrix(int r, int c) : row(r), col(c), size(sizeof(float) * r * c) { mat = (float *) malloc(size); cudaMalloc((void **) &dev_mat, size); }
    ~CUDAMatrix() { free(mat), cudaFree(dev_mat); }
    float *devPtr() { return dev_mat; }
    void cpyToDevice() { cudaMemcpy(dev_mat, mat, size, cudaMemcpyHostToDevice); }
    void cpyToHost() { cudaMemcpy(mat, dev_mat, size, cudaMemcpyDeviceToHost); }
    float &at(int i, int j) { return mat[i * col + j]; }
    const float &at(int i, int j) const { return mat[i * col + j]; }
    void print() {
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                printf("%.2f ", mat[i * col + j]);
            }
            printf("\n");
        }
    }
    void fillRand() {
        for (int i = 0; i < row; i++)
            for (int j = 0; j < col; j++)
                at(i, j) = rand() % 100;
    }
    void fill(float val) {
        for (int i = 0; i < row; i++)
            for (int j = 0; j < col; j++)
                at(i, j) = val;
    }
};

int main() {
    int round = 100;
    int warmupGoal = round / 10;
    double totTime = 0;
#ifdef NT_LAYOUT
    CUDAMatrix A(K, M), B(K, N), C(M, N);
#elif defined(NN_LAYOUT)
    CUDAMatrix A(M, K), B(K, N), C(M, N);
#endif
    A.fillRand(), B.fillRand();
    A.cpyToDevice(), B.cpyToDevice();
    usleep(50);
    for (int i = 0; i < warmupGoal; i++) run_bestPerf(A.devPtr(), B.devPtr(), C.devPtr());
    for (int i = 0; i < round; i++) {
        cudaEvent_t start, stop;
        cudaEventCreate(&start);
        cudaEventCreate(&stop);
        cudaEventRecord(start, 0);
        
        run_bestPerf(A.devPtr(), B.devPtr(), C.devPtr());

        cudaEventRecord(stop, 0);
        cudaEventSynchronize(stop);
        float ti;
        cudaEventElapsedTime(&ti, start, stop);
        cudaEventDestroy(start);
        cudaEventDestroy(stop);
        totTime += ti;
        // cudaError_t err = cudaGetLastError();
        // if (err != cudaSuccess) printf("%s\n", cudaGetErrorString(err));
    }
    C.cpyToHost();
    double FLOPs = (((long long int) (M)) * N * K + M * N) * 2;
    double runtime = totTime / round;
    // printf("%lf\n", totTime);
    double res = double(FLOPs) / runtime / 1.0e6;
    if (res > 25000) fprintf(stderr, "CUDA Error: %s\n", cudaGetErrorString(cudaGetLastError()));
    printf("cutlass GFLOPs: %lf\n", res);
}