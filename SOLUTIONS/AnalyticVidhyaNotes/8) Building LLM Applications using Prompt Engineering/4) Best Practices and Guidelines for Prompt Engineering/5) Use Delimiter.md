Use Delimiter:
==============

  - delimiter are simply special symbols which can help you in understanding the text in a better manner.
  - understand the information in a better manner.
  - some of the common delimiters are comma, and lot of other ones.
  - when you give any input by adding these delimiter you can help structure the input better for the model to understand.
  - for e.g let say instead of giving each ticket separately i created a list where i have the tickets in hand.
  - i pass this as customer support ticket. it has list of all the tickets which are available and now what i want is
    the model should classify this in to the categories.
![image](https://github.com/user-attachments/assets/a876e7ed-826c-44f1-8a14-bff474d2e66a)

  - i write this prompt and send this along to the model .
  - what it does is "when i look at the output of the model" it just classifies everything in to an single category.
  - the model was not able to understand that there are different categories which are available or ticket which are available.
  - in order to do this in a better manner , what you do is you say that **"each of these tickets are now in a delimiter function"**
  - my tickets starts with  a delimiter and again next ticket starts with a **delimiter and ends with a delimiter**.
  - what this will do is it help the model to understand that they are multiple queries or multiple tickets and i want
    a classification for each of the ticket.
![image](https://github.com/user-attachments/assets/2c5f8e22-8a12-4717-8cc1-788618720fab)
![image](https://github.com/user-attachments/assets/cf999bf4-3d74-419d-b40c-47e1e96d55ee)
  - as you can see it is able to say that 1st support ticket is **technical issue** and second is **billing inquiry**.
  - this is very helpful when you are dealing with rows, columns, tables you can use this. but you cant do this by copying it
    you might need to iterate over it.
  - instead of writing in a single prompt, essentially using a loop.
![image](https://github.com/user-attachments/assets/9945e6ae-1433-43f4-a9c6-21e81a4a99c7)

  - iterate over the customer_support_tickets array and use this prompt and just running over it.
![image](https://github.com/user-attachments/assets/b526f63c-837f-4a9b-880c-c2ccc99c931c)

  - in that case it just return 2 **cases technical issues and billing inquiry**

SUmmary:
========

  - so what we are able to do is give these tickets a delimiter, and model able to understand lot better.
