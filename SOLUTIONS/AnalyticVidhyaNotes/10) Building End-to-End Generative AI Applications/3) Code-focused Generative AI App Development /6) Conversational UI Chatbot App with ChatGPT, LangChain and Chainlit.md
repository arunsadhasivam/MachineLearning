Conversational UI Chatbot App with ChatGPT, LangChain and Chainlit:
====================================================================


outline:
=========

![image](https://github.com/user-attachments/assets/3d23a0bf-0588-4d04-a8c7-8330de7b73c1)


keytools to build a ui-based conversational chatbot APP:
==========================================================

![image](https://github.com/user-attachments/assets/428f6920-e688-48b4-b1c1-4870623f4b84)


![image](https://github.com/user-attachments/assets/99c30ab9-81bc-46c2-ab52-1def200c1695)


![image](https://github.com/user-attachments/assets/ce175f0f-022e-4b6c-9d35-c49254938512)
![image](https://github.com/user-attachments/assets/0e134557-5ee0-472f-8c56-7af762f3726c)

- building and deploying app in google colab.
- since deploy in google colab, we dont have public access to the google cloud server
  , so  we use ngrok to access deployed app through public url.

UI-Based chat bot architecture:
================================

![image](https://github.com/user-attachments/assets/7410d9d4-4b17-4db6-8d27-b1da631025c2)
![image](https://github.com/user-attachments/assets/1370ea37-7e43-40c5-8623-96af63bfb705)


- write your code in colab
- store all app code in app.py.
- app.py is backend code for langchain , chatgpt.
-**use writefile app.py to write to collab since collab you can write**
- once it is deployed in colab.
- ui when user enter it goes to app.py to get the prompt or user input and process by chatgpt.
- chatgpt process the input , look at the history data ,current user input and generate response and send back.
- app.py will send back response to user interface.
- user interface is entry point to accept the input
- this way we can create a full fedged conversation with a ui based instead of text based.

Ngr-ok - to access deployed app publicly:
==========================================
![image](https://github.com/user-attachments/assets/3904f135-cabf-4e14-953c-39eeb7b49095)

- since we deployed in ngr-ok we dont have a direct access to deployed google collab cloud server.
- ngr-ok to create a public accessible url
- so ngr-ok will create a public accessible url , which will directly interface with the deployed app
- so no need to worry about being able to  directly accessible in google colab cloud server, and then try to access app, we can just use ngr-ok.
- if not using colab then can directly access it.
- now see how to use ngr-ok


Access deployed apps in colab:
===============================

![image](https://github.com/user-attachments/assets/f07bbf09-349b-4651-b67f-78d91318a782)


- go to ngr-ok dashboard
- create a authtoken
- store it and it is needed when deploy in colab.

![image](https://github.com/user-attachments/assets/e1bccbd2-8077-45dd-b2bc-db7cafe048ea)

Authentication keys for App:
=============================
![image](https://github.com/user-attachments/assets/d45cb722-261f-4333-a7fb-0acfa1d747e1)
![image](https://github.com/user-attachments/assets/298efeeb-61df-4be7-b944-d6e39cbf98aa)

- access above in python.
- 
