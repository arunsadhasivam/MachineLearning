Step 1:
=======


NOTE:
=====

use 3.10 only if python 3.11 is not working

    conda create --name pytorch_cuda python=3.10 -y
    conda activate pytorch_cuda
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

![image](https://github.com/user-attachments/assets/af868a9d-3e50-4887-afa4-1a473f7bcb55)


GPU Kernel
============

![image](https://github.com/user-attachments/assets/dd2cff82-c53e-4bae-96d8-2c303aff6a56)

CPU Kernel
==========

![image](https://github.com/user-attachments/assets/def6c238-d298-4f5d-bff5-4e83abf6b9f2)

![image](https://github.com/user-attachments/assets/65847ac5-641d-4e34-815f-f0ef84117a64)
![image](https://github.com/user-attachments/assets/84e31414-0e8c-40e8-8bc8-058eaa4ded77)


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

![image](https://github.com/user-attachments/assets/bb7a47c7-43cf-499e-82d8-1a7dd012da16)

 


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

![image](https://github.com/user-attachments/assets/11404b23-4bf5-4737-9021-26cfa68491f3)



![image](https://github.com/user-attachments/assets/99ac192f-854c-4d37-b2cc-9e14ca53b99b)

