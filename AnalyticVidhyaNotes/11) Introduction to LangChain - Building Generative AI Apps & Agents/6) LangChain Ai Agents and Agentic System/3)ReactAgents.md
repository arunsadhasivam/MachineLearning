
Multi-User Agent React workflow:
====================================


![image](https://github.com/user-attachments/assets/18e4c8c7-983d-4055-b3d9-ea6e54dff691)



Step 1:(setup):
==============
LangChain recommends **LangGraph** but here use Using **AgentExecutor**.

Tools for weather api, websearch tool setup
![image](https://github.com/user-attachments/assets/47e90201-6645-4d37-b48b-c2d666108211)

![image](https://github.com/user-attachments/assets/89c14f31-f486-47fc-a97e-44e8f5db0a4f)


Step 2:create tools for use by llm:
====================================

create tools  weather api, websearch tool

![image](https://github.com/user-attachments/assets/c913c7c0-f723-4710-ba5f-092dfe25f4b8)

![image](https://github.com/user-attachments/assets/6594eeb0-759b-449c-9ec8-8920d6068779)

Step 3:Test Tool by calling LLM:
=================================


![image](https://github.com/user-attachments/assets/c5201348-a608-4723-b1b0-0dbace197ab8)


tools response:
===============
![image](https://github.com/user-attachments/assets/0281da1c-820d-48b9-a01f-83aab56f491f)

![image](https://github.com/user-attachments/assets/e35577a4-a49b-4ed9-8de7-e21691fec68a)

Step 4: Build and Test AI Agent:
================================

Tool calling agent to  bind the tools to the agent with a prompt.Also add
historical conersation as memory.

Important:
==========
**agent_scratchpad" is a special variable used by ai agent store all intermediate messages which it gets by
calling relevant tools and getting output. it can use this variable to store that information, so that whenever
reasoning and acting ,it can access all intermediate steps, messages from scratchpad**

![image](https://github.com/user-attachments/assets/8a16def4-02df-4c91-b0c5-c87aafffa833)


NOTE:
=====

- Agent does not execute those actions - that is executed by AgentExecutor.
- passing in model chatgpt,not chat_gpt_with_tools.
- create_tool_calling_agent will call .bind_tools   for us behind under the hood.
- finally , we combine the agent( the brains)  with tools inside the Agent Executor ( which will
  repeatedly call agent and execute tools).

  
  ![image](https://github.com/user-attachments/assets/5a4a3cbe-8993-4530-b8b6-ea35c1228f3b)

Response:
==========
  ![image](https://github.com/user-attachments/assets/3c223736-b800-428e-b7f7-e4d751139017)



Step 5: Combine Agent(brain) with tools:
=========================================


finally we combine Agent(brains) with the tools inside the Agent Executor (which will repeatedly call the agent
and exectute tools).


![image](https://github.com/user-attachments/assets/5012ed36-45c5-4f3f-9397-61fcb4ae6c08)

Response:
=========

![image](https://github.com/user-attachments/assets/84373dcd-6c54-4cfc-9937-f173d79a06b2)

Step 6:Query:
==============

send query to chatgpt and agent executor.

![image](https://github.com/user-attachments/assets/02215c11-8e9e-46d5-a835-027409df12ed)


Agent Executor uses Agent to figure out answer if it does not know or not have data.

![image](https://github.com/user-attachments/assets/6bcf59ad-4b17-4b20-a3a4-167bc623bcdb)

Step 7: format output:
=======================

  1.search tool:
  ==============
  
  ![image](https://github.com/user-attachments/assets/ca2ec55d-dedd-4ba2-8ec0-0a7a294e46b6)
  
  2.Weather tool
  ===============
  ![image](https://github.com/user-attachments/assets/41e8b0c5-7389-46f9-a0ae-73eb8a5cf4a5)

  3.Try to query with past reponse check whether it remembers:
  ==============================================================

  As you can see it does not able to rember previous chat.

    ![image](https://github.com/user-attachments/assets/c6060332-2149-41c8-b854-bb2c0f6de386)

    
Step 8: Optimize - Advance Build and Test Multi-User Conversational AI Agent:
==============================================================================


use SQLCHatMessageHistory  - to create conversational Agent.
![image](https://github.com/user-attachments/assets/0d9d729a-f223-4da7-a789-b50a5a3f1d9b)

![image](https://github.com/user-attachments/assets/047c732e-770e-4651-91e1-64c90436c125)

![image](https://github.com/user-attachments/assets/465b2df0-b040-4e5b-8496-d49593331341)


  Conversation Chain + Agent
  ==========================

  here we plugin agent by adding RunnableMessageHistory(agent_executor)

  
![image](https://github.com/user-attachments/assets/89b3be62-6577-4fd1-8ab8-77bd01bdb9ba)

![image](https://github.com/user-attachments/assets/089f05e9-4990-4c1d-a4c6-f99f064bac6f)

simulate user 2 agent using agent. here it remember history of previous question.
here you can see

User 1:
=======


  question 1:
  ===========
  
      tell me who won champion league
  question 2:
  ===========
  
      tell me more about that event - second prompt it remember first question
     based on that champion league it correlate and answer .
  
  ![image](https://github.com/user-attachments/assets/3af5da4f-8736-40f3-9b4b-8aa2bb919f40)


User 2:
=======

question1: 
===========
  how is whether in bangalore

question2: 
===========
   how about dubai.

here it understand  whether they are asking bangalore or dubai


 question 3:
 ===========

 which city is hotter
 
![image](https://github.com/user-attachments/assets/c408680d-e72b-402c-a4eb-75da67db04f1)

![image](https://github.com/user-attachments/assets/f764e0c0-2fa4-4cdb-87bd-285a226b265c)

here it understand whether they are asking bangalore or dubai
![image](https://github.com/user-attachments/assets/a43634b9-7a8a-49d9-a98d-86bf10be43fa)
