Chain of Natural Language Inference:
====================================


![image](https://github.com/user-attachments/assets/cd8cd406-878d-44f4-891e-1ecfab1f71af)


  - chain of natural language inference is a method where llm is guided to follow a series a
    guide steps , is supported by given documents or background context aiming to reduce
    ungrounded hallunications by checking the accuracy of generated text.
  - breaking down the tasks to smaller manageable parts where the model uses the provided text
    to reason and conclude whether the claim is true or false or unsupported.
    enhancing the realibility of the generated context.
  - this prompting is particularly useful for improving the text quality by identifying and correcting
    the inacccuracies , making it a practical tool for applications that require high levels of factual
    consistency and reducing the risk of generating misleading information.


How it works:
=============

![image](https://github.com/user-attachments/assets/e959f79d-502d-413a-b432-0e52fa2c938d)

  - it works in 2 phases
  - 1) detection phases 
    2) mitigation phase
   
1.Detection phases:
====================

   - model first split the text to sentences and check each one to see if it is making things up
     or seeing something that does not match the information given.
   - it does by comparing sentences with  the source text and deciding if they are related,
     contradicting or not connected at all.

2.Mitigation Phase:
===================

    - after finding the sentences that dont match the source , the model uses the detection results
      as a guide to fix this sentences .
    - it try to keep the original format and make the text flowing either by removing or rewriting parts
      that were made up.


Example:
=========

![image](https://github.com/user-attachments/assets/cf1aa6d1-e4c5-4aee-bad2-26bb3a9e86f5)


    - raw responses produced by llm 
    - source text that we again use llm to detect hallunications.
    - reasoning which explain why particular sentences hallunicate.
    - based on reason , we use mitigation agent to refine the response.
    - in detection agent , we convert the raw response to individual sentences and then
      by using additional source we try to find whether it is hallunicated or not.
      
  Sentence level Detection:
  =========================
    - so here you can see each of the hypothesis ( hyp1,hyp2,hyp3) we can treat each of the hypothesis as a
      individual sentences.
    - and based on the additional sources we found that sentence2 is hallunicated . no hallunication in 
      sentence 1 and 3
![image](https://github.com/user-attachments/assets/97a8dd6b-0997-4052-9505-7f15aa69d7ef)

Entity level:
=============
    - then again we take or check hallunications at the entity level.
      then whichever sentences or entities are found to be hallunicated
      we pass them to the chain of thought reasoning process.
![image](https://github.com/user-attachments/assets/bbee5e62-af10-4fbe-b2bb-3ffd9037446b)

Chain of thoughts:
==================

![image](https://github.com/user-attachments/assets/a489ffde-b3b2-4992-8040-1da1f85bc891)

     - for e.g 2nd sentence it found out there is a hallunication in yellow.
     - as you can see the "premise mentions SNC instead of SPCA" which is a contradiction.
     - we use the reasoning further along with the source text and the mitigation instruction to
       correct the hallunicated output.
![image](https://github.com/user-attachments/assets/dade24a2-abdf-46db-9c63-8f4da7dd6272)
      - As you can see the answer contains SNC instead of original SPCA

![image](https://github.com/user-attachments/assets/61fee582-2dcd-4f87-9601-e8247406a330)


Disadvantages:
===============

![image](https://github.com/user-attachments/assets/9529981b-6d07-477e-b3e0-20f8528a17ad)
