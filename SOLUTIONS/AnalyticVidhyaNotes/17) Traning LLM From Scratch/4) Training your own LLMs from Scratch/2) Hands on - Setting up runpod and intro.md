Hands on - Setting up runpod and intro
======================================

    - setup runprod instance
    - followed by data curation , preprocessing of publicly available hugging face code repository
    - this will provide us with a domain specific  dataset.
    - after this train a new byte level , byte pair encoding tokenizer , then we will
      use the process dataset, BP-tokenizer and initialize the new 7B parameter model with
      random weights based on star coder arch.
    - we will use zero stage tree, i.e fully sharded data paralleism strategy for training our
      model on 8GPU.
    - here the task is of code completion , predicting the next token given the code or content so far.

1.Setup run pod:
=====================
    ![image](https://github.com/user-attachments/assets/721fc083-9b75-4b28-98da-6fd40aadf9c3)

      
![image](https://github.com/user-attachments/assets/d6bbd12e-753a-47ca-a793-dcbbed991af1)


![image](https://github.com/user-attachments/assets/34df3860-c44c-4204-8394-3bbca4fa2615)

you can see 200gb of storage using customized deployment option.

After pod setup

2.checkout code:
================


![image](https://github.com/user-attachments/assets/394a2b04-1b28-46a8-b0f4-17e13e72be42)


3.connect to runpod instance:
=============================

![image](https://github.com/user-attachments/assets/fbabbd02-9c81-4f56-8145-5727ff2f7301)

After click connect

![image](https://github.com/user-attachments/assets/8cd23b59-4f9e-47e4-a423-4d7147f1cff1)

![image](https://github.com/user-attachments/assets/b9d3a894-682f-4c59-98fb-965003b9c1eb)


go to workspace and terminal

![image](https://github.com/user-attachments/assets/d5b5ee13-1639-4331-9f0f-23c57a8a2f86)

go to new terminal go to repository and then install all requirement

![image](https://github.com/user-attachments/assets/d3692b59-a4d0-4aa7-bf3c-2ecffe87b81f)

