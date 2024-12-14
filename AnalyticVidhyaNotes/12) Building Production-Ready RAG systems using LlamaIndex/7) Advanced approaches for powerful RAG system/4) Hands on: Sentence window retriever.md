
Sentence window Retriever:
===========================

- sentence Window Retriever using LlamaIndex

<p><details><summary>1.Sentence window Retriever</summary>

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
    
    ![image](https://github.com/user-attachments/assets/9b3987ad-171b-4682-a0d3-f35d6e3bdf2b)
    
</details></p>


<p><details><summary>2.Base Retriever</summary>

Step 7:Base Retriever:
=======================

   ![image](https://github.com/user-attachments/assets/29cc4317-cfa7-46fe-82ef-1330c6733434)


 build index - takes 20-30 min

  ![image](https://github.com/user-attachments/assets/d8f4480a-f3e8-4c08-be5a-ba45c99dab7f)

setting up baseindex as query Engine

  ![image](https://github.com/user-attachments/assets/6f9c6b62-4382-4e10-b7e9-8164d2ce4f9e)

- As you can see result is no way close to actual value . dollar value is no way close $1,484 million
- numbers can confuse llm.

bump the top-k nodes to see whether it improves the result.

  ![image](https://github.com/user-attachments/assets/a65fa9c2-0042-4281-a460-61496e774ffb)

Above is also not correct. although clearly mentioned in the text since numbers present in text
is more.

Step 8:To check the result retrieved from SentencewindowRetriever is correct:
===================================================================================


confirm with chatgpt asking it to reproduce the text where it mentioned in document.

![image](https://github.com/user-attachments/assets/9c8cc182-315e-4b37-9fc8-accd19eb2a80)

![image](https://github.com/user-attachments/assets/a83c2069-988d-466e-89d0-0a0efafc1936)

</details></p>
