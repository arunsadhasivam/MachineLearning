Hands-on SageMaker Studio Training:
===================================


  ![image](https://github.com/user-attachments/assets/5ddc2da1-8a37-4378-bc99-3d16e91df321)

  - start the training.
  - these are some of the training parameters
  - the dataset path as you can see is not s3 path , it is actually /opt/m1/input .. path.
  - during training the hyperparameters will be specified to the model.
  - now, when they are specified to the model, it is expected that it is **available in local** path
    and not in s3.
  - And so sagemaker what it automatically does is copies the data from s3 to local machine and
    then run the model for training.
  - the place it copies is /opt/m1/input/...
  - and this would be channel.
  - so , we create a channel called training and create a folder called training in local path and this
    would be file name.
  - so, this is the final dataset path , which would be available and would be having the data during our training.
  - so, this is the model_id, the max_sequence length, we are using QLORA and see in the code how this
    parameter gets supplied.
  - we just training for 1 epoch and we will be logging for every 5 steps.
  - the learning rate is going to be 2e-4


step 1:loading our hyperparameter:
===================================

![image](https://github.com/user-attachments/assets/6e98ca50-8380-4837-bea5-d8b7089cb9fc)


  - so , specifically in sagemaker, you can use something called script mode in which we would use
    the container provider which will have all the things installed that we would need.
  - And we can just provide a script that we want to run to be able to train our given model.
  - this makes it really helpful, that we can simply not care about creating our own container and some
    of the standard best practices in all the libraries installed by the creators of these libraries.
  - and so for this one, we would be using the hugging face training docker container.
  - so to do it , we can always see the list of containers, that they have provided,
  - or we can also specify something called versions, which they have provided.
  - for hugging face, there is a value called transformers version and pytorch version.
  - if we specify this  ,this finds out the url of the docker container that should be loaded,
  - if this fails,this means that for this particular transformers and pytorch versions , there is no
    docker container found.
  - what we can also do is , if we know the list of docker containers that are available, which would be
    provided by the creators in some of the readme files on the internet.
  - we can just directly copy the image uri and paste this as the image uri in one of the parameters.
  - so this is what the AWS ECR Repository looks like.
  - This is the account id docker ECR Region amazon and this is the docker container name and the default version would be latest.
  - so, that we can either specify this or this.
  - so for this one, we just specify the transformer version and the pytorch version.
  - we will also mention where this training should happen on what instance and what instance what we have choose is ml.g5.2xlarge
  - this is the place where training would happen.
  - instance count is one. we can also do multi-instance distributed training as well , but for now we just put it as one.

  - this is the max run time , this is to ensure that the model does not run to infinity , there is max stop limit.

  - the role which will gives us the permission to download from s3, upload to s3, or any other things that we would want the
    container to be able to do.
  - now , in environment, we are just putting the cache folder, and the hugging face token which is present in our environment
    would be specified like this.
  - we have python version mentioned.
  - now the entry point is the file that we can provide at runtime, which would be loaded and run.
  - this is what the script mode is - we are saying the docker container to run, but the entry point we want our file to
    finally execute.
  - so, by mentioning the entry point and the source directory, we can then take our code and also save it so that sagemaker
    would be able to use it and run it while doing the training.
   - so, we are mentioning that ther is a file called qlora.py which is right here to take this during the training and
     source directory is dot .
   - (.) which also means that this particular directory should also be copied and should also be present in the container
     while training. this means all the requirements file and /tmp file would also be taken and saved and would now be
     available for training.
   - so you can make sure any folder and any files that you would have also be available during the training and while
     running this all of this would be copied and successfully saved in s3.


   - Another thing to note is that the source directory dot(.) finds the requirement.txt at the root and it would
     be installed by default.

   - hyper parameter provided.
   - metrics_definition - in which the log generated by docker container, if we know the log looks like, we can
     give some regex pattern for the metrics to save.
   - we know that loss is always after every 5 steps or whatever we specify in steps . it is printed as loss and there
     is a numeric value that i want to capture    and so format is something like this , we will see loss.
   - there would be colon and then there was the loss printed that i captured using regex.
   - and this way i have 4 parameters, that i want keep capturing:
     1) the loss
     2) randomization
     3) learning rate
     4) epoch.
   - this would be captured and saved , later on see how the loss went up and down.
   - finally when we create this , we have huggingface estimator ready, this has all the information that is needed.
   - but the one things is missing is how the data set is made available, we only mentioned the dataset path
     which has local path, channel folder , file path  like /opt/m1/input
   - so this is provided during the estimater fit
   - the estimater was created before
   - and with the fit option we provided the data.
   - the channel is training and we then we give the s3 path.
   - and sagemaker first goes to s3 path, and dataset and would make it available in a new folder called training in local
     and start our code.


qlora.py:
=========

    - before fitting we see qlora.py.
![image](https://github.com/user-attachments/assets/32411148-0c8d-488a-be04-4935e48ac7e7)


 - this is the training pipeline code looks like.
![image](https://github.com/user-attachments/assets/d34eef1f-8b01-4c0c-87cb-4d788c49fc5e)
 - now, we can go ahead to run the cell to start training.
 - we can see that it creates a training job with name "q1q1lora-gma2b".
![image](https://github.com/user-attachments/assets/a50b89d1-77c9-46b2-bc82-58ef17e0bfd7)


 - so we can go to sagemaker console on left we have job 
![image](https://github.com/user-attachments/assets/b7a2338d-b8c3-4430-9d64-54f9192c9377)
![image](https://github.com/user-attachments/assets/9183bc13-5677-4fad-ad3f-a8e2f000e1e2)
![image](https://github.com/user-attachments/assets/8d01a281-ab61-413f-889a-eaabbb30eeeb)
![image](https://github.com/user-attachments/assets/a01ee573-da5f-4a61-9324-cd30ddc7e39c)
![image](https://github.com/user-attachments/assets/c19e2254-8396-4b2f-a6f2-ea5d89d0e68b)


- you can see the channel
- now, we can see instance is being prepared , the docker image which is GBs is size is getting
  downloaded, once that is done ,the model will be copied and run. we want to wait for 1-2 min for that to happen.
![image](https://github.com/user-attachments/assets/80236aff-ba6d-4f6d-8f03-8be1135e31a8)

- we have now downloaded the docker image, and now we are going to see that there was script_source
  directory (.) was specified that means copy all the directory and use it.
- and so as we mentioned that there was a requirements.txt that was present at the root, sagemaker would automatically
  would start and install this requirements.txt.
![image](https://github.com/user-attachments/assets/d6687a32-01b2-49e8-a65a-53375f63fd41)
![image](https://github.com/user-attachments/assets/74bf49ab-99d5-4ba0-a4c1-5e5f01679554)
![image](https://github.com/user-attachments/assets/31602e36-272e-41e1-8353-f98e8bca6530)

- we can see that the download happens, after that all the training env and hyperparmeter is specified.
- would now created as environment parameters as CLI parameters and would be provided to our qlora.py.
![image](https://github.com/user-attachments/assets/165d6794-dce2-4186-b308-8fadc0650f7b)




- now you can see qlora.py is called and then trainins is started . so this is now downloading model from hugging face
  using token that we created and we have also permission to download the model.
- you can also go to sagemaker studio and can see these logs.
![image](https://github.com/user-attachments/assets/f69ce35a-a9b9-4e23-a38c-f9fccca90eda)
