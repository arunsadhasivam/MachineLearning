Project introduction:
=====================
![image](https://github.com/user-attachments/assets/b48a5ca3-94a6-4127-9124-26edd8e8d14b)

 - discuss on project to work on 
 - To set a bit of context, we have lot of modules such as 
   1) Qwen2 by allibaba.
   2) llama3 by meta
   3) Mistral series of model and so on .

 - These are the open source models which are currently performing comparable and in cases
   perform better than properitery model like openai chatgpt.
 - so currently we can train these llm, and get the output which is better than the
   proprietary versions like openAI's chatGPT or bi-anthropic cloud to really good margin.
 - currently we can train these llm and get output , which is better than even properiatory counterparts.
 - for inference of 1 billion parameters at 32 bit floating point precision requires 4GB of GPU RAM.
 - how did you calculate that.

calculation:
=============

   - Full precision 32 bit takes 4bytes.
   - To put 4bytes and 10 raised 9 parameters, which is 1 million parameters equates to 4 GB of VRAM.
   - this is GPU Ram , which is much more expensive than the cpu one.
   - so llama3 70 Billion model will take 280GB of VRAM and if you want to deploy it , lets take an
     AWS EC2 machine like p4d.24xlarge which has 96 Vcpus around 1200 cpu ram, 8A 100 GPUS which equates up to 320 GB 
     for gpu ram.
  - Now, one hour cost is $32.77 dollars which equates to 19.7 lakhs month cost , just to able to host llama3 70Billion
    parameter model.
![image](https://github.com/user-attachments/assets/b759a9c1-0efb-4f3b-86b9-4beb57940193)
  
  - so , inference by this model is super expensive.
  - And, if we go for the full fine tuning , we see that 1 parameter that we discussed before at full 32 bit precision
    during becomes a total of 6 parameters.
  - 2 parameters additional for the optimization state, 1 additional for the gradient, and 2 for the activation and 
    temporary memory.
  - so, instead of having 4GBs for 1 million parameters, during training it actually requires 24GB of VRAM.
  - so 6 times more RAM is needed to be able to train these models.
  - there are other issues as well with full fine tuning. 

![image](https://github.com/user-attachments/assets/8c7d17cc-9f5f-4b28-8b3b-d69fafaadaff)

  - for example , we have large memory size that we discussed before maintaining and deploying multiple models, a single
    base model is going to be GBS of size and if we train another model , we have to store weights of that as well.
  - this leads to huge base model, that we need to store, we have to deploy and have to manage multiple version of it
    which are very difficult to manage.
  - there is something called catastrophic forgetting of the fine tuning, leading to poor results on general tasks.
  - so, if you have your dataset , we train it on that particular dataset, we see that the model stops performing not that
    well on the other generalized or other tasks in general.
  - because it is been trained and fine tuned on that task.
  - so , this forgetting principle is something, that we should take care of . because for some cases , we also want our
    model to **do good on other usual tasks**, as well as to do better on one of our fine tuned tasks.


  - And so as to able to train, we have multiple training techniques such as SFT(Supervisied fine tuning) , RLHS(Re-inforced
    learning based human feedback) ,PPO,DPO and so forth.

Super vised Fine Tuning:
=========================

![image](https://github.com/user-attachments/assets/50ff3647-2cf1-4941-9053-3a88ad03c383)

  - for this lesson, we strict to supervised fine tuning.
  - we have lot of techniques to train these models using Supervised fine tuning.
  - The base working  of supervised fine tuning is this :
    1) all or some weights of the base models are kept frozen.
    2) and small number of layers are trained or new layers are trained and added later.
    3) so, basically the base model is frozen and we are just training for the additional small number of layers
    4) so total no of VRAM required is less, that is why it is called parameter efficient fine tuning(PEFT)

Parameter Efficient Fine tuning:
=================================

   - some of the PEFT techniques

1.prompt tuning:
=================

    - one is prompt tuning.
    - so in prompt tuning, as you can see in the diagram 1) we have an input 2) transformer is actually frozen 3) and then we get output.
    - now, for the input after the embeddings are created for the prompt, we add some additional paramters called prompt tuning parameters.
    - after we add this , we get the output and then we train using backpropagation and only adjust the weights of the prompt tuning parameters.
    - now, these parameters add to embeddings, doesn't actually mean anything, now we know that every token is some embedding number which
      we represnts in to higher space.
    - these prompt tuning parameters are actually doesn't adhere to any language as such.
    - these are some parameters which some how improves the efficiency of overall output.
![image](https://github.com/user-attachments/assets/2e25a6a0-9f3f-42f0-a57e-8a4dbb25b19b)

    - we also have something called LORA which is low rank adaptation, but we add some additional layers called LORA layers to the transformer
      while taking a forward pass from the input, we also pass it through the LORA weights , transformer is frozen and we get the final output.
    - we then backpropagate and only add the LORA weights parameters and only update them rather than doing a full back pass on the transformer.
    - And so during the training, only these weights are actually trained and not the main transformer.
    - you can also see that the summation of these weights are taken as output. so basically lora layers are an addition to the transformer layer.
    - and these parameters are generally 1 to 5 percent of the total transformer size.

DEEP Dive of LORA:
===================
![image](https://github.com/user-attachments/assets/e30e5b0d-3405-49bc-afbc-a4b539e1aa72)

    -  Reparameterized by adding low rank decomposition matrices.
    - so we have 2 matrices, one with size of D*R and another matrices B with R*N 
    - now  if we cross product them , it becomes D*N and the new matrices W.
    - the matrix W is equal to the size of the transformer layer and therefore this W can simply be added to 
      the transformer layer.
    - you can also see that no matter the different values for R , the final weights which is D*N does not have
      R*N  , thats how cross product works.
    - basically we can increase the value of R, we want then more parameters to be trained and we can decrease it 
      if we want to risk parameters to be trained and the final W formation happens.
    - Now by a research from microsoft , a value of R between 4 to 10 gives good performance, a value greater than that
      will just increase the parameter size and might not actually increase the performance of the fine tuned model.
    - this is how LORA works, where we train 2 matrices(low rank decomposition) A and B and finally cross product of them W
     is actually used and added to base model to finally get the inference.

 Advantages of LORA:
 =====================

![image](https://github.com/user-attachments/assets/27eeb49c-62ad-4601-ba85-73d6369c3889)

     - now, we use GPU, we dont have to actually get a cluster of GPU , but we can on a consumer grade GPU , train 
       a model up to 7 Billion parameter as well . that is huge cost savings.
     - the score that  we get from the LORA trained model is a kind of equal during research found out to be 
       as equal to full fine trained model.
     - which means the training LORA is always the goto option because full fine tuning is going to give same performance.
     - not only it saves cost, but additional advantages as well that we can discuss.
     - so, we can actually train multiple LORA adapters for several down stream tasks with the same base model.
     - because we just have matrix A and B for the given task, that we have fine tuned the base model for.
     - we will not add this final weights W to the base model and save it.
     - we actually separately save it as an adapter.
     - and so we can actually train a lot of adapters for a given base model and in the end just save the base model
       with multiple adapters fine-tuned for different tasks.
     - There is no added latency due to phased fused weights at runtime.
     - so for a given tasks, if we have some set of parameters we finally compute the W.
     - we add it to the transformer weights and fuse it rather than separately having to add the models with these weights
       and getting inference.we can simply add it to the transformer weight and this creates our new model which gives
       the exact same speed as fully fine-tuned model.
      - so, this addition of the LORA weights can actually also happen at runtime taking the base model and weights and
        fusing them and then creating the final model and serving that the different request that it gets.
      - so, we can keep on switching these adapters for different tasks, and in this way we can actually use the
        same base model and different set of tasks can be put in to base model and can serve different type of applications users.

Project Overview:
=================

![image](https://github.com/user-attachments/assets/4ea2be3c-69bd-4a1f-886c-6d78f9731cb2)


  - get in to project
  - first prepare dataset for fine tuning.
  - we will use one of the foundation model as our base model.
  - then we will fine tune using hugging face library.
  - we will be using the dataset , PEFT, TRL which are all library by hugging face to make
    supervised fine tuning pretty easy.
  - we would also be doing quantization to reduce the model size , to be able to fit in to a 24GB VRAM based machine
  - we also using QLORA which is a quantized version of LORA, which not just quantize it but use the quantize model
    to train LORA weights.
  - finally we evaluate the model output.
  - we do everything in the SageMaker.
  - we use Hugging face as the library of the choice.

SageMaker infrastructure:
==========================

![image](https://github.com/user-attachments/assets/c0c4ee77-69ef-47e5-8df4-290327e937be)


    - let see how infrastructure looks like.
    - we have user1 with profile name userprofile1
    - the user has certain role permissions with which the user  logs in to sagemaker studio.
    - once log in to sagemaker studio, the training code is available.
    - the whole studio that is launched has an EBS storage attached to it.
    - and this training code can be present in to machines with very small CPU and RAM requirements.
    - because the final training code is submitted to sagemaker training.
    - this creates a training job in sagemaker and so this is not present on the machine where the code is present.
    - due to which we only pay when we are actually training for the bigger machines and the rest of the time
      we are working on sagemaker studio on very small CPU and RAM based machines.
    - once your training code is ready , we give the data to sagemaker , sagemaker starts training.
    - as training happens, all the model weights are then stored on S3.
    - we can also actually track the sagemaker experiments in our training notebook and we also have a
      service called sagemaker experiments to track the experiments current status.
    - once the final model is ready, you can also register as a sagemaker model which has all the
      information that is needed to deploy it for the inference and create a sagemaker endpoint.
  
