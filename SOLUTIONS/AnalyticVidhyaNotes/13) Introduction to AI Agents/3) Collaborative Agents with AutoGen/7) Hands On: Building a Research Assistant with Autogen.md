![image](https://github.com/user-attachments/assets/425327cb-bba3-437a-8c67-a79909e3e650)Hands On: Building a Research Assistant with Autogen:
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
  - if research report done by research writer agent is good and contains good reference , source and verifiable information.
  - research_writer should be written in clear and concise manner
  - to put them together , we need group_chat_manager


Step 4: create group agent:
==============================

   groupchat = autogen.GroupChat(agents=[user_proxy,planner,engineer,scientist,executor,critic,research_report_writer],
                                 messages=[],
                                 )

  ![image](https://github.com/user-attachments/assets/f4eb6118-a8a2-4914-8d1c-6bfada59e26b)


  - messages arr contains all the messages exchanged throughout this execution and we are going to set
    max number of rounds to be 50 in case these agents fall in to some loop and they can't really
    solve the task.
  - once we have done that , we say autogen.GroupChatManger() to manage this group
  - we pass groupchat and llm_config like previous example to GroupChatManager()
![image](https://github.com/user-attachments/assets/9f49a73e-cee2-49df-9c1a-55931579e6f6)

  - now we all the profiles for all the agents
  - then we set up the manager of this group , we can start  a chat and see if we can actually solve some tasks
  - so the task that is interesting for this type of multi-agent workflow is something like a research report.

![image](https://github.com/user-attachments/assets/23fec251-0758-421c-8eac-83668f0e4062)

  - i really like the example so we are going to say initiate the chat from the user proxy and this chat is going
    to be with the manager and the message right , the prompt that we want is going to be
    "write a four paragraph research report about how to use llm to **improve personal productivity**"
  - A topic that i'm weirdly obsessed with i dont know why honestly.
  - let see what happens when we run this , so now we start a conversation , the admin is saying to chat manager
    and sending out the prompt and now the planner is making up a plan for the project which is good.
  - now the next speaker in context is critic
  - because we get some critics on the plan.


  - inititate manager and the message.


Step 5: run multi-agent chat:
=====================================  

    - when we run this 
    - now we start the conversation.
   

   - the admin is sent to chatmanager and send out the prompt
![image](https://github.com/user-attachments/assets/f6085f79-b9ef-4c2c-ba2e-c0f88ed5171a)


   - now the plan is making a plan for the project
![image](https://github.com/user-attachments/assets/582f2e0c-918f-4fd3-9cd5-c3929471b3ab)

   - now the next speaker is critic to get some critics of the plan 

![image](https://github.com/user-attachments/assets/64a10f04-abae-417b-93e6-e3db8fcbf77a)

    ![image](https://github.com/user-attachments/assets/283c9207-002b-4773-8e75-ba180e809e4f)

   - now we send them off to researchwriter to write the report.

![image](https://github.com/user-attachments/assets/ceb92aa0-c7ee-46f6-bc2a-cc449e80fd85)

   - now we request to get some feeback , press enter after research writer to continue conversation.
![image](https://github.com/user-attachments/assets/5cf29e3c-4478-43a0-800b-a8204356e580)

   - now back to critic
   - the reference does not contain lot of information.
   - so we can something like try to find more url sources using sources like archive for reference section
     and then rewrite the report and improve.let see how feedback follows along.

   - so we send that how the feedback follows along.
   - we send them now the research writer implements and incorporates the feedback in to execution.

   - All right so it did
![image](https://github.com/user-attachments/assets/b804548e-5504-4829-9df2-d2c62b03f78c)
   - you can see additional reference source added.

   - you can inspect the output
![image](https://github.com/user-attachments/assets/0d0bc64b-a181-4cae-ba83-0235c300cd94)

    
    input - paragraph input report is the prompt

  - you can say output_report.chat_history

    ![image](https://github.com/user-attachments/assets/508d3231-f76e-4a73-bec5-77927bf397b4)

  - you can actually find the last element in the report.

![image](https://github.com/user-attachments/assets/1b94488b-1271-49e6-8ae5-8deb096c85de)

  - you can do markdown using Ipython

![image](https://github.com/user-attachments/assets/e8340caa-ba9b-4715-af29-8f147e73c434)
![image](https://github.com/user-attachments/assets/668e792f-daff-441b-ac97-7ded3328b8d4)


  - task was performed and feedback at the end to improve quality of report.
![image](https://github.com/user-attachments/assets/9b84d116-db7a-48a6-820f-d273ea48e317)


- Successfull multi-agent workflow by autogen.
