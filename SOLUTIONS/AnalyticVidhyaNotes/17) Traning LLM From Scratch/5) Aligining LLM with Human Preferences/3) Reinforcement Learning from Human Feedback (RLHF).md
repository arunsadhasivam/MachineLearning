Reinforcement Learning from Human Feedback (RLHF)
==================================================

Stage 1:
========
  - so far we have covered, pretraining stage, where in our training objective is to
    predict the next token in the text.

![image](https://github.com/user-attachments/assets/59d87595-d56b-4a3d-882f-4225931b5ca9)

Stage 2:
=========

  - we have noticed that these base model aren't good in responding to user instructions.

Stage 3:
=========
  - inorder to solve this problem, we further fine tuned the base llm on instructions
    and response pairs i.e instruct dataset. to make it better at following instructions ellicting the
    responses that we want and to have conversation as a human word. the resulting model is known
    as supervised fine tuned model are SFT Model.
![image](https://github.com/user-attachments/assets/a91e6318-513d-4922-9e37-af2e1ea15406)

  - At this stage SFT model would be able to generate unsafe response that is exactly where alignment
    method RLHF comes in to picture.

Complete Training pipeline:
=============================

![image](https://github.com/user-attachments/assets/9f3ebeb2-f69d-470c-b179-53795bf3218e)

 - here this pipeline sums up the entire training process that was used for building the llm like chatgpt.
 - **first stage** is pretraining
 - followed by supervised fine tuning or instruction fine tuning that we have seen in finetuning llm course.
 - final step will be RLHF
 - till now we have covered first 2 steps.
 - now  , we will cover the last step of RLHF.

![image](https://github.com/user-attachments/assets/6396c6d0-40d7-4378-ac7b-dddf86546585)

 - RLHF uses re-inforcement learning using preference data which is generated using  human annotators.
 - in this way it enhances the response that the model generates and aligns to the helpful, harmless and honest.
 - lets understand with e.g

![image](https://github.com/user-attachments/assets/c149959e-893a-4d9c-a956-65e3bcdaf77e)

 - for e.g we have robot named rufus , who wants to learn how to talk like human.
 - rofus has a language model that understand words and senteneces.
 - first rofus will say something using his language model.


![image](https://github.com/user-attachments/assets/39c9af1f-3a31-4ff1-b39e-43db27828408)
![image](https://github.com/user-attachments/assets/3acdb55a-e43d-4a41-a1dc-a210d0278a1b)
![image](https://github.com/user-attachments/assets/086e0d3a-f17e-473a-bce9-406405c72ee8)
![image](https://github.com/user-attachments/assets/486228aa-2301-428c-af85-79544143bdfd)


 - for e.g he will say " i am bot"
 - then a human will listen what rufus says and will give him a feedback whether it sound like
   natural sentence or natural utterances like a human word.
 - then the human might say "thats not quite right rofus" human's dont usually say "i am a bot"
   they might says " i am a robot " or "i am a machine" 
 - then rofus will take this feedback and use to update his language model.
 - it tries to says the sentence again using the new information or new feedback that he has
   received from fellow human. this time it might says " i am a robot"
![image](https://github.com/user-attachments/assets/f046edce-592f-4f97-8890-6f1c40f9ab3c)

 - human listens and give more feeback .
 - this process continues until rofus can speak or generate sentences that sound natural to a human.
 - over time , rufus will learn how to talk like a human or how to converse like a human based on 
   feedback he receive from human. this is how exactly RLHF works.
 - RLHF takes in to account this human feedback and align the llm to human preferences.
 - before going to technical details, lets understand , why do we need re-inforcement learning in
   first place and why do we need them to align with human preference.

 why re-inforcement Learning?:
 =============================

![image](https://github.com/user-attachments/assets/d121c7ca-6de1-4f6b-a404-0ec659c4af87)

 - Reinforcement learning is used to solve complex problems for which there is no clear objective answer.
 - in our case , say when you prompt SFT or instruct model with the query "how are you?" there can be
   lot of correct or valid response. it could neither be " iam good", "i am great", "i am doing well"
   there is no single clear answer to this question. so we need to frame this as re-inforcement
   learning problem.

Understanding Re-inforcement Learning Process:
===============================================

![image](https://github.com/user-attachments/assets/75e14948-c5bc-453b-9b66-1725b4db2099)
![image](https://github.com/user-attachments/assets/f7f44a48-b961-4965-816e-6bbac819337b)

   - The idea behind the re-inforcement learning is this an agent in this case , a model or a policy model
     we learn from the environment by performing action. force that we receive rewards can either be
     positive or negative rewards for performing actions in this environment.
![image](https://github.com/user-attachments/assets/abf01738-5159-4786-aad9-b7e1b9e3bae8)

   - this process goes in a loop , until a agent learns the optimal policy. policy is a strategy that guides
     the agent  to perform actions in the environment. the objective of re-inforcement learning is to
     learn optimal policy that maximises the long-term rewards.
   - lets see how it fits on our model.
![image](https://github.com/user-attachments/assets/8e94879d-0cdb-44c1-b185-e4360327c589)

   - in RLHF, the agent is initialized with the supervised fine tuned model i.e SFT model and then
     we want to learn it via re-inforcement learning using human preference.
![image](https://github.com/user-attachments/assets/a9541c8e-4381-4179-adda-d6edcfd0a4ef)

   - here the action phase of SFT model are all the tokens that it can generate.
   - here the environment is to generate the response to the given prompt.
   - reward is a scalar value, which is given by the reward model which tells us how good
     of completion or how good of the generation the model is producing for a given prompt.
![image](https://github.com/user-attachments/assets/b78ee3d1-4e20-4437-ae48-ca4c6205e294)

   - finally the optimal policy here is to optimizing the agent using human preference and the
     ultimate goal of RLHF is to learn this optimal policy.i.e **we want to align** or find the policy
     model to our preference.
   -  how see steps in RLHF.

 Steps Involved in RLHF:
 ========================
![image](https://github.com/user-attachments/assets/cc3e110d-e41c-4138-97cb-3bb24374cbd3)

   -  Broadly there are 3 steps in RLHF.
   - first step is to create a preference data.
   - second step is to   train the reward model using the preference data generated above or collated above.
   - third step is to learn the optimal policy using proximal policy optimization popularly known as PPO
     or any other re-inforcement algorithm.
   - Now discuss each step in detail.

<p><detilas><summary>1.Create Preference Dataset:</summary>

1.Create Preference Dataset:
=============================

![image](https://github.com/user-attachments/assets/58a6ff6a-57cb-4d96-b676-ebbbf2cb2265)


  - first step is here is to create preference dataset.
  - this is the third type of dataset that we are curating.
  - the first type of dataset that we are curated for pre-training and the second type of dataset
    was collated or curated during instruction fine-tuning.now the thrid one we are curating RLHF.
  - the preference dataset will be used to train the reward model that will be later use for
    optimizing the policy.
  - the way to go about the creating the preference dataset is to sample multiple generations or
    multiple completions to the prompt using SFT model after that we ask the human or human annotators
    to rank the response based on preference.
  - for instance consider the sample prompt "what are llm?". this sample prompt is passed on the
    sft model to generate multiple response. say first response could be "llm are deep learning model trained on massive amount of data"
    second response might be "llm are large language model training on massive amount size of dataset to learn patterns of natural language"
  - so can you guess the better response of the 2 .
![image](https://github.com/user-attachments/assets/9e660322-9bcd-48d6-9a61-cf78134f05b1)

   - obviously the 2nd answer is bit better compared to first one as it details out exactly llm does.
   - so human ranks the response gives llm .response1 better than response 2
   - similary this process carried out on multiple prompt.
![image](https://github.com/user-attachments/assets/32250d4d-c30c-4a6e-8900-5bd95b05e72a)

   - they generated multiple response on each prompt and rank by human annotators. this process is a manual and very much
     time consuming process. very human annoators go through the response generated by llm and compared with them each other
     and rank the response.
   - you might be curious about why we often providing comparitive data instead of directly assigning scalar values or
     rating the response. providing the direct scalar values to the answers can be subjective and can have human
     bias.
   - for e.g few people always rate on low scale, like if they like something they might do 4/5
   - whereas some human bias to higher number , for e.g if even not good they might rate to 3.5/5
   - so assigning the direct scaler values is very much subjective and it also has human bias.
   - therefore instead , we compare the responses generated and it is easier providing certain scalar values.

Format of preference datasets:
===============================

   - format of the preference dataset will be
      1) instruction
      2) choosen
      3) rejected answer.

![image](https://github.com/user-attachments/assets/6f2327c0-5be4-4e29-88c4-180f8c5cdcdc)

    - for e.g Do "people scare you?" is the instruction or the question. the choosen answer was
      " i cannot assist you with the question" and the rejected response was no.
    - you can see human prefer this kind of answer than plain no.
    - this brings us the end of the RLHF.
    - now you have curated this preference dataset.

</detilas></p>

<p><detilas><summary>2.Train Reward Model:</summary>
  
2.Train Reward Model:
=====================

![image](https://github.com/user-attachments/assets/ecb43c87-2183-4603-af14-cc047e1b42b3)
    
  - next step is to train the reward model.
  - we train the reward model on the preference dataset to output the scalar value.
  - this reward model is different from SFT llm .
  - the reward model is designed by replacing the last layer of the llm with a dense layer.
  - the scalar value which is the output of the reward model represents the reward given to the
    generated response.
  - in instance GPT paper, OPENAPI reseacher uses 6Billion parameters LLM to train the reward model.
  - the way the reward model is trained is as follows:
![image](https://github.com/user-attachments/assets/4c8c12fb-74ec-4eaa-a623-7098cea28055)

 
      1) he provide the instruction and as well as **choosen** and **rejected** response.
      2) llm output the **scalar value** for each of the **response** which indicate **reward**
         post that the loss is calculated by first taking the sigmoid on the difference between
         the rewards and taking the logarithm of it and finally followed by taking the **negation** of it.
      3) then the loss is back propagated through the reward model and the optimizer step finally update the
         weight of the reward model using the **gradients** with respect to the loss function.
![image](https://github.com/user-attachments/assets/039a63d1-9e4a-4045-95fc-869a611ac931)

      4) the core concept that we need to learn in this reward modelling is loss function.

Loss Function:
==============

  - let discuss on loss function.
  - initially the reward model would assign random scalar values to the responses then the loss
    turned out to be high. because of the parameters of the reward model would get updated to
    minimize this loss.
![image](https://github.com/user-attachments/assets/3fd293d4-81e2-449a-8d1b-47ed5295d3f1)

  - for e.g let say r1 is the reward of the choosen response
    and r2 is the reward of rejected response.
    in the first iteration,that llm has no knowledge about human preference and it might output wrong rewards for the
    choosen response
  - for instance let assume that llm is assigning the reward of 0 for choosen response and while it is
    assigning a very high reward of 10 for the rejected response.
  - now if you compute the loss by taking the sigmoid on the difference between the rewards and then taking the
    logarithm of it and multiplying with -1 and taking the negation of it we get the loss of 4.39, which is very high.
  - now this loss is back propagated throught the network to compute the gradients and thus gradient are used to
     perform the optimizer step , in order to minize the loss.
![image](https://github.com/user-attachments/assets/32a361bf-fc21-44a8-a555-8ac2d5f649c2)

  - now in 2 iteration model assign high rewards to choosen  response , the reward for e.g 5 and it assign a reward
    of 0 for the rejected response. now if we take the sigmoid of the difference between them and followed by
    logarith of it and negating it and we get very small loss value of 0.03.
  - in this way the reward model is trained to minimize the loss.
  - now that we have trained the reward model to output the scalar reward values.
  - lets look at the next step.

 
</detilas></p>


<p><detilas><summary>3.Learn Optimal Policy Using PPO :</summary>

3.Learn Optimal Policy Using PPO:
=================================

![image](https://github.com/user-attachments/assets/fbff7ea6-af6a-4e22-9f5a-71772c406cc7)

  - as you have seen earlier the goal of RLHF is to learn the optimal policy that maximises the
    long term reward.
  - in our example , the optimal policy refers to aligning the SFT model to our human preferences.
  - now lets take a closer look, at the steps involved in learning this optimal policy.
![image](https://github.com/user-attachments/assets/7bb0fcb2-fc45-4cdd-9b72-ab1555d2ec1d)

  - first step is sample prompt form the prompt dataset.
  - you have a  prompt dataset , you sample prompt from it and next
  - this prompt is passed to the RL policy , in our case initialised with SFT Model.
![image](https://github.com/user-attachments/assets/f02dc158-2859-4647-b662-50c673cc0926)

  - now the RL policy , that is the agent generates the response for the given prompt.
![image](https://github.com/user-attachments/assets/527bcd1f-7bea-4ff7-8a9b-9b863e9341f5)

  - the reward model calculates the reward for the concatenation of the input along with response.
  - now this reward is used to update the weights of the policy agent here using proximal policy optimization.

Summary:
========

![image](https://github.com/user-attachments/assets/52993804-3fa6-4432-bd94-174480137179)

  - RL policy is trained on the prompt dataset
  - rewards are calculated for the generated responses and then those rewards are used to update the
    model parameters using PPO.
  - here PPO is RL algorithm based on policy gradients.
  - the idea behind PPO is to improve the training stability for learning the policy by limiting the change that
    we make to the policy at training epoch.
  - PPO ensures that we dont have very high or very small policy updates. it helps in convergence to a optimal solution.
![image](https://github.com/user-attachments/assets/eaa86773-7f17-4a86-a9b3-bf3438a4751b)
![image](https://github.com/user-attachments/assets/9a906b19-103a-4945-8111-45787ebb6623)

  - Apart from this we also add the KL divergence loss or KL divergence penalty  to the final objective of PPO
  - this ensures that the policy that we are learning via PPO doesnot deviate too much from the original SFT Model.
    i.e it does not deviate too much from the model that know how to generate coherent and grammatically correct response.
    this avoids the model to do reward hacking, wherein it hacks the system by generating non-coherent responses but
    which gets very high reward.
  - so the final reward is the combination of  reward from the reward model and the negative of the KL divergence
    between the response from the policy model in comparison to the response from the reference or base SFT model.
  - note that the initial model and the reward model is frozen and untouch by gradient udpates during the training
    and only the parameters of the policy model are being updated . however we can see that we need to keep 3 model
    copies i.e active policy model , the reward model and the reference base SFT model.
  - so, RLHF is not just complex to implement , it is quite unstable, sensitive to hyperparameter,
    and along with it is very compuationally demanding or memory intensive step.
   - this summarizes the entire training process that is carried out in RLHF.
![image](https://github.com/user-attachments/assets/78aa0f29-c285-46a4-8abb-73104bd9ea53)

   - now SFT model can generate responses that are align with human preference, after performing RLHF states.
   - in summary RLHF starts with collecting human feedback or human preference than we train the reward model
     using the human preference dataset and finally we learn the optimizal policy via **policy gradient algorithm using PPO variant**
  
  comparison of the 3 steps:
  ==========================


![image](https://github.com/user-attachments/assets/bf3a104c-a40a-4e43-9048-e6f2b2acf637)

  

</detilas></p>
