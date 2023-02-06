class Shape:

    def __init__(self, m, n, k):
        self.mm = m
        self.nn = n
        self.kk = k

    def m(self):
        return self.mm

    def n(self):
        return self.nn

    def k(self):
        return self.kk


ThreadblockShape = Shape(64, 128, 8)
WarpShape = Shape(32, 64, 8)
WarpSize = 32
WarpNumThreads = Shape(4, 8, -1)
ThreadTile = Shape(WarpShape.m() // WarpNumThreads.m(), WarpShape.n() // WarpNumThreads.n(), -1)
LaneLayout = 2 if (WarpShape.m() // WarpNumThreads.m() > 4 and WarpShape.n() // WarpNumThreads.n() > 4) else 1
LaneMmaShape = Shape(min(ThreadTile.m(), 4), min(ThreadTile.n(), 4), -1)
ThreadNumShape = Shape(ThreadblockShape.m() // WarpShape.m() * WarpNumThreads.m(), ThreadblockShape.n() // WarpShape.n() * WarpNumThreads.n(), -1)

print(f"""sch.transform_layout(block=A_smem2local, buffer=("read", 0), index_map=lambda i, j: (i, 
    (j // {ThreadblockShape.m()}) * {ThreadblockShape.m()} + # threadblock_offset
    ((j % {ThreadblockShape.m()}) // {WarpShape.m()}) * {WarpShape.m()} +  # warp_idx % 4
    ((j % {WarpShape.m()}) // {(WarpShape.m() // (WarpNumThreads.m() // LaneLayout))}) * {(LaneMmaShape.m() * LaneLayout)} + # lane_idx // 16
    ((j % {(WarpShape.m() // (WarpNumThreads.m() // LaneLayout))}) // {(WarpShape.m() // (WarpNumThreads.m() // LaneLayout) // LaneLayout)}) * {LaneMmaShape.m()} + # lane_idx % 2
    ((j % {(WarpShape.m() // (WarpNumThreads.m() // LaneLayout) // LaneLayout)}) // {LaneMmaShape.m()}) * {(WarpNumThreads.m() * LaneMmaShape.m())} + (j % {(WarpShape.m() // (WarpNumThreads.m() // LaneLayout) // LaneLayout)}) % {LaneMmaShape.m()} # warp_mma_m
))""")

print(f"""sch.transform_layout(block=B_smem2local, buffer=("read", 0), index_map=lambda i, j: (i, 
    (j // {ThreadblockShape.n()}) * {ThreadblockShape.n()} + # threadblock_offset
    ((j % {ThreadblockShape.n()}) // {WarpShape.n()}) * {WarpShape.n()} + # warp_idx // 4
    ((j % {WarpShape.n()}) // {(WarpShape.n() // WarpNumThreads.n())}) * {LaneMmaShape.n()} + # (lane_idx % 16) // 2
    ((j % {(WarpShape.n() // WarpNumThreads.n())}) // {LaneMmaShape.n()}) * {(ThreadTile.n() * LaneMmaShape.n())} + ((j % {(WarpShape.n() // WarpNumThreads.n())}) % {LaneMmaShape.n()}) # temp_warp_mma_n
))""")