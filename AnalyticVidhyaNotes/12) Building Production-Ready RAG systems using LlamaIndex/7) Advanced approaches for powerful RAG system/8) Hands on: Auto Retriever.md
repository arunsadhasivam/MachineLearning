Hands on: Auto Retriever
========================

- Main idea of Auto Retriever is that instead of retrieving the top-k chunk based on similarity search
  using the vector index. we can also retrieve the top chunk based on metadata filter.
- Now the Metadata filter are extracted using LLM and these chunks need to have the metadata information.
- there are some **vector DB that support metadata filter**
- one of them is chroma, PineCone, weavite
- we use chroma, this allows more dynamic and expressive forms of retrieval beyond top-k semantic search.

![image](https://github.com/user-attachments/assets/bfe0c658-e777-4b02-b2cc-b327443ad51e)


Step 1: Step up:
================


