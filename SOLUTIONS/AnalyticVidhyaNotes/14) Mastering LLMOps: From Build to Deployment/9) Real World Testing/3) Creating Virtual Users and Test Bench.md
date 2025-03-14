Creating Virtual Users and Test Bench:
=======================================

- in this lesson, we would be using locus, which is a framework for doing load testing, written in python,
  using locus we create a virtual user which will behave as good as real user with different set of input
  that it will give it to final application.
- the application that we are going to test is the LLM  Module that is deployed in kubernetes with multiple
  adapters in it.


![image](https://github.com/user-attachments/assets/285cb2f6-9d5f-42e5-8b1a-e3bc8aa2ec0e)

- go the notebooks folder > load_testing folder > **locus_setup**.ipynb
- so, we would be creating a docker container for your locus testing . this container we can also
  run somewhere else. but deploy the container in kubernetes itself.
- this container would then expose the UI and then using the UI we would be testing the different requests that we made
  to the lorax container , which is also deployed in kubernetes.
- we have to create a workbench , first import http user from locus.
- we would create a class **quickStartUser** and this will represent one virtual user.
- then expose a variable as host

quick start
![image](https://github.com/user-attachments/assets/1928ef7c-75ad-4b43-88dd-d8660f659a75)

http post
![image](https://github.com/user-attachments/assets/3aad44ec-a989-4d0a-95c5-8a8ebad09c43)

cusotmer support 
![image](https://github.com/user-attachments/assets/6cec023a-16c1-40c1-8871-23570ec446a9)

check balance
![image](https://github.com/user-attachments/assets/c887c325-ecfa-43b9-94e2-af2440593433)


code generator
![image](https://github.com/user-attachments/assets/4d34731b-c2ce-4579-93a9-21b77d89aa19)


- third adapter we would be using would be predibase magic coder, which would be able to write code
  in any language and in the same way we would be using to test our work bench.

- so finally, this is what the user would do , after every call it would wait 1-2 seconds and then
  randomly choose another type of task against the server.

- so, now lets run the file.
- it just creates the same file as a python file outside locus.py
![image](https://github.com/user-attachments/assets/bc5fccb4-9e16-4abd-93be-3a18213d551a)



  sagemaker studio image build:
  ================================
![image](https://github.com/user-attachments/assets/b41529e7-b4b6-429b-bddf-2346f03d4b52)

    - now we would be creating docker container for which install sagemaker studio build
    - by using this already creating a docker container, we
    - then using it again to create this new docker container
![image](https://github.com/user-attachments/assets/ae74de35-9745-43cc-8988-e4d584b1cc99)

    - now , we could calling sagemaker docker build with docker file  and create repository called locus


Docker:
=======
![image](https://github.com/user-attachments/assets/cc88e256-63af-4782-94a8-e91e33ed4075)

  - lets have look at what docker file looks like
  - copy the locus.py file that we created
  - simply run on port 8080
  - simply run the cell
![image](https://github.com/user-attachments/assets/cba2e217-a418-450a-8f82-9971b5f2af2e)
  - above cell will do
      1) code build project ,
      2) code build will create a docker container
      3) Also create the repository for us
      4) will upload the container to that particular repository.

   - we can see repository named locus is created, we can go to aws > top search > container registry
   - we can see locus repository created.
   - still build , if we want to look what is the status, you can go to codebuild > you can see 

![image](https://github.com/user-attachments/assets/a105a42d-3ae6-44cb-9004-66562c393b3b)
    - you can tail the log , in logs we can see 
![image](https://github.com/user-attachments/assets/0947633d-406b-4c5f-8d37-57ff81889836)

          1)docker file being pulled
          2)created
          3) finally pushed to given ECR image.

     - Also check in ECR 
![image](https://github.com/user-attachments/assets/0c152d0d-5b8b-4ed4-911d-27631b6d4cdc)
![image](https://github.com/user-attachments/assets/045be7a1-3c49-488f-acb3-b17402cc6d26)

      - above is the container image url that we want
      - once that is done, we have go to deployment locus and specify the image name over here

![image](https://github.com/user-attachments/assets/95d9adca-4d6e-4db9-8191-68d1ff453602)
       - save this file deployment-locus.yaml
       - using the terminal and this make sure we are in the right folder 
       - run kuectl 
       - it finally creates a deployment
       - kubectl get pod , creates a deployment and this server is running
![image](https://github.com/user-attachments/assets/366f02f4-7cac-4723-9478-f89417f8ff5f)
        - this server is running , next chapter we use it for load_testing.
