Write Clear and Specific Instructions:
=======================================
![image](https://github.com/user-attachments/assets/cbc36d02-7de2-4d27-8011-5fbf60e7e651)

   - previously we see we are looking at the customer support ticket.
   - what we want to do is classify the tickets.
   - in order to do that lets says we start with the prompt classify the support ticket then see the outcome.
   - you can see it return the response "customer support ticket can be classified as technical issue"

![image](https://github.com/user-attachments/assets/95e08320-4e4e-4e4e-ba84-b4ed9eb68592)
     
   - run the second ticket 
![image](https://github.com/user-attachments/assets/c00c0b77-ca04-4671-b9f1-6b8c1e32090a)
   - it says "inability to access the specific features"
   - now what would happen if million of tickets, there will be so many classes ends up defeating the purpose.
   - all the likelihood you  need the classification , because there are different people who can deal with these
     tickets based on this classification. basically want to be classified in 2 or 3 different tickets.
   - what we do for that is write the specific instruction to the model so that it can do exactly that.
   - so what i'm doing is that instead of saying classify these as default prompts , i am saying
     classify the support tickets into broad categories
     1) technical issues 
     2) billing enquiries
     3) product feedback.
   - so depending upon the usecase there could be few more classes, but it should suffice what i am trying to do.

first support ticket:
=====================

   - now run the prompt
![image](https://github.com/user-attachments/assets/4565bfa6-678c-479b-be16-d0edb5182bf8)
   - it says technical issues for support ticket.

second support ticket:
======================   

![image](https://github.com/user-attachments/assets/4223c19e-e965-4354-a162-1ce4d7316835)

    - as you can see now it returns consistent category "technical issues" for the second ticket as well.

Summary:
========

    - by giving a speicific prompt , i am able to categorize these in to specific functions and then i can forward
      these tickets as needed.

Next step:
==========

![image](https://github.com/user-attachments/assets/323db597-801d-42d5-8224-d91ea73f466f)
![image](https://github.com/user-attachments/assets/1322de8a-a079-42aa-beb7-3ec5338120b2)

- go one step further
- generate a response for the customer support ticket related to **user experiencing issues** with accessing their account
- it is adding few trouble shooting steps.
- it is not clear.
- as a company want to re-assure customer that data is secure with us.
- so this time make prompt very specific.
![image](https://github.com/user-attachments/assets/cd815765-ce84-4ffc-9930-f9891d979ec6)
- here you can see it provides all the steps for customer as well as re-assurance that data is secure.

summary:
=========

  - first step is make sure as specific as possible , so that all the context which you have
    gets transferred , outcome from model is what you exactly needed.
