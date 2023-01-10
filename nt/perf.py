import os
import sys
import time

output_dir_name = 'outputs'
old_output_dir_name = 'old_outputs'

def exe(s):
    # print(s)
    os.system(s)
def get_first_digit(s):
    st, ed = -1, -1
    for i, ch in enumerate(s):
        if ch.isdigit():
            st = i
            break
    for i in range(st, len(s)):
        if not s[i].isdigit():
            ed = i
            break
    return int(s[st:ed])
def perf(M=1024, N=1024, K=1024):
    exe(f'cp {output_dir_name}/M={M}_N={N}_K={K}/cuda.cu include/tune.cu')
    szA, szB, nb, nt = -1, -1, -1, -1
    with open(f'{output_dir_name}/M={M}_N={N}_K={K}/lower.py', 'r') as f:
        for l in f.readlines():
            raw = l.strip()
            if raw.startswith('A_shared_dyn = T.allocate'):
                szA = get_first_digit(raw)
            if raw.startswith('B_shared_dyn = T.allocate'):
                szB = get_first_digit(raw)
            if raw.startswith('T.launch_thread(blockIdx_x'):
                nb = get_first_digit(raw)
            if raw.startswith('T.launch_thread(threadIdx_x'):
                nt = get_first_digit(raw)
    assert szA != -1, 'A_shared size not found'
    assert szB != -1, 'B_shared size not found'
    assert nb != -1, 'block num not found'
    assert nt != -1, 'thread num not found'
    shared_size = (szA + szB) * 4
    with open('include/inc.h', 'w') as f:
        f.write('#include "tune.cu"\n')
        f.write(f'\n#define M {M}\n#define N {N}\n#define K {K}\n')
        f.write(f'\n#define SHARED_SIZE {shared_size}\n#define BLOCK_NUM {nb}\n#define THREAD_NUM {nt}\n')
    exe('nvcc speedTest.cu -o bin/cutlassMultiStage -I ../async_nt_cutlass/include -gencode=arch=compute_86,code=sm_86')
    exe(f'bin/cutlassMultiStage > {output_dir_name}/M={M}_N={N}_K={K}/eval_tune_result.txt')
    exe(f'cat {output_dir_name}/M={M}_N={N}_K={K}/eval_tune_result.txt')

def cutlassPerf(M=1024, N=1024, K=1024):
    with open('include/inc.h', 'w') as f:
        f.write('#include "tune.cu"\n')
        f.write(f'\n#define M {M}\n#define N {N}\n#define K {K}\n')
    exe('code ./callCutlass.cu')
    print('Please specify cutlass best perf kernel in callCutlass.cu. Press Enter to continue...', end='')
    input()
    exe(f'nvcc callCutlass.cu -o bin/cutlassMultiStage -I ../async_nt_cutlass/include -gencode=arch=compute_86,code=sm_86')
    if os.path.exists(f'{output_dir_name}/M={M}_N={N}_K={K}'):
        exe(f'bin/cutlassMultiStage > {output_dir_name}/M={M}_N={N}_K={K}/eval_cutlass_result.txt')
        exe(f'cat {output_dir_name}/M={M}_N={N}_K={K}/eval_cutlass_result.txt')
    else:
        exe('bin/cutlassMultiStage')

def oldPerf(M=1024, N=1024, K=1024):
    exe(f'cp {old_output_dir_name}/M={M}_N={N}_K={K}/cuda.cu include/tune.cu')
    nb, nt = -1, -1
    with open(f'{old_output_dir_name}/M={M}_N={N}_K={K}/lower.py', 'r') as f:
        for l in f.readlines():
            raw = l.strip()
            if raw.startswith('T.launch_thread(blockIdx_x'):
                nb = get_first_digit(raw)
            if raw.startswith('T.launch_thread(threadIdx_x'):
                nt = get_first_digit(raw)
    assert nb != -1, 'block num not found'
    assert nt != -1, 'thread num not found'
    with open('include/inc.h', 'w') as f:
        f.write('#include "tune.cu"\n')
        f.write(f'\n#define M {M}\n#define N {N}\n#define K {K}\n')
        f.write(f'\n#define SHARED_SIZE 0\n#define BLOCK_NUM {nb}\n#define THREAD_NUM {nt}\n')
    exe('nvcc speedTest.cu -o bin/cutlassMultiStage -gencode=arch=compute_86,code=sm_86')
    exe(f'bin/cutlassMultiStage > {old_output_dir_name}/M={M}_N={N}_K={K}/eval_old_tune_result.txt')
    exe(f'cat {old_output_dir_name}/M={M}_N={N}_K={K}/eval_old_tune_result.txt')

def run(M=1024, N=1024, K=1024):
    print("Async")
    perf(M, N, K)
    cutlassPerf(M, N, K) 
    print("Apache")
    oldPerf(M, N, K)
        


mp = {}
for i in range(1, len(sys.argv)):
    k, v = sys.argv[i].split('=')
    for l in k:
        mp[l] = v
try:
    run(**mp)
except KeyboardInterrupt:
    print('operation calceled.')