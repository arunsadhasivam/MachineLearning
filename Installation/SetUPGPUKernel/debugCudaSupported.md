To check cuda is working 
==========================

Step1:
======
check nvidia driver whether enabled for developer to access cuda


![image](https://github.com/user-attachments/assets/ac8012e9-24f0-4fc1-8711-89db8e280541)


Step2:Check the nvidia gpu
===========================


![image](https://github.com/user-attachments/assets/fd57e99d-42d0-4bd3-ac40-513ffbf24072)


Check initially in default kernal python (C:\Arun\Python\Python310)

if kernal created in different folder c:\Arun\Workspace sometimes wont work.

import torch

print("CUDA Available:", torch.cuda.is_available())
print("Number of GPUs:", torch.cuda.device_count())
if torch.cuda.is_available():
    print("GPU Name:", torch.cuda.get_device_name(0))

![image](https://github.com/user-attachments/assets/05c6a0d0-74dd-47e9-bb4c-5b4e9dbd1468)
