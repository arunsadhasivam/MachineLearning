Step 1: setup:
==============


we use titoken to use no of tokens in paragraph.

![image](https://github.com/user-attachments/assets/c80a91b5-2fba-4ced-a0c4-14b9f50bacdc)


Step 2: Spliter:
=================

split text in to  chunk size of 1024 .each node have 1024 tokens not characters
i.e 18 nodes have 1024 tokens.



![image](https://github.com/user-attachments/assets/8218665b-22ca-4e7d-b41e-d718049d905a)

![image](https://github.com/user-attachments/assets/e503ec19-004c-4d6d-b1f1-68dc40faea76)


Step 3: count tokens:
=====================

count tokens using titoken.

![image](https://github.com/user-attachments/assets/f5a26c40-6e99-4087-ab71-bb5cda6c16ea)


![image](https://github.com/user-attachments/assets/81597833-17bd-4dec-9b5e-0298627404ef)

 
930 token for node 0 as above screenshot.
![image](https://github.com/user-attachments/assets/7ea89efa-abd4-4f8c-bb4b-600abfdfa9bb)

same token id get from above openai tokenizer platform


![image](https://github.com/user-attachments/assets/f3b29810-7cc2-4dfc-a54f-bd406cc4e5f3)


Step 4: query to llm - count how many token spend in query and fetch response:
===============================================================================

question to system role - system message or specific instruction given to system
            user role -  you are asking question powered by openAI.

![image](https://github.com/user-attachments/assets/b782cbde-effb-4ef0-959c-18cb767faf79)


token to query openAI- 21  and   output response syntesizer tokens-73,  total 94 
![image](https://github.com/user-attachments/assets/1feb7f88-de8e-40c5-b463-10267683a6d2)


total tokens output -73  and no of characters- 386
![image](https://github.com/user-attachments/assets/ab42f5ba-5dd9-48bc-a628-5b8ef4b834fe)

Step 5: to get the exact token id:
====================================

encoder - pass same tokenizer "cl00K-base"
![image](https://github.com/user-attachments/assets/90cec872-99ba-43f1-96b3-c59298fd68c4)

go to open ai tokenizer website and confirm the tokenid


hello - 15339
world - 1917
" "   -0 
![image](https://github.com/user-attachments/assets/ed15b5b7-880a-46fb-a47e-8d12412edf87)


count no of token function:
===========================

![image](https://github.com/user-attachments/assets/3b752bc6-58bf-4761-bdfc-9430863cf6b1)


