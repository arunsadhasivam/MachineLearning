Definition:
===========

  Learn from pretrained Model by little change in model. pretrained LLM e.g Emergency problem solved using
  imagenet Pretrained LLM. in imagenet we have  lot of parameters. but for our case we just need
  to find whether it is emergeny vehicle or not. so take pretained LLM available which has all image data
  of vehicles and then customize to our needs like just choose only 2 fields so it will be more faster.

  so Always LLM needs fineTuning because in LLM it has generalized for all kinds data (input,output) .
  just tailor to our needs to perform faster.


Advantages of LLM
=================
    -Learn from pretrained or like learn from expert
    -faster learning
    -pretrained Model(E.g to learn Math Approach math tutor).
  
Emergency Classification:
=========================

1) CNN - Learning from scratch
2) images features -> shapes->edges.
3) convert from High Dimensional features to low Dimensional features.
   High Dimension - existing LLM , low dimension - customized model on the pretrained LLM(imagenet VGG16)

Pretrained Model:
================

1) BERT -> NLP
2) VGG16 Trained on Imagenet -> choose existing LLM for image problems
3) VLMFit -> NLP
4) VGG16 trained on MNIST -> Image problems

How Does Pre-trained Model to transfer Learning:
================================================

      solved problems       ->       New Problem                            ----->         Learning Transfer Happens by weights and Bias
      (Pre-trainedModel)              Learnings(weights & Bias Matrix)


Pre-Trained Model
==================

- Transfer Learning by weights & Bias

Steps:
======

1) how to choose right Pre-trained Model for Emergency vs Non-Emergency vehicles.
2) since image problems choose VGG16, MNIST

 
 Imagenet                                    |                 MNIST
 --------------------------------------------|--------------------------------------- 
 1)10,000 Objects classes categories         |  Digit  classifier
 2)Images 1.2M train look test               |  10 classes (0-9)
                                             


