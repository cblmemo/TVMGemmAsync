

#include <tvm/meta_schedule/schedule_rule.h>

#include <tvm/tir/index_map.h>
#include <tvm/runtime/packed_func.h>
#include <tvm/tir/op.h>

#include "../utils.h"
#include "./multi_level_tiling.h"

namespace tvm {
namespace tir {
/*!
 * \brief Get the buffer dimensions for all the read buffers of a block, but marks the reduction
 * buffers' dimensions as -1
 * \param block_sref The block to be processed
 * \return The buffer dimensions for all the read buffers of a block, except for reduction buffers
 * \note The method is not designed for generic analysis and relies on assumptions in the scenario
 * of multi-level tiling, so it's intentionally kept inside this file not in the analysis header
 */
std::vector<int> GetReadBufferNDimsPipelined(const StmtSRef& block_sref) {
  const BlockNode* block = TVM_SREF_TO_BLOCK(block_sref);
  const BufferNode* write_buffer = block->writes[0]->buffer.get();
  int n = block->reads.size();
  std::vector<int> results(n, -1);
  for (int i = 0; i < n; ++i) {
    const BufferNode* read_buffer = block->reads[i]->buffer.get();
    if (read_buffer != write_buffer) {
      results[i] = read_buffer->shape.size();
    }
  }
  return results;
}

}  // namespace tir
}  // namespace tvm

namespace tvm {
namespace meta_schedule {

using tir::BlockRV;
using tir::IterVarType;
using tir::LoopRV;
using tir::Schedule;
using tir::BufferIndexType;
using tir::IndexMap;
using tir::Var;
using runtime::TypedPackedFunc;


class PipelinedStateNode : public StateNode {
 public:
  /*! \brief the mapping from reduction loop level to pipeline block number */
  std::map<int, int> pipeline_stages;
  /*! \brief The Pipelined reindex block A for Pipelined computation */
  tir::BlockRV pipeline_reindex_A;
  /*! \brief The Pipelined reindex block B for Pipelined computation */
  tir::BlockRV pipeline_reindex_B;
  /*! \brief The Pipelined reindex store block for Pipelined computation */
  tir::BlockRV pipeline_reindex_store;
  /*! \brief The reindex maping info. */
  tir::AutoTensorizeMappingInfo mapping_info {nullptr};

  State Copy() const final;

  static constexpr const char* _type_key = "meta_schedule.PipelinedState";
  TVM_DECLARE_FINAL_OBJECT_INFO(PipelinedStateNode, StateNode);
};

class PipelinedState : public State {
 public:
  explicit PipelinedState(tir::AutoTensorizeMappingInfo mapping_info,
                          Schedule sch, BlockRV block_rv);
  TVM_DEFINE_MUTABLE_OBJECT_REF_METHODS(PipelinedState, State, PipelinedStateNode);
};

TVM_REGISTER_OBJECT_TYPE(PipelinedStateNode);

PipelinedState::PipelinedState(tir::AutoTensorizeMappingInfo mapping_info,
                               Schedule sch, BlockRV block_rv) {
  ObjectPtr<PipelinedStateNode> node = make_object<PipelinedStateNode>();
  node->sch = std::move(sch);
  node->block_rv = std::move(block_rv);
  node->pipeline_stages.clear();
  node->mapping_info = mapping_info;
  data_ = std::move(node);
}

State PipelinedStateNode::Copy() const {
  ObjectPtr<PipelinedStateNode> node = make_object<PipelinedStateNode>(*this);
  node->sch = sch->Copy();
  return State(node);
}

/*!
 * \brief Extension of MultiLevelTiling with software pipeline and 
 * multiple-level reuse read.
 */
class MultiLevelTilingPipelinedNode : public MultiLevelTilingNode {
 public:
  std::vector<ReuseConfig> reuse_read_list_;

  // Subrule: In order to use GEMM optimization technique,
  // trnasform GEMM-like computation into GEMM
  inline std::vector<State> TransformeToGEMM(PipelinedState state) const;
  // Subrule: Add multi-level load cache
  inline std::vector<State> AddReadReusePipelined(PipelinedState state) const;
  // Subrule: Add write cache with small unroll & vectorize
  inline std::vector<State> AddWriteReusePipelined(PipelinedState state) const;
  // SubRule: PostProcessing
  // (1) add software pipeline
  // (2) decompose reduction
  // (3) unroll & vectorize some loop
  std::vector<State> PipelinedPostProcessing(PipelinedState state) const;

  // Override ApplySubRules to apply pipelined-specific sub-rules
  std::vector<State> ApplySubRules(std::vector<State> states) final;

  // Override Apply to apply pipelined-specific analysis before applying sub-rules
  Array<Schedule> Apply(const Schedule& sch, const BlockRV& block_rv) final;

  // Inherited from ScheduleRuleNode
  ScheduleRule Clone() const final {
    ObjectPtr<MultiLevelTilingPipelinedNode> n =
        make_object<MultiLevelTilingPipelinedNode>(*this);
    return ScheduleRule(n);
  }

  // get all valid vector lens decided by write buffer's dtype
  std::vector<int> GetValidVectorLens(tir::Schedule* sch,
                                      const tir::BlockRV& block) const;

  // Add unroll & vectorize to small loops
  void AddSmallUnrollVectorize(tir::Schedule* sch,
                               const tir::BlockRV& block,
                               const tir::LoopRV& loop) const;
  
 public:
  static constexpr const char* _type_key = "meta_schedule.MultiLevelTilingPipelined";
  TVM_DECLARE_FINAL_OBJECT_INFO(MultiLevelTilingPipelinedNode, MultiLevelTilingNode);
};

// Entry of the mega rule; Inherited from ScheduleRuleNode
Array<Schedule> MultiLevelTilingPipelinedNode::Apply(const Schedule& sch,
                                                     const BlockRV& block_rv) {
  if (!NeedsMultiLevelTiling(sch->state(), sch->GetSRef(block_rv))) {
    return { sch };
  }

  std::set<tir::AutoTensorizeMappingInfo> mapping_infos;
  for (const std::string & intrin : std::vector<std::string>{
    "pipelined_mma_float32",
    // "pipelined_mma_float32_trans",
  }) {
    Optional<tir::AutoTensorizeMappingInfo> mapping_info = tir::GetAutoTensorizeMappingInfo(
      sch->state(), sch->GetSRef(block_rv),
      tir::TensorIntrin::Get(intrin).value()->desc
    );
    if (mapping_info.defined()) mapping_infos.insert(mapping_info.value());
  }

  Array<Schedule> results;
  // add an unannotated schedule for MultiLevelTiling to process
  // make sure pipelined traces could coexist with original MultiLevelTiling trace
  results.push_back(sch->Copy());

  std::vector<State> initial_states;
  for (const tir::AutoTensorizeMappingInfo &mapping_info : mapping_infos) {
    Schedule new_sch = sch->Copy();
    // annotate tiling structure to avoid MultiLevelTiling to process
    new_sch->Annotate(block_rv, tir::attr::meta_schedule_tiling_structure, structure);
    initial_states.push_back(PipelinedState(mapping_info, new_sch, block_rv));
  }
  
  for (auto&& state : ApplySubRules(initial_states)) {
    results.push_back(std::move(state->sch));
  }
  return results;
}

std::vector<State> MultiLevelTilingPipelinedNode::ApplySubRules(std::vector<State> states) {
  states = SubRule(std::move(states), [&](State state) { return TransformeToGEMM(Downcast<PipelinedState>(state)); });
  states = SubRule(std::move(states), [&](State state) { return TileLoopNest(std::move(state)); });
  states = SubRule(std::move(states), [&](State state) { return AddWriteReusePipelined(Downcast<PipelinedState>(state)); });
  states = SubRule(std::move(states), [&](State state) { return AddReadReusePipelined(Downcast<PipelinedState>(state)); });
  states = SubRule(std::move(states), [&](State state) { return PipelinedPostProcessing(Downcast<PipelinedState>(state)); });
  return states;
}

std::vector<State> MultiLevelTilingPipelinedNode::TransformeToGEMM(PipelinedState state) const {
  BlockRV block_rv = state->block_rv;
  const tir::AutoTensorizeMappingInfo& mapping_info = state->mapping_info;
  tir::StmtSRef block_sref = state->sch->GetSRef(state->block_rv);

  // Add reindex stages
  const tir::BlockNode* block = TVM_SREF_TO_BLOCK(block_sref);
  // Hold the reference of the block before reindex
  const tir::Block block_before_reindex = GetRef<tir::Block>(block);
  if (block->reads.size() != 2 || block->writes.size() != 1) {
    // only matmul-like computation is allowed
    return {};
  }
  state->pipeline_reindex_store = state->sch->ReIndex(state->block_rv, 0, tir::BufferIndexType::kWrite);
  state->pipeline_reindex_A = state->sch->ReIndex(state->block_rv, 0, tir::BufferIndexType::kRead);
  state->pipeline_reindex_B = state->sch->ReIndex(state->block_rv, 1, tir::BufferIndexType::kRead);

  // Transform the layout of reindex buffers accordingly.
  // The index map defines the mapping for the computation block. We need to extract the sub index
  // map to transform the load and store block.
  ICHECK_EQ(mapping_info->mappings.size(), 1U);  // assume only one mapping is present
  const tir::IndexMap& index_map = mapping_info->mappings[0];

  // Find the correspondence between block iters and the iters in the index map.
  std::unordered_map<tir::Var, tir::Var, ObjectPtrHash, ObjectPtrEqual> lhs_to_index_map_src;
  std::unordered_map<tir::Var, PrimExpr, ObjectPtrHash, ObjectPtrEqual> rhs_to_index_map_tgt;
  std::unordered_set<tir::Var, ObjectPtrHash, ObjectPtrEqual> unmapped_index_map_src;
  ICHECK_EQ(mapping_info->lhs_iters.size(), index_map->initial_indices.size());
  for (int i = 0; i < static_cast<int>(mapping_info->lhs_iters.size()); ++i) {
    lhs_to_index_map_src[mapping_info->lhs_iters[i]->var] = index_map->initial_indices[i];
  }
  // The number of result iters in the index map is equal or more than the number of rhs (the
  // tensor intrin) iters. When there are extra iters, these iters represent unmapped iters from
  // the lhs. They will be skipped during pattern matching for tensorization. An example of such
  // case is batch matmul, the batch dimension is kept after layout transformations and it will be
  // kept as a outer loop after tensorization.
  int offset = static_cast<int>(index_map->final_indices.size()) -
               static_cast<int>(mapping_info->rhs_iters.size());
  ICHECK_GE(offset, 0);
  for (int i = 0; i < offset; ++i) {
    const tir::VarNode* var_ptr = index_map->final_indices[i].as<tir::VarNode>();
    ICHECK(var_ptr != nullptr);
    unmapped_index_map_src.insert(GetRef<tir::Var>(var_ptr));
  }
  for (int i = offset; i < static_cast<int>(index_map->final_indices.size()); ++i) {
    rhs_to_index_map_tgt[mapping_info->rhs_iters[i - offset]->var] = index_map->final_indices[i];
  }

  auto f_get_sub_index_map = [&](const tir::Buffer& lhs_buffer, const tir::Region& lhs_region) {
    std::vector<tir::Var> sub_index_map_src;
    std::vector<PrimExpr> sub_index_map_tgt;
    const tir::Buffer& rhs_buffer = mapping_info->lhs_buffer_map[lhs_buffer];
    for (const Range& range : lhs_region) {
      ICHECK(tir::is_one(range->extent));
      const tir::VarNode* var_ptr = range->min.as<tir::VarNode>();
      ICHECK(var_ptr != nullptr);
      const tir::Var& lhs_representer = lhs_to_index_map_src[GetRef<tir::Var>(var_ptr)];
      sub_index_map_src.push_back(lhs_representer);
      if (unmapped_index_map_src.count(lhs_representer)) {
        sub_index_map_tgt.push_back(lhs_representer);
      }
    }
    for (size_t i = 0; i < mapping_info->rhs_buffer_indices[rhs_buffer].size(); ++i) {
      const tir::VarNode* var = mapping_info->rhs_buffer_indices[rhs_buffer][i].as<tir::VarNode>();
      ICHECK(var != nullptr);
      sub_index_map_tgt.push_back(rhs_to_index_map_tgt[GetRef<tir::Var>(var)]);
    }
    return tir::IndexMap(sub_index_map_src, sub_index_map_tgt);
  };

  std::unordered_set<tir::Buffer, ObjectPtrHash, ObjectPtrEqual> visited_buffers;

  Map<tir::Buffer, tir::IndexMap> buffer_sub_index_map;  // cache of the sub index map associated
                                                         // with each buffer

  auto f_transform_buffer_layout = [&](tir::BufferIndexType index_type, int buffer_index) {
    const tir::Buffer& lhs_buffer = tir::GetNthAccessBuffer(
        state->sch->state(), block_before_reindex, buffer_index, index_type);
    if (visited_buffers.count(lhs_buffer)) {
      return;
    }
    visited_buffers.insert(lhs_buffer);
    // Refresh block pointer (block sref is not invalidated)
    block = TVM_SREF_TO_BLOCK(block_sref);
    const tir::BufferRegion& reindexed_buffer_region = tir::GetNthAccessBufferRegion(
        state->sch->state(), GetRef<tir::Block>(block), buffer_index, index_type);
    auto sub_index_map = f_get_sub_index_map(lhs_buffer, reindexed_buffer_region->region);
    buffer_sub_index_map.Set(lhs_buffer, sub_index_map);
    state->sch->TransformLayout(state->block_rv, buffer_index, index_type, sub_index_map, NullOpt);
  };

  for (int i = 0, n = block_before_reindex->reads.size(); i < n; ++i) {
    f_transform_buffer_layout(tir::BufferIndexType::kRead, i);
  }
  for (int i = 0, n = block_before_reindex->writes.size(); i < n; ++i) {
    f_transform_buffer_layout(tir::BufferIndexType::kWrite, i);
  }

  // Transform the layout of current block and reindex blocks
  auto f_transform_reindex_block_layout = [&](const BlockRV& block_rv,
                                              tir::BufferIndexType buffer_type) {
    tir::Buffer buffer =
        tir::GetNthAccessBuffer(state->sch->state(), state->sch->Get(block_rv), 0, buffer_type);
    const auto& sub_index_map = buffer_sub_index_map.at(buffer);
    state->sch->TransformBlockLayout(block_rv, sub_index_map);
  };
  f_transform_reindex_block_layout(state->pipeline_reindex_store, tir::BufferIndexType::kWrite);
  f_transform_reindex_block_layout(state->pipeline_reindex_A, tir::BufferIndexType::kRead);
  f_transform_reindex_block_layout(state->pipeline_reindex_B, tir::BufferIndexType::kRead);
  state->sch->TransformBlockLayout(state->block_rv, index_map);

  // no need for CUDA Core
  // state->block_rv = state->sch->Blockize(state->sch->GetLoops(state->block_rv)[-1]);

  return {std::move(state)};
}

std::vector<State> MultiLevelTilingPipelinedNode::AddReadReusePipelined(PipelinedState state) const {
  std::vector<PipelinedState> ret;
  ret.push_back(state);
  for (const ReuseConfig& config : this->reuse_read_list_) {
    ICHECK(config.req == ReuseType::kMustReuse);
    std::vector<PipelinedState> temp = ret;
    ret.clear();
    for (PipelinedState cur : temp) {
      const BlockRV& block_rv = cur->block_rv;
      for (int level : config.levels) {
        Schedule& new_sch = cur->sch;
        // Enumerate all buffers that are read but not written
        // ReadBufferNDims won't change in the following process
        std::vector<int> read_buffer_ndims = tir::GetReadBufferNDimsPipelined(new_sch->GetSRef(block_rv));
        std::vector<PipelinedState> queue = { cur };
        for (int i = 0, n_reads = read_buffer_ndims.size(); i < n_reads; ++i) {
          std::vector<PipelinedState> new_queue;
          for (PipelinedState& new_state : queue) {
            Schedule& sch = new_state->sch;
            int buffer_ndim = read_buffer_ndims[i];
            if (buffer_ndim == -1) {
              continue;
            }
            const LoopRV& loop_rv = cur->tiles[level - 1].back();
            // Do cache_read
            BlockRV cache_read_block = sch->CacheRead(block_rv, i, config.scope, { block_rv });
            // Insert cache_read block to the proper place
            sch->ComputeAt(cache_read_block, loop_rv, true);
            // Fuse the iterators of the cache_read
            Array<LoopRV> buffer_all_loops = sch->GetLoops(cache_read_block);
            // call Array's ctor for initializer list here, which will insert all element
            // in [buffer_all_loops.end() - buffer_ndim, buffer_all_loops.end()) to the Array
            Array<LoopRV> buffer_loops = Array<LoopRV>{ buffer_all_loops.end() - buffer_ndim, buffer_all_loops.end() };
            LoopRV fused_buffer_loops = sch->Fuse(buffer_loops);
            if (config.scope.compare("shared") == 0) {
              AnnotateCooperativeFetching(&sch, cache_read_block);
              sch->Annotate(cache_read_block, tir::attr::double_buffer_scope, Integer(0));
              // Add local_stage
              // buffer index === 0 since newly-created cache_read block only have one read buffer
              BlockRV local_stage_block = sch->CacheRead(cache_read_block, 0, "local", { cache_read_block });
              // Insert local_stage block to the proper place
              sch->ComputeAt(local_stage_block, loop_rv, true);
              // Fuse local_stage iterators
              buffer_all_loops = sch->GetLoops(local_stage_block);
              buffer_loops = Array<LoopRV>{ buffer_all_loops.end() - buffer_ndim, buffer_all_loops.end() };
              sch->Fuse(buffer_loops);
              AnnotateCooperativeFetching(&sch, local_stage_block);
              // only pipeline outermost reduce loop now
              int r0 = level - 1;
              if (r0 == r_indices_[0]) {
                if (new_state->pipeline_stages.find(r0) == new_state->pipeline_stages.end()) {
                  new_state->pipeline_stages[r0] = 0;
                }
                new_state->pipeline_stages[r0] += 1;
              }
            } else {
              // Remap shared memory to local load to avoid bank conflict
              // This remap require shape of the buffer to be a multiple of 128
              // So try catch here for case that shape don't meets the requirement
              try {
                sch->TransformLayout(cache_read_block, 0, BufferIndexType::kRead, 
                  IndexMap::FromFunc(buffer_ndim, TypedPackedFunc<Array<PrimExpr>(Array<Var>)>(
                    [buffer_ndim](Array<Var> indices) -> Array<PrimExpr> {
                      const Var& j = indices[buffer_ndim - 1];
                      Array<PrimExpr> ret;
                      for (int i = 0; i < buffer_ndim - 1; ++i) ret.push_back(indices[i]);
                      ret.push_back((floordiv(j, 128) * 128 + floordiv(floormod(j, 128), 8) * 4 + floordiv(floormod(j, 8), 4) * 64 + floormod(j, 4)));
                      return ret;
                    }, "128_remap"
                  ))
                );
              } catch(...) { }
              AddSmallUnrollVectorize(&sch, cache_read_block, fused_buffer_loops);
            }
            new_state->read_reuse.emplace(i, cache_read_block);
            new_queue.push_back(new_state);
            if (config.scope.compare("shared") == 0) {
              PipelinedState transform_smem_layout_state = Downcast<PipelinedState>(new_state->Copy());
              transform_smem_layout_state->sch->TransformLayout(cache_read_block, 0, BufferIndexType::kWrite, 
                IndexMap::FromFunc(buffer_ndim, TypedPackedFunc<Array<PrimExpr>(Array<Var>)>(
                  [buffer_ndim](Array<Var> indices) -> Array<PrimExpr> {
                    const Var& i = indices[buffer_ndim - 2];
                    const Var& j = indices[buffer_ndim - 1];
                    Array<PrimExpr> ret;
                    for (int i = 0; i < buffer_ndim - 2; ++i) ret.push_back(indices[i]);
                    ret.push_back(j);
                    ret.push_back(i);
                    return ret;
                  }, "transpose_smem"
                ))
              );
              new_queue.push_back(transform_smem_layout_state);
            }
          }
          queue = new_queue;
        }
        ret.insert(ret.end(), queue.begin(), queue.end());
      }
    }
  }
  std::vector<State> retStates;
  for (const PipelinedState& state : ret) {
    state->sch->ComputeInline(state->pipeline_reindex_A);
    state->sch->ComputeInline(state->pipeline_reindex_B);
    retStates.push_back(state);
  }
  return retStates;
}

std::vector<State> MultiLevelTilingPipelinedNode::AddWriteReusePipelined(PipelinedState state) const {
  const ReuseConfig& config = this->reuse_write_;
  std::vector<int> levels = config.levels;
  ReuseType req = config.req;
  ICHECK(req == ReuseType::kMustReuse);
  if (Optional<Array<Integer>> ann = tir::GetAnn<Array<Integer>>(
          state->sch->GetSRef(state->block_rv), "meta_schedule.write_cache_level")) {
    req = ReuseType::kMustReuse;
    levels.clear();
    std::transform(ann.value().begin(), ann.value().end(), std::back_inserter(levels),
                   [](auto&& v) { return v.IntValue(); });
  }

  std::vector<PipelinedState> results;
  // Add one write cache
  BlockRV write_cache =
      state->sch->CacheWrite(/*block_rv=*/state->block_rv, /*read_buffer_index=*/0,
                             /*storage_scope=*/config.scope);
  state->write_reuse.emplace(0, write_cache);
  for (int level : levels) {
    State new_state = state->Copy();
    const LoopRV& loop_rv = new_state->tiles[level - 1].back();
    new_state->sch->ReverseComputeAt(write_cache, loop_rv, true);
    LoopRV innermost_write_cache_loop = new_state->sch->GetLoops(write_cache).back();
    // AddSmallUnrollVectorize(&new_state->sch, write_cache, innermost_write_cache_loop);
    results.push_back(Downcast<PipelinedState>(new_state));
  }
  std::vector<State> retStates;
  for (const PipelinedState& state : results) {
    state->sch->ReverseComputeInline(state->pipeline_reindex_store);
    retStates.push_back(state);
  }
  return retStates;
}

std::vector<State> MultiLevelTilingPipelinedNode::PipelinedPostProcessing(PipelinedState state) const {
  // add software pipeline
  if (state->pipeline_stages.size() != 1) LOG(FATAL) << "Error pipeline stage number!";
  auto iter = state->pipeline_stages.begin();
  int level = iter->first;
  LoopRV loop0 = state->sch->Fuse(state->tiles[level]);
  int buffer_num = iter->second;
  Array<Integer> pipeline_order, pipeline_stage;
  // only the outermost reduce axis will be pipelined now
  // and this loop must consist of 2 * buffer_num + 1 blocks, sequentially:
  // -------------------------------------------------------------
  // | block                             | order         | stage |
  // -------------------------------------------------------------
  // | buffer(1)_global2local            | 0             | 0     |
  // | buffer(1)_local2shared            | buffernum + 1 | 0     |
  // | buffer(2)_global2local            | 1             | 0     |
  // | buffer(2)_local2shared            | buffernum + 2 | 0     |
  // | ...                               | ...           | ...   |
  // | buffer(buffernum)_global2local    | buffernum - 1 | 0     |
  // | buffer(buffernum)_local2shared    | 2 * buffernum | 0     |
  // | compute block (original blcok_rv) | buffernum     | 1     |
  // -------------------------------------------------------------
  for (int i = 0; i < buffer_num; i++) {
    pipeline_order.push_back(i);
    pipeline_stage.push_back(0);
    pipeline_order.push_back(i + buffer_num + 1);
    pipeline_stage.push_back(0);
  }
  pipeline_order.push_back(buffer_num);
  pipeline_stage.push_back(1);
  state->sch->Annotate(loop0, tir::attr::software_pipeline_order, pipeline_order);
  state->sch->Annotate(loop0, tir::attr::software_pipeline_stage, pipeline_stage);
  // decompose reduction compute block
  state->sch->DecomposeReduction(state->block_rv, loop0);
  // add small unroll and vectorize for innermost compute
  // unroll the innermost reduce loop
  if (r_indices_.size() != 2) LOG(FATAL) << "Unsupported reduction structure!";
  int r1 = r_indices_[1];
  LoopRV loop1 = state->sch->Fuse(state->tiles[r1]);
  state->sch->Unroll(loop1);
  return { state };
}

std::vector<int> MultiLevelTilingPipelinedNode::GetValidVectorLens(tir::Schedule* sch, const tir::BlockRV& block) const {
  // Filter out invalid vector lanes according to the data type.
  const tir::BlockNode* block_node = (*sch)->GetSRef(block)->StmtAs<tir::BlockNode>();
  ICHECK_EQ(block_node->writes.size(), 1);
  const runtime::DataType dtype = block_node->writes[0]->buffer->dtype;
  std::function<bool(int)> f_filter = nullptr;
  if (dtype == runtime::DataType::Float(32)) {
    f_filter = [&](int vector_len) { return vector_len <= 4; };
  } else if (dtype == runtime::DataType::Float(16)) {
    f_filter = [&](int vector_len) {
      return (vector_len == 1 || vector_len % 2 == 0) && vector_len <= 8;
    };
  } else if (dtype == runtime::DataType::Int(8)) {
    f_filter = [&](int vector_len) { return vector_len <= 16; };
  } else {
    f_filter = [&](int vector_len) { return true; };
  }
  std::vector<int> valid_vector_lens;
  valid_vector_lens.reserve(vector_load_lens.size());
  std::copy_if(vector_load_lens.begin(), vector_load_lens.end(), std::back_inserter(valid_vector_lens), f_filter);
  return valid_vector_lens;
}

void MultiLevelTilingPipelinedNode::AddSmallUnrollVectorize(Schedule* sch,
                                                   const tir::BlockRV& block,
                                                   const tir::LoopRV& loop) const {
  std::vector<int> valid_vector_lens = GetValidVectorLens(sch, block);
  if (!valid_vector_lens.empty()) {
    int n = valid_vector_lens.size();
    double prob = 1.0 / n;
    tir::ExprRV vector_load_len =
        (*sch)->SampleCategorical(support::AsArray<int, Integer>(valid_vector_lens),
                                  Array<FloatImm>(n, FloatImm(DataType::Float(64), prob)));
    Array<LoopRV> split_loops = (*sch)->Split(loop, { NullOpt, vector_load_len }, true);
    if (split_loops.size() != 2) LOG(FATAL) << "Unexpected split error!";
    (*sch)->Unroll(split_loops[0]);
    (*sch)->Vectorize(split_loops[1]);
  }
}

ScheduleRule ScheduleRule::MultiLevelTilingPipelined(String structure, Optional<Array<String>> tile_binds,
                                            Optional<Integer> max_innermost_factor,
                                            Optional<Array<Integer>> vector_load_lens,
                                            Optional<Array<Map<String, ObjectRef>>> reuse_read,
                                            Optional<Map<String, ObjectRef>> reuse_write) {
  auto node = MultiLevelTilingInitCommon<MultiLevelTilingPipelinedNode>(
      structure, tile_binds, max_innermost_factor, vector_load_lens, NullOpt, reuse_write);
  if (reuse_read.defined()) {
    node->reuse_read_list_.reserve(reuse_read.value().size());
    for (auto& reuse : reuse_read.value()) {
      node->reuse_read_list_.push_back(ReuseConfig(reuse));
    }
  }
  return ScheduleRule(node);
}

TVM_REGISTER_NODE_TYPE(MultiLevelTilingPipelinedNode);
TVM_REGISTER_GLOBAL("meta_schedule.ScheduleRuleMultiLevelTilingPipelined")
    .set_body_typed(ScheduleRule::MultiLevelTilingPipelined);

}  // namespace meta_schedule
}  // namespace tvm
