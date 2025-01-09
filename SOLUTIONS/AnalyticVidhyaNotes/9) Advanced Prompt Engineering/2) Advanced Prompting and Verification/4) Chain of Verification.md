![image](https://github.com/user-attachments/assets/fb6a9294-5c9c-4911-87d2-2f66314a3868)Chain of Verification:
=======================


![image](https://github.com/user-attachments/assets/40183e85-3fb1-4ff1-aac7-53d4878454eb)


    - chain of verification is a technique where language model  first create a draft response to a user query.
      and then generates and answer verifications questions to check its own work before finalizing the
      answer.
    - Aiming to reduce the mistakes and improving accuracy.
    - chain of verification is designed to decrease the generation of plausible yet incorrect information, which is
      also known as hallunications.
    - By allowing the model to self analyze and correct the initial response through a structured step by step approach.

How it works:
==============
![image](https://github.com/user-attachments/assets/cc013b71-6b19-431b-a1a6-fb603f7c0ee5)

  - it works in 4 stages.

first stage:
============

    - model first creates a initial answer for a question which is like a rough draft of what it think is correct.
    - next it comes up with questions,that can help to check if the first answer was right or wrong ?.
    - this is like making a list of things to double check and then on to the answers each of those double check questions one by one
      E.g like we do in certification questions. revist bookmark for few questions
      and revisit before submit the exam.
     - This step helps the llm to figure out if it makes any mistake in the first answer.
     - finally, from what we learned from double checking , the model updates and correct its first answer to make it more accurate.

Example:
========

    - user asks a question "name some politician who were born in new york"
    - then the language model creates a base line response. it says here are some politician who were born in newyork
      1. clinton
      2.trump
      3.michael

Second stage:
=============

    - in the second stage this prompting techniques , plan some verification question like where was clinton, trump born.
    - then it executes those verification, and gets its answer.
    - for e.g clinton was born in chicago, trump in newyork.
    - based on this , finally it generates the response.
    - it generates like here are the politician born in NY like trump.
    - so in this way, reduce hallunications in language model generation.
    - generated output has less hallunications.

Disadvantages:
==============

    - reduce but not entirely prevent incorrect output or hallunications.
    - it correct actual responses more than subtle reasoning.
    - it adds clarity but at a high computation cost due to increased output length.
    - its effectively is constrained by models inherent capabilities such as identifying and knowing what it knows.
  ![image](https://github.com/user-attachments/assets/5d094e99-28ec-4f9f-b8d0-5ac128a6afe6)


Code:
=======

Step 1:load env and libraries:
================================

![image](https://github.com/user-attachments/assets/bee84549-c472-4e49-858c-3c44511319d7)


![image](https://github.com/user-attachments/assets/8971d703-58aa-4bb6-b232-5f15df5fcce3)


 - os package for manipulating files and libraries.
 - different prompt templates
 - runnable pass through and runnable lambda for defining runnable object that execute lambda functions.

![image](https://github.com/user-attachments/assets/3e645774-36a8-472d-95cd-79d5a540a8c4)

step 2: Setting up llm:
=======================

![image](https://github.com/user-attachments/assets/ae8601ca-8e84-4773-9136-02748335c058)

  - set up language model by setting up open-ai api key.
  - initialize language model with temperature parameter of 0.


Step 3: Implementing chain of thought:
=======================================


![image](https://github.com/user-attachments/assets/6089139d-55a5-4580-bcb9-8fdad714d5db)


Stages:
=======
1) Baseline Response stage. - **generate inital answers**
2) Verification question generation stage -  **question template for the verification stage**
3) verification question execution stage - **verification question execution stage.**
4) final Refined response -**once define these  3 stages , then move on to define verification chain and then we also
   set up the final response stage .**

   ![image](https://github.com/user-attachments/assets/e5061645-4400-48f6-acdc-cf40a4278407)

set up the final response stage using the base code.
![image](https://github.com/user-attachments/assets/30fc1e8f-2487-4bc5-a0ab-08d9e42f1aab)

finally assembled all the chain that integrates the various components  where we include the
1) baseline response generation.
2) verification question template creation via a **dedicated chain**
3) generation of verification questions through **another specialized chain**
4) processing verification of answers **with in a verificatino chain**'
5) finallizing the answer generation process  with a **final answer chain**

   ![image](https://github.com/user-attachments/assets/5ac68187-74b6-46d2-b650-94ac495e9509)

Step3 : Respnose generation
==============================

    - once the response are generated it goes to these 4 different stages.
    - question "is narendra modi born in delhi"
    - we get response -base line response
      1) Narendra modi
      2) delhi.
    - then we create verification question - was narendra modi born in delhi.
    - we get the verification answer , we get narendra modi no narendra modi not born in delhi.
    ![image](https://github.com/user-attachments/assets/af449bcb-b3b9-40f5-b983-2eab9743369a)
