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
  - in tree of thought, the thought branches out into multiple  parts
  - chain of thought also generates a sequence of thoughts, whereas

SNO |      CHain of thought                                         | tree of thought
----|---------------------------------------------------------------|-----------------------
 1  |   Prompting thought process moves in a single direction       | thought process branches out in 
  2  |      sfda   
     | adf
    |                                                               |a
    |                                                               | 
