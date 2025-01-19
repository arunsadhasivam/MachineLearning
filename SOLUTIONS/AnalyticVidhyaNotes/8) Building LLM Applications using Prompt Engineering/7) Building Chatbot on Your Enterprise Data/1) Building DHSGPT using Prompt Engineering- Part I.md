Building DHSGPT using Prompt Engineering- Part I:
=================================================

Chat bot on your enterprise data - knowledge not on chatGPT - end to end Project:
=================================================================================

  - we add more knowledge to chatgpt.


  Step 1: Setup Installation:
  ===========================

![image](https://github.com/user-attachments/assets/6383d0d0-97f6-4d57-a077-b9c28e21d92a)
![image](https://github.com/user-attachments/assets/37e71281-f383-40ca-bc91-451e32893a86)


Step 2: define model:
======================

![image](https://github.com/user-attachments/assets/ba1fdafc-e71c-4f4c-aa03-bf665df88b93)
![image](https://github.com/user-attachments/assets/17274d86-7843-454f-8fd7-2a4fdf7d7bce)

- it could not able to come with answer as this data is not available or not trained.
- analytic vidhya competition is not available so could not able to generate answer
- we provide now custom knowledge to chatGPT.

Step 3: Enable custom knowledge to ChatGPT:
============================================

![image](https://github.com/user-attachments/assets/b4739f36-ba21-4bea-bb4b-dd99985ed7f6)

  ![image](https://github.com/user-attachments/assets/266b9b8a-229d-494d-9386-803ecad8692f)

- here create a user prompt
- create a full prompt , saying that use this context as stored in the variable context
- **answer the question that user is prompting using the context.**

![image](https://github.com/user-attachments/assets/af332f3f-dd24-475a-ae1a-1c95bab9fd17)


- As you can see now it able to generate answer.

Step 4: create a new user function:
===================================

![image](https://github.com/user-attachments/assets/cd11adc4-e2e3-4139-b5a1-a61ba458b60c)

![image](https://github.com/user-attachments/assets/8edb9d5f-0662-41d6-8d63-095c88f71651)

 - now create a new function which takes user input **prompt** and **context**
 - if i ask why should i attend DHS 2023?
 - it was able to give me high level answer.
 - ask further info based on knowledge provided
![image](https://github.com/user-attachments/assets/a00947bd-eb18-4939-9899-7125712758f5)

 - it provides answer to all which is in knowledge 
 - lets ask anything which is not in context
 ![image](https://github.com/user-attachments/assets/5dfbbdb8-a342-47e3-b317-f7bb9a36fb7b)
 - date is not anounced since it is not given in "context" input data or trained context.

 - Add more context
![image](https://github.com/user-attachments/assets/30b52b12-fb33-4779-99ed-c7094bdfd150)

 - add more data to context by adding further details of the DHS summit like date of Summit
![image](https://github.com/user-attachments/assets/7660da57-2036-4ac6-986f-8a1dafc9abba)
![image](https://github.com/user-attachments/assets/f6d4013f-8650-46f0-8a5d-a551d13da5dd)

 - now you can see able to come up with answer.
![image](https://github.com/user-attachments/assets/8482cbbc-d178-4492-b088-e63a025c74f9)

 - not able to generate answers for the speakers
![image](https://github.com/user-attachments/assets/a63efbca-9537-451e-80f2-52a6260e4967)

 - adding speaker to context
![image](https://github.com/user-attachments/assets/96a28e78-f915-43a1-aa1c-2d92ddd92a1f)
 - now able to generate answer

![image](https://github.com/user-attachments/assets/e78b913d-b36c-4dfa-89b2-dc74ccb790d5)
![image](https://github.com/user-attachments/assets/3399258f-42d5-4d0d-b733-a300b8017a45)
![image](https://github.com/user-attachments/assets/c39de97b-b6ca-43ca-ba41-3919af938a94)


Step 5: Add Session:
=====================
![image](https://github.com/user-attachments/assets/6e50097f-73b3-408b-9009-05638fbf75df)

  - adding session.
![image](https://github.com/user-attachments/assets/053fb5ea-0040-4ce7-a098-1c62691c428d)

  - 
