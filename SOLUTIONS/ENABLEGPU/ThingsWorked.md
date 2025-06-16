if not working:
================

your pytorch may not be cuda supported uninstall pytorch

    pip uninstall torch torchvision torchaudio -y


**Install PyTorch with CUDA 12.4 (since your `nvcc` is 12.4):**  
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```
🔹 If you later upgrade CUDA to **12.8**, install PyTorch with:  
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
```
    
