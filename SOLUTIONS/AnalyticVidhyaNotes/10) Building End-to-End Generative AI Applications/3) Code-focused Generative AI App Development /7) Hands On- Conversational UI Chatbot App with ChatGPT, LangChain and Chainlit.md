Hands On- Conversational UI Chatbot App with ChatGPT, LangChain and Chainlit:
==============================================================================
![image](https://github.com/user-attachments/assets/eb8672f6-8097-4bd7-a42d-bf7e8622b7a5)

  - build own converstational chatbot ui using langchain,chainlit.

https://github.com/arunsadhasivam/MachineLearning/blob/main/SOLUTIONS/AnalyticVidhyaNotes/10)%20Building%20End-to-End%20Generative%20AI%20Applications/3)%20Code-focused%20Generative%20AI%20App%20Development%20/Conversational_UI_Chatbot_App_with_ChatGPT%2C_LangChain_and_Chainlit/Module_3_7_Conversational_UI_Chatbot_App_with_ChatGPT%2C_LangChain_and_Chainlit.ipynb

Step 1:install dependencies:
==============================

    langchain - framework
    langchain-openai- chatgpt interaction.
    chainlit - ui
    pyngrok - ngrok tunnel

![image](https://github.com/user-attachments/assets/08269c3b-b30c-4788-9429-63f6cca1df81)


Step 2: setup keys
===================


 ![image](https://github.com/user-attachments/assets/c9cc2b5b-b7fe-43c2-a310-cbc8c84776d5)
![image](https://github.com/user-attachments/assets/9d2aba79-d111-457f-8ba8-cf7605775822)



Step 3: write appcode
======================

![image](https://github.com/user-attachments/assets/ee49b2ed-b618-4b6c-9da8-378cc7804a6f)

  %%writefile app.py:
  ===================
  - all code below in this command will get write to app.py

![image](https://github.com/user-attachments/assets/d47011e7-02af-442f-9e02-19e7ebd2f631)


chainlit decorator:
====================

![image](https://github.com/user-attachments/assets/8618f486-f7cc-427e-b7b0-094ed4a53563)

**@cl.on_chat_start:** ->  all the function below gets called whenever application starts for first time.
![image](https://github.com/user-attachments/assets/d7633341-9464-4990-9234-d2e71a2cfe27)

**@cl.on_message_start:** ->  whenever it receives user message.

2 entry point in app.py:
========================

1.@cl.on_chat_start:
=====================

  - usually load necessary dependencies to create necessary langchain pipeline , chains which would be 
    accessible ,whenever user want to access this app.
  - gets called whenever app gets loaded up for first time.

Code:
======
![image](https://github.com/user-attachments/assets/9d69b100-d8b9-4cc1-82b1-89bde3d05097)
![image](https://github.com/user-attachments/assets/15c49a40-9c2b-4e83-86a6-2113a989b5f6)
![image](https://github.com/user-attachments/assets/6573d295-59cb-4e41-9d24-9a15e77687f4)
![image](https://github.com/user-attachments/assets/56115e62-abd9-46c9-b110-8bf72671211e)


  - 



2.@cl.on_message_start:
========================
![image](https://github.com/user-attachments/assets/f7263a4d-1181-458e-8ee9-33d3526d356d)



  - executed whenever user send the prompt.
  - whenever user send the message , the function in the decorator gets executed again and again.
  - access loaded modules , access loaded pipelines like langchain pipelines and we pass our input prompts and generate
    response and show the response in ui.

Code:
======

![image](https://github.com/user-attachments/assets/95f67ed9-0d7f-48c0-b6e5-88828e94387c)
![image](https://github.com/user-attachments/assets/e2db6aee-93aa-47bb-8bbd-ad5502758c0e)


Summary:
========

  - on_chat_start called  where dependency loaded first time.
  - on_message_start called whenever user interacts again and again.

Final:
======

![image](https://github.com/user-attachments/assets/20e2825b-a25a-44cf-a629-46ee9f09119c)

- uncomment %%write app.py
- run this and refresh.

now deploy on ngr-ok:
=====================

command:
=========

    !chainlit run app.py --port=8989 --watch &>./logs.txt &

![image](https://github.com/user-attachments/assets/30063832-ee2e-4694-b1b2-f916c949cf8d)


- to run on terminal(!) ! symbol indicates run on terminal
- port flag (--port) to run on specific server
- to watch - (--watch) watch the file , if you make any live changes , your app will automatically get updated.
- to run in background mode (&)  - so when run the above command the app wont get blocked , run in background
- log using logs.txt
- it is a shell script, batch command,  we are not running the python code . as you can see (!) sign basically mean run on terminal.

![image](https://github.com/user-attachments/assets/68bd9860-d518-487f-81c9-43ed09e94d4b)
![image](https://github.com/user-attachments/assets/5a33280f-3f3a-4cd2-8303-bdf8a1114a9a)

- After run you can see logs and terminal batch script gets added to google cloud server.
- as you can see it is running as per logs
- if it is local running in local machine you can access using localhost:8989 but since it is in colab you can access the url.
- unfortunately it is not accessible in the server since it is running on google colab server
- so we cannot access the url

ngr-ok to expose as public url:
===============================
![image](https://github.com/user-attachments/assets/272d481e-b5ee-4cf9-86ce-beb530454e9d)
![image](https://github.com/user-attachments/assets/a8051bc8-9f02-40cf-98eb-d2b39beaf95f)

- so we use ngrok to create public url to access outside the colab.
![image](https://github.com/user-attachments/assets/36c343f4-9175-4bbe-a3d6-9f0f35732eb4)

- as you can see the public url is showing welcome screen , the welcome screen is available in chainlit.md file

summary:
=========

  - through colab we have written to collab using  %%writefile app.py
  - deployed in colab
  - accessible outside using ngr-ok tunnel.
  - now can use chat

Remove the running app:
=========================

![image](https://github.com/user-attachments/assets/ac69a235-7042-4342-967d-987d6e8c4db6)

- to see process you can run
    
    !ps-ef | grep app

- kill if you are using 2 or more colab , your colab will crash to better avoid kill finally.

    !sudo kill -9  5617
