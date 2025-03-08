Advance Deployment Solutions:
==============================


![image](https://github.com/user-attachments/assets/29783321-d484-48ca-b24b-bb4c15dcf748)

![image](https://github.com/user-attachments/assets/cf0c47d8-73be-4418-aded-53e8789a82e9)

- so lets discuss other container deployment solutions.
- before , what we discussed was having these os images created that we use for scaling up
  and scaling down.
- but we have a lot of other solutions in which we just have to provide the container .
- so , lets say we give the docker container and then we provide certain other metrics on how
  the docker container should be handled and then application takes care of deploying it and
  scaling it and all those things.
- one of the services in AWS is called Elastic bean stalk, which is a platform as a service has really
  easy learning curve and can do all these things for us.



![image](https://github.com/user-attachments/assets/167b22e4-4929-4332-b741-e91af19db1f6)


  - we can simply mention that our docker container needs this much  of CPU, RAM , GPU and it will
    automatically make sure that it scales it up , scales it down.

  - it can also provide automatic load balancing and then also the application monitoring of all these servers.
  - so, there are lot of solutions, which just uses these docker containers and will handle all of the other
    things for you so that we have a smooth deployment process.

Container Deployment Solutions:
================================

1.Elastic Kubernetes Services:
================================
  - then we also have other container deployment solutions such as EKS(Elastic kubernetes services).
  - so, Kubernetes was open source by google and then all these cloud providers adopted kubernetes in to their
    own platform.
  - the adoption of kubernetes in AWS is called EKS which is Elastic Kubernetic services.
  - And in the same way, we have AKS , GKE in Azure and Google.
  - So, this provides us the whole infrastructure as a service .
  - it uses the open source kubernetes version and there is a steep learning curve to it.
  - And so, in kubernetes , we can just, because it is open source they are lot of different third party solutions
    and plugins that we can use to get our job done.
  - but then there is a steep learning curve, it gives us more control to configure our container and to be able to
    change the behaviour of scale up and scale down.
  - And we have multiple other third-party open source solutions as well for different kind of plugings that does
    different things.
  - but at the same time, kubernetes has a learning curve to it.And if we are just getting started and we just
    want our container to be deployed and scaled , we might go for other services because there is a sleep
    learning curve attached to kubernetes.

  - then we have services such as ECS, which is similar to EKS , but it is a proprietary services given by AWS.
  - This works similar to EKS in terms of networking, infrastructure provisioning and all that.
  - And we have much more fine grained control over the container.
  - But i would recommend to go for EKS rather than ECS because of all the open source third-party provided
    solutions available.
   - this also has has the learning curve as steep as kubernetes.
   - And so , if we are going for such complex application management tools , then we might as well do EKS rather than ECS.


Sagemaker Endpoints:
=====================

![image](https://github.com/user-attachments/assets/c75be370-3245-4c53-a466-8c8cc3ece153)



   - we also have sagemaker endpoints that we used before to deploy our LLM applications.
     and we can also use multiple different flavors that sagemaker offers, which we would see in the
     coming videos by which we can deploy LLM applications.

   - And so, sagemaker gives a platform as service,it has very easy learning curve, as we saw in our
     hands on lab. and default supports for multiple LLM Models are also there.

   - so, this was all about creating web servers or REST APIs
   - what if you want to process LLM output asynchronously?
   - that is we have data available, and we just want to process and get the output of the data and we
     dont care about creating REST API which is available and live 24x7.

Asynchronous processing:
=========================


![image](https://github.com/user-attachments/assets/95510d23-5f78-4305-bfb4-2b19c20f4e14)

   - So , in this diagram , we can see that we are in AWS Cloud, there is a VPC.
   - we have ECR,which consists of image of our docker container , we have S3 in which we have the
     input, then we will create an AWS batch services .
    - the batch service will automatically provision these EC2 machines using the docker container that is available
      in ECR . they would run and they would create the output after reading from s3, they would process the output
     and then will put back the output in S3.
    - the way input should be sharded and given to these containers can also be decided and using this in AWS
     batch service, these servers are created , the output is generated and then these servers are simply discarded.
    - so, in this way , when the processing completes, there are no infrastructure as such, and we are not
      build for anything afterwards.
     - so the way it works is we can launch these containers using multiple services in AWS, which is EC2,Fargate or EKS.
     - so, batch can be used with these services in AWS to create these set of servers.


AWS BATCH:
===========


![image](https://github.com/user-attachments/assets/1ce6c53d-bdf6-4b0e-8770-d0f40d33783b)




     - so, scaling would be handled by AWS batch and resources would be removed after task completion.
     - we also have different support for trigger events.
     - Now, another type of asynchronous processing that we can do using webserver would be something like this.
     - we have a AWS cloud, and then a user makes a request by hitting the load balancer .
     - the load balancer selects one of the server , the server takes a request and put it in to the queue.


![image](https://github.com/user-attachments/assets/0eb9b6db-1e7f-428a-80f3-cb346c0cd231)

     - now this queue, will have input request saved, and would persist it and then there would be a set
       of servers in autoscalling group, which would be fetching these requests in the queue.
       
     - once they process the output , they put it back to s3.
     - and the webserver then tries to fetch the output from s3 and give it back to the user.
     - so, on the first request, when the request first hits the webserver, it is saved in queue and we
       respond back without the output processed.
     - then the application on the client side retries after fixed interval, and then the webserver
        checks if the output is yet processed or not.
     - if it is not processed, it will just reply back with success.
     - but once the data is processed, it can also reply back with the output of that particular request.
     - but what we have actually did over here is decoupled the amount of request that we get from the users
       to the no of servers that we want to provision to process the request.
     - Latency might get suffered, but if the application is not very latency critical, we can use this to decouple
      both these systems, and provide a really smooth scaling experience.
     - we can then control this ASG to just have the number of GPUs that we want to keep at at maximum , and then
      process the request at at fixed rate using the SQS queue.
     - so, this is one of the ways by which we can do processing in an asynchronous manner.
     - the latency might suffer a little bit, but then the throughput is something that we can completely control 
       and we can also make sure that the webservers dont lose requests when there is lot of traffic that suddenly
       comes in form the different concurrent users that are hitting the webserver.


Summary:
========
![image](https://github.com/user-attachments/assets/93fd013e-3224-4044-8613-d46ae65441c0)
![Uploading image.png…]()

  - As to summarize, we send request to queue for processing.
  - we use the queue to decouple the request
  - we can separately now scale models EC2 instances.
  - client-side code then retries to check for output.
  -  and if it is there we return back the client.
  -  
