![image](https://github.com/user-attachments/assets/003daefc-94a4-4e13-80e9-bc604a9600c0)![image](https://github.com/user-attachments/assets/1355e436-dd5c-4563-ab46-46eca506ba8a)Setup SageMaker on AWS:
========================


    - setup aws env.
    - use sagemaker to setup aws dev environment.


Steps to create AWS account:
=============================

![image](https://github.com/user-attachments/assets/947ff03e-f8e6-42ff-afb8-23708aa65903)

    - top right we can find create aws account > click > take to sign up page

![image](https://github.com/user-attachments/assets/d9e1d699-4e31-4e4f-86b1-fc902a050378)

    - enter the email, account name , accountname can be changed afterwards, need to add credit card details.
    - no charge upfront , wont charge upfront.
![image](https://github.com/user-attachments/assets/f623ebfe-c655-47f7-8eea-653237fd96dd)

    - click on signup
![image](https://github.com/user-attachments/assets/15d5d4f1-a395-48f2-af17-bc727de07830)

    - it will load on the aws.
![image](https://github.com/user-attachments/assets/2702e0b7-6504-4fa4-b0eb-b3cacdb62954)
    - aws is region specific , every region aws has datacenter.
![image](https://github.com/user-attachments/assets/700d6751-b910-408c-9f65-50a778666b1a)

    - for eg. mumbai we have 3 datacenter , which is physically available for 1 or 2 km.
    - every region has 1 or 2 datacenter ranging from 3 to 5.
    - every region has services specifically assigned to it.
    - there may be cases where some services is not present in some of the region.
    - in our case make sure click mumbai, we use throughout the course work.
    - mumbai is the region we use throughout the course work.

![image](https://github.com/user-attachments/assets/ad1d1f82-1554-45cf-85e6-599b0b55a44a)
    - first thing we do , is setup budget.
    - budget is if you reach limit , we will notify by email.
    - for e.g if we use certain aws resources provisioned and forgot to logout or discord, that is where
      budget can really help . you can set limit or about to reach you will get notification.


Set Budget:
=============

![image](https://github.com/user-attachments/assets/1cefdb6c-d3b8-46cc-a75e-e13172b32bb3)


  - in services > click budgets.
  - take to budget home page.
![image](https://github.com/user-attachments/assets/9a149156-1e31-41fb-9a66-41c162e650fe)

  - already set budget for 100 dollars, this wont charge for 100 dollars upfront , just limit set
  - this is for the end of month.
  

To create a budget:
====================

  1) click on budget.
![image](https://github.com/user-attachments/assets/3aec732e-dfb1-4ea8-a056-9b6ff3e1459b)

  2) choose monthly or daily or zero spend budget.

  3) budget created you can see in home screen
![image](https://github.com/user-attachments/assets/2e04db36-136f-4b17-880b-164c9b1e7f84)

  4) you can also see budget history for all months.
![image](https://github.com/user-attachments/assets/44468d82-d601-48b3-93d7-0f744fdeae4c)

  5) aws account by default has certain restrictions in terms of services they can use.
  6) while most of the services are available by default, there are cases in which we have to increase limit for
     certain services.


  7) to do that , to increase service for aws sagemaker, where you launching  lot of instances, to ensure
     those instance are provising in to our account and to start using them , we need to increase **service quota increase**.

Service quota :
================


![image](https://github.com/user-attachments/assets/caffd5d6-bde2-45aa-aed3-4354784306bc)

  
  1) search for service quota
  2) click on service quotas.
  3) go to service quotas home page > manage quota on aws 
![image](https://github.com/user-attachments/assets/26e55ccf-883e-4595-8b2b-e84e003c9b07)
  4) view quotas, lot of service quota already assigned, you can see utilization and defult value.
  5) utilization is what you use for region.
  6) using instance type known as m1.g5.xlarge -> instance with gpu capabilities and by default it is not available
     in aws account.
  7) once you tyep m1.g5.xlarge you can see options in that you select **m1.g5.xlarge.endpoint usage**
![image](https://github.com/user-attachments/assets/0420f6f6-419b-4bb5-8caf-a03b9ba99124)

  8) work on m1.g5.xlarge.endpoint usage
             m1.g5.xlarge for training job usage.
             m1.g5.xlarge for transform job usage.
  9) once you open on these pages you can increase at account level and can set new values.

![image](https://github.com/user-attachments/assets/2bfe716c-c410-406c-a8e8-0542d280fe93)
![image](https://github.com/user-attachments/assets/cc676a8c-d275-4d8e-83c5-969d76976c4b)

10) click on request  , do the same for 2 quotas m1.g5.xlarge transform 

   1) end point usage
  ![image](https://github.com/user-attachments/assets/6b4399a5-91d0-4f0d-8469-4bcdc7d0fc62)
  
   2) training job usage
  ![image](https://github.com/user-attachments/assets/b7f90bbc-2f30-4589-ad5e-305ab8a72901)
  
  3) transform job usage
     ![image](https://github.com/user-attachments/assets/eeacaf78-c560-4bdc-abf0-db782952261f)

11) once these 2 service  quotas for sagemaker is raised , got approved in 10 minutes
12) most of the cases, it is auto approval no waiting.
13) but some of the services requires the aws support center case 

![image](https://github.com/user-attachments/assets/5d1cf06e-de56-41f5-941d-ad8402036286)

14) you can see service quota history in Quota service history.

![image](https://github.com/user-attachments/assets/9ec92c64-d4d9-4fdd-ba17-ea7bc307c92e)



15) you can see each open service quota request can attached to aws support center case.
16) basically aws support center team will raise case for your quota increase and then you can go to history
    and then click on the link.
17) once you click on link, you would be taken to the case page in which as you can see , the details
    are already pre-populated and to what to ask for raise in quota.
    amazon team will reach for increase in quota, most case they automatically increase.
    in some case you need to talk to them and response why you need to increase.

 ![image](https://github.com/user-attachments/assets/a28a9b03-3802-44fa-8402-a804f9877caf)
18) most cases you need to discuss with the customer support team.
![image](https://github.com/user-attachments/assets/e98e55b2-7608-43e9-bd12-1d6715506294)
![image](https://github.com/user-attachments/assets/af4e2b82-de57-4bfb-80f9-02f0e0512f9a)
