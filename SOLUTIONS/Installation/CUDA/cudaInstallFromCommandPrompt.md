Cuda Installation:
=====================

(base) C:\Arun\Anaconda\envs\CUDA_GPU_HOME>conda install cuda -c nvidia/label/cuda-12.2
Retrieving notices: done
Channels:
 - nvidia/label/cuda-12.2
 - defaults
 - nvidia
 - pytorch-nightly
Platform: win-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Arun\Anaconda

  added / updated specs:
    - cuda


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    cuda-12.1.0                |                0           1 KB  nvidia
    cuda-command-line-tools-12.1.1|                0           2 KB  nvidia
    cuda-compiler-12.4.1       |       hd77b12b_1          19 KB
    cuda-cuobjdump-12.4.127    |                0         4.0 MB  nvidia
    cuda-cuxxfilt-12.4.127     |                0         164 KB  nvidia
    cuda-demo-suite-12.4.127   |                0         4.7 MB  nvidia
    cuda-documentation-12.4.127|                0          89 KB  nvidia
    cuda-nsight-compute-12.4.1 |                0           2 KB  nvidia
    cuda-nvcc-12.4.131         |                0        59.2 MB  nvidia
    cuda-nvdisasm-12.8.55      |                0         5.0 MB  nvidia
    cuda-nvml-dev-12.8.55      |                0         103 KB  nvidia
    cuda-nvprof-12.8.57        |                0         1.3 MB  nvidia
    cuda-nvprune-12.4.127      |                0         151 KB  nvidia
    cuda-nvvp-12.8.57          |                0       108.5 MB  nvidia
    cuda-sanitizer-api-12.8.55 |                0         6.7 MB  nvidia
    cuda-toolkit-12.1.0        |                0           1 KB  nvidia
    cuda-tools-12.1.0          |                0           1 KB  nvidia
    cuda-visual-tools-12.1.0   |                0           1 KB  nvidia
    fontconfig-2.14.1          |       hb33846d_3         224 KB
    libglib-2.78.4             |       ha17d25a_0         1.3 MB
    libnvvm-samples-12.1.105   |                0          32 KB  nvidia
    nsight-compute-2025.1.0.14 |                0       262.1 MB  nvidia
    vs2017_win-64-19.16.27032.1|       hb4161e2_3         198 KB
    vswhere-2.8.4              |       haa95532_0         210 KB
    ------------------------------------------------------------
                                           Total:       454.0 MB

The following NEW packages will be INSTALLED:

  cuda               nvidia/win-64::cuda-12.1.0-0
  cuda-command-line~ nvidia/win-64::cuda-command-line-tools-12.1.1-0
  cuda-compiler      pkgs/main/win-64::cuda-compiler-12.4.1-hd77b12b_1
  cuda-cuobjdump     nvidia/win-64::cuda-cuobjdump-12.4.127-0
  cuda-cuxxfilt      nvidia/win-64::cuda-cuxxfilt-12.4.127-0
  cuda-demo-suite    nvidia/win-64::cuda-demo-suite-12.4.127-0
  cuda-documentation nvidia/win-64::cuda-documentation-12.4.127-0
  cuda-nsight-compu~ nvidia/win-64::cuda-nsight-compute-12.4.1-0
  cuda-nvcc          nvidia/win-64::cuda-nvcc-12.4.131-0
  cuda-nvdisasm      nvidia/win-64::cuda-nvdisasm-12.8.55-0
  cuda-nvml-dev      nvidia/win-64::cuda-nvml-dev-12.8.55-0
  cuda-nvprof        nvidia/win-64::cuda-nvprof-12.8.57-0
  cuda-nvprune       nvidia/win-64::cuda-nvprune-12.4.127-0
  cuda-nvvp          nvidia/win-64::cuda-nvvp-12.8.57-0
  cuda-sanitizer-api nvidia/win-64::cuda-sanitizer-api-12.8.55-0
  cuda-toolkit       nvidia/win-64::cuda-toolkit-12.1.0-0
  cuda-tools         nvidia/win-64::cuda-tools-12.1.0-0
  cuda-visual-tools  nvidia/win-64::cuda-visual-tools-12.1.0-0
  fontconfig         pkgs/main/win-64::fontconfig-2.14.1-hb33846d_3
  libglib            pkgs/main/win-64::libglib-2.78.4-ha17d25a_0
  libnvvm-samples    nvidia/win-64::libnvvm-samples-12.1.105-0
  nsight-compute     nvidia/win-64::nsight-compute-2025.1.0.14-0
  vs2017_win-64      pkgs/main/win-64::vs2017_win-64-19.16.27032.1-hb4161e2_3
  vswhere            pkgs/main/win-64::vswhere-2.8.4-haa95532_0


Proceed ([y]/n)? y


Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
