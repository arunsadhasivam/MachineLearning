LoRA and its variants:
======================


      - most popular and widely used PEFT approaches
      - LORA stands for low rank adaptation.

  ![image](https://github.com/user-attachments/assets/b791ae7e-89ce-4d26-989c-609db270000c)
   
   - This figure how LORA works and its taken from the paper 
   - Pre-trained llm model observed to exhibit the instrinsic low dimension.
   - Based on this observation, the authors of the LORA paper mentioned that during
     fine tuning the weight update(deltaW) also should be instrincly low rank.
   - As such they parameterized delta weight(DW) in to a low rank decomposition with
     matrices B and A that are shown here in orange.
   - Matrix B is having the shape of the DXR and matrix A has shape of RXD
     here D is embedding dimension and R is the rank.
     here Rank represent the rank of the low Rank decomposition DW update , which is
     learned during fine Tuning.
   - low rank matrix B and A only these are learned during fine tuning. whereas
     the entire pre-trained model backbone which is represented here in blue is
     kept frozen i.e it is not trained this drastically reduce the computation requirement
     to fine tune the model.
   - now we know how LORA works and idea behind it.

   
CDOE:
=====


![image](https://github.com/user-attachments/assets/63f1d6f9-4413-4a1b-b554-0ffd7ffcbbf6)


    - input dimension R and out is fout.
    - forward pass - input x is  given along with the related arguments and keyword arguments.
      we get the LORA output , we give the input .

Great feature of LORA:
======================

      - Another great feature of LORA is that during inference , there is no additional latency.
        you train your LORA weights during your fine tuning phase and then merge our LORA
        weights in to the base model and use it as standalone model.

![image](https://github.com/user-attachments/assets/647620d8-319b-492a-8e2d-a49f373b2189)
        
    - what we mean by this is:
    - we have B, A low rank matrices that are fine tuned. to represent this W(x) X 
      h= wx+BAx and h= (W+BA)x since x is common. now you can directly add this
      to get the W merged. once you do ,you can do normal inference of the
      model where in you don't have the latency introduced by additional multiplications of
      B,A,X. in this way there is no additional latency.

     - now look at LORA variants.     
![image](https://github.com/user-attachments/assets/c804c0c4-de70-41b4-90ea-4e2569ca4873)

     - ADALORA - Adaptive budget allocation such that important layers having high rank
       (more params) while prune less important.

LORA fine tuning cost:
======================

![image](https://github.com/user-attachments/assets/cbb3e5dc-076d-44ea-864d-c6d72c29c6e3)


    - we already saw fine tuning cost for Mistral 7 billion model with mix precision of adam optimizer is
      112 GB without even considering the memory requirements of intermediate activation.
    - here using mistral 7B model -14 GB
     
