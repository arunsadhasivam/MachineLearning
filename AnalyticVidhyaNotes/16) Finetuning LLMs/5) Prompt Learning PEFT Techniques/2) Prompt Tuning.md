Prompt Tuning
=============

![image](https://github.com/user-attachments/assets/fc54a5e1-94b2-4f38-a1b1-df1d1cf1d816)


- how prompt tuning works and taken from original paper which develop this method.
- left hand side it first shows the full finetuning or model tuning approaches
  and compare with the prompt tuning approaches.
- you can see pre-trained based model has 11 billion parameters and 3 downstream tasks(TaskA, TaskB,TaskC)
- here in full fine tuning, each of the fine tuned models where each of every parameter trained has
  11 billion parameters similar to the base pre-trained model.
- in full precision , each fine tuned models would take 44gb of storage. three models combined
  would consume 100GB in storage itself.Models here would require 10 to 100 of GPU
 - Now to contrast with the Prompt Tuning based method, here we can see only tiny fractions of
   soft prompt tokens or soft prompt Embeddings are being learned . here in the fine tuning process
   for each batch we get the input embeddings , we prepend the soft prompt token embeddings and
   then passed on to the pre-trained based models to get the prediction . Based on predictions
   and lables we get the loss. we back propagate the loss to get the gradient of loss with respect
   to soft prompt embeddings and then we update the soft prompt embeddings.
- This whole fine tuning process on each of the downstream specific datasets
  to get downstream tasks specific soft prompt embeddings.
- These take very minimal storage in terms of KB as oppose to 44gb.
- here we see how prompt tuning helps to drastically reduce the storage requirements from 44gb to KB's.


  CODE of pytorch:
  ================

 ![image](https://github.com/user-attachments/assets/db551426-9d46-45e8-bd53-822479864a64)


  - we have looked how prompt tuning method works now code below.
  - here we call class PromptTuningModel which takes input base model,no of soft prompt token interested in,
    input dimension embeddings, batch size.
  - we assign base model attribute to the provide pre-trained base model.
  - we will have this prompt embedding attribute which is an object of embedding layer which has
    num_prompt_tokens , no of tokens/embedding dimension.
   - here prompt token is 2-D matrix which has 
       1-D - having batch size
       2-D - having num_prompt_tokens
  - during the forward pass , it takes the input embeddings and other parameters to the  base model.
  - here we first compute the soft-prompt ,
      1)now here we get the soft prompt embeddings . 
      2)to got the soft prompt embeddings we pass the prompt tokens which is nothing but sequence from
        or list from 0 to num_prompt_tokens-1.
  - it is repeated path size no of times .
  - we provide this to prompt embeddings layer and we get soft prompt embeddings(TaskA,TaskB,TaskC).
  - we need to prepend to input embeddings. 
  - now we get the updated embeddings , we pass it to the base model along with other keyword arguments.
  - this predictions can be used to compute  loss and backpropagation is done to get the gradient of
    loss with respect to soft prompt embeddings. prompt embeddings are then updated using the
    optimizer. thats why you learn prompt embeddings.
  - now you see these paramters are  **trainable and rest of the parameters and whole base model
    is kept frozen**. in this way computation requirements are drastically reduced.
   - when you save the model , just need to save the prompt embeddings.
   - The rest of the things are already saved and they are not specific to this prompt tuning method.
     in this way save on storage and compuations.
  
    
