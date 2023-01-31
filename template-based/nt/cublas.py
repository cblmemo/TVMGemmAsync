def cublasPerf(M=1024, N=1024, K=1024, layout='nn'):
    M, N, K = int(M), int(N), int(K)
    # print(f'M={M} N={N} K={K}')
    import tvm
    from tvm import te
    import numpy as np
    from tvm.contrib import cublas
    import tvm.testing
    A_shape = (1, M, K) if layout == 'nn' else (1, K, M)
    B_shape = (1, K, N)
    C_shape = (1, M, N)
    in_dtype, out_dtype = "float32", "float32"
    rtol = 1e-5
    A = te.placeholder(A_shape, name="A", dtype=in_dtype)
    B = te.placeholder(B_shape, name="B", dtype=in_dtype)
    if layout == 'nn':
        C = cublas.batch_matmul(A, B, dtype=out_dtype)
    else:
        C = cublas.batch_matmul(A, B, transa=True, dtype=out_dtype)
    s = te.create_schedule(C.op)
    dev = tvm.cuda(0)
    mm = tvm.build(s, [A, B, C], "cuda", name="matmul")
    a = tvm.nd.array(np.random.uniform(size=A_shape).astype(A.dtype), dev)
    b = tvm.nd.array(np.random.uniform(size=B_shape).astype(B.dtype), dev)
    c = tvm.nd.array(np.zeros(C_shape, dtype=C.dtype), dev)
    mm(a, b, c)
    if layout == 'nn':
        std = np.matmul(a.numpy().astype(C.dtype), b.numpy().astype(C.dtype)).astype(C.dtype)
    else:
        std = np.matmul(a.numpy().astype(C.dtype).transpose(0, 2, 1), b.numpy().astype(C.dtype)).astype(C.dtype)
    tvm.testing.assert_allclose(
        c.numpy(),
        std,
        rtol=rtol,
    )
    time_f = mm.time_evaluator(mm.entry_name, dev=tvm.cuda(0), number=100)
    time = time_f(a, b, c).mean
    FLOPs = 2 * (M * N * K + M * N)
    GFLOPs = FLOPs / time / 1e9
    # print(f'cublas: {GFLOPs} GFLOPs')
    print('%.5f' % GFLOPs)

shapes = [
    'M=512 N=256 K=640',
    'M=512 N=384 K=256',
    'M=512 N=512 K=512',
    'M=896 N=896 K=896',
    'M=1024 N=1024 K=1024',
    'M=1152 N=1152 K=1152',
    'M=1536 N=1536 K=1536',
    'M=2048 N=2048 K=2048',
    'M=3072 N=3072 K=3072',
    'M=4096 N=4096 K=4096',
    'M=8192 N=8192 K=8192',
]

layout = 'nt'

print(f'{layout} perf result:')

for s in shapes:
    d = {'layout': layout}
    ls = s.split()
    for l in ls:
        k, v = l.split('=')
        d[k] = v
    cublasPerf(**d)