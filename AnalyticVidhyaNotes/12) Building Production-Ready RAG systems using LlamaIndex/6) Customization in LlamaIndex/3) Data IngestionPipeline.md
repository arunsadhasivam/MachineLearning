Data Ingestion Pipeline:
========================


![image](https://github.com/user-attachments/assets/631e8314-7858-4189-93f7-f66b04e6b86c)


- Ingestion pipeline you can have custom transformations
- caching options available in LlamaIndex


Step 1 - Environment:
=====================

![image](https://github.com/user-attachments/assets/629d9a77-388b-469b-849c-ad444d235f7d)



Step 2 - Download Data:
========================

![image](https://github.com/user-attachments/assets/51a5070b-1989-4673-b7ec-dfddeb42516f)




Step 3 - Load Data:
======================

![image](https://github.com/user-attachments/assets/851b23a6-cb35-47ab-bd0e-73237b20867f)


<p><details><summary>1.Ingestion Pipeline easily ingest data</summary>


Step 4 - Ingestion Pipeline easily ingest data:
================================================

- new concept of transformations  that are applied to input data
- Transformations can be
  
  ![image](https://github.com/user-attachments/assets/266fcb22-560f-40b1-a3d9-5e2c104b495c)

![image](https://github.com/user-attachments/assets/58f8cba6-07c4-4adb-a1b0-3f34cf70800f)
![image](https://github.com/user-attachments/assets/fd089b31-e0ef-4b92-9b59-c18f81296b50)
![image](https://github.com/user-attachments/assets/05053330-b987-4bea-9243-c060d3e72eb5)

![image](https://github.com/user-attachments/assets/883523ec-b54c-48f2-a701-8fa228114697)

![image](https://github.com/user-attachments/assets/f821d00d-51df-4e7b-9204-702d6d7d43fc)


![image](https://github.com/user-attachments/assets/10958461-29a7-4458-b8dd-cf4a1cd4248d)


document title

![image](https://github.com/user-attachments/assets/a0789052-a5c4-4a05-84fc-f73a88195fe0)


no embeddings

![image](https://github.com/user-attachments/assets/b41b6bd8-8c45-4d98-bbaf-e6593c3ba2ac)


Add embeddings, include embeddings in same pipeline. specify which embedding model to use.

entire document will have 3 transformations
1) first Node will be created
2) Title will be extracted for the Document.
3) Embeddings for each node will be created.

![image](https://github.com/user-attachments/assets/27da6acc-d4c1-4999-af2a-7aca353d8154)

</details> 
</p>


<p><details><summary>2. Transformation Caching</summary>

- caching capabilities in to our ingestion pipeline.
- idea is can we store previous ingested pipeline in to our cache memory
  any steps which is already executed by ingestion pipeline will not executed again.
- it not only saves memory but also reduce unnecessary api calls.
- any repeated steps which is already executed by ingestion pipeline will not execute again.
- e.g if you have already generated embeddings, if you run ingestion pipeline so embeddings
  wont generate again.

  ![image](https://github.com/user-attachments/assets/a41a784c-11af-4e15-819e-90fb2817d032)

  added extra parameter cache.

  next time run for same document ,it run instantly
  ==================================================


  ![image](https://github.com/user-attachments/assets/672e1afa-e869-49a8-ab79-b9a601aa727c)

 


Again persist cache with embeddings also to persist

![image](https://github.com/user-attachments/assets/b67a04fe-91c4-4ea7-9ac6-3d1e74cf5855)


if again run none of the 3 steps will not executed since all 3 already executed.

it just loads and map to pipeline.


</details> 
</p>


<p><details><summary>3. Custom Transformation</summary>

Remove special characters

![image](https://github.com/user-attachments/assets/23405ca9-d6a4-41a0-bccd-e7b6bb454db4)

</details> 
</p>

 
<p><details><summary>4. Tokenization and token counting for Prompting, Embedding and Response Generation</summary>

![image](https://github.com/user-attachments/assets/11b5c5d2-a735-475f-84aa-c69d5b2a6242)

callback manager handle callback for llamaindex
![image](https://github.com/user-attachments/assets/67c5833f-6f61-4772-95b0-87c6bea2adc4)


PromptToken - 1893 is high that include context from nodes 
</details> 
</p>
