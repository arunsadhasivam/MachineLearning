Introduction to kubernetes:
============================


    - lets look at the typical problem that we have.
    - when we have initial application , that we containerize and deploy on server.
    - this is ok until we have small no of user, what if total no of users grow.
    - then we have more docker containers of the same applications and for that we would put a
      load balancer on top. the load with lot of users is eventually distributed equally among all the
      containers.
    - this is how scalling takes place.

![image](https://github.com/user-attachments/assets/03ab8127-6ead-449e-850f-37d1bee3a6bf)

  - now, as the service grows , application often shifts from multiple microservices , 
  - so over here , this docker container can just be about the payment gateway, but there could be
    lot of other services, that make the whole application complete.
  - which means application can consists of multiple different modules, and each module has to be 
    having lot of containers, load balance and being used by multiple users.
  - with **time we can see there are lot of microservices that we need to handle**.
![image](https://github.com/user-attachments/assets/1e1cd7ac-96cd-4756-958a-67e5a3c2ebea)

  - this becomes a problem.
  - one of the problem is manual server management.
  - lets say we take a EC2 instance , then increased the complexity of maintaining and managing
    that server is something that has to be handled by the developers.
  - this also means adding new servers and removing new servers after not in use.
  - EC2 health check, we also need to make sure that these machines are working as expected, and no health issues
  - need to take regular backups and for data safety.
  - need to take regular volume backups ensuring the data safety and other functionalities and state that we might need to save.
    which might be used by application in future.
  - so not all the containers are stateless containers.
  - another problem that we see is reproducible and smooth deployments.
  - there are lot of versions for every single applicaitons at a given time.
  - and it is a pain to be able to update a version and deploy all the new docker containers without a down time
    and this is only for one particular module(like payment) we might have to do it for several different modules
    working with different versions and communicating with each other.

  - secrets and environment variable management is also one of the challenges that we have.
  - then we also have to make sure that we do careful resource allocation, which means these docker containers
    when deployed on EC2 machines, should ensure that hardware is used in optimal way and the RAM and cpu of the
    machine is utilized to a good limit.

  - we also have logging ,monitoring and auto healing.
  - which means all the applications logs should also be centrally located or we shold have a way to be able to
    see the logs should also be centrally located or we should have  a way to be able to see logs and look at
    the different debugging sesions as to what is going on these applications.


![image](https://github.com/user-attachments/assets/38e3a162-a898-41e0-ab7b-3b8b6d4b2824)

  - we also have to monitor the lot of docker containers that got created , and then we also we have auto healing.
  - which means if docker container dies, we should be able to  create a new docker container in its place
    and add to also load balancer.
  - all of this with multiple containers, with multiple modules would become a really big challenge for the
    back end engineers and then we also have microservice communication. which means one container might
    need to contact application of some other container.this internal miciroservice communication is also managed by backend team.

  - as we discussed , auto scalling and automatic load balancing is also something that has to be taken care of.
  - after all of this is created, we have multiple different applications with different modules running on
    different versions we now have to give fine grain access to all this applications to engineers and different teams.
    this also possesses a security challenge in which internally we cannot give full access to the whole infrastructure to every one.
  - And to be able to  create a fine grain access control that needs to be solved.



  - therefore we have kubernetes.

Kubernetes:
============
![image](https://github.com/user-attachments/assets/e4488bea-267e-4dce-9574-c12b0414dba8)


  - Now basis of kubernetes is that we provide with different deployment types , we give it all the information
    that we require of the container
  - we give it all the EC2 nodes that we want to deploy on
  - and then kubernetes does all the heavy lifting for us
  - it does all the decision making , it does all the health checks that is needed for whole application to be managed.
  - kubernetes is a open source platforms , that is designed to automate the whole process for us.
  - it can helps us in terms of deployment
  - it can streamline the whole process of whole process of specifying an application and deployment of applications on the servers
  - it can also takes care of scaling.
  - scaling means we might need to scale docker container and Ec2 instance.
  -  This is not just about scalling out, but also scaling in , whcih means that at the moment when there is less traffic
    we might also need to remove certain nodes, all of these is handled automcatically by kubernetes.

  - And as we discussed, it facilities the management of containerized applications and so all these containers are
    fully managed by kubernetes internally.
  - we also have container grouping, which is organizing the containers in to logical units for easy management
    and discovery.
  - so it is not sure , that one particular container is bound to 1 particular machine, kubernetes automatically takes
    care of grouping container and managing where they should be deployed and how  it shoul be managed.
  - kubernetes has been used for lot of years and over 15 years of production workload experience in google and
    multiple organization . it is opensource and enhanced by community a lot.
![image](https://github.com/user-attachments/assets/26512b41-e8aa-4581-bfe3-57992221efcc)

   - it has lot of best practices in built and it is heavily used in organization as a reliable container orchestration platform.


Key features of kubernetes:
=============================
![image](https://github.com/user-attachments/assets/a397a989-cf2b-4ef4-92d8-c43c826fee4d)

   1.fully managed application life cycle:
   ========================================
      - which means that when we have an application, the different version deployment.
      - the different rollback
      - the removing of an application
      - the storage
      - the volume
      - RAM and CPU allocation all of these managed by kubernetes.


  2.Easy Microservice Communication:
  ===================================
      - we have easy microservice communication, in which all these different applications in the 
        whole platform can talk to each other easily.

  3.Role Based Access control:
  ============================

        - we can give fine grained access to different applications to different teams.


  4.Autoscaling:
  ===============
        - we have auto-scaling of containers and node


 5.ThirdParty plugins:
 =====================

     - lot of 3rd party plugins , which is created by open source community , this really
       helps ecosystems as a whole and we are able to leverage all these plugins that makes our job really easy.

 6.Cron Jobs:
 =============

      - cron jobs and statefull sets, which are these additional features, which it is not just meant 
        for not just server based deployments . as web apps,  we can do things like cron jobs
        and other stateful set management  and things like that.
Summary:
=========
        kubernetes is not just server orchestration platform but it has other lot features that we can leverage.
