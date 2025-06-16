if not working:
================

your pytorch may not be cuda supported uninstall pytorch

    pip uninstall torch torchvision torchaudio -y

it worked after uninstall pytorch and install below 12.4 version.

(PYTHON_CUDA_GPU_HOME) C:\WorkSpace\RAG>pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

        Installing collected packages: sympy, torch, torchvision, torchaudio
          Attempting uninstall: sympy
            Found existing installation: sympy 1.12.1
            Uninstalling sympy-1.12.1:
              Successfully uninstalled sympy-1.12.1
        Successfully installed sympy-1.13.1 torch-2.6.0+cu124 torchaudio-2.6.0+cu124 torchvision-0.21.0+cu124


Tested:
========

    (PYTHON_CUDA_GPU_HOME) C:\WorkSpace\RAG>python Assignment.py
    GPU detected: NVIDIA RTX 2000 Ada Generation Laptop GPU
    
    --- CPU Test ---
    Running on: cpu
    Matrix multiplication time: 0.4297 seconds
    
    --- GPU Test ---
    Running on: cuda
    Matrix multiplication time: 0.2048 seconds
    
    GPU is 2.10x faster than CPU
    



**Install PyTorch with CUDA 12.4 (since your `nvcc` is 12.4):**  
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```
🔹 If you later upgrade CUDA to **12.8**, install PyTorch with:  
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
```
    
