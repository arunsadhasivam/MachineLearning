![image](https://github.com/user-attachments/assets/43a1396f-508f-49a6-97c8-e8c67f7eb6b1)Introduction to Understanding Different Prompt Engineering Techniques:
=======================================================================

![image](https://github.com/user-attachments/assets/1445b7f1-21bc-40c5-a386-49df8b8a0bc7)

  - training objective is to predict the next word in sentence.
  - LLM like GPT-3 they are optimized for textcompletion.

Emergent Properties:
=====================
![image](https://github.com/user-attachments/assets/980b6450-6483-4185-92bd-32406a97011b)

  
  - **As these models gets bigger and bigger it starts acquire some  properties inherently
    during training process, eventhough it is not explicitly trained.**
  - one such property is 
    1) In context Learning - 

in Context Learning:
=====================
![image](https://github.com/user-attachments/assets/bd1e3390-b257-4329-b7ee-9a328a823bb1)

![image](https://github.com/user-attachments/assets/79093163-be00-4c88-ba59-7f727d736a54)

  - open AI demonstrated that the emergent phenomenon of incontext learning in the paper
    "language models or few shot learners"
![image](https://github.com/user-attachments/assets/b7b32b58-dcf3-409d-92bc-c280b8a2007d)

What is in context Learning:
============================

  - in Context Learning refers to a new paradigm of learning with the input to the model
    describes the new task with some possible examples.
  - the model output the result of the new task it has just learned from  the context 
    it has just learned from the context it has got.
  - in context learning is a key capabilities of llm, allowing the model to solve
    new set of tasks from just few set of examples or demostrations.
![image](https://github.com/user-attachments/assets/dac9e903-5127-4a2e-814b-68b168bec1b1)

  - for e.g if we give the descriptions of the task, and few set of examples demonstrating the task
    along with unfinished examples to a llm GPT-3. 
  - These models continue the pattern and generate the immediate token that turns out to be a answer.
  - in this case,the model completes the last example.
  - here above i gave the few examples of how this translation should be , finally there was
    a unfinished tasks and it was able to do this without any further context.
  - this is what happens, the learning was happening through the context, there is no 
    gradient update , retraining of model parameters which is not required in this case.
  - model is capable of learning from only from the context which is provided along with the prompt.
![image](https://github.com/user-attachments/assets/e0835f8a-c7ff-43fa-a9bf-1b0856479ca5)

  - this seems to be completely magically.
  - because models like GPT-3 are optimized for text completion, aren't train to solve specific
    problem or task outside of that . but still this model are capable of understanding and solving the
    task at hand when provided with a few set of examples.
  - hence in context learning is known as **"emergent behaviour of llm"**
  - in context learning is one of the most powerful method , because most of the additional tasks
    can be solved when solved with task description and few set of examples.
  - practically speaking, you have got model to do additional things by just providing examples.

Types of In context learning:
===============================

![image](https://github.com/user-attachments/assets/b4fb0982-0c08-4429-b342-7494bf3160bf)

      - Few Shot prompting
      - one shot Prompting
      - Zero shot prompting.


