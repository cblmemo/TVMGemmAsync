# from tvm import tir
def apply_trace(sch: tir.Schedule) -> None:
  b0 = sch.get_block(name="Y", func_name="main")
  b1 = sch.cache_write(block=b0, write_buffer_index=0, storage_scope="local")
  b2 = sch.cache_read(block=b0, read_buffer_index=0, storage_scope="shared.dyn")
  b3 = sch.cache_read(block=b0, read_buffer_index=0, storage_scope="local")
  b4 = sch.cache_read(block=b0, read_buffer_index=1, storage_scope="shared.dyn")
  b5 = sch.cache_read(block=b0, read_buffer_index=1, storage_scope="local")
  l6, l7, l8 = sch.get_loops(block=b0)
  v9, v10, v11 = sch.sample_perfect_tile(loop=l6, n=3, max_innermost_factor=16, decision=[16, 16, 2])
  v12, v13, v14 = sch.sample_perfect_tile(loop=l7, n=3, max_innermost_factor=16, decision=[8, 4, 8])
  v15, v16 = sch.sample_perfect_tile(loop=l8, n=2, max_innermost_factor=8, decision=[80, 8])
  l17, l18, l19 = sch.split(loop=l6, factors=[v9, v10, v11], preserve_unit_iters=True)
  l20, l21, l22 = sch.split(loop=l7, factors=[v12, v13, v14], preserve_unit_iters=True)
  l23, l24 = sch.split(loop=l8, factors=[v15, v16], preserve_unit_iters=True)
  sch.reorder(l17, l20, l18, l21, l22, l19)
  l25 = sch.fuse(l17, l20, preserve_unit_iters=True)
  sch.bind(loop=l25, thread_axis="blockIdx.x")
  v26, v27, v28 = sch.sample_perfect_tile(loop=l18, n=3, max_innermost_factor=16, decision=[8, 1, 2])
  v29, v30 = sch.sample_perfect_tile(loop=l21, n=2, max_innermost_factor=16, decision=[2, 2])
  l31, l32, l33 = sch.split(loop=l18, factors=[v26, v27, v28], preserve_unit_iters=True)
  l34, l35 = sch.split(loop=l21, factors=[v29, v30], preserve_unit_iters=True)
  sch.reorder(l25, l34, l31, l32, l35, l33, l23, l24, l22, l19)
  l36 = sch.fuse(l34, l31, preserve_unit_iters=True)
  l37 = sch.fuse(l32, l35, l33, preserve_unit_iters=True)
  l38 = sch.fuse(l36, l37, preserve_unit_iters=True)
  sch.bind(loop=l38, thread_axis="threadIdx.x")
  sch.compute_at(block=b3, loop=l24, preserve_unit_loops=True, index=-1)
  sch.compute_at(block=b5, loop=l24, preserve_unit_loops=True, index=-1)
  sch.compute_at(block=b2, loop=l23, preserve_unit_loops=True, index=-1)
  sch.compute_at(block=b4, loop=l23, preserve_unit_loops=True, index=-1)
  sch.transform_layout(block=b3, buffer=("read", 0), index_map=lambda i, j: (i, ((((((floordiv(j, 128)*128) + (floordiv(floormod(j, 128), 32)*32)) + (floordiv(floormod(j, 32), 16)*8)) + (floordiv(floormod(j, 16), 8)*4)) + (floordiv(floormod(j, 8), 4)*16)) + floormod(floormod(j, 8), 4)),), pad_value=None)
  sch.transform_layout(block=b5, buffer=("read", 0), index_map=lambda i, j: (i, (((((floordiv(j, 128)*128) + (floordiv(floormod(j, 128), 64)*64)) + (floordiv(floormod(j, 64), 8)*4)) + (floordiv(floormod(j, 8), 4)*32)) + floormod(floormod(j, 8), 4)),), pad_value=None)
  l39, l40, l41, l42, l43, l44 = sch.get_loops(block=b3)
  l45, l46 = sch.split(loop=l44, factors=[None, 4], preserve_unit_iters=True)
  sch.vectorize(loop=l46)
  l47, l48, l49, l50, l51, l52 = sch.get_loops(block=b5)
  l53, l54 = sch.split(loop=l52, factors=[None, 4], preserve_unit_iters=True)
  sch.vectorize(loop=l54)
  l55, l56, l57, l58, l59 = sch.get_loops(block=b2)
  l60 = sch.fuse(l58, l59, preserve_unit_iters=True)
  l61, l62, l63 = sch.split(loop=l60, factors=[v10, v13, None], preserve_unit_iters=True)
  l64 = sch.fuse(l61, l62, preserve_unit_iters=True)
  sch.bind(loop=l64, thread_axis="threadIdx.x")
  sch.vectorize(loop=l63)
  l65, l66, l67, l68, l69 = sch.get_loops(block=b4)
  l70 = sch.fuse(l68, l69, preserve_unit_iters=True)
  l71, l72, l73 = sch.split(loop=l70, factors=[v10, v13, None], preserve_unit_iters=True)
  l74 = sch.fuse(l71, l72, preserve_unit_iters=True)
  sch.bind(loop=l74, thread_axis="threadIdx.x")
  sch.reverse_compute_at(block=b1, loop=l38, preserve_unit_loops=True, index=-1)
  sch.unroll(loop=l24)
  sch.unroll(loop=l22)
  l75, l76 = sch.split(loop=l19, factors=[None, 4], preserve_unit_iters=True)
  sch.unroll(loop=l75)
  sch.vectorize(loop=l76)
  b77 = sch.decompose_reduction(block=b0, loop=l23)
  l78, l79, l80, l81, l82 = sch.get_loops(block=b77)
  sch.unroll(loop=l81)
  sch.unroll(loop=l82)
  l83, l84, l85, l86 = sch.get_loops(block=b1)
  sch.unroll(loop=l85)
  l87, l88 = sch.split(loop=l86, factors=[None, 4], preserve_unit_iters=True)
  sch.vectorize(loop=l88)
  sch.annotate(block_or_loop=l24, ann_key="software_pipeline_stage", ann_val=[0, 0, 1])
  sch.annotate(block_or_loop=l24, ann_key="software_pipeline_order", ann_val=[0, 1, 2])
  sch.annotate(block_or_loop=l23, ann_key="software_pipeline_stage", ann_val=[0, 0, 2, 3, 3])
  sch.annotate(block_or_loop=l23, ann_key="software_pipeline_order", ann_val=[0, 1, 3, 2, 4])
  sch.annotate(block_or_loop=l23, ann_key="software_pipeline_async_stages", ann_val=[0, 1])
  sch.enter_postproc()
