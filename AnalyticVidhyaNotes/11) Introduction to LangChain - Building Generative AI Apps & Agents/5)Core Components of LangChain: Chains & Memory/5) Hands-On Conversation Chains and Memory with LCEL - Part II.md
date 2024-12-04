
<details><summary>1.ConverstationBufferWindowMemory</summary>
<p>

![image](https://github.com/user-attachments/assets/519e6abe-20e4-459f-b5d5-b41130e959da)
Performance using ConverstationBufferWindowMemory:
=====================================================

it just stores k historic messages which saves memory and windows of k so that token limit exception
can be avoided.
it helps to save token limits and costs.

![image](https://github.com/user-attachments/assets/77741faf-1ab2-4a3f-9dde-f108158007d4)


instead of conversational buffer we set conversation buffer Window Memory to store k historical data
=======================================================================================================


stores 2 messages of conversational history
![image](https://github.com/user-attachments/assets/349b20b6-d341-4438-b792-48261ad93b80)
![image](https://github.com/user-attachments/assets/a30bca30-a9ba-4d50-8fd0-135478ccc835)


Response:
=========

![image](https://github.com/user-attachments/assets/ca0ec14a-d8d4-4648-b2ed-dc7bf864c0e2)

</p>
</details>




<details><summary>2.1.ConverstationSummaryMemory</summary>
<p>

Use:
===

if you have long conversation or   lot of messages , you might exceed the max token limit of context
window allowed for LLM  using conversationalBufferMemory

ConversationSummaryMemory  creates a summary of conversation history over time. this can considerably
condense information from conversational messages over time.

really usefull in using for long conversation , where keeping past history in prompt verbatim would take up too
many tokens.


Step 1:
=======

connect llm to memory 

![image](https://github.com/user-attachments/assets/d40a62b8-4a87-4e5d-8fc1-a5c9bcc6ea26)
![image](https://github.com/user-attachments/assets/cce8fecb-04df-4979-9118-9503b61214a6)

Step2 :
=======
initialize  LCEL conversational LCEL chain and ask question.
![image](https://github.com/user-attachments/assets/07465701-5fda-4893-a999-2bf27742e995)
![image](https://github.com/user-attachments/assets/9ca2f854-82ee-47c4-ae92-7e5659a7cd14)

Step 3:
=======
visualize the memory , it just summarize AI and deeplearning in few words as below otherwise
it will be 4 bullet points (2 for ai , 2 for deeplearning)

![image](https://github.com/user-attachments/assets/bae119a3-58b0-4dcb-bb71-978e2351a79d)


</p>
</details>



<details><summary>3.Converstation Chains with VectorStore Retriever Memory </summary>
<p>


USE:
===

Vector Store Retriever Memory stores historical conversation  messages in a vector stores and queries the **top -k 
most "relevant" history messages** every time it is called.
NOTE:
=====

This differs from most of the other memory classes in that it doesnt  explicitly track the order of interactions but
retrieves history based on embedding similarity to current question or prompt.

Step 1:Enable access to openAI Embedding models:
================================================

![image](https://github.com/user-attachments/assets/cb6f6643-b5a6-4f8c-9741-da308fed5e1a)

Step 2:Create Vector DB (chroma) to store conversational history:
==================================================================

we use here chorma db and initialize an empty database collection to store conversational messages

![image](https://github.com/user-attachments/assets/14c9d0a2-d8b3-4d7a-abd2-15f1fac3f53c)


Step 3: use VectorStoreRetriever Memory instead of conversationMemory earlier
=============================================================================


![image](https://github.com/user-attachments/assets/68a5c827-cf7b-4e69-845c-1600974f616f)

load 2 most similar conversational messages from vector db using cosine embedding similarity.
![image](https://github.com/user-attachments/assets/f4bca505-b1ce-4ba6-922f-3bb1f7512deb)

use runPassThrough to get current  question , historic messages  which  query similar k messages using cosine embedding similarity
![image](https://github.com/user-attachments/assets/f6589305-aa98-44a3-9f3e-6133e7f86e4b)


Step 4: query now:
====================

query and save context

![image](https://github.com/user-attachments/assets/81bdb004-d53f-4b0f-8625-d334e862c340)

every time , each query save context

![image](https://github.com/user-attachments/assets/2866119f-12d4-4af5-af32-dfd1633cbb03)

![image](https://github.com/user-attachments/assets/4e3d1a3c-ecf9-43ba-9381-0f88744c945b)

![image](https://github.com/user-attachments/assets/98df7d00-3624-4967-958e-d14aa204d649)



Step 5:understand what is behing scenes:
========================================

Now for every query around machine learning even if the most recent conversation messages have been about animals.
it uses the vector databases to load the last 2 historical conversations which are closest to the current question
in terms of semantic similarity.

As you see for question "what about Machine Learning?" it checks previous 2 messages which are in similarity
like "what about deep learning" and "tell me about AI" which is closest in similarity in terms of cosine similarity.


![image](https://github.com/user-attachments/assets/d00b0a92-86be-415f-b6cc-f0dda50ef724)


</p>
</details>
