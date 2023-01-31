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
from tvm.tir.tensor_intrin.cuda import get_wmma_intrin_group
from tvm.script import tir as T
from tvm.target import Target
from tvm.tir import Schedule
from tvm.tir.schedule import Trace
from tvm.ir import IRModule

import os, sys
from sch_trace import apply_trace

N, H, W, C, K, R, S = 1, 56, 56, 64, 64, 3, 3


def multi_level_tiling_tensor_core(
    *,
    write_reuse_scope="shared",
    in_dtype="float16",
    out_dtype="float32",
    trans_b=False,
    use_software_pipeline=False,
) -> ms.schedule_rule.ScheduleRule:
    assert write_reuse_scope in ["shared", "global"]
    if not isinstance(in_dtype, list):
        in_dtype = [in_dtype]
    if not isinstance(out_dtype, list):
        out_dtype = [out_dtype]
    if not isinstance(trans_b, list):
        trans_b = [trans_b]
    return ms.schedule_rule.MultiLevelTilingTensorCore(
        intrin_groups=[
            get_wmma_intrin_group(write_reuse_scope, _in_dtype, _out_dtype, _trans_b)
            for _in_dtype in in_dtype
            for _out_dtype in out_dtype
            for _trans_b in trans_b
        ],
        structure="SSSRRSRS",
        tile_binds=["blockIdx.y", "blockIdx.x", "threadIdx.y"],
        max_innermost_factor=4,  # 64 // tensor intrin size
        vector_load_lens=[1, 2, 3, 4, 8, 16],
        reuse_read=ms.schedule_rule.ReuseType(
            req="must",
            levels=[4],
            scope="shared",
        ),
        reuse_write=ms.schedule_rule.ReuseType(
            req="must" if write_reuse_scope == "shared" else "no",
            levels=[2],
            scope=write_reuse_scope,
        ),
        use_software_pipeline=use_software_pipeline,
    )


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
    weight = te.placeholder((kernel_size, kernel_size, CI // groups, CO), name="weight", dtype=in_dtype)
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
            (padded[n, h * stride + rh * dilation, w * stride + rw * dilation, co // out_channel_per_group * channel_per_group + rc, ].astype(out_dtype) * weight[rh, rw, rc, co].astype(out_dtype)),
            axis=[rh, rw, rc],
        ),
        name="conv2d_nhwc",
    )
    return (inputs, weight, output)


def create_conv_workload() -> tir.PrimFunc:
    assert R == S
    return te.create_prim_func(conv2d_nhwc(N, H, W, C, K, R, 1, R // 2))  # type: ignore


def create_conv_workload_tensor_core() -> tir.PrimFunc:
    assert R == S
    return te.create_prim_func(conv2d_nhwc(N, H, W, C, K, R, 1, R // 2, 1, 1, "float16", "float16"))  # type: ignore


def eval_conv_sch(sch: tir.Schedule):
    mod = sch.mod
    rt_mod = tvm.build(mod, target="cuda")
    dev = tvm.cuda(0)
    input_np = np.random.uniform(size=(1, 56, 56, 64)).astype("float32")
    weight_np = np.random.uniform(size=(3, 3, 64, 64)).astype("float32")
    input_nd = tvm.nd.array(input_np, dev)
    weight_nd = tvm.nd.array(weight_np, dev)
    output_nd = tvm.nd.array(np.zeros((1, 56, 56, 64), dtype="float32"), dev)
    gemm_m, gemm_n, gemm_k = 1 * 56 * 56, 64, 3 * 3 * 64
    num_flop = 2 * (gemm_m * gemm_n * gemm_k + gemm_m * gemm_n)
    evaluator = rt_mod.time_evaluator("main", dev, number=10)
    print("Conv2d speed: %f GFLOPS" % (num_flop / evaluator(input_nd, weight_nd, output_nd).mean / 1e9))


def _design_space(mod, kind="cuda"):
    if kind == "cuda":
        return generate_design_space(
            kind=kind,
            mod=mod,
            target=Target("nvidia/geforce-rtx-3080"),
            types=ms.ScheduleRule,
        )
    assert kind == "cuda-tensorcore"
    return generate_design_space(
        kind="cuda",
        mod=mod,
        target=Target("nvidia/geforce-rtx-3080"),
        types=None,
        sch_rules=[multi_level_tiling_tensor_core(out_dtype="float16")],
    )


def print_traces(sketches, prefix=''):
    print(f'Traces Number: {len(sketches)}')
    os.system(f'rm bin/{prefix}trace*.py')
    for i, sch in enumerate(sketches):
        with open(f'bin/{prefix}trace{i}.py', 'w') as f:
            print('from tvm import tir', file=f)
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


def print_trace_and_exit(sketches, prefix=''):
    print_traces(sketches, prefix)
    exit(0)


def generate_default_tensorcore_trace_and_script():
    mod = create_conv_workload_tensor_core()
    actual = _design_space(mod, "cuda-tensorcore")
    print_traces(actual, 'tensorcore_')
    from bin.tensorcore_trace0 import apply_trace
    workload = create_conv_workload_tensor_core()
    ConvModule = tvm.IRModule({"main": workload.with_attr({"global_symbol": "main"})})
    sch = tir.Schedule(ConvModule)
    apply_trace(sch)
    with open('bin/script.py', 'w') as f:
        f.write(sch.mod.script())
    exit()


generate_default_tensorcore_trace_and_script()

conv_decision = [
    ("SamplePerfectTile", [1, 1, 1]),
    ("SamplePerfectTile", [4, 14, 1]),
    ("SamplePerfectTile", [7, 2, 4]),
    ("SamplePerfectTile", [2, 16, 2]),
    ("SamplePerfectTile", [1, 3]),
    ("SamplePerfectTile", [1, 3]),
    ("SamplePerfectTile", [16, 4]),
    ("SampleCategorical", 1),
    ("SampleCategorical", 1),
    ("SampleCategorical", 1),
    ("SampleCategorical", 3),
    ("SampleCategorical", 3),
    ("SampleCategorical", 1),
    ("SampleCategorical", 1),
    ("SampleCategorical", 0),
]
mod = create_conv_workload()
actual = _design_space(mod)
# print_trace_and_exit(actual)
print_decision_to_file(mod, actual[1], conv_decision)

sch = Schedule(mod)
apply_trace(sch)
sch.enter_postproc()
ms.postproc.RewriteCooperativeFetch().apply(sch)
eval_conv_sch(sch)

with open('bin/mlt_gen.py', 'w') as f:
    print(sch.mod.script(), file=f)
