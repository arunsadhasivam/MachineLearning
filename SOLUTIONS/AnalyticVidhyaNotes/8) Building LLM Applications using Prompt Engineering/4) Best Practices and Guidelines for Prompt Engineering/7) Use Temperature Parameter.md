Use Temperature Parameter:
==========================

- temperature parameters do is :
- it essentially tells the model that how you treat randomness.
- you seen that how llm works, it is trying to predict the next word, then there are
  multiple options.

temperature is low:
======================

- if you want the output to be **deterministic then output to be low**
  the model creates the very similar output every time.
  lets say i am trying to generate 10 grand names . so i am deliberately using
  using different case study.
- in the case i am using a case study , for a brand name for a e-learning company in datascience.
- when i use temperature = 0.
![image](https://github.com/user-attachments/assets/ff507850-2839-4fcd-a6e2-74a329226cc6)
- irrespective how many time i run , the output is very similar .  
- this is because i set the randomness to be close to 0.

temperature is high:
======================
![image](https://github.com/user-attachments/assets/c1b46332-f49d-4e00-8605-fa307e35b2af)

  - now set the temperature to 1.
  - now run the same prompt again , it gives the different set of output which is not similar to earlier.
  - dependending upon the application you want.
  - if you want more exploration, you dont want to be restricted to most probabilistic output , you can use
    the temperature and let the model explore in a more open manner.
  - it is very handy trick which comes specifically, when you are look at the model to brainstorm a few ideas.
  - those are some of the tricks or experience which helps us to have better prompt.

Summary:
=========
![image](https://github.com/user-attachments/assets/c0f52e02-b77e-4431-a68c-d8ad0db403b5)

  1) make sure your prompt are clear and specific.
  2) any time add specific examples, so that it learn typically lot more than provide few more parameters.
  3) you should vary the prompt and iterate to get the final prompt.
  4) use delimiter to make sure the model can understand the input.
  5) ask the outpupt in the structure output.
  6) as required, set the temperature to 0(same answer for each run) or 1 (non-deterministic), 

  - these are some of ways in which you can actually make your prompt a lot better and get better output from these llm.
