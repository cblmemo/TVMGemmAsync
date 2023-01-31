"""Tests for MetaSchedule search space on CUDA"""
from typing import Tuple, List

import tvm
import numpy as np
from tvm import te, tir, topi
from tvm import meta_schedule as ms
from tvm.meta_schedule.testing.space_generation import (
    check_sketches,
    generate_design_space,
    print_sketches,
)
from tvm.meta_schedule.testing.te_workload import create_te_workload
from tvm.script import tir as T
from tvm.target import Target
from tvm.tir import Schedule
from tvm.tir.schedule import Trace
from tvm.ir import IRModule

import os, sys
from sch_trace import apply_trace

B, M, N, K = 10, 1024, 1024, 1024
use_bmm = False if len(sys.argv) == 1 or sys.argv[1] == "mm" else False


def batch_matmul_nkkm(  # pylint: disable=invalid-name,missing-docstring
        B: int,
        N: int,
        M: int,
        K: int,
        in_dtype: str = "float32",
        out_dtype: str = "float32",
) -> Tuple[te.Tensor, te.Tensor, te.Tensor]:
    x = te.placeholder((B, N, K), name="A", dtype=in_dtype)
    y = te.placeholder((B, K, M), name="B", dtype=in_dtype)
    k = te.reduce_axis((0, K), name="k")
    z = te.compute(  # pylint: disable=invalid-name
        (B, N, M),
        lambda b, i, j: te.sum(
            x[b][i][k].astype(out_dtype) * y[b][k][j].astype(out_dtype),
            axis=[k],
        ),
        name="Y",
    )
    return (x, y, z)


def matmul_nkkm(  # pylint: disable=invalid-name,missing-docstring
        N: int,
        M: int,
        K: int,
        in_dtype: str = "float32",
        out_dtype: str = "float32",
) -> Tuple[te.Tensor, te.Tensor, te.Tensor]:
    x = te.placeholder((N, K), name="A", dtype=in_dtype)
    y = te.placeholder((K, M), name="B", dtype=in_dtype)
    k = te.reduce_axis((0, K), name="k")
    z = te.compute(  # pylint: disable=invalid-name
        (N, M),
        lambda i, j: te.sum(
            x[i][k].astype(out_dtype) * y[k][j].astype(out_dtype),
            axis=[k],
        ),
        name="Y",
    )
    return (x, y, z)


def conv2d_nhwc(  # pylint: disable=invalid-name,missing-docstring
    N: int,
    H: int,
    W: int,
    CI: int,
    CO: int,
    kernel_size: int,
    stride: int = 1,
    padding: int = 0,
    dilation: int = 1,
    groups: int = 1,
    in_dtype: str = "float32",
    out_dtype: str = "float32",
) -> Tuple[te.Tensor, te.Tensor, te.Tensor]:
    inputs = te.placeholder((N, H, W, CI), name="inputs", dtype=in_dtype)
    weight = te.placeholder(
        (kernel_size, kernel_size, CI // groups, CO), name="weight", dtype=in_dtype
    )
    batch_size, in_h, in_w, _ = inputs.shape
    k_h, k_w, channel_per_group, out_channel = weight.shape
    out_channel_per_group = out_channel // groups

    out_h = (in_h + 2 * padding - dilation * (k_h - 1) - 1) // stride + 1
    out_w = (in_w + 2 * padding - dilation * (k_w - 1) - 1) // stride + 1
    rh = te.reduce_axis((0, k_h), name="rh")
    rw = te.reduce_axis((0, k_w), name="rw")
    rc = te.reduce_axis((0, channel_per_group), name="rc")

    padded = topi.nn.pad(inputs, [0, padding, padding, 0])
    output = te.compute(
        (batch_size, out_h, out_w, out_channel),
        lambda n, h, w, co: te.sum(
            (
                padded[
                    n,
                    h * stride + rh * dilation,
                    w * stride + rw * dilation,
                    co // out_channel_per_group * channel_per_group + rc,
                ].astype(out_dtype)
                * weight[rh, rw, rc, co].astype(out_dtype)
            ),
            axis=[rh, rw, rc],
        ),
        name="conv2d_nhwc",
    )
    return (inputs, weight, output)


def create_bmm_workload() -> tir.PrimFunc:
    return te.create_prim_func(batch_matmul_nkkm(B, M, N, K))  # type: ignore


def create_mm_workload() -> tir.PrimFunc:
    return te.create_prim_func(matmul_nkkm(M, N, K))  # type: ignore


def create_conv_workload() -> tir.PrimFunc:
    return te.create_prim_func(conv2d_nhwc(1, 224, 224, 3, 64, 7, 2, 3))  # type: ignore


def _design_space(mod):
    return generate_design_space(
        kind="cuda",
        mod=mod,
        target=Target("nvidia/geforce-rtx-3080"),
        types=ms.ScheduleRule,
    )


def print_traces(sketches):
    print(f'Traces Number: {len(sketches)}')
    os.system('rm bin/trace*.py')
    for i, sch in enumerate(sketches):
        with open(f'bin/trace{i}.py', 'w') as f:
            print(sch.trace, file=f)


def print_decision_to_file(mod: IRModule, sketches: List[Schedule], decision: List[Tuple[str, List[int]]]):
    if isinstance(sketches, list):
        assert len(sketches) == 1
        sketch = sketches[0]
    else:
        assert isinstance(sketches, Schedule)
        sketch = sketches
    i = 0
    new_decisions = {}
    for inst in sketch.trace.insts:
        if not inst.kind.name.startswith("Sample"):
            continue
        assert i < len(decision)
        if inst.kind.name == decision[i][0]:
            new_decisions[inst] = decision[i][1]
            i += 1
    assert len(new_decisions) == len(decision)
    # print(new_decisions)
    sch = Schedule(mod)
    Trace(
        insts=sketch.trace.insts,
        decisions=new_decisions,
    ).apply_to_schedule(sch, remove_postproc=True)
    with open('sch_trace.py', 'w') as f:
        print('from tvm import tir', file=f)
        print('from tvm.tir import floormod, floordiv', file=f)
        print(sch.trace, file=f)


def print_trace_to_file(sketches):
    if isinstance(sketches, list):
        assert len(sketches) == 1
        sketch = sketches[0]
    else:
        assert isinstance(sketches, Schedule)
        sketch = sketches
    with open('sch_trace.py', 'w') as f:
        print('from tvm import tir', file=f)
        print('from tvm.tir import floormod, floordiv', file=f)
        print(sketch.trace, file=f)


def print_trace_and_exit(sketches):
    print_traces(sketches)
    exit(0)


# mod = create_conv_workload()
# actual = _design_space(mod)
# print_trace_and_exit(actual)


if not use_bmm:
    mm_decision = [
        ("SamplePerfectTile", [8, 16, 8]),
        ("SamplePerfectTile", [8, 16, 8]),
        ("SamplePerfectTile", [128, 8]),
        ("SampleCategorical", 3),
        ("SampleCategorical", 3),
        ("SampleCategorical", 3),
        ("SampleCategorical", 3),
        ("SampleCategorical", 3),
        ("SampleCategorical", 3),
        ("SampleCategorical", 3),
        ("SampleCategorical", 1),
    ]
    mod = create_mm_workload()
    actual = _design_space(mod)
    # print_trace_and_exit(actual)
    print_decision_to_file(mod, actual[2], mm_decision)  # 2: only A_smem is transposed
else:
    bmm_decision = [
        ("SamplePerfectTile", [B, 1, 1]),
        ("SamplePerfectTile", [8, 16, 8]),
        ("SamplePerfectTile", [8, 16, 8]),
        ("SamplePerfectTile", [128, 8]),
        ("SampleCategorical", 3),
        ("SampleCategorical", 3),
        ("SampleCategorical", 3),
        ("SampleCategorical", 3),
        ("SampleCategorical", 3),
        ("SampleCategorical", 3),
        ("SampleCategorical", 3),
        ("SampleCategorical", 1),
    ]
    mod = create_bmm_workload()
    actual = _design_space(mod)
    print_decision_to_file(mod, actual[2], bmm_decision)

sch = Schedule(mod)
apply_trace(sch)
sch.enter_postproc()
ms.postproc.RewriteCooperativeFetch().apply(sch)

with open('bin/mlt_gen.py', 'w') as f:
    print(sch.mod.script(), file=f)

if not use_bmm:
    rt_mod = tvm.build(sch.mod, target="cuda")
    a_np = np.random.rand(M, K).astype("float32")
    b_np = np.random.rand(K, N).astype("float32")
    c_np = a_np @ b_np
    a_tvm = tvm.nd.array(a_np, device=tvm.cuda(0))
    b_tvm = tvm.nd.array(b_np, device=tvm.cuda(0))
    c_tvm = tvm.nd.array(np.empty((M, N)).astype("float32"), device=tvm.cuda(0))
    rt_mod(a_tvm, b_tvm, c_tvm)
    assert np.allclose(c_tvm.numpy(), c_np)
    time_f = rt_mod.time_evaluator(rt_mod.entry_name, dev=tvm.cuda(0), number=100)
    time = time_f(a_tvm, b_tvm, c_tvm).mean
    flop = (M * N * K + M * N) * 2
    print("GFLOPS: %.2f" % (flop / time / 1e9))
else:
    rt_mod = tvm.build(sch.mod, target="cuda")
    a_np = np.random.rand(B, M, K).astype("float32")
    b_np = np.random.rand(B, K, N).astype("float32")
    c_np = a_np @ b_np
    a_tvm = tvm.nd.array(a_np, device=tvm.cuda(0))
    b_tvm = tvm.nd.array(b_np, device=tvm.cuda(0))
    c_tvm = tvm.nd.array(np.empty((B, M, N)).astype("float32"), device=tvm.cuda(0))
    rt_mod(a_tvm, b_tvm, c_tvm)
    assert np.allclose(c_tvm.numpy(), c_np)
    time_f = rt_mod.time_evaluator(rt_mod.entry_name, dev=tvm.cuda(0), number=100)
    time = time_f(a_tvm, b_tvm, c_tvm).mean
    flop = (M * N * K + M * N) * 2 * B
    print("GFLOPS: %.2f" % (flop / time / 1e9))