![image](https://github.com/user-attachments/assets/74ad4d57-33ff-4f5e-89ca-52102b3578d2)![image](https://github.com/user-attachments/assets/e1898585-79fb-428c-8a66-4d41768e5bf1)Training LLMs from Scratch:
============================

  - train llm from scratch.
  - we learned different methods to build llm based applications.
![image](https://github.com/user-attachments/assets/4cbc5b57-cf79-4256-8254-da5516aefe9a)

  - we learned about prompt engineering, RAG,fine tuning llm and lets gets started with training llm from scratch.
    
Training LLM from scratch :
=============================

![image](https://github.com/user-attachments/assets/c0c74080-e69f-486a-b82e-987e73eed0e7)

  - training from scratch refer to build a pre-trained llm like GPT-3, llama2 , falcon180b or so on .
  - the process of training llm from scratch is also known as pre-training LLM.
![image](https://github.com/user-attachments/assets/624481cf-265f-48cc-8163-9264351e3aa5)
  - objective is to predict the next word in the text.
  - these models are optimized for text completion.
  - if you observe , this is simply about training or continuing the text llm that we have been
    talking about getting started with course.

Pros:
=====
![image](https://github.com/user-attachments/assets/95d922df-1639-4bef-bbbd-ecb8f50e2f10)

  - domain specific llm improves the performance of domain related tasks.
  - training our own llm, also gives you the superior performance either across use case tailored to your vertical
    allowing you to build a sustainable advantage.
  - in general small domain specific llm outperform large general specific llm.
  - privacy is one of the important concern, while working with commerical llm like chatGPT, claude.ai.
    because as sooon as the user hits the api, the entire data is sent to the cloud server of the provider.
    this might not seem to be safe while you are working with confidential data.
  - so when you trained your own llm from scratch , the data resides on our own server and on our own premises.
    you have complete control over the llm where in you can monitor the performance, re-train the model depending
    upon the performance.

Cons:
======

![image](https://github.com/user-attachments/assets/651bd20d-10fa-420b-8051-ce65c8065d18)


  - training llm from scratch has no doubt is challenging tasks let discuss.
  - we would need massive dataset which is in the range of lot of GB'S.
  - just to give you a quick check on training dataset for training different GPT models
  - GPT-2 was trained on 2.5 gb of data,GPT-3 was trained on 570 GPU of data.
  - training llm from scratch is hardware intensive task, needs massive GPU infrastructure as well.
![image](https://github.com/user-attachments/assets/8e435612-a46c-416e-b39e-2831c1309b21)
![image](https://github.com/user-attachments/assets/b6815dac-2b60-429f-bbbb-e8d148aeef36)

  - e.g hardware consumed for popular llm - falcon180B trained up to 4050 GPU simultaneously.
    using llama2 trained on 2048 80gb GPU with training time of 21 days of 1.4 trillion token.
![image](https://github.com/user-attachments/assets/be7ea053-f55a-4cf1-9bd6-278bf57b00c4)

   - llm are trained across multiple GPU for several weeks.
![image](https://github.com/user-attachments/assets/ad8f00cd-aae1-4ab0-a2b7-2431a79b4c67)

   - imagine if at all , we have to train GPT-3 on a single V100 GPU , the time it could takes
     is : training 150B parameters is 355 years on a single nvidia v100 gpu.
![image](https://github.com/user-attachments/assets/37f9c719-f985-4aa6-801b-8fe2f9959999)

   - this clearly shows we need parallel distributed architecture for training these models.
   - training llm from scratch involves training billions of parameters over week and other thing
     the cost involved is high.
     

    

    
    
