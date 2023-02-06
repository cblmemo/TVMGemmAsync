"""Tests for MetaSchedule search space on CUDA"""
from typing import Tuple, List

import tvm
import numpy as np
import time
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
from conv_utils import create_conv_workload, create_conv_workload_tensor_core, eval_conv_sch


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
        intrin_groups=[get_wmma_intrin_group(write_reuse_scope, _in_dtype, _out_dtype, _trans_b) for _in_dtype in in_dtype for _out_dtype in out_dtype for _trans_b in trans_b],
        # intrin_groups=[{
        #     "init": "wmma_fill_16x16x16_f16",
        #     "load_a": "wmma_load_16x16x16_f16_a",
        #     "load_b": "wmma_load_16x16x16_f16_b",
        #     "compute": "pipelined_mma_float32",
        #     "store": "wmma_store_16x16x16_f16_shared",
        # }],
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
            print('from tvm import tir\nfrom tvm.tir import floordiv, floormod', file=f)
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


# generate_default_tensorcore_trace_and_script()


def generate_default_cudacore_trace_and_script():
    mod = create_conv_workload(1, 14, 14, 256, 1024, 1, 1, 1, 0, 1)
    actual = _design_space(mod, "cuda")
    print_traces(actual, 'cudacore_')
    from bin.cudacore_trace0 import apply_trace
    ConvModule = tvm.IRModule({"main": mod.with_attr({"global_symbol": "main"})})
    sch = tir.Schedule(ConvModule)
    apply_trace(sch)
    with open('bin/script.py', 'w') as f:
        f.write(sch.mod.script())
    exit()


generate_default_cudacore_trace_and_script()


def inject_decision_and_eval():
    N, H, W, C, K, R, S, STR, PAD, DIL = 1, 14, 14, 256, 1024, 1, 1, 1, 0, 1
    # old_conv_decision = [
    #     ("SamplePerfectTile", [1, 1, 1]),
    #     ("SamplePerfectTile", [4, 14, 1]),
    #     ("SamplePerfectTile", [7, 2, 4]),
    #     ("SamplePerfectTile", [2, 16, 2]),
    #     ("SamplePerfectTile", [1, 3]),
    #     ("SamplePerfectTile", [1, 3]),
    #     ("SamplePerfectTile", [16, 4]),
    #     ("SampleCategorical", 1),
    #     ("SampleCategorical", 1),
    #     ("SampleCategorical", 1),
    #     ("SampleCategorical", 3),
    #     ("SampleCategorical", 3),
    #     ("SampleCategorical", 1),
    #     ("SampleCategorical", 1),
    #     ("SampleCategorical", 0),
    # ]
    conv_decision = [
        # ("SamplePerfectTile", [98, 16, 2]),
        # ("SamplePerfectTile", [1, 8, 8]),
        # ("SamplePerfectTile", [36, 16]),
        ("SamplePerfectTile", [56, 1, 8, 7, 1]),
        ("SamplePerfectTile", [1, 1, 16, 4, 1]),
        ("SamplePerfectTile", [18, 32, 1]),
        ("SampleCategorical", 3),
        ("SampleCategorical", 3),
        ("SampleCategorical", 3),
        ("SampleCategorical", 3),
        ("SampleCategorical", 3),
        ("SampleCategorical", 3),
        ("SampleCategorical", 1),
    ]
    mod = create_conv_workload(N, H, W, C, K, R, S, STR, PAD, DIL)
    actual = _design_space(mod)
    print_trace_and_exit(actual, 'SSSRRSRS_')
    for i in range(1):
        print(i)
        with open(f'bin/mlt_trace{i}.py', 'w') as f:
            print(actual[i].trace, file=f)
        print_decision_to_file(mod, actual[i], conv_decision)

        sch = Schedule(mod)
        apply_trace(sch)
        sch.enter_postproc()
        ms.postproc.RewriteCooperativeFetch().apply(sch)

        with open(f'bin/mlt_gen{i}.py', 'w') as f:
            print(sch.mod.script(), file=f)
        
        eval_conv_sch(sch, N, H, W, C, K, R, S, STR, PAD, DIL)

        time.sleep(3)


inject_decision_and_eval()


def arbitrary_trace():

    def apply_trace(sch: tir.Schedule) -> None:
        b0 = sch.get_block(name="PadInput", func_name="main")
        b1 = sch.get_block(name="conv2d_nhwc", func_name="main")
        b2 = sch.get_block(name="root", func_name="main")
        sch.annotate(block_or_loop=b1, ann_key="meta_schedule.tiling_structure", ann_val="SSRRS")
        b3 = sch.reindex(block=b1, buffer=("write", 0))
        b4 = sch.reindex(block=b1, buffer=("read", 0))
        b5 = sch.reindex(block=b1, buffer=("read", 1))
        sch.transform_layout(block=b1, buffer=("read", 0), index_map=lambda v_n, v_h, v_w, v_rh, v_rw, v_rc: (
            (((v_n * 3136) + (v_h * 56)) + v_w),
            (((v_rh * 192) + (v_rw * 64)) + v_rc),
        ), pad_value=None)
        sch.transform_layout(block=b1, buffer=("read", 1), index_map=lambda v_co, v_rh, v_rw, v_rc: (
            (((v_rh * 192) + (v_rw * 64)) + v_rc),
            v_co,
        ), pad_value=None)
        sch.transform_layout(block=b1, buffer=("write", 0), index_map=lambda v_n, v_h, v_w, v_co: (
            (((v_n * 3136) + (v_h * 56)) + v_w),
            v_co,
        ), pad_value=None)
        sch.transform_block_layout(block=b3, index_map=lambda v_n, v_h, v_w, v_co: (
            (((v_n * 3136) + (v_h * 56)) + v_w),
            v_co,
        ))
        sch.transform_block_layout(block=b4, index_map=lambda v_n, v_h, v_w, v_rh, v_rw, v_rc: (
            (((v_n * 3136) + (v_h * 56)) + v_w),
            (((v_rh * 192) + (v_rw * 64)) + v_rc),
        ))
        sch.transform_block_layout(block=b5, index_map=lambda v_co, v_rh, v_rw, v_rc: (
            (((v_rh * 192) + (v_rw * 64)) + v_rc),
            v_co,
        ))
        sch.transform_block_layout(block=b1, index_map=lambda v_n, v_h, v_w, v_co, v_rh, v_rw, v_rc: (
            (((v_n * 3136) + (v_h * 56)) + v_w),
            v_co,
            (((v_rh * 192) + (v_rw * 64)) + v_rc),
        ))
        l6, l7, l8 = sch.get_loops(block=b1)
        v9, v10, v11 = sch.sample_perfect_tile(loop=l6, n=3, max_innermost_factor=64, decision=[56, 8, 7])
        l12, l13, l14 = sch.split(loop=l6, factors=[v9, v10, v11], preserve_unit_iters=True)
        v15, v16, v17 = sch.sample_perfect_tile(loop=l7, n=3, max_innermost_factor=64, decision=[1, 16, 4])
        l18, l19, l20 = sch.split(loop=l7, factors=[v15, v16, v17], preserve_unit_iters=True)
        v21, v22 = sch.sample_perfect_tile(loop=l8, n=2, max_innermost_factor=64, decision=[18, 32])
        l23, l24 = sch.split(loop=l8, factors=[v21, v22], preserve_unit_iters=True)
        sch.reorder(l12, l18, l13, l19, l23, l24, l14, l20)
        l25 = sch.fuse(l12, l18, preserve_unit_iters=True)
        sch.bind(loop=l25, thread_axis="blockIdx.x")
        l26 = sch.fuse(l13, l19, preserve_unit_iters=True)
        sch.bind(loop=l26, thread_axis="threadIdx.x")
        sch.annotate(block_or_loop=b1, ann_key="meta_schedule.thread_extent_low_inclusive", ann_val=32)
        sch.annotate(block_or_loop=b1, ann_key="meta_schedule.thread_extent_high_inclusive", ann_val=1024)
        b27 = sch.cache_write(block=b1, write_buffer_index=0, storage_scope="local")
        sch.reverse_compute_at(block=b27, loop=l26, preserve_unit_loops=True, index=-1)
        sch.reverse_compute_inline(block=b3)
        b28 = sch.cache_read(block=b1, read_buffer_index=0, storage_scope="shared", consumer_blocks=[b1])
        sch.compute_at(block=b28, loop=l23, preserve_unit_loops=True, index=-1)
        l29, l30, l31, l32, l33 = sch.get_loops(block=b28)
        l34 = sch.fuse(l32, l33, preserve_unit_iters=True)
        v35 = sch.sample_categorical(candidates=[1, 2, 3, 4], probs=[0.25, 0.25, 0.25, 0.25], decision=2)
        sch.annotate(block_or_loop=b28, ann_key="meta_schedule.cooperative_fetch", ann_val=v35)
        sch.annotate(block_or_loop=b28, ann_key="double_buffer_scope", ann_val=0)
        b36 = sch.cache_read(block=b28, read_buffer_index=0, storage_scope="local", consumer_blocks=[b28])
        sch.compute_at(block=b36, loop=l23, preserve_unit_loops=True, index=-1)
        l37, l38, l39, l40, l41 = sch.get_loops(block=b36)
        l42 = sch.fuse(l40, l41, preserve_unit_iters=True)
        v43 = sch.sample_categorical(candidates=[1, 2, 3, 4], probs=[0.25, 0.25, 0.25, 0.25], decision=0)
        sch.annotate(block_or_loop=b36, ann_key="meta_schedule.cooperative_fetch", ann_val=v43)
        b44 = sch.cache_read(block=b1, read_buffer_index=1, storage_scope="shared", consumer_blocks=[b1])
        sch.compute_at(block=b44, loop=l23, preserve_unit_loops=True, index=-1)
        l45, l46, l47, l48, l49 = sch.get_loops(block=b44)
        l50 = sch.fuse(l48, l49, preserve_unit_iters=True)
        v51 = sch.sample_categorical(candidates=[1, 2, 3, 4], probs=[0.25, 0.25, 0.25, 0.25], decision=1)
        sch.annotate(block_or_loop=b44, ann_key="meta_schedule.cooperative_fetch", ann_val=v51)
        sch.annotate(block_or_loop=b44, ann_key="double_buffer_scope", ann_val=0)
        b52 = sch.cache_read(block=b44, read_buffer_index=0, storage_scope="local", consumer_blocks=[b44])
        sch.compute_at(block=b52, loop=l23, preserve_unit_loops=True, index=-1)
        l53, l54, l55, l56, l57 = sch.get_loops(block=b52)
        l58 = sch.fuse(l56, l57, preserve_unit_iters=True)
        v59 = sch.sample_categorical(candidates=[1, 2, 3, 4], probs=[0.25, 0.25, 0.25, 0.25], decision=1)
        sch.annotate(block_or_loop=b52, ann_key="meta_schedule.cooperative_fetch", ann_val=v59)
        b60 = sch.cache_read(block=b1, read_buffer_index=0, storage_scope="local", consumer_blocks=[b1])
        sch.compute_at(block=b60, loop=l24, preserve_unit_loops=True, index=-1)
        l61, l62, l63, l64, l65, l66 = sch.get_loops(block=b60)
        l67 = sch.fuse(l65, l66, preserve_unit_iters=True)
        v68 = sch.sample_categorical(candidates=[1, 2, 3, 4], probs=[0.25, 0.25, 0.25, 0.25], decision=1)
        l69, l70 = sch.split(loop=l67, factors=[None, v68], preserve_unit_iters=True)
        sch.unroll(loop=l69)
        sch.vectorize(loop=l70)
        b71 = sch.cache_read(block=b1, read_buffer_index=1, storage_scope="local", consumer_blocks=[b1])
        sch.compute_at(block=b71, loop=l24, preserve_unit_loops=True, index=-1)
        l72, l73, l74, l75, l76, l77 = sch.get_loops(block=b71)
        l78 = sch.fuse(l76, l77, preserve_unit_iters=True)
        v79 = sch.sample_categorical(candidates=[1, 2, 3, 4], probs=[0.25, 0.25, 0.25, 0.25], decision=0)
        l80, l81 = sch.split(loop=l78, factors=[None, v79], preserve_unit_iters=True)
        sch.unroll(loop=l80)
        sch.vectorize(loop=l81)
        sch.compute_inline(block=b4)
        sch.compute_inline(block=b5)
        l82 = sch.fuse(l23, preserve_unit_iters=True)
        sch.annotate(block_or_loop=l82, ann_key="software_pipeline_order", ann_val=[0, 3, 1, 4, 2])
        sch.annotate(block_or_loop=l82, ann_key="software_pipeline_stage", ann_val=[0, 0, 0, 0, 1])
        b83 = sch.decompose_reduction(block=b1, loop=l82)
        l84 = sch.fuse(l24, preserve_unit_iters=True)
        sch.unroll(loop=l84)
        sch.compute_inline(block=b0)
        v85 = sch.sample_categorical(candidates=[0, 16, 64, 512, 1024], probs=[0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001], decision=1)
        sch.annotate(block_or_loop=b2, ann_key="meta_schedule.unroll_explicit", ann_val=v85)
        sch.enter_postproc()
        sch.unannotate(block_or_loop=b28, ann_key="meta_schedule.cooperative_fetch")
        l86, l87, l88, l89 = sch.get_loops(block=b28)
        l90, l91 = sch.split(loop=l89, factors=[None, 128], preserve_unit_iters=True)
        sch.bind(loop=l91, thread_axis="threadIdx.x")
        sch.unannotate(block_or_loop=b36, ann_key="meta_schedule.cooperative_fetch")
        l92, l93, l94, l95 = sch.get_loops(block=b36)
        l96, l97 = sch.split(loop=l95, factors=[None, 128], preserve_unit_iters=True)
        sch.bind(loop=l97, thread_axis="threadIdx.x")
        sch.unannotate(block_or_loop=b44, ann_key="meta_schedule.cooperative_fetch")
        l98, l99, l100, l101 = sch.get_loops(block=b44)
        l102, l103, l104 = sch.split(loop=l101, factors=[None, 128, 2], preserve_unit_iters=True)
        sch.vectorize(loop=l104)
        sch.bind(loop=l103, thread_axis="threadIdx.x")
        sch.unannotate(block_or_loop=b52, ann_key="meta_schedule.cooperative_fetch")
        l105, l106, l107, l108 = sch.get_loops(block=b52)
        l109, l110, l111 = sch.split(loop=l108, factors=[None, 128, 2], preserve_unit_iters=True)
        sch.vectorize(loop=l111)
        sch.bind(loop=l110, thread_axis="threadIdx.x")
        b112 = sch.get_block(name="root", func_name="main")
        sch.unannotate(block_or_loop=b112, ann_key="meta_schedule.unroll_explicit")
        b113, b114, b115, b116, b117, b118, b119, b120, b121 = sch.get_child_blocks(b112)
        l122, l123, l124, l125 = sch.get_loops(block=b113)
        sch.annotate(block_or_loop=l122, ann_key="pragma_auto_unroll_max_step", ann_val=16)
        sch.annotate(block_or_loop=l122, ann_key="pragma_unroll_explicit", ann_val=1)
        l126, l127, l128, l129, l130 = sch.get_loops(block=b114)
        sch.annotate(block_or_loop=l126, ann_key="pragma_auto_unroll_max_step", ann_val=16)
        sch.annotate(block_or_loop=l126, ann_key="pragma_unroll_explicit", ann_val=1)
        l131, l132, l133, l134, l135 = sch.get_loops(block=b115)
        sch.annotate(block_or_loop=l131, ann_key="pragma_auto_unroll_max_step", ann_val=16)
        sch.annotate(block_or_loop=l131, ann_key="pragma_unroll_explicit", ann_val=1)
        l136, l137, l138, l139, l140, l141 = sch.get_loops(block=b116)
        sch.annotate(block_or_loop=l136, ann_key="pragma_auto_unroll_max_step", ann_val=16)
        sch.annotate(block_or_loop=l136, ann_key="pragma_unroll_explicit", ann_val=1)
        l142, l143, l144, l145, l146, l147 = sch.get_loops(block=b117)
        sch.annotate(block_or_loop=l142, ann_key="pragma_auto_unroll_max_step", ann_val=16)
        sch.annotate(block_or_loop=l142, ann_key="pragma_unroll_explicit", ann_val=1)
        l148, l149, l150, l151, l152, l153 = sch.get_loops(block=b118)
        sch.annotate(block_or_loop=l148, ann_key="pragma_auto_unroll_max_step", ann_val=16)
        sch.annotate(block_or_loop=l148, ann_key="pragma_unroll_explicit", ann_val=1)
        l154, l155, l156, l157, l158, l159 = sch.get_loops(block=b119)
        sch.annotate(block_or_loop=l154, ann_key="pragma_auto_unroll_max_step", ann_val=16)
        sch.annotate(block_or_loop=l154, ann_key="pragma_unroll_explicit", ann_val=1)
        l160, l161, l162, l163, l164, l165 = sch.get_loops(block=b120)
        sch.annotate(block_or_loop=l160, ann_key="pragma_auto_unroll_max_step", ann_val=16)
        sch.annotate(block_or_loop=l160, ann_key="pragma_unroll_explicit", ann_val=1)
        l166, l167, l168, l169 = sch.get_loops(block=b121)
        sch.annotate(block_or_loop=l166, ann_key="pragma_auto_unroll_max_step", ann_val=16)
        sch.annotate(block_or_loop=l166, ann_key="pragma_unroll_explicit", ann_val=1)

    mod = create_conv_workload()
    sch = Schedule(mod)
    apply_trace(sch)
    # sch.enter_postproc()
    # ms.postproc.RewriteCooperativeFetch().apply(sch)
    with open(f'bin/arbitrary_trace_script.py', 'w') as f:
        print(sch.mod.script(), file=f)
    eval_conv_sch(sch)


# arbitrary_trace()
