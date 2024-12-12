Correctness:
============


- Accuracy of the responses to the actual response.


E.g:
====

![image](https://github.com/user-attachments/assets/ba7ea676-f763-4863-b0ed-6b78360a7edc)


here it outlines the growth of uber.

user query:
===========

revenue of uber in 2021.

![image](https://github.com/user-attachments/assets/9a0ea9b3-5f74-40f9-a783-6b7d8eab7b30)

as the above the answer is incorrect.

Correctness Evaluator:
=========================


![image](https://github.com/user-attachments/assets/a8a990d4-ea92-41cf-9551-60619013fbe3)


Calculating the Correctness score:
==================================


 - Answer correctness measures accuracy of the generated answer when compared to the ground truth.
![image](https://github.com/user-attachments/assets/e943c170-65bf-4653-87d7-af112db8c9b5)

<p>
<details><summary>1) Factual Correctness</summary> 

1)Factual Correctness
=======================

- Factual correctness quantifies the factual overlap between the generated answer and ground truth answer.
  ![image](https://github.com/user-attachments/assets/881ab4b8-1714-4e1e-8059-e0c198f78a8e)


![image](https://github.com/user-attachments/assets/d8d27271-fb9a-44eb-9509-f8bcdee0c835)


- here high correctness is 1879 germany
- low correctness answer is Einstein spain 1879
- we calculate F1 score based on the formula
    **F1 = |TP|/(|TP|+ (0.5x (|FP| +|FN|)))**

</details>
</p>


<p>
<details><summary>2) Semantic Correctness</summary> 

**Ground Truth:** Alber einstein  theory of relativity revolutioned our understanding of universe"
**high similarity answer:** einstein ground breaking theory of relativity transformed our compreshension of 
cosmos.
**Low similarity answer:** Isaac Newton's laws of motion greatly influenced classical physics.

step 1 : vectorize **ground truth answer** using an embedding model.
step 2 : vectorize **the generated answer** using embedded model.
step 3 : compare **cosine similarity** between 2 vectors above


This evaluation is based on ground truth and answer , with values on range(0 to 1).
- facts are correct but way answer presented also should be correct.

  ![image](https://github.com/user-attachments/assets/e6cc5d7a-5931-431a-b577-353c44ee0c71)
  ![image](https://github.com/user-attachments/assets/8ba4c639-8e52-4c17-8b24-7a098bd944c4)

Calculate Answer correctness:
==============================

if we have **Factual correctness score** and **Semantic Similarity** we can calculate the 
answer correctness.

![image](https://github.com/user-attachments/assets/335bb583-2234-49d0-97bd-1dd16b93a17f)


Factors improve correctness:
==============================

![image](https://github.com/user-attachments/assets/49cefa77-1f15-4f8a-9984-446b7d16f01d)

 
</details>
</p>
