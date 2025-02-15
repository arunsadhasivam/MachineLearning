install torch:
===================


    pip install torch==2.2.1 torchvision==0.17.1 torchaudio==2.2.1 --extra-index-url https://download.pytorch.org/whl/cu121


 If that doesn't work, try:
 ==========================
 
   pip install torch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 --extra-index-url https://download.pytorch.org/whl/cu121

if you're still getting errors, try these fixes:
================================================

Upgrade pip:
=============

   python -m pip install --upgrade pip

Install from wheel files directly:
===================================


  Go to https://download.pytorch.org/whl/torch_stable.html
  Find the appropriate wheel file for your:
  
  Python version (e.g., cp39 for Python 3.9)
  Windows version (win_amd64)
  CUDA version (cu121 for CUDA 12.1)
