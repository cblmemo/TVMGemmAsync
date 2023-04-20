import sys

sys.dont_write_bytecode = True

rdir = 'tensorcore_outputs'

dbn = 'tensorcore_db'

dtype = "float16"

def get_mm_dirn(M, N, K, t):
    return f'M={M}_N={N}_K={K}_t={t}'

def get_bmm_dirn(B, M, N, K, t):
    return f'B={B}_M={M}_N={N}_K={K}_t={t}'

def get_conv_dirn(N, H, W, C, K, R, S, STR, PAD, DIL, t):
    return f'N={N}_H={H}_W={W}_C={C}_K={K}_R={R}_S={S}_STR={STR}_PAD={PAD}_DIL={DIL}_t={t}'

