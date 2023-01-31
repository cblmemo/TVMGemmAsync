#include <stdio.h>

#include "include/inc.h"

class CUDAMatrix {
private:
    float *mat, *dev_mat;
    int bat, row, col;
    size_t size;

public:
    CUDAMatrix(int b, int r, int c) : bat(b), row(r), col(c), size(sizeof(float) * b * r * c) { mat = (float *) malloc(size); cudaMalloc((void **) &dev_mat, size); }
    ~CUDAMatrix() { free(mat), cudaFree(dev_mat); }
    float *devPtr() { return dev_mat; }
    void cpyToDevice() { cudaMemcpy(dev_mat, mat, size, cudaMemcpyHostToDevice); }
    void cpyToHost() { cudaMemcpy(mat, dev_mat, size, cudaMemcpyDeviceToHost); }
    float &at(int b, int i, int j) { return mat[b * row * col + i * col + j]; }
    const float &at(int b, int i, int j) const { return mat[b * row * col + i * col + j]; }
    // void print() {
    //     for (int i = 0; i < row; i++) {
    //         for (int j = 0; j < col; j++) {
    //             printf("%.2f ", mat[i * col + j]);
    //         }
    //         printf("\n");
    //     }
    // }
    void fillRand() {
        for (int b = 0; b < bat; b++)
            for (int i = 0; i < row; i++)
                for (int j = 0; j < col; j++)
                    at(b, i, j) = rand() % 100;
    }
    void fill(float val) {
        for (int b = 0; b < bat; b++)
            for (int i = 0; i < row; i++)
                for (int j = 0; j < col; j++)
                    at(b, i, j) = val;
    }
};

float equal(float a, float b) { return abs(a - b) < 0.001; }

float multiTest(void (*calc)(float *, float *, float *), int round = 100) {
    srand(time(nullptr));
    // fprintf(stderr, "srand seed: %ld\n", time(nullptr));
    // srand(1666362747);
    static const int warmupGoal = round / 10;
    CUDAMatrix AM(B, K, M), BM(B, K, N), CM(B, M, N), ans(B, M, N);
    double totTime = 0;
    AM.fillRand(), BM.fillRand(); 
    AM.cpyToDevice(), BM.cpyToDevice();
    for (int i = 0; i < warmupGoal; i++) calc(AM.devPtr(), BM.devPtr(), CM.devPtr());
    for (int i = 0; i < round; i++) {
        // A.fillRand(), B.fillRand();
        // A.cpyToDevice(), B.cpyToDevice();
        cudaEvent_t start, stop;
        cudaEventCreate(&start);
        cudaEventCreate(&stop);
        cudaEventRecord(start, 0);
        
        calc(AM.devPtr(), BM.devPtr(), CM.devPtr());

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
    CM.cpyToHost();
    double FLOPs = (((long long int) (M)) * N * K + M * N) * 2 * B;
    double runtime = totTime / round;
    float ret = double(FLOPs) / runtime / 1.0e6;
    if (ret > 25000) fprintf(stderr, "Cuda Error: %s\n", cudaGetErrorString(cudaGetLastError()));
    return ret;
}

// void run_tune_old(float *A, float *B, float *C) {
//     if (SHARED_SIZE > (48 << 10)) cudaFuncSetAttribute(main_kernel0, cudaFuncAttributeMaxDynamicSharedMemorySize, SHARED_SIZE);
//     main_kernel0<<<BLOCK_NUM, THREAD_NUM, SHARED_SIZE>>>(A, B, C);
// }

void run_tune(float *AM, float *BM, float *CM) {
    main_kernel0<<<BLOCK_NUM, THREAD_NUM>>>(AM, BM, CM);
}

int main() {
    float tune = multiTest(run_tune, 100);
    printf("tune GFLOPs: %f\n", tune);
    return 0;
}