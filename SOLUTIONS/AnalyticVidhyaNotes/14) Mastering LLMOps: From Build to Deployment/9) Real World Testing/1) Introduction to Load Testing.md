Real World Testing:
====================


  - load testing in detail.
  - what is load testing and how it is done.
  - lets discuss load testing in terms of llm inference.
  - lets discuss loadtesting scenarios in terms of llm inference.


LLM Inference looks like:
===========================

  - in this diagram, we have g5.xlarge.instance , it has certain amount of CPU , RAM , GPU.
  - which enables to deploy these LLM containers and do LLM Inference.
  - This machine is  then connected to a network bandwidth with a maximum of 10GBPS available bandwidth
    and then is also connected to a storage.
  - lets say we connected to EBS Volume, but the maximum amount of transfer that can happen is 3.5GBPS.
  - this is all about the hardware that we are on.
  - in terms of request that would be made , we can see multiple users are trying to access the server
    and request takes certain amount of lag in milliseconds.
  - so that is the latency that the user faces in getting the response back.
  - multiple users are using this particular docker container , we can see that there is something called
    as throughput , which is token per second, which is at the given instance of time, how many tokens
    are getting generated through this LLM.

  - so, if we would have lot of concurrent users , then the latency would also increase
  - so , the game is between latency and the throughput , if we would have higher throughput , which
    means more tokens per second, which means more no. of users , we would see that it takes more time
    to process these requests so that these latency would also increases with time.
  - the throughput depends on the no of concurrent users and it is measured in tokens per second.
  - if we have higher concurrent users, we will have higher latency.

![image](https://github.com/user-attachments/assets/7cc51e3c-737d-4209-b3cb-266574a061af)

LLM Inference:
===============
    - Now, in LLM Inference, we have two things, 
      1) one is TTFT - Time to first token and then
      2) TPS - tokens per second.


Difference between TTFT VS TPS:
================================

![image](https://github.com/user-attachments/assets/ed128af3-5b50-4487-a8ac-3f37b6d21391)


Prefill phase:
===============

  - now, what is the difference.
  - in llm inference , we have something called prefill phase - this is the first time the 
    container has actually seen a request and the whole prompt is first processed in the LLM
  - and the output key values are cached in GPU itself.
  - this is known as prefill phase, before this time, the request never came.
  - Now, we have
    1) request
    2) we have text
    3) we process and computed all the query key and value pairs and then we saved the 
       whole output in GPU memory itself as cache which is also known as **KV Cache**.

  - this is pretty compute heavy because we have to do everything from scratch.
  - and this is also something that leads to small delay that we see in UI then we use the LLM
    in action.

Decode Phase:
==============

![image](https://github.com/user-attachments/assets/b08f48dd-45da-4c9d-890e-4b2fdab7e3e9)

  - then comes the decode phase.
  - once the **KV cache is filled**, all we have to do is use it to generate the next token and the
    computation **expense of the next token is only spent**.
  - we then add that **token as well to the cache**.
  - then we just **generate the next token** , so on and forth.
  - creating these next token are **not very compute intensive**, but yes, because a lot of key value
    pairs are stored , they are actually lot of **memory intensive**.
  - so, we see memory transfer overhead and the higher batch size that we can fit in to GPU,
    the more amount of tokens per second can be processed by the LLM.
  - so, in LLM , we have prefill phase, and we have decode phase . one is **heavier on compute side**
    and **one is heavier on memory side**.
  - this is how the LLM inference takes 
        1) we have **small initial prefill lag**
        2) then the **decode phase** is generally pretty fast.

How to measure for a given set of users:
========================================
- now, how to measure for a given set of users
- let say we deploy our application, and we can play along with certain different metrics, such as
   1) maximum no of tokens that can be processed.
   2) KV Cache size that we are ready to go for.
      which is trying to consume as much as available in the GPU.

- but ,even after all these what are the metrics for a given set or no. of concurrent users
  that would define how good the application is performing?.
- All of this is done using something called **load Testing**

Load Testing:
==============
![image](https://github.com/user-attachments/assets/694b7473-a8a7-41e9-9ce5-7bff82da754f)

  - in load testing, we have the application as a black box which means we dont know the internals of the application,
    we just testing it from outside.
  - we create a lot of users , now these  are virutal users and we then bombard using these virtual users in application.
  - black box testing focuses on testing the system's behaviour and features and not how it works internally.
  - now, load testing is the subset of performance testing , that generally looks how a system response to normal
    and peak usage.

Performance testing:
=====================

![image](https://github.com/user-attachments/assets/ff318e8c-4f82-4343-96a0-eda4bd4c6cf4)

  - in performance testing, as we discussed, we are bombard with more and more requests to see how it behaves during
    normal usage , but also at peek or highest levels to see what are the SLA numbers.
  - we are looking for slow response time, errors and crashes to determine how users and transaction the system
    can accomodate before the performance suffers
  - so, for a given set of users, we can get certain metrics on how the application is performing in terms of
    latency and then we can use it to define the scaling parameters or other things.
  - because now we know how good the application performs for what number of users.
  - we simulate real user behaviour using code, also known as virtual users.
  - so we can create these virtual users in code once and then we can simply spin up 100 to 200 or 1000 thousands
    of users would bombard the application at the same time.

  - now, these request are then bombared to the application and measure the critical metrics are measured.
  - this is all about load testing.
           
