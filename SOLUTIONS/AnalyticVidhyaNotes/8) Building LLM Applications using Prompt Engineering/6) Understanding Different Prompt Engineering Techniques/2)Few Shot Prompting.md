Few Shot Prompting:
====================


![image](https://github.com/user-attachments/assets/7e6179e5-04fe-4b15-a711-8b5b2325350e)

  - refers to solving new set of tasks by providing a few set of examples or demonstrations in the prompt.
  - given the task description and lets say k no of examples, comprising questions and answers and the last
    examples with only the questions . the model generates the answers for the incomplete question.
  - here is the example of few shot prompting.

![image](https://github.com/user-attachments/assets/6c8823ed-3e5e-450c-90a0-7e81401c12f1)

  - as there are 3 examples which are provided for the model to learn about the task in the prompt.
  - the example clearly demonstrate how you need to structure the prompt for the few shot prompting.
    1) first step is to describe the task.
    2) second step is to provide with set of examples with input and output
    3) last step is the only input which is left for the prediction.
       
Few shot Prompting code:
=========================


  - how few shot prompting works .
 
Step 1: import library:
=======================

![image](https://github.com/user-attachments/assets/5f82958b-cb0f-4fb3-8c34-fb0deab8b78e)

Step 2: import library:
=======================

![image](https://github.com/user-attachments/assets/c25da7ab-666b-4efc-9df6-26a4bc035b2b)


Case study:
============

  - Med MCQA case study.
  - real world medical entrance exam.
  - it is hosted on hugging face (https://huggingface.co/datasets/openlifescienceai/medmcqa)

questions and generated answers:
====================================

 
 - system_prompt - > answers medical question and answers with medical knowledge

![image](https://github.com/user-attachments/assets/f979612b-c387-42b5-93fe-18b8a1c663c9)

![image](https://github.com/user-attachments/assets/f568163d-f4c0-4996-8cb9-a979630c5204)

![image](https://github.com/user-attachments/assets/c8c2f801-8604-4be3-afd0-14af1d9cd88b)

![image](https://github.com/user-attachments/assets/33076cf5-7dce-4bff-8e6c-fbd836d4994a)


it answers for the question using few shot prompting 

![image](https://github.com/user-attachments/assets/6299c3ae-421f-4e89-a08a-f976da187b78)



 
  
