Building DHSGPT using Prompt Engineering- Part II:
==================================================


  - create a solution now instead of providing full context to the model every time.
    if first use the model to see what context it would need to answer the query.
  - in a way run a classifier on the user query , depending upon the response i receive
    i will provide only that specific context to the user and get the answer from prompt.
  - given classifier context given labels
    1) 1- prompt related to session.
    2) 2-prmpt related to speaker
    3) 3- prompt related to DHS summit.
   
  - i am trying to break down the query , which particular context which it refer to
  - and then only that context , i will pass limited answer to chatGPT and get the answer.
  - whenever user sharing the prompt , i need to first classify that with one of labels.
  - for e.g question "which session srikanth is delivering"

![image](https://github.com/user-attachments/assets/47e7bbf5-47e1-4b7c-9798-6e24e2743348)
![image](https://github.com/user-attachments/assets/224f39af-23cf-4e6c-ad7a-815d6407d2e7)

  - if label is **1 get the response with the prompt but the context this time is only session**.
  - if label is 2- get the response with the prompt but the context with only speaker
  - similary if label is 3 - get the response with prompt but context with only dhs
![image](https://github.com/user-attachments/assets/db094f39-c95e-436e-8d44-d8b99260d134)

  - now if i ask top 5 sessions - it gives the right answer still doing the engineering at the backend , still gives right answers.
  - now if i ask top 5 workshop - it gives correct.

Prompt Injection:
==================
![image](https://github.com/user-attachments/assets/6c6d3b69-cf1f-4263-b5ba-67a89fe9e06e)

  - now if i ask entirely new question which is not related , letting to do something which i not support to do
  - this is potential risk, because user might do something which i am not suppose to do.
  - this is called prompt Injection.
  - it a**llows the application to let do which is not suppose or intended to do**.
  - in order to handle this , we need to come up with a approach.

![image](https://github.com/user-attachments/assets/6e66e442-1d18-45f6-a04a-a3c4d15d3c90)

  - to avoid prompt injection , i create a new fourth label otherwise along
      1.session
      2.speaker 
      3.dhs 
      4.otherwise

  - written a logic or updated logic of classifier context to address if people giving query outside of context
  - the chat bot says i am dhs chat bot i can only answer dhs query.
  - if some one asks to **"forget everything "** model is able to address this.

    
