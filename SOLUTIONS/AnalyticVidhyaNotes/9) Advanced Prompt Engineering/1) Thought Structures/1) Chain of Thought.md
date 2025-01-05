Chain of Thought:
==================

    - chain of thoughts increase the reasoning capabilities of the model.

  
![image](https://github.com/user-attachments/assets/d0045554-ab6a-4ff6-9508-2601a41588cb)
![image](https://github.com/user-attachments/assets/1f7944be-2f4b-4a0c-a85f-acf9d957b5d7)


How does it work:
==================
![image](https://github.com/user-attachments/assets/4b60e8d2-21ac-4481-9dac-56e1488fb68d)

![image](https://github.com/user-attachments/assets/bad229db-c248-4f29-bef9-edc20ccc2b0d)

![image](https://github.com/user-attachments/assets/3e572638-6c90-436c-a6f7-5651458dc0bf)

Use case:
=========

![image](https://github.com/user-attachments/assets/85291685-7cec-4789-9544-22564e4faffd)

  - ability to reason
  - commensense reasoning
  - symbolic manipulation.

Chain of thoughts Prompting : example:
=======================================
![image](https://github.com/user-attachments/assets/f0454936-690b-4093-a22b-a1763db06cf0)


  - showing how chain of thought prompt works
  - above is e.g of standard input and output prompting.
  - we pass Q& A pair where the questions is Roger has 5 tennis ball and buys 2 more
    answer is 11.
  - while explaining the answer , we are not giving reasoning how we arrive at the answer.
  - we ask another question like "cafetria has 22 apples used some , how many remaining"
    it returns 27 . it is correct thats exactly we need chain of thought prompting.


Chain of thought prompting vs standard Input Q&A:
======================================================
  - the way chain of thought prompting is different from input & output standard prompting
    is  we explain how we arrive at the answer. in the right you can see we have explained
    how we arrive at the answer like Roger  started with 5 balls , 2 cans of tennis balls
    each is  6 tennis balls . 5 + 6 =11 . this is the answer.

  -similary the cafetria problem.


  Pros: Chain of Thought Prompting:
  =================================

  ![image](https://github.com/user-attachments/assets/a8413668-bd95-439e-be06-02e8d7e51cf6)

   

  - Advantages of chain of thought prompting is it achieves the state of art accuracy while it
    surpass the fine tuned models with verifier.
  - this technique is also applicable to various task , the required multi-step reasoning making it
    a versatile approach in different domain. it also enhances the interpretability of the language model
    by providing the insights to the model reasoning process through the generative chain of thoughts and
    this techniques is ready to use cost effective strategy and does not require model fine tuning.


Disadvantages:
===============
![image](https://github.com/user-attachments/assets/f218d1eb-d638-4957-b320-9dcf76d3743e)

  - Augmenting examplars with the thought chains for fine tuning is resource intensive.
  - sometimes generated chain of thoughts dont necessary yield correct reasoning which might
    potentially lead to less accuracy.

 Summary:
 ========

   - Chain of thoughts are very effective in large language model with millions of parameters and for
     smaller large models  it is less effective and less practical.
    
