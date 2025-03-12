Module Recap:
=============


  - challenges with container management in microservices in general.
  - discuss kubernetes can help and lot of kubernetes features.
  - deeper in to deployment basics like
     1) POD
     2) replica set
     3) deployments
     4) different types of deployment like 1) recreate 2) roll
     and how that can be used to give smooth experience to the end user and also makes developer life easier.
  -  net working in kubernetes , how service able to figure out different **PODS and service** can help in networking
     internally between different **microservices** and outside as **load balancer** and how networking in general work in kubernetes.
  -  Hand on session on deployment on kubernetes where we deployed lorax container and get inference out of it.
  -  saw different types of challenges faced in scaling in terms of ,
        1) how nodes should be managed ,
        2) how POD should be managed
  -  then discussed how Autoscaling can be done using HPA(Horizondal POD Autoscaler) in which we deep dive in to what
     are the internals in HPA and how the whole process works. and also discussed cluster auto scaler which can be
     used to even scale node UP and DOWN different nodes.
  -  hands on session on Horizondal POD Autoscaler to create an action, managing the LORAX deployment that we
     created before in kubernetes.

![image](https://github.com/user-attachments/assets/5a112daa-4398-4c7c-807e-0b5cb4bc178a)
