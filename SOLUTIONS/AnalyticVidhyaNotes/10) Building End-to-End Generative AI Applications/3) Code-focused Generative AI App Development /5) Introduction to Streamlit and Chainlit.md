Introduction to Streamlit and Chainlit:
========================================


  - brief introduction of streamlit and chainlit.


Stream lit:
===========

  - opensource python framework which helps in turning python script to sharable web application.
  - advantage is you just need to code in python, it create beautiful user interface.

![image](https://github.com/user-attachments/assets/34b3ed12-2422-47dc-9c34-98a1430b3548)


chainlit:
==========

![image](https://github.com/user-attachments/assets/510a8aac-877e-4afb-a1a7-74b2d15bff6d)

![image](https://github.com/user-attachments/assets/8a8edfec-31ab-4897-9555-1cca16b5692b)

 - opensource python framework similar to streamlit.
 - focus on building production ready conversational AI.

NgrOK:
======

![image](https://github.com/user-attachments/assets/9c1d6390-31d5-4f4f-9d7d-d02b72b657c1)

https://dashboard.ngrok.com/

- when we deploy app in the colab, it is not very easy to access the userinterface through colab.
- because colab is a notebook, you cannot access the google cloud server on which colab is running.
- this is where you require a application ngrok.
- ngrok to create a tunnel to your application, so that you can access from public url.
- remember to get the ngrok key.
- you just need to go to https://dashboard.ngrok.com/ gets started with auth_token , completely free.
- remember to store the token in yaml.

why we need ngrok:
===================
![image](https://github.com/user-attachments/assets/98d59196-fa17-4bde-bbf9-7b4940273953)

  - google colab runs on a server on google cloud, we cant access that.
  - when we deploy app on colab, we are not actually run on collab, we actually run on google cloud server on which colab is deploying.
  - thats why when we deploy each ui based application on google colab, which is running on google cloud server, which we
    cannot access directly.
  - that is where we will use **ngrok tunnel** to access it from public url , so that you can get the full user interface and
    interact with the deployed application.
