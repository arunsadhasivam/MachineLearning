Finetuning LLMs:
==================

  - this method will help us to tackle the challenges which we face with RAG.


why FineTuning LLM:
====================

![image](https://github.com/user-attachments/assets/29d4b5d1-8db3-4bce-825e-2cc1796b2372)


- pretrained llm like gpt-3, llama2 etc are trained on large scale internet dataset when applied on a specific task
  or our own dataset it can still do the job for us but might not be as good as one with fine tuning.
![image](https://github.com/user-attachments/assets/557e56f1-946f-4c4b-8384-85dee1aebde9)

- for e.g when i ask question like "how do i play and swing cricket ball" to a **pretrained llm** answer " play straight"

![image](https://github.com/user-attachments/assets/aa2427f9-397d-4278-945f-a42a38145a8f)

- when same question with **fine tune llm** trained on cricket book the answer is - "keep play shot close to body, play straight"
- actually fine tuned model giving me lot better model.
- Reason is that fine tune llm adopts the parameters and domain of the pre-trained llm completely to our
  specific domain that we are trying to get the output.
- hence specific domain knowledge will be incorporated in to the model like in our case "cricket"
- As a result , the answer is much more specific and more details.
- similary domain knowledge could be enterprise data, legal,healthcare , finance and other domain.
![image](https://github.com/user-attachments/assets/4b461e9b-ecc0-48ab-9ddb-12447fd318ab)

- for e.g llma2 is a pre-trained llm, but when you fine tune llama2 on the code related data, the resulting
  code llama outperforms llama2 on code related tasks.
![image](https://github.com/user-attachments/assets/1da45709-019c-40fe-b979-fe77c0501198)

- similarly github copilot is a fine tuned gpt-4 model on github repositories resulting in   specialized models on
  code data.


what is fine tuning LLM:
=========================

![image](https://github.com/user-attachments/assets/2e85906b-1af9-46d3-93cc-8a265fd6e181)

  - so **finetuning llm refers to taking pre-trained llm** like GPT-3 or llama2 or any other llm .
  - i.e model architectures and its parameters which its existing knowledge of these pre-trained llms.
  - so this knowledge, which these pre-trained llms are stored in its parameters and the existing knowledge.
  - you pick that and post that we retrain the parameters of the pre-trained model on the domain specific
    dataset. post that we have a fine tuned model in domain specific dataset.
  - now the user can interact with the fine-tuned llm rather than the pre-trained one.

![image](https://github.com/user-attachments/assets/8fe3ea0b-77a8-4c5e-9e9b-8547d693b0d3)

  - let says we want to fine tune for llm for solving a "sentiment analysis on health care domain"
    we take the pre-train llm like gpt-3 model and its actual parameter and retrian the parameters of the model
    on the sentiment analysis dataset.this result in finetune model specific to our sentiment analysis task.

Methods to fine tune LLMs:
==========================

  - there are broadly 2 different methods to fine tune the llms.
    
1.Full Fine Tuning:
===================
![image](https://github.com/user-attachments/assets/bde87e8a-90da-4a26-8fb1-33168f55bbca)

- where in you re-train the parameters of the entire model on our domain specific dataset.
- the challenges with this techniques is computationally it is very expensive process.
- it involves re-training of the entire parameters of the model.
- next method overcomes this challenge.

2.Parameter Efficient FineTuning:
===================================    

![image](https://github.com/user-attachments/assets/1299a6fd-f2e9-4151-b952-0c2caf82a8f0)


  - PEFT or parameter efficient fine tuning refers to training or re-training the fraction of the
    parameters on our domain specific dataset.
  - fraction of parameter can be a additional parameter to pre-train llm or it could be part of the llm.

Popular PEFT techniques:
========================

![image](https://github.com/user-attachments/assets/d5ae616d-a973-406c-8628-5663af280cd0)

  - some of the few popular PEFT techniques are LORA, ADA-LORA , QLORA , IA3,LOHA,LOKR
  - in dedicated course we learn these fine tuning methods.

Pros:
=====
![image](https://github.com/user-attachments/assets/2c1bb224-da5c-450e-8919-a37bad60d260)

  - As oppose to RAG, there is no limit on the size of training data to be used.
  - these model are far mode consistent with their output.
  - they tend to produce right responses whenever you ask it.
  - they produce high performance


Cons:
======
![image](https://github.com/user-attachments/assets/f47ec303-13d5-4a83-af23-35a1174d8ab2)

  - high quality data for training.
  - upfront cost is high.
  - recommend to select domain specific llm for fine-tuning.

Domain Specific LLM:
======================

  - let say solving the sentiment analysis task,
![image](https://github.com/user-attachments/assets/e72f67d6-18bc-4086-be73-c8b526dd2b05)

  - fine tune llm with domain specific will give extra edge over pretrain on general llm
    e.g when working on medicine data, fine tunning the medical related pre-training llm.
    fine tuned medical with domain specific pretrain gives more performance and accuracy compare
    with pre-trained on general purpose llm.
    since it is having more knowledge on medical related data.

   - hence fine tune with pretrain domain specific llm boost performance compared to general purpose llm pre-training.
  
Which is right pre-trained llm for you:
========================================
![image](https://github.com/user-attachments/assets/2737957d-ef9b-49e5-8060-a90990b5b768)

  - when you are solving a issue in particular domain.
  - select the pre-train llm which is closer to your domain you are working on.
  - in case you cannot find one , you can still go ahead and fine tune the general purpose pretrained llm
    and get a high performance model.
  - but if you are working with an enterprise data and you are building a solution where even a slight  
    improvement in performance is critical in that case you need to build our own llm from scratch.

Train LLM from scratch:
========================

  
![image](https://github.com/user-attachments/assets/8f633cde-0e2d-4c19-9ecc-c92b46187ee5)

  - but train llm from scratch needs massive dataset,huge gpu computation power and lot more resources.
    
