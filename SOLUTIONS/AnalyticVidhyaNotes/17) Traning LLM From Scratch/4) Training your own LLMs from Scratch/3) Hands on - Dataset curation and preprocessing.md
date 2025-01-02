![image](https://github.com/user-attachments/assets/94298db4-8096-4000-9172-43d07a47b349)![image](https://github.com/user-attachments/assets/373b85a6-1a44-4e2c-b9f2-44f2cff0f935)Hands on - Dataset curation and preprocessing
==============================================

![image](https://github.com/user-attachments/assets/6ecef4a4-bb2b-4308-bf16-6f95dbd07b1e)


Step 1: dataset Curation and preprocessing:
===============================================

    - we need the github access token and locally save the libraries
    - dataset creation steps.
    

![image](https://github.com/user-attachments/assets/08254f1a-44c0-4c23-aa5e-0c8655fc357a)
      - repository read access above


Full code:
==========

![image](https://github.com/user-attachments/assets/8c9a3bac-df2e-44ac-a788-77bc1a4aff05)
![image](https://github.com/user-attachments/assets/154f6531-d075-4cb1-82ae-9334cd1f4777)


Code walkthrough:
===================

  - mirror repository run , if mirror directory is not there create.
  - mirror folder where we download and store locally the hugging face 
  - mirror directory is the place where we will locally download the dataset i.e open source
    publicly available code base.
  -  **gh_access_token** for api call , first get the repository for hugging_face org 
     which are accessible by access_token gh_access_token.
  - next sort the repo based on stars in desc.
  - we select the top-k (15) publicly available from hugging face.
  - we clone those repository in mirror directory.
  - thats it you can see new folder gets created after run the code.

![image](https://github.com/user-attachments/assets/b90c61e8-d8c5-4415-8fa0-9c69f001dd7a)

   - hf_public_repo is created which has 15 repository from hugging face.
![image](https://github.com/user-attachments/assets/47acaa91-b5a7-4f4c-a1ca-ae1ede2ae341)

   - done with step3 now step 4
   - download nltk
![image](https://github.com/user-attachments/assets/2fda79f3-9f08-4433-a7ba-be7e3e4bb101)
    - now run the data pipeline which uses 16 cpu which is not a concern since we have 72cpu as below
![image](https://github.com/user-attachments/assets/ee1f3fa1-7d2b-4f78-b7d0-aeeac336060c)
![image](https://github.com/user-attachments/assets/329836f5-d8b1-4794-9090-12b74683bea6)

   - running the python pipeline

![image](https://github.com/user-attachments/assets/73ecab4a-f58d-46f8-8f24-a13171fae1b6)

Pipeline.py code walkthrough:
==============================

  - pipeline.py code

![image](https://github.com/user-attachments/assets/c6711fae-c64d-4dee-a753-3eaf15cc6beb)

   - mirror directory is hf_public_repository which is created above.
   - run_code_generation() function in this first pipeline step is using the
     personal co-pilot dataset , filter and preprocessing it and writing to the filtered_data
![image](https://github.com/user-attachments/assets/d4264f26-2e09-4cab-a666-02d301a5fc7c)

![image](https://github.com/user-attachments/assets/77862715-05de-4546-90d5-321959e19862)
![image](https://github.com/user-attachments/assets/bd3f1e0e-787b-4cd9-b75d-8fb3cfc999db)
![image](https://github.com/user-attachments/assets/b9fea2cc-7dbf-44a7-b6c1-490c38c84f73)

   - you can see the personalCopilotDatasetReader comes from reader.py
   - step 1 - reading and doing basic filtering
   - step 2 - compute the minhash signature for each task or each of the gpu which do preprocessing.
   - step 3 - find the matches based on signature on each bucket.
   - step 4 - we have cluster of duplicates based on the result of duplicates.
   - final step is to do de-duplicates based on these cluster of duplicate.
     we take exactly one sample per duplicate.
     post that we get the preprocessed and de-duplicated dataset as we see in the previous module.

reader.py code walkthrough:
===========================

    ![image](https://github.com/user-attachments/assets/3d0e99b1-b496-4d3b-8fc6-b14a3e8f87aa)

![image](https://github.com/user-attachments/assets/1bb26694-c0bf-45a3-89e4-525fb8870fa6)

  - first step , here the main class is  the PersonalCopilotDatasetReader which inherit from
    BaseDiskReader class of datathrough library.

![image](https://github.com/user-attachments/assets/692ff485-0d8b-43ab-b922-5e0ce847d3cc)
![image](https://github.com/user-attachments/assets/50dd7937-2cda-4043-a634-2442e6fcad0f)
![image](https://github.com/user-attachments/assets/8081cfab-b1ea-4c00-90b4-c6a7378bf9ce)

![image](https://github.com/user-attachments/assets/3d188e5c-29ff-48f3-a021-ad23ab9d664b)



  - here the important function is readFile() where in we are reading **each file from all the above repository**.
![image](https://github.com/user-attachments/assets/fbcb7aa6-d37e-4d6e-b261-132da43d62af)

  - such as this setup.py for instance.if file path has .git,_pycache, xcodeproj and antiforat png,images, modes  are ignored.
  - set to content is above format.
  - if it is jupyter notebook(ipynb) do separate preprocessing.
![image](https://github.com/user-attachments/assets/4e6c0cd2-b9a3-4349-a8e4-dd22a5348ad1)

  - doing bunch of preprocessing
  - for any other format other than ipynb just read content.
  - adding metadata, file_path, repo_id
![image](https://github.com/user-attachments/assets/b7c6215f-bec6-4b46-846a-74a37aa49d1d)

Filtering code walkthrough:
============================
  
  
  - filter phase we get the text from document, also metadata from above step.
  - if content is "" the text is removed - filtered
  - if not jupyter notebook we get the basic stats
![image](https://github.com/user-attachments/assets/8d8b8997-55b6-4ee8-929d-35d6c149a50d)
![image](https://github.com/user-attachments/assets/fca62328-46a8-47f4-bf76-ce802d112ccf)

  - if the max line length > some max line length threshold  or mean_line_length > max_line_length
    or alpha_num_ratio > alpha threshold - we filter.


NOTE:
=====

  - pipeline.py we then call filter.
 - we write the ids to removed to be output folder filtered_data
 - pipeline -4 we take the filtered data folder and remove_id to be removed.
 - and then we write to removed folder
 - only the data which is clean , removed and de-duplicated write to **hf_stack** folder , this
   has final  clean dataset.
 - finally run the local pipeline staage1(16cpu) , stage2(matches in each bucket ),stage3(treating cluster single cpu)
   finally last stage 16cpu and call exectutor and run all the tasks we created. 

![image](https://github.com/user-attachments/assets/1e549c61-9a64-4190-a717-3bd3c4fcf9d2)

   
