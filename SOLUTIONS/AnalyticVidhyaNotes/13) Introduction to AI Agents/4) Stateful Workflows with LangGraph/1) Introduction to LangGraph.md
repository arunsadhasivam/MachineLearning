Introduction to LangGraph:
==============================


 - we have look at Autogen, we have looked at langchain as 2 different frameworks.
 - these 2 try to implement a way of putting together llm and tools in the form of useful agents
   and useful agentic workflow to perform complex and interesting tasks.
 - Now, the evolution of langchain as far implementing the agentic workflow goes is the
   creation of **langGraph**.
- **langGraph** - which is langchain based implementation of this Graph infrastructure or putting
  together langchain components and implementing langchain agentic workflow.
- Essentially not only agentic workflows, but workflow that involves computations that leverage llm.

  
Understanding Agentic systems:
===============================

Agentic Systems:
==================

  - system that uses llm to manage the control flow of application.

Key Functions:
===============

  - Routing decisions, tool selection and evaluating output sufficiency(whether or not the output is sufficient to generate answer).
  - evaluating the output , whether the output is sufficient enought to return the output, we saw the agent loop
  - the idea the model can loop over selecting the actions or returning the output to the user until it reaches the
    decision or reaches the threshold point where it finds the output to be sufficient to return to the user.

Agent Loop:
============

    - continuous decision making process that enables agent to solve complex tasks.
  

![image](https://github.com/user-attachments/assets/759c049e-4b64-4385-a17c-767521ca253f)


1.Agent Loop:
==============

  - refresh on agent loop to help to understand on graph based implementations of agentic workflow - LangGraph.
  - it starts with the user input
  - then some model evaluates the input
  - the model might deems that it has enough information to send back to user
  - however if not , if detects action is needed it will execute the action and it will observe the outcome of event
    then that will be feed back to llm for further evaluation to see if it has enough information to return to user.
  - this is the basic agent loop

![image](https://github.com/user-attachments/assets/32e477ad-ee3e-4c76-bda7-494190482119)


Practical Use Case - Customer Support Agent:
============================================


  - perspective imagine scenario that customer support agent powered by llm.
  - user input something like user asks about the status of order
  - the decision from llm is it can provide the status immediately
        or it fetches data from db.
  - if data fetch is needed , the agent queries the db and the agent updates
    the user with order status.
  


![image](https://github.com/user-attachments/assets/093facac-d50c-4566-b0bf-93152bce848d)


Advantages of LLM Agents:
==========================


![image](https://github.com/user-attachments/assets/564283d1-e10d-45fe-8989-148300e54b1f)


  - it then give user the output for the query.
  - you have flexible system which can **adapt to various tasks by determining the best action to take**.
    you have specialization.
  - the agent can be specialized with tools to perform the niche tasks.
  - you also have multi-agent collboration, we see that lot in autogen , now we see in langGraph.
  - where you have specialized llm agent that can collaborate to perform complex tasks.
  - what are the key components of Agentic systems.

Key components of Agentic systems:
====================================


![image](https://github.com/user-attachments/assets/91b8478a-509a-464d-bd39-620c1c9c5077)

  - you have **tool calling** which is the external tools to perform tasks
  - you have ability to take action which is essentially calling the tools and produce outcome.
  - you have ability to keep tracking of context-aware responses.
  - so we have to have memory in some way
  - you have the ability to plan ahead for actions, so structuring steps to ensure optimal decision making.


Agents as Graphs:
====================


![image](https://github.com/user-attachments/assets/bf760c97-ead2-496e-b05f-d2479295eeec)


  - Now, when we look at those components and when we look at the idea of loops, control-flows, we start
    seeing a pattern and that pattern is that **we model these things as graphs**.
  - so workflows build with agents are usually structured as graphs.
  - so you have 
        1)user,
        2) you have prompt
        3) that's sent to llm ,
        4) that produces the outpout  or
        5) model will take an action.
 - so above looks very much like a graph diagram.
 - usually modelling these things as graphs
 - so why langGraph

why LangGraph:
==============

  - LangGraph is designed for building agentic applications with core principles like modelling itself as graph.


![image](https://github.com/user-attachments/assets/ec07ee9f-8f3c-4bbf-90ed-95c3d88d152d)


What are first principles of LangGraph:
=======================================

1.Controllability:
==================

  - LangGraph gives you low level control wich increases reliability in agentic systems.
  
why is this important:
======================

  - when you look at the other implemenations of the systems to put forward these agentic workflows and
    agentic systems e.t.c.
  - you see a lot of just describe the role, describe what this thing does in a superficial way and
    let it go in wild to interact with the agent to solve the task.
  - the idea , one of the principles behind the langGraph is no, no , we want control over whether
    or not we want to give the specific agent more or less freedom to act, how it should act
    and where it should send information.

2.Human in loop:
================
  - besides that , there is a human in loop,
  - there is a build in persistence layer that enhances the human agent interaction patterns with in workflow build with langGraph.

3.StreamFirst:
===============
  
  - streaming essentially is when you send a input to the model and you get a output, because the output might take a while
  - you want to make sure that you can stream output before you get to the final response.
  - there is a **support for the streaming of events and tokens** providing the real-time feed-back to the users.
    
    

  
 
