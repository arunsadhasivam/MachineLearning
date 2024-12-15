![image](https://github.com/user-attachments/assets/3e8b8bc5-1d48-4f1f-b004-e441a748f81b)Recursive Retriever
======================



![image](https://github.com/user-attachments/assets/bc82f44b-bb53-4312-97e4-7f2d86ebccca)


- in this we will disuss recursive retriever and then discuss with real world case study in llamindex.
- Real world knowlege is hierarchial and most documents contain hierarchial relationships.


  ![image](https://github.com/user-attachments/assets/bc7da8f0-1e4a-4c28-afb0-2063e13ec854)


- Imagine a pdf organizing in to chapters representing the structured hierarchy.
- when dealing with the documents with such organized structure and hierarchial relationships,
  the standard RAG Approach will not be most effective method.
- the Naive Approach overlooks the document hierarchial structure , storing the data
  as a disorganized nodes. this omition comprises the performance as it failed to
  consider the document inherent hierarchy. challenging the retriever ability to relevant
  information for user query. this where recursive retriever comes in.


  ![image](https://github.com/user-attachments/assets/c364e6b1-10cc-488e-b885-a0ea4c41fe18)
  ![image](https://github.com/user-attachments/assets/813c67da-0ab0-40b8-b9f5-7688749f0251)


Recursive Retriever Definition:
===============================

  Concept is that we not only explore the directly most relevant nodes but also explore the 
  node relationship to additonal retriever and retrieve them. like take example of pdf
  it maintains the relationship of each chapter.

Difference:
============

SNO   | Normal Retriever                               |  Recursive Retriever
------|------------------------------------------------|---------------------------------------------
  1   | single retriever for whole document            |  Recursive Retriever maintains document 
                                                       |  Hierarchial structures preserving the hierarchial
                                                       |  structure



      
  ![image](https://github.com/user-attachments/assets/c5e0d11b-f929-47da-8750-038f40ac45c5)

  
How it works:
=============


  
