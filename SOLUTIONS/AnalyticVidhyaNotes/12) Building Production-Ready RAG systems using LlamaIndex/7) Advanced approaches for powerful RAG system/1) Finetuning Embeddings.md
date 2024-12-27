Fine Tune Embeddings:
======================

- embeddings plays a vital role in the retrieval stage.
- we use embeddings of the chunks and user query to fetch relevant chunks.
- hence representing the chunks in to right representations is key to RAG performance.


  ![image](https://github.com/user-attachments/assets/aa92def9-079d-4aae-a72d-045552e6d852)


<p><details> <summary>1.Why Finetuning Embeddings</summary>
  
why Finetuning Embeddings:
==========================

 - general Embeddings : general purpose embeddings
 - Domain Specific Embeddings: capture business context of the business domain so
   it improves the representations of the CHunk and improves the RAG.
   

What is FineTuning Embeddings:
===================================

- Taking the PreTraining the embedding model and training on our data with changes.


![image](https://github.com/user-attachments/assets/d646ab21-0c31-491b-b27f-85abdc3f7bfc)

![image](https://github.com/user-attachments/assets/41afc356-fd9d-4967-afdc-ce65f56da3bd)



</details></p>


<p><details> <summary>2. Finetuning Embeddings Code</summary>

  FineTuneing Embeddings Code:
  =============================

  Step 1: Environment:
  ====================

  ![image](https://github.com/user-attachments/assets/99394dc1-b13a-42ac-b05a-c66dcaf4d74d)

  Step 2: Generate Corpus:
  ========================

  ![image](https://github.com/user-attachments/assets/319672a7-7035-4f93-8efa-0a31d2e564dc)

  ![image](https://github.com/user-attachments/assets/b63b5ea0-0d7b-4ce2-bf81-b9ee7d4ff8b7)


  load corpus
  ![image](https://github.com/user-attachments/assets/78269ada-f2fe-48b9-9e23-bbb8a8945aad)

  create training and validation nodes
  ![image](https://github.com/user-attachments/assets/e9689497-8e96-474e-a86a-dcf5e77eeacd)

  Generate Synthetic queries

  ![image](https://github.com/user-attachments/assets/fef8d85d-e422-4ee5-bdd6-b633d43f6359)

  ![image](https://github.com/user-attachments/assets/96bc0cfc-8d30-4ad4-aedf-16a349a7eb97)

 
  Run Embedding FineTuning:
  ==========================
  
  ![image](https://github.com/user-attachments/assets/36b75aec-53e9-4d7a-bd5a-c2c7079481fd)


  finetuning step will very fast in gpu , else if you use cpu it will be very very slow.
  ![image](https://github.com/user-attachments/assets/8d578393-cbf7-4180-8b3a-39324e5fc9d6)


</details></p>

<p><details> <summary>3.Evaluate Finetuned Model</summary>
  
Evaluate Finetuned Model
========================

  ![image](https://github.com/user-attachments/assets/7abb762f-c8c5-4e1b-a7d4-93d6ba0072af)

  ![image](https://github.com/user-attachments/assets/f9738f72-6b60-4354-a040-3fbc6e5cedd0)

  ![image](https://github.com/user-attachments/assets/9ea7c991-a5f1-4498-8f6c-ef30faff219f)
  ![image](https://github.com/user-attachments/assets/434cfd18-8ad4-44d2-92c8-6cbbcb1b5263)



  
</details></p>

<p><details> <summary>4.Run Evals on Model</summary>

Run Eval on first openAI Embeddings.
 ![image](https://github.com/user-attachments/assets/b5ab4adb-4a47-4488-8dae-a525d1ff2098)


Run similar evals on bge-small and finetuned version and compare results.
 ![image](https://github.com/user-attachments/assets/2c208753-51ef-470f-b785-71e737554ab5)
 ![image](https://github.com/user-attachments/assets/21dee36f-3e5b-4643-b050-5f2c053359da)


Eval on fine Tuned BAAI/BGE
 ![image](https://github.com/user-attachments/assets/a233510f-b48c-4b51-b57a-606d3ca74330)

  As you can see fine tuned model has higher performance (0.86)
  
Summary of the results

  Hit rate
  
 ![image](https://github.com/user-attachments/assets/ac7093bb-3987-4b77-8c3f-4291096144a8)
 

</details></p>


<p><details> <summary>5.Build Index and search for answers - Response</summary>

  ![image](https://github.com/user-attachments/assets/35a40160-3118-4f1e-acf1-014e19a37aa4)
 
  ![image](https://github.com/user-attachments/assets/283e7222-09f9-486d-a149-68cdc0c2faba)

  ![image](https://github.com/user-attachments/assets/ec015495-8fea-4ff9-b37e-2adf69a9de01)


</details></p>
