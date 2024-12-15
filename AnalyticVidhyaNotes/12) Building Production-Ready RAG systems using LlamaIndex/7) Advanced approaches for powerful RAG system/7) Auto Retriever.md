Auto Retriever
===============

  - As seen earlier document converted to set of nodes - > stored in vector db -> each node
    contains the information about the raw chunk(i.e text, embeddings and metadata)
  - Now using the metadata of the node and power of vector db, can we retrieve the nodes
    from the vector db for the given user query without comparing the embeddings.
    Thats what autoretriever does.



    ![image](https://github.com/user-attachments/assets/d8bad389-42a2-4391-8f42-8374f52ceece)


How it works:
=============

![image](https://github.com/user-attachments/assets/2cab88fd-b0fe-4204-914e-bfdad799c9dc)


![image](https://github.com/user-attachments/assets/cb638e24-0339-47dc-bcc2-c5a535e70c4d)

- e.g we want to query the documents of US Sports celebrity. we can store in the information of
  each celebrity in the node along with the metadata like sports category and the country of the origin
  for the player in the vector DB.
- now end up with the nodes containing the data and its metadata in vector db.
- post that given the user query , we first use the llm to infer a set of metadata filter and pass it to
  vector Database. Now the vector DB uses these metadata filter and extract this relevant nodes .
- **so auto retriever combines the metadata filter and vector db to retrieve the relevant nodes.**
  ![image](https://github.com/user-attachments/assets/f8ee03bb-ac13-45de-897b-7391e66aa47c)

- here the nodes are node1,node2,node5. in the next stage based on the similarity of the query
  with the node information , the top-k similar nodes are retrieved.
- e.g top-k is 2 , here node1,node2 is retrieved.




![image](https://github.com/user-attachments/assets/7e8c7936-2aa3-4bd1-adeb-7e21590b0676)


Potential Use case of Auto Retriever:
=====================================

![image](https://github.com/user-attachments/assets/3b00de49-8858-45cd-9f52-9b671f8b4f64)


 
