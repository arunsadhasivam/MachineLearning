Data preprocessing
==================

![image](https://github.com/user-attachments/assets/16fad6f0-f389-4c85-be45-4c20a92cfd08)

- in this lesson we discuss about the data preprocessing .
- one of the key principles behind the password models is to have high quality data.
- most of the time while curating the data, the quality can be low.
- as much to ensure high quality , the dataset needs to be cleaned and properly formatted.
![image](https://github.com/user-attachments/assets/de044e6c-651f-4349-be71-b5fd94f9323b)
- thats exactly happens in data pre-processing.
- data processing filter out raw data to create high quality datasets.


common steps involved in data preprocessing:
=============================================

![image](https://github.com/user-attachments/assets/37784154-f6ee-4927-8265-42b2d0a97e8c)

1) data sampling - sampling the datasets to handle the training data distribution. we either oversample
   or undersample data from various sources.often the datasets comprising of high quality are oversampled
   and low quality are under sampled. for eg. gpt-3 created on diverse dataset from various source like
   common crawl, books, wiki. during the model training we can see that high quality training dataset
   such as webtext , wikipedia are oversampled. i.e they complete 2-3 of there epoch and at the
   same time such as common crawl like books are undersample. so that they don't even complete the
   .4 epoch.

![image](https://github.com/user-attachments/assets/a744d373-2941-4c7a-9b3e-29b5e0b81855)

2) next most common steps is data de-duplication - process of removing the duplicate text across the
   training data. for e.g in initial dataset we see "data is fun" 2 times post de-duplication only
   one data is set. one of the reason of data duplication is that we collect the data from
   different source so it might result in data duplication. so these data should be removed before
   model training.

<p><details><summary>Primary reason for doing data-duplication</summary>
  
   primary reason for doing data-duplication:
   ===========================================

![image](https://github.com/user-attachments/assets/8e82e1c2-c771-426f-991a-d57c2fd9a578)

   1) main reason is to eliminate the memorization of the training data. this allows us to
      train model efficiently and usually result in better models.
   2) also result in faster training- because the training dataset size is reduced.
   3) accuratelly evaluate the trainnig , by de-duplicate the text we can reduce the
      train text overlap and allows accurate evaluation.

</details></p>

  <p><details><summary>Primary reason for doing data-duplication</summary>
    
  Methods of data-duplication:
  ============================


  - one of the simpler method is jaccard similarity b/w document   pair-wise
![image](https://github.com/user-attachments/assets/03e00b68-9140-49fd-9257-536bd69cde10)
  - Above considering the 2 document  first - generative ai is fun , second is - generative ai is fun and easy.
    in order to find the jaccard similarity b/w 2 documents is we compute the shingles i.e n-gram of the
    sentence.

![image](https://github.com/user-attachments/assets/cf2e4dce-a4b5-4df6-ba72-72aa19d2b879)

  - in this e.g lets use bi-gram based on the word level to illustrate the jaccard similarity.
    here shinges for the document 1 would be "generative ai" , "ai is " and "is fun" for first document.
    similary for the document 2 . once we complete shingles we compute the jaccard similarity.
    if we take the set 1 and set2 that is set1 of document 1 and set2 of document 2 we  see
    that is 3 shingles or 3 bi-gram that is occuring in both document   , union between the
    bigram of the 2 documents is 5.so jaccard similary is 3/5 which is 60%. we can set a 
    threshold , if we have jaccard similarity more than threshold we can consider that both are
    similar and ignore it.

  - simple algorith, is very efficient in removing duplicates.
    
Limitations:
============    
  - however it has limitations  , it is not scalable for large scale dataset. the reason been that
    to compute jaccard similarity once need to **perform pair wise comparision**.
  - i.e we need each pair of document that is not scalable for large dataset.
  - hence thats where exactly minhash comes in.

MinHash:
========

![image](https://github.com/user-attachments/assets/717f0caf-464f-47b7-982a-bc77b60f0624)

  - most popular data-duplication techniques.
  - it uses novel technique to compute jaccard similarity or approximate the jaccard similarity
    using hashing.
  - it used as a part of most of the data preprocessing steps for training llm like star coders, llama
    and so for.

4 steps involved in minhash tecniques:
======================================


![image](https://github.com/user-attachments/assets/08c402a3-bed7-4b1c-85d2-e01dd6a8ef70)


![image](https://github.com/user-attachments/assets/bed20e75-805a-421b-a33d-aa38a5ddfc06)

  - **first step** is to perform tokenization or shingle where the document be split into singles most often
    n-gram.
  - **second step** is finger printing or min-hashing where we map each document in to set of hash values
    using different hash functions.
  - **third step** is to apply locality sensitive hashing(LSH) to reduce the no of comparsion by grouping
    document in different bucket.
  - **finally** we eliminate the duplicated documents.





</details></p>

<p><details><summary>Common Data preprocessing reason for doing data-duplication</summary>


![image](https://github.com/user-attachments/assets/9d07df31-81df-48d4-b9d0-62d4f9f9a4a6)

  - Apart from datasampling and data duplication, few other data common preprocessing steps can be reviewed

    1) remove boiler plate text
    2) eliminating html code
    3) removing bias/harmful content

   what is for you?
   ================

    - most common data pre-processing steps while training our own llm is
      1) data sampling
      2) data duplication.
      3) specific data preprocessing steps per your data.


</details></p>
    
