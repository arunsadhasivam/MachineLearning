![image](https://github.com/user-attachments/assets/1166257a-f6f2-4baa-9208-7afaf2463c01)Adaptation Prompt tuning:
==========================

![image](https://github.com/user-attachments/assets/ae5bc1ea-7131-4f4b-bb0a-57e284b528ef)

  - Adpation or Adpation Prommpt tuning works are taken from original paper - llama adapt paper which proposes this approach.
  - this approach builds upon on **prefix tunings** methods with key addition being 0 gating layer or parameter which
    controls how much impact these soft prompting embeddings have on the attention layer embeddings.

  CODE:
  ====

   - here similar to prefix tuning method, we have to replace the attention layer of base model with
     the adaptation prompt attention layer.
   - we have first attribute as **base_attention_layer**, then we have **prompt_embedding** similar to prefix tunning
   - we have new addition, **adaptive_gate** , which is 0 gating , it is a parameter then it controls how much
     impact this **soft_prompt_embeddings** will have on the corresponding **attention_layer_embeddings.
   - similar to prompt tuning we have **prompt_tokens**.

   - forward pass takes the **hidden state** and related keyword arguments. we first get the output **hidden state**
     and **query state** from the **base_attention_layer** by passing in the hidden_state and the corresponding
     keyword arguments.
   - once we get the **output hidden state** and **query state** lets initialize few variables that we use
     later such as **head_dimensions**  which is **d** and **batch_size** and **query_sequence_length**.
   - next we get the soft_prompt_embeddings, by calling prompt_embedding_layer with the prompt_tokens
     similar to **prefix** and **prompt tuning**.
   - then we get the **adaption**  or adaption key value projections by calling the key layer and
     value layer of the base_attention_layer by passing softprompt embeddings.
    - next we want to get the adaption attention course. this is  QKTR(T) from attention layer computation.
    - once we get the attention course, we do this softmax on the sequence dimension then we get the
      **adaptation gate** parameters multipled with the **softmax scores** to get the **final score**.
    - Now, initializely we see the adaption_gate is initiallize to 0, so initially this course will all be 0
      this is acting as a identity matrix or idenity function for the **attention_layer** here.
    - so, we gradually start incorporating more and more impact from this soft prompt embedding, leading to
      smooth learning.
     - then we can see in adaption output -  we just multipling our scores Multipled (X) by  adaption k projections
       to get the adaption output , then we add the adaption output with our hidden state to get resulting hidden
       state.
    
