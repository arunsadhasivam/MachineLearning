![image](https://github.com/user-attachments/assets/f521439b-37cb-4107-ac6e-8afab66d2851)Hands on - Training LLMs from Scratch using DeepSpeed ZeRO 3/FSDP Distributed Training on 8 GPUs
=================================================================================================


![image](https://github.com/user-attachments/assets/b99985b1-257f-4eab-bc90-166388a6da21)


- in this lesson , how to use the fully sharded data paralleism or deep speed zero redundancy optimizer stage3
  to train 7B parameter model on A100 GPU on the dataset using tokenizer that we have created in the previous lessons.
- here the code that we are looking in the training subfolder of module 4.


![image](https://github.com/user-attachments/assets/f794d0e7-fbcf-4f77-b6a0-b194a0edeabf)

Training code:
===============

![image](https://github.com/user-attachments/assets/c9ef4c11-5369-4e62-896f-e652f0f1e9a5)
![image](https://github.com/user-attachments/assets/bf7beb6c-cf80-4ed4-921d-35d43c6b8afe)
![image](https://github.com/user-attachments/assets/acae30e7-1515-4269-923a-644c4b2907e3)
![image](https://github.com/user-attachments/assets/e1269827-76e4-4ccc-abc3-6b0e4d8e05ba)
![image](https://github.com/user-attachments/assets/bff89d4d-8bea-4d1f-ac57-380313f4e9e4)
![image](https://github.com/user-attachments/assets/689658eb-1681-46e8-9425-87a7b5220071)

- lets look at the training .
- first step is to get the arguments i.e model arguments, data training arguments and training arguments.
- here lets look at the model arguments
    1) model name or path
    2) then get the tokenizer_model_name or path.
    3) use_flash_attention or not  
    4) use_retrant - gradient check.


  Data Trainig Arguments:
  ========================

   - hug_stack dataset that we have created.
   - max_seq-length of each sample is 4096. because we pretrain on code file can be really long so that we want to train
     such data set.
   - test_size is 0.1 ,if no test file we create 10%
   - pretrain from 7b parameter model.
   - we use blue train as 
   - resize model embedding to sync with the length of tokenizer
![image](https://github.com/user-attachments/assets/31280d65-3d49-4566-b6cc-f6c718541773)

 - we create an trainer object to which we give the model , trainer arguments, eval dataset
   and print the resulting model. if you have resume from checkpoint. else it train from start.
- you can see also fim.py - logic to **fill in the middle**.


Summary:
=======

![image](https://github.com/user-attachments/assets/521699c1-7627-40de-ad91-2d138abf7899)

  - now so we have the code to trian the module where in we first pass the arguments ,
  - load tokenizer that we train
  - load the dataset that we curated
  - then create train and valid split
  - then we create the trainer object
  - pass the 7Billion model that is randomly initialized along with the tokenizer, the dataset and other training arguments.
  - then train the model and save it.
  - this is the entire flow.
  - another part is to create a config , we will be using hugging face accelerate library
    for helping with nitty gritty details for distributed computing .
  - it already has fsdp and deep speed integration in it. all one need to do is to specify
    the config file or create a accelerate config .

Steps to do config file:
=========================

go to config folder 2 config there. 

![image](https://github.com/user-attachments/assets/c3625e4d-2c1c-441e-946f-d9bae143399d)


in order to create new config , call dummy_config.yaml , give multi-gpu in the prompt requested.

 
![image](https://github.com/user-attachments/assets/8f9dd36f-f4db-466d-a498-44b0ef576bd1)

  As you can see updated in config file

![image](https://github.com/user-attachments/assets/61564d08-01a8-4b48-b68f-2146ed66cc61)

- in this way all we do is create a config when using accelerate for either deepspeed or FSDP.


deep-speed-config.yaml:
========================

![image](https://github.com/user-attachments/assets/ecae2d6b-4f95-44db-95e3-1d108b496a27)



 - once we are ready with config above , then we need to launch your training job.
 - here is the whole lauch command that we use.



![image](https://github.com/user-attachments/assets/bb0dc7ce-f98a-4a18-9ee8-b03c8629e79d)

- seed is 100
- tokenizer that we use is that we have trained is "hugcoder"
- dataset_name : hug_stack
- max_seq_len: 2040
- output_dir  : hugcoder_dummy.
- accumulate gradient for 4 steps i.e entire batch size is 16x4 =64 and 64X6 gpu = entire global batch size. 
![image](https://github.com/user-attachments/assets/672a0096-c140-4fa8-b17e-16861d13842b)

- use gradient checkpoint to save memory.

- so once we have got everything ready , all we do is run the code.


run code:
=========

below command to run the code. below see it uses deep speed to start.




![image](https://github.com/user-attachments/assets/b314f436-f912-445b-96ce-cc4243774c27)
![image](https://github.com/user-attachments/assets/3e59763b-ebd7-404c-8264-ea213adf53dd)
![image](https://github.com/user-attachments/assets/48548c0c-25c1-4553-8b05-478805bd39d0)
![image](https://github.com/user-attachments/assets/441544f0-a17c-464d-8d65-1822d910ebb7)
![image](https://github.com/user-attachments/assets/507d6792-8360-412a-91de-fa1b286c620a)
![image](https://github.com/user-attachments/assets/0ccbb788-8f4d-451e-a116-9df609411562)

  - below shows 42 layers
  - it uses the config here and
  - fully sharded data paralleism.
  - see it is logging in to wonb
![image](https://github.com/user-attachments/assets/bf0a4838-b0a6-4377-9c3f-4f69a5fde3f1)

  - you can see loss in graph started around 10.731.
  - thats how we trained the model using deepspeed using a100 gpu.

![image](https://github.com/user-attachments/assets/08b3b9f5-081e-492e-8dd0-60cea4a30e0a)


NOTE:
=====

  - Also file to run using   run_fsdp.sh which is from pytorch.
  - both does the same thing but they have different implementation details.
  - we also looked at the loss plot.
  - in terms of evaluation , we wont carry out any evaluations or qualitative evaluations
    because training a 7b parameter model form scratch requires atleast 1 trillion tokens.
  - if we just use training loss and compute loss and compute it . we see that we need
    atleast gather and collect , which we dont have. we only train using only 110 million tokenss
    which is 10 power 4 less.
    ![image](https://github.com/user-attachments/assets/284af805-99ce-4ea9-8c45-9c7b175f0704)
