
Text Classification on Twitter Complain Dataset using Prompt Tuning (Part-2):
==============================================================================


![image](https://github.com/user-attachments/assets/4e8746e0-2787-418a-ad00-6d6ecd33a04d)


As you can see model trianalbe percentage is 0.008

#15 soft prompt token learned by via fine tuning.


Step 5: create optimizer:
==========================

![image](https://github.com/user-attachments/assets/171df1fe-be3b-4338-867c-418a6ad9a53e)


  - decay - 0.1
  - learning 10e-4 
  - no of training steps - length of train dataset loader.

Step 6: Qualitative evaluation on test sample:
================================================

![image](https://github.com/user-attachments/assets/bacb414f-9baa-41be-bc77-84d8cdd0a754)


As you can see output is giberlish output not in expected format.


Step 7: Training and evaluaton loop:
====================================

![image](https://github.com/user-attachments/assets/2b6e23d7-7d89-4026-9537-19942d8a2e04)

 - in previous we use sftTrainer
 - here we use own trainer ( custom flavor script)
 - put batch on gpu
 - we use automatic mix precision
 - forward pass and get the output prediction and loss
 - backpropagate to get the gradients.

After running

![image](https://github.com/user-attachments/assets/708af69b-12b9-4e48-adc5-7b8571644716)

 - lower the loss , lower the perplexity
 - training a model has finished and we got training perplexity of 1.0858
  
Step 8: Qualitative evaluation on test samples after finetuning:
================================================================

   - now qualitatively evaluate on test sample.
   - save the metrics to wondb

![image](https://github.com/user-attachments/assets/b22f5335-11fd-4bcd-8e16-5b458e92caba)

   - model correctly above predicts as complaint . i.e some user raised an complaint
     as "for tommy product"

Step 9: Saving the model and optimally pushing to hub:
======================================================

![image](https://github.com/user-attachments/assets/fc5e94a8-4c48-410d-8d9e-b10dee129b61)

    - save locally and then push to hub , set private to true.
    - As you can see it is pushed to hub

    ![image](https://github.com/user-attachments/assets/ab500859-b34a-43df-818f-153464ac0414)


    - Model is just 246kb compare to 14GB of base model. the fine tune model occupies less storage.
![image](https://github.com/user-attachments/assets/a0b70522-0320-4a23-a172-e997446dcd61)

    - this is how PEFT model stores via 2 files above 1) adapter_config.json and 2) adapter_model.safetensors.

![image](https://github.com/user-attachments/assets/8a9afc36-7ada-4ffa-ae56-bfc68cc60c6d)

    - for full fine tuning , tiny-llama 1.1 billion parameter model - 22gb
    - with prompt tuning , 7Billion Parameter(7 times model of tiny-llama) - still takes less memory
    - this is how PEFT approaches reduce the storage and compute cost.


Step 9: Load the PEFT checkpoint and do the qualitative analysis of the test sample:
=======================================================================================    


![image](https://github.com/user-attachments/assets/752d6176-6ad6-4ab6-916e-ecacac8d6236)


     - load first the trained PEFT config, via PEFT config from pre-trained method similar to how we
       use pre-trained model to load base model. similar our PEFT config we can do PEFT config from
       pre-trained , give PEFT model name or path i.e PEFT model id, we get config
     - we load the base model via AutoModalLM.casualLM and to get the base model , name or path
       we can get from the config.base_model_or_path and load in float_16.
     - then to get the pre-trained adaptive weights i.e prompt tuning embeddings. we just need
       to do PEFTModel. from pretrained , give the base model the path to the PEFT model and going
       to load the tokenizer via from Pre-trained model of Autotokenizer.
       
![image](https://github.com/user-attachments/assets/27cecadc-3210-43e4-b49d-78046efd707d)

 ![image](https://github.com/user-attachments/assets/17d1bd80-9351-427d-9c6c-3b6a3769e555)


 - here you can see how model performs
 - output is virgin media - complaint and model correctly read and predict it.
 - 
