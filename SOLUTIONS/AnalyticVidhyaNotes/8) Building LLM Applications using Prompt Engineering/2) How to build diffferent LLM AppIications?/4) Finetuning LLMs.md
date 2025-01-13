Finetuning LLMs:
==================

  - this method will help us to tackle the challenges which we face with RAG.


why FineTuning LLM:
====================

![image](https://github.com/user-attachments/assets/29d4b5d1-8db3-4bce-825e-2cc1796b2372)


- pretrained llm like gpt-3, llama2 etc are trained on large scale internet dataset when applied on a specific task
  or our own dataset it can still do the job for us but might not be as good as one with fine tuning.
![image](https://github.com/user-attachments/assets/557e56f1-946f-4c4b-8384-85dee1aebde9)

- for e.g when i ask question like "how do i play and swing cricket ball" to a **pretrained llm** answer " play straight"

![image](https://github.com/user-attachments/assets/aa2427f9-397d-4278-945f-a42a38145a8f)

- when same question with **fine tune llm** trained on cricket book the answer is - "keep play shot close to body, play straight"
- actually fine tuned model giving me lot better model.
- Reason is that fine tune llm adopts the parameters and domain of the pre-trained llm completely to our
  specific domain that we are trying to get the output.
- hence specific domain knowledge will be incorporated in to the model like in our case "cricket"
