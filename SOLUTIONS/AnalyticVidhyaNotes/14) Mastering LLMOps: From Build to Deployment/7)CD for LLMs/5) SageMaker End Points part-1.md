SageMaker End Points part-1:
============================


    - so up to this point , we have seen how to take this LLM Models, how to deploy
      and then containerize using different platforms.
    - now in this video, we discuss about how to deploy llm using sagemaker.


Sagemaker Endpoints:
=======================

  - sagemaker has something called sagemaker endpoints
  - which generally consists of 2 things
      1) sagemaker module - module consits of module container
      2) 

1.sagemaker model:
===================
![image](https://github.com/user-attachments/assets/396dc9c7-fcc1-4f98-b94f-fe496f2721c3)

    - the model consists of model container in which you can bring your own docker container and just 
      specify the path from where it should be pulled.
    - model artifacts from s3.
    - so, this fetches the model data, the train model weights from amazon S3.
    - you also need to mention , what IAM permission role that particular sagemaker module will have.
    - this would allow access to resources such as S3 and other places where in code we would have mentioned
     that the model should be able to pull from other sources as well.
    - and then we also have network settings. if you want to configure the network preferences, we can also
     mention that in a sagemaker model.
    - now the sagemaker model then creates a end to end artifact. this artifact can then be used to deploy.
    - the way we want to deploy is something we mention in sagemaker endpoint configuration.
    - sagemaker endpoint configuration could be of three types:
       1) one is provision.
       2) another is provision async
       3) and third is serverless.
![image](https://github.com/user-attachments/assets/0dbb4fd1-0b26-449f-b2ea-046e6f603491)


Provision Standard:
====================

    - provision this standard deployment setup in which we take a container and we deploy it as webserver

provision async:
=================

  - Provisioned async deploys the container but the input and output is handled asynchronously.

Serverless:
============
  - serverless is offered on demand and the container is not present once the request is taken care of .
  - go deeper in to this in upcoming slides.


Model cards:
=============



![image](https://github.com/user-attachments/assets/b8c737af-2be4-432c-95f8-39e162206db7)

  - these are some additional features using which we can share the **model details with our team and stake holders**
    and we can add details such as what **kind of data it was trained o**n , what this model should specifically used for,
    some of the example data sets and **code that we want to also mention** and other details regarding what the model is all about and what problem it solve.

  - you also have something called data capture , in sagemaker endpoints, in which all the input and output data that the live
    model after deployment receives automatically can be stored in s3.
   - this can later on be used for automatic retraining and for other analysis and improvements.

Real-time inference:
======================


![image](https://github.com/user-attachments/assets/f0127f48-bf85-437b-87eb-067836e95842)

   - lets get in to first type of deployment which is Real-time inference.
   - in which as we can see here , we have sagemaker endpoints, which internally manages autoscalling group.
   - this is not the autoscalling group that we have full control over.
   - we just specify in our endpoint configuration, what kind of autoscalling that we are looking for.
   - sagemaker on its own manages the autoscalling for us.
   - then we have EC2 instances, these EC2 instances will then have their container deploy and it will
     have access to S3 prefix location from where it will download the model weights and it will start working.
   - now the single endpoint in sagemaker would have fixed url , that can be private or public and then we can use it
     to make REST API calls and get the response back.


Summary:
=========
  - we can deploy the model as webservers and keep them persistent.
  - which means it would be available 24x7, **and if there is no requests, the model still be deployed and still be charged
    for EC2 instances** that is provisioned for us.

  - we also have inbuild support for autoscaling , in which we just have to mention certain autoscaling parameters
    in the sagemaker endpoint configuration and autoscaling is taken care by sagemaker.

  - it is useful for high concurrency traffic in real time , and because the containers are always available and they
    scale up really well, this is particularly good for high concurrency traffic.
    
  - but most of the time, we should know what kind of traffic we are expecting and what are the high peaks and lows
    because the autoscaling still is going to take time in provisioning a new machine, putting the docker container on it.
    and also fetching the model from s3 and then starting the GPU server which might take certain time.
 ![image](https://github.com/user-attachments/assets/78f4ce3a-8d5a-4a0b-93f6-213f1d90f137)


  - so we have maximum 6 MB of the   request payload, so in the REST API body that we would supply which will have
    our input in the prompt, the maximum 6 MB should be size of the payload and 60MB would be response time.

  - so it is actually 60 seconds that should be response time in which we would be getting back the response.
  - any response more than that we would give error.
  - we have support for both CPU , GPU instances , so the EC2 instances that we mention over here can be
    CPU based or GPU based, based on our requirement.


  Hosting Types:
  ===============

     - what are the different hosting types in real time inference.

     - one of them being deploy and scale a single model type on instance, something you already have been seen before.
       that we have a sagemaker single endpoint having just one particular model put in to a autoscaling group using s3.
![image](https://github.com/user-attachments/assets/12bcce53-ec5d-47c9-9ac4-33b474b4aec4)


    - so, this is a single model deployment.
    - what we can also do is create another multi instance kind of deployment in which we mention that the docker container 
      is the same , its just the different model location have different weights which we can mention using prefix.
    - so, over here , the prefix looks something like this which the main key is the location slash model 1 is the
       folder for model1 weights (/model1) and model2 is the folder for the model2 weights and then  we can just
       create a configuration in which all these containers are same its just that model1 just have different folder downloaded.

     - apart from the docker container base image is same.
     - so these 2 are downloaded the model1 folder.
     - these are placed in to auto scalling group, and this is called a sagemaker multi-container endpoint.
     - based on the request, we can mention which particular model sagemaker should send the request to.

![image](https://github.com/user-attachments/assets/a82d3101-b0f7-4ad9-bb1e-0985331bc0a0)

     - if during the REST API, we mentioned that we want to send this to type model2 , then sagemaker will make sure
       that the request goes to this container , not this container and we get back the response which sagemaker gives back.


Summary:
=========
![image](https://github.com/user-attachments/assets/8090ec60-01e4-4e39-b5af-4477cb2916b3)

     - so summarize, in multi-model and single endpoint, we share instance resources between models.
     - so this EC2 instance would be having a GPU backed machine.
     - and in that GPU,all these three models share the same GPU.
     - most similar models that share the exact same container image .
     - so as we mentioned, model1 and 2 are exactly the same docker container. its just the s3 path and the 
       data that is downloaded , the weights of the model are different.
![image](https://github.com/user-attachments/assets/932022c8-411e-4877-bfcc-39cd0d126556)

     - different model artifacts are loaded from the same prefix folder .
     - the invocatino specifies the target module to be invoked.
     - and sagemaker autoscales different model types based on the invocation request pattern of these models.
     - so the advantages that we have is that we dont have to create mulitple sagemaker endpoint for multiple modules

![image](https://github.com/user-attachments/assets/43b16970-007c-4491-8179-61808a8ebeec)


      - making a multi container endpoint not just ensures that the request goes to correct container , but based on the demand
        sagemaker will automatically figure out which particular model type to scale based on what is more in demand.
      - so if model2 requests are more, model2 would be scaled more than model1.and this way we are efficiently using GPU and 
         CPU sharing saves lot of costs.

![image](https://github.com/user-attachments/assets/f62d30be-8496-49fb-89e2-b90a0b1d287a)

      - and we also have multi model with multi-container with single endpoint. we can host up to 15 different type of container 
        in a single endpoint. and so this is for the case where the docker containers are also different and there are multiple
        module .
![Uploading image.png…]()

      - we can put all of them into one single endpoint and we can mention different types of model that we want to call.
      - we can at max 15 different types of containers mentioned for a given single endpoint.
        and respectively , those containers with their own s3 path would be loaded and request would be served.
      - this is known as multi-model with muulti-container with single end point.
     
  

  



  
      

