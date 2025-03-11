Hands On - Kubernetes Setup:
============================

  - now that we have done the connection part to kubernetes, lets says installating the **load balancer**
    and the different **containers or pods that we want for our services**.


1.set up load balancer controller:
===================================

  - file name : 7_setup_lBC_permission.sh - set up load balancer controller and this is going to setup
    the permissions that are required that the load balancer controller will take.


![image](https://github.com/user-attachments/assets/9c82c657-b281-4008-b069-f58acc7f98fa)


 - As we see the EKS Enhances the capabilities of kubernetes inside AWS by leveraging a lot of AWS
   services which are already present.
 - instead of using load balancer inside the kubernetes cluster, we can use the AWS load balancers
   and so to be able to do that seamlessly, we have one of the controller we can install in kubernetes and this
   controller will automatically take care of creating load balancers in AWS and attaching it to POD inside kubernetes.
 ![image](https://github.com/user-attachments/assets/5d67726d-3c94-4fff-9b32-b48c5e63168c)

- so, this controller is what we are installing above.
- we start by giving the cluster name
- account id
- certificate manager takes care of installing certificates between kubernetes resources.
- policy - giving it policy name
- finally create service_account -> service account are basically giving pods a access to different
  AWS resources using roles.
- policy that is created over here , would be created into a role and that role would be attached into kubernetes
  by the name of AWS load balancer controller.
- and with this name, the ALB controller deployed inside the kubernetes would be able to access and create load balancers
  on behalf whenever we need to connect to a pod to a load balancer.
- and finally , we do a kubectl apply to install this certificate manager as well.
- so, lets run this command.
- a policy is created, creating another cloudformation stack to create the necessary role with the available permissions.

  ![image](https://github.com/user-attachments/assets/5db87f7f-c158-4b51-8042-bd4296d2c38b)
![image](https://github.com/user-attachments/assets/32fb755c-9852-4446-ab2f-3453015a7442)

- and now we can see the installation is complete
- the cert manager is installed.
- we can see also the cloud formation stack was created.

![image](https://github.com/user-attachments/assets/b9693078-b481-4fb6-8b8e-17aa3448efa8)
![image](https://github.com/user-attachments/assets/bbe33b0a-0718-408c-b33d-6eaa58c03225)

   
 - stack created a role , this role has policy permissions.

deployment of all resources done
=================================

![image](https://github.com/user-attachments/assets/0e427337-c3dc-49a7-88c8-030335427a4e)

  - after deployment of all resource done
  - we can now go ahead and start the deployment to kubernetes of our application.
