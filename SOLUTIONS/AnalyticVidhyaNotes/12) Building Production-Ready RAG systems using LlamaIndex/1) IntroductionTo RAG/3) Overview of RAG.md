Objective:
===========

To provide right answer to the user query from external knowledge.

Steps in RAG:
=============

![image](https://github.com/user-attachments/assets/6f3b2f65-892e-4695-8f46-f6a6fd5a4c78)


1)Data Ingestion:
==================

To Prepare the external knowledge required for efficient retrieval and synthesis.

![image](https://github.com/user-attachments/assets/f134124d-9ae6-4095-aff3-7feb5b29b37c)

2)Indexing & Storing:
=======================

![image](https://github.com/user-attachments/assets/dcdce8ea-58af-4eb1-9aad-275b08fb9189)

- quick Retrieval :Indexing - quick retrieval speeding up the process of finding relevant information.
- Enhanced Accuracy: Improves the relevance and quality information retrieved.
- Scability : Allows the system to efficiently handle large data volumes.

3)Retrieval:
============

![image](https://github.com/user-attachments/assets/ea438ceb-6c59-48be-9192-68f66d034090)

- To retrieve top k relevant chunks or context.
- Top K relevant chunks or context to pass to response synthesis which has LLM to generate
  right response.
- query is done through query Engine interface. Query Engine Interface combines 
  with retriever and response synthesizer to create end/end pipeline for RAG.
  This Pipeline allows user to asks questions about the data in natural language and
  returns result.

4)Evaluation:
=============

Accessing the quality  and relevant answers generated

Over all Framework:
===================


![image](https://github.com/user-attachments/assets/3744a1db-124c-4f78-af36-170161d2170b)


1) External knowledge base in split in to multiple chunk of data
2) Each chunk is converted in to embeddings and then organized in to a index stored in vector db.
3) then retrieval algo fetches top k relevant documents to the user query from index. and finally
   top k documents and user query is passed to generated llm to generate right answer.

4) Lastly we have query Evaluation and interface.



