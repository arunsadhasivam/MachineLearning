Evaluation:
===========

![image](https://github.com/user-attachments/assets/99f12287-eec4-409a-8870-80aa87911328)

WAY 1: HUMAN:
============
    - Next step in fine TUning is important evaluation is goal standards to properly gauge the 
      model capabilities.
    - screen shot is arena leader board , where user chooses a model as winner based on the 
      users yellow ratings.similar to way player are ranking.
    - this gives the hollistic view (leader board) on the model that are very helpful, honest
      and harmless based on human interactions with them.

WAY 2: GPT-4 Models:
=====================

![image](https://github.com/user-attachments/assets/c99cab28-926d-4365-982c-0c1b92fb7eec)
      
     - Another way is to use powerful model such as GPT-4 . this is gaining popularity
       but it has own set of bias. for e.g gpt-4 model evaluations are skewed towards synthetic data 
       or it prefer longer generations.

WAy3:LLM BenchMarks:
====================

![image](https://github.com/user-attachments/assets/e6606641-ad8f-4112-a854-8148545adeed)


    - Another way to evaluate model performance is to how well they fair on established benchmarks
      such as MML-A,GSM-K, hellaswag.
    - This should be consider as noisy proxy and useful to gauge the generic capabilities of the model.

![image](https://github.com/user-attachments/assets/ce637eb6-b2b0-4cf5-a199-e53e4f0a44ee)


    - As you can be finetune for own use case such as only for summarization,making certain functional calls,how to behave
      as a agent, how to generate json output based on given instruction and so on.
    - In order to properly evaluate your model, you must create our own tasks specific to test suite.
    - The test suite for specific tasks, ensure our evaluating the performance with respect to the final real world
      problem in mind.
    - This often involves, thorough error analysis and then coming up with automated test to ensure the next iteration of 
      fine tuning solves that types of failure.
