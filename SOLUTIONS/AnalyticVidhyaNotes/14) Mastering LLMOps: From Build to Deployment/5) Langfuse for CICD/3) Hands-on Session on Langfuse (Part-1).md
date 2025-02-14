Hands-on Session on Langfuse (Part-1):
=========================================

  - working with langfuse
  - install langfuse python libraries.
  - use langfuse to connect to the langfuse cloud deployment
  - use sagemaker for this.


Step 1: go to sagemaker : domain:
==================================

![image](https://github.com/user-attachments/assets/6a914544-9df6-4fe4-b1ad-c04c330c7a89)

![image](https://github.com/user-attachments/assets/3afbd871-13af-4e86-805c-d2136155677e)

  - open a sagemaker studio, click on jupyter lab, and then run our notebook.
  - make sure instance ml.t3.large is selected.
![image](https://github.com/user-attachments/assets/334f8d70-e9b4-40ff-a044-5d384dd57e97)

  - see jupyter lab.
  - go to dhsworkshop folder
  - go to notebook
![image](https://github.com/user-attachments/assets/3fe34bd6-b931-4b2b-b541-6cbcab3232f1)
![image](https://github.com/user-attachments/assets/077789ce-4aa1-46c8-9fec-295c8fcf47dd)

  - click on 2nd folder langfuse.
  - once we have langfuse folder open,


Step 1: set up key:
=======================
 
![image](https://github.com/user-attachments/assets/e61870e7-3b3d-455a-831c-92ae19127427)
![image](https://github.com/user-attachments/assets/4f845399-508d-436b-855b-9edb0ced0558)


  - langfuse dashboard can be found at https://cloud.langfuse.com
  - once you go to that , you will be told to create a new account
  - signup using gmail profile.
  - now login into dashboard.
![image](https://github.com/user-attachments/assets/e4a3e195-55f5-41b0-85b8-9a20113eae26)

  - create a new project demo-2
  - this create a new project (demo-2)
  - we have project created where multiple user can collbaorate it with each other.
  - now this is one of the deployment  at (cloud.langfuse.com) , which means that docker container and
    all the infrastructure needed to run this is actually hosted on langfuse side.
  - we always have the option to take these docker containers, run it on itself.
  - and in that case the host name changes to whether the name internally.
  - in this one we have created a new project, and to be able to connect to project programmatically, we'll create api keys.
![image](https://github.com/user-attachments/assets/f76935b3-8865-4723-8e0b-dc80df3bb977)
![image](https://github.com/user-attachments/assets/c239d2ab-c7a5-4060-b957-1fbdfe8d6929)
final env key file
![image](https://github.com/user-attachments/assets/29ad4550-a5f9-4a81-9680-81c601d42106)

  -  and for the secret key, public key enter the value.

Step 2:see lot of options
=========================== 

    - click on playground , we can work with lot of different prompt and different model providers
      and use it to be able to experiment with multiple different prompt types and prompt models.
      and all these hyper parameters
    - As you can see, there is no model, you can click on add new model.
![image](https://github.com/user-attachments/assets/18996bc8-97ce-4e8c-99f4-3a012926bbbd)
![image](https://github.com/user-attachments/assets/e1c29f03-d33a-4408-a01e-58560baf6248)

    - currently it supports openAI, anthropic, azure.
    - you can directly connect to ui to make api call.
    - this does not actually make api call from the browser to openAI, but send it to the langfuse
      backend, which then calls openAI on our behalf.
![image](https://github.com/user-attachments/assets/f3ad127b-82a8-4d2a-aaee-5f5e0c174a33)

    - on the right now , we have openAI model ,the key just created.
    - and then we have option to select different model names,set different temperature , output token limit 
![image](https://github.com/user-attachments/assets/ce51e3b7-5794-41db-9fe7-29e6a34d4d67)

    - as we can see api key is secured with langfuse platform.
    - now you can enter anything to get response " you are an doctor"
![image](https://github.com/user-attachments/assets/a6411cfd-efb9-4630-8e1f-52979ea1029c)

    - as you can see questions about our wellbeing?
    - in this way , we have given different system and user prompts and this is working fine .
    - so , this is a little about playground.

Prompt Management:
===================
![image](https://github.com/user-attachments/assets/a893c1c9-d8ee-4371-be48-3b8c3153be4f)

    - now head over to next set of cells.
    - we have something called prompt management,
    - so the prompt that are hardcoded are actually be upload to langfuse as well
    - then we can manage the prompts from langfuse and get it in to our application code.
    - so for prompt management, in the dashboard > left > we have prompt > add new prompt
    - we add prompt and supply context.and this is just a system message saying " answer this questions using provided context only"
    - we just given this name "rag-based-prompt-with-context"
    - as you can it automatically detected a variable called {{context}} because of double curly braces we have.
    - along with prompt , we can also set additional metadata.
![image](https://github.com/user-attachments/assets/77e101eb-939d-4f6d-bf91-b046ccfb0ab1)
     - we also have chat based prompting templating in which, just like we saw in the play ground
     - we have the option to mention user or system and then mention the input  that is given.
     - so this createa prompt . create prompt > click on this button
![image](https://github.com/user-attachments/assets/87674e2d-1765-40b0-8fca-bf3c55b12044)
![image](https://github.com/user-attachments/assets/523e6b43-ef3a-41ee-b4df-ffb13a7f2c79)
![image](https://github.com/user-attachments/assets/d5826135-9b7d-45fe-be4b-b3c859fbf969)

production version
![image](https://github.com/user-attachments/assets/cc99f2f4-8228-412c-aa35-67c8931f3b66)

     - this finalizes our prompt.

   
    
Decorator based integration:
=============================


![image](https://github.com/user-attachments/assets/e8e95433-0424-4b72-a4b5-85caa9c883ab)


    - takes a langfuse context using variable called langfuse context.
    - then update the observation with specific data.
    - we want to know what was the input and for that , we are going to provide in the key-value arg
      one of the value as messages and this message will enter in to input.
    - because the generation type was used, langfuse is specially made for llm call generation.
    - we can then use this to specify these set of parameters.
    - as we discussed, the generation is special form of span which is specifically created for model.
    - we have certain additional parameters, when we want to update observation.
    - one of them being input, model and the additional metadata.
    - so for input, we have entered the message, 
    - for model we can specify the model name that we will also be given.
    - for metadata , if there is any other information that we want to act, we can have it over here.
    - and then not just the current observation, which is related to the model , if you have old trace
      and for which we want to add metadata we can simply add langfuse_context.update_currenttrace()
      in which we will enter the session_id and user_id otherwise some other values will be provided.
    - we also have metadata for the whole trace if there is anything else we want to put.
    - over here , we just put down key called is_openai and bool 
![image](https://github.com/user-attachments/assets/0f7f20e3-78b4-4e1b-a991-1d804ef3ec5c)
    - we can add additional metadata to traces.
    - later on on the UI , we will be able to filter based on values of the metadata.
    - also , we have openAI imported, 
    - so openai.chat.completions.create() will create chat completions and supply the arguments.
      in the format exactly open ai wants.
    - the main cell in the function in main() we have 2 parameters  sesssion and user_id
      and just call the function with session_id and user_id.
    - and then we just specify the additional key values arguments exactly like open ai wants.
![image](https://github.com/user-attachments/assets/0f657ee3-cf45-4f08-8d2b-cc34d1a26d99)

 ![image](https://github.com/user-attachments/assets/bcb2f540-6854-40cb-8584-2ee9103d9d59)
   ![image](https://github.com/user-attachments/assets/14001fcd-8df4-40db-86d6-7c9acd19d759)

    - run click on traces
![image](https://github.com/user-attachments/assets/ed5e7cb2-6435-4833-afa5-38b98425d858)
![image](https://github.com/user-attachments/assets/d866bb5b-2e7e-4372-970f-f76ceae7558f)
![image](https://github.com/user-attachments/assets/02e914a4-d3e1-4c4a-a7a7-5c56b41438fd)


![image](https://github.com/user-attachments/assets/67964be8-1aac-4e3a-bdc2-cef7dc284819)
![image](https://github.com/user-attachments/assets/9743a83b-9d8b-48c3-9212-e28fee855b2c)

    - session_id by different users
    - on left we can click > sessions > you can see all of your sessions.
    - one of our session is android or any name you want.
    - have multiple user id
    - each session we can find out what was input and output generates.
    - we want more exact trace in more details,for user_id alice you have trace available
    - you can see generation and trace values.
    - this way you can group, multiple users in session.
    - you can also create users and once users are created, you can see how many each call 
    

    


    
