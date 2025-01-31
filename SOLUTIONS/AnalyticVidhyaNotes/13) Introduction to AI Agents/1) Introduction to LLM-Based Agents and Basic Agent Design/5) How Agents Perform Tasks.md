How Agents Perform Tasks:
===========================

- what agents are ? their importance
- talked about the idea of levels of complexity.
- implementation of the agents.
- thoughts about 2 levels of complexity.

First Level:
============

- 1st level - just putting in the prompts and information about the functions and asking the model to
  call the proper function to solve the task.

Second Level:
===============

- 2nd level - openAI function calling which is very standardised way to connect llm to the tools.

Third Level:
=============
![image](https://github.com/user-attachments/assets/c40b99ea-04ab-4e00-be39-6fb53f576f3e)

- now the third level would be to think of idea of agent in a more florescent including something
  called the agent loop or react agent loop. which essentially means this is taken from
  very interesting article called langchain.
- idea here is that the llm takes input from user
- llm goes over the loop
- the loop is simple, the model has decision to make 
    1) it could either perform a action that could be search the paper, search wiki, checking the web, check whether  
       all available as action to be performed.
    2) or the model deems that it has necessary information already with in the scope of the training previous to 
       add connections to any actions, model can provide any output, provide final response to the user.

 - so the model can perform 2 things - can take action , can give response.
![image](https://github.com/user-attachments/assets/182927f1-e22e-4060-8728-72ef6be9ed0a)

 - if the model performs an action, the output of an action we call **observation** as show in diagram.
 - this observation gets fedback to the model , we go again to the same decision where model now has the initial
   query from the user and again it has possibility of taking either another action or  giving a output to the user.
 - that is the agent loop would constitutes the third level of complexity.
 - now we have real agent working to perform complex tasks.
 - because now the model is autonomously deciding what to do and when an output is given to the user.
 - that is the agent loop.

Good Agents are router:
=======================   

![image](https://github.com/user-attachments/assets/c51c4f0a-717b-4293-93d9-b6c6fc252d36)
![image](https://github.com/user-attachments/assets/11a13fe2-e522-4c98-8819-2fefefe51ccd)

 - there is a interesting idea, that good agents are routers.
 - good agents usually implements routing type procedures and architecture  that routes information in some
   meaninng way and leverages some llm with in the scope of routing procedures.

- langchain is framework that implements these procedures.

https://blog.langchain.dev/what-is-a-cognitive-architecture/

- 

