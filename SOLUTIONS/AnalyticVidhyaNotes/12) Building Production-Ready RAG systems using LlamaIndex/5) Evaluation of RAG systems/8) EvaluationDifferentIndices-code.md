Evaluation Different Indices - Rag Pipeline:
==============================================


Step-1:Setup-Environment:
==========================

![image](https://github.com/user-attachments/assets/0a68fc5e-7fb9-44bc-89b7-7a4682031e6d)



Step-2:download:
==========================


Reference answer - stored in  evaluation answer and questions in evaluation queries

![image](https://github.com/user-attachments/assets/40a10e94-50ab-4da7-8a5d-226ec4dfdcf6)
![image](https://github.com/user-attachments/assets/d9a65dbd-96c6-4e54-a31a-8882894f46f4)
![image](https://github.com/user-attachments/assets/0289afd3-3cfa-4644-b85e-95c9d6bcc0cc)


Step-3 :LLM:
============

use hugging face
![image](https://github.com/user-attachments/assets/7d67a400-4ca2-446e-89d0-796f4ed3987b)



Step-4 :Embeeding Model:
=========================


- used small embedding , give vector length of 384.

  ![image](https://github.com/user-attachments/assets/fda04550-663d-4fb9-8ad1-41cf8b398222)

Step-5: build Vector Store index:
=================================

- use vector store index, create query Engine.

![image](https://github.com/user-attachments/assets/8daa2924-c342-4046-b936-cd91b1c2df22)


Step-6: Build Keyword Table Index:
=====================================


simple keyword table index and convert to query Engine like vectorIndex

![image](https://github.com/user-attachments/assets/caa5961d-3eea-483d-ad17-09c9876e786a)



Step-7: Download RagEvaluator Pack:
=====================================


- Assign rag dataset to Rag Evaluator pack
- Evaluate vector store index.
- one by one pass the vector_store_query_engine to evaluator _pack

![image](https://github.com/user-attachments/assets/ccc6088f-76cd-4add-b7d2-bc4f7df74e96)

![image](https://github.com/user-attachments/assets/d3283bc1-4bcc-4920-bbc8-5efacd20940f)

vector benchmark score
=======================

![image](https://github.com/user-attachments/assets/e9288980-223e-488a-9c44-3293eccb5346)



similary keyword table index

![image](https://github.com/user-attachments/assets/b242441f-8db0-4f84-82ca-546e6ebd8dc1)

![image](https://github.com/user-attachments/assets/e3ffb721-18cf-49ac-a7db-e5e8036f52fa)

![image](https://github.com/user-attachments/assets/69841e03-e440-4c38-9539-d9a60f49e24d)
