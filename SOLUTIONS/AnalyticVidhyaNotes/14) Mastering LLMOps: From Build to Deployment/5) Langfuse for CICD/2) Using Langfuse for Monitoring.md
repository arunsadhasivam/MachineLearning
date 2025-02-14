Using Langfuse for Monitoring:
================================


Langfuse for CI/CD:
====================
![image](https://github.com/user-attachments/assets/3b67500c-16b7-4fe3-a3a5-02fbd5cd423e)

  - in our ci/cd pipeline , we will be using multiple langfuse components.
  - langfuse can be integrated with langchain , which is a very seemless integratoin with python sdk.
  - we have versioning and release with langfuse.
  - for every version and release that we created of our applications, by default supported in langfuse
    and we can track the output specific to a particular version and releases.


Team and data Management:
==========================

  - for team and data management, langfuse has something called project and each project can group all
    the experiments inside it.
  - Users sign with single sign on and it also has role based accessed control support in which any user
    can be given one of the roles and based on these roles they will have permissions in the langfuse URL or the APIs.
  - so , 1) one could be owner which has all the permissions.
         2) one could be admin, which has all the owner features, except they cannot delete a project or transfer a project.
         3) then role called member , which is one of the default user role and
         4) viewer is another role they can only have read only permission
         5) member on the other hand has write permissions.
  - cloud based SAAS Solutions provided by default langfuse is hosted on cloud and we can directly use and integrate it
    using the APIs and can manage and see things in their UI, but if you want , it is open sourced and can deploy
    the same container  in our own organization and use that URL instead of main cloud based offering to be use langfuse.
 - so, as we discussed on-Prem deployment is also available, and the cloud solution is ISO and SOP2 certified.
 - this ensure that these security certifications are there in place , which means that the whole cloud solution is
   properly secured and can be used to host our sensitive data.
 - lets go through what tracking in langfuse looks like.
 - so this is a typical request, which on the left we have the user interacting with the application, the user had the
   user id - user123 and certain other meta data information as to which platform it is from which the user is calling our
   application.
 - once the call is made, it goes through something called trace. now this is what happens inside the python code , it is
   now taken care of by a function which internally does a generation of embedding then we have step called vector store
 - After this step is done, then we have prompt creation, and finally we have generation by LLM call.
 - after this generation is done, this result is returned by application to the final user.
 - that particular user in the same session, can call the application again, which means it is a new trace it enters
   the same python function again, there is a generation of embedding,
 - Another step happens is vector store , retrieval , the same prompt creation and llm generation.
 - so, this user is interacted with the application twice.
 - and in the same way, the user can interact in different ways .
 - and so multiple users can also interact , giving different userid and different metadata.

![image](https://github.com/user-attachments/assets/df281a06-afa7-4130-a03a-1c0bd72b4a9d)

summary:
=========

   - the trace in langfuse is typically represented as single request or operation.
   - a session is grouping of multiple traces, this grouping can be based on user or client name or any thing else.
   - then we have something called **span**
   - in langfuse **span means a unit of work**.
![image](https://github.com/user-attachments/assets/f8e59f73-69c2-46fc-a6e0-c39c7b38aa45)

   - so in our diagram, span could be an
       1) embedding generation output,
       2) a vector store retrieval ,
       3) a prompt creation using all these things
       4) and generation of LLM call.
   - the generation of llm call is specially known as generation.
   - because we have more information to be logged , this is a special case of span, in which we log
     the generation of AI model and also additional information on the prompt model in completion.
   - so this is what tracing in langfuse is, which is the core component of the langfuse ecosystem.
   - now, let see how all of these done in code.


CODE:
======

Langfuse Python Decorator:
=============================

![image](https://github.com/user-attachments/assets/50bcacb1-f346-4c30-863c-468be7b982ec)

- we have simple langfuse python decorator , which is called @observe decorator() which can be applied
  to functions we want to trace.
- so simply, we might be having a function which could be calling and doing all these operations
  and can simply annnotate @observe at top of this.
- what it actually does, is it tells lanfuse to capture certain things, which is the timing and duration of
  that particular function , function name , the function arguments and key value arguments
  by which it was been called.
- the return value is considered as output by that particular function.
- we can also have additional tags, metadata and IDS that can be added for that particular calls, which we can
  later see in langfuse UI.
- it also has support for callbacks in langchain.
- so, rather than decorating our function using @observe decorator , we can pass simply pass in
  a function to langchain chain .
- this will automatically take care of all the steps and send it to the langfuse ui.
![image](https://github.com/user-attachments/assets/e782b717-028f-4699-a30e-b1f04bac3883)

- Now, let see another cool feature of langfuse for prompt management.
- above , in this, we have an engineer or manager, we have langfuse solution which might be hosted on cloud
  or onprem solution deployed with in our organization.
- that particular deployment will have  different kind of prompts, and every prompt will also have other
  configuration metadata.
- and then llm application can be deployed in production, where with in the tag of production,it tries to fetch
  the prompt in real time and then caches the LLM with that particular prompt call.
- then user starts using the LLM application and also as you can see , these prompts can be managed on
  a central repository and can be edited by engineers and managers.
- based on cache interval, we can ensure that the new changes done to the prompts are automatically fetched
  in a given interval.
- so let's say if we set it to  one minute, after one minute, this cache would be invalidated and will be fetched
  again from langfuse deployment.
- it might be from the same prompt, or the prompt might be changed.
- we can also setup  default prompt values, so if the connection to the langfuse deployment fails, then the
  default prompt template can be taken.
- in this way, without deploying our application again and again and having to change the prompt , this gives
  us really good flexibility that engineers and managers can see the prompt and make changes in real time.
- And lets say if a prompt is not that good and produces wrong output for the end user, that particular engineer or
  manager can also rollback the prompt to a previous version.
- this makes the prompt management really efficient using langfuse.

![image](https://github.com/user-attachments/assets/58484082-c80b-4b6c-ba24-424f448c1397)

- we have decoupling enabled in which we have decoupled the prompt with our application.
- non- technical user can also create an update by the langfuse console.
- as we discussed, we can quickly rollback to previous version of prompt.
- the platform benefits is also that it can track the performance of this prompt in langfuse tracing.
- and so we know, which prompt was actually responsible for that particular generation.


Langfuse scores and evaluations:
=================================


- 

1.@observe():
==============

    - 
       


