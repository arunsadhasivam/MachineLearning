Introduction to AWS Services:
==============================

![image](https://github.com/user-attachments/assets/e3b390fc-b231-4ef9-b874-04338a7dcb27)

  - high level overview of AWS services.
  - initially server use to be bought and rent and connected to some kind of network.
  - now, we can just launch a server online , which is also known as cloud services
  - one of the cloud services being AWS,
  - aws launched in 2006.
  - it started with 3 services **EC2, S3 and SQS**.
  - which we discuss later in slides.
  - currently it has 200 services and its not only used to access servers and also lot and lots of features
    which keep evolve over time.
  - it is available in 33 regions, and very region have multiple  data center and total no of availability zones
    or datacenters which we can say 105 currently.


AWS Basics - Storage:
======================

![image](https://github.com/user-attachments/assets/12035d1e-9c39-4543-877e-f9f1bc528417)

1.EBS- Elastic Block Storage:
===============================

    - we consider like harddrive or SSD we use.

2.S3 - Simple Storage Service:
==============================

    - similar to dropbox we use.





3.ECR- Elastic container Registry:
====================================

![image](https://github.com/user-attachments/assets/db3284a7-7730-4dca-8a12-0492d065ce21)

  - docker registry is official registry for docker where we can push packages.
  - same way AWS implemented a **Elastic container Registry(ECR)**

4.AWS Basics - Compute:
==========================
![image](https://github.com/user-attachments/assets/100a3cb1-72aa-4995-8f2f-f15734557a35)


  - we than have compute solutions.
  - Basically Elastic compute cloud offering by the AWS and you can attach different hard drives and SSD to
    different kinds of servers that we will provision in the later  course work.
  - we have **Elastic Kubernetes service**, which just takes these containers  and EC2  machines and
    deploy it and then manages them at the same time.
  - this whole service is similar to kubernetes, which is open source service, which then modified slightly
    for amazon integration,  which is known as EKS.

5.Developer Tools:
===================

![image](https://github.com/user-attachments/assets/646bce24-5304-4dff-8d1b-7b278021e8da)

  - and then we have developer tools, we have AWS codecommit, this is similar to github and version control
    repository inside AWS.
  - you also have codebuild which is similar to jenkins, where your code is taken , build and packaged.
  - we also have code pipeline , which is a series of steps and consists of multiple steps that are run one after
    the another . we finally create a release and put these packages   in to some kind of repository.

6.Orchestration service:
=========================

![image](https://github.com/user-attachments/assets/a7d94aee-130b-410d-a2e6-2bb6b0dd2cbe)

  - then the orchestration we have 
     1) cloudFormation.
     2) EventBridge
   
      
1.CloudFormation and Terraform:
================================

  - so all these infrastructure that needs to be created can also be done using YAML Files.
  - then we use these YAML files , to create multiple infrastructure, by chaning small parameters here and there.
  - so one of the services in AWS is cloudFormation which helps us to create these YAML files and also helps to
    create these YAML files and automatically  infrastructure.
  - Another **IEC Services which is Infrastructure as Code**  is known as **Terraform**  which is widely used for this
    same purpose.

Event Bridge:
=============
  - event Bridge which is similar to cron jobs in linux
    where we can get notified for different triggers and changes which happens in our infrastructure
    and then we can also take measure around it.
  - we can also have automated triggers created by different cron jobs.
  - and we can also setup regular intervals which these would be created based on multiple parameters and then
    event bridge   will notify or do those changes.

COmbination of CloudFormation and Event Bridge:
================================================

  - so basically combination of cloudFormation and eventBridge can be used to automate and create a lot of things.
  - these are one of popular AWS offerings.


7.AWS Basics - Artifical Intelligence:
======================================
![image](https://github.com/user-attachments/assets/52ad092d-f055-466c-bc32-f773bef5da81)

   - For AI(artificial intelligence) we have AWS SageMaker which is their full-fledged machine Learning Platform.
   - which we will deep much in later of course.
   - then we have AWS BedRock , which can be used to access foundation models as API and it is a pay as we go service.
   - we then we also have 
         1)AWS transcribe- which can take speech and can give text out of it.
         2) AWS Translate - which can convert text one language to another language.
         3) Textract - can take documents and then do OCR on top of it.
         4) Polly  - can take documents and then can speak multiple languages with different accents.

8.AWS Security:
===============
![image](https://github.com/user-attachments/assets/e7290a7a-6a82-402e-98f5-d9cc45e0ef63)

  IAM (identity and access management) :
  =======================================
    
    - on a high level, what it does is every user has their own particular account which we can see over here.
    - the user can also be added in to multiple groups.
    - service accounts are just accounts from machine and then this user is given access to certain policies
      which is access and deny rule to be able to have access to other services.
    - a policy would be a document in which what are all permissions are available for the users are written down.
    - these permissions could be allow or deny permission.
    - also have role which is access to services.
    - if one service want to talk to another service, we can attach a role to it, which allows that particular
      service to be able to access the other service.
    - on a high level , this is all that we need to know and security in and itself is a full-fledged topic
      in AWS . but for your use case it is fine to know this much.


    
  
