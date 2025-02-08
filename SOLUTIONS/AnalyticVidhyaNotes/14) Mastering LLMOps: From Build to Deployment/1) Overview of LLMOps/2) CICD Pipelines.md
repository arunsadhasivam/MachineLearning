Overview of LLMOps:
===================


Software life cycle:
=====================

  - majorly divided in to 2 teams
  - DEV and operations.
  - DEVOps consists of CI and CD(continuous deployment)


Continuous Integration:
==========================


 ![image](https://github.com/user-attachments/assets/fb6370e1-806f-466d-a3b0-ed206fe7e1f4)


  - Dev team plans the project scope
  - Git for version
  - Central build and package - this software is centrally taken to another software to build and package
  - then this particular package which is packaged ready for testing.
  - once it is tested, and it does what is suppose to do.
  - specific version of that particular package is ready to be deployed.



Continuous Deployment:
===========================

    - done by the operations teams (OPS Team)
    - the package which was created in CI is now ready to be deployed in multiple env
    - one such env is production.
    - once the package is deployed and it is ready to use , lot of tools have been developed to manage this container
      and to make sure that they operate as they suppose to.
    - they also have to be continuously monitor for their health to ensure that they perform really well in production.
    - this is something that comes under CD.

CICD in LLM:
=============
  ![image](https://github.com/user-attachments/assets/19224162-44f6-4903-8b52-eafbe91c6494)

  - CICD that we took from software life cycle is kind of similar but some changes in context to LLM.

 Continuous Integration(CI):
 ============================

   - CI is a team of data scientist or ML engineer which first take the business use case and then frame the
     machine learning problem at hand.
   - they are multiple data store , pipelines has to be build to ensure that this data is accessible to engineers.
   - we also hae VC and easy collaboration. that is different version control system so that team can collaborate.
   - EDA is to ensure data is of high quality and to have some insights from data.
   - the engineer use  prompt engineer to better get the output of the foundation models.
   - there might be cases where training has to be done in distributed and scalled fashion,  which also to be
     ensured in CI.
   - Then the experiments that is done by datascientist team has to be reproducible in nature.
   - so, these research experiments, even after six months down the line, should be reproducible in the same manner.
     which means, all the artificats has to be packaged  and versioned properly , so that we dont lose track of these
     experiments.
   - once we have continuous model feedback .
   - once the application is live , we get this data ,live data that is captured and can be used to **retrain** the
     models to make sure the **accuracy** keep on increasing or stay same throughout the time.
   - retraining is part of CI, in which we have to maintain these models and keep on re-training them.
     

Continuous Deployment:
=======================

   - The CD is something LLM Ops engineer has to , in which they have to ensure that these models are
     containerized and versioned properly.
   - Security of servers and infrastructures is a key component that should be ensured to ensure that
     these models are not leaked to the outside world and at the same time they don't produce output
     which is toxic in nature.
   - the llm ops engineer also has to optimize the **startups and inference times** of these models
   - also the deployment is also something that has to be taken care of.
   - scaling these models up and down is also something that needs to be done which ensures the smooth
     operation from the **live user side**  and at the same time we dont have to scale so much.
     so that the cost of hosting these models become huge.
   - so there is a very good sweet spot that has to be managed by auto scalling.
   - and then monitoring the model performance are also something that  needs to be done.
   - this is what the whole continuous integration and continuous deployment   **in terms of LLM-Ops**


CI Pipelines with Foundation Models:
=====================================

  ![image](https://github.com/user-attachments/assets/dd85baa4-83c1-445b-a8c0-69252ea2fe65)


   - lets look at one of pipelines to work with the foundation models.
   - pipelines are the steps which are executed one after the another.

1.Feature Store:     
==================
   - so in one of the step we have feature store.
   - data is extracted from the feature store.
   - feature store is nothing but a repository of data , in which we can gather these features
     for our own use case.

2.Data Extraction:
===================

    - Next is Exploratory data Analysis and validation needs to be done.

3.Data validation:
===================
   - just validate the data.

4.Data processing:
==================
    - cleaning the data to be injected for prompt engineer

5.PromptEngineering:
====================

    - we might start give context using the vector store and then calling the foundation model for output.

6.Vector Database:
===================

    - we give context using vector database.

- we keep on repeating this process until we are able to get really good output.
- once this research and work has been completed, we will check the code in the source repository.
- this can be any version control like GIT or bit-bucket.
- once the code pushed to source repository, we might create a release.
- release is nothing but exact snapshot of the code base.
- once release is created, the package is finally created, which is nothing but that particular release
  has packages and libraries that has to be deployed and then containerized in an efficient way.
- this packaging ensure that all the libraries are in place and the application is independent and
  can be run in any environment.
- once the container is created, it is put to another registry which is container registry, this
  container registry can be used to deploy at a later stage to deploy this particular model.
- so ,**model deployment part** will take these container from registry and will deploy it into differnt
  stages and one of the stages being production and then we have live users using it.
- lets assume that, one of our prompt engineering code base is successfully deployed in to model.
- this then might use the vector store or any other vector store which is already present in that environment 
  and then **call foundation model** to **generate** output.
- so this is what an example of CICD pipeline for foundation model looks like.


- in a similar way , we can have a pipeline for model training.

Model Training:
===============

![image](https://github.com/user-attachments/assets/7cd7fb7f-90c4-499d-99dc-e4b8bc3eaf17)

  - process is similar
  - we have again feature store , data extraction (EDA) and we find out features that are useful
  - and then we do pre-processing on that.
  - This data can be then used for prompt engineer, where you can do 2 things:
     1) try differnt prompt on the model to see what output fits better.
     2) otherwise if you want to fine tune , take model and do a model training on it.
        After fine-tune is done , we do a model evaluation.

  - we keep on repeating this process until , we find out a really good prompt and really good
    fine tuned model that fits our use case.
  - we then simply store the **model in the model registry** , which is a repository of all models that needs to be saved.
  - once all this done, this code can also be checked in to source code repository. we can trigger release.
  - the release will take exact snapshot of that particular time and then the packaging starts.
  - once the packaging starts, it takes the model from model registry and also the code consits of prompt that needs to be used
    before calling the model.
  - the whole model and the prompt needs to be packaged together into let's say docker based container.
  - this container has to be saved in some kind of model registry.
  - this model registry then has the final container that can be deployed to the real live users.
  - once this model is deployed , users can start using it and this is how end-end flow CICD pipeline looks for model training.


Advantages of Full Fledged CICD pipeline:
===========================================
![image](https://github.com/user-attachments/assets/155159d1-6037-4daa-9f18-15bf599d2ffa)

 - Automated infrastrucure creation.
 - release to multiple env.
 - as we can see dev deployment, model is deployed for the engineers to test the output.
 - once the output is good enought, we can also deploy the model in staging env.
 - in staging env , we might create virtual users or QA team test the model output and then ensures that
   model is ready to be actually given to real users (stage).
 - then we can take put in to another environment known as production, this is the environment where 
   real users of the application users.
 - this is also something QA team check if the output is what is expected to be.
 - in this we have model which is served to three different kinds of endusers and to ensure that the
   model output is as per needed.
 - then the dev and staging are the **two environment that gives us a chance to correct** any issues 
   that should not actually goes to real user(PROD)
 - so this is what multiple environment looks like and each of these environment can simply
   be created by just running the  **automated infrastructure for a new env**.
 - so tomorrow we have another new env called UAT, we can just run the same deployment script which
   will create a whole infrastructure for us.
 - the cost of each environment is also significant , because over here we have the model deployed in 
   dev, stage and prod.
 - this means three servers are deployed for single applications.
 - so , while having LLM ops it is good we have to ensure that we have significant no of env
   to ensure that the real users dont get affected but at the same time this comes at the cost.
 - multistage testing as we discussed is done in which the engineers and virtual users which are just
   users created through code and actual users get to test the final applications and QA team ensure
   that model does what is suppose to do in all the 3 env.
 - therefore it gives a really good robust testing environment  to ensure that the real users dont suffer.

 - we can ensure security best practices ,  now that we are creating our environment by ourselves by using
   automatic scripts. we can ensure that all these environment has the security that is needed.
 - Monitor the infrastructure changes, so these CICD pipeline can be created in a way which automatically 
   monitor the different infrastructure changes and then we can also ensure that all these changes 
   are also reflected back to the scripts and code that we write to create these infrastructure.
 - so all these changes that happens in the live env are also taken back to the code base to ensure
   that these CICD pipelines are replicable in future.
 - so all the changes in live env can also be taken back and put in code , in future if any new
   env is created, the same set of changes that we did in the past are also present in the new env.

 - in LLM ops we really we really push for  creating the infrastructure via code so that all the changes
   are actually incorporated in the code and reproducable in nature.
  

  
