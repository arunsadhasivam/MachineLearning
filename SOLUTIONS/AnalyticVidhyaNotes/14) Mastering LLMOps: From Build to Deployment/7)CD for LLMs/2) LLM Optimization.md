LLM Optimization:
==================


![image](https://github.com/user-attachments/assets/911c65f7-8af2-4c86-b8bb-235b6ce92bbb)


- After having discussed how inference looks like
- what memory consumption goes through
- what is prefill and decode phase
- lets dicuss how we can now present this llm as end-end service to be used by end users.
- in this diagram, we have user first hitting the loadbalancer.
- the load balancer would be having dns address and the user would request the loadbalancer.
- the load balancer automatically load balances all the request between multiple servers .
- so these are simple webservers , which take the request and then forward a particular request to a model
  webservers.
- this is the llm application is.
![image](https://github.com/user-attachments/assets/690aead3-2f72-44dc-986f-952feac20c84)

- so , these can be on a regular CPU based machine and these one on GPU based machine.
- so, when we call to model webserver, when this spin up , they take the ECR Registry which is the
  docker container and then there is model artificat which is all the model weights saved , they also take
  that and then they spin up as model web servers.
- so, the webserver calls the model web server, gets the model web server's response back.
  may be does further processing or saves in database.
- then gives back the response back to user.


 Architecture:
 =============
![image](https://github.com/user-attachments/assets/097a3fb0-57f4-48ea-ba47-81d3196bf4b1)

 - in this architecture , we can see that we can use it as REST API, and also add support for streaming.
 - so, the caller can implement REST APIs and also REST APIs with streaming enabled to be able to get
   the token output as stream.
 - so, in that , the webserver streams all the model webserver's output and keep giving it back
   to the user for every request.
 - and  a simple REST api will be where the webserver will wait for the model's full response back
   and then will give whole response back to the user.
![image](https://github.com/user-attachments/assets/6d63ffeb-eb9e-4901-8110-60292e2740ed)

 - so, the **models are mostly on a GPU backed VM** and these **webservers can be CPU based machines**.
 
 - Loadbalancers, as we discussed,even distributes load to all webservers and automatically adds them as scale.
 - so, tomorrow, if the application scales up , there would be another server added here , so the same goes for
   the model webserver as well as. they will be also scaled up. (model-gpu, webserver-cpu)

 - loadbalancers will automatically will add new machines, discard machines whoes health check is failing.
   and make sure the request goes to healthier server.


 - so, what is the advantages of EC2 web services

Advantages of having Middleware service:
=========================================
![image](https://github.com/user-attachments/assets/fc1c2220-6d1d-47c3-bb3f-7ac0590bcae8)

   
 -  so , what is the advantages of this EC2 webservice? why cant we just **directly call from the loadbalancer** these model webservers
 - so, one is the llm framework dont have really have good web-app security, which means that all the framework that we have
   which are optimized for llm inference does not have all the features necessary for the webapplication security and so any thing
   it is, be it JWT Tokens or API keys or any kind of other SAML or LDAP authentication, we can make sure all of that happens
   over here and the application is well safeguarded and protected.

- and once that is the case , then we can take the request and send it to the model.
- otherwise if there are any security issues, we can just discard the request at this phase only.

we can also separately scale model and main applications:
==========================================================


![image](https://github.com/user-attachments/assets/d70dc882-2580-4850-85b9-0ad5b1acf766)

  - what is this means is our llm applications can be huge, one of the component of that is llm inference?
  - the application might be doing a lot more things.
  - so, the best way to do this that the application logic,the major of the chunk of application logic can be put
    in smaller CPU based machines . so we put all the app logic over here.
  - and the part where the llm inference is needed is then done on these servers which are GPU backed.
  - separating between the (cpu vs gpu) is this if the traffic increases for some different part of the llm application,
    let say that the llm handles payment and so if the payment increases ,we dont have to scale these servers which would be
    gpu based machine , and we can scale the cpu based machines, since the endpoint doesnt use llm so this ensure that
    scalling of the application only needs cpu scalling.

  - so, this ensures that the scaling of the applications only cost us these smaller cheaper CPU-based machines
    and not the Expensive GPU based machines . e.g for the payment

 - then the part of the llm application which does the llm inference will then call this model webservers, if that
   request increases, then obviously the model webservers will also scale more , then there will be a scalling
   of GPU based machines.
 - in this way, by segregating the application logic to make sure only llm based api calls to the model are made
   we can now separately scale the EC2 webservers of the application and the GPU based LLM.

  - and this can do a lot of cost savings, and we could see that GPU based machines and spining this up and scaling
    takes way more **latency than scaling cpu based** machines.

  - so segregating this is a good practing.


Control client-facing API Structure:
=====================================
  
  - we can also control the client facing API structure.
  - so, whatever framework that we are using for the model webserver, if you want to make any changes and create our
    REST API's or REST API's streaming. we can also do it over here.
  - and make sure that the structure follows that whatever chanages that we want to have.


 Integrated with tools like DB:
 ===============================

 - we also integrate with db and vector store.
 - for e.g we can have langfuse integrations,of the llm call that we are doing and all the request that we
   want to save it , these outputs and databases or send it to monitoring for langfuse.
![image](https://github.com/user-attachments/assets/608bbab7-69ba-4610-a7c6-a41ce842ddc1)

  - All of that would be done over here , rather than updating the model's code and taking the
    inference over there.
  - And so, in this way the application is more rich in terms of adding multiple features, doing more monitoring,
    saving the output in vector stores and db over here rather than using or chaning the model's web framework
    which it came pre-packaged with.
  - so, this is why it is good practices to have middle ware services in between.



LLM Optimizations:
=====================

  - discuss llm different optimizations techniques.
  - lets look different optimization techniques that we can inculcate when doing the llm based inference.

1.GQA Grouped Query Attention:
===============================

![image](https://github.com/user-attachments/assets/08529f30-a5b3-4216-936a-7d2fb7bd8eef)

    - one is grouped query attention, which is less attention weights than multi-headed attention for e.g LLAMA3.
    - so, the weight works is the attention layers in a transformer are attached to multiple pathways and if these
      attention layers can be shared then the total computation that needs to be done can be decreased.
    - this is not something we can change in the applications, but then there are lot of llm's which are created
      and trained with grouped query attention and therefore the amount of computation needed in them is less.
    - one thing we can do is quantization, which is decreasing the memory computation from floating point 32 to floating brain point 16
    - brain float 16 is created by google , which has same dynamics range as floating point 32 but the no of bits that we save
      and compute are less.
    - so, in quantization we change the full floating point precision that we are using for compuation to smaller size of FB16 of BF16
      or even 8-bit of 4bit modules 

    - this decreases the amount of compuation as well as the memory consumption too.
    - so the memory go down and computation that we need to do as well.
    - how can we use for existing llm.
How we use for Existing LLM:
=============================

  - we use the library called **bits and bytes** which can on the fly change the model's bit size to 8 and
    4 bits and this can be done on fly which means that if you already have llm we can use bits and bytes
    which will decrease the memory foot print.

 - one thing to note over here is , the output precision, or the **accuracy is going to decrease with quantization.**

 - so, we should realy test the application before deploying it , to see the quantization output are good or not.

Activation Aware Quantization (AWQ):
==============================================

- we also have something which is really popular Activation Aware Quantization (AWQ) in which we have to pre-compute
  the quantization and then deploy the application.
- this technique is proven to give much faster performance than libraray like bits and bytes and also less performance
  degradataion in terms of accuracy.
- the way it does all of the computation is that the **important parameters are preserved** based on weight activation
  that it goes through.
- so, there is a computation , that we need to do before hand, which automatically finds out which weights are important
  based on activation, only changes or **quantizes the other weights to smaller bits** and in this way we are still able
  to maintain a **good performance** and this technique also results in faster performance.


Summary:
========

- these are the 2 quantitation methods which are used a lot these days. 
  1) bits and bytes - out of box 
  2) Activation Aware Quantization (AWQ) - we have to make sure we precompute or llm that we use already support AWQ before hand.


- we have somethings KV Cache optimization.
- so, previously we saw whenever a llm call is made , for the first time, the whole output is then saved into cache.
- this is known as KV Cache, to optimize or efficiently store and use these KV cache we have certain library.
- one of them is 
    1) Flash Attention - 

![image](https://github.com/user-attachments/assets/361a06d6-5f10-43b2-8511-23978b5496ab)

1.Flash Attention:
===================

- one of the famous library is flash attention.
- it does something called fusing of multiple kernels together, 
- so, if there are multiple operations that happens in the LLM these different kinds of transformers operations can be
  fused in to single CUDA kernels.which is something that flash attention libraries does.
- it also effectively uses the GPU memory layers.
- so, we discussed that this cache is stored in GPU memory but then GPU itself has a lot of different memory layers
  and flash attention libraries jsut makes sure that the **KV Cache** that is stored is effectively used by different
  GPU memory layers to speed up both training and the inference.
![image](https://github.com/user-attachments/assets/3e131469-abc1-44e4-8240-4b4df7875f97)

Pagination of KV Cache:
=======================
![image](https://github.com/user-attachments/assets/5b30800f-557a-4c70-b4e8-6d6509c6db51)

- and then we have something called **pagination of KV Cache** in which saving **KV Cache** in non-contiguous
  block spaces in memory.

- so, there are times, when lets say we have one block of 10GB as one of the storage space,and if we just
  have a memory of 7Gb , so we save it in that space and the rest of the 3 GB space would go unused because the
  next block would come after this 10GB block.
- and so we see these places of memory that are not used, because saving of space was not optimized.
- The pagination of **KV Cache** ensures that there are no non-contiguous or wastage of these spaces up in between.
- and we just make sure that there are no empty spaces as less as possible and to optimize on it there are libraries
  which does these **KV Cache pagination** really well. 


Optimizations during request:
==============================

  - Optimizations that we can do during the request that hits the LLM application.

1.Static Batching:
==================
  - so, we have something called static batching in which multiple requests processed by the model at every inference step.
  - so, this is like having rather than processing one request having a batch of request and processing them together.
  - so, all request go through the **prefill phase and decode** phase together .
  - if we batch a lot of request together , then the latency would be less , but the throughput(tokens per second) will increase.
  - and so we can see what is the tradeoff that we can go through and we can also find out a good number which gives really good
    latency and throughput performance something in the middle ground based on the application needs as to what should be that
    number we want to go through.

2.continous batching:
======================
![image](https://github.com/user-attachments/assets/40c9c754-6bff-49ad-a115-69f9c9532088)

  - we also have continuous batching.
  - in which , rather than taking the request in a single batch and prefilling them together and decoding together
    at the same time.
  - we can also make sure we do this at random, which means that we will do token level batching, and so for 50 request
    that hit the llm , we would process the next set of tokens for these 50 requests, then we will see which request
    can be taken out and what new request can be added to the batch.
  - so lets say we get a new request, so we can for the next step ,just for that particular new request do prefill phase
    and then add it to this tokens to compute the next set of tokens.
  - so which is all of the application now decodes together and at some point at random , we will prefill some of the
    requests and some of the new requests that comes in and because we are checking at every set of token level
    batching phase which means we are checking after  every five or six steps of new tokens created.
  - we can then also see  which of the requests are complete and can take them out of the batch and send it back to user.
  - in this way, we are going to  do smart batching, then we can see good addition of advantages that we can get
    from batching , which is like higher throughtput  , more tokens get processed per second. and we can also
    make sure that we can easily swap in and swap out these request.
  - so, the latency can also be improved.

Summary:
=========
  - so, in static batching we have fixed way of doing inference which is just to have a fixed batch size and then prefill
    and decode together
  - but in continuous batching, we use a smarter way of batching the request and so we can **get better performance**
    in terms of even latency and throughput (tokens per seconds).
