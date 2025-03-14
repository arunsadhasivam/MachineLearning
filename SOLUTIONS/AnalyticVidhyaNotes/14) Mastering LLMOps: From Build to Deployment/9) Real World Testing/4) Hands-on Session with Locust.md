Hands-on Session with Locust:
==============================

  - now that we have done a deployment, we would be creating or exposing this container to the outside
    world.
  - for that we need to create a service and ingress.
  - thus we can see we have service_locus.yaml.
  - here the server is running on port 8089 and we would run the service on port 80.
  - so, the service will automatically forward the request to 8089 and we name the service as locus_service
  - we could see the selector would be app:locus.
  - using this selector it would be able to find pods.



Deployment:
============
![image](https://github.com/user-attachments/assets/38989aa5-9afb-475a-bdd5-2676936ca28b)

    - deployment - locus-deployment.
    - deployment has 1 replica.
    - all we did was to create the match label and selector to be able to find POD better.
    - name the container as LOCUS
    - simply give the certain CPU, RAM
    - mention the name of image to pull.
    
    


Service.yaml:
=============


![image](https://github.com/user-attachments/assets/40556da1-9ae3-4148-a518-15654b05574c)

- once service is created then go to ingress

Ingress
========


- Attached a service to load balancer
- we have done this before , and this one to be able to create a load balancer
- for this we need a ingress config.
- type is ingress
- scheme that we want to be internet facing.

![image](https://github.com/user-attachments/assets/6e88fb62-af8b-4db2-804a-ec5c4670ab23)

- finally for all the path  "/" for this load balancer , we want to send it to service (locus-service)
- the service would obviously take the request and forward to 8089 where the server is running.
    
- lets go ahead and install it.
![image](https://github.com/user-attachments/assets/44a32b7c-2c0e-42bb-8ab2-13c5fce66858)


   kubectl apply -f service-locust.yaml

also install ingress

  kubectl apply -f ingress-locust.yaml
  

- also do kubectl ingress
- once service and ingress is installed, you can see that the loadbalancer is created.
- you can see kubectl ingress , you can see 2 ingress that are presented.
![image](https://github.com/user-attachments/assets/f5291efb-d2e7-41d5-ad7f-013fb6c13673)

- go to EC2 and see in loadbalancer section, see your loadbalancer created or not.

![image](https://github.com/user-attachments/assets/e9e4fab0-ea2c-4547-a7d2-ab9269c0a66b)

- wait till the loadbalancer is installed.

![image](https://github.com/user-attachments/assets/e651532d-4606-4b37-99fc-5069aa02a7c5)

- you can see locus is available at the location

![image](https://github.com/user-attachments/assets/722ff79c-2226-4591-a1e2-d14f5a14565a)

![image](https://github.com/user-attachments/assets/2ab2ed20-0b3b-432e-ad52-f99a9dba18c4)
![image](https://github.com/user-attachments/assets/ffe68359-a048-439e-b448-4059c115eb36)


- you can see locus ui from the above endpoint.
- as we can see the second address for kubernetes container, the llm that we deployed
- you can use swagger to make request and endpoint documentation.

- but the host in lorax should be LLM endpoint.
![image](https://github.com/user-attachments/assets/1bc4e69b-7a07-40d0-88eb-bd8a7bf7b4b3)


- now kubernetes and LLM are connected in lorax to test the load.
- now the user that we created has 3 different tasks which the users randomnly select and make a call to this host
  and generate endpoint with different adapters.

 - we can mention the max no of users
![image](https://github.com/user-attachments/assets/65fef8db-f99f-4994-b7e2-d157aa31549e)

 - slowly ramp the total no of users, we ramp every 2 sec.

![image](https://github.com/user-attachments/assets/66533af3-2879-49c9-b618-f694bde13117)

 - we can see that there is locus pod available
 - lets look what HPA gives

![image](https://github.com/user-attachments/assets/0e6c16fd-8b02-4d71-bfda-ba62090d27e5)

 - to change the utilization , go to hpa.yaml
   ![image](https://github.com/user-attachments/assets/7dae3852-6b0b-4d3f-ad27-e624aba76f87)
 - now do kubectl apply to make the hpa changes to take effect.

 - this changes the new average cpu utilization value.

![image](https://github.com/user-attachments/assets/2cc820c7-39d8-4afb-824e-0648f267e69e)

![image](https://github.com/user-attachments/assets/1997a2d6-b597-4ca4-a9f9-d8ebb7907e01)

 - above means if cpu goes above this or decrease below, scale up or down the pods
 - if the cpu is above scale up , if it goes below scale down the pod.
 - scale up to max which is 2 , min is 1 pod.
 - now hpa is working nicely.
 - now bombard with lot of request and monitor how hpa is handle to this load.
 - monitor easily using "watch kubectl get hpa"
![image](https://github.com/user-attachments/assets/22d4181b-ffdb-4297-90b8-6a14940c3f31)

 - now , we can move forward and run our load testing.
 - we can see that the load test ,first create all these users and we have now customer support, sql_generator
   and wikisql , we have all these request we have made, we have the medium time that it takes.

![image](https://github.com/user-attachments/assets/cf5ba4e3-b5f6-46bb-96a2-62fcb03cf3d6)
![image](https://github.com/user-attachments/assets/d2cf93cf-5d0c-412e-b75b-d1082922bf5e)
![image](https://github.com/user-attachments/assets/62212e6f-300b-4206-a042-920698c3c0bd)

 - average time taken by the request
 - average response time of the user.
 - 100 users are concurrently bombarding the request.
 - thats how you can see response time is 33 sec for query which is pretty high
 - now, that we are seeing so much load being added, we go back to HPA , we can see
   target CPU is gone up to 50%  of the given value which is above 20% marks.
 - which means HPA scale POD up.

   ![image](https://github.com/user-attachments/assets/883d2cde-d4ff-42da-be9d-dd608a404b5e)

  ![image](https://github.com/user-attachments/assets/4bc8ec43-10f8-4dce-96a9-1953649e4be1)

  - now it needs to scale up the pod 
  - now see the pods again , to see HPA automatically created pod and pod is not still ready yet.
  - since time taken to 
      1)download the container,
      2)start the container
      3) load the module in GPU 

   - so 3 things are time taken to scale up the pod.
   - so currently this pod is getting ready.
![image](https://github.com/user-attachments/assets/8f00bcf6-94a7-4ccc-82dc-5fe566fb26c6)

   - you can see kubectl logs with the pod name 
![image](https://github.com/user-attachments/assets/1131b781-6171-4f38-b61a-57d27da6888b)
![image](https://github.com/user-attachments/assets/6a134da3-97f9-4f57-8e6d-98dfbeecb82e)


  - you can see webserver is starting up based on logs.
  - you can also watch on this
![image](https://github.com/user-attachments/assets/619daa80-6fc0-48c6-8c6b-838bab1847ed)
  - you can get status updates regularly .
![image](https://github.com/user-attachments/assets/d6525121-6cb3-4b63-83aa-ffee12b2d3ea)
  - you can go back to load testing, we now see that the response time started to decrease bit since
    we have another pod gets added.

![image](https://github.com/user-attachments/assets/e4a6112a-f04b-48a2-b472-c41100335977)

  - now, would be taking certain requests , which will be automatically be loadbalanced by loadbalancer.
  - so, the total requests per sec that would be handled , now we can see changed .
  - now the total requests per sec increased, because both the models are now able to take requests in total.
  - the 50% percentile time has decreased from 34 sec to 8 sec now.because there are now 2 containers
    that are ready to handle response.

request doubled
![image](https://github.com/user-attachments/assets/3ee38439-2548-4e85-a93a-798fdd501012)

response time comes to half for 50 percentile.
![image](https://github.com/user-attachments/assets/2f2b8a19-7e9a-4869-bddb-cdd5141f86d5)

  - in this way , we can see total request per sec is almost doubled and response time atleast for 50
    percentile come down to half.
  - in this way, scaling up has happened, once we stop this, after sometimes, HPA would see that
    2 containers are not required and automatically scale it down to  1 container.
  - in this way , we have done the load test, we know the metrics that we are looking for.

 ![image](https://github.com/user-attachments/assets/ed9a9ceb-e092-4a9f-9ca7-a955f1f872d5)

  - so , we can stop our load test and we can see the 
      1) current request per sec that we are abel to achieve
      2) at what given percentile time
      3) how many requests failed
      4) how many response failed
      5) how many request succeded
      6) what was the average min/max time took to get the response back.
      7) what is the 95% and 99% percentile time to get the response.

    - in this way, we can do extensive load testing on our given llm model, to see
      whether it fits it our needs and the SLA requirements that we want for the
      specific use case.
      
