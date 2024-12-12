Evaluation:
===========


![image](https://github.com/user-attachments/assets/080a0090-8348-469d-a508-5a087e18e390)


<p>
 <details><summary>1)Retrieval Evaluation </summary>


1)Retrieval Evaluation:
========================

Step 1: setting Logging:
========================

configure logging and import evaluators

1) FaithfullnessEvaluator
2) Relevancy Evaluator
3) correctness Evaluator
4) Retriever Evaluator
5) generate_question_context_pairs - additional questions of the context which have been retrieved.
6) EmbeddingQAFinetuneDataset

![image](https://github.com/user-attachments/assets/5614bef2-44c0-4e1f-8746-0602cf6c5a80)
![image](https://github.com/user-attachments/assets/f64a5977-3e27-49a1-a800-4bf4f40a0324)
![image](https://github.com/user-attachments/assets/b677cbb8-20ff-4878-9a70-68516cf7e505)


Step 2: Download Data:
=======================

![image](https://github.com/user-attachments/assets/549b23a5-06b7-4249-95f1-2bd0deb6b1ba)


Step 3: Load Data:
=======================

![image](https://github.com/user-attachments/assets/3a35010f-4f9f-4ff4-a615-16ad48e35f32)


Step 4: Generate QA:
=======================

generate 20 questions for evaluation.

![image](https://github.com/user-attachments/assets/44c87d0d-9937-409f-892c-b573e32f06f8)

once evaluation dataset created with QA pairs, lets explore.

![image](https://github.com/user-attachments/assets/efa956a5-de5a-484d-850f-398a0544ca5d)


first question

![image](https://github.com/user-attachments/assets/5370e993-d476-428a-bc1b-b03d05b5c6ca)

corresponding answer

![image](https://github.com/user-attachments/assets/044894e6-5fbc-4dca-b016-d587e3b9d4d1)


Step 5:To be consistent fix the evaluation query
=====================================================


![image](https://github.com/user-attachments/assets/f681fba2-a918-426c-a935-a549b3965423)

Step 6: Response Evaluator and Response Generator:
=============================================================

- create **Response Evaluator(GPT-4)** that judge llm and **response generator(gpt-3.5turbo)** LLM

![image](https://github.com/user-attachments/assets/9cd02e75-02c0-4b06-b9ba-70fb84f0ef95)


Step 6: Vector Index:
=====================

create vector store index by passing the document.

open ai llm for creating embedding.

![image](https://github.com/user-attachments/assets/67f4bb2d-6dd9-4fef-af7b-dceb42c6ec07)

set vector index as query engine.

Step 7: create retriever using vector Index:
==================================================


retrieve top k=3 most relevant chunk by providing similarity_top_k parameter =3

![image](https://github.com/user-attachments/assets/e980a632-bb41-4d2e-ae98-871613941eb6)

![image](https://github.com/user-attachments/assets/b9bb90e2-e97e-401c-bc67-5cb5ba8def87)

</details>
</p>


<p>
<details><summary>Step 8: Context Relevancy Evaluation</summary>  

Step 8: Context Relevancy Evaluation:
======================================

Measures if response + source nodes matches the query.

![image](https://github.com/user-attachments/assets/78652a08-266f-4abe-87a8-5cbdf9561dd1)


 ![image](https://github.com/user-attachments/assets/9b8d7177-81a1-47f9-9c73-4ac5d7e85857)


![image](https://github.com/user-attachments/assets/24bc423b-61b7-48e6-b4e9-567fbdb1b34c)
![image](https://github.com/user-attachments/assets/9a4fe3d1-9983-451d-89f1-a9a88d4f0dd9)

Evaluate the response above(response_vector.response) using relevancy_evaluator.

![image](https://github.com/user-attachments/assets/9f74848e-471b-4c1d-8691-38bcee91277c)


![image](https://github.com/user-attachments/assets/45a1602d-2516-4ce3-b9da-2866d945b7b9)


</details>
</p>




<p>
<details><summary>Step 9: Relevance Information with multiple nodes</summary>  


Step 9: Relevance Information with multiple nodes:
==================================================

you can evaluate for all the source nodes.

![image](https://github.com/user-attachments/assets/bdde117c-1a80-4ec2-b35d-d41fe61f81fc)
![image](https://github.com/user-attachments/assets/a58a3dd9-f230-4b37-96ec-bbca063503b6)
![image](https://github.com/user-attachments/assets/808c0e07-1f9d-4573-b462-6a24dc7a0639)

</details>
</p>




<p>
<details><summary>Step 10: Faithfullness Evaluator </summary>  

Step 10: Faithfullness Evaluator:
================================
To confirm that response is not hallucinated response.

![image](https://github.com/user-attachments/assets/8b3588e9-cb11-4614-8463-dce62598fca7)


score will be 0 to 1 . 
passing yes - not hallucinated.

</details>
</p>



<p>
<details><summary>Step 11: Correctness Evaluator </summary>  

Step 11: Correctness Evaluator:
================================
- Evaluates the relevance and correctness of   generated answer against reference answer.

![image](https://github.com/user-attachments/assets/9bf533e7-caaa-421d-a491-97080cd63a00)


5.0 result - good 

![image](https://github.com/user-attachments/assets/cd68a437-7be3-4a45-b004-1a91e4ceb1c9)

above evalutes the relevance of the answer with reference answer.
</details>
</p>



<p>
<details><summary>Step 12: Batch Eval Runner-Run Evaluation in Batche </summary>  


Step 12: Batch Eval Runner-Run Evaluation in Batches:
=======================================================

- evaluate all the queries 20 questions and those 20 answers.

![image](https://github.com/user-attachments/assets/3c4f23ab-cdb3-4073-ab39-4a3ea56cfd11)

![image](https://github.com/user-attachments/assets/4ff70a32-0fe4-4bac-8037-02598c368f0c)


correctness score : 0.9 its says it is not generating correct answers for few questions.

</details>
</p>




<p>
<details><summary> Benchmark using LLAmaIndex </summary>  

Benchmark using LLAmaIndex
===========================

![image](https://github.com/user-attachments/assets/ff056cbb-b998-40e5-bc35-27068a2cb29a)

![image](https://github.com/user-attachments/assets/6a9bfbb7-99dc-4f37-98f3-9c50af9ed816)

Step 1:Download
================

uncomment and download RagEvaluator Pack

download Rag Evaluator and move to folder.

![image](https://github.com/user-attachments/assets/4462c6fb-0e09-4693-9213-025d6259e36f)

Step 2:Build Rag Pipeline:
==========================

- already load rag dataset
- confirm rag dataset and source files in the corresponding folder

    ![image](https://github.com/user-attachments/assets/1aaaadaf-693d-428f-a508-2abb24c8b2b8)

first query and reference answer

![image](https://github.com/user-attachments/assets/8de1e822-c84f-4d04-b67a-f85ddd518f76)


 create basic Rag System 
 - first create document
 - from document create index
 - that index set up as an query engine.

![image](https://github.com/user-attachments/assets/af63436f-602d-4449-9801-d41385038a9c)

create rag evaluator pack and run.
![image](https://github.com/user-attachments/assets/aaa3cf44-2465-463a-a892-7f685e3eb463)

</details>
</p>
