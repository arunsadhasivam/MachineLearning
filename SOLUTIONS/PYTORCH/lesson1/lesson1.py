import torch
import torch.cuda
import numpy as np


a = torch.tensor([[2,2]])
#print(a.device)

cpu_tensor = torch.rand(2)
#print(cpu_tensor.device)

if torch.cuda.is_available():
    gpu_tensor = cpu_tensor.to("cuda")
    #print('gpu',gpu_tensor.device)
    back = gpu_tensor.to('cpu')
#print('back',back.device)


a= torch.tensor([[1,2],[3,4]])
#print(a)
b = torch.tensor([[1,2],[3,4]])
#print(a.add_(b))
print(b.view(-1))

def  tensor_multiple(cuda_enabled):
    start = 0
    end = 0
    if torch.cuda.is_available():
        start= torch.cuda.Event(enable_timing=True)
        start.record()
    a = torch.tensor([[1,2],[1,3],[1,4]])
    b = torch.tensor([[1,2],[1,3],[1,4]])
    if(cuda_enabled) :
        #make sure check whether cuda available else
        #Torch not compiled with CUDA enabled error throw
        a = a.to("cuda")
        b = b.to("cuda")
        #print('gpu activated...')

    if torch.cuda.is_available():
        end= torch.cuda.Event(enable_timing=True)
        end.record()
    c = a+b

    if torch.cuda.is_available():
        torch.cuda.synchronize()
        #print(c , start.elapsed_time(end))
        return start.elapsed_time(end)
    else:
          #print(c)
          return end-start

isCudaAvail = False
if torch.cuda.is_available():
    isCudaAvail = True
cpu =tensor_multiple(isCudaAvail)
#print('cpu=',cpu)#0.3
gpu = tensor_multiple(False)

#print("gpu=",gpu)#0.055
# assign values from numpy


#since call by reference both value changed




def  reference_check() -> None:
    print('-----both in cpu since numpy only run in cpu ---')
    a = np.ones(3)
    b =  a
    #b = b.to("cuda")
    a+=1
    print("a=",a) #[2,2,2]
    print("b=", b)#[2,2,2]



 
def  reference_check_torch() -> None:
    print('-----one variable in cpu and another in torch no CUDA----')
    a = np.ones(3)
    b = torch.from_numpy(a)
    #b = b.to("cuda")
    a+=1
    print("torch a=",a) #[2,2,2]
    print("b=", b)#[2,2,2]

# one in cuda and another in cpu
def  reference_check_difference_device() -> None:
    print('-----one variable in cpu and another in GPU----')
    a = np.ones(3)
    b = torch.from_numpy(a)
    b = b.to("cuda")
    a+=1
    print("cpu a=",a) #[2,2,2]
    print("cuda b=", b)#[1,1,1] see reference not copying if one in gpu another in cpu    
reference_check_torch()
reference_check()
reference_check_difference_device()
