SageMaker Deep Dive:
======================


  - now, up to this point, we have seen how to modularize our code really well using langchain.
  - we also how to monitor our application end to end using full-fledged llm platform like langfuse.
  - in this module, we will cover in **depth AWS sage maker**, which is a full-fledged end to end highly scalable
    machine learning training platform.

  - gets started.


Domain :
=========

  - one of the main core concept in sage maker is domain.
  - we can think of it as a collection of users.
  - now this domain could be created for , lets say a team or a department.
  - domain consists of list of authorized users , an undrelying EFS volume and private and public shared spaces.
  - so basically , these users can interact using the public shared spaces , but they will also be having their
    own private spaces for their particular private research.
  - All shared AWS sagemaker services can be seen by all users with in a given domain.
  - so as i said, teams can collbaorate really well , because all the changes and all the running experiments
    would be containerized in to one single domain.
  - domain can be created by quick setup, in which domain created accessing the AWS resources using public internet
    and a standard setup . in which AWS resources are accessed internally without connecting to internet.
  - More fine grained access control over the security and networking.
  - so, basically , if we are new, we can just go for quick setup.

![image](https://github.com/user-attachments/assets/0d0f1042-bf24-4e12-8d41-5d5fcd7961ec)

  - but , if the organization does not want to connect to internet, to be able to use internal AWS
    resources, a standard setup gives them the flexibility to define their own terms in terms of security and networking.
  - so based on this, if we are new , we simply go for the quick setup, which has good standard set of practices already setup by AWS.
  - otherwise, we will go to the standard setup and then setup everything ourselves.


![image](https://github.com/user-attachments/assets/342d416f-42ce-4501-89ef-a7f70b0e1aca)

  - this is how domain looks like
  - the box over here shows AWS cloud region.
     1) in which we have AWS sagemaker
     2) then we have user profile1 and userprofile2
     3) every profile would then be able to access the AWS sagemaker domain using some of the role.
     4) As we discussed in security , our role just gives them permission to access services.
     5) as we can see over here , we have 2 spaces  each of the user is accessing their own note book which has
        underlying storage , these are the private spaces which no 2 users can see other person.
    6) we have shared space in which we can launch multiple applications , as you can see userprofile3 and userprofile4
       are able to **interact and collaborate in the same jupyter notebook** over here.
    7) this shared space also has **shared volume** , so in this way our collaboration is private but at the same time
       also be public. so the whole team can work in multiple project in a given domain.
    8) we have sagemaker virtual machines, we can go to amazon sagemaker pricing page, to see the list of VM
       which are available to use in the sagemaker.

![image](https://github.com/user-attachments/assets/049f5813-174b-4a27-adb0-e2d3c2293f69)

    9) we can setup the region and find the lot of instances that we can use to train or work with the data.
    10) As you can see this instance is called m1.t3.medium it has 2 virtual core , 4gb of ram and price per hour $0.054 per hour.

![image](https://github.com/user-attachments/assets/07ffe423-3470-44d6-9cf5-c5bf4447cfdd)

    11) we have server in EC2 called ml.t3.medium, this is the exactly the same server but only difference is they are based on 
        fixed Amazon linux2 os.
    12) Now, lets go through the different set of instance classes taht we can use in sagemaker based on what kind of workload
        are we dealing with.
    13) we have standard instances of t and 3  , which gives the balance of everything.
    14) we have compute optimize for code , which is very heavy and computation.
    15) we have memory optimized series which is R series in which the RAM would be given more for the 
       database work and lot of analytics needs more RAM.
    16) choosing an instance in R Series would be a better choice.
![image](https://github.com/user-attachments/assets/2557ed5b-eceb-4f03-b6db-bfc9d922d08c)

  - we also have GPU optimized image, this is the G and  P series , so if we have instance called ml.g5.xlarge , for which
    we raise the quota before . that is one of the instances with GPU capabilities.
  - the pricing page , you can see their cost , the amount of eCPU, RAM and GPU memory they have.

  - And then we have certain deep learning inference optimized images called inf series .
  - the inf series is sagemaker's properitory VM  , which are optimized for inference.


Training with sagemaker:
========================

  - when we are training , we have 3 options,
  - we have support for built-in algorithms , in which these frameworks such as
      1) pytorch
      2) tensorflow.
      3) huggingface
      4) chainer
      5) sci-kit learn
      6) MXNet and
      7) spark ML Containers are already present.


![image](https://github.com/user-attachments/assets/d625b43b-d990-4470-bdc0-d267df6e5424)

 - we can just directly start using them for our workload.
 - we also have something called script mode, in which we can use Sagemaker's containers but we can then
   just directly start using them for our workload.
 - we also have something called script mode , in which you can use sagemaker's containers , but we can
   then provide the script to run which will essentially use all the libraries , and it is just
   script will do the changes that we needed.
 - this gives the really good flexibility of using the pre-built containers by sagemaker , as well as
   same time, make code changes based on what we want to achieve.
 - and this has support for both training and deployment.
 - so , basically with script mode , we can not just train these models , but we can also write functions
   in which the same container can now be deployed as a web server.
 - then , we have custom container.
 - so, if we have docker container , that we want to use in sage maker, that is also completely possible
   and then that also can be supported for training and deployment using sagemaker by following certain set of
   guidelines.
 - so, this makes it really comfortable to use the built in algorithms , if we want lot of changes,
   we can also go for script mode.
 - and if you want to use a full-fledged custom solution, then custom container is also a option.
