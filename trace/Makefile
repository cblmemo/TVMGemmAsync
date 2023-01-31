top: build run
build:
	@nvcc speedTest.cu -o cutlassMultiStage -gencode=arch=compute_86,code=sm_86
run:
	@./cutlassMultiStage > out.txt