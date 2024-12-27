Function Calling using QLoRA
=============================


Instruction Fine Tuning using QLORA:
=====================================


Setp 1: setup Env:
==================

![image](https://github.com/user-attachments/assets/b164141f-880b-44b3-a9a1-8b34d3c8d1da)


  - set wonb project
    
Setp 2: Data Processing:
=================================


![image](https://github.com/user-attachments/assets/5073f15c-45a5-4ee1-8369-03729fb309a9)

 - code llama which is 13 billion parameters
 - format in a way to get chatml

![image](https://github.com/user-attachments/assets/abd564c2-05c2-4d74-90e5-14a065c332e3)
![image](https://github.com/user-attachments/assets/d8bb1bc0-9212-4a46-a047-b09a03fefe7d)
![image](https://github.com/user-attachments/assets/648b50f9-1f51-4d12-8cee-34ce9b2a7ebc)

- This is how you can make your chatbot to act as an agent, it make api call, use calculator
  or use google map . it can use separate tools to achieve end objective.

- internally chatgpt also works like make function call to different tools based on the objective.

Setp 3:Create PEFT Model:
===========================

    - quantization  is 4-bit
    - using double quantization to save gpu memory
    - it uses same chatml, template same we used so far, tokenizer, pretrained model.

  ![image](https://github.com/user-attachments/assets/f6738653-edf1-4991-a045-0bead27fecd6)


  ![image](https://github.com/user-attachments/assets/75f32db3-8b6d-43eb-9e3a-3b6aea44e41f)

![image](https://github.com/user-attachments/assets/0045a256-07aa-4e02-a318-c417507a3cba)
![image](https://github.com/user-attachments/assets/4d037e35-299c-4f5a-8762-3414eefdfcc2)

 - it uses 24gb of memory
 - pretrained model loaded now set training arguments with the output directory being
   core llama function instructs.


Setp 4:Training:
===========================

![image](https://github.com/user-attachments/assets/c91503c9-a8a1-4bd3-a14b-395389f0c34b)

   - accumulate gradient for 4 step
   - logging every 5 step
   - learning rate is 5power -4
   - learning rate is cosine

![image](https://github.com/user-attachments/assets/74e22f40-d36c-48c8-8df0-050063345a65)

     
   ![image](https://github.com/user-attachments/assets/c125dd3e-d233-4c20-9cf9-ac2b760bc974)

- no of parameter is 13 billions
- we have low rank  matrices of lora and lorb
- all are linear 4bit meaning it is quantized, so gpu memory is decreased
- now save and run the model.
- it takes so much time

![image](https://github.com/user-attachments/assets/158863a6-59a7-4099-86e8-f9db86f0c33c)

  ![image](https://github.com/user-attachments/assets/59c516bb-9e2f-467b-8c4b-087b6522ddbe)
![image](https://github.com/user-attachments/assets/d21b9771-ddab-40ba-af3a-70ae64326947)


- memory req is 32 gb that too 13 billion parameter compared to in full tuning
  1.5 tiny llama model it tooks 24gb . it is almost 12 magnitude larger model.
  
  
Setp 4:load the fine tune model and get the predictions on the trained model:
=====================================================================================

![image](https://github.com/user-attachments/assets/acbde961-b1cb-4f8d-8023-18a8f6be0893)

![image](https://github.com/user-attachments/assets/23d818a1-5076-4d5e-8fc2-42cbc87f7317)

![image](https://github.com/user-attachments/assets/a8436956-19cf-421e-abb9-da44a66a31f1)

![image](https://github.com/user-attachments/assets/bc9842ea-2591-4087-a0ce-9639d55fc743)


- good result for fine tuned model.
