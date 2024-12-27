
LLM:
====

pretrained large amount of publicly available data.

What can LLM do?
====================

- Blog writing - mail
- Summarization of all whole document
- Coding Assisting - expert debugging assistance.
- Idea Generation - brain storming sessions
- Q& A - who win world cup based on trained data 

limitation:
===========

  above who win world cup - bound to data trained. it might not able to answer latest

Augment LLM with our private Data:
===================================

Below are paradigms to insert data in to LLM from private data to
sync with current data.

  Paradigms to insert Knowledge into LLM:
  =======================================
  
  1) Fine Tuning
  2) In Context Learning.
  3) RAG.


1)Fine Tuning:
==============

  - takes a model already trained and then tunes or tweaks the model to make it performa a similar task.
  - start the training on new data but the weights on the initial network.
  
  issues:
  =======
  
  - high computation
  - high preparation effort
  - high cost
  - Need ML Expertise

2)In Context Learning:
=======================


- Take llm and insert entire context in the prompt of llm along with the query to answer the question.
- this is prompt engineering.

  Issues:
  =======

  - long context issue -  max token allowed is 4097
  - To avoid this issue , we have a strategy to break down fullcontext in to smaller managable segment of context(context1,
    context2,context3)
  - This strategy help to query without exceeding maximum token limit.
  - still challenge exist to retrieve right context for query. how to deal with source data
    that is potentially very large(GBs, TBs)
  - for this RAG comes in to picure bridge the GAP between static knowledge of LLM and
    the dynamic vast world of information.achieves combining LLM with information Retrieval System.
  
    

![image](https://github.com/user-attachments/assets/b62446be-ce6b-4a5c-929d-8db83f6dfd7b)


3)RAG:
=====

- Augmenting LLM with external knowledge sources Like db,graphs,documents which provide access to
  latest and specific information.
- enhancing context awareness - more contextually relevant and consistent response.
- facilitating easy knowledge update the knowledge source is very easily then updating
  entire LLM.

