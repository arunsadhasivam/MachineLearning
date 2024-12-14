
Sentence window Retriever:
===========================

- sentence Window Retriever using LlamaIndex


  Step 1:setup Env:
  =================

  ![image](https://github.com/user-attachments/assets/10d7d3b8-f449-4a8c-a1fa-68d538fed924)

Step 2:Download Data:
========================

  ![image](https://github.com/user-attachments/assets/c41d4309-ee88-48b2-9964-7257c65bf65f)



Step 3:Load Data:
=================

  ![image](https://github.com/user-attachments/assets/3312b1a5-e453-473b-926e-dc44736c6a8a)


first page

  ![image](https://github.com/user-attachments/assets/7be10181-014c-4c5b-ac65-067057763249)


Step 3:Configure OpenAI-LLM:
=============================

  ![image](https://github.com/user-attachments/assets/6e80b36c-11cc-41e8-a9ea-2ca30bc945f9)


Step 4:Configure OpenAI-LLM:
=============================

  ![image](https://github.com/user-attachments/assets/e4197942-6a30-4ee9-96cd-48eeb118ed9a)


 - window size is 3
 - each sentence goes to "original_text"
 - we store the context window, raw chunk in the key.
 

Step 5:Vector Store index:
=============================

 - pass to the vector store index
 - this step takes minimum 30 minutes.
 - for 300 page document so have good gpu since we have 4000 nodes.
 - creation of embeddings , indexing  will take lot of time.

   ![image](https://github.com/user-attachments/assets/1a4cfde7-e46c-4be0-8ef3-e66891777482)

Step 6:Metadata replacement PostProcessor:
============================================  

   ![image](https://github.com/user-attachments/assets/a7d76b4b-f2a6-4ce9-843a-7024db155677)

  - Node processor as metadata post processor, we have original_text and window.
  - each chunk, context window stored in window metadata, context window will replace the
    original_text at the time of query and window will replace the original_text
  - replacement of the original_text with the context_window is achieved by **metadataReplacementPostProcessor**


    original text for the current window and the context window.
    - As you can see source node has the information.

    ![image](https://github.com/user-attachments/assets/cf371e00-fabd-4256-8e24-131a1628d2af)

    Above is the complete information passing to llm for final response generation.

    below is the final response
    
   ![image](https://github.com/user-attachments/assets/1a4cfde7-e46c-4be0-8ef3-e66891777482)


Step 7:Base Retriever:
=======================
