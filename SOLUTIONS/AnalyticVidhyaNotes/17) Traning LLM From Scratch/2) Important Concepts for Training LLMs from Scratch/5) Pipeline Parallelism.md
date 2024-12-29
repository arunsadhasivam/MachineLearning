![image](https://github.com/user-attachments/assets/beb42721-094c-49c4-9dcb-2f1f3fa774d5)Pipeline Parallelism:
======================



Model paralleism:
===================

![image](https://github.com/user-attachments/assets/6c55edbd-2899-467a-a99b-752d1f287101)

  - Model paralleism is the single gpu idling time. where in , at any point in time only one gpu
    is active, whereas other gpu is in idle state . thats when pipeline paralleism comes in.

Pipeline paralleism:
====================

![image](https://github.com/user-attachments/assets/4d9250be-df20-4134-b64c-5ca657a5634d)

  - Pipeline paralleism is identicle to **model paralleism** but it solves the gpu idling problem.
    it does so by chunking the incoming batches in to micro batches and artifically create a pipeline
    which allows different gpu to concurrently participate in the computation process. here below
    there is a illustrate from g5 paper, which showcase pipeline paralleism of degree4 since
    4 gpu are participating in the pipeline.
  - At the top the naive model paralleism strategy leads to severe underrated due to
    sequential nature of the network.
  - here at any point in time , only one device is active while all the other devices are in idle state
    on the bottom  , pipeline paralleism divides the input batches in to micro batches enabling
    different devices i.e (there is different gpu) to work on separate micro batches in parallel
    or concurrently.

    ![image](https://github.com/user-attachments/assets/779ec3fe-cf04-4bc2-b054-e26cbf5ee4a8)

  - lets deep dive this in detail.consider that we have access to 4 gpus , the data that is a given
    batch is divided in to 4 microbatches , let say f0, f1,f2 and f3 .
      1) at step 1 the first batch f0  is sent to gpu0.
      2) at step2 f0 from gpu0 is moved to gpu-1 
      3) gpu0 is provided with next microbath f1
      4) now both the gpu are processing different micro batches in parallel.
      5) step 3 f0 moves from gpu1 to gpu-2 , f1 moves from gpu-0 to gpu-1 and gpu0
         is fed the next microbatch f0.
         ![image](https://github.com/user-attachments/assets/c567684c-639d-4490-8457-7b5a67e85e9a)

      7) now all the 3 gpu are processing the different microbatches in parallel .

![image](https://github.com/user-attachments/assets/19e0f772-5593-442e-811a-ef8bea527851)

      8) at step4
         1)f0 moves from gpu-2 to gpu-3
         2)f1 moves from gpu1 to gpu2 ,
         3)f2 moves from gpu0 to gpu1 and
         4)gpu0 is fed the next microbatch f3. 

![image](https://github.com/user-attachments/assets/a43a0cbe-62d3-49e0-829f-aca3915fc06d)

      9) now all the 4 gpu's are processing different microbatches and this process continues so on.
![image](https://github.com/user-attachments/assets/a8572b4b-2e16-4beb-812d-f4d52840f873)

Forward Propagation:
=====================
      ![image](https://github.com/user-attachments/assets/0c45b1a6-55f9-4120-ab48-8bedd3202023)

   - finally end of the forward pass we have the output of different microbatches at the gpu3.

Backward propagation:
======================

![image](https://github.com/user-attachments/assets/511ffd38-1255-414d-8e78-b82992cd3e16)

   - Now the backward propagation takes places across different gpu in parallel similar to way did in forward pass.

Gradient:
=========

   - gradient are computed and the weights of the model are updated via optimizer step.
![image](https://github.com/user-attachments/assets/7cb471ec-90ab-4253-a507-bfa082f1135a)

Pros:
=====

   - here  is the illustration from g5 paper where researchers compare the modelparalleism vs pipeline paralleism.
   - the baseline naive(2) is the performance of the **need to partition approach** where the model is split in to
     2 partition without the pipeline. the pipeline(k) refers to the performance of the pipeline paralleism that
     split the model into k partitions with k dividers.
   - As you can see the **pipeline paralleism increase the speedup  as the no of devices increases**.
     
  Cons:
  =====

    - here the communication overhead in moving data from one gpu to another.
    - under utilization of gpu, while pipeline paralleism solves the gpu idling problem compare to
      model paralleism, but it does not so completely. it keep the gpu active 50 - 60% of the
      time . whereas the rest of the time , some idle state  going on.

      ![image](https://github.com/user-attachments/assets/df549f2c-e7b7-41b7-ac8e-aeef9bb253c2)
