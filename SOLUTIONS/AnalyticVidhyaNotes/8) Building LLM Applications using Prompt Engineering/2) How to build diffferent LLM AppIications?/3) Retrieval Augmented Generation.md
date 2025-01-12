![image](https://github.com/user-attachments/assets/868ad720-98a2-4c7d-a671-3a36e8cce67f)Retrieval Augmented Generation:
===============================

    - build llm applications using RAG.
    - rag is one of the most popular method to build applications powered by llm.
    - primary objective of this lesson is to understand what RAG is and why do we need.

why RAG:
========
    - knowledge of chatGPT is limited, 
    - when ask information about events after jan 2022, it cannot give us the appropriate response.
    - for instance, when prompted about the recent news, who won worldcup 2023, chatgpt could not give answer.
![image](https://github.com/user-attachments/assets/77cd2663-25f1-4f71-881a-e6c8173d5f36)

    - similary when i prompt chatgpt to answer about own enterprise data like give me the blogs of analytic vidhya
       published yesterday , it could not give correct output. reason is training data . training data includes 
       information available up to jan 2022.
    - it does not have the ability to access new information behond that date.
    - it keep refreshing over time, when you are wathcing it might not jan 2022. the point is that it is not
      till up to date.
![image](https://github.com/user-attachments/assets/0504712d-1e94-4181-b1d8-fcb8793d7507)

    - question is how do we enable our own external knowledge in to chatgpt and prompt llm on our own data. this is where
      RAG comes in to picture.

![image](https://github.com/user-attachments/assets/219e9ce9-e350-4bc3-a1ee-fbbd847d7740)      
    - with RAG , we have option to connect external knowledge base to llm like chatgpt and prompt llm to fetch the answer
      about your data.

![image](https://github.com/user-attachments/assets/85ed5e0b-d8ff-4737-ac07-59bbb027d1fc)


USES of RAG:
==============

![image](https://github.com/user-attachments/assets/484b31dd-612f-41bb-83c4-36f5a534e1f8)
![image](https://github.com/user-attachments/assets/1f3a10b2-91e2-44c2-9ae2-8aa5e0edd13c)

    - the external knowledge base could be structured data, unstructued data, semi-structured data in form of pdf,books,research paper or enterprise 
      data.
    - once the enterprise data is connected to llm, you can build qa systems , and begun asking questions on our data.
    - suppose you would like to review the companies financial report, you can simply upload the raw document like PDF to these RAG systems and
      begin analyzing the data by writing the prompts . 
![image](https://github.com/user-attachments/assets/f4f0dc5c-de34-4a1b-9427-e8ad1a0e12e2)

    - similary the enterprise data could be legal , healthcare and so on.
    - we can build customized chat bot on  your enterprise data using RAG.
    - analytic vidhya create a chat bot for the data hack summit (which is flaghsip conference) to assist user query using RAG.
    - similarly we can create chatbot for enterprise usecase using RAG.

How to build RAG Applications?:
===============================

  - it does not involve any model training, you can connect just any external database to model and
    prompt it through llm.
  - 2 main components in RAG.
![image](https://github.com/user-attachments/assets/b786a673-2fd3-466e-bb10-961341c10500)

 
    1 Retrieval:
    =============
    ![image](https://github.com/user-attachments/assets/5545c546-3230-4271-9f89-cf0d9aa5b156)

      - job of retrieval algorithm is to retrieve the relevant document based on the input query from the
        external knowledge which we have provided.
      - input to the retrieval algorithm is the query and the output is the relevant document.
      - the user asks the query , the query is then send to the retrieval algorithm.
      - the retrieval algorithm, fetches the relevant document required to generate the answer.
      - now the relevant document, and the input query is then passed on to a generator  which is basically
        a llm to generate the right answer from the relevant document.
           
    2.Generator:
    ============
![image](https://github.com/user-attachments/assets/0d2ceb01-0965-43fe-9ecc-f1aa9e14693c)

      - now the relevant document, and the input query is then passed on to a generator  which is basically
        a llm to generate the right answer from the relevant document.
        


Summary of Retrieval + generator:
==================================

    ![image](https://github.com/user-attachments/assets/6250d10b-a3b6-483b-81a3-0627e03f8ab0)


  - user prompt first sent to the retrieval algorithm,
  - retrieval algorithm fetches the relevant document and pass on to the llm for generating the answer.

PROS:
======

  - RAG is nothing but the prompt engineering to external knowledge.
  - hence no model training is required.
  - you also no need to worry about compute resources.
  - only external knowledge is required for enabling llm with custom knowledge which can be in form
    of structured, unstructured or semi-structured data.
  - it would incur a minimal cost to build RAG systems.

CONS:
====

  - it is bit on the higher side compare to prompt engineering , since it involves various other
    components like Retrieval and generator that adds up a bit to the cost.
  - RAG systems work efficiently with limited external knowledge, the performance however decline
    based on size of external knowledge.
  - for e.g RAG can perform well with 1000s of document,but with increase in no of documents
    says 100 of thousand might not work well.
  - these systems tend to produce incorrect output and not consistent interms of producing the correct output.
  - similary hallunication problem which we have faced in prompt engineering techniques.
    ![image](https://github.com/user-attachments/assets/61b11223-d417-4a77-8d2a-4a98fb57bc73)


