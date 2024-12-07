
<p>
<details> <summary> 1. Embeedings</summary>

Embeddings:
===========

- text converted to chunks.
- but machine understands only numeric so convert to **numerical vector**  text to vector embeddings.
- convert textual chunks to numerical representations which are then stored in vector store index.
- these **numerical representations of text chunk are vector embeedings**. they encapsulate the
  meaning and context of the text.
- during the query and retrieval state , the user query which is usually in form of text should
  also be converted to embeddings to retrieve topk chunks by retrieval engine.
- in synthesis stage llm returns response based on top-k retrieved documents and user query.

</details>
</p>


<p>
<details> <summary> 2)Why we need Embeddings?</summary>
  
1)Why we need Embeddings?
============================

![image](https://github.com/user-attachments/assets/5e9fb1b5-661b-4abe-8a32-e75c426d2614)

Definition:
===========

- Embeddings are text data in numerical format.
- They capture semantic relationship in language
- 

![image](https://github.com/user-attachments/assets/0cbc7c99-6ec9-414d-84be-74fb1788a9ef)



</details>
</p>


<p>
<details> <summary> 3)Interpreting Embeddings</summary>

Interpreting Embeddings:
=========================

numerator - dotproduct of 2 vector/mod of ||a||.||b||

1) cosine similarity range from 1 to -1
2) 1=similarity
3) -1=dissimilarity
 


![image](https://github.com/user-attachments/assets/f264c52b-0917-4eb4-a5e5-b6337dd9f7ce)





</details>
</p>


<p>
<details> <summary> 4)Applications of  Embeddings</summary>

**1) find most similar words**
 
   ![image](https://github.com/user-attachments/assets/8d02f2af-77bf-4c01-9533-224367835624)

**2)finding the odd one out!**

    ![image](https://github.com/user-attachments/assets/69341692-72ea-4385-87af-3544bf144fb7)

 
**3) Sentence similarity:**
    
   ![image](https://github.com/user-attachments/assets/aaafb357-2fc6-4c4a-8acb-492eded372cf)

As you can 2 sentence are similar in meaning has cosine similarity score < threshold.

**3) Document Clustering:**
   k-means algorithm which works on cosine-similarity to group similar document.
   ![image](https://github.com/user-attachments/assets/43af15ea-60e1-41bc-895a-ac0423d5f1c2)

</details>
</p>



<p>
<details> <summary>5)Open/Closed Source Embeddings Available</summary>

1)Closed Source Embeddings:
==========================
![image](https://github.com/user-attachments/assets/8cda563e-f81e-41a3-a441-cc8480a71bf9)

2)Open Source Embeddings:
==========================

![image](https://github.com/user-attachments/assets/9a45bf14-da11-4196-824b-30b51c5a2f88)

</details>
</p>


<p>
<details> <summary>6)How to choose correct Embeeding.</summary>

1) look for domain specific embeddings like medical , retail, hightech

2 )if we dont find go to the state-of-the-art embeddings.

3) you can check the massive Text EmbeddingBenchMark(MTEB)

  [link](https://huggingface.co/blog/mteb)
   based on score you can choose the embeddings.
   
4) Fine Tune Embeddings to improve performance of RAG System.
   


</details>
</p>
