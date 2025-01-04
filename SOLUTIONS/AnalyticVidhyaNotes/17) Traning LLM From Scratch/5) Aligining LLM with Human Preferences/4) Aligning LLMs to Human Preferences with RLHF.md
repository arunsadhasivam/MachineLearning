Aligning LLMs to Human Preferences with RLHF:
===============================================


![image](https://github.com/user-attachments/assets/6c1d98f8-a4bc-4331-89fe-fc6065ca40ae)

![image](https://github.com/user-attachments/assets/52b50125-5216-4022-ab05-ca79f94c564a)


  - RLHF has 3 stages 
    1) you perform sft (instruction fine tuning)
    2) training a QR Model (Query Response)
    3) use SFT model and reward model to perform re-inforcement learning.
      
 - in this lesson, we will see how to perform PPO ( last stage of RLHF)
 - we also saw that RLHF can be quiet unstable and lot complex
 - therefore we will example directly from PRL library with respect to how PPO can be implemented in a relatively simple
   setting.
 - we optimize GPT-2 to produce positive movie reviews and the reward model is a word sentiment classifier.
 - which can tell whether given review is positivie or negative
 - here we fine tune gpt2(small)  model to generate positive movie reviews based on imdb dataset
 - the model gets the start of the real review such as "this movie is " and the model is tasks to produce
   positive continuation. so there can be multiple continuation.
 - this movie is worst, or this movie is worst ever watched.
 - our aim is to align the model to only to generate positive reviews , so that is our main goal and we want to align
   model with it.
 - to reward positive continuation and to penalise negative continuation , we will use BIRT classifiers which
   analyzes the sentiment of produce generation. for e.g we have this starting of real review " this movie is "
   and model generates really great.so  prefix and the generation then given to reward model i.e **query + Response**
   pass to the reward model which is BERT sentiment classifier.
 - here you can see model is rewarding with positive 1.0 value because this movie is really great is a positive sentiment
   and as such , we want our model to get as high reward as possible.


   CODE:
   =====


 1.set up code env:
 ==================


    ![image](https://github.com/user-attachments/assets/10c0fd75-acde-4264-99a5-833df10f440f)

 2.load libraries:
 =================

 ![image](https://github.com/user-attachments/assets/c5314d8a-c6e7-492a-8f65-ee4a2837ebe3)


3.configuration:
================

![image](https://github.com/user-attachments/assets/823aeef5-8930-4dcf-a358-fc8310d81e4b)

 - here creating a object of PPO config class where in we provide the model , so we can see that this model
   has already been instruction tuned or supervised fine tuned on imdb dataset.
 - this is the model that is result from SFT stage and along with learning rate and we will log in wandb project
 -  we will initialize the wandb project
 -  the model we load is gpt2-imdb , this model is additionally fine tuned on imdb_dataset for 1 epoch.

4.load imdb dataset:
==============================

    - load imdb dataset it contains 50k movie reviews , filter comments > 200 characters.
    - tokenize the text and feed to the random size length sampler.

    ![image](https://github.com/user-attachments/assets/829326f6-da72-47b7-b345-4c276335fe59)
![image](https://github.com/user-attachments/assets/f443a554-1ee3-4e6d-a1b1-b7ec52ee17de)

5.load pretrained gpt2 language models:
=======================================

![image](https://github.com/user-attachments/assets/c4c97b43-51f4-4383-8f93-98abda26fd4a)

  - here you can see our model it is gpt-2 imdb model which is additionally finetuned with imdb dataset.
  - we loaded using automodal for casualLLM with value
  - here you load gpt2 imdb model which has value head and tokenizer
  - along with that model we load model twice because  1 acts as a (policy) and other acts as a reference.
  - 1 model which optimize is a policy 
  - 2 model serves as a reference to calculate the KL-divergence from starting point.
  - as in previous model, we want re-inforcement learning  , but we dont want model to deviate drastically from
     sft stage.that is computed using the KL-divergence laws. for that you require reference model also.
  - as we can saw, KL-divergence law acts as a additonal reward signal i.e negative of the laws is the reward
    to make sure optimal model does not deviate too much from original model i.e does not do any reward hacking.


6.Initalize PPO Trainer:
=========================

  ![image](https://github.com/user-attachments/assets/9a1fb49d-fbd1-4aa8-938f-c89de3b2d725)

  - PPO Trainer is imported by hugging face, PPO Trainer takes care of device placement and optimization later on.
  - provide following parameter ppo config, reference model, tokenizer,dataset.
  - now create a objecet of PPO trainer , next step to load BERT classifer, this is the reward model.

7.Load BERT Classifier:
=======================

![image](https://github.com/user-attachments/assets/99f8e5af-3edc-4ace-8159-d6c2a03a0bd3)

  - this is the reward module.
  - we directly create a pipeline object , this pipeline is imported from transformers.
  - **since this is the sentiment analysis task , there is a pre-build out of box pipeine that one can
    use , just provide the model name.**

    ![image](https://github.com/user-attachments/assets/831941c9-4050-4b0d-8116-289640bc3260)
  - we use **distil-bert-imdb** model which is a reward model trained on imdb dataset in order to
    classify whether a given review is positive or negative.
  - lets create a sentiment pipe , let see whether it is really doing sentiment classification property
  - if you give the text "this movie is really bad" you can see this score for positive label is highly negative
    and score for the negative label is highly positive . that is it is giving high rate or score or weightage
    to negative so it is negative sentiment.

  - similarly,if you give text with positive sentiment " this movie is really good" the score for positive
    sentiment is high.

8.General Settings:
===================

![image](https://github.com/user-attachments/assets/28d1be2e-0865-4402-acf7-7fbc44d7a227)

  - these above are generation settings, we want to sample when we want to create possible generations 
  - here we consider top_p is 1 and top-k is 0 and given the pad token id.
  - for more information on decoding strategies or generation strategies there are good blogs on hugging face

9.optimizing model:
===================

![image](https://github.com/user-attachments/assets/b8b0331e-a886-4659-8947-7b0d8e9af7cc)
![image](https://github.com/user-attachments/assets/146d0286-a5e3-46bc-81b9-4d8f3c80ad22)
![image](https://github.com/user-attachments/assets/25e13011-389c-4044-8958-65eab4eef0af)

    - training loop
    - there are 3 major steps 
      1) get the query response from the policy network.
      2) get the sentiments for query/response from BERT
      3) optimize policy with PPO using the (query,response,reward) triplet.
    - here we first the responses for the given query , we have ppo_trainer to generate possible completions
      for the given start of the review , then concatenate them and then get the sentiments of the
      concatenation of the query and as well as response while the reward classifier and we get these
      response.
    - final step is to optimize the model or create the policy model using the query tensor, response
      tensors and as well as rewards. this is how entire policy optimizer works.
    - as you can see it just uses 1 gpu 


![image](https://github.com/user-attachments/assets/9416c767-c80a-4956-8fa5-75106be8d53f)
![image](https://github.com/user-attachments/assets/c65dcde9-973b-4f61-8305-408a0c40d256)

   - above see generating positive review

10.model evaluation:
==========================


![image](https://github.com/user-attachments/assets/60fe11f1-a5fb-4051-a40e-f404d83e4256)
![image](https://github.com/user-attachments/assets/6ffb98d3-d71c-4796-90b0-5ee99e15f156)

![image](https://github.com/user-attachments/assets/e8e5141a-a9fe-4382-8413-fc6d53cece5c)

  - qualitative validation on set of dataset samples.
  - for e.g "Born Again" is the query , the response
  -  1)before performing PPO the model= response   completed with " is just awful" - negative review
     2)post performance of PPO  model = response completed with - " is a fun ride" - full positive review.

  SNO |  query                       |  Before Performing PPO         | After performing PPO
 -----|------------------------------|--------------------------------|---------------------------
   1  |    Born Again                |     is just awful(-ve review)  | is a fun ride(+ve review)
      |                              |                                | 


  - you can see before PPO or before RLHF the reward was highly negative and after PPO RLHF
    it is highly positive.
  - in this way we have aligned the GPT-2 small model to only generate positive review given the
    start of the review.
  - you can see median of rewards after PPO is 2.3 which is great
  - it shows that our model is learned to complete a given review to complete a positive sentiment.

![image](https://github.com/user-attachments/assets/585d5351-ffc4-42c0-ad10-c183a919a06b)


11.save the model :
==========================  

![image](https://github.com/user-attachments/assets/c1f956cf-8b7e-4afb-b926-c98375783dc1)
