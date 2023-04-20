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
  sch.annotate(block_or_loop=b0, ann_key="meta_schedule.tiling_structure", ann_val="SSSRRSRS")
  b1 = sch.reindex(block=b0, buffer=("write", 0))
  b2 = sch.reindex(block=b0, buffer=("read", 0))
  b3 = sch.reindex(block=b0, buffer=("read", 1))
  sch.transform_layout(block=b0, buffer=("read", 0), index_map=lambda v_i, v_k: (v_i, v_k,), pad_value=None, assume_injective_transform=True)
  sch.transform_layout(block=b0, buffer=("read", 1), index_map=lambda v_j, v_k: (v_k, v_j,), pad_value=None, assume_injective_transform=True)
  sch.transform_layout(block=b0, buffer=("write", 0), index_map=lambda v_i, v_j: (v_i, v_j,), pad_value=None, assume_injective_transform=True)
  sch.transform_block_layout(block=b1, index_map=lambda v_i, v_j: (v_i, v_j,))
  sch.transform_block_layout(block=b2, index_map=lambda v_i, v_k: (v_i, v_k,))
  sch.transform_block_layout(block=b3, index_map=lambda v_j, v_k: (v_k, v_j,))
  sch.transform_block_layout(block=b0, index_map=lambda v_i, v_j, v_k: (v_i, v_j, v_k,))
  l4, l5, l6 = sch.get_loops(block=b0)
  l7, l8 = sch.split(loop=l6, factors=[None, 8], preserve_unit_iters=True)
  l9, l10 = sch.split(loop=l5, factors=[None, 8], preserve_unit_iters=True)
  l11, l12 = sch.split(loop=l4, factors=[None, 16], preserve_unit_iters=True)
  l13, l14, l15, l16, l17, l18 = sch.get_loops(block=b0)
  sch.reorder(l15, l17, l12, l10, l8)
  b19 = sch.blockize(loop=l12, preserve_unit_iters=True)
  sch.annotate(block_or_loop=b19, ann_key="meta_schedule.auto_tensorize", ann_val="m16n8k8_sync")
  sch.annotate(block_or_loop=b19, ann_key="meta_schedule.auto_tensorize_init", ann_val="m16n8k8_init")
  sch.annotate(block_or_loop=b19, ann_key="warp_execution", ann_val=1)
  l20, l21, l22 = sch.get_loops(block=b19)
  v23, v24, v25, v26, v27 = sch.sample_partitioned_tile(loop=l20, n=5, partition_pos=3, innerpart_factor=2, decision=[2, 16, 1, 1, 8])
  l28, l29, l30, l31, l32 = sch.split(loop=l20, factors=[v23, v24, v25, v26, v27], preserve_unit_iters=True)
  v33, v34, v35, v36, v37 = sch.sample_partitioned_tile(loop=l21, n=5, partition_pos=3, innerpart_factor=4, decision=[2, 16, 2, 8, 1])
  l38, l39, l40, l41, l42 = sch.split(loop=l21, factors=[v33, v34, v35, v36, v37], preserve_unit_iters=True)
  v43, v44, v45 = sch.sample_perfect_tile(loop=l22, n=3, max_innermost_factor=4, decision=[256, 2, 1])
  l46, l47, l48 = sch.split(loop=l22, factors=[v43, v44, v45], preserve_unit_iters=True)
  sch.reorder(l28, l38, l29, l39, l30, l40, l46, l47, l31, l41, l48, l32, l42)
  l49 = sch.fuse(l28, l38, preserve_unit_iters=True)
  sch.bind(loop=l49, thread_axis="blockIdx.x")
  l50 = sch.fuse(l29, l39, preserve_unit_iters=True)
  sch.bind(loop=l50, thread_axis="blockIdx.y")
  l51 = sch.fuse(l30, l40, preserve_unit_iters=True)
  sch.bind(loop=l51, thread_axis="threadIdx.y")
  sch.annotate(block_or_loop=b19, ann_key="meta_schedule.thread_extent_low_inclusive", ann_val=32)
  sch.annotate(block_or_loop=b19, ann_key="meta_schedule.thread_extent_high_inclusive", ann_val=1024)
  b52 = sch.write_at(loop=l51, block=b19, write_buffer_index=0, storage_scope="m16n8k8.matrixC")
  sch.reverse_compute_inline(block=b1)
  b53 = sch.read_at(loop=l46, block=b19, read_buffer_index=0, storage_scope="shared.dyn")
  b54 = sch.read_at(loop=l46, block=b19, read_buffer_index=1, storage_scope="shared.dyn")
  b55 = sch.cache_read(block=b19, read_buffer_index=0, storage_scope="m16n8k8.matrixA")
  sch.compute_at(block=b55, loop=l47, preserve_unit_loops=True, index=-1)
  l56, l57, l58, l59, l60, l61, l62 = sch.get_loops(block=b55)
  l63, l64 = sch.split(loop=l62, factors=[None, 8], preserve_unit_iters=True)
  l65, l66 = sch.split(loop=l61, factors=[None, 32], preserve_unit_iters=True)
  l67, l68, l69, l70, l71, l72, l73, l74, l75 = sch.get_loops(block=b55)
  sch.reorder(l74, l66, l64)
  b76 = sch.blockize(loop=l66, preserve_unit_iters=True)
  sch.annotate(block_or_loop=b76, ann_key="meta_schedule.auto_tensorize", ann_val="m16n8k8_load_A_row_major")
  b77 = sch.cache_read(block=b19, read_buffer_index=1, storage_scope="m16n8k8.matrixB")
  sch.compute_at(block=b77, loop=l47, preserve_unit_loops=True, index=-1)
  l78, l79, l80, l81, l82, l83, l84 = sch.get_loops(block=b77)
  l85, l86 = sch.split(loop=l84, factors=[None, 32], preserve_unit_iters=True)
  l87, l88 = sch.split(loop=l83, factors=[None, 8], preserve_unit_iters=True)
  l89, l90, l91, l92, l93, l94, l95, l96, l97 = sch.get_loops(block=b77)
  sch.reorder(l96, l88, l86)
  b98 = sch.blockize(loop=l88, preserve_unit_iters=True)
  sch.annotate(block_or_loop=b98, ann_key="meta_schedule.auto_tensorize", ann_val="m16n8k8_load_B_row_major")
  sch.compute_inline(block=b2)
  sch.compute_inline(block=b3)
  sch.storage_align(block=b53, buffer_index=0, axis=-2, factor=32, offset=8)
  sch.storage_align(block=b54, buffer_index=0, axis=-2, factor=32, offset=8)
  sch.annotate(block_or_loop=b53, ann_key="vector_bytes", ann_val=16)
  sch.annotate(block_or_loop=b54, ann_key="vector_bytes", ann_val=16)
  sch.annotate(block_or_loop=l47, ann_key="software_pipeline_stage", ann_val=[0, 0, 1])
  sch.annotate(block_or_loop=l47, ann_key="software_pipeline_order", ann_val=[0, 1, 2])
  sch.annotate(block_or_loop=l46, ann_key="software_pipeline_async_stages", ann_val=[0])
  sch.annotate(block_or_loop=l46, ann_key="software_pipeline_stage", ann_val=[0, 0, 1, 2, 2])
  sch.annotate(block_or_loop=l46, ann_key="software_pipeline_order", ann_val=[0, 1, 3, 2, 4])
  sch.enter_postproc()
  b99 = sch.get_block(name="Y_o", func_name="main")
  l100, l101, l102, l103, l104, l105, l106, l107, l108, l109 = sch.get_loops(block=b99)
  b110 = sch.decompose_reduction(block=b99, loop=l103)
  sch.unannotate(block_or_loop=b110, ann_key="meta_schedule.auto_tensorize")
  sch.annotate(block_or_loop=b110, ann_key="meta_schedule.auto_tensorize", ann_val="m16n8k8_init")
  sch.unannotate(block_or_loop=b99, ann_key="meta_schedule.auto_tensorize_init")
  sch.unannotate(block_or_loop=b110, ann_key="meta_schedule.auto_tensorize_init")
  b111 = sch.get_block(name="Y_o_init", func_name="main")
  sch.unannotate(block_or_loop=b111, ann_key="meta_schedule.auto_tensorize")
  sch.tensorize(block_or_loop=b111, tensor_intrin="m16n8k8_init", preserve_unit_iters=True)
  b112 = sch.get_block(name="A_reindex_shared.dyn_m16n8k8.matrixA_o", func_name="main")
  sch.unannotate(block_or_loop=b112, ann_key="meta_schedule.auto_tensorize")
  sch.tensorize(block_or_loop=b112, tensor_intrin="m16n8k8_load_A_row_major", preserve_unit_iters=True)
  b113 = sch.get_block(name="B_reindex_shared.dyn_m16n8k8.matrixB_o", func_name="main")
  sch.unannotate(block_or_loop=b113, ann_key="meta_schedule.auto_tensorize")
  sch.tensorize(block_or_loop=b113, tensor_intrin="m16n8k8_load_B_row_major", preserve_unit_iters=True)
  b114 = sch.get_block(name="Y_o_update", func_name="main")
  sch.unannotate(block_or_loop=b114, ann_key="meta_schedule.auto_tensorize")
  sch.tensorize(block_or_loop=b114, tensor_intrin="m16n8k8_sync", preserve_unit_iters=True)
