![image](https://github.com/user-attachments/assets/5f039672-2bf6-44a3-a49a-22473c93c7d5)Chinchilla Scaling Laws
=======================

  ![image](https://github.com/user-attachments/assets/efbfbf70-9cfb-4db3-b5da-4c2de5ff5a32)
![image](https://github.com/user-attachments/assets/b0b8e6fd-ca9c-4265-84bd-0dc85e1fcb09)
![image](https://github.com/user-attachments/assets/22fa5f48-600a-47ad-b179-6ab2814fe070)
![image](https://github.com/user-attachments/assets/b7b3bc9a-802e-4ef2-97cf-7fd65693e88d)

  - each llm has been trained on certain amount of training dataset and has certain amount of parameters
    for e.g gpt-3.5 has been trained on 300B tokens,palm2 2T Tokens, llama2 17 billion parameter model trained on 2 trillion tokens.
  - so, while training your own llm it is critical to understand how much training data do we need and what should be optimal training
    size. 
  - we have defined an llm with 2.5 billion parameters ,**what should be optimal training dataset** that i need to use to train the 
    model efficiently.
  - or vice-versa, if we have training dataset with **1 billion tokens what should be optimal model size** that i need to use for training llm.
  - that is what scalling loss define.
  - understanding the scalling loss, let us effectively balance between the size and the complexity of our model as well as the size of the
    dataset.


Scaling laws:
=============

  - scalling loss - define how much training data is required to train and llm of the particular model size. it gives you rough estimates
    of the no of training token to be used for achieving the optimal model with in the given compute budget.

  ![image](https://github.com/user-attachments/assets/8e9a11fd-790c-4b4b-8f69-f8095ec7a302)
    ![image](https://github.com/user-attachments/assets/3925289a-9215-4445-8e3b-0157aba94441)
    ![image](https://github.com/user-attachments/assets/a0eaec64-e00b-404a-94d0-8ed0f85b1a98)

OPENAI
======


  - early work on scaling laws was done by openAI . the work they did was introduced in paper " scalling laws for neural
    language model was published in 2020". in this they stated that **increasing the model size was more important than
    increase the data size**.
    ![image](https://github.com/user-attachments/assets/b14e9fd2-5dde-4870-91aa-4a874e7e0a85)


DEEP MIND:
==========

  - After 2 years , in 2022, deepmind proposed a idea opposite to it.
  - Deep mind propose **" model size and no of training token should increase at roughly same rate"** to achieve best performance.
  - they stated that most of llm are significantly undertrained.
  - they suggested **gpt-3 175 billion parameter models are undertrained and it needs to use 11 times more training data to
    get optimality to get better performance.**

![image](https://github.com/user-attachments/assets/1c861da9-4b3d-45b6-984c-9a7a8ea9d0e3)
  ![image](https://github.com/user-attachments/assets/08994e26-97a4-4269-89f9-3e23bd74faa1)

 - they showcased by training over 400 models ranging from 70 million towards 16 billion parameters on 5 to 500 billion
   token datasets. these scalling laws are popularly known as cinchilla scalling laws.

   ![image](https://github.com/user-attachments/assets/abed8299-021a-4fe9-bb5d-d2d757a01620)

 - these  scalling laws compute optimal training is achieved when you double the model size you also double
   the tokens. in simple terms to cinchilla law  states that "to achiveve the optimal data of llm of x parameter
   we should have 20x tokens i.e token to parameter ratio is 20:1. if you are training 50 million parameter
   model , you would need 1400 billion tokens around 20 text token per parameter. As per cinchilla law,
   gpt-3 and palm1 are significantly undertrained,  not enough data. whereas latest model like mamba
   and palm2 are potentially overtrained, too much data.
 - Rest of the model like **chinchilla,   palm2 ,ultra,gemini holds the cinchilla** scalling laws , maintaining
   the ratio of the **token trained to the parameters in the ratio of 20:1**

  ![image](https://github.com/user-attachments/assets/436d72f1-01cc-4b47-a86b-5001b53074a6)


key take aways:
===============


![image](https://github.com/user-attachments/assets/2b5b1b7e-beae-4ef6-b169-6b4dd8d242b0)

  - so when you are training your llm **depending on our size of training data set , you can configure
    the size of llm** and define the llm as per cinchilla scalling laws.or based on the compute
    budget and llm that you want to train , you can collect the training dataset according to
    chinchilla laws.
     
    ![image](https://github.com/user-attachments/assets/2739cffb-acb7-40f9-8014-b7956bb177bb)
