Hands-on Session on SageMaker Deployment:
===========================================


    - we see how a model is save.
    - now, we see how to deploy the model.
    - for deployment, we dont use the same container, which we use for training , reason being training 
      and deployment are heavily dependendent , we will see why in some of the later videos.
    - now , we will see that we have another container created by hugging face specifically made for deployment.
![image](https://github.com/user-attachments/assets/b211978a-e514-4876-962b-55078cf9030c)

    - we will load that 
    - hugging face estimator that we created before for training we can use the same estimator , to get the s3 path of the module.
    - we go to s3 datasource and s3url other wise we can copy the same (hard code and use it) for now.
    - llm_image would be used for inference would be this.

Config:
=========
    
![image](https://github.com/user-attachments/assets/b1a8b61e-3cb6-4fa7-b5a2-9049cd327125)

  - in config , copy the model from s3 to local path.
  - mention no of gpu, max_token
  - this is then for the server using for docker container hugging-face image.
  - again create a hugging face model, give a nice deployment name.
  - role to be able to copy from s3 and make it available in local machine.
  - image_url - docker image url.
  - model_data -
  - environment config.


deploy:
=======

![image](https://github.com/user-attachments/assets/978a3853-5435-4380-869a-a5bf10d8c303)

  - deploy with instance count 1
  - deploy_instance (GPU machine)
  - container_startup_health_check_timeout - healthcheck (5 min) if it is not available after 5 min , they fail model deployment.
                                             5 min then is enough for model to startup, load and run.

  - run it
  - model is created u1-sql-generator-model.


Evaluation:
===========
![image](https://github.com/user-attachments/assets/87cf83c7-e19e-4204-8791-c9d704f85a45)
![image](https://github.com/user-attachments/assets/35914f5d-a8b5-474a-b3dc-7e4d914d0bb0)

  - sagemaker studio from the left , click on models > see model created over here.
  - creating a model is not essential not same as deployment of model.

Model cretion vs deployment:
=============================
  - model is basically a set of artificates which has all the information needed to deploy it.
  - we can see from this model, we can generate a model we have all the environment variable needed to run it.
  - the model data location  from s3 where we can find it a docker image to run and then click on deploy it to
    automatically deploy it.
  - other wise you can use sdk to deploy it.
  - some times we use it , sdk to deploy model using model.deploy() as above function.
![image](https://github.com/user-attachments/assets/d2a1d548-ab0d-4f27-b71a-4d60bad77125)

  - this then creates a deployment which we call endpoint.
  - the endpoint is using all of the information to deploy the model.
  - if we click on endpoint , we can use the setting (iam  role)
![image](https://github.com/user-attachments/assets/6473febf-08f2-437f-95e8-7986260f01ad)

  - you can do the test inference by provide the json file or use sdk to programmatically test it.
![image](https://github.com/user-attachments/assets/3e1bb81d-1ce7-43c5-9e84-68b570875ae6)

  - you can see all the training jobs that is happening on the sagemaker dashboard as well.
  - go to sagemaker > see training jobs
![image](https://github.com/user-attachments/assets/4eedb2e3-2744-4dba-bcd6-85aa08ae7eb3)

- for endpoints go to endpoints 
![image](https://github.com/user-attachments/assets/dbe16ab3-7f87-4025-891f-104e814d4737)


metics:
========

- now in deployment state. you can also see other metrics as well as cpu-utilization, memory utilization to see
  how the model performs.
![image](https://github.com/user-attachments/assets/500b899c-087c-4c1c-8a82-8b91a86c3e67)


ALarms:
=======
![image](https://github.com/user-attachments/assets/b70c2c47-d3a5-4597-b25d-9257f144dbe3)

  - you can set alarms
  - this make it really easy to create and deploy the   model that we have created , as a final rest api endpoint.


Logs:
=====
![image](https://github.com/user-attachments/assets/2d7e6d45-ce8b-411c-973e-51d70234360f)
![image](https://github.com/user-attachments/assets/aec684d5-e7eb-4be3-9e26-a04a565e5330)

  - you can also see the logs
  - this makes it really easy to able to deploy the model that we have created as a final REST API endpoint.
  - you can also click to see the model container logs.  
  - it takes to another service called cloud watch.

![image](https://github.com/user-attachments/assets/be4029d6-6bf6-4e06-a679-1fb1183cad27)
![image](https://github.com/user-attachments/assets/4e21e943-91ee-4c9e-a4ff-e1080dd028de)
![image](https://github.com/user-attachments/assets/c4891a38-ed12-43bb-8add-b54fbb9be0bb)

go to cloud watcher to see logs.

![image](https://github.com/user-attachments/assets/f7d7a436-5fe6-4a0f-8260-5b06ff493e76)

Evaluation:
============

![image](https://github.com/user-attachments/assets/576110a6-01ca-4d29-a860-dd3139cc2749)


- we now be do inference on this endpoint using same sagemaker sdk.
- the way we do it , would be by first creating the boto3 client.
- load dataset which is present in s3,
- makesure load in to local
- we will then create an instance of predictor.
- which needs endpoint name, the endpoint name we get from llm we created earlier.
- but this is just string of endpoint value.
- this creates a deployed llm.
- we create Serializer , deserializer type.
- then we create request , the request then takes any given sample.
- it applies the same chat template that we have for the prompt ,
- then print the prompt we have
- and print the values as role assistant.
- we take the random sample , we will see input message,
- we also see expected output, also see the generated output which we just got using request function.


  ![image](https://github.com/user-attachments/assets/609bd5bb-7038-495f-9fae-240d88ff736f)

- we see input message was like this
![image](https://github.com/user-attachments/assets/4b2a23a7-872f-488c-a944-04a23f46bb60)

- we see all the prompt, all the values, expected output which was something like this
- select region, name, sum(biomass) from farmingregion.
- this is how the prompt looks like just make sure using hugging face.
- we just made sure that we using hugging face that we change the prompt into input type
  that the model needs  , we send it for inference.
- as you can see , just 5 min of training, it is able to give output that we are looking for.
![image](https://github.com/user-attachments/assets/8abbf350-77c7-4ac5-9ea1-29334188b059)


delete the endpoint:
====================

![image](https://github.com/user-attachments/assets/d1d4ebfd-a221-4785-ba02-60d18078bfac)

 - so if just delete the model and delete endpoint , it just delete all the 2 things that we have created.

![image](https://github.com/user-attachments/assets/38609d16-7105-44b4-97e8-ffd78b2ff839)
- Also the deployed version of it , the endpoint is also deleted.

summary:
========
![image](https://github.com/user-attachments/assets/953a3739-75cb-4d23-8e01-a3397a42ce8d)

  - end to end what we did was
  - we trained the given model in to one of the sagemaker training jobs.
  - we also deployed it and checked the output of the training.
  - everything is now logged properly in AWS environment.
  - sagemaker has model artificats at multiple places, it was also saved all the files in s3.
  - this is how the whole **training and deployment** can happen in sagemaker.
  - now we will head on to know how we actually take all of this and create a end to end pipeline.
