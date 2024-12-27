Text Classification on Twitter Complain Dataset using Prompt Tuning (Part-1):
==============================================================================


  - we have already gone through the theory.
  - hands on project
  - connect to jupyter note
  - once login , install requirements.
  - log in to WANDB
  - choose module 4 - fine tuning notebook.
  - how to do prompt tuning for the text classification task.
  - import autoModel ,AutoTokenizer ,setSeed to have reproducible experiment to see same result(reproducable result).
    
**Task Type**- Text classification
**PEFTType** -  Prompt Tuning Type.

Step 1:Load the data and config:
=================================

![image](https://github.com/user-attachments/assets/4fde28bf-48ec-4c2a-8ef4-768bf8c637c4)

Data set - twitter complaint
TextLabel - tweets text
Learning Rate - 10e pow 4
output - complaint or not a complaint.

Step 2:DataSet preparation:
===========================


![image](https://github.com/user-attachments/assets/51c49f3c-ecba-45b4-8b78-d5e5726ebea7)

![image](https://github.com/user-attachments/assets/5d493bfa-840a-486e-8724-97a22d3ae230)

  - load dataset using loaddaset from library.
  - get the class label and map 0 and 1 numbers or class label to corresponding natural language class descriptions.
  - then call dataset.map to replace integer name with corresponding names.
  - trained dataset has 50 samples , trained dataset has around 3400 samples
  - this shows how to learn from few shot samples and generalize to a large text dataset.
  - here you can see result tweet is no complain.
  - distribution of label ( 17 of samples are complain , 33 - not complain )
    little of skewness towards most samples tweets are not complain.
  - Now preprocess the dataset


Step 3:Preprocess dataset:
==========================

![image](https://github.com/user-attachments/assets/c5ed1166-9150-419a-a275-76c6eba256f5)
![image](https://github.com/user-attachments/assets/12b242ac-2c3f-47e4-9757-e700da2fa98a)

![image](https://github.com/user-attachments/assets/4cd5110c-328c-4a39-8060-7f0f3522fcb6)
![image](https://github.com/user-attachments/assets/1e98185d-dbce-4760-8075-8a5f59e223ef)
 
  - first load token for mistral
  - max_target_length - no complaint or complaint.
  - preprocess entire dataset to feed to model.
  - doing in batch manner in each call you will have n no of examples.
  - we want to remove original column from the dataset.
  - simplicity train , eval same.
  - we are going to have **train data loader** where we shuffle **train** data set and **eval** dataloader
    is just train data loader **without shuffle**.
  - if sentence is with label is short then it we prepend with **pad_tokens** of the left hand side to make it 64 max length.
  - input embeddings.
    ![image](https://github.com/user-attachments/assets/907c8d4e-d1e3-4d65-9f1e-a4eb5726d716)
  - **attention_mask** - it has all **pad_token** has **attention_mask of 0** since it is pad_token rest it need to attend to.

    ![image](https://github.com/user-attachments/assets/5045db6e-27c7-4e9c-9375-cff6e37660ce)

  - labels - you can (-100) loss is ignored for the token ,
    loss only for label -> 708( no complain),22105 (complain)
    
  After preprocess dataset, we pre-process the text dataset.

  
Step 3:Preprocess text dataset:
===================================

![image](https://github.com/user-attachments/assets/1d7da277-1c1b-423d-be31-73e28b948563)

  
  - we have similar text process function.
  - we have input id, attention mask similar to dataset above
  - but we dont have label because it is text dataset, so we need to predict on sample.
  - we use train data loader again,we only have newline - label:thas it  . task of the model is to predict the next word
    should be complain or no-complain.
  - Next step to create PEFT Model, Optimizer and LR Scheduler.


Step 4:PEFT Config:
===================


![image](https://github.com/user-attachments/assets/c55efd8b-7324-4b72-aa5e-818ba787c04f)

   - first create prompt tuning config.
   - here we want to initialize the soft prompt tokens with these embeddings or embeddings for these words.
     i.e classify the tweet is complain or no-complain and then new line.
   - so to prompt tuning config Class we pass text_type as CAUSAL_LM - because we need to predict
     the next word as complain or no-complain that is CAUSAL_LM.
   - num_virtual_tokens  - that we want to have is  len of the token we initialize with.
   - input_text - we want to initialize with.
   - tokenizer - to tokenize the sentence in order to initialize the prompt embeddings that will
     be learned through  this fine tuning process.
     ![image](https://github.com/user-attachments/assets/861bdd2d-3399-459a-838d-a7921d3a8bd5)
   - first create PEFT model here first load base model via Automodal CAUSAL_LM from pretrain give
     the base model and load in half-precsion of float 16.
    - once we have this model, now we see to get the PEFT model all we do is to get the
      PEFT model and pass the base model and the PEFT config that we created.
    - thats it, giving the model and PEFT config calling it as PEFT model , you get PEFT Model.
    - here we are printing the no of trainable parameters to show that we are only fine tuning
      fraction of parameters compare to old model. We also to enable **gradient checkpointing**
      and going to have model reside on GPU.

     ![image](https://github.com/user-attachments/assets/c094ac3d-9962-4048-a393-9f34b50be278)
     ![image](https://github.com/user-attachments/assets/34d269bf-dc02-474c-bb03-a2a14f05a1c9)

     - see now loading the base model ( 7 billion parameters model) and half precision it takes 14gb
       full precision in 28 gb.
 
     
    
