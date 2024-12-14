Auto Merging Retriever
======================
  - in basic algorithm , retrieval algorithm gathers the fragmented context chunks and input them in to
    llm for response generation. however these chunks often from similar document section may overlook
    pertinent content from other document areas, affecting the RAG pipeline effectiveness.
  - As you can see in the sentence window retrieval focus on the local context around specific sentences,
    however relevance context information may be spread over different sections of the document.
  - This is where Auto merging Retriever steps in.
  - it enhance the selection process for more **comprehensive context integration**.
  

Definition:
===========

  AutoMerging Retriever combines the related leaf nodes into larger group based on a threshold.
  This helps create a bigger context for  better information synthesis.


  ![image](https://github.com/user-attachments/assets/d7a5b630-2f92-4d06-b060-97c554b2886a)


4 steps in Automerging:
=======================


![image](https://github.com/user-attachments/assets/9bd85028-ddf3-4714-ad79-28ac05a4c298)

threshold 0.5



![image](https://github.com/user-attachments/assets/a974a2dd-83b3-4062-a182-48de1ae3fdd9)


![image](https://github.com/user-attachments/assets/0c5d550c-7538-4912-897d-76f5c6e93dc1)


![image](https://github.com/user-attachments/assets/2c2a1918-e677-4fb5-844c-79b4ec62e091)

- first level chunk size -2048
- second level chunk size is 512
- leaf node chunk size is 128 - if for a query if the no of relevant child nodes linking to the
  parent document exceeds the threshold(0.5) we merge all leafnodes present in the parent nodes
  and return the parent nodes rather than smaller leaf nodes.
  
  **third step if no of relevant child nodes linking to the parent document exceeds certain threshold(0.5) then we merge all leaf nodes
  present in parent node and return parent nodes rather than smaller leaf nodes.and with merging of all small leaf nodes ,
  we opt to return the parent node size of 512 tokens instead of  individual leaf nodes**
  
- for a given user query with default Retriever without auto merge capabilities
  retrieve the top k nodes directly use leafnodes and directly use for reponse synthesis.
- whereas in the AutoMerge Retriever merge the leafnodes to parent nodes and return parent nodes.
- popular usecase research paper analysis , merging the smaller paragraph to larger context
  whereever necessary.

  


SNO   | default Retriever   without Automerge             | AutoMerge Retriever
------|---------------------------------------------------|---------------------------------------------------
 1    |   first retrieve top k nodes directly             | here 3 such child nodes, third step if no of
      |   uses leafnodes and directly use leafnodes for   | relevant child nodes linking to the parent 
      |   response synthesis                              | document exceeds certain threshold(0.5) then
      |                                                   | we merge all leaf nodes present in parent node
      |                                                   | and return parent nodes rather than smaller leaf nodes.
      |                                                   | and with merging of all small leaf nodes , we opt to
      |                                                   | return the parent node size of 512 token instead of 
      |                                                   | individual leaf nodes.  
------------------------------------------------------------------------------------------------------------------------    
