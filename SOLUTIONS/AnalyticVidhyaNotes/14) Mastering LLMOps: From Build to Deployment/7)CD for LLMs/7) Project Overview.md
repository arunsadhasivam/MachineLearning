Project Overview:
=================

    - this is all about sagemaker deployment.
    - we have something called sagemaker project.
    - up to this time, all we did 
        1) sagemaker used for training and fine tuning of the models.
        2) sagemaker pipelines to create these steps to do end to end processing, training and deployment of models
        3) different types of inference(synchrnous,asynchronous, serverless)
     - what if we all of these usecases to be created as one of the artificat which consists of all these things
       packaged as one bundles , which we can then distribute to teams and they can use it right off the bat.
      - for that we have somthing called sagemaker project.
![image](https://github.com/user-attachments/assets/d0ea2fd4-fe50-4ba4-b4ac-8280b81d69c3)


1.Cloud Formation Template:
==============================


      - so we have something called cloud formation template, we then mention all the automation jobs using 
        cloud formation that we want to do 


2.Code repository:
===================

      - what are the repositories that we want to create , we want to create s3 and everything.
      - all of that can be put into a cloud formation template and then we can mention the cloud formation template in our
         sagemaker project.
      - we also have code repository , if we want to mention it in our sagemaker project.

3.SageMaker Pipelines:
=======================

      - they are sagemaker pipelines that we can create and put in sagemaker project

4.Sagemaker Exeriment:
=======================

      - sagemaker experiments to track the experiment output.

5.Model Groups:
===============

      - different types of model groups that this sagemaker project should create and 
      
6.Endpoints:
=============

      differnt types of endpoint  that finally should be made available.

SageMaker projects:
===================
   - once we have all of this , we package it together int to a sagemaker project , and we can then distribute to teams.
   - once they will install the project, using cloud formation template , they will have all the infrastructure 
     automatically created all the things would be at place, and they can just simply start using them.

   - this is a really good way to **fully automate** end to end **journey** of **LLM OPS engineer**

Summary:
========

![image](https://github.com/user-attachments/assets/e9858828-fb30-4f63-b190-c7a40fdb3553)

- This ensures we can fully automate using cloud formation.
- this also ensures no prone to human error.
- we can also enforce some security best practices that we want to put.
- we can set up template based on organizational needs.
- so once these templates are created, we can simply distribute to the teams and they can install it.
- and we can also enforce some security best practices that we want to put
- we can set up templates based on organizational needs, and so once these templates are created , We can simply
  distribute to the teams and they can install it.
- we can also use AWS provided pre-built templates and modify them based on our needs.
- AWS has lot of pre-built templates, and we can simply take them , we have sagemaker project ready
  we can look at the code base, edit it , make it our own template and distribut to our teams.



Multi-LORA Serving:
======================

   - After discussed all this, lets discuss
   - another really interesting way to host the llm models .
   - we have something called Multi-lora Serving.
   - as we can see in diagram, we have EC2 instance, inside the EC2 instance we have a docker container
     that has access to GPU that is available in that instance.
   - we then have the docker container first image saved in ECR Registry, and we have the model weights
     saved in S3.
   - we also have the base model , that is saved in huggingface and in one of the previous section,
     we actually trained a base model , the Gemma2B and put the final weights in S3.
   - now, we can load the base model, the adapter weights, and the base container image and can finally
     start the docker container.

   - this docker container has access to GPU , where it put the base model and then adapter that we trained.
   - what if we have not just trained one use case , but we have trained for multiple use case?
     1) we have adapter 2, adapter3 all of them loaded together
   - then when we do a request to the docker container , this docker container automatically figures out
     what adapter has to be used and then gives back a final response.
    - **in this way, we are loading multiple adapters which are trained for different usecase in to one single container
     and are able to give back response based on type of adapter or the problem usecase we want to solve**.
![image](https://github.com/user-attachments/assets/3fc89980-6a57-4841-b9a1-d921737c6402)

     - so this is **multi-lora serving**.
     - in which we are just having 1 EC2 machine, 1 Docker container , but we are able to solve for multiple
       usecases using all the adapters trained for those usecases during the sagemaker training phase.

Summary:
========
   - so to summaries previously in sagemaker pipeline, as we have trained a lora adapter using a basemodel
     and uses a supervised fine tuning based fine tuning using hugging face **PEFT** library.
    - we can have **multiple adapters fine-tuned for different tasks and then multi-LORA serving dynamically** loads
     and serves multiple **LORA Adapters** based on incoming requests that comes in.


![image](https://github.com/user-attachments/assets/8571ab47-0fc5-436c-9b3c-23a24d43964b)

  - so the incoming request simply mentions that this is the input prompt and this is the adapter name it is looking
   for , if the adapter name is not present in GPU, 
        1) the container is smart enough that they can load dynamically these
     adapters ,
       2) put in GPU, do the inference using the base model in the adapter and return back the response.
       3) then keep the model adapter in GPU until it is not used anymore or some other adapter takes its place based
        on the GPU memory size.
  - the increase in memory for multiple adapter is small as every adapter is around 1 to 3% of model weights.
  - this is something we have seen in LORA.
  - how using **LORA Adpater** , the final adapter rate is hardly 1 to 5% around that of the total modal weight
    and therefore , the increase of GPU memory is really small.
    thats why if we have the base model and we have more space, we can just load multiple adapters without actually exceeding
  - or being able to use lot of memory not too much memory is needed in GPU to be able to load lot of adapters.
  - 

    



  
       
