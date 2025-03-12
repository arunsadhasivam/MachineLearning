Hands-on Session Autoscaling with HPA:
========================================
![image](https://github.com/user-attachments/assets/03dd6e4f-5c9b-4e35-ab87-e50cbae67e38)


   - now we have an LLM deployed on kubernetes as deployment, where we specifically mention replicas to be two.
   - which simply install 2 replica sets as we see in the deployment.yaml.
   - we manually mention the replica as 2.
   - if you want to automatically scale up and down , the no. of PODs in the kubernetes cluster , we use horizondal POD autoscaler.
   - so, in this video, we would be working with HPA . to do that , we will simply have to go to underscore EKS Folder under setup 9.1

![image](https://github.com/user-attachments/assets/40ae61ec-b6a8-4cda-ab2a-a0ea74213041)
![image](https://github.com/user-attachments/assets/e0dc7e5a-6fa6-415d-a965-2285bd6debc0)

   - install metric server API, and then see metrics server API is correctly working or not.
   - start a new terminal , run bash script . make sure inside correct folder.
   - setup HPA.sh
   - we can see metrics server is installed under the status of metrics service.
![image](https://github.com/user-attachments/assets/51e8f999-750c-4770-95ec-1ec954199b14)

   - see now the metric server still starting up.
   - to be able to continously monitor use watch command on top.

![image](https://github.com/user-attachments/assets/341a2d18-d82f-4574-ad03-f5a1d0357c58)
logs
![image](https://github.com/user-attachments/assets/b2cef41c-84d2-4a98-b001-c72c3e1fda6d)

   - now we can finally see metrics server is up and running.
   - so this metrics servers, takes all CPU RAM utilization between all the nodes and all the PODs
     and then makes it available as API , which HPA or horizondal autoscaler is able to take.


EKS Artifact folder:
=====================

- now go to EKS Artifact folder, and see the horizondal POD autoscaler that we would create for our lorax application.
- so the kind is horizondal POD Autoscaler and we will name it as lorax HPA.
- The specification would be to scale the deployment, which we named as lorax deployment in our deployment.yaml
- you can also check by running below kubectl get deployment command.
       kubectl get deployment
![image](https://github.com/user-attachments/assets/d77e1715-1ae6-42b0-b5c7-e0c37b6a26cd)

lorax deployment.
![image](https://github.com/user-attachments/assets/0b6675fe-a234-49d9-abd6-05e1a78134ac)

- and we can see deployment is called lorax deployment 
- lorax deployment has 2 as minimum no of replicas
- so we want to scale the lorax deployment with minimum as 2 and maximum as 2.
- the metric to scale these things up and down, is to look up the CPU utilization, and see the average
  utilization across all PODs of this deployment to be 80%
- if the average utlization of CPU is above 80% then scaling would happen.
- if it goes below 80% then scale down   would happen.

![image](https://github.com/user-attachments/assets/207d3e28-0954-455d-ba74-a2d3ba2e325e)

- in this way , HPA would be automatically scale up and down with a min replica of 1 and max of 2.
- so lets now apply this, we will go to the artifacts folder and applly this file with command
      kubectl apply -f hpa.yaml

  ![image](https://github.com/user-attachments/assets/74e94b10-76b8-4ac0-a87d-8c4bfe8173ea)

- and this horizondal POD autoscaler is created.
- to know the status

    kubectl get hpa
- we can also watch

  ![image](https://github.com/user-attachments/assets/6f00ea9d-1974-4bc9-ba35-8ff1b558243c)
- you can continuously watch as well.
![image](https://github.com/user-attachments/assets/702ab16a-a03a-4fc7-8806-1027b40e50f4)

- you can see HPA initially as target unknown, currently able to find average CPU utilization of all POD
- now the target is 20% , min pod is 1 and max is 2.
![image](https://github.com/user-attachments/assets/7d2e9da8-9e5b-448d-9b84-29f3cbf8ed4a)

- currently the no. of replicas are 2 and because the average utilization is below 80% HPA will quickly
  know the no. of PODs needed are not 2 and 1 will also be enough.
- so, it automatically scale down the deployment , wait for sometime HPA in action and scaling down the POD
  for us.
- and we can see that after certain cool down period, when the cool down period is over HPA evaluates the
  status of the POD and sees the target Utilization was under utlized and so it removed a POD automatically.
![image](https://github.com/user-attachments/assets/19e565ab-ffb5-422e-b912-3da436eaf0f3)

- now no of POD is 1, you can see using command
   kubectl describe HPA

to see the description of what happened
![image](https://github.com/user-attachments/assets/09e7e3bc-37fd-439d-a6fc-fd97f1a4f6d6)

 
- so we saw the new size is 1, the reason was metrics is below the target. so the scaling down happened.
- so the same way scaling up happens when target increases
- this is what horizondal POD autoscaling.
- now , in the next section we will see and work on load testing and see automatic scale up in action.
- it is horizondal POD autoscaler on high level.
