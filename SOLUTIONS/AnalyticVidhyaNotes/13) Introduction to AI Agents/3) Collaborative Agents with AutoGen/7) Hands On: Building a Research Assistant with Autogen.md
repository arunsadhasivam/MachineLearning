Hands On: Building a Research Assistant with Autogen:
======================================================

  - we build previously very simple agent.
  - ability to execute some code.
  - however now take it up notch with autogen what multi-agent workflow looks like

Step 1: install dependencies:
==============================

![image](https://github.com/user-attachments/assets/20e0c7fb-626a-4c0a-b516-ea63a077db97)

Step 2: import autogen and setup config list:
==================================================

![image](https://github.com/user-attachments/assets/8690bceb-5f51-4c3f-a8b4-7d883e4456ec)

 - Also give filter dictionary to filter out which model you want agent to use
 - in this case we use gpt-40 , most powerfull model across
 - now we have config and the filter.
![image](https://github.com/user-attachments/assets/c2ab9a1b-c0af-4371-9f8a-947024e69fd0)

 - now build up some agent.
 - so that we can put together.

![image](https://github.com/user-attachments/assets/8fa4af12-2e13-41e2-8c9e-b55dc0e01d3f)

![image](https://github.com/user-attachments/assets/3b821400-50e1-43b3-9e07-411fbb336d62)
![image](https://github.com/user-attachments/assets/d0856e1b-d23f-4a08-8d0c-ab3d52c9dd75)


Step 3: Multi-Agent workflow:
==============================

![image](https://github.com/user-attachments/assets/065b6098-1562-41e9-bbe5-1d723f45672f)

  - first create **system message** for proxy agent to Approve
  - current **code_execution_config**=false -> since we are not executing code for system_agent.

![image](https://github.com/user-attachments/assets/4fd45c06-153e-4ecb-a6a6-c8a719ad5a3e)

  - create a Assistant Agent planner.
  - suggest a plan to revise a plan
  - create a plan to explain which step performed by engineer and which is performed by scientist.
  -  now we have planner and engineer
  -  copy the template we have
  -  now then set up the agent.
  - remaining profile engineer, scientist,executor

![image](https://github.com/user-attachments/assets/10e50938-1c1a-4ab3-a7e3-1e922c892556)

![image](https://github.com/user-attachments/assets/4e008036-8c86-41df-8e30-d4818c26d2f0)

  - good configuration for the execution.
  - use docker if possible , but for this demo no docker.
