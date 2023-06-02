import os, sys
from util import get_mm_dirn, rdir, dbn
from tvm.tir.tensor_intrin import cuda  # get tensor intrin

tasks = [
    "M, N, K = 512, 256, 640",
    "M, N, K = 512, 384, 256",
    "M, N, K = 512, 512, 512",
    "M, N, K = 512, 768, 3072",
    "M, N, K = 512, 3072, 768",
    "M, N, K = 896, 896, 896",
    "M, N, K = 1024, 1024, 1024",
    "M, N, K = 1152, 1152, 1152",
    "M, N, K = 1536, 1536, 1536",
    "M, N, K = 2048, 2048, 2048",
    "M, N, K = 3072, 3072, 3072",
    "M, N, K = 4096, 4096, 4096",
    "M, N, K = 8192, 8192, 8192",
]

t = 1000

for ta in tasks:
    M, N, K = map(int, ta.split(' = ')[1].split(', '))
    dirn = get_mm_dirn(M, N, K, t)
    print(dirn)

    os.system(f'rm -rf {dbn}/{dirn}')
    os.system(f'rm -rf {rdir}/{dirn}')
    os.system(f'mkdir -p {rdir}/{dirn}')
    os.system(f'python3 GemmRuleGenerate.py {M} {N} {K} {t} > {rdir}/{dirn}/tune_outputs.txt')

    os.system(f'python3 gemmPerf.py {M} {N} {K} {t} > {rdir}/{dirn}/perf_result.txt')