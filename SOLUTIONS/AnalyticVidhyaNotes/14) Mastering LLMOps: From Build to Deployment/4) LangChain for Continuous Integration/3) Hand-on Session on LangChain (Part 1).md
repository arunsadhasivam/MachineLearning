![image](https://github.com/user-attachments/assets/7a3a225d-f6ea-4279-84bf-dbe8fe9adbed)
Hand-on Session on LangChain (Part 1):
=======================================


  - hands on go through langchain
  - go to aws sagemaker and click on domain.
![image](https://github.com/user-attachments/assets/32dee79d-b263-435f-a166-fdd6db455ddf)


Start sagemaker:
================
  - click on user profile and 
  - open up amazon studio.
  - click on **jupyter lab**.
![image](https://github.com/user-attachments/assets/e07cc84d-446d-4275-b468-179f7b4def0d)

  - click on **run**
![image](https://github.com/user-attachments/assets/4310918b-b9eb-4cf1-8838-108926b45984)

  - click on **Run space** make sure it is ml.t3.large.
![image](https://github.com/user-attachments/assets/ec009514-736a-4544-8429-7d774deefd8f)

  - click on openJupyterlab



step 1:setup requirements.txt:
=================================


do pip install requirements.txt to install all dependencies.

![image](https://github.com/user-attachments/assets/69edcc2c-6dc8-410e-9a61-a4fc2f1096ab)
![image](https://github.com/user-attachments/assets/9fb20f24-eb15-4378-b886-f3f3efa44f13)

Step 2: set env:
================


![image](https://github.com/user-attachments/assets/880e2647-d050-4151-b4dd-4100a634d105)

![image](https://github.com/user-attachments/assets/7ab95430-33b9-441f-b1aa-6752ee93f99e)

load api key

Step3: code:
=============

![image](https://github.com/user-attachments/assets/dcca2a18-4c0a-4c05-af46-fe9b38162aae)

- this class would be used to structure final prompt.
- now, the library automatically recognizes new classes such as system messages - human message
- this makes it really powerful to change these prompts at run time and be compatible with multiple llm at the
  same time.

Step 4:Message holder
=====================

![image](https://github.com/user-attachments/assets/b1e128fc-8749-4bef-bcbb-21d9cdc42773)

 - chatprompt created.
 - it also has human message.
