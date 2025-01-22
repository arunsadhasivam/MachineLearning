Understanding Generative AI Applications - Architecture and Impact:
====================================================================

![image](https://github.com/user-attachments/assets/f5ad3f2f-d4f9-4162-b3b0-df2a10ecf913)

    - look at the standard components of a gen ai applications
 
  
1.standard components of genAI applications:
================================================
![image](https://github.com/user-attachments/assets/193b7dc5-d7ae-4ae7-8cfb-f2aebb761eb9)


  - user interface which will typically accepts user prompt, questions.
  - backend applications to handle the logic and processing and connect the llm.
  - this is where we definitely need the llm like CHAT GPT to generate response based on input questions, prompt.
  - optionally need a database to store the documents, embeddings, results and so on just like when you are 
    build an RAG based chatbot.
  - custom data or documents are optional depend on usecase.
  - **need the server to deploy and monitor the app(to be covered in LLMOPS course)**
![image](https://github.com/user-attachments/assets/3a1a099b-3914-4245-86ff-02f5f7df6ea8)


1.Front end UI:
===============

    - user input the prompt or questions
    - this will go to the back end app typically running in python.
    - some necessary processing if it needs to retrieve relevant document 
      it would retrieve from vector DB and it would go to the LLM where llm models will
      process input promt along with additional documents if necessary to generate a response
      and send it back to the backend applications. 
    - this would forward to the user interface where would see the response from the llm being displayed
      and then accordingly you can keep having the conversation using the front end UI

2.NO Code based generative AI Apps:
======================================
![image](https://github.com/user-attachments/assets/478da5b0-7ee4-470c-bdb1-fc88e715f52c)

  - no code based gen AI apps like chatGPT and huggingface we will cover in this course.
![image](https://github.com/user-attachments/assets/da2aa370-8dab-4633-b7e5-110bf9499718)

  - front end customization is minimal.
  - no need to write to code for front end although less flexibility in the UI elements.
  - backend customizations options are limited to fixed model choices and prompts.
  - but it is simple to get going with minimal amount of knowledge in program.
  - building POC is easy without need to learn code.
  - you will use UI based interface to build an entire applications.

3.Code based generate AI apps:
================================

![image](https://github.com/user-attachments/assets/9390fe19-ea95-4c43-92d9-514dd954b26a)

  - LLM APis from hugging face and openAI allow for the various models.
  - using programming language like python to interface with the apis
  - front end customizations is flexible and detailed.
  - backend customizations can be done with python and libraries like langchain and llamaindex
  - lot more flexibility,control and customization.
  - it is not necessary to write huge codebases to create quick proof of concepts (POC)
  - usually in less than 100 lines you can make chatbot going.
  - knowledge of front end language like javascipt is not necessary only need chainlit, streamlit is enough

4.Impact of end to end generative AI apps:
===========================================

![image](https://github.com/user-attachments/assets/154b9142-9aa1-4649-9dde-8e9f39b3edd4)
![image](https://github.com/user-attachments/assets/84e2fe6e-8cb2-414a-bf6d-ad04c30f5312)


  - you can build quick working POC with just single language which is Python or
    use platform like hugging chatter CHATGPT to build an end to end apps.
  - knowledge of front end language like javascript is not necessary.
  - easily signoff from poc to full applications and system to scale it up.
  - simplify the applications using for end to end users so that you can boost adoption,
    as long as you can simple elegant minimal user interface people will use it.
