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
 - 
 

