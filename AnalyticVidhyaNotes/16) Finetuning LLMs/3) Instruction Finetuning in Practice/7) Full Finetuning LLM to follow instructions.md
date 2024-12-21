Full Finetuning LLM to follow instructions
===========================================


![image](https://github.com/user-attachments/assets/9d5c3519-d6b3-4078-97f0-cb60dae3fd46)

TASK - Next token prediction:
===============================

Step 1: Instruction Fine Tuning:
==================================

![image](https://github.com/user-attachments/assets/9f266ace-327d-4b4a-b091-8c36ca128d88)


- run are logged on WAND_PROJECT
- using tinyllama- which has 1.5 billion parameters

  ![image](https://github.com/user-attachments/assets/85d560fd-dd1e-42ed-91ff-f71b963e1893)
- assistant - chat bots answer user question high level instruction.


Step 2: load pretrain model and tokenizer:
===========================================

![image](https://github.com/user-attachments/assets/ba4bd2ef-c51b-4d67-af7e-6f85529809cb)

Embedding size resized 

Step 3:Store base model predictions on subset of 25:
====================================================

![image](https://github.com/user-attachments/assets/7aee4085-06ec-4ff6-bfb2-cad8a2fb1e0e)

- to know the difference of instruction pipeline , store the base model with subset of 25 examples.
- each conversion apply chat template
- goal to complete the assistance response.
- model.generate () decoding strategies , batch decode to get the human readable token.
- eval data has 25 samples a new column added base assistance message.
- for e.g user prompt with a short explanation how netflix work in 2000
- resonse below

 
Step 4:Print the response :
============================ 


![image](https://github.com/user-attachments/assets/83780e17-aaa9-4fe6-8f10-98e4810d0e7a)


  - see base assistance message from base model.
  - when user prompt was how netflix works in 2000.
  - instead of response , it asks more questions.
  - let try fine tune this to get response.
    
 
Step 5:FineTuned Model-Training :
==================================== 

![image](https://github.com/user-attachments/assets/2b0f0e65-f316-492d-8395-bc2763b63dac)

    - warm_up_ratio = learning rate
    - save_strategy, evaluation_strategy is "epoch" to save the model after every epoch.
    - weight_decay  - enable weight to be small.
    - report_to - tensor_board,wandb

 
Step 6:print the fineTuned Response:
==================================== 

![image](https://github.com/user-attachments/assets/e4da9125-8a8e-4570-a74b-f51ca6ea2409)



after training just call run
![image](https://github.com/user-attachments/assets/92515e28-8bcd-496a-b1b4-85ff46dd6edc)

trainloss - 1.8
validation loss -1.8


![image](https://github.com/user-attachments/assets/3130c41f-53e6-4786-9c5f-7d46e08a6cfe)

![image](https://github.com/user-attachments/assets/17d3836b-a08d-4f97-a408-1d3abfbc2d87)
    
Step 7: see nvidia - storage performance:
===========================================

![image](https://github.com/user-attachments/assets/d1bcc866-ab55-4979-ba58-6d19c655b559)


   - **gpu memory occupied by 1.1 billion parameter model with full fine tuning is 21.9 gb out of 40 gb**
   - let load fine tuned model.

Step 8: see nvidia - storage performance:
===========================================

![image](https://github.com/user-attachments/assets/81598f51-e5c9-4af8-b199-572281322457)

response

![image](https://github.com/user-attachments/assets/e0b7f786-340f-4225-8baf-69acba34abec)

    - load fine tune model.
    - set to float16.
    - eval mode()

    
Add instruct column message

![image](https://github.com/user-attachments/assets/b60724be-b348-4706-8497-174679867a7b)

- it returns response
- it does not ask further questions.

Step 9: compare outputbase model vs fine tune model.:
===============================================================

 

![image](https://github.com/user-attachments/assets/9309de4c-dd0b-4d99-9952-e1ed426f6c2a)

As you can base assistance model some of then are blank


Step 10: compare outputbase model vs fine tune model.:
===============================================================

![image](https://github.com/user-attachments/assets/56e16c3f-fb5d-4a8a-9cff-c4e256a6932f)


gpu memory consumed - 22gb  

![image](https://github.com/user-attachments/assets/b6c21b4b-32c5-4bf0-b832-7871854e7140)


Summary:
========
 - since gpu consumed is 22gb
 - As you can fully finetuning has more expensive if we want to use larger model
   for e.g llama has   7 billion parameter as smallest variant.
 - we see next parameter model fine tuning techniques.
