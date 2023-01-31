import sys
import os
import numpy as np
import traceback

import tvm
import tvm.testing
from tvm import te, topi, tir
from tvm import meta_schedule as ms
from tvm.target import Target


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
):
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


def create_conv_module():
    conv_workload = conv2d_nhwc(1, 56, 56, 64, 64, 3, 1, 1)
    return tvm.IRModule({"main": te.create_prim_func(conv_workload).with_attr({"global_symbol": "main"})})


def eval_sch(sch: tir.Schedule):
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
    # rt_mod(input_nd, weight_nd, output_nd)
    # tvm.testing.assert_allclose(C_nd.numpy(), np.dot(A_np.T, B_np), rtol=1e-5)


def apply_trace(sch: tir.Schedule) -> None:
    b0 = sch.get_block(name="PadInput", func_name="main")
    b1 = sch.get_block(name="conv2d_nhwc", func_name="main")
    b2 = sch.get_block(name="root", func_name="main")
    sch.annotate(block_or_loop=b1, ann_key="meta_schedule.tiling_structure", ann_val="SSRRS")
    l3, l4, l5, l6, l7, l8, l9 = sch.get_loops(block=b1)
    v10, v11, v12 = sch.sample_perfect_tile(loop=l3, n=3, max_innermost_factor=64, decision=[1, 1, 1])
    l13, l14, l15 = sch.split(loop=l3, factors=[v10, v11, v12], preserve_unit_iters=True)
    v16, v17, v18 = sch.sample_perfect_tile(loop=l4, n=3, max_innermost_factor=64, decision=[4, 14, 1])
    l19, l20, l21 = sch.split(loop=l4, factors=[v16, v17, v18], preserve_unit_iters=True)
    v22, v23, v24 = sch.sample_perfect_tile(loop=l5, n=3, max_innermost_factor=64, decision=[7, 2, 4])
    l25, l26, l27 = sch.split(loop=l5, factors=[v22, v23, v24], preserve_unit_iters=True)
    v28, v29, v30 = sch.sample_perfect_tile(loop=l6, n=3, max_innermost_factor=64, decision=[2, 16, 2])
    l31, l32, l33 = sch.split(loop=l6, factors=[v28, v29, v30], preserve_unit_iters=True)
    v34, v35 = sch.sample_perfect_tile(loop=l7, n=2, max_innermost_factor=64, decision=[1, 3])
    l36, l37 = sch.split(loop=l7, factors=[v34, v35], preserve_unit_iters=True)
    v38, v39 = sch.sample_perfect_tile(loop=l8, n=2, max_innermost_factor=64, decision=[1, 3])
    l40, l41 = sch.split(loop=l8, factors=[v38, v39], preserve_unit_iters=True)
    v42, v43 = sch.sample_perfect_tile(loop=l9, n=2, max_innermost_factor=64, decision=[16, 4])
    l44, l45 = sch.split(loop=l9, factors=[v42, v43], preserve_unit_iters=True)
    sch.reorder(l13, l19, l25, l31, l14, l20, l26, l32, l36, l40, l44, l37, l41, l45, l15, l21, l27, l33)
    l46 = sch.fuse(l13, l19, l25, l31, preserve_unit_iters=True)
    sch.bind(loop=l46, thread_axis="blockIdx.x")
    l47 = sch.fuse(l14, l20, l26, l32, preserve_unit_iters=True)
    sch.bind(loop=l47, thread_axis="threadIdx.x")
    sch.annotate(block_or_loop=b1, ann_key="meta_schedule.thread_extent_low_inclusive", ann_val=32)
    sch.annotate(block_or_loop=b1, ann_key="meta_schedule.thread_extent_high_inclusive", ann_val=1024)
    b48 = sch.cache_write(block=b1, write_buffer_index=0, storage_scope="local")
    sch.reverse_compute_at(block=b48, loop=l47, preserve_unit_loops=True, index=-1)
    l49, l50, l51, l52, l53, l54 = sch.get_loops(block=b48)
    v55 = sch.sample_categorical(candidates=[1, 2, 3, 4], probs=[0.25, 0.25, 0.25, 0.25], decision=1)
    l56, l57 = sch.split(loop=l54, factors=[None, v55], preserve_unit_iters=True)
    sch.unroll(loop=l56)
    sch.vectorize(loop=l57)
    b58 = sch.cache_read(block=b1, read_buffer_index=0, storage_scope="shared", consumer_blocks=[b1])
    sch.compute_at(block=b58, loop=l44, preserve_unit_loops=True, index=-1)
    l59, l60, l61, l62, l63, l64, l65, l66, l67 = sch.get_loops(block=b58)
    l68 = sch.fuse(l64, l65, l66, l67, preserve_unit_iters=True)
    v69 = sch.sample_categorical(candidates=[1, 2, 3, 4], probs=[0.25, 0.25, 0.25, 0.25], decision=1)
    sch.annotate(block_or_loop=b58, ann_key="meta_schedule.cooperative_fetch", ann_val=v69)
    sch.annotate(block_or_loop=b58, ann_key="double_buffer_scope", ann_val=0)
    b70 = sch.cache_read(block=b58, read_buffer_index=0, storage_scope="local", consumer_blocks=[b58])
    sch.compute_at(block=b70, loop=l44, preserve_unit_loops=True, index=-1)
    l71, l72, l73, l74, l75, l76, l77, l78, l79 = sch.get_loops(block=b70)
    l80 = sch.fuse(l76, l77, l78, l79, preserve_unit_iters=True)
    v81 = sch.sample_categorical(candidates=[1, 2, 3, 4], probs=[0.25, 0.25, 0.25, 0.25], decision=1)
    sch.annotate(block_or_loop=b70, ann_key="meta_schedule.cooperative_fetch", ann_val=v81)
    b82 = sch.cache_read(block=b1, read_buffer_index=1, storage_scope="shared", consumer_blocks=[b1])
    sch.compute_at(block=b82, loop=l44, preserve_unit_loops=True, index=-1)
    l83, l84, l85, l86, l87, l88, l89, l90, l91 = sch.get_loops(block=b82)
    l92 = sch.fuse(l88, l89, l90, l91, preserve_unit_iters=True)
    v93 = sch.sample_categorical(candidates=[1, 2, 3, 4], probs=[0.25, 0.25, 0.25, 0.25], decision=3)
    sch.annotate(block_or_loop=b82, ann_key="meta_schedule.cooperative_fetch", ann_val=v93)
    sch.annotate(block_or_loop=b82, ann_key="double_buffer_scope", ann_val=0)
    b94 = sch.cache_read(block=b82, read_buffer_index=0, storage_scope="local", consumer_blocks=[b82])
    sch.compute_at(block=b94, loop=l44, preserve_unit_loops=True, index=-1)
    l95, l96, l97, l98, l99, l100, l101, l102, l103 = sch.get_loops(block=b94)
    l104 = sch.fuse(l100, l101, l102, l103, preserve_unit_iters=True)
    v105 = sch.sample_categorical(candidates=[1, 2, 3, 4], probs=[0.25, 0.25, 0.25, 0.25], decision=3)
    sch.annotate(block_or_loop=b94, ann_key="meta_schedule.cooperative_fetch", ann_val=v105)
    b106 = sch.cache_read(block=b1, read_buffer_index=0, storage_scope="local", consumer_blocks=[b1])
    sch.compute_at(block=b106, loop=l45, preserve_unit_loops=True, index=-1)
    l107, l108, l109, l110, l111, l112, l113, l114, l115, l116, l117, l118 = sch.get_loops(block=b106)
    l119 = sch.fuse(l115, l116, l117, l118, preserve_unit_iters=True)
    v120 = sch.sample_categorical(candidates=[1, 2, 3, 4], probs=[0.25, 0.25, 0.25, 0.25], decision=1)
    l121, l122 = sch.split(loop=l119, factors=[None, v120], preserve_unit_iters=True)
    sch.unroll(loop=l121)
    sch.vectorize(loop=l122)
    b123 = sch.cache_read(block=b1, read_buffer_index=1, storage_scope="local", consumer_blocks=[b1])
    sch.compute_at(block=b123, loop=l45, preserve_unit_loops=True, index=-1)
    l124, l125, l126, l127, l128, l129, l130, l131, l132, l133, l134, l135 = sch.get_loops(block=b123)
    l136 = sch.fuse(l132, l133, l134, l135, preserve_unit_iters=True)
    v137 = sch.sample_categorical(candidates=[1, 2, 3, 4], probs=[0.25, 0.25, 0.25, 0.25], decision=1)
    l138, l139 = sch.split(loop=l136, factors=[None, v137], preserve_unit_iters=True)
    sch.unroll(loop=l138)
    sch.vectorize(loop=l139)
    l140 = sch.fuse(l36, l40, l44, preserve_unit_iters=True)
    sch.annotate(block_or_loop=l140, ann_key="software_pipeline_order", ann_val=[0, 3, 1, 4, 2])
    sch.annotate(block_or_loop=l140, ann_key="software_pipeline_stage", ann_val=[0, 0, 0, 0, 1])
    b141 = sch.decompose_reduction(block=b1, loop=l140)
    l142 = sch.fuse(l37, l41, l45, preserve_unit_iters=True)
    sch.unroll(loop=l142)
    sch.compute_inline(block=b0)
    v143 = sch.sample_categorical(candidates=[0, 16, 64, 512, 1024], probs=[0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001], decision=0)
    sch.annotate(block_or_loop=b2, ann_key="meta_schedule.unroll_explicit", ann_val=v143)
    sch.enter_postproc()
    sch.unannotate(block_or_loop=b58, ann_key="meta_schedule.cooperative_fetch")
    l144, l145, l146, l147 = sch.get_loops(block=b58)
    l148, l149, l150 = sch.split(loop=l147, factors=[None, 448, 2], preserve_unit_iters=True)
    sch.vectorize(loop=l150)
    sch.bind(loop=l149, thread_axis="threadIdx.x")
    sch.unannotate(block_or_loop=b70, ann_key="meta_schedule.cooperative_fetch")
    l151, l152, l153, l154 = sch.get_loops(block=b70)
    l155, l156, l157 = sch.split(loop=l154, factors=[None, 448, 2], preserve_unit_iters=True)
    sch.vectorize(loop=l157)
    sch.bind(loop=l156, thread_axis="threadIdx.x")
    sch.unannotate(block_or_loop=b82, ann_key="meta_schedule.cooperative_fetch")
    l158, l159, l160, l161 = sch.get_loops(block=b82)
    l162, l163, l164 = sch.split(loop=l161, factors=[None, 448, 4], preserve_unit_iters=True)
    sch.vectorize(loop=l164)
    sch.bind(loop=l163, thread_axis="threadIdx.x")
    sch.unannotate(block_or_loop=b94, ann_key="meta_schedule.cooperative_fetch")
    l165, l166, l167, l168 = sch.get_loops(block=b94)
    l169, l170, l171 = sch.split(loop=l168, factors=[None, 448, 4], preserve_unit_iters=True)
    sch.vectorize(loop=l171)
    sch.bind(loop=l170, thread_axis="threadIdx.x")
    b172 = sch.get_block(name="root", func_name="main")
    sch.unannotate(block_or_loop=b172, ann_key="meta_schedule.unroll_explicit")
    b173, b174, b175, b176, b177, b178, b179, b180, b181 = sch.get_child_blocks(b172)
    l182, l183, l184, l185, l186, l187 = sch.get_loops(block=b173)
    l188, l189, l190, l191, l192, l193 = sch.get_loops(block=b174)
    l194, l195, l196, l197, l198, l199 = sch.get_loops(block=b175)
    l200, l201, l202, l203, l204, l205 = sch.get_loops(block=b176)
    l206, l207, l208, l209, l210, l211 = sch.get_loops(block=b177)
    l212, l213, l214, l215, l216, l217 = sch.get_loops(block=b178)
    l218, l219, l220, l221, l222, l223 = sch.get_loops(block=b179)
    l224, l225, l226, l227, l228, l229, l230, l231 = sch.get_loops(block=b180)
    l232, l233, l234, l235, l236, l237, l238 = sch.get_loops(block=b181)


ConvModule = create_conv_module()
sch = tir.Schedule(ConvModule)
apply_trace(sch)
eval_sch(sch)
# with open('bin/script.py', 'w') as f:
#     f.write(sch.mod.script())
print(sch.mod.script())