Parallel and Distributed paradigm:
==================================


![image](https://github.com/user-attachments/assets/f40e3dbd-8894-4214-bded-a13ac2ef09cd)


  - As seen earlier llm contains huge no of parameters, they are training on massive datasets.
  - as a result , they need massive computing power, in terms of large compute clusters having several gpu.
  - hence training llm is very hard ware intensive task.

![image](https://github.com/user-attachments/assets/56dbd2bf-e2a7-4e5c-9c7a-67c78144484e)

  - for e.g gpt-4 is supposed to be trained on cluster with more than 25000 gpu for 100 days
    llam2 model - 70b parameter model with 2 trillion token - compute cluster 6000 gpus for 12 days
    Falcon model - 80b parameter model with 6000 gpus -
    phi1.5       - 16 gpus

  - Therefore in order to train these llm we require compute cluster having several gpus depending
    on the size of the model and training datasets that is being used for trainig the dataset that is
    been used for training these llm.

    ![image](https://github.com/user-attachments/assets/6555b595-f531-46aa-8ee3-e1d27c2e65eb)

  - hypothetically speaking, if we need to train the gpt-3 on a single gpu , can you guess
    time it requires, it  requires 355 years. this clearly demonstrates the need for the mechanism
    through which you can distribute the  model training on several devices and run in parallel.
  - that is what distributed and parallel systems comes in to picture.

    ![image](https://github.com/user-attachments/assets/f5f29d2e-19d1-4458-b330-9cc105006284)

  - This parallel and distributed systems split  the task in to multiple sub-tasks and each
    on them run in-dependently or in parallel across these processor or devices or accelerators
    such as gpu so they can be completed simultaneously or in parallel.

![image](https://github.com/user-attachments/assets/d42e0363-890d-4353-a48f-3e5ea790e2c2)


  - using the parallel and distributed systems, the first thing we achieve is
    1) Acceleration of the training process - train llm faster in less time.
    2) memory efficiency - for e.g we already saw in fine tuning llm course that fully fine tune
       7b parameter llama or mistral model one would require atleast 100gb and biggest gpu
       currently available in market has memory limit 96GB. so we require such a distributed
       system to even load the model in order to train it. depending on the weight in which
       we do parallel and distributed computing, there are 6 different paradigms or techniques
       1) Data paralleism
       2) Model paralleism
       3) Pipeline paralleism
       4) Fully sharded data Paralleism /zero iii
       5) Tensor paralleism
       6) 2d and 3d Paralleism ( combined)
    

    
