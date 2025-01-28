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
    
 
2.RAG System architecture:
===========================
   
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
  - our application use chroma_db
  - once done, this concludes the first step which is document processing and encoding.
  - where we start of with 
        1) some **document**, 
        2) **document loader** to extract the text , 
        3) we use **text splitter** to convert in to chunks
        4) we use llm **embedder model** to convert every chunk to embedding.
        5) **encoding** in to embedding.
        6) store the **chunk and its corresponding embedding in a vector db** along with metadata like page no, **file name from which chunk came**.
   
    

    
 


2.QA search and generation:
============================
    

- this usually starts with user where user asks a user query
- send it over our application.
- once your query is send , we need to find out based that okay based on user's asked questions
  which are the document chunks which are relevant , which could be used to answer questions.
- so the first step is to take user query which is text pass it again to **llm embedder** and convert it to **query embedding**
- basically like every document chunk is converted to **embedding vector**
  similarly the **text of the user query** is converted to same embedding model to **query_embedding** embedding vector

- next step is we have vector database retriever on top of our vector db.
- this embedding is sent to this DB Retriever , what the vector database does it tries to figure out
  which are the document chunk embedding is similar to the question.
- so lets say we have bunch of document chunks , and each of these **document chunks** have corresponding **embedding**
- now what happens when a new question comes in , it goes through same llm embedder and we have embedding representation for the question.
- this embedding will be send to the vector database through the retriever and it will see hey **out of all the documents chunks**,
  which are the embedding which are close to the query embedding. it could be may this is very close or this is very close e.t.c
- what it will do is it will return back response **saying hey document no 3,4,1 are most similar document chunks**
- this is the step where based on our input questions and embeddings, the db Retriever goes to the vector db , goes through
  all the chunk embeddings, and figures out which document chunks are similar and relevant and could be helpful to answer a question.
- now once we have similar document chunks , we need to send our actual questions and these relevant document chunks to llm like chatgpt.
- so this is where similar document chunks and along with our questions as we can see here, both of them are sent int to  a langchain
  prompt templates. 

LLM Prompt:
===========
- these langchain prompt templates  will construct the llm model  prompt  saying **given these relevant document chunks, given these
  relevant contextual information**,can you answer the questions **only using** these documents.
  and this is send as a prompt to llm like chatgpt.
- chatgpt will generate response based on these documents to its best of its capabilities and response is send back to user
  and the response is shown in app interface.

Difference:
===========

- so this is very similar to chatbot app that we build earlier except now we are trying to answer questions not just by using
  chatgpt knowledge when it is **trained initially** but by using
- also the **custom knowledge base**
- this is 2 step RAG system.


 

 Key tools to build UI-based QA RAG chatbot APP
 ===============================================

![image](https://github.com/user-attachments/assets/5d66fe2a-8da1-4f74-bb89-6e88cdf63a7d)
![image](https://github.com/user-attachments/assets/ac5bc49f-d149-445f-8429-da75b9fda838)
![image](https://github.com/user-attachments/assets/33741f9f-15e5-4592-acd4-ee506b193ac0)
![image](https://github.com/user-attachments/assets/1571b9e1-30c8-4a04-9931-9a72eff387cb)


- langchain - python framework to build llm system
- llm model - openAI chatgpt
- llm embedder model - to embed the document chunk(token to embedding) to embedding as well as query embedding(query to query embedding).
- you can also uses hugging face and sentence transformer.
  we have llm embedder model like hugging face,openai, google gemini and sentence transformer    
- build ui interface like streamlit,chainlit.
- google colab -build all application code and deploy in colab.
- **to store embeddings and corresponding document chunks and metadata - use chroma_db- open source vector db**
   can retrieve similar documents.
- other are pinecone,weavelit
- ngr-ok to access deployed app publicly as we use google colab.




UI Based QA RAG ChatBot Architecture
=====================================

![image](https://github.com/user-attachments/assets/bb2b3aa9-083f-43eb-a79e-ffb3046b6c97)


    - input pdf document
    - upload and encode
    - app.py acts a backend
    - QA rag chain running using langchain framework.
    - all the app.py backend running on colab
    - streamlit user interface.
    - steps in chatbot:
       1) upload pdf document
       2) goes to app.py
       3) in app.py we will create custom retreiver function basically load text from pdf
       4) convert to chunk
       5) use llm embedder and store in vector db.
    - once first upload pdf done and vector db has chunk, we are ready to use QA chat bot
    - next is QA chatbot and response generation.
    - here only user asks question, then question sent to QA RAG chain using langchain
    - langchain would do is based on question it convert question to an embedding using llm embedder model.
    - it will query vector db and find out similar document chunk.
    - send the question along with the similar document chunk to chatgpt saying " hey given the text document"
      answer the question using only the contextual information. 
    - chatGPT will generate the response and that response is sent back to langchain and then in ui interface.
    - this is the overall flow.

Difference:
===========

- in this flow , the only addition to basic chat bot flow is **llm embedder model** which will accept encode
  our document and our query.
- vector database which helps in retrieving the similar document.

Authentication keys for APP:
============================
![image](https://github.com/user-attachments/assets/971649e3-56af-4411-b6a0-bd24214548c9)

![image](https://github.com/user-attachments/assets/279c7831-1a53-4bb9-9f57-6dc806f4f61d)

    
- you can use open ai.
- ngr-ok tunnel api key
- use yaml file in a safe manner to avoid exposing publicly.


RAG Case Study- QA Chat bot for Rare Diseases:
===============================================

![image](https://github.com/user-attachments/assets/9ec861e2-d1b2-4583-9ef1-6c396d8b7ce7)


- Q&A chatbot to answers the diagnosis of dent's diseases
- leverage 2 step RAG architecture.
![image](https://github.com/user-attachments/assets/20668472-f459-4c0b-8d7b-598edc21b1e8)
    
https://generativeai.pub/case-study-how-ai-can-help-cure-rare-diseases-a55f46de32d1

    - standard 2 step process.
    - first step extract useful information from various site , using just upload document, web scrapping, crawling and so on.
    - as you can see extracted text from various sources like audio, video, images, google scholar and several other non-standard forms.
    - once the text was extracted,ended up creating document chunk, then use embedder for creating document chunk and store document chunk
      and embedding in vector db.
    - 2nd step is QA search and response generation.
![image](https://github.com/user-attachments/assets/716fac71-1796-4959-9801-5223a5bde1f3)

- where based on questions, **ask to application using embedder model , create embedding for question**, retrieve document for the
  **questions which are closed to question in terms of similarity**, construct prompt and send to llm(chatGPT) for response.

- some enhancement like 
        1) understanding intent,
        2) adding some semantic keyword,
        3) prevent halllunications

Summary:
========

    - but the 2step process is same
      1) encode and store in vector db
      2) do search in vector db and llm to answer the question based on custom knowledge.
