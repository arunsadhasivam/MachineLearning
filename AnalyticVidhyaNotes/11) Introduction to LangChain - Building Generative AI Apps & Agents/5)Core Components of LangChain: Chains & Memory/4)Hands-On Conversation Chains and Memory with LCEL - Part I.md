![image](https://github.com/user-attachments/assets/d67875d0-cd12-4fb0-82c2-bf74fa4b24cf)![image](https://github.com/user-attachments/assets/f610eee7-156a-4e47-b696-87207cbbb3b1)
Conversation :
==============

  conversation history or memory , during prompts it uses conversational memory to 
  respond to response.it adds to context "who won world cup in cricket" , next question
  "who is runner" it understand you are asking about cricket world cup based on history.

  
![image](https://github.com/user-attachments/assets/a8fbd6a7-88d6-4daf-bb6c-760962e60451)


  Various build in memory constructs:
  ===================================

  1) ConversationalBufferMemory - 
  2) ConvesationBufferWindowMemory
  3) ConverstationSummaryMemory
  4) VectorStoreRetrieverMemory
  5) ChatMessageHistory - wrapper to store messages in an in-memory list.easily to manage memory for multi-users and sessions
  6) SQLChatMessageHistory.

![image](https://github.com/user-attachments/assets/aa9d39aa-2cbc-4e69-9ae6-0a952dbf1b3a)



<details><summary>1.Simple LLM CHain without conversation Chain to show issues</summary>
<p>

Step 1: install dependencies - chroma vector DB for vector store memory:
=========================================================================


![image](https://github.com/user-attachments/assets/8581d00e-3f28-4882-bb64-95ac8c9eacce)


Step 2: Env-load api key:
=========================

![image](https://github.com/user-attachments/assets/00c83e7a-015b-484a-92e7-a0b6ab8f85ab)

Step 3: load LLM as before:
==========================

![image](https://github.com/user-attachments/assets/354bf7a7-4a12-42f1-a111-2dabe168a33d)

Step 4:problem with simple LLM Chain- cant track previous conversational history:
=================================================================================

![image](https://github.com/user-attachments/assets/7f369359-4d81-4757-9eed-27dbd57f40b7)
![image](https://github.com/user-attachments/assets/d0ddf761-c01c-48c6-bfd2-21eed34468f4)

![image](https://github.com/user-attachments/assets/9f56e9d6-1ebd-47b1-9f24-261270700931)




</details>
</p>


<details><summary>2.Converstation Chains with ConversationBufferMemory</summary>
<p>

NOTE:
====
this is the simplest Version of in-memory storage  of historical converstation messages. it is basically a buffer
for storing conversation memory.
Remember if you have really long conversation, **you might exceed the max token limit of context window allowed
for LLM**.


Step 1: create a standard prompt template with message place holder to store all historic messages:
==================================================================================================

system prompt and query prompt to get user input query.

![image](https://github.com/user-attachments/assets/55b03c45-bdbe-4e4a-9901-62fc9d23b593)


step 2: function to retrieve the historic conversational messages:
==================================================================

![image](https://github.com/user-attachments/assets/db8904a0-9af2-416c-8dcc-385fd8fe5b9c)

 
step 3: test function above with Runnable lambda:
=================================================

Test function with Runnable lamdba which will go into our chain.
Advantage is this returns history but also we need to send our currrent query to the prompt.

![image](https://github.com/user-attachments/assets/3892c7e3-058d-47fa-b11d-6d370c642626)

this behaves same as above function in step2 but can be plugged in to langChain chain.




step 4: pass query to Runnable PassThrough:
===========================================

To pass current query untouched along with pass current prompt messages.

![image](https://github.com/user-attachments/assets/c6a505ca-25a2-491d-a713-0db2624c7679)

-will return history but also need to send current query to the prompt.
as you can see we pass **query** with **history**
it returns "query" with "history.

 NOTE:
====
**Runnable Lambda** helps us to call the function at runtime.
**Runnable Pass Through** enables us to not just history but also what is current prompt or message
                          and both goes to LLM.



step 5: use Conversation LLM Chain :
======================================


history and current query is feed to prompt using **RunnablePassThrough.assign()**

![image](https://github.com/user-attachments/assets/4ca5e5c3-c5c4-4789-85c4-0d9e9ae1c1ad)

![image](https://github.com/user-attachments/assets/32d17544-fb85-4382-993b-22293e67f1d9)
