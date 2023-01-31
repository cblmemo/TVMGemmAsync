conv:
	nvcc convSpeedTest.cu -o bin/executable -I ../cutlass/include -I ../cutlass/tools/util/include -gencode=arch=compute_86,code=sm_86
gemm:
	nvcc gemmSpeedTest.cu -o bin/executable -gencode=arch=compute_86,code=sm_86
run:
	bin/executable