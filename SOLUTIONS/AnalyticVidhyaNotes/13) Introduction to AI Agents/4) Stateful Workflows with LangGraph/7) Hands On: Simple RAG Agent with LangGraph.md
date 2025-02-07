Hands On: Simple RAG Agent with LangGraph:
===========================================


Agentic RAG:
============

![image](https://github.com/user-attachments/assets/318e102e-e7f8-440c-87fc-aee38d47aa24)


    - build very simple Agentic Rag.
    - meaning connect a Agent through access through a document or pdf
    - so that we can ask questions to the pdf and get response back.
    - All we need is setup a graph, setup logic for agent and retrieving of the information.

Step 1: imports:
=================

![image](https://github.com/user-attachments/assets/f887ab3b-1c25-4a3b-9ff1-d88c9a8373da)

PyPDFLoader - to access pdf or getting the pdf
chroma - vector db for rag.
openAIEmbeddings - for embeddings part
chatOpenAI - model


Step 2: load pdf:
=====================================

![image](https://github.com/user-attachments/assets/6bd11eb7-80c8-4aa7-b1a5-7b528c654cbe)
![image](https://github.com/user-attachments/assets/c21e3898-cee9-42ed-8f4a-09a028f9e5df)

  - load and split into no of pages of document.
  - load_and_split() meaning we are going to have list of documents match the no. of pages in document.
  - **len(docs) matches the no of pages of document**. the splitting ones are document object.
  - vectordb chroma.fromdocuments() get all the documents from pdf.
  - **document** objects relative to the object **document loader** from langchain.
 
Step 3: vector db:
==================

store in vector db and set the retriever

![image](https://github.com/user-attachments/assets/786adae3-bebe-49b6-a2dc-6ab460392eae)


Step 4: vector db:
==================
  - Now, all we do do is to transform this in to a tool , incorporate in our graph.
  - create a retriever_tool with name 'retriever_from_paper' and 'Search and return information about paper'
  - now you put it in tools

![image](https://github.com/user-attachments/assets/efad5657-764c-4c44-be48-90c072ef89ce)

Step 5: set Agent State:
=========================

![image](https://github.com/user-attachments/assets/76001418-b570-4a0c-b7a5-32dce2500727)

  - set messages which are to keep track of messages throughout the execution of graph.
  - BaseMessage are core object of langchain to exchange messages with ai.
  - only thing we keep track of is the messages list which we use thoughout the execution of graph.
  ![image](https://github.com/user-attachments/assets/d009da48-8950-4bc6-a566-aa9b7ffd4c31)


 - we take the state , message from state and then set up the model
 - we set temperature to 0
 - streaming = True and model='gpt-4.0'
 - then bind the model to tools
 - then set the response to model.invoke(messages)
 - return dict with updated messages.

 ![image](https://github.com/user-attachments/assets/a7e1aa70-2e7a-4dcf-ba49-7c0976d3f7e0)


 - Now , we have agent working.
 - this is the essentially going to invoke() the agent model to generate response based on current state given
   the question asked about the pdf, and then it will decide to retrieve using retriever tool or just end.
 - it has access to the retriever tool, to this binding of the model with the tool that we are doing above.
 - Now, we have agent , we can do is setup the rest of the graph.

Step 6: Setup rest of the graph:
===================================
 
  - create a graph.
  - first node you are going to add is agent node.
  - retrieve_node is toolNode(retriever_tool)
  - then add the retrieve_node to graph give the name as 'retrieve'.

![image](https://github.com/user-attachments/assets/28d85853-79d8-4589-961b-c08805991e93)
![image](https://github.com/user-attachments/assets/1a950211-304a-4a4f-a83b-00aa07bfcc15)

  - now set the edge.
  - first edge is START and we are going to associate with the agent.
  - graph.add_edge() the first edge
  - then add graph.add_conditional_edges('agent') and then in dictionary we say retrieve reference to retrieve_node
  - then we say END
  - then compile the graph
  - only thing missing is that, we need to set the retrieve back to the agent.
  - so that it will actually provide the answer.
  - lets add edge from retrieve to the agent.

![image](https://github.com/user-attachments/assets/75c16541-f3a9-40f8-998b-a6af494b2b50)
![image](https://github.com/user-attachments/assets/eb4a8ce2-6e08-4796-af07-817146ddad75)


Step 7: Execute with example:
===================================

