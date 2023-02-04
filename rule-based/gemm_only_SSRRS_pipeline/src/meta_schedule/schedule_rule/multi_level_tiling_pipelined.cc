

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

  State Copy() const final;

  static constexpr const char* _type_key = "meta_schedule.PipelinedState";
  TVM_DECLARE_FINAL_OBJECT_INFO(PipelinedStateNode, StateNode);
};

class PipelinedState : public State {
 public:
  explicit PipelinedState(Schedule sch, BlockRV block_rv);
  TVM_DEFINE_MUTABLE_OBJECT_REF_METHODS(PipelinedState, State, PipelinedStateNode);
};

TVM_REGISTER_OBJECT_TYPE(PipelinedStateNode);

PipelinedState::PipelinedState(Schedule sch, BlockRV block_rv) {
  ObjectPtr<PipelinedStateNode> node = make_object<PipelinedStateNode>();
  node->sch = std::move(sch);
  node->block_rv = std::move(block_rv);
  node->pipeline_stages.clear();
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

  // Subrule: Add multi-level load cache
  inline std::vector<State> AddReadReusePipelined(PipelinedState state) const;
  // Subrule: Add write cache with small unroll & vectorize
  inline std::vector<State> AddWriteReusePipelined(State state) const;
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

  Array<Schedule> results;
  // add an unannotated schedule for MultiLevelTiling to process
  // make sure pipelined traces could coexist with original MultiLevelTiling trace
  results.push_back(sch->Copy());
  // annotate tiling structure to avoid MultiLevelTiling to process
  sch->Annotate(block_rv, tir::attr::meta_schedule_tiling_structure, structure);
  for (auto&& state : ApplySubRules({ PipelinedState(sch, block_rv) })) {
    results.push_back(std::move(state->sch));
  }
  return results;
}

std::vector<State> MultiLevelTilingPipelinedNode::ApplySubRules(std::vector<State> states) {
  states = SubRule(std::move(states), [&](State state) { return TileLoopNest(std::move(state)); });
  states = SubRule(std::move(states), [&](State state) { return AddWriteReusePipelined(std::move(state)); });
  states = SubRule(std::move(states), [&](State state) { return AddReadReusePipelined(Downcast<PipelinedState>(state)); });
  states = SubRule(std::move(states), [&](State state) { return PipelinedPostProcessing(Downcast<PipelinedState>(state)); });
  return states;
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
    retStates.push_back(state);
  }
  return retStates;
}

std::vector<State> MultiLevelTilingPipelinedNode::AddWriteReusePipelined(State state) const {
  const ReuseConfig& config = this->reuse_write_;
  if (config.req == ReuseType::kNoReuse) {
    return { std::move(state) };
  }
  std::vector<int> levels = config.levels;
  ReuseType req = config.req;
  if (Optional<Array<Integer>> ann = tir::GetAnn<Array<Integer>>(
          state->sch->GetSRef(state->block_rv), "meta_schedule.write_cache_level")) {
    req = ReuseType::kMustReuse;
    levels.clear();
    std::transform(ann.value().begin(), ann.value().end(), std::back_inserter(levels),
                   [](auto&& v) { return v.IntValue(); });
  }
  std::vector<State> results;
  if (req == ReuseType::kMayReuse) {
    // Case 1. If the write cache is already there, we don't need to add another.
    Array<BlockRV> consumer_rvs = state->sch->GetConsumers(state->block_rv);
    if (consumer_rvs.size() == 1 && IsWriteCache(state->sch->GetSRef(consumer_rvs[0]))) {
      for (int level : levels) {
        State new_state = state->Copy();
        const LoopRV& loop_rv = new_state->tiles[level - 1].back();
        new_state->sch->ReverseComputeAt(consumer_rvs[0], loop_rv, true);
        results.push_back(std::move(new_state));
      }
      state->write_reuse.emplace(0, consumer_rvs[0]);
      results.push_back(state);
      return results;
    } else {
      // Case 2. No write cache is added
      State new_state = state->Copy();
      results.emplace_back(std::move(new_state));
    }
  }

  // Case 3. Add one write cache
  BlockRV write_cache =
      state->sch->CacheWrite(/*block_rv=*/state->block_rv, /*read_buffer_index=*/0,
                             /*storage_scope=*/config.scope);
  state->write_reuse.emplace(0, write_cache);
  for (int level : levels) {
    State new_state = state->Copy();
    const LoopRV& loop_rv = new_state->tiles[level - 1].back();
    new_state->sch->ReverseComputeAt(write_cache, loop_rv, true);
    LoopRV innermost_write_cache_loop = new_state->sch->GetLoops(write_cache).back();
    AddSmallUnrollVectorize(&new_state->sch, write_cache, innermost_write_cache_loop);
    results.push_back(std::move(new_state));
  }
  return results;
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
  }
  std::vector<int> valid_vector_lens;
  valid_vector_lens.reserve(vector_load_lens.size());
  if (f_filter != nullptr) {
    std::copy_if(vector_load_lens.begin(), vector_load_lens.end(),
                 std::back_inserter(valid_vector_lens), f_filter);
  } else {
    valid_vector_lens = vector_load_lens;
  }
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
