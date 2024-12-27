![image](https://github.com/user-attachments/assets/f04b4036-83f6-42e6-8346-e25dd7d0b76a)Natural Language to SQL query generation using IA3
===================================================


IA3 method to perform instruction fine tuning 
- Task **task to convert natural language to sql queries.**
- load the required libraries
- wanb project as mistral instruct fine tuning

Step 1:Step env:
=================

 ![image](https://github.com/user-attachments/assets/52f40d25-30c0-47d6-8a36-3c7d08c034ec)


- get IA3 config



Sep 2- Data Processing:
==========================

![image](https://github.com/user-attachments/assets/59586f98-db1f-4f0b-9d6a-61653e8b3bd1)


- model is mistral 7 billion model
- data set is wikisql
- 15.8 samples validated

  ![image](https://github.com/user-attachments/assets/178d5ffc-3c18-4448-986c-78b0e38f63ec)
![image](https://github.com/user-attachments/assets/bfbc28a0-bebc-40e0-b411-29cac26c3135)


Sep 3- create PEFT Model:
==========================

![image](https://github.com/user-attachments/assets/824c4c81-7d0d-47ba-836b-18f298bd20d3)

- first set the ia3 config
- we are going to target the key projection layer, value projection layer and down projection layer.
- feed forward is down projection layer, task type is casual_lm

  

Sep 4- Training:
================


- training module setup output as mistral sql instruct.
- we give per device batch size is 8
- we accumulate gradient
- no save strategy since it is demo, in production use case always save at regular intervals.
- evaluation strategy as epoch.

![image](https://github.com/user-attachments/assets/43c7a760-4763-45ea-b830-c67b65d27d2c)
![image](https://github.com/user-attachments/assets/d6711294-2c2f-434c-b9b2-f22e58ce38fc)
![image](https://github.com/user-attachments/assets/f94894d6-f297-4abb-bf53-cc8afbe33842)
![image](https://github.com/user-attachments/assets/337b6123-0dbc-49a5-9da7-a7c963d8047a)
![image](https://github.com/user-attachments/assets/4956b8f0-e7aa-40f1-a386-1fb376d298f1)


Sep 5- Loading Training model and getting predictions of the trained model:
=============================================================================

![image](https://github.com/user-attachments/assets/47600c0b-03fe-4fed-8047-f84b619c3f6c)
![image](https://github.com/user-attachments/assets/f9b9f7ce-acc4-4230-8073-890643a78b3b)
![image](https://github.com/user-attachments/assets/f59d5709-b4c1-4ef3-9a25-1241479d52b0)
![image](https://github.com/user-attachments/assets/f8a141c7-de13-474f-97db-50b26495922c)


- input is the table and the natural query , we give sql:query as prompt
  where total attendance on date 10/05/1974 it generate sql query.
  
