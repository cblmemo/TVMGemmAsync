#include "simplifiedCutlassMultiStage.cu"
#include "bin/tvm_cuda_with_async.cu"

class CUDAMatrix {
private:
    float *mat, *dev_mat;
    int length;
    size_t size;

public:
    CUDAMatrix(int l) : length(l), size(sizeof(float) * l * l) {
        mat = (float *) malloc(size);
        cudaMalloc((void **) &dev_mat, size);
    }

    ~CUDAMatrix() {
        free(mat);
        cudaFree(dev_mat);
    }

    float *devPtr() {
        return dev_mat;
    }

    void cpyToDevice() {
        cudaMemcpy(dev_mat, mat, size, cudaMemcpyHostToDevice);
    }

    void cpyToHost() {
        cudaMemcpy(mat, dev_mat, size, cudaMemcpyDeviceToHost);
    }

    float &at(int i, int j) {
        return mat[i * length + j];
    }

    const float &at(int i, int j) const {
        return mat[i * length + j];
    }

    void print() {
        for (int i = 0; i < length; i++) {
            for (int j = 0; j < length; j++) {
                printf("%.2f ", mat[i * length + j]);
            }
            printf("\n");
        }
    }
};

void test() {
    CUDAMatrix A(1024), B(1024), C(1024);
    for (int i = 0; i < 1024; i++) {
        for (int j = 0; j < 1024; j++) {
            A.at(i, j) = j == 0 ? 1 : 0;
            B.at(i, j) = i == 0 ? 1 : 0;
            C.at(i, j) = 3;
        }
    }
    A.cpyToDevice(), B.cpyToDevice();
    dim3 grid(64, 1, 1), block(256, 1, 1);
    int smem_size = int(sizeof(SharedStorage));
    kernel<<<grid, block, smem_size, nullptr>>>(A.devPtr(), B.devPtr(), C.devPtr());
    auto err = cudaGetLastError();
    if (err != cudaSuccess) printf("CUDA Error: %s\n", cudaGetErrorString(err));
    C.cpyToHost();
    C.print();
}

float equal(float a, float b) { return abs(a - b) < 0.001; }

// #define USE_CUTLASS_ORIGINAL

void multiTest(int round = 300, int maxCheckThreshold = 1) {
    srand(time(nullptr));
    // fprintf(stderr, "srand seed: %ld\n", time(nullptr));
    // srand(1666362747);
    static const int l = 1024, warmupGoal = round / 5;
    CUDAMatrix A(l), B(l), C(l), ans(l);
    int cur = round;
    float totGFLOPs = 0, totTime = 0;
    int verifiedCnt = 0;
    while (cur--) {
        // fprintf(stderr, "\r                                                                                                             ");
        fprintf(stderr, "\rRound %d ", round - cur);
        // fprintf(stderr, "Initializing A/B matrix...\n");
        for (int i = 0; i < l; i++) {
            for (int j = 0; j < l; j++) {
                // A.at(i, j) = i <= j ? rand() % 100 : A.at(j, i);
                // B.at(i, j) = i <= j ? rand() % 100 : B.at(j, i);
                // A.at(i, j) = 1;
                // B.at(i, j) = 1;
                // A.at(i, j) = rand() * 337 + 28;
                // B.at(i, j) = rand() * 359 + 76;
                A.at(i, j) = rand() % 100;
                B.at(i, j) = rand() % 100;
                ans.at(i, j) = 0.0f;
            }
        }
        A.cpyToDevice(), B.cpyToDevice();

        if (verifiedCnt < maxCheckThreshold) {
            // fprintf(stderr, "Calculating std...\n");
            for (int i = 0; i < l; i++)
                for (int j = 0; j < l; j++)
                    for (int k = 0; k < l; k++)
                        // i == 0 && j == 0 ? fprintf(stdout, "k = %d, ans[i][j] = %f, A.at(k, i) * B.at(k, j) = %f\n", k, ans[i][j], A.at(k, i) * B.at(k, j)) : 0, 
#ifdef USE_CUTLASS_ORIGINAL
                        ans.at(i, j) += A.at(k, i) * B.at(k, j); // A: ColumnMajor, B: RowMajor
#else
                        ans.at(i, j) += A.at(k, i) * B.at(k, j); // A: ColumnMajor, B: RowMajor
#endif
        }
        
        // fprintf(stderr, "Calculating in cuda...\n");
        cudaEvent_t start, stop;
        cudaEventCreate(&start);
        cudaEventCreate(&stop);
        cudaEventRecord(start, 0);

#ifdef USE_CUTLASS_ORIGINAL
        dim3 grid(64, 1, 1), block(256, 1, 1);
        int smem_size = int(sizeof(SharedStorage)); // 32768
        kernel<<<grid, block, smem_size, nullptr>>>(A.devPtr(), B.devPtr(), C.devPtr());
#else
        dim3 grid(64), block(256);
        int smem_size = int(sizeof(SharedStorage));
        // cudaFuncSetAttribute(main_kernel0, cudaFuncAttributeMaxDynamicSharedMemorySize, 81920);
        // smem_size = 81920;
        main_kernel0<<<grid, block, smem_size>>>(A.devPtr(), B.devPtr(), C.devPtr());
#endif

        cudaEventRecord(stop, 0);
        cudaEventSynchronize(stop);
        float ti, GFLOPs;
        cudaEventElapsedTime(&ti, start, stop);
        cudaEventDestroy(start);
        cudaEventDestroy(stop);

        auto err = cudaGetLastError();
        if (err != cudaSuccess) fprintf(stderr, "CUDA Error: %s\n", cudaGetErrorString(err));

    //    if (verifiedCnt < maxCheckThreshold) sleep(1);

        C.cpyToHost();

        if (verifiedCnt < maxCheckThreshold) {
            // fprintf(stderr, "Verifying...\n");
            for (int i = 0; i < l; i++)
                for (int j = 0; j < l; j++)
                    if (!equal(ans.at(i, j), C.at(i, j)))
                        return 
                            fprintf(stderr, "Error with (%.2f - %.2f) = %.2f at (%d, %d)\n", ans.at(i, j), C.at(i, j), (ans.at(i, j) - C.at(i, j)), i, j),
                            // printf("\n\nA:\n\n"), A.print(),
                            // printf("\n\nB:\n\n"), B.print(),
                            printf("\n\nC:\n\n"), C.print(),
                            printf("\n\nans:\n\n"), ans.print(),
                            void();
            verifiedCnt++;
            fprintf(stderr, "Verifiy passed this round. ");
        }

        GFLOPs = 2149580800.0 / ti / 1e6; // totTime is in microsecond
        fprintf(stderr, "Total time this round: %.5fms, speed this round: %.2f GFLOPs, ", ti, GFLOPs);
        if (round - cur > warmupGoal) {
            totGFLOPs += GFLOPs;
            totTime += ti;
            float avgGFLOPs = totGFLOPs / (round - cur - warmupGoal), avgTime = totTime / (round - cur - warmupGoal);
            fprintf(stderr, "average time: %.5f, average speed: %.2f GFLOPs", avgTime, avgGFLOPs);
        } else fprintf(stderr, "warmuping...");
    }
}

int main() {
    // test();
    multiTest(300);
    return 0;
}