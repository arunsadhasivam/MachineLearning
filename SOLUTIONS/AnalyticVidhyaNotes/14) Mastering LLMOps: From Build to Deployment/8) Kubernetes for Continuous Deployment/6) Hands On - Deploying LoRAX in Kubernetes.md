![image](https://github.com/user-attachments/assets/2d9c999a-0659-494c-bd15-7645b8cd6d69)Hands On - Deploying LoRAX in Kubernetes:
==========================================
![image](https://github.com/user-attachments/assets/647a29b3-42e7-41d1-b48d-773e057f0898)

  -  now to start installing all parts which are in docker container in the kubernetes cluster,you
     would have to head on to another folder which is up over here known as EKS artifacts , but
     before we do that , first thing we would have to do before installing main docker container is to first create a secret file.
![image](https://github.com/user-attachments/assets/792c240d-5f05-47d6-949a-297f6575e45f)
 ![image](https://github.com/user-attachments/assets/64fd6c89-9766-4fd1-8c1e-bbb34bbec8c6)

  - a secret file is a simple resource in kubernetes which can provide different parameters to the parts and this would be
    encrypted and stored in kubernetes cluster.

  - open the secret.yaml file, you can see that you have to inser the hugging face token
  - create env file , inside then create a HF_TOKEN(hugging face token)
  - once done go to deployment.sh


deployment.sh
===============

![image](https://github.com/user-attachments/assets/93ed8cfd-5b33-4674-979a-075591fda648)
![image](https://github.com/user-attachments/assets/b1043728-14b3-4b7c-bfeb-669053463000)

 - go to terminal bash > run this command
      bash 9_deployment_to_k8s.sh


deployment.yaml
=================

    - match the deployment to be able to find the pods.
    - name of the container is lorax


![image](https://github.com/user-attachments/assets/cb9930bf-74f6-4ad7-88c0-65c5f53f0b1a)

![image](https://github.com/user-attachments/assets/b82be994-5888-4caf-aef0-8c1684ab3a00)

   - application takes some time to start, so until that time the request should not be send request to container
   - loarax if not present , it takes up from the google registry.
   - running on port 8080
   - liveness probe, startup probes are 2 probes
   - the application takes some time , time till it starts it should not send request to given pod.
   - to ensure that it does not happen, 2 probes are useful.
   - these probes gives ml container or any other container to give enough time to start up ,
     once the container responds successfully, we just then run something called the liveness probe.
   - it justs checks and waits for the application to be live.
   - so whenever the application goes down, the liveness probe fails which restart the container.
   - so for our lorax container, if we do a http get on the slash health endpoint on port 8080
     we do get the success 200. this way we can ensure that the liveness probe succeed.
     
   - and the same for the startup probe but we just mentioned that it is okay to fail **600 times every second**.
     this means for 10 minutes , which is enough for the container to startup and load the module in GPU.
     would be provided before the liveness probe would run and restart the container.

   - we are also going to provide some volume mount and some environment variable as we can see , we have
     also injected the secret using the secret name - HF_TOKEN secret and the key that we are looking for
     his the HF_TOKEN so this would automatically be provided.
    - the model that we want is mistral module, these are the environment variable using the variable module_id

     

Install:
=========

  - install the project using command kubectl
     kubectl apply -f deployment.yaml

  - see deployment finally done.
  - we can see that the deployment done and if we do kubectl get pods  you will see these pods are
    in container creation stage which means that first the docker images would be downloaded and these
    containers would be run , so after some  **you can that the status becomes ready**.


service:
=========

![image](https://github.com/user-attachments/assets/6bb52fef-55a0-4559-a4f3-8fdadcd893ea)

  - service basically load balances all these pods for us.
  - if we do a selector called **app lorax** we will be able to fetch all the pods that are specific for the lorax container
    and then we would be able to load balance them in kubernetes.
  - name of the service is lorax-service.
  - to connect to service , connect to port 80 , but internally the service connects to pod and forward
    the request to the target port 8080 and the service type is cluster_ip
  - go ahead and install it.
![image](https://github.com/user-attachments/assets/1a3069fb-4972-4328-9b42-503bee28ae81)

![image](https://github.com/user-attachments/assets/289b9600-db7d-4dae-842a-1fc4235ec588)

  - to see the pods run kubectl get pods.
  - get details of the pods , we will see that the pods are in still container creation phase.
  - again do kubectl get pods , we can see the status is that the container is assign to given node
    and that node is now pulling the image that is required to run it.

![image](https://github.com/user-attachments/assets/6eae7278-613f-4de7-b575-9b660ad4425f)
![image](https://github.com/user-attachments/assets/0f4fd4fb-ab3a-43b0-ad9f-9d44a79526ef)
![image](https://github.com/user-attachments/assets/e8eb06d4-b49e-4718-8c9d-d699573e0c65)
![image](https://github.com/user-attachments/assets/f3ccbb9a-720a-4bc6-a3ce-891cc497de45)

  - put watch on pod get to get again and again.
  - to get the log of specific pod
  - time to install loadbalancer infront.


Load balancer controller:
=========================

![image](https://github.com/user-attachments/assets/ec7405a1-098f-42bc-ac32-af5d86604f86)

  - attach loadbalancer in front.
  - now we have installed load balancer controller, previously to be able to create a load balancer in AWS
    and attach to kubernetes is very simple using ingress.yaml.
  - ingress.yaml file to attach
  - one of the things would be the target type which means the ip address directly and the type of load
    balancer that we are looking for is internet facing.
  - which means that the load balancer would be publicly available to internet.
    and here by simply specify the rule that to this load balancer for any path we want to simply
    direct it to the service called lora-service and port no 80 where it is running.
![image](https://github.com/user-attachments/assets/81b89e21-e2f5-4436-b3f0-577816d5eb9c)

   - then the service takes the request , and from port 80 it forwards to the container port 8080.
   - now simply we need to install this.
   - once we do that, we would see a new load balancer would be created in AWS and for that
![image](https://github.com/user-attachments/assets/e62811ca-bb26-4c29-969d-c0fe53037e3f)
![image](https://github.com/user-attachments/assets/bf878698-6ce4-493f-8952-afe9643debee)

   - to view that go to EC2 Features > Load Balancer
   - the dns name can be changed to userfriendly.
   - this dns is the public facing ip
   - we have /health endpoint that we are calling, you can see we are getting 200 as response code.
![image](https://github.com/user-attachments/assets/4190a36e-1f08-4bb2-92f9-28002e0d44b5)

swagger documentation.
![image](https://github.com/user-attachments/assets/61d475bb-9787-4a0e-8a63-c3a17a112e64)
![image](https://github.com/user-attachments/assets/5e082dc0-6c7b-417c-8d02-1ea5cf245930)

   - we can also go to swagger docs of lora endpoint
   - we can see lorax deployed with different endpoints
   - /generate, /generate_stream,/health,/info endpoints.
   - now simply use it with model of our choice in our case mistral ai.
   - now successfully deployed our machine learning model in kubernetes.

![image](https://github.com/user-attachments/assets/e8e128c7-0f50-49cf-baec-1a723e8ff245)






  
    



