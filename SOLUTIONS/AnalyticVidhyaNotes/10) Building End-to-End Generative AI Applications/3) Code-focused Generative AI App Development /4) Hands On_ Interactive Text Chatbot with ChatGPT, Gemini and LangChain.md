Hands On_ Interactive Text Chatbot with ChatGPT, Gemini and LangChain:
=========================================================================




Step 1: install dependencies:
===============================

![image](https://github.com/user-attachments/assets/3e03e83a-c182-4718-bd7f-09807196b1ab)



Step 2: load keys:
==============================

![image](https://github.com/user-attachments/assets/09835f5b-897a-4727-a35f-0b117dbbf3e6)


Step2.1:load gemini-optinal
============================

![image](https://github.com/user-attachments/assets/a852023e-c93d-4d2c-884e-be45497b521b)


Step3:load necessary dependencies:
========================================

![image](https://github.com/user-attachments/assets/969caa39-561e-405c-b75d-478308e8b13f)


Step3.1:load necessary dependencies-optional-gemini:
======================================================

![image](https://github.com/user-attachments/assets/e0c24cbb-8b6c-43f4-a9f5-41f50dd6e5c6)


Step4:build converstational bot
======================================================

![image](https://github.com/user-attachments/assets/bce93029-cba7-4df9-90b6-e1693ec669e4)
![image](https://github.com/user-attachments/assets/1d1ac00e-9253-491f-bf76-3f1351ac22d8)
![image](https://github.com/user-attachments/assets/215eb438-7039-40bf-8735-9ee62a2744ed)
![image](https://github.com/user-attachments/assets/818f0f7a-6e3e-449e-aaa0-9074acc4954e)


- do in a loop keep asking for input from user.
- do while enter 'STOP'
- save the context.
- since it is conversational chain, need to store the input_prompt and response from chat_gpt in memory.
- this happens again and again until user enter 'STOP'
![image](https://github.com/user-attachments/assets/21a45329-beab-4933-881f-6b054338fffa)


- above the user enter prompt again and again.
![image](https://github.com/user-attachments/assets/3a31138e-31a9-44ee-8668-5ca9dc9aed7e)

change llm behaviour add system_prompt instead of default :
==================================================================
- change llm behaviour by using system_prompt('act as a sarcastic child')
![image](https://github.com/user-attachments/assets/ebc7ad1e-919e-4737-8500-63bb5bc3738c)

- now chatgpt behaves as sarcastic child(funny child).
- you can see "eye roll " icon comment 
