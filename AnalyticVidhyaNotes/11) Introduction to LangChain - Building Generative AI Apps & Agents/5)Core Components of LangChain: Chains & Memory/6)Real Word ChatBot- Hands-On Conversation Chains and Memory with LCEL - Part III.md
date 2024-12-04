
Real Word Chat Bot:
===================

Multi-user conversational Chains with ChatMessageHistory:
=========================================================

**chatHistory** - refers to a class in LangChain which can be used to wrap an arbitrary chain. chatHistory
keep track of inputs and outputs of the underlying chain and append them as messages to a message   database.
Future interactions will then load those messages and pass them into the chain as part of input.


**chatMessageHistory** - is that store separate conversations histories  per user or session which is often
the need for real-word chatbots which can be accessed by **many users at the same time**.

**get_session_history** - session pertaining to only that particular user.
TO separater between separate conversations, and should be passed as part of config when calling new chain.

Step 1:getSession_hisory Implemenation:
=========================================


![image](https://github.com/user-attachments/assets/96a8e3d5-6198-4f9d-834d-9aabb85d4dd2)

Step2:prompt to load in history and current input from user:
============================================================

main storage like below:

user1 :[conversation history]
user2 :[conversation history]
user3 :[conversation history]

so if work on user2 only those related to conversation of user 2 will be retrieved from sesssion.
history store=[] dictionary to store sessionid and session corresponding user history.

![image](https://github.com/user-attachments/assets/c0de4b88-11bd-4014-ad99-875c76ed8be1)
![image](https://github.com/user-attachments/assets/8bcf8815-a77b-4cc1-b4ce-9da6f504f9c5)

Step3:chat with LLM to stream result:
=====================================

![image](https://github.com/user-attachments/assets/28fb265a-161b-4c71-8b05-62d52340bb39)






