![image](https://github.com/user-attachments/assets/23509725-e151-4be3-8775-881a106b2464)Hands on: Auto Retriever
========================

- Main idea of Auto Retriever is that instead of retrieving the top-k chunk based on similarity search
  using the vector index. we can also retrieve the top chunk based on metadata filter.
- Now the Metadata filter are extracted using LLM and these chunks need to have the metadata information.
- there are some **vector DB that support metadata filter**
- one of them is chroma, PineCone, weavite
- we use chroma, this allows more dynamic and expressive forms of retrieval beyond top-k semantic search.
- for any query we will employ llm to do filtering on the metadata , and then finally do a combination
  of metadata filtering + semantic search  not raw semantic search in normal retriever.

![image](https://github.com/user-attachments/assets/bfe0c658-e777-4b02-b2cc-b327443ad51e)


Step 1: Step up:
================

create chroma db collection.

![image](https://github.com/user-attachments/assets/48e36c41-ab3b-4e36-b5a3-39902684af64)


Step 2: Define some sample data:
================================

  - define sample data, define node manually. the text node class not only contains
    the text which present in the nodes and also metadata information.
  - All these nodes 2 metadata( category, country)


    ![image](https://github.com/user-attachments/assets/bb60e98f-2cdf-4a7b-acda-4ceef9479c9c)

  create above nodes manually 

   ![image](https://github.com/user-attachments/assets/a8be559a-074c-4264-9a0e-ad7dc5c38b58)

   ![image](https://github.com/user-attachments/assets/c0bd7536-681b-44e9-979f-839b421796ed)



Step 3: Build vector index with chroma vector store:
====================================================

- create vector store index and the storage context has information about what kind
  of vector store is stored where ?

  ![image](https://github.com/user-attachments/assets/f318fffa-ac29-46a4-bb69-8e75b80d32b0)

  ![image](https://github.com/user-attachments/assets/57196cc3-5abe-40b9-817d-03b1d3ae250a)

Step 4: VectorIndexAutoRetriever:
=================================

   ![image](https://github.com/user-attachments/assets/a7c4d463-98af-4d33-9d02-31389c07434e)


  - 2 information present in metadata(category , country)
  - below is info about metadata itself
  - now we will run retriever with sample data and retrieve some information.


    ![image](https://github.com/user-attachments/assets/54b58c5b-aa9c-455c-b8bf-1e031904c625)


Step 5: Running over some sample data:
======================================

    ![image](https://github.com/user-attachments/assets/7b0dd4b5-dbd7-4f04-b4f9-80ee81642e59)


    - as you can see it was able to filter 'sports' and country 'united states'
    - who is extracting the category from the query - llm does that.

    ![image](https://github.com/user-attachments/assets/ad2e5b15-e8e7-4308-bb15-74a5ce5fff57)


    Node text response is used to synthesis the response.
    
Step 6: Run Response Synthesis:
================================


![image](https://github.com/user-attachments/assets/2a508be2-c605-4ea4-85e4-3f2b44155e1a)


final response above got from the response synthesizer.
