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



  


 
