Case study_ Developing a Complex Generative AI application - QA RAG Chatbot:
===============================================================================


Outline:
========
![image](https://github.com/user-attachments/assets/0073d02a-fae8-4db9-a88a-5770f4bc7f69)

    - what is Rag System?
    - Rag System Arch
    - key tools to build ui based QA RAG Chatbot App
    - Ui- based QA RAG Chatbot Architecture.
    - Authentication keys for App.
    - Store chatGPT and NGr-ok API keys in YAML format.

<p><details><summary>1.What is a RAG System</summary>  


What is Rag System:
=====================
![image](https://github.com/user-attachments/assets/88f7b235-41d6-48c0-8d98-ddb9e03947ce)

  - RAG stands for Retrieval Augmented Generation.
  - Used for building QA Chatbots.
  - follows 2 steps process
    1) first step have your own custom data
      you process these documents , you encode them and convert to embeddings.  
    2) where you use this knowledge and augment llm ,existing knowledge base.
       this is where you do QA search and generation of response for your question
  - helps regular llm augment their information with custom knowledge before generating answers.
  - quickly become defacto stanford and architecture for building search and QA Systems.
 
    <p><details><summary>1.Document processing and encoding</summary>  
      
    Step 1: Document processing and encoding:
    ==========================================
    
    ![image](https://github.com/user-attachments/assets/7e2b3277-107f-405e-b2f9-ef44b5ddebce)
    
      - this is where you take in your custom document or custom knowledge base.
      - this is where custom documents are processed and chunked.
      - these chunks are typically converted to embeddings where the llm embedding model which is
        usually transformer model.
      - chunks and embeddings are stored in vector DB along with metadata like file name, page no.
    
    Note:
    =====
    
      - Now once
        1) your custom documents
        2) your own knowledge base processed
        3) chunked
        4) converted to embeddings
        5) stored in vector db 
        This is where you build the RAG system QA and search 
    
    </details></p>    
    
    
    <p><details><summary>2.QA Search and Generation</summary>  
    
    Step 2: QA Search and Generation:
    ==================================
    ![image](https://github.com/user-attachments/assets/754bec29-9d40-41fd-a240-f1f888668729)
    
       - Based on the user question or query the system retrieves the relevant document chunks
       - these are the document chunks based on custom knowledge base which are similar to the question which is
         asked by the user.
       - these chunks are passed on to the llm along with your query to augment its knowledge.
       - this is where once the relevant documents chunks related to the questions are retrieved
         the question along with the document chunks are sent to llm like chatGPT.
       - given the source of contextual information (to the chatgpt) can you answer the question fruitfully.
       - then the llm like chatgpt generates the response to the user query or question based on contextual information.
    
    - these are the standard steps to build RAG system.
    
    </details></p>

<p><details><summary>2.RAG System architecture</summary>  
   
![image](https://github.com/user-attachments/assets/18acfdb8-a8a7-41e0-9ef0-a1934a4f997b)

Step 1:
=======

 - you can have custom document usually pdf or databses
 - so in first step you use **document loader** which is dependendent on the kind of data (pdf,text,csv)
 - these document loader will load up the document files and extract the document text out of it.
     

Step 2:
=======

  - we have text content from first step.
  - we create small chunks or small entities of these documents.
  - because of storing entire document and representing as single vector may not be useful.
  - we need to store in form of shorter chunks like paragraph and so on.
  - so we use **text splitter** and split the documents in to smaller paragraph.

Step 3:
=======

  - once the document text goes out of **text splitter**,

Step 4:
=======

  - we got **document chunk** after go pass through text splitter.

Step 5:
=======
  - in the fifth step we pass on to the **llm embedder**.

Step 6:
=======

  - llm embedder model to take every model chunk and create corresponding chunk embedding.
  - as you might know an embedding is basically **vector representation of the meaning of some text.**
  - every document chunk will have its corresponding **embedding vector.**

Step 7:
======
  - once you have embedding , the next step is to store it in **vector db**
  - so in this step 7 , we dont just store embeddings, we also need to **know this embedding is the meaning or
    representation of which document chunk**.

  - **we store every document chunk along with its corresponding chunk embedding in a vector db**
  - we use currently chroma_db.
  - this confirms the first step.
       


</details></p>    
 



    


</details></p>  
