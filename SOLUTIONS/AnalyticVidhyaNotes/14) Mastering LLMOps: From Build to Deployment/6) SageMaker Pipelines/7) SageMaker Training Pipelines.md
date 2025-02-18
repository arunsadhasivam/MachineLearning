SageMaker Training Pipelines:
===============================

    - so, now we know that we know how to train LLM in sagemaker , we can actually automate the
      whole process end to end , this is where sagemaker pipeline comes in.  


SageMaker pipeline:
=====================
![image](https://github.com/user-attachments/assets/70852c05-fc2f-47cd-acef-985e2b52007a)

  -  in Sagemaker pipeline , as you can see we have aws cloud region, inside this we have one the
     service  being sagemaker pipeline.
  -  so, pipeline is a series of steps with a specific purpose.
  -  so, over here , we can see that the data processing is one of the step, followed by training and evaluation.
  -  certain condition , which ends with being saving the model and failing.
  -  these are multiple steps that are put in place in sagemaker pipeline.
  -  A directed acyclic graph is automatically created.
  -  so basically these steps can be run one after the other in parallel, but at the end of the day cycles are not allowed.
  -  automatically manages and creates EC2 infrastructure.
  -  As, we can see these steps can run on different types of instance, and would automatically created the sagemaker , and even
     destroyed the sagemaker.
  -  it is also available as a python sdk , so the **sagemaker pipeline package that we saw earlier(5-hands on sagemker studio video)** is applicable to this.
  -  in which one of the module  called pipeline (previous 5-hands on sagemaker studio)
  -  which we can simply use to create a whole pipeline.
  -  and it is fully integrated with the sagemaker studio ui.
  -  so , all the features that we saw in the training , is also applicable to sagemaker pipelines.


why do we even need pipeline:
===============================


  - Now, lets answer questions why do we need pipeline
  - so , we have features like automatic step retry , step caching, by which if something fails
    the whole process can be repeated again.
  - And then we have step caching.
    
Step Caching:
=============
   - A lot of times, if we are running the whole pipeline, we dont actually need to generate the output
     if we see it matches the certain criteria.
   - this saves a lot of times.
   - we have something called global parameters.
   - so, lets say we create a pipeline , in which we simply specify no of parallel processing that should happen.
   - we can set it up as a global parameter or may be some of the experiements, sometimes you want to run it  on different
     kinds of machines that we can just specify while running the pipeline .
   - this can be one of the parameter in which you can specify that the data processing steps should happen in the particular machine.

 Lineage tracking:
 ===================

      - then we have data lineage tracking, and we have an integration with s3 for IO.
      - in which , because pipelines need data to be fetched and stored from s3, this really helps us and forces us to 
        standardize the whole process.
      - and then we need containerization as well.
      - the pipeline code cannot just run in one of the jupyter lab instance , it needs a proper container , and this forces us to
        actually containerize the whole application.

 Infrastructure provisioning:
 ============================

     - it supports for spot instances as well .

Advantages:
============

    - one of the biggest advantages of pipeline is that we can have:
        1) step retry
        2) step caching along with
        3) spot instances 

Spot Instances:
=================
![image](https://github.com/user-attachments/assets/0c20d5c5-5091-490c-a384-6efdefac3f24)

    - spot instances are instances by AWS in which multiple users bid for the machine and based on the
      bidding, sometimes it is transfered to other users .
    - and these machines can die at any moment.
    - and so in spot instance , biggest advantages is you get 90% of cost-saving but there is a risk that the machine
      might be taken away from you in between.
    - Now, by implementing automatic retry and step caching, we can know also using spot-instances . because the pipeline
      is now more robust and can actually using retry, try to train the model even though the some of the machines has failed.
    - and then we can sagemaker experiment integration.
    - so all the things that we saw before in the projects is also something that is applicable over here.
    - if we implement a pipeline, then it is automatically tracks the hyperparameters , the model artifacts, the evaluation metadata
      that is created and other metrics.
    - so, now let's discuss , what are the different kind of steps that sagemaker supports.


Sagemaker pipeline steps:
==========================

![image](https://github.com/user-attachments/assets/0e0eae14-df48-4c18-a2f1-9f4e4fbf046e)

![image](https://github.com/user-attachments/assets/f4f63d38-130a-4dbf-a665-6b142d918f2d)

1.processing steps:
====================

      - used to create a processing job and specifically made for data processing.

Use cases:
===========

    - we want to data pre-processing or post-processing , sagemaker processing steps will be called.
    - this can also be used for model evaluation after training, and can also have the output files as evaluation reports.
    - and so processing's output can be a file which is stored in s3 or a full-fledged evaluation report that you can even
      pass to next step.
    - now lets see how it works.
Working:
========
    - so, sagemaker starts a processing job with the EC2 machine that we specify in the processing job parameters
    - we also mention the s3 data and so processing job will copy the data from that s3 to the local location in Ec2 that we specify.
    - it can then run the script with the container that was mentioned.
    - and then once the script runs, then copies the output back to S3 location that we specify.
    - and now , this machine is deprovisioned. 
    - all of this is done automatically by sagemaker.
    - we just mention all of this as a parameters in the processing step.
    
Module Training step:
=======================

![image](https://github.com/user-attachments/assets/64bb9c50-ae1e-4b4b-8ed5-1bc49d66988a)

    - and then we have module tranining step
    - specifically 2 steps are there :
       1) training step
       2) tuning step.

1.Traning step:
===============

    - As the name suggests, training step is used to train a machine learning module.
2.Tuning step:
===============
    - whereas tuning step is to do hyperparameter tuning for a given model.


Use cases :
=============

![image](https://github.com/user-attachments/assets/3cf11740-3f14-4147-9d83-349d9050a35b)

  - now, let see what are the usecases of the training step.
  - you can train models with pre-built containers or can even bring our own custom container to train these models.
  - hyper parameter tuning can run the models in parallel,based on the parameters that we want to optimize on
    this tuning step can actually run models in parallel to speedup the hyperparameter search .
  - and based on the tuning objective, top 50 performing versions are retained.
  - so, these are top 50 best performing models for that particular parameter that needs to be hyper-optimized.
  - and so lets see how model training works.

How it works:
=============
![image](https://github.com/user-attachments/assets/7b1407d2-72fd-426d-ad0e-b6e84c31a0fc)

  - sagemaker starts a job with EC2 machines 
  - takes the training and validation data from S3 and copies it to EC2.
  - now, as we can see, training needs training and validation data, which are specifically mentioned 
    in the arguments as to what all specific locations the training data resides in and validation data is present in.
  - Now, it can run one or multiple container based on if it is a training job or a hyperparameter tuning job.
  - and then we have container logs which can be tracked.
  - we can also specify a specific regex pattern, by which we can also filter and only send that particular output 
    as something that needs to be tracked in the sagemaker experiments.
  - and so not all the logs are important.And so the regex pattern is really a good way  if you want certain metrics to be
    tracked.
  - and after training , we provision all of the machines automatically,

Module Inference steps:
========================
    
  - And then we have model inference steps.
  - This is specifically used to run the inference on the final training model.
  - This specifically has a
      1. model step.
      2. transform step.

1.model step:
==============

    - model step creates a model for the model registry 
    - so basically this model is not deployed.
    - these are just artificats which is stored in S3 and then a model exactly knows 
      1) where these  artificats are , 
      2) what containers should be run to actually spin up the model,
      3) the artificats location in S3 is needed to take these artificats from S3 , 
      4) put it in machine and then run the model.

    - so model step has all the information that we need to successfully retrieve or deploy the version model.
    - and so, if we are satisfied with our result, we create a model step which registers the model and saves
      all the artificats information that we need to spin up this model in future.

2.Transform Step:
==================
![image](https://github.com/user-attachments/assets/44b95adf-aadc-4540-911c-5b9aa7002285)

    - we also have a transform step which can be used to run inference on a large dataset.
    - so, when we want to run batch inference using a machine learning model, we can use a transform step.
    - so a transform step looks like this:
       1) sagemaker starts a transform job with EC2 machine(s)
       2) takes the data from S3 and automatically split in to chunks.
       3) The strategy for chunking can be specified by the user.
       4) all these chunks is then send for inference to different model.
       5) the no of parallel instance that we want to run , is a another parameter that we can simply specify
          in the step 
       6) After the inference is run with all these models in parallel, we also have the capability to optionally
         aggregate the data and then the output is stored back in s3.
       7) After wards , we just de-provision the EC2 machine(s)
       
      
Logical Steps:
===============

  - so, now there are conditions where we want logical steps.
  - what is this means is this? that there are moments in pipeline that we want to fail the pipeline,
    because the output generated is not that good. so , we dont want to waste the resources and the time that is
    needed for the future pipeline.because the output that is generated is not better than the previous one.
  - so lets say in one of the step, we do an evaluation where we compare the present model's accuracy with the last accuracy.
  - if the accuracy in this pipeline run is better, than we create a model step which registers the model as we discussed.
  - And if it fails, than we just create a fail step.
  - when fail step is run, this simply means that the failed outcome has come in and the whole pipeline is considered as a fail pipeline.

Use cases:
===========
![image](https://github.com/user-attachments/assets/e0be8405-7424-494a-9d06-16d8023bd6c2)

usecases where this is useful:

    - so, we can fail the pipeline if a given target evaluation metric is not achieved
    - we can early stop the execution of a pipeline to save on AWS resources and it did not register a given model
      if the performance is not acceptable.

     - then we have event based systems.

Event Based Systems:
=======================

![image](https://github.com/user-attachments/assets/36135027-611d-4830-b99d-88c0f2224598)

    - Basically, these pipelines run from start to finish and then there might be places where we want to do more
    - we want these pipelines to actually send messages, or callbacks to team.
    - we have certain steps
    - 2 of the pipeline steps being the
      1) callback step
      2) lambda step.

1.callback step:
=================

![image](https://github.com/user-attachments/assets/35df8dcf-fc60-4b29-a88b-0e47c570aa49)

  - in a callback step, we send the message to a queue and halt the whole pipeline till further response is received from the
    queue consumer.
  - The queue consumer reads this message, gets the state of the pipeline, and then he can decide if you want to continue or end it.
  - you also have something called as lambda step.

2.lambda step:
================

![image](https://github.com/user-attachments/assets/2a8dc5c7-15ef-488c-9952-f51b63b81165)

  - There is a **service in AWS called lambda Function** which is just a small package which can as container ,does a certain
    function and just exists.
  - this lambda function we can run as a pipeline execution step, and then pipeline waits for the lambda function to give a
    response back or the execution fails.
  - in this lambda step function, we know all the information about the pipeline execution and we can use it to automate
    certain other aspects of things.
  - we also have something called as AWS Event Bridge.


3.AWS Event Bridge:
===================

![image](https://github.com/user-attachments/assets/00874140-8690-4224-80c4-fbf8ec59e5b4)

  - AWS event Bridge which can monitor the status change events across the various features in sagemaker.
  - so there are a lot of events that gets generated when these pipeline run.
  - these things can be state change of pipeline , 
        1) so if a transform job ends and then a training job is started, that also an event,
        2) A new model that is created in the pipeline, that is also a event
  - you can use and subscribe to all these kinds of events and create a other certain automated systems.
  - now, for these event-based systems on a high level , we just want to know that they are used for full-fledged
    automation and orchestration of some kind.

Use Cases:
===========

![image](https://github.com/user-attachments/assets/cc3ba098-1008-47eb-b659-38963b8db257)

![image](https://github.com/user-attachments/assets/f6a792aa-91b2-45ad-ac28-8a89fcc3eaa5)

  - some of the usecases might be
    1) we want to notify the team on a pipeline job or training status.
    2) so, what we simply do is subscribe to event bridge event which will whenever the pipeline
       go to someother step gets notified.
    3) and then we can run something like **AWS Lambda function** or some other system, we can automatically trigger
       and then run and then do something.
  - we can deploy an model, when it is changes the state to approved.
  - so , in model registry with every model and version there is a status of that model.
  - that status can be rejected, approved or needs approval .
  - if an state changes from needs approval to approved and then we can automatically fetch that trigger using
    event Bridge and then start another pipeline automatically which then takes the model and deploys it to production.
  - call with other microservices and notify transform job completion.
  - basically , this is also something that we can do is we can batch transform  a large amount of data asynchronously
    and when all the batch transform job completes we can then notify the other set of microservices that this job
    data is complete and you can have now start using the data for other purposes in downstream task.


Sagemaker Infrastructure:
============================

  - lets see sagemaker infrastructure looks like:

![image](https://github.com/user-attachments/assets/6124cacd-6011-490b-a0f0-157ee728bcf7)

  - As always we have a bigger box as AWS cloud region , because sagemaker is a region based service
    inside this we have a sagemaker domain in which the whole team works.
  - and then we have an EC2 instance, this is where we design the pipeline .
  - the instance has an EBS Storage and then as we can see a user logs in using a role permission,
    this allows him a access to login to the sagemaker domain , create own private space with jupyter
    lab or vs code studio and then design the sagemaker pipeline using the python sdk of the sagemaker package.
  - once that the pipeline is created as code, we can just run that pipeline.
  - This sends the call to sagemaker pipeline  service and based on all the information that we mentioned on how
    the pipeline should run , it automatically creates all of these machine logs into sagemaker experiments
    and if needed saves them as sagemaker model.

Advantages:
=============

  - what are the advantages that we say:

1) one is the standardized library requirement using containers.
2) we have modularized the data fetching and pre-processing using S3.
3) we can run different steps on different steps on different machines.
4) Now, as for a given step, a machine is one of the parameters that we have to specify and then that
   particular step run on that machine . for all the steps, we can specify different set of machines
5) so, if our data processing job is heavy on memory then we might take an instances which is optimized for that.
6) but for training we have a GPU-backed machines  and so on soforth.
7) we have infra-scaling for pre-processing and hyper-parameter tuning.
8) we saw that for pre-processing , we can spin-up multiple machines, and also for hyperparameter tuning
   in parallel and their output would automatically be aggregated by sagemaker.
9) and obviously, we have automatic tracking in sagemaker experiments , so all the things that happens here
    and the things that we specify as parameter are automatically logged in sagemaker experiments.


![image](https://github.com/user-attachments/assets/e21535ac-08c4-4bae-aaea-43011730058b)

- and then we have easy pipeline re-run using global parameters.
- The sagemaker pipeline that we design over here goes to the sagemaker pipelines,
  we can also see it in the UI and we can run it through the UI.
  In the UI , you will see all the global parameter that are present for the pipeline.
- that we have created, and we can just run the pipeline again with this new set of parameters.
