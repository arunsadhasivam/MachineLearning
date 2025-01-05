Self Consistency:
==================

![image](https://github.com/user-attachments/assets/b468e6fb-9cdc-4a68-b92d-9af9b2c3455f)

- self consistency prompting is a prompting method which solves the complex problems by
  considering multiple ways to think about a problem.

How does work?:
===============

  ![image](https://github.com/user-attachments/assets/4dbbf095-1bfa-45fd-a1fb-0df93b23c632)
![image](https://github.com/user-attachments/assets/727db002-1bb7-478b-b08a-52222a9a48ca)

  - 1)it generates multiple reasoning path
    2) and it evaluates the various reasoning paths
    3) and choose most recurring outcome
  - it surpass traditional greedy decoding by avoiding pitfalls like repetition and local-optimality issues.


  Self consistency Prompting : example:
  =====================================

![image](https://github.com/user-attachments/assets/0773c784-7004-4cd5-b015-e5856b282d83)

  - here is the eg of self consistency prompting.
  - here  we pass prompt by passing Q & A pair
  - then we ask Question is the user input and ask the language model for answer.

  - janet ducks lay 16 eggs per day. she eats 3 for breakfast , 4 for friends .
    she sells $2 per egg. how much she makes everyday.

chain of thougths output:
==========================

  - if you use chain of thought prompting which uses internally greedy decoding techniques and
    it answers 14.

Self -consisitency output:
==========================

  - if it uses self-consistency prompting which it reasons 3 different ways and it takes
    the majority vote answer which is 18.


Advantages:
===========    
  - this approach makes the language model answer more reliably by checking in many ways
    which inturns gives us some confident in model generating output.
  - also tells us how sure the program is about which is helpful.
  - this is a simple method and does not create extra training and effort

![image](https://github.com/user-attachments/assets/ce31b485-ca3d-4001-86e0-1163633d3385)

Disadvantages:
==============

  - some of the disadvantages of this approach is that it evaluates multiple solutions which requires
    more processing power and also it sometimes generate non-sense or in-accurate answer.
  - provide better results than some method , but not guarantee correctness.

CODE:
=====

1.Setting the env by importing required packages:
==================================================

![image](https://github.com/user-attachments/assets/dc959c1e-e154-4493-a906-48399c5da1e5)

2.set open_api_key:
===================

![image](https://github.com/user-attachments/assets/f01710ac-0bfb-4017-9a37-a139bceb4974)


3.Prompting:
=============

![image](https://github.com/user-attachments/assets/801c6832-bd6b-4480-80e7-6d8664bb9998)


4.pipeline:
============

![image](https://github.com/user-attachments/assets/a602a144-8490-47bb-9083-085ecac2f93e)

5.generate structured response :
================================

 ![image](https://github.com/user-attachments/assets/187c0384-06a8-483e-89e1-5d44fc9ad358)
![image](https://github.com/user-attachments/assets/59df9e0c-81fb-47e0-a6ee-503a5fbc3cd6)


- we have tempature of  0.1, the thought process also change.

6.generate final response:
===========================

![image](https://github.com/user-attachments/assets/4a03e3d2-33f4-4eed-aa97-1939d902bf50)
![image](https://github.com/user-attachments/assets/aa092d5d-7b9a-45b8-9f8e-4e87fe6fd7bc)


- final answer will be majority vote
