
Real Word Chat Bot:
===================

  
  <details><summary>1.Multi-user conversational Chains with ChatMessageHistory</summary>
  <p>
  
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
  
  Step4:run query-conversational Chain:
  =====================================
  
  User 1:
  =======
  
  ![image](https://github.com/user-attachments/assets/2feae83f-ad91-46d9-a214-887e9eb7b2d8)
  
  retrieves from history
  
  ![image](https://github.com/user-attachments/assets/6359fa97-5373-4956-9f85-c167c49aa545)
  
  Another user 2:
  ===============
  
  ![image](https://github.com/user-attachments/assets/0b642f64-3eb4-4169-b5b9-b01aace9ada6)
  
  see it is not colliding with conversation of user 1.
  it asks which context so it is not using context of user1
  ![image](https://github.com/user-attachments/assets/b2c74908-c878-4325-87ac-d977f668e4fa)
  
  
  confirm by summarize:
  =====================
  
  Multi user conversation with **same chain with Different Memory** for different conversation chain.
  
  it takes user2 #james
  
  ![image](https://github.com/user-attachments/assets/05d05f2f-c768-4c91-9d6a-40800ccab258)
  
  now pass user1 #bob
  
  ![image](https://github.com/user-attachments/assets/fd404132-e0b0-4e41-a01d-e12175e78b1c)

</p>
</details>


Drawbacks:
==========
might run out of memory since if more users present in chat more memory to store (userid, conversation history)



<details><summary>2.Multi-user conversational Chains with Persistance-Sql ChatMessgeHistory</summary>
<p>


memory-buffer-window:
=====================
to store k windows.

![image](https://github.com/user-attachments/assets/3ce0a0fd-5146-4f5f-8620-5fa3242ea48f)


Instead of ChatMesssageHistory use SQLChatMessageHistory:
============================================================


Step1: sqlChatMessageHistory:
=============================

![image](https://github.com/user-attachments/assets/4058d013-4753-42c1-bc7d-02cf58006538)

Step2:Chat Prompt Template: 
=============================

![image](https://github.com/user-attachments/assets/75b64cf1-f358-44d3-b83b-1432ba0a4b80)

Step3:MemoryBuffer k window 
===========================

Runnable pass Through the **current input prompt** and historic **most k=2 recent conversations messages**  
![image](https://github.com/user-attachments/assets/40d15b8a-82ea-4349-94c1-7606c09bef3c)

Step 4: load conversational chain:
==================================

based on user id it retrieve conversation from sql db.

![image](https://github.com/user-attachments/assets/5814a1cd-9d49-4bb1-8d2c-1a7552ed3e6e)


Step 5: Test Conversation Query :
==================================

User 1:
=======
 test with user #jim

![image](https://github.com/user-attachments/assets/128cb923-e09e-4749-a051-eb9aff76d9f8)
![image](https://github.com/user-attachments/assets/ffdb3513-a393-46c9-96d5-7b577bc6c3c6)
![image](https://github.com/user-attachments/assets/0701716a-c052-4f1d-b046-8c6358297b99)
![image](https://github.com/user-attachments/assets/bf2d292e-f9ea-404a-853e-77be091d0bb9)

User 2:
=======

test with user #john

![image](https://github.com/user-attachments/assets/7572837a-f0fa-47f9-bffe-74df816710df)

![image](https://github.com/user-attachments/assets/d4dd6207-60f7-4dc2-9485-d2490934d3b3)

![image](https://github.com/user-attachments/assets/bccbb0b4-5894-4ce4-b01b-9b9372b14106)


![image](https://github.com/user-attachments/assets/baa15184-8290-47c4-bd2f-84d33958f141)

</p>
</details>
