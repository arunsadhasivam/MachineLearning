Hands-on Model Training:
========================


 - now, start with processing step.
 - we would be using processing step to
   1) fill in the missing data(compute missing values),
   2) scale and normalize the numerical fields
   3) split the data in to training , validation and test set
- but the data present where ? it is in s3 bucket.
- from s3 it should be downloaded to machine and then all processes happens , we have final
  set of train,validate,test dataset , uploaded back to s3.
![image](https://github.com/user-attachments/assets/ef584386-4eb7-487e-8ff4-6065dfbaed67)
![image](https://github.com/user-attachments/assets/6e270cf7-b9f3-4478-b74c-b4760b21092e)


Step1:Preprocessing:
===========================

![image](https://github.com/user-attachments/assets/9d4333a8-dd4f-4202-bf3c-a4fbcb956d8a)

- sklearnprocessor does is it has sci-kit learn installed , because it has sklearn process
  we could be sure that scikit-learn would be available with some other packages as well.
- we can simply use the same method, which is the script mode , in script mode we have code
  preprocessing.py which would automatically gets copied.


preprocessing.py:
==================

![image](https://github.com/user-attachments/assets/fa28fde8-d82f-437c-944b-c833bdac6046)


 - we can see how we are assuming sci-kit is present  as well numpy and panda.
 - the file would be made available during preprocessing.
 - we then do feature changes and transform and finally we are able to create our dataset.
 - so we then split in to train , validation and test
 - and then we save it in different dataset format.
 - feature engineering we do
 - main gist is we create a full pre-processing script, which converts the file in to different
   train,test and validate file and save it to local directory.
 - as we can see base_dir - is local and we create train,test, validate csv and which are copied to s3
   once the process is done.

- this code which is present on this sagemaker instance machine, should be available to the
  preprocessing step machine and the way which is done is simply specifying in script mode
  the code which is in present in preprocessing.py.
- just by doing this , this file(preprocessing.py) would be copied to s3 and this would be downloaded
  to the instance - the preprocessing step instance and will run and do all necessary steps required.

- so once we have this processor , where we also mention the type of machine , it should run on .
- this then loads the **container** for us and the role needed and then we create a **sagemaker session**
  where we mentioned the pipeline session.

pipeline run():
================


![image](https://github.com/user-attachments/assets/2b3b7ba2-7004-4c15-8957-8a4fa5bd2271)

- the **fit()** and **run() method**  doesn't actually run now , but it will run later once the pipeline is run.
- thats the advantage of supplying the **pipeline session rather than sagemaker session**.
- so that we first create the **end-to end pipeline** and during the **pipeline.run()** all these functions will run.
- we load all these as well and then we can run the processor supplying the input and output.
- destination should be **/opt/ml**, **channel** should be **processing**
- input is where the data should be copied, during the output all the folders (train,validation,test)
  would be present up here.
- should also be loaded back to s3.
- we mentioned the code file that should run present in /code/pre-processing.py
- sagemaker also make sure saves to s3 , so that later on can use it.
- finally we run this , and create a step out of it.
- we call this step as step_process and name as **avalon_process**.
- code inside the step is step arguments.


Training:
==========

- once the preprocessing is done , we can start training
- in training we would need the validation dataset, and training dataset to be able to do training and
  validation.
- this is something that is in s3 folder path , created by the processing step , we can get hold of this
  path, just by using one of the class which is **step_process** and supply it for training.
- we will see how that happens.
- once the traininig is done , the training artificats which is the model are also saved in s3.
- so , to do this we will retrieve one of the image_url, this is the same thing which we discuss during training
  1) i.e if we have the container name that we want to run , we can provide that or
  2) otherwise there are functions which can helps us to find out what is the **ECR** image_url that should be supplied.
![image](https://github.com/user-attachments/assets/649ed6df-97e4-45ab-8550-d3ee35e60c70)


![image](https://github.com/user-attachments/assets/9422b261-11cc-478f-86df-3d56c12da4c1)

- these are docker containers which have all of the requirements for that particular framework.
- so for e.g over here in the **sagemaker.image_uri.retriever()** we have provided the framework as **xgboost**,
  version is 1.0_1,   python version py3 ,region, instance.
![image](https://github.com/user-attachments/assets/fea02f2a-3a6e-49fc-b788-8c8748775dc1)

- with all these , this is the image that works

  ![Uploading image.png…]()
