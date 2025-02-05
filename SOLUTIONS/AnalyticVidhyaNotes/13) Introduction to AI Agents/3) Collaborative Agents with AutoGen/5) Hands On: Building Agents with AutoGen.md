![image](https://github.com/user-attachments/assets/99168122-5bb2-4ce5-a58e-007a495b16bc)Hands On: Building Agents with AutoGen:
========================================

  - First Agent in Autogen

    ![image](https://github.com/user-attachments/assets/1e8fec98-de2d-4ea3-9235-917ae30115d4)



  Task: to send something to agent:First Agent in Autogen
  ===========================================================

  %matplotlib inline
  from autogen import AssitantAgent,UserProxyAgent,config_list_from_json
  from autogen.coding import LocalCommandLineCodeExecutor
  config_list = configlist_from_json(env_or_file="OAI_CONFIG_LIST")

  ![image](https://github.com/user-attachments/assets/001ffe46-c814-4da8-8749-ceeb3aa32cbf)


Step1:Setup First Agent:
==========================

  load config

  ![image](https://github.com/user-attachments/assets/1be890d8-04eb-4c55-b2ce-5ab2fd5b7b17)


Step2:set Folder to store intermediatory artifacts:
=====================================================

![image](https://github.com/user-attachments/assets/84ed379c-0ea4-4540-94f7-3f0980f8ce3f)


user proxy agent:
=================

   allow to execute code 

   ![image](https://github.com/user-attachments/assets/d97eaa72-5e2c-49ed-96b7-bbb07192401e)


Step3:initiate chat between userproxy and assistant:
=====================================================

  - give a task to user_proxy.

![image](https://github.com/user-attachments/assets/5eb34495-852c-4d87-b981-2a073b555f42)
![image](https://github.com/user-attachments/assets/af9c4cc2-7dd9-48ae-8c0b-843b2005e573)
![image](https://github.com/user-attachments/assets/cfd1a01d-5809-4376-ac83-106127522869)

  - you can inspect the execution of userproxy
  - above code does not store image any where

Step4:store image:
===================


user_proxy.initate_chat(assistant, message="plot  a chart of any stock price and compare to openAI's and store it as stockprice.jpg")
![image](https://github.com/user-attachments/assets/ccfd82bd-17f6-47f5-b38c-ac650f94550d)

![image](https://github.com/user-attachments/assets/91c3b4a2-71e0-470e-9e39-b85eb9e662f1)

check the image saved locally

![image](https://github.com/user-attachments/assets/aeea963a-831d-4f8d-b5e7-31439708ef5b)

![image](https://github.com/user-attachments/assets/17752a28-64ae-4bc2-8c59-08e7c8bcc41a)


Step5:check multiple complex task:
==================================


 - pull couple of archive from specific topic and summarize them into a report about a topic
 - let see how well model perform.
 - actually write a method called executeAgent which contain a prompt with that prompt you can do multiple task.

![image](https://github.com/user-attachments/assets/d4d143be-0efd-4121-91d3-6a7fbe76d390)

![image](https://github.com/user-attachments/assets/7c8f29e0-5946-4686-b037-3ff2c34da392)


- report generated
![image](https://github.com/user-attachments/assets/3e64f028-561c-4d74-a99f-12ccd0e28ecf)
