Skeleton of Thoughts:
=====================

![image](https://github.com/user-attachments/assets/643788b8-8281-4ac8-bb79-7b1fe57da12f)

  - **outlines the answers first**, and then files in **details in parallel,speeding up the response**.
  - this approach is inspired by **how humans think** and write.
  - where we often **outline the thought before eloborating on them**, allowing for a more organized
    and efficient way to generate answers.

How does it work:
===================

![image](https://github.com/user-attachments/assets/16042d6f-72ac-484c-a193-3d931a77e26a)
![image](https://github.com/user-attachments/assets/05b1848c-8b4b-423b-9ea4-99b3b4728bfa)


  - this prompting techniques involves 2 main stages:
  - how it works - " question - what are effective strategies for conflict resolution in workplace?"
    Answer - 1. active listening
             2. identify issues
             3. compromise.
  - first stage is skeleton stage, where we only define the outline.

Normal decoding:
=================

![image](https://github.com/user-attachments/assets/1b415d2c-7825-4105-8191-cd6b673f3341)

    - for a question generate answers sequentially.
    
Stage 1:Skeleton stage:
========================

  - where you can see above (1. active listening, 2. identify issues 3.compromise) are the 3 outlines

Stage 2: Point expanding:
==========================
  - then in the  second stage Point expanding stage we generate answers in parallel not sequential
  - thats why this method is very fast compare to normal decoding methods.
    
    
Skeleton of thoughts example:
==============================

![image](https://github.com/user-attachments/assets/30e4bd64-0745-4ef2-94d3-0973f97845ac)

  - allow let user to generate a question to generate the skeleton 
  - for e.g you are an organization responsible for only giving skelton  ( not full content)
  - instead of writing full sentence, each skeleton point should be short.

example 2:
==========

  - question : making a cake
  - skeleton : step 1: collect ingredients
               step 2: mix dry ingredients
               step 3: add met ingredients
               step 4: baking oven and so on
  - in this stage we have created a skeleton , and not generated answer in detail.
  - answer generation happen in stage 2  : **point expanding prompt template**
  - in the point expanding prompt template the user asked a question that you are responsible
    for continuing the writing of one and only one point the overall answer to the following question.
  - we pass the question and then we pass the skeleton from prommpt one.
  - and then we write , continue and only continue the writing of point  point index.
  - write it ver shortly in 1 or 2 sentences and do not  continue to answer points
  - **so using this prompt 2 we generate the answers for each of the skeleton points in parallel.**

Disadvantages:
==============

![image](https://github.com/user-attachments/assets/12602a8a-171b-4b1c-b95d-a80330664ebe)
