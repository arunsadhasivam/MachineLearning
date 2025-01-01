Model Evaluation:
===================


  - after training, evaluate the model.

Need for evaluation:
====================

![image](https://github.com/user-attachments/assets/2aff5900-cb37-441c-ad1d-1d1a1ae70404)

  - benchmark the performance the against the existing state of art model.
  - strength and weakness of llm.
  - so that we can work on weakness improve performance.



Evaluate the LLM:
=================

![image](https://github.com/user-attachments/assets/7f9a924f-83be-4a05-9cf0-2acaefa83534)

    - diverse set of benchmarks on the llm to evaluate
       1) General knowledge (MMLU)
       2) common sense reasoning.
       3) Factuality
       4) Math
       5) code.

1.MMLU:
=======

![image](https://github.com/user-attachments/assets/5e29e0c0-062f-4c72-a180-ca497476e17b)
![image](https://github.com/user-attachments/assets/dadd612b-d45c-4e0c-b3e0-3617566613d9)

   - Massive multiset language dataset (MMLU)
   - mmlu consists of multiple choice questions (MCQ) questions from various subjects such
     as humanity, social science, micro-economics and so on.
   - mcq span around 57 different subject ranging from elementary to advance professional level.
   - above is mcq questions from different subjects.


2.commonsense benchmarks:
=========================

  - broadly there are 3 widely used datasets for this task.
    1) helloswag
    2) Big-Bench Hard
    3) Drop 


<p><details><summary>2.1 Helloswag</summary>
                                    
  2.1.HelloSwag:
  ==============

![image](https://github.com/user-attachments/assets/7979cc1c-014d-4a12-a91b-802b4b4567ce)

      1) most popular dataset for understand the commense reasoning of llm.
      2) it is proposed in the paper "helloswag" can a machine really finish your sentence.
          it contains mcq sentence where the listening context is given and list of 4 possible
          completions for that context is given and list of 4 possible completions for that context.
     3) The task at hand for the llm is to pick the best reasoning completion for the given context.
     4) this dataset is good starting point for understanding the common sense reasoning of llm of day to-day
        task.

  </details></p>


  <p><details><summary>2.3 Big-Bench Hard</summary>

                                           
   2.2.Big-Bench Hard:
  ====================

![image](https://github.com/user-attachments/assets/cc5d3e06-4e61-4956-ba14-dd39bbcf8f52)

    1) Next popular benchmark is big bench hard
    2) dataset consists of 23 challenging task like boolean expression, casual judgement and advanced
       reasoning capabilities of the llm.
      

  </details></p>


 <p><details><summary>2.3 Drop/summary>

  2.2.Drop:
  =========

  ![image](https://github.com/user-attachments/assets/28985592-f65c-4874-9c2b-6750e7c06297)

  - which is short for **discrete reasoning over paragraph**.
  - dataset comprises of several comprehensive passages and questions with respect to passage.
  - llm is expected to answer from the given passage.
  - here the most challenging part of the dataset is llm must resolve references in a question
    perhaps at multiple input position and also be capable of performing discrete operations
    like addition,counting, sorting.
  - these questions require  comprehensive understanding of the world. i.e world knowledge of
    the llm.
  


   </details></p> 


  <p><details><summary>3.Factuality/summary>
    
   3.Factuality:
  =================

  - one of the most common phenomenon of llm is hallunication.
  - very often produce real looking or believable generations which are infact false information or lies
    or non-factual. so we dont want our model to be dishonest.thats where we want test the factuality of
    the model. 
  - one of the popular benchmark for this tasks is **"truthfullQA"**
![image](https://github.com/user-attachments/assets/48ea727d-9e22-4069-9848-35231b3ce218)

  - truthfullQA - this measures llm is truthful in generating answers to misconceptual questoins.
  - the curated questions are generally answered incorrectly by humans due to false beliefs,
    misbeliefs, consipiracy theory and so on.
  - to perform well, models must avoid generating false non-factual , dishonest answers which
    are available throughout the internet.
  - this benchmark is good measure of evaluating the truthfullness , honesty and factuality of the
    given llm.
     


  </details></p> 


  <p><details><summary>4.Math Benchmark</summary>

  4.Math Benchmark
  ================

   - two most popular benchmar are
     1) GSM8K - consists around 8 thousand 
     2) MATH

  GSM8K:
  ======

![image](https://github.com/user-attachments/assets/e7362950-5b56-4c6d-b64a-cef33a95ea75)

    - as name suggest it consists of 8 thousand (8K) high quality school grade math problems.
    - this benchmark how well the llm is able to solve simple math problem.

 MATH:
 =====
    - another challenging dataset is math benchmark. it consists of complex maths problem ranging
      from geometry, algebra, number theory , counting on probability and so on.
    - for llm to perform on this dataset , it must have domain knowledge of various mathematical
      advance problem solving skills.
    - by end of the benchmarking , we will have fair understanding of the advanced problem 
      solving and mathematical skills of the trained llm.

</details></p> 


  <p><details><summary>4.Math Benchmark/summary>
    
5.CODING  :
===========
    - most widely used benchmark for this is 
       1) human eval
       2) Natural 2 code.

  </details></p> 
    


How to evaluate the LLMs:
=========================

![image](https://github.com/user-attachments/assets/61c93325-eef1-4be4-82a1-3ebf1e23cb38)

  - **zero shot prompting** : where in you provide no examples to the model to answer the questions
  - **few shot prompting** :where you provide the list of k examples that can fit in the model prompt, to the
    model comprising the questions as well as expected answer.
  - finally put the question that we are interested in and let the model generate the answer.
  - because you provide the k example , it sort of understand it and performs in-context learning.
  - **Chain of thought prompting:** where in you provide k examples consisting of questions and as well as
    detailed step by step solutions or detail steps to arrive at the given solutions.

  Summary:
  ========

    - depending upon the complexity of the tasks , we choose any of the above 3 methods is selected for
      evaluation of performance of llm. 
    - once you delve about the own llm, you can submit your large language model to the open llm leaderboard
      on hugging face hub.
    - these leader board automatically calculates the scores across the benchmark that we have discussed
      and compares our llm to the start of art llm such as gpt-4 , mistral,gemini.

      ![Uploading image.png…]()
