import os
import sys

db_path = './db'
output_path = './outputs'
old_db_path = './old_db'
old_output_path = './old_outputs'

def exe(s): print(s), os.system(s)
def tune(M=1024, N=1024, K=1024, t=5000, O=0):
    O = int(O)
    name = 'stochastic' if (O == 0 or O == 65536) else 'default'
    try:
        print(f'Now running as {name}, press Ctrl + C to confirm. Will auto start after 15 seconds.', end='', flush=True)
        import time
        time.sleep(15)
    except KeyboardInterrupt:
        print()
    if O == 0 or O == 65536:
        if os.path.exists(f'{db_path}/M={M}_N={N}_K={K}'): exe(f'rm -rf {db_path}/M={M}_N={N}_K={K}')
        exe(f'mkdir -p {db_path}/M={M}_N={N}_K={K}')
        if os.path.exists(f'{output_path}/M={M}_N={N}_K={K}'): exe(f'rm -rf {output_path}/M={M}_N={N}_K={K}')
        exe(f'mkdir -p {output_path}/M={M}_N={N}_K={K}')
        if O == 65536:
            exe(      f'python3 asyncStochasticGenerate.py {M} {N} {K} {t} >     {output_path}/M={M}_N={N}_K={K}/tune_output.txt'  )
        else:
            exe(f'nohup python3 asyncStochasticGenerate.py {M} {N} {K} {t} >     {output_path}/M={M}_N={N}_K={K}/tune_output.txt &')
    elif O == 1 or O == 65537:
        if os.path.exists(f'{old_db_path}/M={M}_N={N}_K={K}'): exe(f'rm -rf {old_db_path}/M={M}_N={N}_K={K}')
        exe(f'mkdir -p {old_db_path}/M={M}_N={N}_K={K}')
        if os.path.exists(f'{old_output_path}/M={M}_N={N}_K={K}'): exe(f'rm -rf {old_output_path}/M={M}_N={N}_K={K}')
        exe(f'mkdir -p {old_output_path}/M={M}_N={N}_K={K}')
        if O == 65537:
            exe(      f'python3             oldGenerate.py {M} {N} {K} {t} > old_outputs/M={M}_N={N}_K={K}/tune_output.txt'  )
        else:
            exe(f'nohup python3             oldGenerate.py {M} {N} {K} {t} > old_outputs/M={M}_N={N}_K={K}/tune_output.txt &')
    else:
        print('wrong `O` argument!')

mp = {}
for i in range(1, len(sys.argv)):
    k, v = sys.argv[i].split('=')
    for l in k:
        mp[l] = v
try:
    tune(**mp)
except KeyboardInterrupt:
    print('\nTune canceled.')