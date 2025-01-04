Preference tuning LLMs with DPO:
================================


    - gone through supervised, dpo and ipo



  Step 1: dataset:
  =================

  ![image](https://github.com/user-attachments/assets/38bb5f2b-833b-47dd-a675-04e25cbda0b8)

![image](https://github.com/user-attachments/assets/2574bc64-bbce-4c7b-af00-704709c1850d)

  - above is the dataset for stf trainer.


Step 2: train.py:
=================


![image](https://github.com/user-attachments/assets/df8d0331-c794-4987-81e5-bcf4ea70888b)
![image](https://github.com/user-attachments/assets/0502b6d6-1df7-46dc-80c1-958e150215db)
![image](https://github.com/user-attachments/assets/6254b72b-ad86-424a-b958-c127f7591df3)
![image](https://github.com/user-attachments/assets/a3d1091e-a4b4-4e79-b5be-bdc6b525fe2e)
![image](https://github.com/user-attachments/assets/17cd74f3-6462-4473-9584-9c7bea38967e)
![image](https://github.com/user-attachments/assets/f31cdc99-a170-45e9-b954-896fee29e8c1)
 
![image](https://github.com/user-attachments/assets/a4c4a59a-a991-4864-afc3-3d734d72ca1f)

 
 - using qlora to reduce the memory requirement to build in single gpu.
 - specify whether you need nested quantization or not.
 - main method we create and prepare model.


Step 3: utils.py:
=================

  - function to create and prepare model - given the model arguments.
  - if SFT  itself is peft lora adapter ,if the model was finetuned using qlora
    then we do peftconfig else qlora now use peftconfig else create normal model and we do
    full fine tuning using DPO.
  - In DPO, one important point to note is it needs the current active model as well as
    reference model.
  - so it needs 2 model.
  - but in PEFT, what can happen you can use single base model and have 2 different set of
    adapter, thats exactly what we do.
  - since we have only single base model and 2 small adapters on it it requires much less
    memory when compared with full fine tuning with DPO which require huge amount of GPU memory.
  - here we use multi adapter support in PEFT in order to reduce the memory requirements.
  ![image](https://github.com/user-attachments/assets/d5342194-da7c-4f52-94cc-0f58d37e6e11)

    
![image](https://github.com/user-attachments/assets/02f8bc08-8d73-48eb-badc-d79aae0b7141)
![image](https://github.com/user-attachments/assets/f0401f0e-bf7b-4101-87b7-2e2834eb4fd4)


Step 4: run_dpo.sh:
======================


![image](https://github.com/user-attachments/assets/0ff8cd55-e5c6-4299-945c-2969f8f7df11)
![image](https://github.com/user-attachments/assets/488882c6-db03-45cd-ac4f-a8b671585f8b)

![image](https://github.com/user-attachments/assets/41301d94-faf0-4761-8fc0-7e120054dfb8)

![image](https://github.com/user-attachments/assets/0c53c56f-3460-48a0-b966-e4d00ae175fb)


summary:
========

  how to perform dpo and how it is easy with hugging face.
