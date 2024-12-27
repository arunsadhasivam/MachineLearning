What do you mean by Training LLMs from Scratch?
================================================


![image](https://github.com/user-attachments/assets/dc3c45e7-7e63-4abd-89f1-fe6227173f2c)

 - build llm from scratch means build the base model.
 - gpt-3,llama2, phi2 refer to pre-training llm
 - base model are trained to predict the next word that is the training objective
 - this objective is known as CASUAL language modelling.

![image](https://github.com/user-attachments/assets/7f8555b9-ac9c-4353-9fc8-714bf4a0a446)

  - here you can see that based on all code before the cursor, the model is trying to generate
    what ever it follows it. i.e autocompleting or completing the code.
    this is called predict the next token.
  - it goes on predicting token by token in order to help us complete the code.
  - therefore these base llm are continuing text. for e.g given the text "hugging face"
    it completes the text by completing by completing the "renowed platform dedicated..."

![image](https://github.com/user-attachments/assets/03e2a15c-f3b5-49aa-9307-182585207f84)

  - these model capabilities of AI so on.

    ![image](https://github.com/user-attachments/assets/0f0d7f74-c433-4908-af20-6a27d6687cba)
  - these models contains **billions or trillions of parameters** and they are trained on massive internet
    scalled dataset consisting of **billions or trillions of tokens**. as a reason big challenge is compute.


  ![image](https://github.com/user-attachments/assets/5452bf7c-43de-475e-8949-c58f432cf966)
![image](https://github.com/user-attachments/assets/3aef93b6-71bd-4880-80de-2c488ddbcc96)
![image](https://github.com/user-attachments/assets/5c56562a-6d5d-4591-98f2-0a48954b7dc3)

   - These models are computationally very expensive.
   - it needs massive **gpu based computing power**
   - e.g llama2 70 billion parameters model was trained on **2 trillion tokens across 600 GPUS for 12 days**.
   - As a a result it involves millions of money inorder to train the large language models.
   - hence most often these llm are developed by organizations like google,meta, amazon,

![image](https://github.com/user-attachments/assets/f7baad08-aa70-4cb0-83b0-61d90d189df8)
    - hence most of enterprise organizations tend to develop small language models or fine tuned
      **base large language models** for the specific usecase to achieve better performance.
    - small language models are trained in few days across few no of gpus result in low cost
      compared to llm. e.g phi-1.5 models is trained across 32 A100 gpu 8 days.
    - given the cost should we train your llm or use google, meta , microsoft apis.
