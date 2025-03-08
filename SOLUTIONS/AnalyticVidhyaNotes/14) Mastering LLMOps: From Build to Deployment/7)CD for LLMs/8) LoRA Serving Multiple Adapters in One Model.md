LoRA Serving Multiple Adapters in One Model:
============================================

    - doing hands on Multi-LORA Prediction in which we would we have a docker container which can
      load a lot of adapters and do inference together.


    - so make sure logged in to sagemaker notebook.
    - inside DHS workshop folder.
    

Step 1:load project
==========================


![image](https://github.com/user-attachments/assets/75dcb0f2-90f6-4a55-8fa7-5cec65b907dd)

![image](https://github.com/user-attachments/assets/bbe93c8c-a3d7-4cad-a167-ee47320dbf9f)


/sage_maker/multi-lora folder


![image](https://github.com/user-attachments/assets/e26aa93b-0ee5-49fb-b957-b9e38a1d645a)


Step 1:multi-lora.ipynb
=================================

  ![image](https://github.com/user-attachments/assets/b7e36480-d1ca-4ade-8adb-de27d1b6c598)



Step 2 : setup credentials:
============================
![image](https://github.com/user-attachments/assets/1233735e-f392-4f91-be2e-957427dabd18)


role - get the role for accessing the aws services which only have permissions.


Step 3: setup tokens:
======================

![image](https://github.com/user-attachments/assets/3f4e64e5-c074-442c-a5a1-7fa5b675798b)

- hugging face to set up token.

output   
![image](https://github.com/user-attachments/assets/58996106-115b-4f48-a91f-bab8c5d3434d)
![image](https://github.com/user-attachments/assets/6fd1a655-1323-45d4-9a4e-a555c19ea242)

step 4:docker images container in ECR:
==========================================
 ![image](https://github.com/user-attachments/assets/4ad92894-465a-4686-bbf1-6ae46c0e54b5)
![image](https://github.com/user-attachments/assets/708714e2-b7ac-4c3b-98d2-ba4fa4155244)
![image](https://github.com/user-attachments/assets/961fd431-1775-434d-9aff-eb41c076e2fd)
![image](https://github.com/user-attachments/assets/a0ba032d-923a-40f0-a73c-a7ff9c62bd4e)
![image](https://github.com/user-attachments/assets/1d1ff16b-0c90-41f6-b8d6-ab1be401aba0)


After install 

![image](https://github.com/user-attachments/assets/7a90acd3-8594-4a9c-b61d-c409ea96e222)


![image](https://github.com/user-attachments/assets/7a272f51-5a19-48f2-b47b-a0ee22e0dd4f)

see the registry 
it is in ecr repository

![image](https://github.com/user-attachments/assets/e2889158-bd8b-4c2b-b98d-a4633e9a8f9e)

![image](https://github.com/user-attachments/assets/31518e88-bc5b-414e-b8df-79f258e64c72)


- now we have docker container installed in ECR and now we can pull from sagemaker.

Step 5: deploy sagemaker model:
=================================


![image](https://github.com/user-attachments/assets/d1de0ee8-9838-4d40-be68-b7fb7083c54b)

Step 6: deploy sagemaker model:
=================================

code 

![image](https://github.com/user-attachments/assets/3b9d70b0-198f-464c-a209-63ca8c683a09)

deployed model 
![image](https://github.com/user-attachments/assets/a9c491ea-0500-4be0-bfef-6eeb1d643a1a)

container logs
![image](https://github.com/user-attachments/assets/2ee655ed-982e-4376-9aea-bcb0e5549f4e)


response output completed running.
![image](https://github.com/user-attachments/assets/0274478e-3305-444e-b02c-5e7ed48a1eba)

cloud watch

![image](https://github.com/user-attachments/assets/bda3559d-9c85-4c5c-8240-6f63e02a84fb)

on click on the link
![image](https://github.com/user-attachments/assets/03624ef1-944c-430b-933a-28f2fd420f6d)

Step 7: multi-LORA Inference:
=================================


adapter specifically for named entity recognition.

![image](https://github.com/user-attachments/assets/d8db4d37-8de0-42a3-93e8-d233bbe70621)


hugging face named-entity model :

![image](https://github.com/user-attachments/assets/af279090-90ed-4950-9974-1b2f498d4521)

helper function getRequestBody


![image](https://github.com/user-attachments/assets/9e615143-9fac-4e19-9b18-1a0232a7648c)

output 
![image](https://github.com/user-attachments/assets/3ad92a38-fa02-4a8e-a7d5-c0ad69944fd6)

step 8 : destroy:
===========================


- finally delete the endpoint configuration and endpoint as well.
- so we wont get charged for any more hardware resources because hardware itself destroyed.

![image](https://github.com/user-attachments/assets/c56b2910-a5ca-4ed6-84b5-0b2f8e042ebe)
