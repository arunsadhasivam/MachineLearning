Relevancy:
==========

- identify top-k queries which are relevant to the document.
- how relevant the response to the given query.
- how **closely the content matches to the user query.**
- **faithfullness in contrast measure how accurate the llm response actual context.**
  

![image](https://github.com/user-attachments/assets/c06e0a4c-5095-40bc-ad3f-d775da3b0f84)

Calculating the Relevance Score:
================================


- Answer similarity is defined as mean cosine similarity of original question to the
  number of artificial question which are generated (reverse engineered) based on answer.
- lower score incomplete or redundant answer
- higher score for better relevancy.

![image](https://github.com/user-attachments/assets/6ccadb93-e8f4-4b47-8dcc-302b1f2abfc5)


Example:
========

1) we reverse engineer the original question.
2) e.g Question: "where is france and what is it capital?"
3) low relevance answer -> france is in western europe.
4) High Relevance answer -> France is Western europe and paris isits capital.
5) calcuate the mean cosine similarity between generated question and actual answer.

![image](https://github.com/user-attachments/assets/35a7d15f-7bce-4c9d-bd83-57050a449ca3)

Factors improve relevancy:
============================

![image](https://github.com/user-attachments/assets/8cbd1494-6497-4b0c-ba6e-b3999b4da9fa)


- for low relevancy may need to tweak these factors to improve relevancy score.
