# TVMGemmAsync

Evaluated under [apache tvm](https://github.com/apache/tvm).

## File Structure

```
📦 TVMGemmAsync
 ┣ 📂 nn
 ┃ ┃ ┣ 📜 *Generate.py         # template-based tune
 ┃ ┃ ┣ 📜 callCutlass.cu       # benchmark script for cutlass in cuda
 ┃ ┃ ┣ 📜 speedTest.cu         # benchmark for generated kernel
 ┃ ┃ ┣ 📜 cutlass_profiler.py  # profiler of cutlass
 ┃ ┃ ┣ 📜 perf.py              # call all benchmark script
 ┃ ┃ ┣ 📜 tune.py              # issue one tune task
 ┃ ┃ ┗ 📜 run.py               # sequentially run multiple tune task
 ┗ 📂 nt
   ┗ same with nn
```

## Usage

For convenience, users could only run `perf.py`, `tune.py`, `tun.py`, and `cutlass_profiler.py` manually.

All these files support a format to specify command line argument (written in regular expression):

```
python3 *.py (([M|N|K|t|O]+)=([0-9]+))*
```

M, N, and K stand for Gemm problem size, t for max tuning trials, and O for option (used only in `tune.py`).

for example:

```
// if M == 1024 N == 2048 K == 3072
python3 *.py M=1024 N=2048 K=3072
// if M == N == 1024, K == 2048, t == 5000
python3 *.py MN=1024 K=2048 t=5000
// if M == N == K == 7384, t == 2398, O == 65536
python3 *.py MNK=7384 t=2398 O=65536
```

To profile a Gemm task, follow these steps:

0) `cd nt/nn` based on the layout you choose
1) specify `cutlass_build_path` in `cutlass_profiler.py`
2) run `cutlass_profiler.py` with M, N, and K in the format mentioned before

2. find `f'{result_path}/M={m}_N={N}_K={K}/best_perf.txt'` for cutlass best performance kernel
3. open `callCutlass.cu`, change three lines that marked `MOFITY THIS LINE` with cutlass best performance kernel argument
4. run `tune.py` with M, N, K,  `O == 0` or `O == 65536`  and whatever `t` to get a template-based tuning kernel
    * `O == 0`: using `nohup` command, running in the background
    * `O == 65536`: not using `nohup` command
5. run `tune.py` with M, N, K, `O == 1` or `O == 65537`  and whatever `t` to get Apache TVM tuning kernel
    * `O == 1`: using `nohup` command, running in the background
    * `O == 65537`: not using `nohup` command
6. run `perf.py` with M, N, and K to get the final result

All output path is configurable in the corresponding python script.

By using `run.py`, it will sequentially tune all tune tasks using `&&` in the Linux shell and `O == 65536/65537`.

