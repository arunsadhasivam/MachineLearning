Why and What is Finetuning LLMs?
=================================


  - ChatGPT and its capabilities.
  - Fine TUning is the process of adapting the pre-trained general purpose module further.


    ![image](https://github.com/user-attachments/assets/23c21fe5-1002-4fd3-997b-da0137712375)

   - Think of General purpose pre-trained model as a general purpose lawyer.
   - if you go with the requirement of the "patenting and copyright" if you go to them
     general lawyer he can give only general instructions. however if you go to the
     specialized in intellectual property domain they can better guide you with things
     like what actually count as invention for patenting, whereas patenting in single country or multiple
   - in similar way the conventional paradigm in deep learning domain is to first pre-train a model on a
     webscale generic data to get the **base generic model** then followed by fine tuning on specific
     downstream tasks to get the specialized model which achieves the business outcomes.
   - fine tuning enables change in model behaviour to provide the consistant outputs to better control
     tone and style of the output.
   - main goal on the fine tuning is to align the model to be helpfull in performing tasks that we are
     interested in , by being harmless and honest.


Why Fine TUning:
================

![image](https://github.com/user-attachments/assets/17a4d8d9-f8ec-4fa6-8984-af2b018c2565)

   - As already discussed fine tuning creates a specialized model capable of outputting consistent response 
       1) have domain expertise - led to less halunications.
       2) better consistency - led to best performance.

    
   - As example below , base model of llama index, asked top5 places to visit in india.
     it does not understand the question to answer user expectations.
   - so if you start generating more questions like what are top5 places in europe and so on.
   - it can answer well because it gone through the data from many website.
   - whereas finetuning model can correctly provide the expected answer where 5 indian places
     thereby fulfill user intent.
   - Therefore 
      1) fine tuning process led to change in behaviour of the model to better understand and
         follow the instructions or another way.
      2) to elicit the expected behaviour from the pre-trained general purpose model is to
         perform prompt engineering.
   - this raises a question when to do promptengineer vs when to do fine tuning.

![image](https://github.com/user-attachments/assets/c7f176b5-c184-4fd0-97b9-86f45542a422)



Prompt Engineering vs Fine Tuning:
==================================



 ![image](https://github.com/user-attachments/assets/2fa78346-7ff4-4699-bade-3e0506fa2e88)


Advantages of Fine Tuning:
==========================



![image](https://github.com/user-attachments/assets/402d4d8d-daf9-4e97-952c-e309cab68f21)

- fine tune a smaller model perform well than prompting models with order of magnitude parameters.
  this leads to better scalability and reliability.


  Instruction Fine Tuning:
  =========================


  ![image](https://github.com/user-attachments/assets/74fc723f-6ae5-4613-8fd9-eded6fe65b2c)


  - this is perfectly in the generative ai landscape . LLama chat , Bard, chat-gpt are
    instruction fine tuned.
   - main idea is to fine tune on a dataset comprising of instruction input response tuples.
     this enables model to perform instructions. this enables model to follow instructions.
     This leads the model to answer or minic human which is crucial to develop chatbot or
     conversational AI.
