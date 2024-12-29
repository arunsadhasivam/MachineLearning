Model Paralleism:
=================

![image](https://github.com/user-attachments/assets/5142cf0d-890d-4233-b4e4-1d96bbe03707)


  - in this lesson, we will understand model paralleism and its significance when training llm.
    As we have seen earlier in the data paralleism model, each gpu stores the entire model
    replica, and each gpu have limited storage capacity. As the size of the model goes on
    increasing or the size of the model that we are planning to train becomes sufficiently
    large, a single gpu **cannot fit all the parameters of the model** in it.


  - thats exactly model paralleism comes in .model paralleism split the model layers across multiple gpu like below
![image](https://github.com/user-attachments/assets/501eab22-0e25-4122-8b89-d0c011b149bb)

  - here above is illustration showing 8 layer model, using model paralleism we slice in to 2 shard placing
    layer(0-3) on gpu0 and layer(4-7) on gpu1 . in this we can distribute the large model across multiple
    gpu and train and this reduces the memory requirements during the training process.
  - each gpu only need to have memory capacity for only 4 layers instead of 8 layers.

Deep process:
============

1.Forward propagation:
======================

![image](https://github.com/user-attachments/assets/cd7b1bb4-ac52-4671-b644-e92d9cfebc92)
![image](https://github.com/user-attachments/assets/82866f3d-0213-4bec-a22d-d2df5772392f)

  - during the model training process,in the forward pass the data travels from layer 0-1,1-2,2-3
    just like any other forward pass.
  - but when the output need to go from layer 3 to layer4 it needs to travel from gpu 0 to gpu1
    ,this introduces communication overhead. if the participating gpu or these 2 gpu if they are in
    same computing node or same physical machine  then this copying is pretty fast.
   - but if the 2 gpu are located on 2 different machines  i.e multi machine setup or multi-node
     setup then the computational overhead could be significantly larger.
   - Now the output from layer 3 is copied from gpu0 to the gpu-1 and then the forward process progress
     from layer4 to layer5 to layer6 ... layer n as any other forward pass. this completes the forward
     pass.
     
2.backward Propagation:
=======================     

![image](https://github.com/user-attachments/assets/fc7f0f49-5ce4-4715-bc27-c249a722d223)

    - backward propagation happens in the reverse manner.


Summary:
========

![image](https://github.com/user-attachments/assets/d88d06cd-e687-4eb2-8eff-acc955f84824)


  - in a nutshell , device0 carries the forward pass f0 and device1 carries the forward pass f1
    after this loss is computed and then backpropagation starts.
  - first back pass B1 happens on device1 and then backward pass B0 happens on device0.
  - this completes the entire forward and backward pass in model paralleism.


Cons:
=====

![image](https://github.com/user-attachments/assets/e32fc074-7f77-4a70-8c14-4a8a6df97fb4)

  - The problem with model paralleism is that , any point in time , **only one gpu is Active
    and the rest of the gpu is idle**. This happens because there is a dependency between
    the output of the devices.
  - if there is 4 gpu -> at any point in time only one gpu is active and rest 3 gpu is idle.
    this results in very inefficient use of hardware resources which is very costly.
