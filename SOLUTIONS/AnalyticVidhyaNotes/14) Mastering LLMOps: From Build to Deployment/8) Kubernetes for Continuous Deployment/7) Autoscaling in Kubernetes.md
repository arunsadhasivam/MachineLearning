Autoscaling in Kubernetes:
===========================

 - now that we have deployed our given LLM using the Lorax container on top of kubernetes and
   we were able to do inference, it would be cool if it can automatically scale up and scale down
   based on traffic , this is where autoscaling comes in to picture.

Challenges in Scaling:
========================
![image](https://github.com/user-attachments/assets/2fc04de9-1048-4a7f-bff4-22635a3daad3)
![image](https://github.com/user-attachments/assets/a12ff934-9b9a-40a3-b1a9-5bb432e0a518)

 - In scaling, we have to automatically scale container based on certain metrics like
   CPU memory or requests per seconds .

  - we have new containers that has to be automatically created and assigned to a given node
    so this is somethings that we would have to do manually if we want to scale it up to figure out
    in which machine it should be deployed.

 -  after deploying it , we have to load balance it as well.
 -  so, new nodes to be automatically created with all the necessary OS and packages and then
    manage nodes and also the container's health.
 -  once a new nodes is added, and the container is deployed on it , we also need to ensure that
    now the new machine can also suffere high CPU or memory limits and would not can also
    have different issues by which the machine itself doesn't work.

 - also the container inside based on the traffic the CPU and memory might also crash , we also
   have to then container's health at the same time.
 - this is also one of the challenges in scaling that we face.
 - we have to remove nodes when not needed to save on cost.
 - so, scaling up is fine but scaling down is also something should be taken care of.
 - Graceful termination of container to avoid bad user experience.
 - when removing containers, we have to make sure that the request that are on-going should be given
   enough time to actually respond back with the given inference output and no new requests should
   actually come to the container and the existing one are given enough time to be able to respond it back.
 - this is known as graceful termination, instead of killing the container immediately, spend some
   time , and let this container have some time to respond to all the hanging requests in place.
  - in kubernetes to do the automatic scalling , we have one of the resource known as horizondal pod autoscaler.
  - lets discuss more in details , how HPA (horizondal pod autoscaller) works.


Horizondal Pod Autoscaler(HPA)
=================================

![image](https://github.com/user-attachments/assets/952f0cd8-64f2-40c4-bcb2-ab3fb736232b)


- based on the configuration, we can right down the scaling parameter.
- using the metrics API, we can get to know about the different metrics of EC2 Nodes and also different
  types of pods.
- this value is then read by one of the services known as HPA(Horizondal Pod autoscaler)
  and based on the configuration that we told to HPA, which could be scale the application when the
  CPU goes above 70% usage from the given value and scale it to this much number and things like that.

- this configuration is given to the HPA, and HPA after taking from the metrics API knows how all the
  applications deployments are doing and then given our configuration to HPA, takes the decision
  as to the deployment should be scaled up or scaled down.

- now, lets says for our use case, we want that the average CPU utilization between all the PODS
  in the given deployment, should be greater than 70 and if that is the case then scale it up to 5 nodes maximum.
- so, when there would be more traffic, the CPU and memory would increase , this would then report by kubelet
  to the metric server.

 - the metric server then expose it as a API , and this API would then be accessed by HPA and HPA would know
   that the CPU utilization of the POD have increased and the average CPU utilization is above 70.

 - now because it is above 70 , based on our configuration, it should then scale the POD up
 - so, HPA would then control the deployment, and the no of replica PODS would be increased from 2 to 3.
 - now because there are more PODS to serve the request, the average CPU utilization goes down.
 - therefore once it stablizes,thats where the no of replicas would be
 - let says the no. of users decreases then the average utilization simply goes below 50, then the
   HPA gets to know about it,based on the configuration, we can also write down scaling down parameter.

 - because let say we give it that the average CPU utilization should be less than 50,  then scale down the servers, HPA would
   automatically scale down the server.

 - then less no of PODS would serve the traffic.
 - then this way, automatic scaling up and scaling down happens in kubernetes using the metric server , metrics API and HPA.

Summary:
========
![image](https://github.com/user-attachments/assets/730b7967-5dcf-425f-8688-c58e8ebbbcbd)

  - we can automatically update a workload resources, such as deployment to automatically scale the workload
    to match the resource.

  - we have vertical scaling would mean assigning more resources ,for example memory or CPU to the POD that are
    already running the workload.

   - there is a cluster autoscaler that scales nodes as well , based on the usage metrics.
   - currently , in vertical scaling, what happens is we actually deploy the POD with higher CPU and RAM
     but in HPA , we are doing horizondal pod autoscaling .

   - which means we just create another POD with the same specification and this just helps in distributing the load
     evenly to the new PODS.
   - we also have cluster autoscaler, rather than horizondal POD autoscaler , which works along with the HPA and
     it is responsible for scaling nodes up and down.

![image](https://github.com/user-attachments/assets/a151b14e-494b-4201-9edc-c405d45f5fff)

   - so , in our case , we saw that the deployment replicas , the PODs went up and down, but then these pods are
     actually deployed on EC2 machines.
   - what if all the EC2 machines are at max capacity? At this point we also need new machines .
   - so cluster autoscaler ensures that the more no. of nodes are added and removed based on the requirements
     that we have and the limits that we set for these nodes.
   - And cluster autoscaler would automatically sense that and then would add the EC2 Machines
     and when traffic is less it will also remove EC2 machines to save cost.


Project Details:
=================

![image](https://github.com/user-attachments/assets/195a9153-fecc-401b-bf8d-3d08677f7909)

     ![Uploading image.png…]()

  
    - we see manual scaling in deployments, and then  we set up horizondal POD autoscaler based autoscaling.
  
