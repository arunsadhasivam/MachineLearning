
Overview:
=========

![image](https://github.com/user-attachments/assets/90118c7c-271c-451a-b7cc-0582868b514b)


prerequisite 1:install library and setup env:
==============================================


![image](https://github.com/user-attachments/assets/d68a6afc-bce9-4854-9db8-fcff26b8f8bf)

env files
==========

![image](https://github.com/user-attachments/assets/71c7ae11-f03b-4863-b813-2c0828ced82f)

prerequisite 2: load env files api key:
================================

![image](https://github.com/user-attachments/assets/085883de-8a4c-40f1-987f-cab76fd10867)


Step 1-Data Ingestion:
======================

![image](https://github.com/user-attachments/assets/49a7198e-4e7d-4647-8e36-8c2dcb70c115)
![image](https://github.com/user-attachments/assets/8eef2d5b-2cb1-4268-a8b0-51b5e1e05e91)




![image](https://github.com/user-attachments/assets/8af20c5f-3d96-4d78-846a-8fbffbc92376)


Note:
=====

As you can see both documents[0].id_ and documents[0].doc_id returns id of first document.

metadata

![image](https://github.com/user-attachments/assets/d79825cf-c69d-4f67-80f1-3b4e552df216)

to get text content of document.

![image](https://github.com/user-attachments/assets/f0a05367-143c-4190-810e-57273cdea410)

  
  Step 1.1-Embedding Model:
  =======================
  
  you can use either large or small
  
  ![image](https://github.com/user-attachments/assets/50dbe63f-e134-4fe6-8916-9c96165d4582)
  
  Step1.2 - LLM
  =============
  
  ![image](https://github.com/user-attachments/assets/a94574fe-9dc7-4112-b67f-8684f8e67e56)

Step2 - Indexing:
==================

gpt-4 or turbo

![image](https://github.com/user-attachments/assets/646fa4c2-bf56-49a1-9bb0-5d39f4bf556a)

Step3 -Retrieval:
==================

set index as retriever. 

method **index.as_retriever()** converts **index** to **retriever** and **retriever() methods allows to query index**.


![image](https://github.com/user-attachments/assets/81c7fe9d-9226-4f02-b805-fb0a359d5689)

![image](https://github.com/user-attachments/assets/e016ed11-9043-4891-bd60-69cd201a5c9f)


Step 4- Response Synthesizer:
=============================

![image](https://github.com/user-attachments/assets/5ded0650-5c41-4c63-8d1f-9d70844eb417)

