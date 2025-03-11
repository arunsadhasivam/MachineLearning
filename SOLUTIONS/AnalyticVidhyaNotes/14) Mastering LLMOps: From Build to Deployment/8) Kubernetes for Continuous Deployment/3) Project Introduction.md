Project Introduction:
=====================

    ![image](https://github.com/user-attachments/assets/7ffc9979-de72-4d26-8703-dbf9f1551eab)

![image](https://github.com/user-attachments/assets/4df62d0a-6062-4514-9b91-583b60759033)

  - up till now , we learned about deployment, networking types like services and lets take it
    all together how different microservices interact with each other in kubernetes.

  - we have amazon kubernetes cluster ( amazon ks)
  - we know that we can create services and services are responsible for load balance to specific pods.
  - so, over here we have a **service type** of load balancer, which spins up aws loadbalancer and
    automatically sends request to relevant pods.
  - cluster ip does internal connection between different deployment in kubernetes.
  - here service type of cluster ip is created with name payment app on port 5000.
  - so, front end can simply can connect to cluster this  ip service type
  ![image](https://github.com/user-attachments/assets/589c5083-26bd-4825-8bfb-64a661910642)

  - now, this service (cluster ip service) is responsible for using selectors to find out the **label app type is react** and
    **app-name is payment** which might be on different EC2 machines and would automatically send the request send to this
    to these pods  above.
  - similar way the backend will communicate to deployment of database(paydb:5432)   we can see we have postgres 16.3
  - backend communicate through pay-db:5432.
  - so in this way multiple microservices are there , all are managed using replica-sets, replica-sets are managed by deployment.

![image](https://github.com/user-attachments/assets/6de41c2b-7d19-4933-99b6-695e8034bbb9)

  - deployment takes care of one type of applications , here it is react app. here you can see the backend and here it is
    database. all communicate using services . services could be of type **cluster ip or load balancer**.



  Important:
  ==========

    - they all communicate together through services.
    - service could be cluster ip or loadbalancer.
    - loadbalancer connects things outside of kubernetes - talks to outside world.
    - cluster type ip is internal to kubernetes - not exposed to outside world.
    - with this the whole things is managed automatically using kubernetes.
    - kubernetes takes care of managing them up and down and managing the lifecycle of pods and communication between them.


Project overview:
=================

  - for docker container , we are going to use for the llm inference a **container known as LORAX**
  - LORAX is a fork of TGI, TGI is a Text Generation Inference by hugging face which is a docker
    container specifically optimized for inference.
  - Now, as we can see LLMs are good for fine tuning and when it comes to inference , using the same container there are
    lot of things which we can take advantages of , which are not present in those containers.
  - for LLMs there are containers **which takes advantage of lot of caching that can be done in GPU** , and therefore
    optimizing on the overall performance of the application.
  - therefore separate containers are actually created for LLM inference.
  - one of the pretty famous one by a company called **pretty base is LORAX**


Advantages:
===========

  - state of art serving throughtput - which means that these are optimized to take more concurrent users
    and at the same time can do things like multi-LORA to be able to handle a lot of different types of users
    and higher throughput at the same time.

  - we have efficient management of **attention key and value memory with page attention and flash attention**.
  - so, basically these inference containers are very well in optimizing all the different   layers of GPU and
    can cache all the key and value that the llms generate and then this can speed up the inference speed.
   - because all of the key and value are cached, only the next token prediction calculation is something that remains.
   - so, in this way we see higher throughput and lower latency.
   - we can also do continuous batching of the incoming request, which is automatically internally handled, in which
     as the request are batched together the throughput increases and we have many quantizations available such
     as GPTQ, AWQ already supported by LORAX containers.
   - so then quantization can can help us decrease the memory foot print of these LLMs and to be able to deploy them
     on GPUs with less available GPU RAM.
![image](https://github.com/user-attachments/assets/6fa4949d-f641-45eb-bfd9-710990218c7d)

CUDA Kernels for optimization :
====================================
    - so they are also optimized with CUDA kernels and then they fuse a lot of kernels together to increase further on the
      time it takes to run these LLMs on GPUs.
    - this is end of LORAX

Steps to create project:
=========================
![image](https://github.com/user-attachments/assets/13902e15-1d28-42d2-95a4-03b987063583)

  - create a kubernetes cluster
  - then in that particular kubernetes cluster , we will create a deployment with our LORAX container
  - test our inference.

    

  
