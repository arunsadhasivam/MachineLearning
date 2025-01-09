Self Refine:
=============


![image](https://github.com/user-attachments/assets/238b50c5-da70-4b55-8352-f8889ba7be83)


  - self refine is way to make llm better at its job by letting it try first 
    and think about how to make it better and try again with those improvements.
  - does not need any extra examples or any extra lessons or training from humans.
  - it uses its own attempt to learn how to do things better
  - make it smart and independent way to make things better.
  - like how we learn new things , try then see what went wrong and then retry again . all of this
    happens inside llm.


How Self-Refine Prompting works?:
==================================

![image](https://github.com/user-attachments/assets/79dad88b-2318-4492-afe8-627fbe99a4e4)

    - it has below iterations.
      1) begin with model creation  an initial response to a query
      2) the model evaluates its response,suggesting improvements
      3) refinement- adjustment are made to enhance the initial response.
      4) iteration - this cycle repeats until a satisfactory answer is not formed.


Self- Refine Prompting : Example:
=================================

![image](https://github.com/user-attachments/assets/cb5784c4-15ec-4c0a-833d-c5c08162dd49)


  - dialogue - "user asks question - i am interested in playing tennis. response  i'm sure it is a great way
    to socialize.
  - feedback - provide no information about table tennis or how to play it.
  - refine - that is great to hear - it is a fun sport requiring quick reflexes
    
Example 2:
==========
  - same way for code optimization like write  a function to write a series of number from 1 to n
  - feedback code is not optimized. 
   
Cons:
=====

![image](https://github.com/user-attachments/assets/d6274fc5-5800-4aaa-8a2c-007ea8562db7)
