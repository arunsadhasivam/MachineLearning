Chain of Density:
=================

![image](https://github.com/user-attachments/assets/5fff2080-6807-4985-be7e-785a4fa13737)

  - generally used for solving text summarization and range of problems.
  - chain of density is special way to make summarize using llm like chat gpt4 where it starts with
    simple summary and then adds more important details step by step without making the summary longer and sharing.
  - it is packed with useful information ,but still easy to use.
  - this prompting techniques uses smart techniques like making complex ideas simpler combining different pieces of
    information into one, and shortening   text without loosening text without losing its meaning to fit in more
    digits in to same space.
  - Aiming to summary that there are informative and yet pure and clear.
  - so this main goal of this approach is to keep it informative and keeping the summary easy to follow.
  - similar to how human make summary, especially useful for people who need quick and clear information.


How it works?:
==============
![image](https://github.com/user-attachments/assets/47d08385-f700-413d-8a6f-0e4db6f9ffd4)


Step 1:
=======
  - starts with creating a basic summary that includes only few key details.
  - focus on simple and easy to understand.
  - initial summary is not very detailed ,covering just 1 or 3 main points from source material.
    
Step 2:
=======
  - next , the method involves adding more details or entities to initial summary without increasing its length.
  - This means carefully choosing  which new details to include and how to fit them in .
  - making the summary richer in information with keeping  it concise.
  - then to incorporate these additional details, the summary is then rewritten using techniques  like abstraction,fusion
    and compression.
  - this ensures the summary remain the same length but contains more relevant information after each steps.
  - this process repeats for a fixed number of times, each time identitying and adding new and important details
    that are missing in the previous version of the summary.
  - this attractive approach gradually increases the density of information.
  - aiming to strike the **balance between being informative and easy to read.**

    
Example:
========

![image](https://github.com/user-attachments/assets/64209cc7-1095-4515-b96a-4c95a4429585)

- as you can see entity dense summary of the article.
- repeat the following 2 steps 5 times.
- 1st step is identify the information entities
- 2nd step says write a new ,denser summary of identical length which covers every entity and detail
  from previous summary and missing entities.

- add more and more information or entities in to summary.
- hence this technique is chain of density.

Practical use case:
===================

![image](https://github.com/user-attachments/assets/e471ec14-1912-437d-a09e-abf4b1bfec37)

   - this chain of density techniques generate quick comprehension by generating detailed and accessible summary
   - this is ideal for text summarization,news, education and rapid learning context
   - developers can create advanced text summarization tools,aiding readers and swiftly grasping the essence
     of extensive documents.

  
    
Disadvantages:
==============
  
