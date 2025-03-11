Hands On - Kubernetes Installation:
======================================


    - lets start first by installing kubernetes cluster on AWS.
    - on AWS we have specific services called EKS(Elastic kubernetes service) which is a flavor of kubernetes in AWS.
    - why EKS specifically ?
    - because it gives us additional advantage and it uses a lot of AWS features inside and enhance the capabilities
      of kubernetes and makes it more suitable for AWS.
    - and now we will start by first going through our notebooks.
    - the _underscore EKS Folder and we will start by doing the setup.


Step 1-Setup:
==================

  - now in setup, we will first go and install kubectl.
  - kubectl is a command line tool, which can used to connect to our kubernetes cluster.
  - first install kubectl
  - for that open new tab, like open notebook, open new terminal.
  - make sure we have in right folder /dhs-workshop/notbook/4_eks/setup.

![image](https://github.com/user-attachments/assets/33cce990-d441-4adb-9dd6-a196e3fd240d)


clusters:
=========

![image](https://github.com/user-attachments/assets/140fa799-53b5-4140-8034-66d480193c8e)


 to create nodes in multiple zones.


these configuration we can install kubernetes.


 install:
 =========

  - we can start the cluster creation process by running the fifth file(5_create_cluster.sh)

  ![image](https://github.com/user-attachments/assets/3a28c238-61a2-4789-8bac-762d117161eb)
![image](https://github.com/user-attachments/assets/811ed259-bb01-4619-9e2f-0e19470f33a2)

![image](https://github.com/user-attachments/assets/cc2bec5f-8784-487d-bffd-98302356f825)

  - this fifth file as you can see just runs the eks_ctl create cluster and specify.
  - so we go ahaead and install bash create cluster.sh.

Summary of steps flow:
========================
  - now you can see cluster creation process started , this starts with send the cloudformation template
    to the cloudformation service to create the whole kubernetes cluster and assign some node to it.
    it takes 10-15 min time.
![image](https://github.com/user-attachments/assets/3652c0ac-3902-4959-8dda-45695db46a55)
![image](https://github.com/user-attachments/assets/041637c7-7087-48f4-9189-4921cd7006c3)
![image](https://github.com/user-attachments/assets/f5f13cb0-2e73-431b-9ad8-f9907acd2ec5)
![image](https://github.com/user-attachments/assets/cb0ba5b9-6b87-448c-9a19-9c50229eb96b)
![image](https://github.com/user-attachments/assets/48878c90-f529-4ad2-8895-330dd810ad19)

  - you can see stack created.
  - click on to see the resources to be created for this kubernetes cluster.
  - what are the different events that tooks place? apart from creating NAT gateways, different route tables
    as well as VPC with all the subnets that is being created.
  - we also see nodes group that is added to this.
![image](https://github.com/user-attachments/assets/0ac22bd0-dba5-4eba-8fe1-801190739688)
![image](https://github.com/user-attachments/assets/bc068781-de43-4785-8955-1090ada340e7)

  - i have 16 , one can request to increase to 16

Autoscalling group:
===================

 - Now as we can see that we are using EKS(Elastic Kubernetes Serice) the way it increases and decreases the
   node using something called **Autoscalling Groups**
 - Now, Automatic scaling up and down is a feature in AWS by the name of **autoscaling group**.
 - and so we can see how using EKS instead of **installing kubernetes on our own** , we can simply leverage the
   feature of AWS directly from the kubernetes console.
![image](https://github.com/user-attachments/assets/f58fd16c-fb52-47b6-8710-cb7c569af7ad)
![image](https://github.com/user-attachments/assets/034b1c5b-4212-462f-85cf-dc78a863bdfc)

 - so, once we create the node group , automatically created and this take care of scaling nodes up and down
   whenever we tell it or kubernetes cluster will tell it accordingly.

connect to cluster:
===================

  - create a namespace called prod, set the namespace as prod
  - then we will check how many nodes are available using the EKctl command.
  - also check we have access to kubenetes cluster
  - go to terminal enter bash_6_connect_to_cluster.sh to connect to cluster.

![image](https://github.com/user-attachments/assets/7027bafd-c75f-4baf-a06f-2f3102293c31)

  - so as we can see the kubernetes command also working fine , which was to check the access
    by running something called kubectl can -i .
![image](https://github.com/user-attachments/assets/5f66e726-0c52-4937-9232-fccefe04e5cf)

  - so can i in the prod namespace , create pod and the answer to this is yes.
  - we are now connected to kubernetes.
    


