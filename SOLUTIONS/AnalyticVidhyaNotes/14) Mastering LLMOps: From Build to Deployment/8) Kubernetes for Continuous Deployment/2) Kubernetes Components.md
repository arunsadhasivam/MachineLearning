Kubernetes Components:
=======================


    - kubernetes ecosystem is pretty huge with lot of resources
    - we cover one of the important component that is needed to able to work with kubernetes
      and gain all the benefits that kubernets provides in terms of deployment and scalling.
    - we touch on the most important services in kubernetes and then do lot of hands on project.
    - idea is not to go lot deeper in kubernetes, but leverage some of key important features
      that fits our use case.
      

Kubernets infrastructue:
==========================

![image](https://github.com/user-attachments/assets/acd76b0d-b33e-4925-878c-ea37fd56b38d)


 - so kubelet is responsible to manage a full fledged EC2 machine and will get instructions
   but the final work would be done by kubelet of downloading and running the docker containers

 - and hereby , we can see the user is able to communicate with this container and
   also different containers are able to talk with each other.


Pod:
====

![image](https://github.com/user-attachments/assets/0c2a0e29-c796-4294-9f5f-1bf7a020e7e6)


Deployment:
============

![image](https://github.com/user-attachments/assets/9e909a73-648f-4129-8c31-88896d7b37e7)

![image](https://github.com/user-attachments/assets/fe8c2e2a-1a5c-46b9-a467-e8faf4c47576)


Networking in kubernetes:
==========================


![image](https://github.com/user-attachments/assets/e8a73e3f-d47f-4217-b5f2-7e86267ba55f)


- you can see kubernetes send request to new versions as well
- red line shows it stop sending request to the old versions.
- future these will automatically removed, in this way smooth transition form old to new version
  without actually disturbing the connections done by user.

Service Type:
==============

![image](https://github.com/user-attachments/assets/a938f83d-59d9-441f-87be-392478e28f88)
![image](https://github.com/user-attachments/assets/c7b81efa-f7c6-4ddf-b985-d9e6ff08c59a)
![image](https://github.com/user-attachments/assets/8740b1df-0f69-4a24-bfa7-f5d3e4cd15bb)
