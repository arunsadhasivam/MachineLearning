Fully Sharded Data Parellelism/ZeRO 3:
=======================================


![image](https://github.com/user-attachments/assets/a335d47c-988d-49c0-b913-7c12ac479d39)


    - in this lesson, we look at the sharded data paralleism.


<p><details><summary>Recap of Model and pipeline Paralleism:</summary>
Recap of Model and pipeline Paralleism:
=========================================


1.Model pipeline:
==================

    - Recap: in dataparalleism , each gpu contains the entire model replica.
      whereas the data is shared across the gpu . on each gpu the forward pass
      and backward gpu happen on the respective sub-batch.
     - posted the local gradient or average via all reduced operation to get the global gradients.
     - now the global gradients are used to update the weights. 
     - challenge with data pipeline is it maintains a copy entire model on each gpu.
       making it very memory in-efficient . this is what tackle in pipeline paralleism.

![image](https://github.com/user-attachments/assets/a286bd02-130a-4a1c-9359-bf2a1ac709ce)
    

2.Pipeline Paralleism:
======================

![image](https://github.com/user-attachments/assets/b702efc0-4c49-4817-8485-7cdbb8c3ebd8)

     
      - here in this pipeline paralleism, model is shared across multiple gpu or multiple devices
      -  pipeline paralleism has few limiations
         1) communication overhead
         2) under utilization of gpu.
       - can we have paralleism techniques that can reduce the memory requirements and quite also
         reduce the under utilization thats where FSDP(Full sharded data paralleism) comes in 

3.Fully Sharded Data Pipelism:
==============================

![image](https://github.com/user-attachments/assets/3ca8c646-1211-4670-a984-333e5ffbd997)

How fsdp works:
===================
  -  main idea is to shard the optimizer states also knows as zero redundancy state to
     shard the gardients which is knows as zero-stage-ii and the model parameters which is
     known as zero-stage-iii across the data parallel workers i.e across gpu.
  - during the forward pass, each gpu gets the sub-batch of data. 

![image](https://github.com/user-attachments/assets/bb691f01-76ae-4bea-ba6a-163b50442f30)



  - each gpu first perform the all-gather operation to gather the weights that are required to perform the
    forward pass and then the forward pass for the sharded model happens. this happens for all the 
    sharded layers.
  - post the forward pass , the loss is calcualted .
    
  ![image](https://github.com/user-attachments/assets/4fc4ad7b-c358-4a2d-83f0-faa47d40f127)

  - during the backward pass again each gpu performs an all-gather operation to gather the required weights from
    the local model shards. post then backward pass happens to get the local gradients.
  - After getting the local gradient, a **reduce scatter operation** is performed i.e the local gradients are
    averaged and then sharded across the gpu.
  - so that each gpu have the gradient to update the weights of the local shards. thas how fsdp is able to
    perform model sharding and at the same time it is able to perform data paralleism.
  - in this way it becomes memory efficient because each gpu has only a local shard instead of the whole
     model replica. same time there is no gpu underutilization. because each gpu is working all the time
    to process its own sub batch.
  - Therefore the FSDP is both memory efficient and compute efficient.
  

Pros:
=====

![image](https://github.com/user-attachments/assets/c5e3d5ed-db3b-4604-865f-9afb60832f5f)


</details></p>
