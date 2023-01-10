import pandas as pd
from io import StringIO
import os
import sys
import traceback

# run 'cutlass_profiler' repeatedly for `REPEAT_TIME` in order to get more accurate result
REPEAT_TIME = 4
# path for cutlass `build` directory
# in most cases, it will be {$CUTLASS_HOME}/build
# this cutlass library should only build kernels with `nn` layout
cutlass_build_path = '~/async_nn_cutlass/build'
# path to store result
# for GEMM problem M=m, N=n, K=k, result will be stored to f'{result_path}/M={m}_N={n}_K={k}'
result_path = './cutlass_best_perf'

def buildDataFrame(f):
    csvText = ''
    start = False
    for line in f.readlines():
        if line.startswith('CSV Results:'):
            start = True
            continue
        if start and line != '\n':
            csvText += line
    csvTextIO = StringIO(csvText)
    df = pd.read_csv(csvTextIO)
    return df

def bestPerf(filename, async_only=False):
    with open(filename, 'r') as f:
        df = buildDataFrame(f)
    # filter of pipeline kernel
    if async_only:
        df = df[df["stages"].astype(str).str.contains("2") == False]
    idx = df['GFLOPs'].idxmax()
    maxGFLOPs = df['GFLOPs'][idx]
    for i in df['GFLOPs']:
        assert(i <= maxGFLOPs)
    return df['Operation'][idx], maxGFLOPs

def main(N=10):
    d = {}
    for i in range(1, len(sys.argv)):
        k, v = sys.argv[i].split('=')
        for l in k:
            d[l] = v
    
    m = 1024 if 'M' not in d else d['M']
    n = 1024 if 'N' not in d else d['N']
    k = 1024 if 'K' not in d else d['K']
    dirn = f'{result_path}/M={m}_N={n}_K={k}'
    if not os.path.exists(dirn):
        os.system(f'mkdir -p {dirn}')
    with open(f'{dirn}/best_perf.txt', 'w') as f:
        bestPerfList = []
        print(f'Profiler args: M={m}, N={n}, K={k}', file=f)
        f.flush()
        
        for i in range(N):
            print(f'executing task No.{i + 1} ...', file=f)
            f.flush()
            outputFilePath = f'./{dirn}/profiler_{i + 1}.out'
            if os.path.exists(outputFilePath): os.system(f'rm {outputFilePath}')
            os.system(f'{cutlass_build_path}/tools/profiler/cutlass_profiler --kernels=sgemm --m={m} --n={n} --k={k} >> {outputFilePath}')
            kernel, GFLOPs = bestPerf(outputFilePath)
            print(f'best perf kernel: {kernel}, GFLOPs: {GFLOPs}', file=f)
            f.flush()
            bestPerfList.append((kernel, GFLOPs))

        name2cnt = {}
        for p, mg in bestPerfList:
            if p not in name2cnt:
                name2cnt[p] = 0, mg
            name2cnt[p] = name2cnt[p][0] + 1, max(name2cnt[p][1], mg)
        
        print(name2cnt, file=f)
        mk, mv = '', -1
        for k, v in name2cnt.items():
            if v[0] > mv:
                mk, mv = k, v[0]
        print('Best perf kernel:', mk, 'GFLOPs:', name2cnt[mk][1], file=f)
        f.flush()
        # copy-paste best perf kernel to result for convenience
        os.system(f'cat {cutlass_build_path}/tools/library/generated/gemm/{mk}.cu >> {dirn}/best_perf.txt')

if __name__ == '__main__':
    try:
        main(REPEAT_TIME)
    except Exception as err:
        print(f'\nunexpected error: [{err}].')
        traceback.print_exc()