
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



