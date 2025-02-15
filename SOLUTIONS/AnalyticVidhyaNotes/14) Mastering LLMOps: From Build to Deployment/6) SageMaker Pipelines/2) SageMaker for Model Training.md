SageMaker for Model Training:
==============================



    - Now, we have see how multiple users or multiple projects can be implemented using same umberella using  domain.
    - in which, each user or teams gets their own public and private space and collborate really well on multiple projects
    - lets look at how training is done in sagemaker.


ML Workflow:
=============

![image](https://github.com/user-attachments/assets/94b9de4f-9689-4293-adca-8848d1951169)


  - we have our code base and then we download our datasets,
  - we start by installing a lot of libraries, that is needed for training.
  - we then start our training and once the training is done on train set and validation set
    we go for evaluation in which we see the model results in the test set.
  - if we are happy with the result of evaluation  , we finally save the model checkpoints as artifacts.
![image](https://github.com/user-attachments/assets/a4868b33-972d-4093-beef-32877eca1b28)

![image](https://github.com/user-attachments/assets/8cd72165-ab76-4076-99e0-e7445101fda4)

  - and this in the workflow, we are having lot of challenges, let see what all things we need to track.
    1) First is dataset, this dataset might change with time and we should know what things changed and what was the
       exact dataset in which the model is trained.
    2) The data pre-processing code which is present over here might change after certain time, which will make it
       really hard to compare two models performance.
    3) we have version libraries and framework, and this is really needed to ensure that the same libraries
       and packages are needed while training and evaluation to ensure we can reproduce the same result in feature.
    4) we also have hyperparameters while training , which we need to keep track of.
    5) And we also have experiment log,
    6) when the training happens, we want to know what exactly happened at that point of time.
    7) There are certain training metrics which we also need to track , such as accuracy, the evaluation loss
       that was happening during the whole time.
    8) And then we have evaluation metrics, which is after our model is trained and we tested our output
       in the test set, what were the metrics we got?
    9) and finally , if the output was very good and we want to save it , we save it in model artifacts.
    10) then we need to compare different runs together for the evaluation metrics.



![image](https://github.com/user-attachments/assets/c6641699-432a-45bb-9371-0a61ab301706)

 Development Environment:
 ===========================

   - lets see how development looks like.
   - we have multiple environment, we can choose from.
   - so, some might want to work on **VS code like code editors**, while some prefer **jupyterlab** environment
   - we also have application called canvas , which is a no-code solution we can use in which we dont need to
     code at all to gain insights and train our ml Models.
   - we also have Rstudio IDE available for teams, which works with R.
   - we have studio classic , which is the older version of sagemaker studio , but it is also given if teams
     still want to use the older version.
   - we also have MLFlow, which is a opensource ML-ops library , a full-fledged framework , which is really popular
     and that is also given as a integration for sagemaker.
   - we have all these information to choose from for coding purpose.

Integration:
=============

  - let see how to integrate and talk to sagemaker.
  - we have sagemaker 
      1) Rest API available
      2) we have cli
      3) and we have SDK
  - for python we have specifically , we have package  called sagemaker , which we can install and simply
    talk to amazon sagemaker.
  - we also have Boto3, in which we can talk to AWS in a very simple SDK and get our job done.
  - there are other services as well that sagemaker offers 
     1) one is sagemaker jumpstart  in which we can quickly test our foundation models.
     2) amazon bedrock - which is the pay as you go foundation model in AWS region. 
  - so, if we just quickly want to check these new LLM models, we can just use the **bedrock** api to get the output


Sagemaker Experiments:
=======================
![image](https://github.com/user-attachments/assets/d4d769e9-148a-410d-8a4f-6322f06b2eaa)


  - let see how sagemaker experiments look like:
  - once we start a training, we can organize one particular training as a sagemaker experiment.
  - As you know that every research project needs a lot of runs, again and again working with
    different set of changes to get the final job done, which is to get the best model possible
    for our use case.  for that we have experiments. in which we can track multiple runs of the same kind.
  - in this diagram , we can see we have AWS cloud, inside which we have sagemaker domain, and inside
    sagemaker we have jupyter lab instance. in that jupyter lab instance, we would be writing some code
  - then we would be doing some pre-processing , then some training and then little bit of evaluation of
    how the output went.
  - and we can track all these metrics, in to a sagemaker experiment.
  - now, with this sagemaker experiment , we can logon to the sagemaker ui and see output of all metrics that we track.
  - lets say we make certain changes again, and then whole pipeline that we created as code.
  - The code runs, the pre-processing happens again , and then there's training and evaluation , this time
    there was different log outputs and some different metrics that was generated , which can also be now logged in
    sagemaker experiment.
  - so all these metrics and different chages which we did can be put in **central place called sagemaker experiments**. 
![image](https://github.com/user-attachments/assets/f3f5e876-7041-4f5e-a885-0ea51a5a1be2)

  - and we can go there in future to just see how all these runs performs
  - we can also then save the dataset in s3 and when the model is ready we have a service in sagemaker
    known as model registry, where we can save the machine learning model artifacts.


Summary:
========
 
 ![image](https://github.com/user-attachments/assets/2bf9f396-44bc-4728-97fd-bb098c925b48)

 
