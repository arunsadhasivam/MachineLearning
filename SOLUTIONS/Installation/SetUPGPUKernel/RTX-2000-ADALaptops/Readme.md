Step 1:
=======




    conda create --name pytorch_cuda python=3.10 -y
    conda activate pytorch_cuda
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

![image](https://github.com/user-attachments/assets/af868a9d-3e50-4887-afa4-1a473f7bcb55)


NOTE:
=====

Even though you have in environment variable python 3.11 and installed 3.11 you can set 
your kernel **pytorch_cuda** to use python 3.10

![image](https://github.com/user-attachments/assets/bb178c05-16d6-44e6-811e-719d55cc6d40)


Step 2:
========

nvcc --version

![image](https://github.com/user-attachments/assets/3c236a34-147a-47dc-af95-50f6163012e8)


if i use python 3.11
======================

![image](https://github.com/user-attachments/assets/8867af14-0852-45ad-99ab-ae51f08f7008)


step 3:
========


 ![image](https://github.com/user-attachments/assets/3abaa284-7a01-4bac-a98d-cd9ff78e18c2)
![image](https://github.com/user-attachments/assets/36cc64c0-65c4-4092-a081-b0b5c63d3fac)


Using Python instead of conda:
==============================

Step 1:
========

        C:\Arun\PythonEnv>python -m venv PYTHON_CUDA_GPU_HOME
        
        C:\Arun\PythonEnv>cd PYTHON_CUDA_GPU_HOME
        
        C:\Arun\PythonEnv\PYTHON_CUDA_GPU_HOME>cd Scripts
        
        C:\Arun\PythonEnv\PYTHON_CUDA_GPU_HOME\Scripts>activate
        
        (PYTHON_CUDA_GPU_HOME) C:\Arun\PythonEnv\PYTHON_CUDA_GPU_HOME\Scripts>
            pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124





