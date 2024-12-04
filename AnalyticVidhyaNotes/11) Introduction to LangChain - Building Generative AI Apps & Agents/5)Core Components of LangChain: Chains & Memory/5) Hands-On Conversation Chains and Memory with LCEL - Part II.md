
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
