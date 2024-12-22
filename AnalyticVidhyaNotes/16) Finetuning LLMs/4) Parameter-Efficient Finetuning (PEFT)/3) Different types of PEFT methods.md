Different types of PEFT methods
================================

![image](https://github.com/user-attachments/assets/ffa892af-1a23-44de-a021-6dea4b45a353)


Types of PEFT Approaches:
=========================

![image](https://github.com/user-attachments/assets/c8fee4e8-25c9-4ebc-a604-bed60dc53ab1)

1) Prompt Tuning, Prefix Tuning, Adaptation Prompt
2) LORA, QLORA, AdaLORA,LOFTQ,LOHA, LOKR - Reparameterized weights of model in to low rank matrices.
3) IA*3, Bottleneck Adapters - Additive methods (sequential) old


- IA*3 Additive Methods are based on idea of adding Fully Connected network between model layers
- SoftPrompting Approaches are Prompt Tuning, Prefix Tuning, Adaptation Prompt
- Popular and most used approaches are Lora and its Variants(QLORA).


- LORA and QLORA - Idea is to Reparameterize the weights of the models in to low rank matrices
  This reduces the no of renewal parameters while allowing it to work with high dimensional
  parameters of the LLM.


  How to use PEFT Methods in Practices:
  =======================================

  ![image](https://github.com/user-attachments/assets/23374c67-b82e-4bda-a8d0-33d2a6843919)


    - hugging face maintain open source library.
    - it can be used on consumer hardware ( 8gb to 24 gpu)
    - it is interoperable with hugging face ecosystem.
    - more than 100+ contributors
      
