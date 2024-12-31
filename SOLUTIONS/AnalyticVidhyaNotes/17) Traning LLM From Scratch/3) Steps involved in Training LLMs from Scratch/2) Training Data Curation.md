Training Data Curation
=======================

![image](https://github.com/user-attachments/assets/08b0196d-e444-4e9a-a84f-b18993501390)


   - one of the primary and most important step while training llm from scratch.
   - it is the process of collecting and aggregating the data for training , first step that drives the performance of llm.
   - most of the time spent on this task "training data curation"
   - llm are commonly trained on a mixture of filtered web data and curated high quality corpora such as wiki,github,stackoverflow,
     social media conversion , books and technical and scientific papers.
![image](https://github.com/user-attachments/assets/b2126387-ffe6-4393-b08b-1117b58d7a46)

   - the curation process is relatively necessary to produce high performance models.
   - curation process is driven by 3 main principles:
![image](https://github.com/user-attachments/assets/00752338-7ca8-4704-a6cc-157544d2463d)

     1) Massive scale e.g gpt3(trained using 300 billion tokens , llama2  2trillion tokens etc)
     2) diversity - diverse dataset enables model to improve the cross domain knowledge and inits generalization capabilities.
     3) high quality dataset - high quality dataset is key for building high performance models. small language models
        like phi-series ,microsoft focused on collecting or synthetically generating high quality dataset i.e text
        books quality dataset and outperformance llm with 25% more parameters.


Open Datasets:
==============


![image](https://github.com/user-attachments/assets/aaa66d75-0c79-4e59-88d1-dd1eb933ab5f)

   - most popular dataset for training llm is commoncrawl
   - the common crawl dataset is free, opensource, openrepository of webcrawl data . it contains
     petabyte of data and it is regularly collected since 2008. the size of the dataset is sufficient to
     train largest models without ever updating on the same sequence twice.
   - it is available freely on amazon webservices public dataset and on multiple academic cloud platforms
     across the world.
![image](https://github.com/user-attachments/assets/15e5c953-2e5d-4e7d-8047-f10b66a68eb9)

   - the next popular dataset is **refine web dataset** , which was used to train falcon series of model.
   - it is created by falcon team for training the falcon series model with largest billion parameters.
   - this dataset is the result of properly filtering and re-duplicating common crawl data.
   - you can access it for free via hugging face dataset.
![image](https://github.com/user-attachments/assets/522a5faf-7a45-4a01-9877-e11dbc2f9905)

   - another popular dataset is **pile** . pile is 825gb english text corpus targeted at training
     large scale llm. the pile is constructed from 22 diverse subsets, both existing and
     the newly constructed. many of which derived form academic or professional sources.
     five broad categories like academic, dialog, pros and others
![image](https://github.com/user-attachments/assets/ca5f50a9-62e6-4d99-aafa-8010042634f7)

   - Apart from general massive corpus dataset, access to domain specific dataset like code,
     medicine etc that helps you llm which are specifically focused to these domains.
   - stack is from hugging face contains over 6tb of permissively code source covering 350
     language code. dataset is created as a part of big code project.
   - open scientific collaboration working on responsible development of llm's for code.
   - this stack serves as a pre-training dataset for code llm i.e code generative ai systems
   - this enables the **synthesis of the program from natural language** description and
     **filling in the code when you are writing the code in IDE**.

![image](https://github.com/user-attachments/assets/99788d30-df93-4175-89f4-4ac88673ac60)

   - **Mathpile dataset** - high quality math centric corpus comprising about 9.5 billion tokens
   - it draws from a wide range of source such as textbooks, lecture notes, archives and
     webpages.
    - it comprises mathematical corpus suitable for college, post-graduate level and maths competition.

Summary:
=======
    - so , depend on the domain we go about the collecting the data specifically suited for the domain.

Steps involves in training data curation:
==========================================

![image](https://github.com/user-attachments/assets/0f135a18-26ae-471b-a17c-5598aa737e2b)

  - the way to go about collecting the training data is to first to estimate the size of the training dataset
    that you need for achieving the optimal model. **you can do this using cinchilla scalling laws**.
    ![image](https://github.com/user-attachments/assets/8888fd6c-ed22-4bde-a736-5c6f18b90397)

  - post that you will need to look for highest quality opensource datasource like textbooks,technical papers,
    books and so on and soforth. before move on to traditional web scrapping and traditional dataset.
  - if you are not possible to get the open source dataset, then you are left with the web data or
    human evaluators, human annotators via platforms like mechanical turkes.
   
    
