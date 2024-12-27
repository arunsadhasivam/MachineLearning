Metadata Management
===================

 - customized metadata at the time of 

Step 1 - Environment Setup:
===========================


![image](https://github.com/user-attachments/assets/258b20b5-377f-414b-9836-3aaf38a22d47)


default metadata when loading file

![image](https://github.com/user-attachments/assets/972546be-aae1-4fad-9265-311f2ea63599)

Step 2 : download data:
=======================

![image](https://github.com/user-attachments/assets/01b19ecd-a858-48e0-a310-a5a47fca37a2)


Step 3 : Customize metadata:
============================

- document can be created by data loaders or through document constructor.

1)simple directory reader class:
================================

  ![image](https://github.com/user-attachments/assets/a72e0c33-8fcf-46a8-82f0-acbe7470c690)

metadata
![image](https://github.com/user-attachments/assets/8b355413-8422-447f-ab81-9ed186f565eb)


2)customize metadata through constructor:
=========================================

- create a document by using text part of previous document and customize metadata.
  
![image](https://github.com/user-attachments/assets/f0dac324-d594-4c6b-bbd7-a94ba2d5d011)

![image](https://github.com/user-attachments/assets/985d45b9-0a9c-4798-af1d-54f464a3e17f)

2.1)Change after document has been created:
===========================================


![image](https://github.com/user-attachments/assets/cc52b0e2-3d99-4923-a7f2-b7f92f2c65ff)

see file name changed from **paul_graham_essay.txt** to **paul_graham_essay_2001.txt**

2.2)File Directory Reader and File Meta Hook:
=============================================

![image](https://github.com/user-attachments/assets/263e85d7-2681-4cdc-ac97-aeb18f6d2b5f)

- right at the time of file creation you can mention using directory reader to create value for filename


<p>
<details>
  <summary>2.Advanced Metadata Customization</summary>

1.Customization of LLM Metadata Text:
======================================

- Any metadata you set is included in embeddings generation and LLM.
- 
![image](https://github.com/user-attachments/assets/a670f73e-ccb0-4792-a595-c1091b2bfd29)

  ![image](https://github.com/user-attachments/assets/f298ae4a-6ef5-4b97-a7f9-82eb54e2e0c0)
![image](https://github.com/user-attachments/assets/3989a03a-4855-42c2-8063-a6a4f78ee3ae)


You can exclude so that llm wont access it .

you can add category.

![image](https://github.com/user-attachments/assets/a1f051f8-12a1-49d9-b647-f2a6be4909f8)

Now exclude the metadata for embeddings

![image](https://github.com/user-attachments/assets/8345b30f-759a-4e1c-8497-8156695097b0)

![image](https://github.com/user-attachments/assets/519362f8-d8cf-480e-862a-e4a163cef766)


![image](https://github.com/user-attachments/assets/45e0d9e0-a6c6-4836-a867-01dab44f3d9e)


get content available to EMBED Model

![image](https://github.com/user-attachments/assets/7df810ca-1b9d-49f3-93c0-118075727c19)


![image](https://github.com/user-attachments/assets/0d5ae797-2e5b-4dca-8f98-28d9cb4ecb85)

As you can see since filename is not included it shows up above.

2.Customization of Metadata Format:
======================================


- customize metadata format
- own text template

  ![image](https://github.com/user-attachments/assets/18992b0d-c7ee-40dd-8131-0f35c35e915c)


3.End end Example:
==================


- custom document object with metadata
- added excluding keys
- all information to be added for llm(excluded_llm_metadata_keys)
- text template like next line

llm mode
  ![image](https://github.com/user-attachments/assets/b5e8144c-83c0-4039-a056-b050ddf253a6)

embed mode

   ![image](https://github.com/user-attachments/assets/b31430f4-0d20-4f38-8c8e-d71ef337add7)

</details>
</p>
