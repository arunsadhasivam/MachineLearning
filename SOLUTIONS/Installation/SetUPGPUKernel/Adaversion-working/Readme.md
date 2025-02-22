Step 1:
=======

conda create --name pytorch_cuda python=3.10 -y
conda activate pytorch_cuda
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124


Step 2:
========

nvcc --version

![image](https://github.com/user-attachments/assets/3c236a34-147a-47dc-af95-50f6163012e8)


if i use python 3.11

![image](https://github.com/user-attachments/assets/8867af14-0852-45ad-99ab-ae51f08f7008)


