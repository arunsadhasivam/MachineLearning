Components of LlamaIndex:
=========================

![image](https://github.com/user-attachments/assets/912e4d78-6645-4f2a-8d3b-0a191bb1348b)

1) **Ingestion and Indexing** - external knowledge is loaded and split in to multiple
   chunk of data. each chunk is then converted to vector embeddings and stored in index.
2) **Retrieval** - Retrieval Algorithm fetches top k relevant documents from user query from index.
3)**Responsive Synthesis** - Synthesis stage top k documents and user query are passed on the llm to
   generate appropriate response.
   
