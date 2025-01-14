Prompt Engineering with ChatGPT API:
====================================


1.Setup env:
============

  - ChatCompletionAPI of openAPI enables developers to send request(prompt) and receives responses.
  

    ![image](https://github.com/user-attachments/assets/cde56cf6-a8e2-4e02-a86a-7cb0e8fc1a24)

    
  - it needs 2 main parameters

1.model :
==========

 - language model such as GPT-3.5 or GPT-4

2.messages:
============
![image](https://github.com/user-attachments/assets/dfc79426-6867-4a27-b16a-d3f5fae26f9b)

  - message can have 2 properties
    1) role  - role can take values 'system','user' or 'assistant'
    2) content - text of the message from the role.

Different Roles:
=================

1.user role:
============
  ![image](https://github.com/user-attachments/assets/f2115735-6d85-41fd-8676-2ebcd1a7fcd9)
  
     - it can take input task/query provided by the user.
  
 
![image](https://github.com/user-attachments/assets/f69d6ade-604c-4e78-98e4-da93c35152d0)
             
2.system role:
==============
  - provide system level instructions, guiding your model behaviour throughout the conversation.
  - for e.g you can say the system role 'that you are an assistant that speaks like shakespeare'
  - try the above prompt with user and system role
  - first user role

   <p><details><summary>basic user role.</summary>

![image](https://github.com/user-attachments/assets/91447672-b672-43bd-baac-6e3b78d0ea0f)
  </details></p> 


<p><details><summary>limit 500 words</summary>
     limit to 500 words

![image](https://github.com/user-attachments/assets/28bcc3dd-1d34-4726-9757-e62622462e99)

    - above looks very technical
</details></p> 

<p><details><summary>this time mention like beginner</summary>
    - this time mention like beginner

![image](https://github.com/user-attachments/assets/fb652746-6536-4ded-b7b4-9faf0653c40c)
![image](https://github.com/user-attachments/assets/3564e827-6b86-43bb-93b6-3bdc4e627de7)

       - as you can see it broken down in to different section.
 </details></p> 

<p><details><summary>write blog post - Add Sections</summary>
    - so that my article more frequently in searches


![image](https://github.com/user-attachments/assets/952b3027-8193-4612-8f1f-9edea324e940)
![image](https://github.com/user-attachments/assets/7aa5a5af-2b04-4a6b-8653-c4d17d6f26b8)

       - as you can see it broken down in to different section.
       - looks like can be published.
       - above can be published, discoverable , simple to follow.
       - however it needs to follow some structure where search engine can understand
 </details></p> 


 <p><details><summary>SEO Friendly</summary>
    - in prompt mention seo that is frequently in search result.

![image](https://github.com/user-attachments/assets/0c2f48df-0d91-4850-8752-5d481db07590)
![image](https://github.com/user-attachments/assets/b69fbf00-3ce7-4810-ba38-de22eee1a670)
![image](https://github.com/user-attachments/assets/fe85259e-45c1-41f1-bb13-a7a8a24c1a95)

       - as you can see it broken down in to different section.
     
 </details></p> 


<p><details><summary>10 FAQ</summary>
    - faq questions in results.

![image](https://github.com/user-attachments/assets/5856cddb-31a0-47f8-a24a-5232ea23e5e2)



       - as you can see it broken down in to different section.
 </details></p> 
    
