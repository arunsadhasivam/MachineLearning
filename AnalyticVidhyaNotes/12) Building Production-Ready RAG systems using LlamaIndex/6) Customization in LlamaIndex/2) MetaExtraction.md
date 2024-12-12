![image](https://github.com/user-attachments/assets/b9d62b00-d469-4cd1-8a49-c9c6615a9b02)

<p><details><summary>1.Automatic Metadata Extraction</summary>

1.Automatic Metadata Extraction
================================

- Automatic Metadata Extraction allows better retrieval results.
- 2 extractors
  1) QuestionAnsweredExtraction - generate Question & Answer pairs from a piece of text
  2) SummaryExtraction - extract summaries not only with current text but also with in adjacent texts.
     
![image](https://github.com/user-attachments/assets/ef0e2728-ebc1-40b4-a2f5-acf7b1d6eccb)


2.Define Metadata Extractors:
=============================

![image](https://github.com/user-attachments/assets/7eab0f3f-f6fe-4f3e-8c24-69c86bb1173e)

1)summary Extraction
=============================

- create summary and add to the metadata

![image](https://github.com/user-attachments/assets/2f93c434-4583-4010-a43a-849ec6abe91a)


Load in data , Run Extractors:
==============================

- use webpage reader class UnstructuredURLLoader
- entire webpage loads to single document.
- pass document to node parsers


  ![image](https://github.com/user-attachments/assets/5cf5749f-87af-4db0-8b9a-4fe72cfbcb1a)


  ![image](https://github.com/user-attachments/assets/74d57926-8e8f-4297-92d0-7289b70d583c)


RUn metadata Extractors:
========================

pass nodes to  summary extractors 

![image](https://github.com/user-attachments/assets/ee255116-7d71-40a3-8472-4b61d7af0aec)

prev_section_summary - key holds the summary of prev node.
section_summary - current node summary.
![image](https://github.com/user-attachments/assets/bf68c0d8-868a-43f9-b00a-72b1e244c1a1)
![image](https://github.com/user-attachments/assets/af6a7d39-ec32-4284-8925-125e870d6da9)

![image](https://github.com/user-attachments/assets/d0cf55e4-7ea0-4f44-9ca2-5b4584235c78)


 text part
![image](https://github.com/user-attachments/assets/f25e67ca-2c8c-4c4c-ab2b-5133a909e812)


- 1 st node you dont see prev section summary only see next and current section summary
- similary for last node no next section summary



2)QuestionAnsweredExtraction
=============================



</details></p>
