SageMaker End Points part-2:
============================

    - what we have discussed till now is synchronous and provision endpoint
    - these are all webservers which are available 24x7 
    - what if , we dont want to have request response structure that should be real time in nature.
    - what if , if we can still have fix number of provision server which would process the request
      but want to do asynchronously.they are not criticial time bound to give back the response.
    - and this way we have more control over as to how many CPUs or EC2 instance we want to scale and
       put.
    - since not 24x7 so you dont need to webserver running all the time if up all time we need to pay
      so asynchrounous means we pay for the time we run the server.
![image](https://github.com/user-attachments/assets/a0d50d32-8ec4-4019-baf7-b17c97591366)

    - This is called asynchronous inference.
    - we are essentially decouple the number of requests from user to the number of requests we are
      able to handle using queue in between.
    - this has lot of advantages and sagemaker provides this in-built
    - this is known as asynchronous inference.


2.How asynchronous inference works:
======================================
![image](https://github.com/user-attachments/assets/14bac904-41e0-46ae-a8c9-8032157bc406)

  - so we have a user which has access to sagemaker asynchronous endpoint and over here user
    submit the request.
  - the request gets stored in internal SQS queue.
  - now this queue is subscribed  by multiple servers put inside a autoscalling group.
  - but what can be the autoscalling policy depend on us ,
  - you might want to scale for CPU usage or scale down and up based on memory or have some
    other parameters that we like to have and once these servers take these requests and process
    them , once the result is generated this is put in to s3 .

SNS (Simple Notification Service)
===================================

  - so this whole process might take some time, it depends on how many servers we want to keep
    in to provisional phase and how many requests have actually been arrived at this internal SQS queue.
  - so, the output is now present in S3 . what the user can also do after puttting the request is
    they can subscribe to an SNS topic.
  - so which means that they put the input that they are expecting a output for.
  - and then they simply subscribe SNS topic .
  - once the data is put in S3 , sagemaker can also generate an update to SNS topic.
  - so SNS is (Simple Notification Service) and when an update is generated , the subscribed users
    gets to know the data or results generated , ready to be fetched.
  - then the user can simply go and fetch the output from s3.
  - in this way, we have decoupled all incoming request and also the same time all the outgoing requests.
  - if we have certain usecases where we dont want to get instant results and output, we can use this.
  - and also this make sure that we dont lose requests , if we are not able to create an output of it.
  - so, lot of times in servers, 
        1)we have maximum no of connections it can handle,
        2) maximum no of request it can handle.
        3) if the requests overflow ,
        4) our requests actually not processed
        5) we get error.
  - in this case, no matter what SQS(queue) make sure that the message is put in the queue, even the
    message overflow, it might process slowly . but at the end Queue still have the input message
    and the next server in the autoscalling group can also process if one server dies or anything.
  - so , we can have mix of spot instances , that we have discussed before or on-demand instances
    and we can save huge amount of cost using asynchronous inference.


 Summary:
 ========
![image](https://github.com/user-attachments/assets/085f6da5-246f-4676-ad71-84e6c039e3a7)

     - provisional servers but call them asynchronously.
     - so these are servers which are available 24x7.
     - we have request with large payload sizes of 1gb.
     - we have certain limitations in the provisional phase , but in asynchronous , we can actually
       give the payload sizes of 1gb.
     - so we have certain limitations in the provisional phase, but in asynchronous , we can actually
       give payload sizes up to 1GB.
    - we also have now rather than 60 seconds, long processing time up to 1 hr.
    - we have near real-time latency , this actually depends on how many servers are provisioned in atutoscalling group.
    - decoupled infrastructure using Queue and Notification topics , so we have decoupled the input phase and
      processing phase .

    - we have support for both CPU and GPU instances.


1.Serverless inference:
=========================

![image](https://github.com/user-attachments/assets/9fa555a2-400e-4d69-9da6-fd6640240fea)

  - now lets get in to another type of deployment which is serverless inference.
  - now , in both the scenarios that we see before , real-time and asynchronous  , we have provisioned
    EC2 Machine in place.
  - in this one specifically, we have something called **lambdas**, in which once the request is received
    we create a docker in real-time to process the request and then after some time the docker instance
    is removed. which means that when there are no request incoming , there are no servers per see.
  - so we dont need to pay for compute charges, even though there are no requests , so this can save
    lot of cost and then another good part is the scalling that this provides .
  - so the way this works is sagemaker endpoint would be available in serverless mode.
  - it will have internal lambda service, which will create a small docker container whenever a request would arrive.
    the output would be processed by the models and will be submitted back to user.
  - these container after sometime gets discarded .



Summary:
=========

  - ideal for spiky traffic patterns with high concurrency limit.
  - in lambdas, we can scale lambdas up to 1,000 and even 2,000 concurrent lambdas request at the same time,
    which would be hard to achieve with servers.
  - because it take lot of time to scale up and down.
  - the lambda server not just ensure 1,000 or 2,000 users are able to concurrently get the request.
  - but this amount of concurrency quickly scale up and down as well , all of this will be handled
    automatically handled by lambda.
  - once there are no requests , there are no servers or lambda docker containers that you have to manage or pay for.


Cold Start Time:
=================
  - there is a cold start time, which is associated with the docker based containers.
  - the cold start time, is assoicated with the docker based containers.
  - The cold start time is essentially the time it will take for a container to be downloaded and to be startup.
  - the startup time is essentially called the cold start time.
  - so, during this time, the request cannot be processed  because the containers is still starting up.
  - afterwards, when the container is ready to take request, we are able to give it the request and generate the
    response back .
  - thats why lambda doesn't quickly remove the container , because it's now ideally available to be used
    for REST API.
  - so, it waits for another 5 to 10 minutes before removing the container.
  - this ensure that if we get a request again the next time, they get processed quickly by the startup container and
    we don't suffer with cold start time.

  - if we want to do it fresh and load a new container for every request .
  - so, this way we have cold start time, warm start time.
  - but the fixed RAM values ranges from 1 to 6GB  in size.
  - so, this is one of the limitations of the lambdas.
  - and that is also one of the reasons that we cannot have these LLMs put on serverless lambda function.
    because the RAM that is available is 1 to 6 GB .
  - we also **no provisioned GPU Support** and CPU is also that we mentioned based on RAM value.
  - so the RAM at 1 and RAM at 6 will be given different proportions of the CPU.
  - and we mentioned GPU support , so llm cannot be actually provisioned on this.
  - some really small LLM can be put on that and containerized and also the inference would be CPU based not GPU based.
  - we also have constraint on the container size of 10GB, that is the full docker container image size which also
    then gets a 5GB of additional storage attached to it.
![image](https://github.com/user-attachments/assets/8828d9da-eae5-4cad-b71e-0e4487fbc209)

  - the request that would hit the container service have certain limit which is the payload size can be maximum of 4 MB in size
    and it can run up to sixty seconds only. **if the request takes more than 60 seconds to process by the container** , the
    request actually gets an error.  

  - **so better to use custom AWS Lambda with up to 10 GB RAM with 29 second runtime**
  - so if we know for our use case, the model inference is way less than 29 seconds , so it could be 5 or 10 seconds in
    which we are absolutely sure that the lambda would be able to process the request , then it is better to use
    raw vanilla AWS lambda service rather than using sagemaker endpoint on serverless mode , which internally uses lambda.

  - if we do that we will have not 6GB max RAM limit, but up to 10GB RAM limit and 29 seconds of runtime.
  - which  is bit less than the serverless mode,

  - but as we mentioned, if it works for our use case, it is better to go for this one rather than sagemaker endpoints in
    serverless mode.

Batch Transform Jobs:
=======================

![image](https://github.com/user-attachments/assets/9c71957b-8677-4600-9a2a-d17658b4c163)

  - finally we have something called batch transform.
  - this is one of the step that we also discussed in sagemaker pipelines
  - this is used to get prediction for the entire dataset.
  - so, lot of times we dont have to provision a synchronous , asynchronous, or serverless functions or anything
    that needs a REST Api based request.

  - if we have a dataset that we want to process , we can simply have a batch transform job in which there is no
    endpoint and the servers are launched based on set limit of concurrency that we do
  - then the data is something that we mentioned, that data is distributed and copies to all concurrent transforms jobs.
  - they get processed, and then it finally saves the output in S3.
  - so the entire dataset is sharded given to all these concurrency jobs.
  - the output is then combined and put back in s3.
  - servers are then deployed upon completion of the request.
