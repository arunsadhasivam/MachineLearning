What is Parameter Efficient Finetuning?
=========================================


Definition:
===========

- allow to finetune large pretrained model with fewer parameters.

    ![image](https://github.com/user-attachments/assets/b27d2441-1fe9-4fa5-b146-b8e06ac4c6a7)

Goal:
=====

 
  
![image](https://github.com/user-attachments/assets/04fb50f8-f902-43c5-81d7-301e0bf2f4b9)


How does PEFT Works:
====================

![image](https://github.com/user-attachments/assets/2aa591df-5a14-4a17-9675-517c50260da5)


  - PEFT only fine tune a small number of (extra) model  parameters while freezing most
    parameters of the pretrained LLMS, thereby greatly decreasing the computational
    and storage costs.
  - limitations of **Full fineTuning** are addressed .
  - also address **catastrophic forgetting** - phenomena where model forget certain
    knowledge after fine Tuning. this is observed in full fine tuning as all parameters
    of model are adapted to only downstream tasks. this makes model to forget own prior knowledge before
    fine tuning.
   - so in PEFT we fine Tuning only fraction of parameters.

![image](https://github.com/user-attachments/assets/0507ac3b-8666-4211-ad34-6ee74788113d)

![image](https://github.com/user-attachments/assets/a7c2b47a-4a75-42b7-922f-0f3a2130121e)



    
