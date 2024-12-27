IA3 and Bottleneck adapters:
==============================


  - IA3 is short for Infused adapter by inhibit and amplifying in the activation.

    ![image](https://github.com/user-attachments/assets/57dee085-6788-4cc8-9544-22c7c6c7b463)

  - here left hand side we see the attention layer , right hand side is the FFN (feed forward network)
  - trainable parameters are expressed in yellow.
  - trainable parameters they perform element wise multiplication between the output projections of the
    key and value lk and lv respectively.
  - input features for the second hidden layer of the ffn block with lfs.
  - in this element wise multiplication , some features can be waited less by these parameters.
    and some features can be weighted more. i.e some features can be inhibited and other can be
    amplified by more weightage. in this way PEFT approaches is able to learn what are the features
    that are important to adapt our pretrained model to the downstream task.


    CODE:
    ====


    ![image](https://github.com/user-attachments/assets/aa71e3a7-f772-44ff-affc-bca9a0fb272c)


  - here define IA3 as a set of trainable parameters with shape f_in (input embedding dimension)
    or f_out.

  - in the forward pass get input feature x , if we are transforming input - we do element
    wise multiplication with input and trainable parameter to get the transformed input
    and then pass to the base layer and return the output.
    else we first get the output from base layer by giving it the input and related arguments and given
    arguments  and transform the output by element wise multiplication with the trainable parameters.

one of the earlies peft approaches are 
![image](https://github.com/user-attachments/assets/ca7f1927-4e57-4cf2-89f0-a4df53adfd02)


 - see sequential bottleneck adapters work. this above block shows  transformer block multi head attention residual
   connection, layer normalization, ffn layer(Feed forward network layer) and then layer normaliation.
 - we inject the adapter network after the multihead attention block, after the feed forward network block.
 - in each adapter network layer , we have following architecture, where in we have down projection layer
    or down projection hidden layer which takes the input features of the dimension d and project them to
   very small dimension k and then do non-linear activation on top of it and pass to up projection layers
   which takes input with k dimension and project it back to the embedding dimension d.

CODE:
====

![image](https://github.com/user-attachments/assets/480edf44-ba18-467c-ba02-2e81b577f50e)

 - here down_proj is linear layer where f_in (input embedding layer) k is small meager dimension.
 - 
