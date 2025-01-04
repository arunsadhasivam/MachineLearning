DPO and IPO
============


  - direct preference optimization and its variance
  - IPO identity preference optimization

Lets gets started , with the challenges associated with RLHF

![image](https://github.com/user-attachments/assets/b32a0c57-6fab-42f7-999b-61622fa9e99c)

Challenges with RLHF:
======================

  - RLHF is a complex and unstable process where in you need to first train the reward model and
    then fine tune the RL policy to maximize the rewards without deviating too much from the
    original train model.
  - training RLHF does not lead to convergence as suppose to other model.
  - it needs lot of experimentation and hyper parameter tuning.
  - hence stanford researcher proposed new alignment algorithm known as DPO , it is proposed as an
    alternative to RLHF. it is much more stable and it is as performance and it is computationally
      good and light weight.
 ![image](https://github.com/user-attachments/assets/5002bac0-62f2-42d4-ad48-1f3dee5848d8)


NOTE:
=====

  **- it eliminates the need for external reward and reinforcement learning as opposed to RLHF.**


Steps involved in DPO:
=====================

    - 2 step process

1.collecting preference dataset:
==================================

    ![image](https://github.com/user-attachments/assets/6aa4bdce-0602-49ce-ac9c-f8cf91d949f7)

![image](https://github.com/user-attachments/assets/27f3d718-119e-4d76-b904-8d6a586c55fe)

  - first step is to collect the preference dataset similar to collecting the preference dataset in RLHF.
  - the preference dataset consists of instructions , choosen and rejected response.
  - the next step is the directly fine tuning of the SFT model.
  - directly fine tune the SFT model i.e instruction tuned model on the preference dataset using
    binary cross entrophy loss function , as a result the parameters of the model are fine tuned
    with the preference which **aligns with the reference of the human annotators i.e human preference**
![image](https://github.com/user-attachments/assets/0097e666-8fa4-4831-9d63-ee723b1eeaa9)

  - for instance coniser a prompt, choosen and rejection response pair from preference dataset.
  - this sample prompt is pass to the sft model to generate the response.
  - sft model generates the response for the given prompt , post that the response is compared
    with the choosen and rejected response and binary cross entrophy loss is computed . this loss
    is then backpropaged to the network.
  - the weights of the sft model are updated.
  - **as a result , we obtain sft model that is aligned with human preference.**

Summary:
========

![image](https://github.com/user-attachments/assets/d44cdfb5-56a2-4c5f-b73c-1cdb8d0800a6)


  - in summary, given the human preference over the model response, DPO can optimize
    the policy using the simple cross-entry objective while producing the optimal policy
    to an implicit reward function to fit the preference data.

IPO:
=====

  - one shortcoming DPO is that quickly overfit to the preference dataset.
  - to avoid this researchers and deep mind introduce identity preference optimization.
  - it acts as a regularization term to the DPO loss function.

![image](https://github.com/user-attachments/assets/cb757e60-bb30-4dab-9023-39e57a434561)


Regularized loss function:
===========================

  - this regularized loss function enables us to train model to converge with out requiring tricks
    like early stopping, very sensitive hyperparameter tuning and so on.
