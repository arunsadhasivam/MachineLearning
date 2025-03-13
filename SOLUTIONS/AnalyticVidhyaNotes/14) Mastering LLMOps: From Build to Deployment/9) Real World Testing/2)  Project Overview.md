Project Overview:
==================

 - discuss handson project that we will be working with.
 - first, we would be having lot of virtual users on one of the EC2 machines created using Locus framework.
 - then, as we have deployed in kubernetes already , lorax container , we would be using that, in that case
   on an EC2 machine, there would be lorax container deployed, which will load then different adapters
   from places like S3 or Hugging face hub.
 - This kubernetes deployment is then placed using a deployment with HPA Scaling.
 - so, we have horizondal POD autoscalling in place which will automatically scale UP and DOWN
   based on different set of load that we provided to it.
 - therefore it can scale UP and DOWN and the load balancer will ensure that the load is equally
   distributed between different deployments.
 - so, we have a load balancer in place.
 - this would be public load balancer and then virtual users would hit this load balancer which would
   automatically distribute requests between the given containers.
![image](https://github.com/user-attachments/assets/32ec0989-1651-4501-99f2-455191590b79)


Recap:
======

 - so to recap, we will first use locus for load testing
 - we will use the multi-LORA serving , which would be using multiple adapters in the same container.
 - we will then create virtual users and make them as close in behaviour as the real users would be using
   the application.
 - then we will define the test bench, which is certain testing metrics that we want to do, which could be
   things like number of the users that we want to concurrently launch , how the traffic should go UP and DOWN
   and also certain different values such as
     1) how time the response takes for 90% of the users
     2) 95% percent of the users

![image](https://github.com/user-attachments/assets/6349874e-0fcc-4bb1-898a-f705068c69fe)

 - these are the key metrics that we would  gather using load testing.
 - this is the hands on project we would be working with.    

  
