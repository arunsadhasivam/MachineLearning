2D and 3D Parallelism:
=======================

![image](https://github.com/user-attachments/assets/6f2d0406-b56e-4451-9a60-a6761ceb9ae2)

  - in this lession we learn 2d and 3d paralleism.
  - so far, we have discussed different paralleism techniques such as dataparalleism where in
    each gpu has own model copy, where in each gpu gets its own different sub-batch of data.
  - in model paralleism, the model is sharded across diferent gpu
  - in pipe parallism, it overcomes the limitations of simple model paralleism by effectively
    use the GPU.
  - then we look at the fully shared data pipeline in which it optimizes the state, gradient and
    as well as model parameters are sharded across the gpu and it also uses the data pralleism.
  - then we looked at the tensor paralleism, matrix compuations are executed in parallel across
    multiple gpu.
  - each techniques offers advantages and has its own limitations when training large language model.
  - instead of completely relying  on 1 single strategy, can we combine and leverage the advantages of
    these different strategies to train the llm efficiently at scale. thats why 2d and 3d paralleism
    does.

2D and 3D paralleism(mix):
==============================

![image](https://github.com/user-attachments/assets/2af96565-8532-415f-b566-7203f479cf17)

  - in 2D and 3D paralleism, we combine the **data paralleism** along with the **pipeline paralleism** to leverage the
    advantages of the data and model sharding.
  - the data as well as model is sharded across multiple gpu and model training takes place.
  - this way we are able to train the llm efficiently at scale.
![image](https://github.com/user-attachments/assets/4c52021f-0407-4aa1-804d-b774968fbe0e)

  - similary , to get an even more efficient training an 3D paralleism is used where in pipeline paralleism
    is combined with tensor paralleism i.e model paralleism along with data paralleism i.e zero-data Parallel.
    by this way we can leverage the advantages of different paralleism techniques. this helps to accelerate
    the training process and train the model efficiently at scale.
 - most of the llm like falcon 180b, llama 80B uses 3D paralleism to accelerate the training process of these llm.
 - mostly 3D paralleism preferred for **very large language models**  
