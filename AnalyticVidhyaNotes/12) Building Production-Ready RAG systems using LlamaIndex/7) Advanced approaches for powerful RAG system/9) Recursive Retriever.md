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
          |                                                |  Hierarchial structures preserving the hierarchial
          |                                                |  structure preserving relationship between chapters.



How it works:
==============

  - we can configure different retriever independently for each chapter present in the book.
  - Each retriever fetches corresponding relevant nodes of the chapter in the book, post that
    we create a special node called index nodes that stores the **summary of the each chapter
    and links it to the coresponding retriever of the chapter**.This index node will helps us to
    redirect to the corresponding retrievers depending on the user query.
  - Finally we create a recursive retriever that execute the entire pipeline.
  - At the query time, when the user query pertains to chapter 3, the corresponding
    index ndoe is retrieved. underlying retriever is the query and the relevant nodes
    are extracted accordingly.
  - This illustrate how the recursive retriever parses nodes recursively based on the
    user query. By now , you can must be clear the recursive retriever is suitable
    when data has hierarchial structure like file structure or nested document
    collections.
   - It allows you to retrieve relevant information at different levels of hierarchy,
     make  it usefull for scenario like knowledge base retrieval, document management
     systems or any data with nested organization.
      
  ![image](https://github.com/user-attachments/assets/c5e0d11b-f929-47da-8750-038f40ac45c5)


  ![image](https://github.com/user-attachments/assets/478c5516-0009-4027-bfb4-cc599df0141b)

  ![image](https://github.com/user-attachments/assets/4203fdf2-ea1e-4195-a89d-b0c2e8f91ad1)

Use Case:
=========

- in this example, we walkthrough the wikipedia article about the millionare, which
  contains both text and variety of the  **embedded structured tables**.
- text part stored in the usual text node - we can use panda query engine over
  each of the table and then represent each table by a index node which stores
  a link to query engine.
- this node is stored along with the other nodes  in vector store.
- during query time, if an index node is fetched then the underlying query engine
  retriever will be queyr.
- this manner recursive retriever retrieves the relevant information from
  not only the text chunks , but also effective from the tables with in the
  document.


![image](https://github.com/user-attachments/assets/44706ad9-d170-4bda-a73f-096edf920294)



  
