![image](https://github.com/user-attachments/assets/cb53a742-88af-48ed-983b-b8642a0cd971)Estimate Cost of Training LLMs from Scratch:
=============================================

    - previously module we looked at all steps that are involved in trainig llm.
    - in this model hands on exercise.


How to estimate cost of training :
==================================

![image](https://github.com/user-attachments/assets/4c10053f-03ce-45df-b953-261c36ba06f3)

  - three primary factors involved:
    1) No. of parameters
    2) No. of training tokens.
    3) Hardware.
  - first steps is to calculate the computation cost - i.e no of floating point operations for the
    entire training duration.
  - Hardware cost - hardware cost of hardware we use.

  calculate the computation cost:
  ==================================

![image](https://github.com/user-attachments/assets/c51aaa48-39bf-4f14-8c81-8e31019230d0)

  - depends on no of model parameters and no of training tokens.
  - there is a simple formula to approximate it
  - during the forward pass , each parameters participate in  1 addition and 1 multiplication 
    operation.
  - during the backward pass, each parameter participate in 2 addition and 2 multiplication operation.
  - i.e during 1 forward and 1 backward pass, each parameters participate in 6 operations.

Forumula:
=========

  - if model **have n parameters than formula becomes 6N floating point operations per token.**
  - if you training on P No of tokens , the entire formula becomes **6NP**.


1.Cost estimates of llama2:
===========================

![image](https://github.com/user-attachments/assets/ffe90e43-d1b6-4fd3-b424-1ca94b564560)


 input: no of parameters : 70B
        no of tokens     : 2T
        computation cost :**8.4*e pow(23)** floating point (6*7* epow10 * 2 e pow 12)

  - no of parameters is 70B and tokens is 2T
  - so total compuation cost becomes 6(floating point operation in 1 forward , 1backward pass per parameters)
  - 7*e pow 10 - total no of parameters involved
  - 2* e pow 12 - training on  2 Trillion token.

 Summary:
 ========

 above is the total approproximate no of floating point operations one would perform while training
 llam2 model which has 70B parameters on 2Trillions tokens.

 
2.Hardware Cost:
=================

![image](https://github.com/user-attachments/assets/f90363ec-b773-4853-aaf6-987f982efdb6)

- Depends upon type of GPU/TPU you are using, type of interconnection,cpu, related storage and many things.
- for e.g A100 GPU in half precision can perform - 3.12e14 Flops per sec - peek performance.
- however when training such large language models , you wont achieve above peak performance for A100
- this happens because the models are very large to fit on any single gpu , communication overhead
  when output goes form 1gput to next and so on.
- because of the so many inefficiences , we wont able to perform the peak performance of the given gpu.
- thats where model **flops utilizations** come in to use.
![image](https://github.com/user-attachments/assets/ca8031e2-08ad-4e68-ae77-5c1dba367aa9)

- it gives the real word estimate of the performance that we are able to leverage from gpu.
- here if you have most efficient implementation i.e most efficient distributed computing implentation,
  still we would be able to achieve the around 50% of the peak performance.
  50% of 3.12e14 is 1.5e14 flop per sec
- that is most efficient implementation out there such as megatron ll.
- now we compute the time taken.total no of floating point operations during the
  entire training run that we have calcuulated for the llam2 model was 8.4e23 floating point operations.

![image](https://github.com/user-attachments/assets/778fe180-a659-46f3-8d4a-2f48d20848be)

- if you are able to achieve 8.4e23 floating point operations then how many hours would that would consume.
- so it is total no of operations / no of operations that we perform per sec * no of sec in hr
- so formula becomes
- to train llama 70b model on 2t tokens using a100 gpu with model flops utilization of 50%
  we  get  No.of hours 8.4 e23/(1.5e14*3600)  = 1.55e6 A100 hours.
  ![image](https://github.com/user-attachments/assets/9b00757b-f9bf-4fe6-ad01-62d2878e3f0a)

 - Total cost is cost : 1.55e6* ($1.8/hr) = $3Million dollars to train from cost.
 - thats why to train a llm from scratch it take 3Million .

![image](https://github.com/user-attachments/assets/edc8b905-f598-4d10-831a-3b40d9ae103b)

Summary:
========

![image](https://github.com/user-attachments/assets/34a59f47-718b-4880-abdd-b2ac45e97f19)


 - cost of llm is (computation cost /MFU) * hardware cost.
   MFU - model flops utilization that we are expecting or observed.
      

 
