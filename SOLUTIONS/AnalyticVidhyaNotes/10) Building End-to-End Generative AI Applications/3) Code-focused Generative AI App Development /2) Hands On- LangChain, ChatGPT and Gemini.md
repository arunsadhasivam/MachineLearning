Hands On- LangChain, ChatGPT and Gemini:
========================================


- langchain to interface with chatGPT or gemini both.
  
Step 1:set up Env
====================

![image](https://github.com/user-attachments/assets/14caaa3f-259a-4f31-be42-ef450bc0dab4)


Step 2:openAI credential:
=========================

![image](https://github.com/user-attachments/assets/5100cba0-01cd-461c-99d7-423ca59f61e3)


-upload key for openai credentials
![image](https://github.com/user-attachments/assets/aa555872-d6c3-4b46-93e1-d70fdf45bada)
![image](https://github.com/user-attachments/assets/40921552-999d-4fa0-8367-7c742e39a884)


Step 2.1:optionally load gemini:
======================================
![image](https://github.com/user-attachments/assets/8669227b-7971-4db0-961a-eaad9a8f920c)


Step 3: load necessary dependencies and chatGPT llm:
=======================================================

![image](https://github.com/user-attachments/assets/2d622ae4-fccc-43bd-a30e-22eee5cd2ecd)



Step 3.1:optionally load gemini llm:
=======================================================

![image](https://github.com/user-attachments/assets/97118ce6-7afa-44a6-8b0f-8109dd16aab3)

- ends creating connections and now create prompt and then query.

Step 4: create basic chain:
============================

- uses lcel(langchain expression language)

![image](https://github.com/user-attachments/assets/f10e70bc-8b65-4602-8ad1-a9c26cf28bcc)


 - create a flow or pipe chain
 - create a basic chain using lcel
 - create a template out of string that becomes prompt template
 - create a **pipeline called chain saying i have prompt send this prompt to model**
 - when i am sending prompt to the model i am using vertical bar(|) it is overloaded vertical bar or **pipe
   operator which is basically saying whatever in the prompt that will be send to the model.**
   
Step 4.1: chain with gemini:
============================

  - for gemini everything remain same except instead of model of chatgpt pass gemini_model

![image](https://github.com/user-attachments/assets/c77f4dea-220f-46cb-bb2b-034ef91ac764)

Step 5: map function:
======================

![image](https://github.com/user-attachments/assets/9edccd7f-c25f-451a-8779-16ffd4966f4d)

  - map function enables you to run multiple input one after other and generate the response.
  - no conversation history.

step 6: converstation history:
================================

  - challenge with basic lang chain chains.
  - if you create a simple chain where you accept the input question from user
  - send to model llm and generate response.
  - assume if you chain A question "what are four color of rainbow"
  - it response saying "red, orange, yellow, green"
  - again if you call the chain "asking what are other 3"
  - but it gives totally different answer.
  - because every query is a isolated query to chatgpt , it does not remember any past history

![image](https://github.com/user-attachments/assets/a66ba519-b605-409a-b38b-7ffb97400926)


Step 7: add memory to build a conversation chain:
===================================================

![image](https://github.com/user-attachments/assets/b8aa2a35-35e7-4c93-9f67-729ee1751844)

![image](https://github.com/user-attachments/assets/a53e6f42-b3d7-49ba-ae77-9f20f747e565)


- first step create a sequence of prompt
- where first message is system_prompt telling chatgpt to act as helpfull ai assistant - using this 
  system_prompt you can control how chatgpt can behave with you.
- then put a place_holder after this , as the name suggests it is a place_holder which will be populated
  with historical messages when you have conversation with the chatGPT.
- third prompt will be your question , prompt which you send to chat gpt.
- whole idea is to make chatGPT behave in a certain way , taking in to account any past conversation
  which you have with chatGPT , take your new questions, send that to chatGPT to answer this input question.
  that will be the flow.

- converstation buffer window memory is a nice langchain construct which can hold the last k conversations which you
  have with chatgpt.  

- run the prompt template
- now call memory.load_memory_variables

  ![image](https://github.com/user-attachments/assets/8bfad8ff-3a5c-4490-9103-6128a75873b5)
![image](https://github.com/user-attachments/assets/2f674fcb-d29d-4856-98a9-ef16fc434000)

 - now create conversation chain pipeline
 - RunnableLambda tells-load memory data from memory variables which is the conversation buffer memory.
 - this tells runtime load the historical conversations you have with chatgpt and store it in history.
 - itemgetter("history") is accessing the conversations from the history variable
 - then it tells us, rather it tells langchain that ok now send this history to the prompt
 - prompt is where user asks questions
 - so along then with the historical conversation and prompt send both to the model and get response back.
 - history conversation and history send both to model and get response.

 - run conversation chain
 - now call chain.

![image](https://github.com/user-attachments/assets/daa1285c-d129-457c-a498-a22976ce316d)

![image](https://github.com/user-attachments/assets/a4e52892-0e6d-4207-8176-289c62b456e4)
![image](https://github.com/user-attachments/assets/ba8145ac-a776-449b-9be4-f71f1d5cbcac)
