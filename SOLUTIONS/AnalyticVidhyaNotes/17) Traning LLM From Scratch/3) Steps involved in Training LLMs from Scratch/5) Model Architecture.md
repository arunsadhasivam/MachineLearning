Model Architecture:
===================


  - Deep dive model architecture of llm and best practices.
  - till now we have dicussed training data curation, data pre-processing and tokenization.
  - next step is define model architecture,most of the state of art llm are inspired from transformer architecture.
  - therefore undoubtedly the backbone of the llm we see today.



Transformers Architecture:
===========================

  - it contains 2 components
  - encoder and decoder.

![image](https://github.com/user-attachments/assets/b28c5fcc-0b82-495f-bb90-ac8d657732ad)

  - **encoder** - accepts the input and converts in to higher level representation. which is then
    pass to the decoder.
  - **Decoder:** - the decoder than generates the output based on **encoders representation**.

![image](https://github.com/user-attachments/assets/469783e8-5d93-47ba-a060-83ff54bd3892)

  -  Each encoder block consists 2 sub-blocks
        1) self Attention sub-block and
        2) NLP or feed forward Neural network sub-block.
   
  - These 2 sub-blocks are fundamental building blocks of transformers, that makes it powerful.
  - here input is passed to self attention layer and followed by feed forward layer to get the output.
  - similary blocks consists of  3 sub-blocks.
![image](https://github.com/user-attachments/assets/5e5c34d5-427d-4302-a1c1-0fe260584750)

     1) self attention block
     2) encoder-decoder attention (cross attention)
     3) feedforward neural network.
  - this fills up the encoder and decoder in transformer.

![image](https://github.com/user-attachments/assets/d63e32bf-756a-4886-ae90-7965d31869b0)

  - This build up the entire block of encoder and decoder in transformer.


![image](https://github.com/user-attachments/assets/89cef4c3-e39c-44ad-aeef-f1938e77906c)

  - This encoder and decoder blocks are repeated multiple times to have final modal architecture.
  - Above diagram is detailed modal architecture of transformer from paper "attention is all you need".
  - As illustrated here the inputs are first tokenized and converted in to input embeddings followed
    by addition of positional embeddings.
  - it is passed on to **multi-head attention layer** which enhances the input representations of the
    input embeddings to capture the contextual semantic representations and then it is passed on to
    feed forward neural network. this process is repeated for n-blocks on the encoder side.

  - finally the output of the encoder is passed on to the decoder.
  - decoder does the similar compuations to the encoder and adds another layer knows as **cross attention layer**
    or **encoder-decoder atttentionlayer**.
  - finally it generates the output probability based on encoder outputs and decoder input .


![image](https://github.com/user-attachments/assets/e5d27777-5bbb-40e0-a6d8-2fd228d67fa1)

  - **As of today , current state of art llm are focussed only on decoder part of transformer**
  - for e.g llam2 , mistral7, phi-2 e.tc are trained on decoder based architecture.
  - thus we understand that the decoder architecture is needed for training our llm.

How to define the model architecture:
=====================================

  - broadly there are 3 methods to define modal architecture.

  1.Existing Modal Architecture:
  ==============================

![image](https://github.com/user-attachments/assets/35fd14a5-f754-4e37-bfb2-e515a334f77b)

    - use the existing modal architecture of the state of art llm.
    - we can select the state of art llm available out there and then fine tune this model on our
      domain specific training dataset to common up with domain specific llm.
     - for e.g code llama2 is the start of the art llm which are finetuned on the base model
       llama2.
![image](https://github.com/user-attachments/assets/1f2c3e7e-a717-4fd8-b904-e9b0fc5774e3)

     - similary github copilot is  fine tuned on base llm gpt-4

  PROS:
  =====

![image](https://github.com/user-attachments/assets/289e48b4-dcd2-4f86-a539-6d65d063411a)

   - notable advantage of this approach is lies in the fact that researchers have conducted various
     experiments and explore diverse elements in developing current model architecture.
   - we can leverage these established model architecture for training our llm.
   - this reduces most of our effor from most of our side to come up with our own architecutre.
   - the next advantage is that we can gain high performance by further fine tuning i.e known
     as **continued pre-training**.
   - the only thing that we need to consider when using existing models or existing model architecuters
     is to collect the training datasets asper the training loss.

2.Modify existing Model Architecture:
=====================================

![image](https://github.com/user-attachments/assets/9d36b841-c624-447c-82ae-383011367572)

![image](https://github.com/user-attachments/assets/7ce07f5b-b409-47ba-bec4-604c1ee168d6)


  - in this approach , we change couple of settings of the model architecture. 
  - it could be modifying few layers or changing few hyper parameters of existing architecture to come up
    new model.
  - for e.g mistral 7b is the most powerfull 7b model till date. it is based on the transformer architecture
    with few changes incorporated. these changes are 
    1) sliding window architecture.
    2) rolling buffer cache.
    3) prefilling and chunking.

  - similary Mosaic pre-trained transformers (MPT) adapts architectural changes such as using
     1) it uses fash Attention.
     2) it uses ALBi (attention with linear bias) and does not use positional embeddings.
     3) it does not use biases.


PROS:
=====

    - Adapting the existing arch and tweaking to get the new model tends to find exceptionally well per
      coming up with state of art models.

  - Next is to go one step further, to design new model architecture. this approach is typically done
  - by well funded oraganizations such as mistral, microsoft e.tc
  - since it requires run many experiments which require lot of compute,technical skills ,time.
  - As well as lot of monetary funds.

![image](https://github.com/user-attachments/assets/8eabc434-5849-493f-bc09-3cef03a89433)

  - for e.g moe(mixture of experts ) is the new model architecture  by mistral
  - it is best open source model available currently.
  -  question is which is best approach of the above 3.

Summary:
=======

 - which approach which one to choose.
 - budget constraints can choose 1 or 2 i.e adapt or modify existing arch
 - the focus here is collecting high quality dataset to achieve domain specific llm.
 - there fore if you have minimal budget, either adapt existing model with continued pre-trained
   or modify few settings of the model and do a continued pre-trained or trained from scratch
   with own domain specific data. which required manual or automatic restart to ensure smooth
   convergence.


![image](https://github.com/user-attachments/assets/5fc3439a-1faf-4615-baeb-d5432220ecc5)

  - Modal checkpointing helps in resume the training process by restoring the parameters,
    optimizers state, learning rate scheduler state and so on.
  - post that we train our llm 

  


        
