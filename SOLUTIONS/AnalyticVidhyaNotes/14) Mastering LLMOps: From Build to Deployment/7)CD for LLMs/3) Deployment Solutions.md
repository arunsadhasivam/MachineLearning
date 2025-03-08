Deployment Solutions:
======================
![image](https://github.com/user-attachments/assets/bf491617-569d-4a22-bbf0-1b00aece4703)

  - different deployment types.
    1) ollama - which is the one of very popular libraries which enables us to local testing of open model
       
    3) 


1.Ollama:
==========

  - very popular libraries which enables us to do local testing of open models.
  - quick to setup
  - we can interact with cli and rest API.
  - the reason to mention ollama is the convenient it gives to be able to test these new models.
  - ollama can be simply installed and downloading and running a new model is just 1 line of code.
  - and so for local quick testing , using ollama would be really good choice.


2.API by sagemaker - services:
================================

  - we can also uses sagemaker based services for testing.
  - one of the services that was introduced for machine learning is bedrock.
  - and use this for the new foundation model, that we get , we can just use pay-per-use model in which all the
    API we will make would just be costed, just like any other services and we just have to do the api call
    rather than deploy the whole llm ourselves.
 - we have provisioned throughput option for higher usage .
 - so, if you want to make sure that the time it takes for the inference is less, we can also make sure that some
   of the LLM are reserved for us and that is what the provision throught can be used for.
 - we have to pay more for provision throughput but then also the latency would be less now.
 - we also have the posibility to train the foundational module , and deploy it and still use it as api.
 - the advantage of this is , region specific, so for e.g if we train and deploy for our region and use the API of bedrock.
 - we can make sure that the data still resides inside the given region.
 - we can also have other 3rd party api providers.


3.ReadyBase or OpenAPI or Anthropic:
=====================================
![image](https://github.com/user-attachments/assets/022fa13d-1a5b-4516-b22c-91d2c1d3013e)

  - gives us a pay per use.
  - the data boundary for some of the case is not defined.
  - for openAI azure based deployment, we know the particular region that we would be using , we can use that
    particular region to make sure that the data does not go out of the given specific country or jurisdication boundation.
  - but then we also have APIs which doesn't provide us which region they are going to be deployed in.
  - we also have cases where we can finetune these APIS and use our particular dataset to train these models and then
    use the fine tuned endpoint.
  - so, finetuning is possible but not as equal as fine-tuning ourselves.
  - these 3rd party providers can also fine tune basically and you can use these APIs for our own purpose.
  - A lot of times, we dont require to deploy our own llms but we can use these APIS beforehand just to make sure
    that our case is very well solved.
  - and if needed we can only go for training , finetuning and deploying our own methods.



Bare Metal Servers:
=====================
![image](https://github.com/user-attachments/assets/4604a2cc-2b62-46d3-8bfd-c4c7b821c324)

  - lets look at the cases where we want to deploy our own llm , to be used for the final users.
  - in this diagram, we have users,users are going to hit loadbalancers
  - in that loadbalancers, it takes all the request and it send it to EC2 machines.
  - Now, we can see some of the machines are spot instances, some are CPU based , some GPU based.
   and all of these machines scales up and down based on one of the configuration in AWS known
   as **Auto scalling group.**
 

  - So, when we put it on group, these applications based on certain parameters can scale up and scale down.
  - these parameters could be 
        1) cpu usage or.
        2) memory usage

  - that these machines going through, and based on configuration they would scale up or scale down.


Bare Metal Servers - Custom VM Images:
=======================================

![image](https://github.com/user-attachments/assets/ba72d7bc-c4bd-444b-a435-18898c488869)

  - so, in bare metal servers, we can use custom VM images, having the webserver installed.
  - so, once we get these EC2 instance , this would have one of os such as ubuntu already installed.
  - but we still have to install docker.
  - still have to pull these images from container registries and write down script to start the servers.
  - what we can do is? do all these operations,and also put the startup script to start the servers and
    then recreate this os and package it somewhere.
  - what that does is ? whenever these machine are going to scale and new machine gets added it will already
    have docker installed in it , it will already have the model pullead and the script and we can write down
    the what the startup script looks like and
   - what command has to be run and these machines then directly start the deployment process of llm
    that is present already on the os image.

  - we can create these modified os images whcih can really help us lower down the time it takes for the server to be
    ready with our llm application.
  - we then have as we discussed automatic scalling based on metrics CPU and memory .
  - so, we can have one of the auto scalling group configuration rules such that if the average CPU utilization
    goes above 70% then scale the server with this particular configuration where we can mention certain other values
    to scale the server to scale up or scale down based on the needs.


Spot Instances:
================

  - in this multiple users of AWS cloud are bidding on certain number to get hold of certain EC2 servers.
  - so, we do get these servers at at cheaper cost , somewhere around 70 to 90% cheaper but if somebody else
    bids for a **higher number for EC2 instances.this EC2 instance can get discarded** from our account and
    provisioned to some where else.

  - so AWS just provide us the 2 min around window to be able to do the application backups or whatever changes
    that we want to do before the machine taken out and these are known as spot instances.
   - the advantages of this is they are extremely cheaper compare to on-demand servers.
   - on demand servers AWS does not take it out. we actually control the whole life cycle.
   - we mention when the machine are stopped or terminated as to when these should be taken out of the account.
   - but spot instances can be taken at any time.
   - so spot instance we dont have control, if any body bids high you will be terminated from using.
   - so how we can use this for our advantages ,  is this we can create an autoscalling  group with multiple
     different types of servers.
   - so, as you can see some of the servers were spot instances and some mix instances were CPU based , some could
     be GPU based , and we could use a mix of these instance types to create our autoscalling group.
   - and so if suddenly this server is taken out , by AWS we can make sure that the load balancer supports
     some of the different techniques such as round robin in which the next request goes to the next server
     and it will just make sure that these request are evenly distributed and if the request fails because server actually got terminated.
   - the user application that is facing the issue, should be good enough to do retry and in the next retry the load balancer
     will send it to another server not the same server again.


   - this ensures , that if we put something like client-side retries, application retries and then if the application is
     stateless which means that even if this get discarded at any moment it's totally fine there was no important data
     or state which was stored in the application that needed to be taken out and we can just simply start another new server and start processing requests in that.

  - doing this, helps us in saving a lot of cost , and then we can then use a mix of spot instances and other instances which are
    on-demand instances to create this application scalling which is high on performance because there are
    lot of servers that is taking these requests and also high on cost saving
   - because we are using spot instances and along with on-demand ones.
   - so these are known as mixed instance type. which makes possible to configure combination of on-demand and spot instances.

   - this paradigm exists not just in AWS but also in GCP and Azure cloud providers as well.
   - so, we can use this same type of techniques in these cloud providers to do high cost saving , and high
     scaling and performance.

        Mix instance - spot instance + on-demand instance.
     


Server based deployments:
==========================


   - CPU VS GPU VS TPU VS LPU
   - so some of the applications if they dont require very low latency what we can do is
      1) we can put them on CPU based machine , this will create very high latency and throughput not good but
         saving cost . because the application is not time critical.

      2) GPU based inference - GPU would be used for inference this provide low latency and higher TPS which is
         throughput , but cost is more.

      3) TPU - which is one of the different version of GPU by google these provide higher performance than regular GPU.
         for some of the google based tensor flow   based applications and these TPU can be used other libraries
         as well. they provide  a bit higher perforance then regular GPU.
     4) LPU - language processing Unit , which was introduced by GROQ2 so this is another iteration of GPU
        and these are specifically made chips for LLM inference and this is properitory by Groq and seen
        really high TPS(tokens per second ) generated using these chips.   

     SNO  |     CPU                         |  GPU
    ------|---------------------------------|-----------
     1    |   1)high latency                | 1) low latency
          |   2)low throughput(TPS)         | 2)high throughput
          |   3) low cost                   | 3) very high cost.
          

      - this is also something looks forward to.
      - if we have certain applications which are time critical we might need to use GROK based APIs  to be
        able to provide that level of latency.
      - something like call center , which might not be possible to automate using AI by using
        CPU , GPU or even TPU based machines. but LPU by GROK2 can give such a low latencies that
        we can do real time service calls based calls using these inference APIs.
