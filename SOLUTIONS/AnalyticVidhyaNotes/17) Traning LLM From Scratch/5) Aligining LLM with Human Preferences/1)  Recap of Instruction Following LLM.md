
Recap of Instruction Following LLM:
===================================

1)why instruction following LLM?:
=================================

![image](https://github.com/user-attachments/assets/6154ce2f-df81-455c-8bed-934c92247cc2)

![image](https://github.com/user-attachments/assets/0430fd79-286f-4956-b983-c78149d2f7a3)

  - previous lesson how to train own llm from scratch.
  - trained base llm.
  - base llm are good at continuing text as these llm are optimized for text completion.
  - capable of doing most of NLP tasks through task formulation
  - for e.g given input translate following to hindi, if givent to base llm, it response in hindi
  - base language models cant guarantee the desired user response.
![image](https://github.com/user-attachments/assets/6f35b41f-364d-4ef0-825a-07c63303d559)
  - **cant gurantee the user response in a answer format that user expecting**.
  - for e.g a question "what are llms?" to the base llm -> it returns
    1) answer 1- llms are language models  trained on massive data
    2) answer 2 - it might ask further clarification questions like? what are different types of llms?

  - this happens , because it has gone through several such patterns during training process.
  - this we already looked at the finetuning llm course.
  - this bring us to instruction following llm.

Instruction Following llm:
===========================

  - good at following instructions i.e able to provide responses that the user is looking for.

    ![image](https://github.com/user-attachments/assets/63a1b5ed-e63b-42ff-a9bc-d63e591a9512)

  - when the above save questions are asked "what is llm?" - it responses with the llms are language models  trained on massive data
  - it response with appropriate answer.
  - it fulfill the requirements of the user
![image](https://github.com/user-attachments/assets/5e966c8f-3ceb-4528-bde8-eba217571ec7)

  - **instruction following llm is the result of finetuning the base or pretrained llm on instruction response pair
    this process is known as supervised fine tuning and the model that results from this is known as SFT Model**.
  - Lets quickly take the steps in developing SFT Model.
  - SFT Model has 4 steps:
    1) Data Collection
    2) Data preprocessing.
    3) Model training
    4) Evaluation.
    



