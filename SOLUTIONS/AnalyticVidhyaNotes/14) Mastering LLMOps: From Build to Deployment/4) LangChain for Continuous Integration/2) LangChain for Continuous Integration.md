LangChain for Continuous Integration:
======================================

    - langchain has lot of components, which is divided in to multiple sections, we have
       1) main lang chain  - which is chains, agents, retrieval strategies - core of the langchain ecosystem.
       2) 


1.main lang chain:
===================

    - it has chains, agents, retrieval strategies.
    - core of the langchain ecosystems.
    - it has also have open source library support langchain as a library is opensourced which has 2 major components
          1) core:langchain core - LCEL and base abstractions. 
          2) also we have lot of community support for e.g @langchain/openai -> code to make it easy to work it openai,
           same way for anthropic, and other providers as well.

2.LangGraph:
=============
    - langGraph - which helps us to buiild agent very quickly using graph database
    - we also have langSmith , which is a developer platform that lets you to debug, test, evaluate and monitor llm applications.
    - once you have llm applications ready , you also measure a lot of different parameters, test and evaluate things as they 
      go along , even during testing or even during deployment and thats what langsmith takes care of and has very high
      integration with langchain.


3.langGraph Cloud:
==================

    - which is the deployment part of langGraph in which you can take our langGraph application and deploy it on 
      langGraph Cloud.

4.LangServe:
============
![image](https://github.com/user-attachments/assets/f7590a8e-8ad3-4ee9-ae01-41bb9fe6e4f9)

  - chain as rest APIs
  - it makes it really easy to take these langchain chains and represent as **webserver base REST api's**
  - so from a project to actual web server, can be made really easy using langServer.
  - we have 2 main aspects of this langchain ecosystem.
    1) one is open source software
    2) then we have commerical part of these things.
  - so in the diagram we can see that commerical is mentioned with this box and **OSS is something open source**
  - And so we have langchain is the architecture and this is the underlying library
  - in the same way , the langGraph is also open sourced 
  - ALL the integrations, that we can do with the langChain and LangGraph is also opensourced.
  - then to deploy our langGraph applications to the cloud,is an offering that is given by langChain as an
   langGraph cloud which is properitory in nature.
 - And then to monitor all these things, is very easy using langSmith which gives lot of feature but it is also
   commercial in nature.

<p><details><summary>1. LangChain core components </summary>
    
 LangChain core components:
 ==========================
![image](https://github.com/user-attachments/assets/6077179d-fe03-4df7-9384-4a6f7e665b04)

1.LLM
======
    - discuss langChain core components , what they are , how they can help us to create llm based applications very quickly.
    - langchain has lot of integrations , and in integrations we found that one of them is LLM which is raw foundation models 
      and can help us quickly integrate with multiple different types of 3rd party api providers like chatGPT,anthropic.

2.ChatModels:
==============
    - these models comes in 2 variant
      1) one is the chat one - it is fine tuned instruction and then in library also they are called differently.
      2) one is the base model 

3.Agents:
=========
    - self guided llm, which you give them the ability to use different tools and then they make their own decisions.

Note:
======

    - in Langchain , specifically agents is also another section which makes it really easy to create and work with agents.

</details></p>




<p><details><summary>2. Dealing with documents </summary>

Dealing with documents:
===========================


- in dealing with documents, we have lot of integrations



1.Document Loaders:
====================

- which helps us to data ingest on multiple things.
- we might need to fetch data from google drive, and at some point to fetch from wikipedia 
- all these integrations can be easily be find out in langchain making our **job really simple**.

2.chatLoaders:
==============

- which is the data ingestion in chat format.
- we can use this to load chat and then quickly convert it into **chat format for LLMs**.

3.DocumentTransformers:
========================

- document transformers in which we have raw documents just retrieved and we want to transform
  in to another format , we can simply do it using **document transformers**.

4.TextEmbeddingModels:
=======================

- Then we have text embedding models, in which after these documents are created we transform them in to chunks
  or different formats, then we can simply do embeddings on them and there are multiple text embedding models
  that are available. text embedding model is really a **good integration** using which you can use all these
  text embedding models in a very easy to use manner and standardized ways.

</details></p> 
  

<p><details><summary>3. Memory (Database) </summary>

1.Memory:
=========

- database part in which we have memory which deals with **chat messages** that we want to store in a particular
  format, which can we implemented easily langchain memory integrations

2.Graphs:
=========

   - we have graphs which gives us really good integrations with various types of graph databases.

3.vector Stores:
=================

   - we have vector stores which is a **datbase** we use for searching similar documents and then
   - langchain has support for a lot of different vector stores as well.

4.Model Cache:
==============

  - cache the output of the  model.
  - so that we dont need to call **model again and again for similar input query**.
  - for that the integration is called model cache.

5.Stores:
=========

  - a lot of this times, the data we want to store in different storage solution, then that is
    also something langchain provides.

</details></p> 



<p><details><summary>4. Retrievers (Database) </summary>

1.Retrievers:
===============

  - all these things, that we saw in document loaders in which we have to
    1) load the document.
    2) Transform the document in a certain way.
    3) create these embeddings.
    4) store it.
    5) we have to run search on it.

  - all these can be done easily using retrievers.
  - all these process automatically be done and also means database like vector store be queried
    and will have final output.
  - retrievers are **really good way for end to end integration for data loading and data search**.

2.Tools and Toolkit:
====================

    - tools and toolkit, we saw web scrapping as one of the tools but there are lot of tools.
    - toolkit is just common set of tools.
    - we have toolkit for google, which might have tools in it 
                1) to send email
                2) able to retrieve google drive documents.
                3) able to do something else with gmail.
    - lot of functionality that langchain provides.
</details></p>   


<p><details><summary>5. Retrievers (Database) </summary>

1.callbacks:
============

  - we dont need lot of code to get all these functionalities we can just use langchain by default.
  - we dont need custom code to get all just use langchain
  - so, **when working with code base if we want deeper integration with what is happening inside our chain**,
    we can also implement using callback.


2.Adapter:
==========

   - if we started working with openai, and we want to work with openai kind of api in a similar fashion,
   - but in langchain, adapaters are provided which makes it looks like the API is exactly as same as OpenAI
     but it is actually in langchain format.
   - adapters are this simple modification in which different LLMs and langchain integrations can be done
     but the LLM API format looks like openAI.
     
</details></p>   




RAG Pipeline with LangChain:
==============================
