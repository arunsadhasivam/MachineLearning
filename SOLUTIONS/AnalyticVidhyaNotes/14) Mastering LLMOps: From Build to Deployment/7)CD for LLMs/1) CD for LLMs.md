CD for LLMs:
==============

  - why we use langchain to modularize the code.
  - we use langfuse to monitor the llm calls and end to end application monitoring and observability.
  - we use sagemaker pipeline, training to train the llm and retrain them.
  - once all of them is done, llm is ready to deploy, what are best practices and strategies followed
    to deploy the llm.
  - whole section focus on continuous deployment.
  - we look continuous deployment.


continuous deployment:
========================

![image](https://github.com/user-attachments/assets/93f11405-f452-40c4-8091-55446be7f6b8)

  - what is continuous deployment looks like.
  - we have automatic or manual trigger to application code base.
  - once the trigger happen, we build the code and containerise that.
  - once the containerize is done we can test.
  - when we do testing, we want to see that the llm behaves and gives outptut as expected.
  - this is the testing phase consisits of **some examples** .

  - what input and output excepted, we just matches **llm output to expected output**.
  - what we also do is , deploy our given container to one of the environment.
  - deploy to test,stage and deployed once deployed tested by qa and dev.
  - progress to next stage, automated approval or manual approval
  - once done of approval, then deployment of container happen in production.
  - this is how process continues with all new set of changes.
  - the final code changes are automatically deployed in production.
  - generally 3 stages can have many if it is critical goes through lot of stages for testing..
  - mostly 3 stages
      1) dev
      2) stage
      3) production.


versioning:
============

![image](https://github.com/user-attachments/assets/afe055b8-9eb8-4e84-91f2-df660eed1f39)

Understanding LLM Inference:
=============================
![image](https://github.com/user-attachments/assets/9681bcbb-49db-4f32-aa6c-d39fd76fde98)

- box represents (g5.xlarge) gpu attached  with max 20 Gbps.
- Models take token as input
- latency vs throughput vs bandwidth as tradeoffs
- latency measure in ms, throughput measured in tokens per sec, how many token pass to the application at a
  given app at a given sec. since multiple users are using. measure traffic as tps.
- higher the traffic , throughput , even though throughput will increase since more token are getting generated
  and more user are using, the latency is decreased. since it take longer for one request. since llm is
  busy in processing too many request at the same time.
- so throughput increases latency decreases.

LLM Inference (TTFT vs TPS):
=============================


- now we have llm inference.
- this is when llm deployed , now we are getting the output from llm.
- we have 2 things.
  1) one is called TTFT(Time to first token)
  2) TPS (token per second)
- so we have one of the phase called prefill phase.
- we get the input , so we submit to llm and the llm takes the inference of it and saves it
  all of the output as cache.
- so these key values which are computed in llm is cached in the GPU Ram.
- thats why the pre-fill phase is compute heavy.
- because this is the first time, for a given request the llm seeing this input and the prompt and then
  computes all the key value cache that happens inside the transformer architecture and then saves it in to RAM.


Decode Phase:
==============
- we hav something called decode phase, once all the input is stored, then all the llm has to do is to generate
  the next token, and next token and so on.
- then it keep doing this in cyclce and will just get the next token and do it it reaches the last or max_token reached
  or stop limit reached.
- this is known as decode phase.
- now, the decode phase uses the prefill phase KB Caching, which is the key value caching that happens in the GPU RAM
  to be able to compute only the next token.
![image](https://github.com/user-attachments/assets/627f79f1-239e-4c7d-a906-a9ea87031bc4)

- this is what the decode phase look like.
- so , **the prefill phase** -is compute heavy , it is seeing for the first time doing all the computation.
- **decode phase** - depends on the prefill phase just have to do the next token generation.
- so one is compute heavy (prefill phase ) and decode phase is memory heavy.

  Prefill Phase - Compute heavy
  Decode Phase - Memory Heavy


LLM Inference memory:
=======================

![image](https://github.com/user-attachments/assets/bf5d968f-fe17-4338-8ffd-99a03f9f40b9)

- so we saw that time till first token is the first token that we get and latency it takes for the first token.
- why we measure TTFT is the because this is the time when the prefill phase happens , and the first token gets generated
  and reaches to us in a streaming manner if we are using the LLMs. and then all these subsequent tokens we have seen
  in the live applications comes really fast.
- that actually the decode phase that happens.
- and now let's see what inference memory consumption goes through.
- the model weights all the parameters are loaded to GPU RAM.
- this KB Caching of the prefilled phase depends on the batch size , all the computations done is saved in the
  GPU itself for a given request.
- this also going to take the storage space.
- the KB's size is few GB in size , and the reason being all of the parameters of the transformers outputs are saved
  into the RAM.
- so , for multiple Request , this starts to be bigger and is GB in size.
- so we even though higher batches is better to be able to get more TPS , which is token per second but then
  this is also going to consume a lot more memory of our GPU.
![Uploading image.png…]()




