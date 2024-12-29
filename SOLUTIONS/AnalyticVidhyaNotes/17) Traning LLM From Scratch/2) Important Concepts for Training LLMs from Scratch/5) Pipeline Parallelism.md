Pipeline Parallelism:
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
  - here at any point in time , only one device 

