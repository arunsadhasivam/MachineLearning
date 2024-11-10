To check cuda is working 
==========================


import torch

print("CUDA Available:", torch.cuda.is_available())
print("Number of GPUs:", torch.cuda.device_count())
if torch.cuda.is_available():
    print("GPU Name:", torch.cuda.get_device_name(0))

![image](https://github.com/user-attachments/assets/05c6a0d0-74dd-47e9-bb4c-5b4e9dbd1468)
