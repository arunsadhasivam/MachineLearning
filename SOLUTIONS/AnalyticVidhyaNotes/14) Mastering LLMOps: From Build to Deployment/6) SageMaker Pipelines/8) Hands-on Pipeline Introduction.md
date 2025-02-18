Hands-on Pipeline Introduction:
===============================

    - work with sagemaker pipelines.
    - so previously, we trained a model first by preparing a dataset.
    - then we created a sagemaker training job.
    - that job started and trained our models and saved in S3.
    - we then use this S3 model artificats to finally deploy the model.
    - once the model was deployed, we are able to evaluate and see the output of our trained models.


So this is the sagemaker training is:
=========================================

  - once the training is done, we can also automate the whole data pre-processing , training and deployment process
    using something called sagemaker pipeline.
  - in this lesson, we would be working with sagemaker pipelines, which automatically does the data pre-processing
    training, and afterwards makes a decision of should the model be saved or should the pipeline discard,
    because some of the metrics does not match.
  - so for this, we will log into sagemaker , once you are in sagemaker studio, i have the jupyter notebook lab opened.
  - make sure that you are in notebook, sagemaker folder and we will be working with 2nd folder pipelines.

![image](https://github.com/user-attachments/assets/69389032-0630-4a71-849e-4f283a8f10de)



  - so just like before , we would be having our whole thing setup in smaller machine which is T3.largermachine.
  - But all of these steps in pipeline, would work on different kind of instances as we would set and provision them
    as we go along.
  - so this is what the notebook looks like, we have the sagemaker pipeline,
  - in the pipeline, we have 
        1) data pre-processing step
        2) Model training step.
        3) general evaluation
        4) check accuracy. - if the model accuracy of given model is not good as we want , we will fail the pipeline,
                             if it is better than we expected then we would create model using register module step.
        5) registermodel step - register the model. if the model accuracy is good than expected.

  - and then this is then save it to sagemaker model registry.
  - this is how the whole pipeline looks like.


Avalon:
========

  - we would be working with the dataset called avalon.
  - this is also one of the official sagemaker example, in which avalon is a type of shell
    whose age can be found out using the number of rings present, so the age is number of rings present
    so the age is no of rings + 1.5

  - but to find out the rings its hard because it is has to done through the microscope.
  - and this is one set of problem, where given multiple different parameters about the weight, shell,heights,
    we should be able to predict the age automatically.



Code:
======

1.setup:
=========

![image](https://github.com/user-attachments/assets/573c0e44-274f-4540-91e9-5089a74c3ed1)


2.UserID:
==========


  ![image](https://github.com/user-attachments/assets/487ca92f-7a34-4a2c-9f8e-2f8ed176403b)


![image](https://github.com/user-attachments/assets/bd3143b9-2954-442d-9a71-91dc12332011)


3.syncDataset:
==============

    - copy to our s3.

    ![image](https://github.com/user-attachments/assets/1bf55833-2d23-45dc-af85-af7f6e784537)

data is uploaded

4.Global Parameters:
======================

- we can specify as a global parameter and while running the pipeline we can specify it .
- we can even give a default value.
- we can see processing instance should run on this machine, which is the process instance
- if the value is not provided then the default value will be taken from default=process_instance.

![image](https://github.com/user-attachments/assets/7d2e65bf-d23b-44f1-a38c-e6becc0dd6f2)

 - instance_type, modelapproval status, input data and mse threshold 
