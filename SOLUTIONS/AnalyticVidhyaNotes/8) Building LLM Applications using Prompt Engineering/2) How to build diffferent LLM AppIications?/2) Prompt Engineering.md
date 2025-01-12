Prompt Engineering:
===================

- one of the simplest and most commonly used method to build llm application.
- in this lesson , we explore the concepts of prompt engineering and why it is such
  an important concept.
- before understanding what is prompt engineering ,understand prompt.

Prompt:
=======

![image](https://github.com/user-attachments/assets/d8ec6ae0-a0ce-458d-9716-ab445ac0e9e4)

![image](https://github.com/user-attachments/assets/5888d3ec-4b7f-4c1d-b975-b34cc202e6ed)

  - we know llm have been trained on massive dataset and are capable of following instruction
    from user.
  - it gains the knowledge of the events, fact or any other information present in training data.
  - we can access the knowledge present in the llm through prompts.
![image](https://github.com/user-attachments/assets/12fe4e2b-74ad-4e62-a49b-08494735f6ed)

  - prompt is a text given to the llm as an input for getting the desired output.
  - prompt is like telling the llm what you want to do and answer for you.
  - simply enter what you looking for and llm will provide the information that you need.
  - get powerful output by just simple prompt.

  why prompt Engineering:
  =======================

     - before understand why prompt engg, understand why we need.
     - most of the llm gives the correct output for the input prompt.
     - sometimes it fails to provide you the correct output, and go wrong.
     - for e.g they are not very good at multiplying numbers, often give incorrect answer like e.g multiplication of numbers.
![image](https://github.com/user-attachments/assets/5eed3157-1879-4143-ac0e-474b07cbb5f9)

     - for e.g simple math question 923*999 as you can see wrong answer.
![image](https://github.com/user-attachments/assets/79c215d9-6604-473b-b35f-ce752e141e2c)

     - so change the prompt " always write out the full number of o's" gives correct answer as you can see above.
![image](https://github.com/user-attachments/assets/8fcca462-73f8-4dcc-8289-92907b761d25)

     - prompt engineering helps us to improve the accuracy of our output and also helps us to achieve the
       desired and specific output.

![image](https://github.com/user-attachments/assets/fb310cc9-049c-4e9c-bd17-baa409fad019)

Definition:
===========

  - prompt engineering is the process of refining the prompt over iteration to get the optimal outputs.
  - prompt engineering is all about iterative way to improve the prompt.
  - it's about how to rewrite the prompt to get better results and exploring the different ways
    to achieve the required output.

![image](https://github.com/user-attachments/assets/239ba74e-e547-4d05-b0ce-235653c00d4b)

![image](https://github.com/user-attachments/assets/0f4b5fd9-f955-48f1-8f9e-424e22e04c3e)

![image](https://github.com/user-attachments/assets/1b9afc7b-ab0e-4cd4-8d0b-dd40aa97d2fa)

  - it is an iterative process, 
      1)where you write a prompt , 
      2) see the results, 
      3) rewrite the prompt again to get desired results,
      4) this process continue
   
  - mastering prompt engineering comes with extensive practices and experience with these llm.
  - there are some best practices to write effective prompt and method for prompt engineering.
  - that will be focus on rest of the course.

How to build llm applications using prompt engg?
================================================

![image](https://github.com/user-attachments/assets/72397819-ece7-42a1-82d5-d4dbf0e82b6b)

  - build llm applications you need to have access to 2 things.
      1) pretrained llm
      2) right prompts with required information/context.


Pros:
=====
![image](https://github.com/user-attachments/assets/b00f3513-e89b-4408-8d9c-802fad22bfe9)

  - simplest and easiest way to build llm.
  - as it does not know technical knowledge or coding.
  - no model training.
  - this means you dont need to worry about training data.
  - no need to worry about computing resources.
  - it is cost effective and efficient approach.
  - when using enterprise llm  api such as openAI, claude.ai, they charge based on no of prompt.
  - if you opt for open source llm, you need to host on cloud and access it through your api incurring cloud
    for deployment and maintenance.in this case , you need to afford the cloud cost
    of deploying and maintain llm.
    
   
CONS:
=====
![image](https://github.com/user-attachments/assets/aae7e4e8-851b-46bc-b129-e5c8872c29f0)

    - inconsistent with their output , no guarantee of output always.
    - hallunication.
    - hallunication one of the fundamental problem with llm.
    - they make up if they dont know the answer.
    - very less information fits in , because chatgpt has restriction on no of input tokens up to 4096
    - it can accept only these no of token in single prompt, if prompt exceeds more than inuput length 4096 , throws error.
    - you want to provide more information in single prompt for these llm, but this is not possible because of 4096 token limitations.
    - not up to date.
    
    
