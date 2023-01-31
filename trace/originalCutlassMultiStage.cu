// #pragma once

#include <type_traits>
#include <cstdint>
#include <cstdio>

#define CUTLASS_HOST_DEVICE __forceinline__ __device__ __host__
#define CUTLASS_DEVICE __forceinline__ __device__
// #define CUTLASS_PRAGMA_UNROLL #pragma unroll

#define CUTLASS_ENABLE_L2_PREFETCH 1
#define CUDA_CP_ASYNC_ACTIVATED 1

struct IntPair { // pair
    int x; // continuous / row
    int y; // strided / column

    CUTLASS_HOST_DEVICE
    IntPair swap() const {
        return {y, x};
    }

    CUTLASS_HOST_DEVICE
    IntPair operator+(const IntPair &o) const {
        return {x + o.x, y + o.y};
    }

    CUTLASS_HOST_DEVICE
    IntPair &operator+=(const IntPair &o) {
        x += o.x, y += o.y;
        return *this;
    }
};

template<int X, int Y>
struct IntPairTemplate {
    static constexpr int x = X;
    static constexpr int y = Y;
};

template <typename T>
struct sizeof_bits {
    static int const value = int(sizeof(T) * 8);
};

template<typename T, int N, int Align = 16>
struct AlignedBuffer {
    using Storage = uint8_t;
    static int const kBytes = (sizeof_bits<T>::value * N + 7) / 8;
    alignas(Align) Storage storage[kBytes];

    CUTLASS_HOST_DEVICE
    T *data() {
        return reinterpret_cast<T *>(storage);
    }
};

template<typename T, int N>
class Array {
public:
    T storage[N];

    CUTLASS_HOST_DEVICE
    void fill(const T &value) {
        #pragma unroll
        for (int i = 0; i < N; ++i) {
            storage[i] = value; // static_cast<Storage>(value) ???
        }
    }

    CUTLASS_HOST_DEVICE
    void clear() {
        fill(T(0));
    }

    CUTLASS_HOST_DEVICE
    void print() const {
        for (int i = 0; i < N; i++) printf("%f ", storage[i]);
        printf("\n");
    }
};

template <typename T, int N, int Alignment = sizeof_bits<T>::value * N / 8>
class alignas(Alignment) AlignedArray: public Array<T, N> {};

using LongIndex = int64_t;
using Index = int32_t;

enum LayoutType {
    ColumnMajorType, RowMajorType
};

template<typename T, LayoutType Layout>
class TensorRef {
private:
    T *ptr_;
    LongIndex stride_; // Layout's stride

public:
    CUTLASS_HOST_DEVICE
    TensorRef() : ptr_(nullptr) {}

    CUTLASS_HOST_DEVICE
    TensorRef(T *ptr, LongIndex stride) : ptr_(ptr), stride_(stride) {}

    CUTLASS_HOST_DEVICE
    LongIndex stride() const { return stride_; }

    CUTLASS_HOST_DEVICE
    LongIndex offset(const IntPair &coord) const {
        if (Layout == RowMajorType) return LongIndex(coord.x) * stride_ + coord.y;
        else return LongIndex(coord.y) * stride_ + coord.x;
    }

    CUTLASS_HOST_DEVICE
    T *data() const { return ptr_; }

    CUTLASS_HOST_DEVICE
    T &data(LongIndex idx) {
        return ptr_[idx];
    }

    CUTLASS_HOST_DEVICE
    void add_coord_offset(const IntPair &coord) {
        ptr_ += offset(coord);
    }

    CUTLASS_HOST_DEVICE
    void reset(T *ptr, LongIndex stride) {
        ptr_ = ptr, stride_ = stride;
    }
    
    CUTLASS_HOST_DEVICE
    T &at(IntPair coord) {
        return data(offset(coord));
    }
};

template<LayoutType Layout>
class GlobalMemoryIterator {
public:
    using Pointer = float *;
    using NonConstPointer = typename std::remove_const<float>::type *;
    using BytePointer = char *;
    using Fragment = Array<float, 4>;
    using AccessType = AlignedArray<float, 1>;

private:
    uint32_t predicate_;
    BytePointer pointer_;
    // int iteration_vector_, iteration_contiguous_;
    int iteration_strided_;
    bool is_residue_tile_;
    IntPair thread_offset_, residue_offset_;

private:
    CUTLASS_DEVICE
    void compute_predicates_(IntPair extent, bool is_steady_state = false) {
        predicate_ = 0b1111u;
        return;

        predicate_ = 0u;
        #pragma unroll
        for (int s = 0; s < 4; ++s) {
            IntPair iteration_coord = {0, s * 2};
            IntPair coord = thread_offset_ + iteration_coord;
            bool guard;
            if (is_steady_state) {
                // if (AdvanceRank == 0) guard = (coord.y < extent.y);
                // else 
                guard = (coord.x < extent.x);
            } else guard = (coord.x < extent.x && coord.y < extent.y);
            predicate_ |= (unsigned(guard) << s);
        }
    }

    CUTLASS_HOST_DEVICE
    void set_predicates(int thread_id, const IntPair &threadblock_offset) {
        // IntPair residue_extent;
        // if (AdvanceRank) {
            // int residue_size = (1024 - threadblock_offset.y) % 8; // = 0
            // if (!residue_size) residue_size = 8;
            // residue_offset_ = {0, residue_size};
            // residue_extent = {1024, threadblock_offset.y + residue_size};
        // } else {
        //     int residue_size = (1024 - threadblock_offset.x) % Shape::x; // = 0
        //     if (!residue_size) residue_size = Shape::x;
        //     residue_offset_ = {residue_size, 0};
        //     residue_extent = {threadblock_offset.x + residue_size, 1024};
        // }
        residue_offset_ = {0, 8};
        thread_offset_ = threadblock_offset + IntPair({thread_id % 128, thread_id / 128});
        compute_predicates_({1024, 8}, false);
        set_iteration_index(0);
    }

    CUTLASS_HOST_DEVICE
    void add_pointer_offset(LongIndex pointer_offset) {
        pointer_ += 4 * pointer_offset;
    }

public:
    CUTLASS_HOST_DEVICE
    GlobalMemoryIterator(
        Pointer pointer,
        int thread_id,
        IntPair threadblock_offset
    ) : 
        pointer_(reinterpret_cast<BytePointer>(const_cast<NonConstPointer>(pointer))),
        is_residue_tile_(true) {
        if (Layout == RowMajorType) threadblock_offset = threadblock_offset.swap();
        set_predicates(thread_id, threadblock_offset);
        add_pointer_offset(LongIndex(thread_offset_.x) + LongIndex(thread_offset_.y) * LongIndex(1024));
    }

    CUTLASS_HOST_DEVICE
    void clear_mask(bool enable) {
        predicate_ = enable ? 0u : predicate_;
    }

    CUTLASS_HOST_DEVICE
    void set_iteration_index(int index) {
        // iteration_vector_ = 0;
        // iteration_contiguous_ = 0;
        iteration_strided_ = index;
    }

    CUTLASS_HOST_DEVICE
    bool valid() const {
        return (predicate_ & (1u << iteration_strided_));

        int pred_idx = iteration_strided_;
        if (pred_idx / 16 != 0) printf("Error!\n");
        int residual = pred_idx % 16;
        int byte_idx = residual / 4;
        int bit_idx  = residual % 4;
        return (predicate_ & (1u << (byte_idx * 8 + bit_idx))) != 0;
    }

    CUTLASS_HOST_DEVICE
    AccessType *get() const {
        // return reinterpret_cast<AccessType *>(
        //     pointer_ +
        //     iteration_contiguous_ * 4
        // ) + iteration_vector_;
        return reinterpret_cast<AccessType *>(pointer_);
    }

    CUTLASS_HOST_DEVICE
    void increment() {
        // ++iteration_vector_;
        // if (iteration_vector_ < 1) return;
        // iteration_vector_ = 0;
        // ++iteration_contiguous_;
        // if (iteration_contiguous_ < 1) return;
        // iteration_contiguous_ = 0;
        ++iteration_strided_;
        if (iteration_strided_ < 4) {
            pointer_ += 8192;
            return;
        }
        iteration_strided_ = 0;
        pointer_ += 8192;
        pointer_ -= 32768;
    }

    CUTLASS_DEVICE
    void add_tile_offset(IntPair tile_offset) {
        if (Layout == RowMajorType) tile_offset = tile_offset.swap();
        if (is_residue_tile_) {
            thread_offset_ += residue_offset_;
            compute_predicates_({1024, 1024}, true);
            add_pointer_offset(LongIndex(residue_offset_.x) + LongIndex(residue_offset_.y) * LongIndex(1024));
            // if (AdvanceRank) {
                pointer_ += LongIndex(32768) * LongIndex(tile_offset.y - 1);
                pointer_ += 128 * tile_offset.x;
            // } else {
            //     pointer_ += LongIndex(32768) * LongIndex(tile_offset.x - 1);
            //     pointer_ +=   8 * tile_offset.y;
            // }
        } else {
            // if (AdvanceRank) {
                pointer_ += LongIndex(32768) * LongIndex(tile_offset.y);
                pointer_ += 128 * tile_offset.x;
            // } else {
            //     pointer_ += LongIndex(32768) * LongIndex(tile_offset.x);
            //     pointer_ +=   8 * tile_offset.y;
            // }
        }
        is_residue_tile_ = false;
    }
};

template<LayoutType Layout>
class SharedMemoryStoreIterator {
private:
    using AccessType = Array<float, 1>;

    AccessType *pointer_;
    LongIndex stride_;

    int iteration_contiguous_, iteration_strided_;
    Index byte_offset_;

public:
    CUTLASS_HOST_DEVICE
    SharedMemoryStoreIterator(TensorRef<float, Layout> ref, int thread_id) : stride_(ref.stride()), byte_offset_(0) {
        pointer_ = reinterpret_cast<AccessType *>(ref.data() + thread_id);
        set_iteration_index(0);
    }

    CUTLASS_HOST_DEVICE
    void set_iteration_index(int index) {
        iteration_contiguous_ = 0;
        iteration_strided_ = index;
    }

    CUTLASS_DEVICE
    AccessType *get() const {
        int access_offset = iteration_strided_ * 2 * stride_ + iteration_contiguous_;
        char * access_byte_ptr = reinterpret_cast<char *>(pointer_ + access_offset);
        return reinterpret_cast<AccessType *>(access_byte_ptr + byte_offset_);
    }

    CUTLASS_HOST_DEVICE
    void increment() {
        // ++iteration_contiguous_;
        // if (iteration_contiguous_ < 1) return;
        // iteration_contiguous_ = 0;
        ++iteration_strided_;
        if (iteration_strided_ < 4) return;
        iteration_strided_ = 0;
        return;
    }

    CUTLASS_DEVICE
    void add_tile_offset(IntPair coord) {
        if (Layout == RowMajorType) coord = coord.swap();
        byte_offset_ += sizeof(float) * (coord.x * 128 + coord.y * 8 * stride_);
    }
};

// TODO __nv_cvta_generic_to_shared_impl not found
// currently just use the google version
inline __device__ unsigned cutlass_get_smem_pointer(void *ptr) {
    return static_cast<unsigned>(__cvta_generic_to_shared(ptr));
}

inline __device__ unsigned cutlass_get_smem_pointer(void const *ptr) {
    return cutlass_get_smem_pointer(const_cast<void *>(ptr));
}

CUTLASS_DEVICE
void shared_load(Array<float, 4> &D, void const *ptr) {
    unsigned addr = cutlass_get_smem_pointer(ptr);
    uint4 v;
    asm volatile ("ld.shared.v4.b32 {%0, %1, %2, %3}, [%4];" : 
    "=r"(v.x), "=r"(v.y), "=r"(v.z), "=r"(v.w) : "r"(addr));
    D = reinterpret_cast<Array<float, 4> const &>(v);
}

template<typename Shape, LayoutType Layout>
class SharedMemoryLoadIterator {
public:
    using Fragment = Array<float, 8>;

private:
    TensorRef<Array<float, 4>, Layout> ref_;

    CUTLASS_DEVICE
    IntPair layout_inverse(int offset) {
        int row_major = offset / 16;
        int residual = offset % 16;
        int column = residual / 2;
        int row_minor = residual % 2;
        return {row_major * 2 + row_minor, column};
    }

public:
    CUTLASS_DEVICE
    SharedMemoryLoadIterator(TensorRef<float, Layout> ref, int lane_id) {
        IntPair lane_offset;
        if (Layout == ColumnMajorType) lane_offset = {layout_inverse(lane_id).x * 4, 0};
        else lane_offset = {0, layout_inverse(lane_id).y * 4};
        ref.add_coord_offset(lane_offset);
        ref_.reset(reinterpret_cast<Array<float, 4> *>(ref.data()), ref.stride() / 4);
    }

    CUTLASS_DEVICE
    void add_tile_offset(IntPair coord) {
        if (Layout == RowMajorType) ref_.add_coord_offset({coord.x * Shape::x, coord.y * Shape::y / 4});
        else ref_.add_coord_offset({coord.x * Shape::x / 4, coord.y * Shape::y});
    }

    CUTLASS_DEVICE
    void set_kgroup_index(int k_group) {
        // no operation here
        return;
    }

    CUTLASS_DEVICE
    void load(Fragment &frag) const {
        Array<float, 4> *dst_ptr = reinterpret_cast<Array<float, 4> *>(&frag);
        for (int mn = 0; mn < 2; ++mn) {
            void const * ptr;
            if (Layout == RowMajorType) ptr = ref_.data() + ref_.offset({0, mn * 8});
            else ptr = ref_.data() + ref_.offset({mn * 4, 0});
            shared_load(dst_ptr[mn], ptr);
        }
    }

    CUTLASS_DEVICE
    void increment() {
        if (Layout == RowMajorType) ref_.add_coord_offset({Shape::x, 0});
        else ref_.add_coord_offset({0, Shape::y});
    }
};

using GlobalMemoryIteratorA = GlobalMemoryIterator<ColumnMajorType>;
using GlobalMemoryIteratorB = GlobalMemoryIterator<RowMajorType>;
using SharedMemoryStoreIteratorA = SharedMemoryStoreIterator<ColumnMajorType>;
using SharedMemoryStoreIteratorB = SharedMemoryStoreIterator<RowMajorType>;
using SharedMemoryLoadIteratorA = SharedMemoryLoadIterator<IntPairTemplate<32, 1>, ColumnMajorType>;
using SharedMemoryLoadIteratorB = SharedMemoryLoadIterator<IntPairTemplate<1, 64>, RowMajorType>;

template<int SizeInBytes = 4>
CUTLASS_DEVICE
void cp_async(void *smem_ptr, void const *global_ptr, bool pred_guard = true) {
#if CUDA_CP_ASYNC_ACTIVATED
    unsigned smem_int_ptr = cutlass_get_smem_pointer(smem_ptr);
    asm volatile(
        "{\n"
        "  .reg .pred p;\n"
        "  setp.ne.b32 p, %0, 0;\n"
#if CUTLASS_ENABLE_L2_PREFETCH
        "  @p cp.async.ca.shared.global.L2::128B [%1], [%2], %3;\n"
#else
        "  @p cp.async.ca.shared.global [%1], [%2], %3;\n"
#endif
        "}\n" ::"r"((int)pred_guard),
        "r"(smem_int_ptr), "l"(global_ptr), "n"(SizeInBytes)
    );
#else
    using AccessType = Array<uint8_t, SizeInBytes>;
    if (pred_guard) *static_cast<AccessType *>(smem_ptr) = *static_cast<AccessType const *>(global_ptr);
#endif
}

template<int SizeInBytes = 4>
CUTLASS_DEVICE
void cp_async_zfill(void *smem_ptr, void const *global_ptr, bool pred_guard = true) {
#if CUDA_CP_ASYNC_ACTIVATED
    unsigned smem_int_ptr = cutlass_get_smem_pointer(smem_ptr);
    int src_in_bytes = (pred_guard ? SizeInBytes : 0);
    asm volatile(
#if CUTLASS_ENABLE_L2_PREFETCH
        "cp.async.ca.shared.global.L2::128B [%0], [%1], %2, %3;\n" ::"r"(smem_int_ptr),
#else
        "cp.async.ca.shared.global [%0], [%1], %2, %3;\n" ::"r"(smem_int_ptr),
#endif
        "l"(global_ptr), "n"(SizeInBytes), "r"(src_in_bytes)
    );
#else
    using AccessType = Array<uint8_t, SizeInBytes>;
    if (pred_guard) *static_cast<AccessType *>(smem_ptr) = *static_cast<AccessType const *>(global_ptr);
    else {
        AccessType zeros;
        zeros.clear();
        *static_cast<AccessType *>(smem_ptr) = zeros;
    }
#endif
}

CUTLASS_DEVICE
void cp_async_fence() {
#if CUDA_CP_ASYNC_ACTIVATED
    asm volatile("cp.async.commit_group;\n" ::);
#endif
}

template<int N>
CUTLASS_DEVICE
void cp_async_wait() {
#if CUDA_CP_ASYNC_ACTIVATED
    asm volatile("cp.async.wait_group %0;\n" ::"n"(N));
#endif
}

class Mma {
private:
    // iterator responsible for store to smem
    SharedMemoryStoreIteratorA smem_iterator_A_;
    SharedMemoryStoreIteratorB smem_iterator_B_;
    // iterator responsible for load from smem
    SharedMemoryLoadIteratorA warp_tile_iterator_A_;
    SharedMemoryLoadIteratorB warp_tile_iterator_B_;

    CUTLASS_HOST_DEVICE
    void warp_mma(Array<float, 64> &D, const Array<float, 8> &A, const Array<float, 8> &B, const Array<float, 64> &C) {
        TensorRef<float const, ColumnMajorType> a_ref(reinterpret_cast<float const *>(&A), 8);
        TensorRef<float const, RowMajorType> b_ref(reinterpret_cast<float const *>(&B), 8);
        TensorRef<float, RowMajorType> d_ref(reinterpret_cast<float *>(&D), 8);
        D = C;
        int k = 0;
        #pragma unroll
        for (int n = 0; n < 8; n += 2) {
            #pragma unroll
            for (int m = 0; m < 8; m += 2) {
                int m_serpentine = (n % 4) ? (6 - m) : m;
                {
                    IntPair mn = {m_serpentine, n};
                    IntPair mk = {m_serpentine, k};
                    IntPair kn = {k, n};
                    d_ref.at(mn) = a_ref.at(mk) * b_ref.at(kn) + d_ref.at(mn);
                }
                {
                    IntPair mn = {m_serpentine + 1, n};
                    IntPair mk = {m_serpentine + 1, k};
                    IntPair kn = {k, n};
                    d_ref.at(mn) = a_ref.at(mk) * b_ref.at(kn) + d_ref.at(mn);
                }
                {
                    IntPair mn = {m_serpentine + 1, n + 1};
                    IntPair mk = {m_serpentine + 1, k};
                    IntPair kn = {k, n + 1};
                    d_ref.at(mn) = a_ref.at(mk) * b_ref.at(kn) + d_ref.at(mn);
                }
                {
                    IntPair mn = {m_serpentine, n + 1};
                    IntPair mk = {m_serpentine, k};
                    IntPair kn = {k, n + 1};
                    d_ref.at(mn) = a_ref.at(mk) * b_ref.at(kn) + d_ref.at(mn);
                }
            }
        }
    }

public:
    class SharedStorage {
    private:
        AlignedBuffer<float, 4096> operand_A;
        AlignedBuffer<float, 4096> operand_B;

    public:
        CUTLASS_HOST_DEVICE
        TensorRef<float, ColumnMajorType> operand_A_ref() {
            return TensorRef<float, ColumnMajorType>(operand_A.data(), 128); // ShapeA::kRow
        }

        CUTLASS_HOST_DEVICE
        TensorRef<float, RowMajorType>    operand_B_ref() {
            return TensorRef<float, RowMajorType>   (operand_B.data(), 128); // ShapeB::kColumn
        }
    };

    CUTLASS_DEVICE
    Mma(SharedStorage &shared_storage, int thread_idx, int warp_idx, int lane_idx) :
        smem_iterator_A_(shared_storage.operand_A_ref(), thread_idx),
        smem_iterator_B_(shared_storage.operand_B_ref(), thread_idx),
        warp_tile_iterator_A_(shared_storage.operand_A_ref(), lane_idx),
        warp_tile_iterator_B_(shared_storage.operand_B_ref(), lane_idx) {
        int warp_idx_mn = warp_idx % 8;
        // int warp_idx_k = warp_idx / 8; // == 0
        int warp_idx_m = warp_idx_mn % 4;
        int warp_idx_n = warp_idx_mn / 4;
        warp_tile_iterator_A_.add_tile_offset({warp_idx_m, 0});
        warp_tile_iterator_B_.add_tile_offset({0, warp_idx_n});
    }

    CUTLASS_DEVICE
    void copy_tiles_and_advance(GlobalMemoryIteratorA &iterator_A, GlobalMemoryIteratorB &iterator_B, int group_start_A = 0, int group_start_B = 0) {
        iterator_A.set_iteration_index(group_start_A);
        smem_iterator_A_.set_iteration_index(group_start_A);
        if (group_start_A < 4) {
            typename GlobalMemoryIteratorA::AccessType *dst_ptr = reinterpret_cast<typename GlobalMemoryIteratorA::AccessType *>(smem_iterator_A_.get());
            auto gmem_ptr = iterator_A.get();
            cp_async(dst_ptr, gmem_ptr, iterator_A.valid());
            iterator_A.increment();
            smem_iterator_A_.increment();
        }

        iterator_B.set_iteration_index(group_start_B);
        smem_iterator_B_.set_iteration_index(group_start_B);
        if (group_start_B < 4) {
            typename GlobalMemoryIteratorB::AccessType *dst_ptr = reinterpret_cast<typename GlobalMemoryIteratorB::AccessType *>(smem_iterator_B_.get());
            auto gmem_ptr = iterator_B.get();
            cp_async(dst_ptr, gmem_ptr, iterator_B.valid());
            iterator_B.increment();
            smem_iterator_B_.increment();
        }
    }

    CUTLASS_DEVICE
    void operator()(
        int gemm_k_iterations, Array<float, 64> &accum,
        GlobalMemoryIteratorA iterator_A, GlobalMemoryIteratorB iterator_B, const Array<float, 64> &src_accum
    ) {
        #pragma unroll
        for (int stage = 0; stage < 3; ++stage, --gemm_k_iterations) {
            // iterator_A.clear_mask(gemm_k_iterations == 0);
            // iterator_B.clear_mask(gemm_k_iterations == 0);

            iterator_A.set_iteration_index(0);
            smem_iterator_A_.set_iteration_index(0);
            #pragma unroll
            for (int j = 0; j < 4; ++j) {
                typename GlobalMemoryIteratorA::AccessType *dst_ptr = reinterpret_cast<typename GlobalMemoryIteratorA::AccessType *>(smem_iterator_A_.get());
                int src_bytes = (iterator_A.valid() ? 4 : 0);
                cp_async_zfill<4>(dst_ptr, iterator_A.get(), iterator_A.valid());
                iterator_A.increment();
                smem_iterator_A_.increment();
            }

            iterator_B.set_iteration_index(0);
            smem_iterator_B_.set_iteration_index(0);
            #pragma unroll
            for (int j = 0; j < 4; ++j) {
                typename GlobalMemoryIteratorB::AccessType *dst_ptr = reinterpret_cast<typename GlobalMemoryIteratorB::AccessType *>(smem_iterator_B_.get());
                int src_bytes = (iterator_B.valid() ? 4 : 0);
                cp_async_zfill<4>(dst_ptr, iterator_B.get(), iterator_B.valid());
                iterator_B.increment();
                smem_iterator_B_.increment();
            }

            iterator_A.add_tile_offset({0, 1});
            iterator_B.add_tile_offset({1, 0});
            smem_iterator_A_.add_tile_offset({0, 1});
            smem_iterator_B_.add_tile_offset({1, 0});

            cp_async_fence();
        }

        accum = src_accum;

        cp_async_wait<2>();
        __syncthreads();

        Array<float, 8> warp_loaded_frag_A[2];
        Array<float, 8> warp_loaded_frag_B[2];
        // Array<float, 8> warp_transformed_frag_A[2];
        // Array<float, 8> warp_transformed_frag_B[2];

        warp_tile_iterator_A_.load(warp_loaded_frag_A[0]);
        warp_tile_iterator_B_.load(warp_loaded_frag_B[0]);
        warp_tile_iterator_A_.increment();
        warp_tile_iterator_B_.increment();
        // iterator_A.clear_mask(gemm_k_iterations == 0);
        // iterator_B.clear_mask(gemm_k_iterations == 0);
        int smem_write_stage_idx = 3;
        int smem_read_stage_idx = 0;
        // warp_transformed_frag_A[0] = warp_loaded_frag_A[0];
        // warp_transformed_frag_B[0] = warp_loaded_frag_B[0];

        #pragma unroll 1
        for(; gemm_k_iterations > -3; ) {
            #pragma unroll
            for (int warp_mma_k = 0; warp_mma_k < 8; ++warp_mma_k) {
                warp_tile_iterator_A_.load(warp_loaded_frag_A[(warp_mma_k + 1) % 2]);
                warp_tile_iterator_B_.load(warp_loaded_frag_B[(warp_mma_k + 1) % 2]);
                warp_tile_iterator_A_.increment();
                warp_tile_iterator_B_.increment();

                warp_mma(accum, warp_loaded_frag_A[warp_mma_k % 2], warp_loaded_frag_B[warp_mma_k % 2], accum);

                if (warp_mma_k < 7) {
                    int group_start_iteration_A = warp_mma_k;
                    int group_start_iteration_B = warp_mma_k;
                    copy_tiles_and_advance(iterator_A, iterator_B, group_start_iteration_A, group_start_iteration_B);
                }
                if (warp_mma_k + 2 == 8) {
                    int group_start_iteration_A = warp_mma_k + 1;
                    int group_start_iteration_B = warp_mma_k + 1;
                    copy_tiles_and_advance(iterator_A, iterator_B, group_start_iteration_A, group_start_iteration_B);

                    cp_async_fence();

                    cp_async_wait<2>();
                    __syncthreads();

                    iterator_A.add_tile_offset({0, 1});
                    iterator_B.add_tile_offset({1, 0});
                    smem_iterator_A_.add_tile_offset({0, 1});
                    smem_iterator_B_.add_tile_offset({1, 0});

                    if (smem_write_stage_idx == 3) {
                        smem_iterator_A_.add_tile_offset({0, -4});
                        smem_iterator_B_.add_tile_offset({-4, 0});
                        smem_write_stage_idx = 0;
                    } else ++smem_write_stage_idx;
                    if (smem_read_stage_idx == 3) {
                        warp_tile_iterator_A_.add_tile_offset({0, -32});
                        warp_tile_iterator_B_.add_tile_offset({-32, 0});
                        smem_read_stage_idx = 0;
                    } else ++smem_read_stage_idx;

                    --gemm_k_iterations;
                    // !! this is not useless
                    iterator_A.clear_mask(gemm_k_iterations == 0);
                    iterator_B.clear_mask(gemm_k_iterations == 0);
                }
            }
        }
    }
};

class FragmentIterator {
private:
    using AccessType = Array<float, 4>;

    AccessType const *accumulators_;
    int index_;

public:
    CUTLASS_HOST_DEVICE
    FragmentIterator(const Array<float, 64> &accum) : accumulators_(reinterpret_cast<AccessType const *>(&accum)), index_(0) {}

    CUTLASS_HOST_DEVICE
    void increment() {
        ++index_;
    }

    CUTLASS_HOST_DEVICE
    void load(Array<float, 8> &frag) {
        AccessType *frag_ptr = reinterpret_cast<AccessType *>(&frag);
        #pragma unroll
        for (int n = 0; n < 2; ++n) {
            frag_ptr[n] = accumulators_[index_ * 2 + n];
        }
    }
};

class EpilogueSharedMemoryStoreIterator {
private:
    using AccessType = AlignedArray<float, 1>;

    AccessType *pointer_;
    LongIndex layout_stride_;

    CUTLASS_DEVICE
    LongIndex layout_get(const IntPair &coord) {
        return LongIndex(coord.x) * LongIndex(layout_stride_) + LongIndex(coord.y);
    }

public:
    CUTLASS_DEVICE
    EpilogueSharedMemoryStoreIterator(const TensorRef<float, RowMajorType> &ref, int lane_id) :
        pointer_(reinterpret_cast<AccessType *>(ref.data())), layout_stride_(ref.stride()) {
        // RowMajorInterleaved<2>
        int residual = lane_id % 16;
        IntPair lane_offset = {(lane_id / 16) * 2 + residual % 2, residual / 2};
        pointer_ += layout_get({lane_offset.x, lane_offset.y * 4});
    }

    CUTLASS_DEVICE
    void store(const Array<float, 8> &frag) {
        AccessType const *scalar_frag_ptr = reinterpret_cast<AccessType const *>(&frag);
        #pragma unroll
        for (int n = 0; n < 2; ++n) {
            #pragma unroll
            for (int s = 0; s < 4; ++s) {
                pointer_[n * 32 + s] = scalar_frag_ptr[n * 4 + s];
            }
        }
    }

    CUTLASS_DEVICE
    void add_tile_offset(const IntPair tile_offset) {
        pointer_ += layout_get({tile_offset.x * 4, tile_offset.y * 64});
    }
};

class EpilogueSharedMemoryLoadIterator {
private:
    using LoadType = AlignedArray<float, 1, 4>;

    uint8_t *byte_pointer_;
    int stride_;

public:
    CUTLASS_DEVICE
    EpilogueSharedMemoryLoadIterator(const TensorRef<float, RowMajorType> &ref, int thread_idx, int warp_idx, int lane_idx) :
        byte_pointer_(reinterpret_cast<uint8_t *>(ref.data())), stride_(ref.stride() * 4) {
        IntPair thread_offset = {(warp_idx / 2) * 4 + (warp_idx % 2), lane_idx % 32};
        byte_pointer_ += thread_offset.x * stride_ + thread_offset.y * 4;
    }

    CUTLASS_DEVICE
    void load(Array<float, 8> &frag) {
        #pragma unroll
        for (int group = 0; group < 2; ++group) {
            uint8_t const *byte_pointer = byte_pointer_ + group * 2 * stride_;
            LoadType *frag_ptr = reinterpret_cast<LoadType *>(&frag);
            LoadType const *memory_pointer = reinterpret_cast<LoadType const *>(byte_pointer);
            #pragma unroll
            for (int column = 0; column < 4; ++column) {
                frag_ptr[group * 4 + column] = memory_pointer[column * 32];
            }
        }
    }
};

CUTLASS_DEVICE
void global_store(const AlignedArray<float, 1> &D, void *ptr, bool pred_guard) {
    uint32_t const &data = reinterpret_cast<uint32_t const &>(D);
    asm volatile(
        "{\n"
        "  .reg .pred p;\n"
        "  setp.ne.b32 p, %2, 0;\n"
        "  @p st.global.u32 [%0], %1;\n"
        "}\n"
        :
        : "l"(ptr), "r"(data), "r"((int)pred_guard)
    );
}

class OutputTileIterator {
private:
    using AccessType = AlignedArray<float, 1>;

    bool predicates_[4];
    uint8_t *byte_pointer_;
    int state_[3];
    Index thread_start_row_, thread_start_column_;

public:
    CUTLASS_DEVICE
    OutputTileIterator(float *pointer, int thread_idx, int warp_idx, int lane_idx, IntPair threadblock_offset) {
        IntPair thread_offset = IntPair({(warp_idx / 2) * 32 + (warp_idx % 2) * 4, lane_idx % 32}) + threadblock_offset;
        thread_start_row_ = thread_offset.x;
        thread_start_column_ = thread_offset.y;
        #pragma unroll
        for (int c = 0; c < 4; ++c) {
            predicates_[c] = ((thread_offset.y + c * 32) < 1024);
        }
        byte_pointer_ = reinterpret_cast<uint8_t *>(pointer) + LongIndex(thread_offset.x) * LongIndex(4096) + LongIndex(thread_offset.y) * sizeof(AccessType);
        state_[0] = state_[1] = state_[2] = 0;
    }

    CUTLASS_DEVICE
    void store(const Array<float, 8> &frag) {
        uint8_t *byte_pointer = byte_pointer_;
        AccessType const *frag_ptr = reinterpret_cast<AccessType const *>(&frag);
        #pragma unroll
        for (int group = 0; group < 2; ++group) {
            int frag_row_idx = group;
            int row_offset = group * 2;
            bool row_guard = ((row_offset + thread_start_row_) < 1024);
            AccessType *memory_pointer = reinterpret_cast<AccessType *>(byte_pointer);
            #pragma unroll
            for (int column = 0; column < 4; ++column) {
                bool guard = row_guard && predicates_[column];
                global_store(frag_ptr[frag_row_idx * 4 + column], (void *)&memory_pointer[0], guard);
                memory_pointer += 32;
            }
            if (group + 1 < 2) byte_pointer += 32768;
        }
    }

    CUTLASS_DEVICE
    void increment() {
        ++state_[0];
        byte_pointer_ += 4096; // advance row
        thread_start_row_ += 1;
        if (state_[0] == 4) {
            state_[0] = 0;
            ++state_[1];
            byte_pointer_ += 49152; // advance group
            thread_start_row_ += 12;
            if (state_[1] == 2) {
                state_[1] = 0;
                ++state_[2];
                byte_pointer_ += 131072; // advance cluster
                thread_start_row_ += 32;
                if (state_[2] == 1) {
                    state_[2] = 0;
                    byte_pointer_ += 65536; // advance tile
                }
            }
        }
    }
};

class Epilogue {
public:
    class SharedStorage {
    private:
        AlignedBuffer<float, 2320> storage; // <16, 145>

    public:
        CUTLASS_DEVICE
        TensorRef<float, RowMajorType> reference() {
            return TensorRef<float, RowMajorType>(storage.data(), 145);
        }
    };

private:
    SharedStorage &shared_storage_;
    EpilogueSharedMemoryStoreIterator warp_tile_iterator_;
    EpilogueSharedMemoryLoadIterator shared_load_iterator_;

    CUTLASS_DEVICE
    static void acc2smem_source_not_needed(int Advance, FragmentIterator accum_fragment_iterator, EpilogueSharedMemoryStoreIterator &warp_tile_iterator) {
        #pragma unroll
        for (int i = 0; i < Advance; ++i) {
            accum_fragment_iterator.increment();
        }
        Array<float, 8> accum_fragment;
        accum_fragment_iterator.load(accum_fragment);
        warp_tile_iterator.store(accum_fragment);
    }

public:
    CUTLASS_DEVICE
    Epilogue(SharedStorage &shared_storage, int thread_idx, int warp_idx, int lane_idx) : 
        shared_storage_(shared_storage),
        warp_tile_iterator_(shared_storage.reference(), lane_idx),
        shared_load_iterator_(shared_storage.reference(), thread_idx, warp_idx, lane_idx) {
        int warp_k = warp_idx / 8;
        int warp_mn = warp_idx % 8;
        int warp_m = warp_mn % 4;
        int warp_n = warp_mn / 4;
        IntPair warp_offset = {warp_k * 4 + warp_m, warp_n};
        warp_tile_iterator_.add_tile_offset(warp_offset);
    }

    CUTLASS_DEVICE
    void operator()(OutputTileIterator destination_iterator, const Array<float, 64> accumulators) {
        FragmentIterator accum_fragment_iterator(accumulators);
        #pragma unroll(8)
        for (int iter = 0; iter < 8; ++iter) {
            __syncthreads();
            acc2smem_source_not_needed(iter, accum_fragment_iterator, warp_tile_iterator_);
            __syncthreads();
            Array<float, 8> aligned_accum_fragment;
            shared_load_iterator_.load(aligned_accum_fragment);
            // for(int i=0;i<8;i++)if(aligned_accum_fragment.storage[i]!=1024.0)printf("%.2f ", aligned_accum_fragment.storage[i]);

            // Array<float, 8> output_fragment;
            // output_fragment = aligned_accum_fragment; // linear combination for alpha = 1, beta = 0
            // destination_iterator.store(output_fragment);
            destination_iterator.store(aligned_accum_fragment);
            destination_iterator.increment();
        }
    }
};

class GemmKernel {
public:
    union SharedStorage {
        typename Mma::SharedStorage main_loop;
        typename Epilogue::SharedStorage epilogue;
    };
};

__global__ 
void kernel(float * A, float * B, float * C) { // C = A * B
    extern __shared__ int SharedStorageBase[];
    typename GemmKernel::SharedStorage *shared_storage_ptr = reinterpret_cast<typename GemmKernel::SharedStorage *>(SharedStorageBase);
    typename GemmKernel::SharedStorage &shared_storage = *shared_storage_ptr;

    IntPair threadblock_tile_offset = {int(blockIdx.x / 8), int(blockIdx.x % 8)};
    IntPair threadblock_offset = {threadblock_tile_offset.x * 128, threadblock_tile_offset.y * 128};
    int thread_idx = threadIdx.x;
    IntPair tb_offset_A = {threadblock_offset.x, 0};
    IntPair tb_offset_B = {0, threadblock_offset.y};
    GlobalMemoryIteratorA iterator_A(A, thread_idx, tb_offset_A);
    GlobalMemoryIteratorB iterator_B(B, thread_idx, tb_offset_B);
// if(blockIdx.x == 0) printf("%d %d %d\n", int(blockIdx.x), int(threadIdx.x), int(reinterpret_cast<float*>(iterator_A.get()) - A));
    int warp_idx = __shfl_sync(0xffffffff, threadIdx.x / 32, 0);
    int lane_idx = threadIdx.x % 32;
    Mma mma(shared_storage.main_loop, thread_idx, warp_idx, lane_idx);
    Array<float, 64> accumulators;
    accumulators.clear();
    int gemm_k_iterations = 128;
    mma(gemm_k_iterations, accumulators, iterator_A, iterator_B, accumulators);
    // accumulators.print();

    OutputTileIterator iterator_C(C, thread_idx, warp_idx, lane_idx, threadblock_offset);
    Epilogue epilogue(shared_storage.epilogue, thread_idx, warp_idx, lane_idx);
    epilogue(iterator_C, accumulators);
}

void run_cutlassMultiStage(int M, int N, int K, float * A, float * B, float * C, float alpha, float beta) {
    dim3 grid(64, 1, 1), block(256, 1, 1);
    int smem_size = int(sizeof(typename GemmKernel::SharedStorage));
    kernel<<<grid, block, smem_size, nullptr>>>(A, B, C);
}

using SharedStorage = typename GemmKernel::SharedStorage;

// class CUDAMatrix {
// private:
//     float *mat, *dev_mat;
//     int length;
//     size_t size;

// public:
//     CUDAMatrix(int l) : length(l), size(sizeof(float) * l * l) {
//         mat = (float *) malloc(size);
//         cudaMalloc((void **) &dev_mat, size);
//     }

//     ~CUDAMatrix() {
//         free(mat);
//         cudaFree(dev_mat);
//     }

//     float *devPtr() {
//         return dev_mat;
//     }

//     void cpyToDevice() {
//         cudaMemcpy(dev_mat, mat, size, cudaMemcpyHostToDevice);
//     }

//     void cpyToHost() {
//         cudaMemcpy(mat, dev_mat, size, cudaMemcpyDeviceToHost);
//     }

//     float &at(int i, int j) {
//         return mat[i * length + j];
//     }

//     const float &at(int i, int j) const {
//         return mat[i * length + j];
//     }

//     void print() {
//         for (int i = 0; i < length; i++) {
//             for (int j = 0; j < length; j++) {
//                 printf("%.2f ", mat[i * length + j]);
//             }
//             printf("\n");
//         }
//     }
// };

// void test() {
//     CUDAMatrix A(1024), B(1024), C(1024);
//     for (int i = 0; i < 1024; i++) {
//         for (int j = 0; j < 1024; j++) {
//             A.at(i, j) = j == 0 ? 1 : 0;
//             B.at(i, j) = i == 0 ? 1 : 0;
//             C.at(i, j) = 3;
//         }
//     }
//     A.cpyToDevice(), B.cpyToDevice();
//     dim3 grid(64, 1, 1), block(256, 1, 1);
//     int smem_size = int(sizeof(typename GemmKernel::SharedStorage));
//     kernel<<<grid, block, smem_size, nullptr>>>(A.devPtr(), B.devPtr(), C.devPtr());
//     auto err = cudaGetLastError();
//     if (err != cudaSuccess) printf("CUDA Error: %s\n", cudaGetErrorString(err));
//     C.cpyToHost();
//     C.print();
// }

// float equal(float a, float b) { return abs(a - b) < 0.001; }

// void correctnessTest(int round = 100) {
//     static const int l = 1024;
//     CUDAMatrix A(l), B(l), C(l), ans(l);
//     int cur = round;
//     while (cur--) {
//         fprintf(stderr, "Round %d\n", round - cur);
//         for (int i = 0; i < l; i++) {
//             for (int j = 0; j < l; j++) {
//                 // A.at(i, j) = i <= j ? rand() : A.at(j, i);
//                 // B.at(i, j) = i <= j ? rand() : B.at(j, i);
//                 A.at(i, j) = rand();
//                 B.at(i, j) = rand();
//                 ans.at(i, j) = 0;
//             }
//         }
//         A.cpyToDevice(), B.cpyToDevice();
//         dim3 grid(64, 1, 1), block(256, 1, 1);
//         int smem_size = int(sizeof(typename GemmKernel::SharedStorage));
//         kernel<<<grid, block, smem_size, nullptr>>>(A.devPtr(), B.devPtr(), C.devPtr());
//         auto err = cudaGetLastError();
//         if (err != cudaSuccess) printf("CUDA Error: %s\n", cudaGetErrorString(err));
//         C.cpyToHost();
//         for (int i = 0; i < l; i++)
//             for (int j = 0; j < l; j++)
//                 for (int k = 0; k < l; k++)
//                     ans.at(i, j) += A.at(k, i) * B.at(k, j); // A: ColumnMajor, B: RowMajor
//         for (int i = 0; i < l; i++)
//             for (int j = 0; j < l; j++)
//                 if (!equal(ans.at(i, j), C.at(i, j)))
//                     return fprintf(stderr, "Error with %.2f at (%d, %d)\n", abs(ans.at(i, j) - C.at(i, j)), i, j),
//                         printf("\n\nA:\n\n"), A.print(),
//                         printf("\n\nB:\n\n"), B.print(),
//                         printf("\n\nC:\n\n"), C.print(),
//                         printf("\n\nans:\n\n"), ans.print(),
//                         void();
//     }
// }

// int main() {
//     // test();
//     correctnessTest();
//     return 0;
// }
