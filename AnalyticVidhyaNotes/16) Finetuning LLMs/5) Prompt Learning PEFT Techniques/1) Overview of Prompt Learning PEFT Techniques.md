Overview of Prompt Learning PEFT Techniques
===========================================


![image](https://github.com/user-attachments/assets/3e120ca0-8b9a-4bfd-9684-3da848d86f30)


- Prompt Learning Methods are also called Soft Prompt Based Methods.
- Prompt Learning Methods map the problem of finding **discrete hard prompt to continuous
  soft Prompt**
- learning in previous courses, how capable zero-shot prompting and few shot or incontext
  learning based methods or approaches. however when there are lot of training examples
  available optimizing the discreate natural language prompts becomes challenging.


Solution:
=========

  - we solve here by instead of optimizing the discrete natural language prompt, learn them
    by introducing trainable prompt tokens or prefix token and prepending them to
    input embeddings or intermediate hidden states during fine-tuning.
