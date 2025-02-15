![image](https://github.com/user-attachments/assets/ddffe68e-83c6-46ea-8e81-ba5661a29e33)Hands-on Session on Langfuse (Part-4):
=======================================


  - this is all evaluation.
  - now we go through the interesting feature that langfuse provide is dataset.
  - we can create dataset, and we can run evaluations before deploying an applications.
  - this dataset can be created using API.
  - now, i just run 
  

![image](https://github.com/user-attachments/assets/0ed9631f-f7f0-4d29-85ce-db4dbe172cbe)

1.Dataset creation:
======================
![image](https://github.com/user-attachments/assets/b19abf96-25ca-4be0-a8df-5e2eb9416692)

  - we create langfuse object
  - we can add certain items to the dataset.
  - this going to be simple one, in which we ask the module to tell the capitals of cities.
  - so, the input is Italy - > capital rome.
  - we just loop over this and create dataset using API


2.create or view dataset in UI:
===================================

![image](https://github.com/user-attachments/assets/25771b34-8b29-49ae-bcc9-a4214c0ae9b7)
![image](https://github.com/user-attachments/assets/4adc7069-dcc1-421b-8782-9d7632e09dcc)
![image](https://github.com/user-attachments/assets/b282127d-1808-4815-808f-bbcf507c3409)

  - in datasets, you can see in left.
  - a dataset known as cities is added.

![image](https://github.com/user-attachments/assets/49f3f1bf-7a12-46d7-9ed8-db1c4747b60e)
![image](https://github.com/user-attachments/assets/0f6a29d7-42e9-48c2-980d-500bb89fc711)

 - in the right we have something called items, click on that we can see that the input vs output
 - output is the capital of the countries.
 - Now, this dataset is created using APIs
 - what if we have trace , and we want to add this to the dataset .
 - the reason could be that we found something, which we are missing before
 - and then we want to add this check to ensure that our dataset grows with time.
 - we can simply click add to dataset.
![image](https://github.com/user-attachments/assets/5f2a301e-19e6-489e-ae8b-8121b8593aac)

 - we can select one of the dataset mentioned,we can select one of the dataset mentioned,
 - if you want to do any changes to input and output , and then we click on add to dataset.
 - in this way we can take a trace and then add to dataset  and keep growing the dataset with time.
 - so once your dataset is created you can run evaluations using langfuse during continuous integrations.
 - so one of the evaluation let say you want to make sure that the expected output by the LLM is matching  exactly the output
   that we have. it is similar to testcase of JUNIT

 - we can obviously take some other metrics we want like BLOW score ROGE L Scores.
 - but for now, we keep it simple, see the input that we give generate the output exactly as one of the output that we have
   in the dataset.


Test Function:
================
 - so now we will create function called getLLMOutput() in which we create a chat template by one of the system
   messages provided.
 - we create a variable called input message and then we have model 'gpt-turbo3.3'
 - we will have chain created and invoke the chain with given input message.
![image](https://github.com/user-attachments/assets/607e6084-1167-4b31-94f3-8d3fe72f6e3f)

 - in cofig we have callback lang_fuse_handler().
 - so , using this we can call the model with variable system messages
 - so, now we have the function ready which calls our llm as a chain and then runs the chain output ,
 - we can now create another helper function() which takes the whole dataset and goes through the dataset
   one by one and run evaluation on it.

![image](https://github.com/user-attachments/assets/ec5d43ed-7fd9-405b-a6b2-8b18d4f9dc89)

 - we create a function called runSystemPrompt() on dataset , which takes an experiment name and the
   system message and then we go through the whole dataset again . To call the dataset , we just
   click on lang_fuse.getDataset(), once that is done the code then go through dataset.items().
 - for every items, we ask a function getLangChainHandler() in which we just have to mention
   the experiment name. this is to group all the dataset items together for one experiement.

 - this grouping would really help us to create average scores and things like that.
 - and so that we just give it the experiment name and we have the langfuse Handler and then
   we can call the function getLLMOutput() which we just created over here in the input provided the country.

 - the system messages, we keep on changing based on the experiment.
 - we want to see which one works best and the langfuse handler is something that we created over here.
 - so , this runs , this will give us some output , the output response from here .


 - we will then use it to call the simple evaluation function which has the **item.expectedOutput**  which is
   the capital of that country, and checks it with our output that was generated now by llm using system messages.

Evaluation Score:
==================

![image](https://github.com/user-attachments/assets/fbc62798-2309-423a-b4d9-e682180843be)

 - thus the **evaluation score** and then we can just tell the langfuseHandler to trace and score
 - that the trace name is this , the value is whatever value we got and the datatype is Boolean.
 - the datatypes can also be numbers and string.
 - and we have different types of score based on usecase.
 - we just call langfuse.fuse() just to make sure all the data is flushed to cloud
 - and in this way, we have a function , in which we can mention an experiment name and a system prompt
   and a whole dataset will run on that experiment.


Run the prompt:
================

![image](https://github.com/user-attachments/assets/3de62c7f-e1e1-4ab0-b157-e105dfa0aabd)

 - so , lets load cell , and so we will now run this on three different function calls with different argument.
 - the first one will call this experiment as directly asked without output_parser
 - the second will call langchain asking specifically.
 - the third will be langchain asking specifically
 - okay , in our first attempt, we just asked what is the capital of following country , now this might lead to
   additional data being given by llm.
 - And the second one , is the user will input country respond with only the name of the capital . now this ensures
   that the output is just the capital.and the expected output matches with current one.

 - and this is also additional to it.in which our new experiment we try another prompt. yeah, which tells specifically
   that state only the name of the city.
 - now, we just run this . all these experiment run , and then now go to the dataset.
![image](https://github.com/user-attachments/assets/99ed4d61-067a-4761-9040-fa9c91f71bb1)

 - over here , we see dataset, click on it > then as you can see multiple runs > in items we see this was the data.
 - we can see different experiments.
 - now, these experiments run, and the total no of experiments we run 
![image](https://github.com/user-attachments/assets/4a87fe4b-d091-41e8-8edc-b8bf2c792012)
click on right
![image](https://github.com/user-attachments/assets/95f6e56d-1bb4-42c8-8f5e-27506a5f7b03)


![image](https://github.com/user-attachments/assets/44863f1c-4a93-4316-b868-46db3a8e4d92)

- then in runs , we can see partial data is already been uploaded.
- so it keeps on uploading data as it comes along.
- and then this run would also be successfully complete
![image](https://github.com/user-attachments/assets/abdbfa45-bc59-4f6d-8e15-c3f5e876f8a0)

- and we can see that the exact match was 0.7 in this case which is directly ask without parser.
![image](https://github.com/user-attachments/assets/78d78b53-399e-45be-b2ff-ad59f539a4d1)


![image](https://github.com/user-attachments/assets/3dba35e0-61e0-4cfe-a237-7035947c7f68)

 - why is that the case, if we can click on it you can see what was input , what was output
   what was expected output.
 - so the test failed because the score was not exact match, reason being the input
   that we are giving, the system message " what was the capital of country"
 - and it actually give the full-fledged output rather than "single output" so mismatch happened.
 - in this way , we can experiment with different system prompt , run it on dataset as multiple
   experiments.
 - so this can run as CI, and we can make sure that application does not go to any environment
   be it staging or production without the CI passing and matching a certain threshold.

 - so we can also see that there are score averages automatically computed here for all the scores inside that
   particular experiment.

Summary:
=========
  - so, this is all about langfuse ,
  - we see how use langfuse to trace all our applications, 
  - we also see ,how we can use langfuse with langchain using a simple langfuse handler.
  - we also explore lot of other features like evaluation,datasets, score.


