Prompt Engineering Using Open Source LLMs:
===========================================


Step 1:
=======

  ![image](https://github.com/user-attachments/assets/a939dfa6-b11d-4765-aae1-644931de1873)

    
  - loading llama2 to our local.
  - load autokenizer and torch.
  - load the tokenizer , which is essentially a pre-trained tokenizer 


Step 2:
========
![image](https://github.com/user-attachments/assets/626704e7-08be-4879-bbf1-096c3082f74a)

    - run tokenizer
    - which is pre-trained tokenizer which contains all token about which the training has been done before.
    -

Step 3:
=======

![image](https://github.com/user-attachments/assets/4dd958e6-707f-4159-8349-f60d89778971)

    - download pipeline 
    - pipeline is useful for enabling us text generation in llama2.
    - requires roughly 12gb of ram.
    - once this is done then start using this model for prompt and getting the response from there.

Summary:
========

     - download entire model in local.
     - so the advantages of this download in local is 
     - now anything which we do is happening in our local env.
     - we are not passing on our data to external world.
     - what ever we generate will stays on our environment.
![image](https://github.com/user-attachments/assets/81fb69f5-1307-42d5-93f2-4fa09f02bb85)

![image](https://github.com/user-attachments/assets/0bb6f762-f4e2-4808-af4e-c8e5d8d83a3c)

Step 4:
========

  - define a function to accept prompt.
  - max-length is max output tokens that we want from our model.
 

Prompting llam2:
===================
![image](https://github.com/user-attachments/assets/5d58893f-5224-47c6-9968-95c27c975017)

    - model has been trained using specific template.
    - it has special token which starts and ends here.
    - we need to provide instructions between <INST>
      and in between we have system prompt.
    - user message goes in <user_message>


Important:
===========

  - this is the template in which the model has been trained and all our prompts to the
     model should go in the same template.
  - this is something you have to look at , everytime you do a different model , you have to make sure that
    the **prompting is in the template which is provided along with the model**.
![image](https://github.com/user-attachments/assets/dcd31275-cf26-467e-a4b3-60b2c751bd77)
    
   - input prompt : "suggest series like money heist"
     ![image](https://github.com/user-attachments/assets/33463892-46c3-4adb-a452-cddef3e671e5)


<p><details><summary>1.Case Study - Machine Translation on Product Reviews Data</summary>

Case study:
==========================================================
![image](https://github.com/user-attachments/assets/a83b3e98-6f59-47f2-82da-8c210d7e6e89)

    - whether llama2 can do conversion french to english.
    - as you can see it produces correct output


</details></p>


<p><details><summary>2.Case Study - Generic Translator - Any language to english language</summary>

![image](https://github.com/user-attachments/assets/5350e7ab-4b5e-49ba-8675-9a69e6b034ac)
![image](https://github.com/user-attachments/assets/d74267c9-68b4-49b8-87b1-8da78875523e)

 - able to translate 1 to english ,2  ,3 and reviews.
 - simple prompt we create a universal translator.
 - by giving the input prompt without specifying what language it is , it is able to convert by identifying the language.

</details></p>

<p><details><summary>3.Case Study - Generic Translator - other than english output</summary>

![image](https://github.com/user-attachments/assets/69bee687-6e00-4d4a-9f68-53917995e23d)

![image](https://github.com/user-attachments/assets/d35da326-166e-4908-96b6-c244c827f515)

- spanish, hindi output

</details></p>
