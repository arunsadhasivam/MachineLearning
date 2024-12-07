

DataLoaders:
=============

![image](https://github.com/user-attachments/assets/5ba59a7c-f11d-4a47-869f-b00e407850b6)


Installation:
==============


![image](https://github.com/user-attachments/assets/2d56eda5-efca-4a9e-b588-a368d16cf7ec)



<details><summary>1) Document Readers </summary>
<p>
  
  Option 1: Loading PDF:
  =====================
  
  ![image](https://github.com/user-attachments/assets/0f6e5010-46c9-4420-b14b-e54a25686154)
  ![image](https://github.com/user-attachments/assets/14d9e040-8551-49f3-8070-49c0ce38593d)
  
  Option1.1 -PDF Reader:
  =====================
  
  ![image](https://github.com/user-attachments/assets/20b49cf2-0fd0-43bf-924a-37ef200eb193)
  ![image](https://github.com/user-attachments/assets/5683528f-c9d3-4b05-acd7-3bac1967b0e6)
  
  Option 2: load CSV:
  ===================
  
  
  
  ![image](https://github.com/user-attachments/assets/2758775a-de1c-4527-a3db-de24f1933245)
  
  Option2.1: read csv:
  ====================
  
  ![image](https://github.com/user-attachments/assets/802b0660-8ff0-4e57-845e-79a20e50c4fc)
  
  
  Option3: loading Web Page:
  ==========================
  
  ![image](https://github.com/user-attachments/assets/58720703-861a-4995-8eb1-16fd314cfb7d)
  

   Combine Multiple Documents:
   ===========================


   ![image](https://github.com/user-attachments/assets/33f68466-c673-490f-af5b-1cf49eb817af)

   Read from directory:
   =====================

   To Read specific files from a given directory.
   
  ![image](https://github.com/user-attachments/assets/53f0ca7a-1ff3-4316-80af-aeceb4e229b8)
  ![image](https://github.com/user-attachments/assets/0a2b9ce5-b1b3-4d2f-a72d-32babaadc098)


</p>
</details>


<details><summary>2) Chunking and tokenization </summary>
<p>
  
  2)Chunking:
  ==========
  
  Breaking text to chunks or smaller segments which are vectorized and stored , boosting the efficiency
  of NLP tasks
  
  ![image](https://github.com/user-attachments/assets/104332e5-cb14-4c6d-b51e-d6ee26ab78a2)



  - smaller or more precise chunk leads to finer match between user query and context and enhancing the
    accuracy and relevance of information retrieved.
  - larger chunk might include irrelevant information introducing noise and retrieval accuracy.
  -  by maintaining the chunk size,  RAG can maintain balance between comprehensiveness and precision.
 

  How to choose the correct RAG Size:
  ====================================

  - choice of rag size is crucial it should be small enough to ensure relevance and reduce noise but
    large enough to maintain context integrity.

  - chunking is implemented in llamaindex using nodeparser.

  What is tokenization:
  ====================

  ![image](https://github.com/user-attachments/assets/6a1a0753-5ae0-4764-9aa2-f6db41e4e3a4)


Tokenization:
==============

1)subword Tokenization -
========================
    breaks words in to subwords from dictionary, model can handle words it hasn't seen before.
      "e.g" -> "prashant" -> 8  characters  subword Tokens "Pr" -"ash"-"ant"
      "Pr" -> unrelated document
       "ash"-> dictionary
       "ant"-> 3 tokens

1.1) Types of Subword Tokenization:
===================================

![image](https://github.com/user-attachments/assets/5d0a9edc-de47-488c-bd5c-525ed4ca06ad)

2)why important to know token no of tokens in a chunk or document:
===================================================================

- crucial to know the max tokens llm can handle. this limit is to input context limit
  and output response synthesis limit.
- **input context limit/window** - maximum no of token model can accept or process as input.
- **output response sysnthesis limit**-  max no of tokens that model can generate as outptut.


![image](https://github.com/user-attachments/assets/ca26370a-871c-4e9e-94d7-d233f98cef76)

  Embedding models:
  =================
  ![image](https://github.com/user-attachments/assets/8063acc4-0384-4f80-947d-868a390175a8)

  Note:
  ====
  top 4 are prioritery or paid model has higher input /output token limit.
  last 4 are free model has low input context limit and output token limit is not mentioned.
  means it can pay attention to most 8000 tokens.

</p>
</details>

