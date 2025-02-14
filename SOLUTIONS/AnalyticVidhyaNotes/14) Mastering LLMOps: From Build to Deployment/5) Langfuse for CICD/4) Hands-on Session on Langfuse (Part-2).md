Hands-on Session on Langfuse (Part-2):
=======================================

  - langfuse 2nd notebook.

Integrate Langchain and Langfuse:
=================================

Step 1: env variable:
========================

    - integrate langchain with langfuse.
    - cache ttl seconds till that time dont go to langfuse.

![image](https://github.com/user-attachments/assets/bbd3ee0e-36dc-48a4-8c52-eb28b0fe3a38)


  
step 2 : get Prompt:
======================

![image](https://github.com/user-attachments/assets/633f1793-6f00-4383-9896-e09daa02eb0e)

![image](https://github.com/user-attachments/assets/72e2f053-4962-4601-bd1a-752216cd80cd)
![image](https://github.com/user-attachments/assets/baceb934-7178-4941-830a-8d5b586c4875)


- in this way switch and rollback
- another good reason to set the ttl cache limit is every new user prompt should not go to langfuse
  to fetch the prompt.
- because prompt wont change often.

difference between langchain vs langfuse format:
==================================================

  - in langfuse we have double curly brace {{context}}
    but in langchain we have single curly brace {context}
  - we can also see langfuse.config give us the additional metadata that we setup here.
![image](https://github.com/user-attachments/assets/b4518326-d798-4e68-9b5f-dd33cc894c44)
![image](https://github.com/user-attachments/assets/b9aa8828-8451-450e-b1ac-bb73c7c139be)

  - do all the things we do in langchain
  - we create an RAG application , like wikipedia dataloaders
  - we would chunk them up
![image](https://github.com/user-attachments/assets/016e8446-a998-4f4e-a845-b8cdf232b911)
  - we create a vector store.
  - this is same thing we did before.

![image](https://github.com/user-attachments/assets/f57cb6b8-62fa-4a80-a9c2-24a25a6ec70f)

use the prompt in langfuse:
=================================

  - now, in model call, we use the chatOpenAI model from openAI, but as you can see the
    model values is taken from the prompt.
   - as same the temperature.


Chain:
=======
![image](https://github.com/user-attachments/assets/3acf49d6-1446-44a6-b32e-b5d3f55eaf26)

![image](https://github.com/user-attachments/assets/35be3e46-6b55-4696-a787-5ffb3b4f68c9)


  - we get the prompt , convert to langchain specific format and create a chain.
  - now integrate langchain with langfuse.
  - now the chain is created, 


Langfuse Handler:
===================
![image](https://github.com/user-attachments/assets/cb4e3235-be58-41c8-84a7-2445bee99ac6)


  - langfuse_handler is just simple object which has to be given a callback to the **langchain** chain
  - so, during invocation, langchain.invoke() we will provide us the input , and in the config parameters
    we just give back the handler.
  - the handler can have the session_id, user_id and other metadata and even tags that we can give.
  - we call this , we will see that the chain run and everything gets logged in langfuse.
  - we also see langfuse_handler.flush() for smaller amount of time, in our server langfuse can also
    cache the data that it needs to send. this is to ensure that it sends the data in batch.
    but, if you want to send it exactly at that time , just to make sure that all the data is flushed to the
    langfuse cloud. we can just use lang_fuse_handler.flush().

  - once done we go to the console and in traces we will found that there is a new trace in which the
    user_id and session_id is exactly what we mentioned 

![image](https://github.com/user-attachments/assets/b17a0425-db60-4007-8ba6-26874b50424c)
    - if you click on this above , the whole chain has a ful fledged trace , there it took 2.2 s to get the
       full-fledged output.

![image](https://github.com/user-attachments/assets/fedc7c3c-f955-494d-b221-c7eeec4152c1)

    - span tooks 2.21 sec
    - then we will have runnable context and passThrough.

![image](https://github.com/user-attachments/assets/b80407a6-fb3f-46e6-8f4b-10aa4530bd48)
    - special type of span for model generation.

![image](https://github.com/user-attachments/assets/ed26d1b6-5cab-4249-9c98-3e5a80be5775)
    - you can see how many output token, total cost
    - langchain for the model it knows and it goes to langfuse , langfuse is also able to read
      the values and arguments about the model.
    - because the special type was generation.
![image](https://github.com/user-attachments/assets/ef14595c-b8df-4a78-a640-5d919d2be5e9)

    - because of this , model knows the model uses gpt-mini , langfuse also support , for that
      it knows the cost it took to call these api and thats why it automatically compute the cost.
    - the other parameters we supply like temperature.
![image](https://github.com/user-attachments/assets/5ce3f199-5d66-43e0-916f-b0ae7d195b1e)

    - now, we can keep on tracking the trace in our application.
