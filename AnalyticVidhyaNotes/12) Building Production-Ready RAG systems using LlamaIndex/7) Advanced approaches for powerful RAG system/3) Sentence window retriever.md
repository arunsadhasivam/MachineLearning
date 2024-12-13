Sentence window retriever
=========================

Naive Approach:
================

   ![image](https://github.com/user-attachments/assets/7b06e02d-0042-4543-9ca7-e75907c8962a)

  - breakdown documents in to smaller section and create Embeddings for each piece.
  - Then match these embeddings with the user query to select top relevant section.
  - these selected sections are then moved to response synthesis stage.
  - uses same texture for both embeddings and synthesis

Issue:
======

    - works well only for smaller chunks , whereas llm needs more context to synthesis on good answer.

Good Approach is sentencewindow to avoid above issue


Advance Retriever Techniques:
===============================

1)Sentence Window Retriever:
=============================


**Combination of Sentence window Node Parser + MetadataReplacementNodePostProcessor**

  ![image](https://github.com/user-attachments/assets/8bd013cd-f6e0-446b-bb63-410a7082ae91)

   - designed to retrieve relevant sentence on short segment on unstructured data
   - it uses sliding window techniques to extract overlap text segment
   - computes embeddings for each segment and finds most similar segments to the query.

   ![image](https://github.com/user-attachments/assets/32dee113-2f64-44dd-8e7f-8bbfef93d93c)


How does it work:
==================

  7 steps 

  ![image](https://github.com/user-attachments/assets/9d999ea0-00b7-4e8b-b30c-32829403ef5b)
  ![image](https://github.com/user-attachments/assets/e8f69109-e688-4e64-a1e2-bd9958d8ff32)
  before and after retrieved nodes are highlighted

  ![image](https://github.com/user-attachments/assets/f983070a-4a5b-47f4-81e5-dd92c1f37ea5)
  ![image](https://github.com/user-attachments/assets/16728589-e2b4-4a9d-9280-54648d3b5cb7)


UseCase:
=========

  1) ideal for retrieving specific sentences
  2) Handles Dispersed Information.



  
