import tvm
from tvm import te
import numpy as np
from tvm.contrib import cudnn
import tvm.testing

def cublasPerf(N, H, W, C, K, R, S, STR, PAD, DIL):
    P = ((H + 2 * PAD - R * DIL) // STR) + 1
    Q = ((W + 2 * PAD - S * DIL) // STR) + 1
    XT_shape = (N, H, W, C)
    WT_shape = (K, R, S, C)
    conv2d_shape = (N, P, Q, K)
    in_dtype, out_dtype = "float32", "float32"
    rtol = 1e-5
    XT = te.placeholder(XT_shape, name="X", dtype=in_dtype)
    WT = te.placeholder(WT_shape, name="W", dtype=in_dtype)
    conv2dT = cudnn.conv_forward(XT, WT, PAD, STR, DIL, 1, 1, -1, out_dtype)
    s = te.create_schedule(conv2dT.op)
    dev = tvm.cuda(0)
    conv = tvm.build(s, [XT, WT, conv2dT], "cuda", name="conv2d")
    x = tvm.nd.array(np.random.uniform(size=XT_shape).astype(XT.dtype), dev)
    w = tvm.nd.array(np.random.uniform(size=WT_shape).astype(WT.dtype), dev)
    res = tvm.nd.array(np.zeros(conv2d_shape, dtype=conv2dT.dtype), dev)
    conv(x, w, res)
    # if layout == 'nn':
    #     std = np.matmul(a.numpy().astype(C.dtype), b.numpy().astype(C.dtype)).astype(C.dtype)
    # else:
    #     std = np.matmul(a.numpy().astype(C.dtype).transpose(0, 2, 1), b.numpy().astype(C.dtype)).astype(C.dtype)
    # std = np.convolve
    # tvm.testing.assert_allclose(
    #     c.numpy(),
    #     std,
    #     rtol=rtol,
    # )
    time_f = conv.time_evaluator(conv.entry_name, dev=tvm.cuda(0), number=10)
    time = time_f(x, w, res).mean
    gemm_m, gemm_n, gemm_k = N * P * Q, K, R * S * C
    FLOPs = 2 * (gemm_m * gemm_n * gemm_k + gemm_m * gemm_n)
    GFLOPs = FLOPs / time / 1e9
    # print(f'cublas: {GFLOPs} GFLOPs')
    print('%.5f' % GFLOPs)
    return GFLOPs

shapes = [
    "N=1_H=224_W=224_C=3_K=64_R=7_S=7_STR=2_PAD=3_DIL=1",
    "N=1_H=56_W=56_C=64_K=64_R=1_S=1_STR=1_PAD=0_DIL=1",
    "N=1_H=56_W=56_C=64_K=64_R=3_S=3_STR=1_PAD=1_DIL=1",
    "N=1_H=56_W=56_C=64_K=256_R=1_S=1_STR=1_PAD=0_DIL=1",
    "N=1_H=56_W=56_C=256_K=64_R=1_S=1_STR=1_PAD=0_DIL=1",
    "N=1_H=56_W=56_C=256_K=128_R=1_S=1_STR=2_PAD=0_DIL=1",
    "N=1_H=28_W=28_C=128_K=128_R=3_S=3_STR=1_PAD=1_DIL=1",
    "N=1_H=28_W=28_C=128_K=512_R=1_S=1_STR=1_PAD=0_DIL=1",
    "N=1_H=28_W=28_C=512_K=128_R=1_S=1_STR=1_PAD=0_DIL=1",
    "N=1_H=28_W=28_C=512_K=256_R=1_S=1_STR=2_PAD=0_DIL=1",
    "N=1_H=14_W=14_C=256_K=256_R=3_S=3_STR=1_PAD=1_DIL=1",
    "N=1_H=14_W=14_C=256_K=1024_R=1_S=1_STR=1_PAD=0_DIL=1",
    "N=1_H=14_W=14_C=1024_K=256_R=1_S=1_STR=1_PAD=0_DIL=1",
    "N=1_H=14_W=14_C=1024_K=512_R=1_S=1_STR=2_PAD=0_DIL=1",
    "N=1_H=7_W=7_C=512_K=512_R=3_S=3_STR=1_PAD=1_DIL=1",
    "N=1_H=7_W=7_C=512_K=2048_R=1_S=1_STR=1_PAD=0_DIL=1",
    "N=1_H=7_W=7_C=2048_K=512_R=1_S=1_STR=1_PAD=0_DIL=1",
]

res = []

for s in shapes:
    d = dict()
    ls = s.split('_')
    for l in ls:
        k, v = l.split('=')
        d[k] = int(v)
    # res.append((cublasPerf(**d), d))
    res.append(cublasPerf(**d))

for r in res:
    print(r)