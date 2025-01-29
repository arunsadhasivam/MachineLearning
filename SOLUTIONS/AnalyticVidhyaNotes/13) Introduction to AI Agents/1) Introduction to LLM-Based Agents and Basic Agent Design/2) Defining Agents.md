Defining Agents:
=================

![image](https://github.com/user-attachments/assets/2858f0e2-080e-496b-8a7e-5e2b1a2b7355)
![image](https://github.com/user-attachments/assets/2bcfd655-93f2-4b95-a0ca-91b3e6ba3d66)
![image](https://github.com/user-attachments/assets/256a89fc-2d19-41b7-b571-f23c0249bdc4)
![image](https://github.com/user-attachments/assets/347300d2-d794-420d-954b-85c148d4d282)

  - Thought+Actions - can consider very simple framework.

![image](https://github.com/user-attachments/assets/652039d2-1d3f-4406-9e2c-44e0d5ac0e5e)


Thought+Action Example:
=======================
![image](https://github.com/user-attachments/assets/30af1afa-caea-47a2-a94e-edf066a24e1e)

  - decision making for online course
  - first initial **thoughts** , want to learn about agents.
  - then action is "go to internet and search & research a cool platform"
  - Thought " Analytic vidhya has a course"
  - Action " look up analytic vidhya courses"
  - Thought " analytic vidhya course by lucas  is awesome"
  - so not a bias thought at all.
  - the idea is combination of interleaving thoughts and action.
  - then action to enroll to the course.


Thinking:
=========

Think :
========

![image](https://github.com/user-attachments/assets/63cd72be-2078-4b6b-a708-26987d29e4a9)

Action :
========

![image](https://github.com/user-attachments/assets/ee8684b2-579e-43f1-96d6-091fa070b81f)


 - idea of **thinking** would be to think about the things we do in future , planning, ordering, prioritizing etc
 - when we think about **action** here , what we mean is the usage of tools things like search browse web.


 what is an agent:
 ===================
![image](https://github.com/user-attachments/assets/d691a6f2-0461-4825-b585-aa34b8732b36)


   - combination of llm and a tool.
   - llm means a large language model which can predict the probability of the next word,sentence and next token .

![image](https://github.com/user-attachments/assets/aba503e0-4429-4045-81c9-a0ee810ee0d8)

   - model that can predict what comes next. for e.g model might be trained and receive some input like "i love eating ----"
   - and output might be pancakes
![image](https://github.com/user-attachments/assets/d2e67013-6a8e-4557-afd9-f1e3bdde57ec)

   - what is a tool in the context? tool is something that can perform action in the real world.
   - in this context of this course, we are going to thinking about tools usually as python
     function that performs some utility functionality ,something that's is useful for some context.
     things like browsing the web and retrieving the result relevant to question.
   - or checking the wheather and so on.

Toolformer:
============
![image](https://github.com/user-attachments/assets/f04b67ba-6e1e-488c-8df5-b6d8b378bf3b)

   - LLM can teach themselves how to properly call external tools.
   - Interesting paper called toolformer cameout , what they observe is that "llm can predict the next word
     can teach temselves how to call external tools".
   - via external api to help them solve particular problems in particular tasks for e.g here model is
     using Q&A systems to discover who is the publisher of the new Journal Medicine and find out that is
     "massachusetts medical society".

   - or they can use wikipedia to find out.
   - so, these models can teach themselves how to call external tools.
   - tools here means python function.

React:
======

![image](https://github.com/user-attachments/assets/ec5878d0-4580-44ca-affc-1731bb8922e1)

  - Now Another paper which is foundational for current surge of interest and clickability and overall enthuiasm
    around agents. the paper is known as "react"
  - the paper says you could use interesting prompting techniques to incentivize the model to interleave thoughts, action
    and observation out of those actions in order to perform complex and interesting tasks.
  - you can see example of a react loop where the model starts by having some initial thought , which leads to perform a
    specific action , in this case , search.
  - the output of the action leads to observation which is then fed to next thought , action, observation and so on .
  - so you see where we took this idea of interleaving thoughts and action from.
  - so these 2 papers (Toolform, React) form the foundation for this idea of this basic loop of thoughts and actions to
    go downstream and perform interesting and complex tasks. 
