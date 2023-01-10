#include <stdio.h>

#include "include/inc.h"

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

float equal(float a, float b) { return abs(a - b) < 0.001; }

float multiTest(void (*calc)(float *, float *, float *), int round = 100, bool check = true) {
    srand(time(nullptr));
    // fprintf(stderr, "srand seed: %ld\n", time(nullptr));
    // srand(1666362747);
    static const int warmupGoal = round / 10;
    CUDAMatrix A(K, M), B(K, N), C(M, N), ans(M, N);
    double totTime = 0;
    A.fillRand(), B.fillRand();
    if (check) {
        ans.fill(0);
        for (int i = 0; i < M; i++)
            for (int j = 0; j < N; j++)
                for (int k = 0; k < K; k++) 
                    ans.at(i, j) += A.at(k, i) * B.at(k, j);
    }  
    A.cpyToDevice(), B.cpyToDevice();
    for (int i = 0; i < warmupGoal; i++) calc(A.devPtr(), B.devPtr(), C.devPtr());
    for (int i = 0; i < round; i++) {
        // A.fillRand(), B.fillRand();
        // A.cpyToDevice(), B.cpyToDevice();
        cudaEvent_t start, stop;
        cudaEventCreate(&start);
        cudaEventCreate(&stop);
        cudaEventRecord(start, 0);
        
        calc(A.devPtr(), B.devPtr(), C.devPtr());

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
    C.cpyToHost();
    if (check) {
        for (int i = 0; i < M; i++)
            for (int j = 0; j < N; j++)
                if (!equal(ans.at(i, j), C.at(i, j)))
                    return fprintf(stderr, "Error with (%.2f - %.2f) = %.2f at (%d, %d)\n", ans.at(i, j), C.at(i, j), (ans.at(i, j) - C.at(i, j)), i, j), -1;
    }
    double FLOPs = (((long long int) (M)) * N * K + M * N) * 2;
    double runtime = totTime / round;
    float ret = double(FLOPs) / runtime / 1.0e6;
    if (ret > 25000) fprintf(stderr, "Cuda Error: %s\n", cudaGetErrorString(cudaGetLastError()));
    return ret;
}

void run_tune(float *A, float *B, float *C) {
    if (SHARED_SIZE >= (48 << 10)) cudaFuncSetAttribute(main_kernel0, cudaFuncAttributeMaxDynamicSharedMemorySize, SHARED_SIZE);
    main_kernel0<<<BLOCK_NUM, THREAD_NUM, SHARED_SIZE>>>(A, B, C);
}

int main() {
    float tune = multiTest(run_tune, 100, false);
    printf("tune GFLOPs: %f\n", tune);
    return 0;
}