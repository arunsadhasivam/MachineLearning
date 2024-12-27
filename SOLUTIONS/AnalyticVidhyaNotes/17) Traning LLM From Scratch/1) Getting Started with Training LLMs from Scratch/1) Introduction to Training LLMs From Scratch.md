Introduction to Training LLMs From Scratch
===========================================


- Instruction Following LLM like chatgpt, bard, gemini are used currently for business
- Each LLM are built on top of base LLM e.g chatGPT4 is fine tune from base model CHATGPT
- therefore the **instruction LLM are build on top of the base LLM**.
- Researchers build base LLM and they further finetuned inorder for this model to follow the instructions
  and align with human preference to be helpful , honest and harmless.
- since then, various llm are developed by training on different domain specific dataset by experimenting with
  model architectures and scaling the llm in terms of both parameters and data.
- significant contributions and experiments to this reasearch have been made by organization such as
  openai ,meta,google and anthropic,microsoft,mistral and others.
- let us take a look at the evolution of the llm by some of the companies.
- openai release 4 different varients of GPT : gpt-1,gpt-2,gpt-3,gpt-4 based on size of data as well model.
- gpt-1 (117 billion parameters and it was trained on 4.5gb of data.
- gpt-2 (10 times more data and it had 1.5 billion parameters)
- gpt-3 ( 175 billion parameters and trained on 570gb of data)
- gpt-4 (1.8 billion parameters based on architecture) - also multimodal model capable of processing text and images.

- SImilarly meta llama released with 65 billion parameters with 70 billion parmeters.
- google palm 540 billion parameters & trillion tokens.
- gemini multimodal surpases state of art benchmark in terms of coding and performance.
- over period of time training the llm and performance increases.
- central tendency is as it gets bigger and bigger in terms of model size as well as training data they
  generally becomes more powerfull in terms of its capability in solving various different tasks
  such as logical understanding, coding and so on.
![image](https://github.com/user-attachments/assets/8cc09db3-ac47-4d05-8edd-18d84825e356)


- recently big interest in building small LLM. idea is building small LLM trained on
  high quality data compete with llm trained on general purpose internet data set.
  e.g microsoft released phi-1,phi-2
![image](https://github.com/user-attachments/assets/c50d7bc5-ee81-4e65-ab64-a293f7cf22d2)
- phi-1 it outperforms bigger model like palm.
- reason for success is even though small but it is trained on high quality data like text book level data
  as well as synthetically generated data from gpt-3.5 so it results in superior
- microsoft released phi-1.5 model which has 1.5 billion parameters which is a general purpose
  model trained on high quality data most of its synthetically generated. its performance
  is compared to model which are 5 times larger in size. eventhough it is small performance
  is great, because model is trained on high quality curated dataset and synthetic dataset.
  microsoft further build on this release 5 phi-2 model.
  ![image](https://github.com/user-attachments/assets/4126d4bc-46f0-4430-8156-8d14460bc301)




![image](https://github.com/user-attachments/assets/d27a2795-64db-458f-9c00-ca07a2cbd21d)

![image](https://github.com/user-attachments/assets/cff33834-8bd9-4713-9682-416f504a9866)

  
 

![image](https://github.com/user-attachments/assets/2c4e5fd5-4002-4de6-b777-fbf5a4f61a65)
![image](https://github.com/user-attachments/assets/d145d1b3-5ce7-4f84-8105-a52b8c5d2dbc)
![image](https://github.com/user-attachments/assets/66bc540e-1a5d-42e7-8bad-a8a866a691b3)
![image](https://github.com/user-attachments/assets/716e44d5-a965-49ed-9829-3c967df7f6ea)
![image](https://github.com/user-attachments/assets/c0d5ba29-8b4d-49ba-81c7-d1d65dd91105)
![image](https://github.com/user-attachments/assets/df7b1d8c-c5cd-4966-99af-96680e50961e)


Small Language models:
======================

2 primary reason for small language models for performance.

1) training on domain specific dataset for e.g phi-1 is specifically trained for python code and
2) high quality data from internet , common crawl  or synthetically generated data from strong
   model like gpt-4 , llama-4.
3) Recently mistral released llm consist of 7 billion parameters outperforms llama model up to
   34 billion parameters across various benchmarks.

   ![image](https://github.com/user-attachments/assets/f53bf2fb-beca-4bf0-86b3-14ae73c33a3e)
