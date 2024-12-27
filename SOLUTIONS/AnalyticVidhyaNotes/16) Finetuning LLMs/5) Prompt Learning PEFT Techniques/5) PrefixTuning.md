Prefix Tuning:
================


  - another softprompt based method.

![image](https://github.com/user-attachments/assets/36084275-a4dc-4ca5-993b-ed87328bf4e7)

  - task to take input which is tuple of tokens with knowledge base which includes relationship
    between entities e.g harrypotler and hogwards has a relationship of education between them.
  - task is to natural language utterances which encapsulates the relationship between the entities.
  - i.e for this e.g "harry potler is graduated form hogwarts"  is the output utterance.
  - given this task , that we want to finetune the base model e.g GPT, we will see how prefix tuning
    can be used.
  - here you can see given the attention layers, these are hidden state , these are input hidden state
    ,these are hidden state of target utterances. we will be prepending soft prompt embeddings this is
    similar to prompt tuning with the difference that here the prompt embedding are in each of the
    attention layers of the model. for e.g if GPT has 16 layers, each layers we have learnable, or
    trainable prefix prompt embeddings. now that we have gone over the theory.


CODE:
=====

![image](https://github.com/user-attachments/assets/9afd1768-9cba-4a95-a60f-6694eb08cd62)


  - in each attention layer , we have learnable prefix token, we will be creating a attention layer
    called **prefix tuning attention layer** and will be replacing all the attention layer class in our
    modelling code with this **prefix tuning attention layer**.
   - here our first attribute is **base_attention_layer**  we will taking that as input for the
     init_function() and second attribute is prompt_embeddings  these are the trainable parameters
     that are learning during fine tuning . here it is a object of embedding layers with num_prompt/embedding
     dimension. and similar to prompt tuning we have **prompt_tokens**.
   - during the forward pass, we get the hidden state from the previous attention_layer and the related
     keyword argument.
   - first we get the soft prompt embeddings, by giving prompt embeddings by giving the prompt_tokens to the
     **prompt_embeddings** clear to get the **soft_prompt_embeddings** and then we concatenate the **soft_prompt_embeddings**
     to the hidden state along the sequence dimension to get the updated hidden state.
   - then we use the updated hidden states and then give that as input to **base_attention_layer** with the
     relative keyword argument.
    - this is how implement prefix tuning.


