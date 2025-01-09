Chain of Symbol:
================

![image](https://github.com/user-attachments/assets/8690d48c-ae82-49c2-9bf5-53a9aebc23e2)


  - this prompting is generally used for planning tasks.
  - helps language models understand and plan things by replacing long descriptions with easy symbols.
  - this approach involves 1
    1) making the language model guess the solution in simple steps
    2) fix the mistake in the case
    3) finally, replacing the detailed descriptions with symbols that represent
       spatial relationships , making it easier and quicker for the language model to process.
 - by using the symbols to represent the relationship between the objects
 - chain of symbol prompting techniques make it easier for these language models to understand and
   solve problems that involves figuring out how objects are arranged, leading to better performance
   for tasks that require this thinking.

how it works?:
==============

    - it starts by making language model by guess the solution in simple steps which is a way to 
      break the complext task in to easier parts.
    - after a initial guess, any mistakes in the language model solutions are corrected to ensure accuracy
      which helps in refining the process and making it more reliable and 
    - finally detailed descriptions of spatial relationships are replaced with symbol simplifying the
      information and make it quicker for language model to understand and process , thus enhancing efficiency.

Example:
========

![image](https://github.com/user-attachments/assets/6be8e618-a083-4a8a-ba33-10d6f407c4df)


    - compared chain of thought with chain of symbol technique
    - input is planning question " there are a set of bricks . the yellow brick C is on top of brick E...."
    - how we use few shot prompting where give some examples . this is how prompting looks like 
    - bricks from bottom to top are produced
    - output of model is not corrected
    - in chain of symbol , instead of long description we have symbols
    - like B/A/D/E/C
    - finally the result is correct.

Practical use:
==============
![image](https://github.com/user-attachments/assets/715fabc3-c0f4-4ccc-a3ee-16700f7e1be6)

    - enhance the spatial problem solving
    - facilitation tasks like navigation and route planning.
    - utilizes symbolic representation conserve time and computational resources
    
      

