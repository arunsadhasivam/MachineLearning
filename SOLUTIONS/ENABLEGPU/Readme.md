Step 1:
=========

check nvidia smi

![image](https://github.com/user-attachments/assets/20d37e4e-c9bb-486f-a587-46f1a52d33d0)


  go to NVIDIA Control Panel > 
![image](https://github.com/user-attachments/assets/f41d0a78-2fe5-4834-aa58-2216042c4517)


![image](https://github.com/user-attachments/assets/1d60242f-28bc-48d0-ad5b-6af5468bebc9)

change cpu to ada gpu

![image](https://github.com/user-attachments/assets/2a1b5f1d-6096-44af-ae24-0165afd5749a)

 ![image](https://github.com/user-attachments/assets/278d5c11-ba73-4094-8a5f-c08f9cf2b249)
![image](https://github.com/user-attachments/assets/f5d45f34-782b-4e35-b120-ef70608ba1ea)



After restart it works!!!
==========================


![image](https://github.com/user-attachments/assets/21a00a83-3464-49ca-9703-12865308fee0)


Steps to debug:
================


Step 1: 
=======

uninstall pytorch it should be gpu pytorch not cpu pytorch
    
    pip uninstall torch torchvision torchaudio -y


Step 2:
========

install torch cuda support cu124(cuda version 12.4)

**Install PyTorch with CUDA 12.4 (since your `nvcc` is 12.4):**  
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```
🔹 If you later upgrade CUDA to **12.8**, install PyTorch with:  
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
```

Step3:
=======

restart once the vscode or system if not working.

    
    
