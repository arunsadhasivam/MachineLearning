Step 1: install langchain and other modules:
=============================================

![image](https://github.com/user-attachments/assets/253dde6a-1c5e-4f8e-8da3-8238ad93a3df)

Step 2: Setup OPEN Api Key:
=============================


![image](https://github.com/user-attachments/assets/db5f6a00-fbff-4d8c-8c0b-71ab01e9d551)


Step 3:Load Connect to LLM:
============================

![image](https://github.com/user-attachments/assets/cd7995c5-9280-45f8-99b8-fe962f9c3bda)



Step 4:create LangChain:
=========================

currently LLMChain in depreciated mode as in favor of LCEL(LangChain Expression Language) variant.
first import LLMChain and **use prompt Template and link to chatgpt LLM chain using LLMChain Construct** as below

![image](https://github.com/user-attachments/assets/eaaddf8c-026c-4eb9-bff7-cf568df1e936)

![image](https://github.com/user-attachments/assets/8b76abb7-a604-4c9f-8c6d-c779ec202e73)

step 5: invoke LLM:
===================

![image](https://github.com/user-attachments/assets/e157c4f9-39f1-402f-bd85-c7501500411b)


![image](https://github.com/user-attachments/assets/2235403b-82f9-4deb-99dc-c7380573cf0c)



step 6:print and format result:
================================

![image](https://github.com/user-attachments/assets/4b801095-2698-4e4c-8c45-0ee3ae7e8d1b)

![image](https://github.com/user-attachments/assets/4fa41559-cf82-4d0c-bfc0-bdb371c44c2d)

![image](https://github.com/user-attachments/assets/ff9fdff3-c23c-4f07-a51e-ebfdff296612)



<details><summary>2.Sequential CHain</summary>
<p>


 2.Sequential CHain:
====================


4 steps

Step 1: create a chain:
=======================

let say we have it support queue

![image](https://github.com/user-attachments/assets/90bc8d5f-c398-4818-8d72-a1c80f6de629)



Step 2: create a sequentialchain and LLMChain:
===============================================

- SequentialChain and multiple LLMChain.
- objective is individual chain takes care of specific subtasks and use LLMChain to merge the tasks.

  create a first chain with prompt template and customer message in place holder and language as
  key "output_key" for translation language in dictionary.

![image](https://github.com/user-attachments/assets/3b6a5740-4df1-4b43-ac80-bae5717bfc47)

prompt 2 chain and add prompt3  - generate resolution response in english.

![image](https://github.com/user-attachments/assets/bf9321dd-379a-4a30-8c9a-a36445821ef2)


![image](https://github.com/user-attachments/assets/d0dc3ee9-5096-42fe-a083-3f5d4a2f66e0)


prompt4

![image](https://github.com/user-attachments/assets/2266356d-469a-48f3-af90-98c8c7c27fd0)


Link all 4 chains:
==================

link all chains sequentially , provide input and outptut data (what want to see in response), 
verbose to true to see all intermediate results.


![image](https://github.com/user-attachments/assets/041acf50-3cd6-492b-891b-f28b49e851d7)


response with formatted:
=========================

![image](https://github.com/user-attachments/assets/e3dada75-5efe-494a-8323-42e130321c07)

run chain of all messages:
==========================

![image](https://github.com/user-attachments/assets/e7f25341-fcfd-4d67-82c7-4910cf3d058a)

one of the result:

![image](https://github.com/user-attachments/assets/08fca45b-453c-4776-8b93-4522631fe050)

formatted result:
==================

![image](https://github.com/user-attachments/assets/2863054d-39d9-4b7c-a315-8ef37d120877)

 </p>
</details> 




<details><summary>3.Others CHain</summary>
<p>

![image](https://github.com/user-attachments/assets/d568880f-5fcd-450e-94dd-b7a6737bd1f7)
 </p>
</details> 

