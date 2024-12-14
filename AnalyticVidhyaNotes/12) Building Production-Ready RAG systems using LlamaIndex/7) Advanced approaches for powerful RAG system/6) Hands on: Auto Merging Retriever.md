Hands on: Auto Merging Retriever
================================

- Auto Merging in Llamaindex is retrieval Mechanism to improve quality and relevance of information
  which is retrieved from large datasets.
- Value proposition behind the Auto Merge Retriever is that is automatically combines
  relevant nodes or chunk and that results in more coherence and more informative output.
- Question And Answer use case will provide more correct answer by combing the relative chunks .
- also in document summarization provide more comprehensive summary by combining relative sections.


Step 1 : Setup
================

![image](https://github.com/user-attachments/assets/713f0e74-0745-45b6-aeed-cf4b7f675f9c)


Step 2: load data:
==================

 ![image](https://github.com/user-attachments/assets/9f3aac4c-3de8-44a7-a71e-15cdaccf3e36)

Step 3: pinew pdf reader:
=============================

to illustrate automerging capabilities and usecase merge multiple documents.

![image](https://github.com/user-attachments/assets/5b830121-a475-46a4-bcd1-59f1e2259ad0)


Step 4: Hierarchial Node Parser:
================================

![image](https://github.com/user-attachments/assets/4fce4009-dd29-4ac9-b834-c4d2610accc6)


1st level -2048
2nd level - 512 chunk size
3nd level - 128 chunk size

load the hierarchial node parser and sentence splitter

![image](https://github.com/user-attachments/assets/9c919639-aaa5-4ca3-a005-46c9d97b05b1)



Step 5: Helper Function to count no of Nodes:
=============================================

![image](https://github.com/user-attachments/assets/8cfa4971-0ced-458f-9b98-055e88648d60)


balance is  parent node - root - highest level node-  has chunk size of 2048

Step 6: Load in to Storage:
===========================

- Vector Store index - to store leaf nodes.
- simple document store  - to store raw text of each of the nodes.
- document store include vector store by default.
- vector store index created to store the embeddings.
- run to create vector store index might take time depend on the total no of leaf nodes and document size.
  
  ![image](https://github.com/user-attachments/assets/b742752f-bc7c-4965-b98f-4be6df404216)

  ![image](https://github.com/user-attachments/assets/026ca998-5a0c-4f75-a831-4dd0ae803ac7)



Step 7: Define Retriever:
=========================

- Import AutoMergeRetriever from llama_index core retriever
- setting the base retriever to be base index from vector store index with topk similarity.
- setting the AutoMergeRetriever by pass the above baseretriever and storage context.
- difference between the normal and AutoMergeRetriever is it has automerge capabilities
  **if total no of retrieved chunks exceeds certain chunk >0.5 then instead of giving the
  leaf node for response synthesis , it will actually retrieve its parent node and
  that parent node will be given for response synthesis.**


- see below 3 nodes merge in to parent node
- finally parent node given to response synthesis
- total nodes retrieved by automerge retriever is 4 (1-parent node and 3 -merged child node)

  
![image](https://github.com/user-attachments/assets/55b2c06b-5304-48a6-8dc3-dfcf6fc99e65)

base node 6 nodes without automerging


![image](https://github.com/user-attachments/assets/a32c7f54-ccfe-4570-9736-f86fbcdfa6ca)

![image](https://github.com/user-attachments/assets/c0ad59c4-c79e-4c16-b331-05009e61eedd)


you can see 1 node has huge chunk size ( 3 chunk got merged in this node) and other remaining 
3 nodes same as without merge.

 Step 8: Query Engine:
=========================

  - query engine to retrieve the response.
  - query string is same and retrieval mechanism retrieves the same 6 nodes
    out of which 3 are merge to parent nodes.

![image](https://github.com/user-attachments/assets/c55074ed-2602-449f-827c-39a30d69b532)

![image](https://github.com/user-attachments/assets/724199c6-d543-43b1-8528-35d6f15ea597)


now base query without automerge

![image](https://github.com/user-attachments/assets/0dd3796b-e740-4f12-a8ed-84c4a171b75d)

Summary:
========

- response from AutoMerge is more elaborate compare to the base retriever.
