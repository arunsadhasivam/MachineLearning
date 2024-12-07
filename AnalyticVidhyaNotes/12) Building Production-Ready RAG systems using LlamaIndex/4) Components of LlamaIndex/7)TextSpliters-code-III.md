

1.Text Splitters
==============
<p>
<details> <summary> 1.Code Splitters</summary>


![image](https://github.com/user-attachments/assets/e2e27683-86ee-4882-9d11-855eb06c3ce8)


**chunk_lines_overlap** is needed to have coherence in chunk to avoid abrupt breaking of node.
that is few codes are common in both nodes splitted.
e.g first node end has some text which is in beginning of next node to avoid 
abrupt breaking of nodes.

**max_chars** - maximum chars allowed in chunk.

![image](https://github.com/user-attachments/assets/0431a003-7b59-4f71-93a7-e68e3498cea8)


![image](https://github.com/user-attachments/assets/84bbb89d-0143-4c15-bc73-55c5c0577268)


code present in 1 node
![image](https://github.com/user-attachments/assets/2fdf4d1f-4a02-42dd-86e5-e0b17e765605)


</details>
</p>


2.Advanced Node Parsers and splitters
=======================================

<p>
<details> <summary>2. Sentence Splitters</summary>

read essay from paul gram
![image](https://github.com/user-attachments/assets/783a9ff6-90fc-4847-9047-a710c159dd2a)

![image](https://github.com/user-attachments/assets/c41bc767-0495-4e42-a6bc-9bd9c5b25896)


</details>
</p>


<p>
<details> <summary>2.1. Sentence Window Node Parser</summary>
![image](https://github.com/user-attachments/assets/20300f8a-df56-472e-94c4-51796a97ec52)

window-size - no of sentences on each side to include in window.
            - every full stop is 1 sentence.
window-metadata-key - metadatakey for window sentences.


create nodes using window 
![image](https://github.com/user-attachments/assets/2e6d4272-93be-45f5-ac01-1931e252ab06)


![image](https://github.com/user-attachments/assets/bcd40745-fce3-4d37-910a-23345546ee19)

![image](https://github.com/user-attachments/assets/c84fc18b-b3aa-429e-ade3-6921b853c6aa)

printing first 10 nodes. every full stop is 1 sentence.
![image](https://github.com/user-attachments/assets/49abb351-cac0-49a0-bc51-3939b698dbb4)
![image](https://github.com/user-attachments/assets/adf79b07-0279-4007-a327-9c9d06bf8f58)



</details>
</p>



<p>
<details> <summary>3. Semantic Splitter Node Parser</summary>

  Semantic parsers requires embedding model.
  operates by dividing each sentence to chunks and find the cosine similarity between 2 chunks or adjacent chunks.
  cosine similarity  - means vector representation of each of chunk in semantic space. 

  Cosine Similarity:
  ===================

  **dissimilarity** - if dissimilarity Exceeds Threshold or limit , then 2 chunks are different then remain separate.
  **similarity**   - if dissimilarity Below Threshold or limit, then 2 chunks are same in terms of meaning and content
                 then we concatenate 2 chunks.This process ensure model processing efficiency.
                 After concatenate we see less chunks since silimar meaning is concatenated.
                 for this we need embedding model.
              
  

</details>
</p>
