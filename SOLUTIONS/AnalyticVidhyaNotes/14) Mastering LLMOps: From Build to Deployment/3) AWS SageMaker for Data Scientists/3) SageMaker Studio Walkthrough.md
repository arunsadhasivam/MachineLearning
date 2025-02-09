![image](https://github.com/user-attachments/assets/629e78ab-4d62-4cde-9ba8-05fcb649c722)SageMaker Studio Walkthrough:
=============================

![image](https://github.com/user-attachments/assets/196d37b9-0c7f-4afd-aafe-392cd8bc5f11)

    - Account now have high limit , then suppose to be having for certain cases for services.
    - login to sagemaker , full-fledged machine learning platform by aws.



 Sage Maker:
 ============


 ![image](https://github.com/user-attachments/assets/0d5d66c4-1be3-4d78-9d4e-5aed60b7fab6)


  - click on search > sagemaker to login to sagemaker.
![image](https://github.com/user-attachments/assets/0fab95d5-28e8-4e9d-96db-8920f1c642b4)



1.domain:
===========

 - click on domain
 - click create domain
![image](https://github.com/user-attachments/assets/f9fece23-9abf-4091-a903-4422d357875d)

 - we discuss on how to setup domain
 - 2 options to setup domain
![image](https://github.com/user-attachments/assets/03ea483b-d9dd-4601-925d-18ae7738cb0d)


1.quick setup:
===============

   - select quick setup it took 2 min.
   - on domains page get a new domain.
![image](https://github.com/user-attachments/assets/2fe95a7f-a727-4f48-ae07-c1d212a4dff4)
    - click on the domain created above open the domain settings.
    - user profile you have default user already created.


![image](https://github.com/user-attachments/assets/4f65825a-27af-4285-be02-b176773facad)

    - you have default user already created, once you see created click on launch.
    - it open aws sagemaker studio console.

![image](https://github.com/user-attachments/assets/55e9d9f7-0dba-4d2f-a995-37653eddbfad)

    - you login automatically to it.

![image](https://github.com/user-attachments/assets/c07511c4-1937-4139-8023-497292cae5ff)
    - left you see all apps.

![image](https://github.com/user-attachments/assets/bcb9da87-5424-424d-92be-f1476e7fc758)

    - click on jupyter lab.

    - click on jupyter lab space with giving name

![image](https://github.com/user-attachments/assets/a30f2618-2730-48a8-96be-7a8485aaca49)

    - click on create space, it take few min.
    - once the space is created , you can see instance you can choose.

![image](https://github.com/user-attachments/assets/bcfd7245-ba0a-43a2-baab-d9baf844672e)

    - you can choose which machine you want to launch.
    - in terms of underlying storage , please increase 30 gb

![image](https://github.com/user-attachments/assets/224e2059-511e-4568-8303-1f4df5e96337)

![image](https://github.com/user-attachments/assets/279cca7f-9512-4d1d-9782-af37e080aac7)
     - click run space after selecting instance,image, storage.
     - it then starts to provision a machine for us.
     - see status is staring 

   ![image](https://github.com/user-attachments/assets/3cd90661-9a05-4eb0-acdc-e5af1f970527)

    - list down all running instance we have.
    - we wait for some time  1-2 min
    - now open jupyter lab.

![image](https://github.com/user-attachments/assets/df1e5936-be5e-4891-8211-de09c4845657)
    - open jupyter lab , takes us to jupyter lab inside sagemaker env.

![image](https://github.com/user-attachments/assets/002e14a7-946c-48ee-b4ea-aacffe48d596)
    - you can initial screen.
    - left you have file browser.
    - it shows open kernel, terminal and github repo to clone.

![image](https://github.com/user-attachments/assets/437f570b-705e-4382-976f-7a18da075512)

![image](https://github.com/user-attachments/assets/c55a8717-3beb-49ae-aeef-0347dcca4efa)

![image](https://github.com/user-attachments/assets/cc6ca4ca-e388-4e68-98df-687a8c3278ef)

    - clone git repo
    - launcher you have python notebook,also have option to open terminal , textfile, markdown.
    - lower left you have instance memory to see how your code performing.

![image](https://github.com/user-attachments/assets/e9999646-1b8f-4cf0-9f7c-abf084810173)
    - this is how setup dev env.


Logout:
=======

  - very important , we cant simply close the tabs.
  - because that wont remove the VM that we have provisioned right now.
  - to do so , we have to go to sagemaker studio > save all our changes will you logout
  - in sagemaker studio once you saved all the changes > click on stop space to remove vm.

![image](https://github.com/user-attachments/assets/7db7211d-2f31-4aef-bec5-d545ee94da55)

  - Also over here , when we running the vm notebook, for e.g when you click on langchain, it open one of notebook
  - when you run any cell over here, by clicking on run button you can see it open up launcher and kernal.

![image](https://github.com/user-attachments/assets/40162aa7-3cc3-4c00-a590-0caf9519eee1)
  
  - save all our changes, click on shutdown all, it **shutdown jupyter app kernel**.

![image](https://github.com/user-attachments/assets/5b4ace2e-4a30-43f8-b5c6-c865b237a89f)

![image](https://github.com/user-attachments/assets/082d198a-fbb6-42ba-9960-764fe1e9fa51)

  - to remove whole workspace , click on stop workspace.


![image](https://github.com/user-attachments/assets/438325c2-4132-4376-aa6a-6e9e061f07b0)


![image](https://github.com/user-attachments/assets/5e85abc7-ffe7-4438-852a-ad5896989461)

![image](https://github.com/user-attachments/assets/4d37d960-fde4-4ed7-a735-0cfbbaf914ca)


- click on ui jupyter lab space, that is stopping status.
- also verify on jupyter lab also it is stopped

![image](https://github.com/user-attachments/assets/9d1c982c-e7a2-4701-ac12-54ccc37dd725)

![image](https://github.com/user-attachments/assets/d3d14b50-d4e3-49d6-845f-4da51e74da89)


- you can also ensure stop instance and applications as well.
- this ensure that nothing is build while we are not working , now we can safely close.
- click on signout.
- it takes us to domain page.

![image](https://github.com/user-attachments/assets/05855be3-9d35-4916-9eca-6c2b2ca4b495)

- this is all need to setup end-end aws env.
