Tree of Thoughts
==================

![image](https://github.com/user-attachments/assets/8e298191-9e05-48fd-9779-44588ef6b1e0)

  - letting them to explore different ideas in order to find solution.
  - tree of thoughts is tree like structure , to look at the many possible paths and choose the best one.
  - this method specially used that needs carefull planning or when first choice can completely affect the outcome.
  - it led the model to think ahead if other options and in need to go back if needed to turn the decision.


how tree of thought work:
===========================

 Step 1:
 =======

![image](https://github.com/user-attachments/assets/764f0ec5-9e91-451d-bef9-93b75e89b74d)

    
Step 2: 
=======

![image](https://github.com/user-attachments/assets/5b83e2fc-1f5d-40ba-b807-2078c78609ee)

 - very first steps is generate multiple thought
 - selecting the most promising to solve problems.
 - so this allows the language model to explore the different reasoning thoughts.
 - organizing the thought in to a tree structure , where each branch represents a possible solution
   or step towards solving a problem.
 - Then the tree of thoughts works by generating multiple thoughts as intermediate steps which are
   coherent units of text that guide the model towards the final decision.
 - it enables to consider various options and outcomes before making choice.
 - this framework employs search algorithm like DFS and BFS and allows the model to systematically
   explore and evaluate its thoughts , deciding which path to follow based on potential success or
   reaching the solution.
 - Tree of thought enhances the problem solving abilities by enable the model to perform deliberate
   decision making.
 - Go ahead and backtrack if needed, making it more effective for task that require strategic planning.


Different between tree of thoughts and chain of thoughts:
==========================================================

![image](https://github.com/user-attachments/assets/bd24c3c7-1e89-4d9f-a486-745eed96fed5)


  - chain of thought prompting , thought process moves in a single directions.
  - in tree of thought, the thought branches out into multiple  parts.
    
  - chain of thought also generates a sequence of thoughts, whereas
  - tree of thought consider different sequence to derive the best outcomes.
  - tree of thought can also reverse or change its reasoning paths if they dont
    lead to a solution. this flexibility not present in chain of thought.

SNO   |  chain of Thought                                                                     | Tree of Thought
------|---------------------------------------------------------------------------------------|-----------------------------------
1     |chain of thought prompting , thought process moves in a single directions              | in tree of thought, the thought branches out into multiple  parts
2     |chain of thought also generates a sequence of thoughts                                 | tree of thought consider different sequence to derive the best outcomes
3     | cannot reverse decision                                                           | tree of thought can also reverse or change its reasoning paths 

visual difference between chain of thought and tree of thought:
================================================================

![image](https://github.com/user-attachments/assets/d13797d4-148a-4827-9909-abf2a805f8de)

- as you can see zero shot or one shot of future prompting.
- second image is go through the multiple thought process
- whereas in chain of thought  between input and output, we go through multiple different processes,
  and at each thought process, we evaluate the two processes, whether it is positive or negative thought.
- if we come across a negative thought, we discard that reasoning part. And then we go through the
  positive thought processes and eventually get the output.
- 

![image](https://github.com/user-attachments/assets/f8df5207-61a3-43cd-ac65-a9ca6cfd85d4)

above is eg of tree of thought processing.

- above is creative writing task.
- input is 4 random sentences and output should be coherent as such with 4 paragraphs.
- end in the four input sentences respectively.
- such a task is open ended and exploratory and challenges creative thinking and high level planning.
- input " write a coherent passage of 4 short paragraph . the end sentence of "
- based on this input , then we build a tree of thought with depth =2 and only 1 intermediate third step.
- the language model first generates five different paths and then votes for the best one
- similary generate five messages based  on the base blog then vote for the best one.
- here breadth limit = 1.
- as only one choice is kept  per step and simple zero  shot would prompt.
- that is analyze,the choice below and then conclude  which is most promising for the instruction is used to
  sample five votes at what steps.
- based on zero shot prompting , we evaluate all the different plans , out of the five different plans,
  2 plan is generated as output.

Pros:
======

![image](https://github.com/user-attachments/assets/2890ede7-b6a2-42e0-985e-115e16e3db60)



Cons:
=====

![image](https://github.com/user-attachments/assets/2ac471e4-31da-443c-b75a-fe9547dcbc73)

 
