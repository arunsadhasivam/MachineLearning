Interactive Text Chatbot with ChatGPT, Gemini and LangChain:
=============================================================


    - build interactive chatbot using chatgpt, gemini, and langchain.


KeyTools to build Text-based Chatbot APP:
==========================================

![image](https://github.com/user-attachments/assets/b85ddb85-1d57-47ea-94f3-59b1ff86e065)


keytools to build a text based chatbot APP:
===========================================

![image](https://github.com/user-attachments/assets/116f5532-300a-437d-bf65-60c0f22ed5e5)
![image](https://github.com/user-attachments/assets/3a51aacd-b89e-41f4-b07e-624e380ca082)
![image](https://github.com/user-attachments/assets/d31cb334-e31a-4610-8a27-ff67bea6ef06)


Text Based Chatbot Architecture:
================================

![image](https://github.com/user-attachments/assets/95ad4a46-4062-433a-85f2-aa1cbb334f26)


- user enter prompt
- send it to text based chat bot
- prompt would go inside the conversion chain.
- it load up any past conversation history with chatgpt.
- then it send the augmented prompt with our past history conversation to chatgpt.
- chatgpt generate response.
- send it back  to langchain.
- langchain would send response to user / interface.
- we can keep asking questions, say way with conversational history.
