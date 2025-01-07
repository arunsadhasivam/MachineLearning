Rephrase and Respond Prompting :
================================

![image](https://github.com/user-attachments/assets/3e7c45f9-c29f-48d1-9f1d-da58e2e97346)


 - simple and effective way to help language models **understand and answers the questions by first
   making the question clearer** and then **providing the answer**.
 - this method involves asking the computer of the language model to take the question given
   by the end user and then change the version easier to understand. then user is clear
   of question to come up with the answer.
 - by doing this Rephrase and respond prompting improves the accuracy of the response by
   llm.
 - it makes them more reliable for range of questions.

How it works:
=============

![image](https://github.com/user-attachments/assets/0963c85f-bc8d-46df-aa98-ce4616cef208)


-  2 step involves:
   1) one step:
   2) two step:
   where we rephrase and extend the original questions and then get a response from language model.    
 -  we can make the prompting techniques even more impactful by combining chain of thought prompting  on top of it.

 Example:
 ========

 ![image](https://github.com/user-attachments/assets/fffad660-67c5-4802-a32c-a7597346a1c4)


1step rephrasing and respond:
==============================
  - first example 1 step rephrase and responsd prompting 
    where user asks the " last letters of words in edger bob and concatenate them"
  - language model rephrase to "can you form string or series of character by joining together
    final letters from each word in phrase edger bob".
  - this is the one step **since we rephrase the original question** and the
    **rephrase question is used to generate the answer**
    

 
2step rephrasing and respond:
==============================     

  - along with rephrase questions we also phase the original question to generate the answer
  - e.g "  **question:** last letters of words in edger bob and concatenate them"
  - **rephrase question** "can you form string or series of character by joining together
    final letters from each word in phrase edger bob"
  

   - we pass like "last letters of words in edger bob and concatenate them"
     "can you form string or series of character by joining together
    final letters from each word in phrase edger bob"

  - pass both to get the answer.

Disadvantages:
==============

 - falter with complex tasks like deciphering first character in chinese idom.
 - poor training can led llm to incorrect answer
 - without guidance (zero-shot Chain of thought) can generate non-sense or wrong answer.
![image](https://github.com/user-attachments/assets/7de2a2a1-4b87-4c70-9f64-10ddecec36a7)

 
