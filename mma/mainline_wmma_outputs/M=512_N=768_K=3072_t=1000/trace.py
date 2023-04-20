from tvm import tir
from tvm.tir import floordiv, floormod
from tvm import tir
from tvm.tir import floordiv, floormod
from tvm import tir
from tvm.tir import floordiv, floormod
from tvm import tir
from tvm.tir import floordiv, floormod
from tvm import tir
from tvm.tir import floordiv, floormod
from tvm import tir
from tvm.tir import floordiv, floormod
from tvm import tir
from tvm.tir import floordiv, floormod
from tvm import tir
from tvm.tir import floordiv, floormod
# from tvm import tir
def apply_trace(sch: tir.Schedule) -> None:
  b0 = sch.get_block(name="Y", func_name="main")
  b1 = sch.get_block(name="root", func_name="main")
  sch.annotate(block_or_loop=b0, ann_key="meta_schedule.tiling_structure", ann_val="SSSRRSRS")
  b2 = sch.reindex(block=b0, buffer=("write", 0))
  b3 = sch.reindex(block=b0, buffer=("read", 0))
  b4 = sch.reindex(block=b0, buffer=("read", 1))
  sch.transform_layout(block=b0, buffer=("read", 0), index_map=lambda v_i, v_k: (v_i, v_k,), pad_value=None, assume_injective_transform=True)
  sch.transform_layout(block=b0, buffer=("read", 1), index_map=lambda v_j, v_k: (v_k, v_j,), pad_value=None, assume_injective_transform=True)
  sch.transform_layout(block=b0, buffer=("write", 0), index_map=lambda v_i, v_j: (v_i, v_j,), pad_value=None, assume_injective_transform=True)
  sch.transform_block_layout(block=b2, index_map=lambda v_i, v_j: (v_i, v_j,))
  sch.transform_block_layout(block=b3, index_map=lambda v_i, v_k: (v_i, v_k,))
  sch.transform_block_layout(block=b4, index_map=lambda v_j, v_k: (v_k, v_j,))
  sch.transform_block_layout(block=b0, index_map=lambda v_i, v_j, v_k: (v_i, v_j, v_k,))
  l5, l6, l7 = sch.get_loops(block=b0)
  l8, l9 = sch.split(loop=l7, factors=[None, 16], preserve_unit_iters=True)
  l10, l11 = sch.split(loop=l6, factors=[None, 16], preserve_unit_iters=True)
  l12, l13 = sch.split(loop=l5, factors=[None, 16], preserve_unit_iters=True)
  l14, l15, l16, l17, l18, l19 = sch.get_loops(block=b0)
  sch.reorder(l16, l18, l13, l11, l9)
  b20 = sch.blockize(loop=l13, preserve_unit_iters=True)
  sch.annotate(block_or_loop=b20, ann_key="meta_schedule.auto_tensorize", ann_val="wmma_sync_16x16x16_f16f16f16")
  sch.annotate(block_or_loop=b20, ann_key="meta_schedule.auto_tensorize_init", ann_val="wmma_fill_16x16x16_f16")
  sch.annotate(block_or_loop=b20, ann_key="warp_execution", ann_val=1)
  l21, l22, l23 = sch.get_loops(block=b20)
  v24, v25, v26, v27, v28 = sch.sample_perfect_tile(loop=l21, n=5, max_innermost_factor=4, decision=[2, 4, 2, 1, 2])
  l29, l30, l31, l32, l33 = sch.split(loop=l21, factors=[v24, v25, v26, v27, v28], preserve_unit_iters=True)
  v34, v35, v36, v37, v38 = sch.sample_perfect_tile(loop=l22, n=5, max_innermost_factor=4, decision=[6, 2, 4, 1, 1])
  l39, l40, l41, l42, l43 = sch.split(loop=l22, factors=[v34, v35, v36, v37, v38], preserve_unit_iters=True)
  v44, v45, v46 = sch.sample_perfect_tile(loop=l23, n=3, max_innermost_factor=4, decision=[48, 1, 4])
  l47, l48, l49 = sch.split(loop=l23, factors=[v44, v45, v46], preserve_unit_iters=True)
  sch.reorder(l29, l39, l30, l40, l31, l41, l47, l48, l32, l42, l49, l33, l43)
  l50 = sch.fuse(l29, l39, preserve_unit_iters=True)
  sch.bind(loop=l50, thread_axis="blockIdx.y")
  l51 = sch.fuse(l30, l40, preserve_unit_iters=True)
  sch.bind(loop=l51, thread_axis="blockIdx.x")
  l52 = sch.fuse(l31, l41, preserve_unit_iters=True)
  sch.bind(loop=l52, thread_axis="threadIdx.y")
  sch.annotate(block_or_loop=b20, ann_key="meta_schedule.thread_extent_low_inclusive", ann_val=32)
  sch.annotate(block_or_loop=b20, ann_key="meta_schedule.thread_extent_high_inclusive", ann_val=1024)
  sch.transform_layout(block=b20, buffer=("write", 0), index_map=lambda i0, i1: (i0 // 16 // (v27 * v28), i1 // 16 // (v37 * v38), i0 // 16 % (v27 * v28), i1 // 16 % (v37 * v38), i0 % 16, i1 % 16,), pad_value=None, assume_injective_transform=True)
  b53 = sch.cache_write(block=b20, write_buffer_index=0, storage_scope="shared.dyn")
  sch.reverse_compute_at(block=b53, loop=l51, preserve_unit_loops=True, index=-1)
  b54 = sch.cache_write(block=b20, write_buffer_index=0, storage_scope="wmma.accumulator")
  l55, l56, l57, l58, l59, l60, l61, l62 = sch.get_loops(block=b53)
  sch.reorder(l59, l57, l58, l60)
  sch.compute_at(block=b54, loop=l59, preserve_unit_loops=True, index=-1)
  l63, l64, l65, l66, l67, l68, l69, l70, l71 = sch.get_loops(block=b54)
  l72 = sch.fuse(l66, l67, preserve_unit_iters=True)
  sch.bind(loop=l72, thread_axis="threadIdx.y")
  sch.reverse_compute_inline(block=b2)
  l73, l74, l75, l76, l77, l78, l79, l80 = sch.get_loops(block=b54)
  b81 = sch.blockize(loop=l79, preserve_unit_iters=True)
  sch.annotate(block_or_loop=b81, ann_key="meta_schedule.auto_tensorize", ann_val="wmma_store_16x16x16_f16_shared_dyn")
  l82, l83, l84, l85, l86, l87, l88, l89 = sch.get_loops(block=b53)
  l90 = sch.fuse(l85, l86, l87, l88, l89, preserve_unit_iters=True)
  v91 = sch.sample_categorical(candidates=[1, 2, 4, 8], probs=[0.25, 0.25, 0.25, 0.25], decision=2)
  sch.annotate(block_or_loop=b53, ann_key="meta_schedule.cooperative_fetch", ann_val=v91)
  b92 = sch.cache_read(block=b20, read_buffer_index=0, storage_scope="shared.dyn", consumer_blocks=[b20])
  sch.compute_at(block=b92, loop=l47, preserve_unit_loops=True, index=-1)
  l93, l94, l95, l96, l97, l98 = sch.get_loops(block=b92)
  l99 = sch.fuse(l97, l98, preserve_unit_iters=True)
  v100 = sch.sample_categorical(candidates=[1, 2, 4, 8], probs=[0.25, 0.25, 0.25, 0.25], decision=2)
  sch.annotate(block_or_loop=b92, ann_key="meta_schedule.cooperative_fetch", ann_val=v100)
  b101 = sch.cache_read(block=b20, read_buffer_index=1, storage_scope="shared.dyn", consumer_blocks=[b20])
  sch.compute_at(block=b101, loop=l47, preserve_unit_loops=True, index=-1)
  l102, l103, l104, l105, l106, l107 = sch.get_loops(block=b101)
  l108 = sch.fuse(l106, l107, preserve_unit_iters=True)
  v109 = sch.sample_categorical(candidates=[1, 2, 4, 8], probs=[0.25, 0.25, 0.25, 0.25], decision=2)
  sch.annotate(block_or_loop=b101, ann_key="meta_schedule.cooperative_fetch", ann_val=v109)
  b110 = sch.cache_read(block=b20, read_buffer_index=0, storage_scope="wmma.matrix_a")
  sch.compute_at(block=b110, loop=l48, preserve_unit_loops=True, index=-1)
  l111, l112, l113, l114, l115, l116, l117 = sch.get_loops(block=b110)
  l118, l119 = sch.split(loop=l117, factors=[None, 16], preserve_unit_iters=True)
  l120, l121 = sch.split(loop=l116, factors=[None, 16], preserve_unit_iters=True)
  l122, l123, l124, l125, l126, l127, l128, l129, l130 = sch.get_loops(block=b110)
  sch.reorder(l129, l121, l119)
  b131 = sch.blockize(loop=l121, preserve_unit_iters=True)
  sch.annotate(block_or_loop=b131, ann_key="meta_schedule.auto_tensorize", ann_val="wmma_load_16x16x16_f16_a_shared_dyn")
  b132 = sch.cache_read(block=b20, read_buffer_index=1, storage_scope="wmma.matrix_b")
  sch.compute_at(block=b132, loop=l48, preserve_unit_loops=True, index=-1)
  l133, l134, l135, l136, l137, l138, l139 = sch.get_loops(block=b132)
  l140, l141 = sch.split(loop=l139, factors=[None, 16], preserve_unit_iters=True)
  l142, l143 = sch.split(loop=l138, factors=[None, 16], preserve_unit_iters=True)
  l144, l145, l146, l147, l148, l149, l150, l151, l152 = sch.get_loops(block=b132)
  sch.reorder(l151, l143, l141)
  b153 = sch.blockize(loop=l143, preserve_unit_iters=True)
  sch.annotate(block_or_loop=b153, ann_key="meta_schedule.auto_tensorize", ann_val="wmma_load_16x16x16_f16_b_shared_dyn")
  sch.compute_inline(block=b3)
  sch.compute_inline(block=b4)
  sch.storage_align(block=b92, buffer_index=0, axis=-2, factor=32, offset=8)
  sch.storage_align(block=b101, buffer_index=0, axis=-2, factor=32, offset=8)
  v154 = sch.sample_categorical(candidates=[0, 16, 64, 512, 1024], probs=[0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001], decision=0)
  sch.annotate(block_or_loop=b1, ann_key="meta_schedule.unroll_explicit", ann_val=v154)
  sch.enter_postproc()
  sch.unannotate(block_or_loop=b53, ann_key="meta_schedule.cooperative_fetch")
  l155, l156, l157, l158 = sch.get_loops(block=b53)
  l159, l160, l161, l162 = sch.split(loop=l158, factors=[None, 8, 32, 4], preserve_unit_iters=True)
  sch.vectorize(loop=l162)
  sch.bind(loop=l161, thread_axis="threadIdx.x")
  sch.bind(loop=l160, thread_axis="threadIdx.y")
  sch.unannotate(block_or_loop=b92, ann_key="meta_schedule.cooperative_fetch")
  l163, l164, l165, l166, l167 = sch.get_loops(block=b92)
  l168, l169, l170, l171 = sch.split(loop=l167, factors=[None, 8, 32, 4], preserve_unit_iters=True)
  sch.vectorize(loop=l171)
  sch.bind(loop=l170, thread_axis="threadIdx.x")
  sch.bind(loop=l169, thread_axis="threadIdx.y")
  sch.unannotate(block_or_loop=b101, ann_key="meta_schedule.cooperative_fetch")
  l172, l173, l174, l175, l176 = sch.get_loops(block=b101)
  l177, l178, l179, l180 = sch.split(loop=l176, factors=[None, 8, 32, 4], preserve_unit_iters=True)
  sch.vectorize(loop=l180)
  sch.bind(loop=l179, thread_axis="threadIdx.x")
  sch.bind(loop=l178, thread_axis="threadIdx.y")
  b181 = sch.get_block(name="root", func_name="main")
  sch.unannotate(block_or_loop=b181, ann_key="meta_schedule.unroll_explicit")
  b182, b183, b184, b185, b186, b187, b188 = sch.get_child_blocks(b181)
  l189, l190, l191, l192, l193, l194, l195, l196 = sch.get_loops(block=b182)
  l197, l198, l199, l200, l201, l202, l203, l204 = sch.get_loops(block=b183)
  l205, l206, l207, l208, l209, l210, l211 = sch.get_loops(block=b184)
  l212, l213, l214, l215, l216, l217, l218 = sch.get_loops(block=b185)
  l219, l220, l221, l222, l223, l224, l225, l226, l227, l228 = sch.get_loops(block=b186)
  l229, l230, l231, l232, l233, l234 = sch.get_loops(block=b187)
  l235, l236, l237, l238, l239, l240, l241 = sch.get_loops(block=b188)
  b242 = sch.get_block(name="Y_o", func_name="main")
  l243, l244, l245, l246, l247, l248, l249, l250, l251, l252 = sch.get_loops(block=b242)
  b253 = sch.decompose_reduction(block=b242, loop=l246)
  sch.unannotate(block_or_loop=b253, ann_key="meta_schedule.auto_tensorize")
  sch.annotate(block_or_loop=b253, ann_key="meta_schedule.auto_tensorize", ann_val="wmma_fill_16x16x16_f16")
  sch.unannotate(block_or_loop=b242, ann_key="meta_schedule.auto_tensorize_init")
  sch.unannotate(block_or_loop=b253, ann_key="meta_schedule.auto_tensorize_init")
  b254 = sch.get_block(name="Y_o_init", func_name="main")
  sch.unannotate(block_or_loop=b254, ann_key="meta_schedule.auto_tensorize")
  sch.tensorize(block_or_loop=b254, tensor_intrin="wmma_fill_16x16x16_f16", preserve_unit_iters=True)
  b255 = sch.get_block(name="A_reindex_shared.dyn_wmma.matrix_a_o", func_name="main")
  sch.unannotate(block_or_loop=b255, ann_key="meta_schedule.auto_tensorize")
  sch.tensorize(block_or_loop=b255, tensor_intrin="wmma_load_16x16x16_f16_a_shared_dyn", preserve_unit_iters=True)
  b256 = sch.get_block(name="B_reindex_shared.dyn_wmma.matrix_b_o", func_name="main")
  sch.unannotate(block_or_loop=b256, ann_key="meta_schedule.auto_tensorize")
  sch.tensorize(block_or_loop=b256, tensor_intrin="wmma_load_16x16x16_f16_b_shared_dyn", preserve_unit_iters=True)
  b257 = sch.get_block(name="Y_o_update", func_name="main")
  sch.unannotate(block_or_loop=b257, ann_key="meta_schedule.auto_tensorize")
  sch.tensorize(block_or_loop=b257, tensor_intrin="wmma_sync_16x16x16_f16f16f16", preserve_unit_iters=True)
  b258 = sch.get_block(name="Y_reindex_shared.dyn_wmma.accumulator_o", func_name="main")
  sch.unannotate(block_or_loop=b258, ann_key="meta_schedule.auto_tensorize")
  sch.tensorize(block_or_loop=b258, tensor_intrin="wmma_store_16x16x16_f16_shared_dyn", preserve_unit_iters=True)
