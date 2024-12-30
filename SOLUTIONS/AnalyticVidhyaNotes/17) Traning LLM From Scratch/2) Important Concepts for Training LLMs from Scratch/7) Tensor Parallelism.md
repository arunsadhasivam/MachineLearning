Tensor Parallelism
======================


![image](https://github.com/user-attachments/assets/e870b8e0-bab0-4fb3-9bcd-a1b0cb2c76a3)

    
  - matrix operations are the heart of deep learning, serve as a mathematical foundation
    for the ability to learn from data.
  - particularly in the context of neural network, data is technically represently and
    manipulated in the form of matrices.
  - core operation involves matrix multiplication, addition and other linear algebric
    operations.
  - whether it is **dense layer or self-attention layers in transformers , all are
    driven by matrix operations**.
  - question is can we paralleism of the **matrix multiplications or matrix operations** that exactly
    tensor paralleism does.


    Tensor paralleism:
    ==================


    ![image](https://github.com/user-attachments/assets/81f10b0c-1cea-4593-adae-09b95537555f)


    - In tensor paralleism, the computations happening in the model are split across multiple gpu.
      each gpu process only computes the slice of the tensor and then aggregate the full tensor for
      the operations that require the old output.

![image](https://github.com/user-attachments/assets/e49dd335-75e4-452d-8533-387da3c8102a)

    - here is the illustration , how matrix multiplication can be parallelised across multiple gpu
      in a fully connected layer.
    - the second sub-block of the transformer block is a fully connected layer followed by non-linear
      activation say RELU. we can compute by writing y=Gelu(X*A). x is input matrix and A is weight matrices
    - with tensor we can efficiently compute in parallel, either rowise or columise. this gives raise to
      2 types of tensor paralleism:
      1) column paralleism - we split the weight matrix in a column wise fashion - matrix A is split in to 2 partition
                             where A1 is the first column and A2 is the second column of the weight matrix A .
                             we compute the matrix multiplication of X*A1 to get Y1 and X*A2 to get Y2 and then
                             concatenate to get the Y. As you can see in above screenshot.
      2) row paralleism  -  similarly we split in row wise fashion. where A1 matrix has first 2 rows and
                            A2 matrix has next 2 rows , first 2 colums of x and next 2 columns of X 
                            x1*A1 and x2*A2  to get Y1 and Y2 as earlier. finally concatenate to get Y.


Transformer layer:
==================

![image](https://github.com/user-attachments/assets/06d66e93-5da1-4214-8d02-a4036c77930e)


  - Transformer layer consists of self-attention block , which is followed by a 2 layer multilayer perceptron block.
  - we first see by detailing the tensor paralleism in the mlp block. here we can see in above screenshot, we
    first have input matrix x in the first hidden state or the first mlp layer we want to compute Y which is
    equal to GELU applied on top of the matix operation with in input matrix X and with weight matrix A.
  - here B first partition the matrix A in a column-wise fashion across the accelerated raters across the GPU.
  - if you 2 gpu as shown , we will partition A in column wise fashion such A1 has half and A2 has remaining half
    of the column.
  - Next the way these function f during the forward pass is of identity operation , i.e it just copies x on each
    of the GPU.
  - Then the input matrix X is multiplied by A1 patition and RELU is applied on top of it without the need of
    synchronization reducing the computation overhead to get Y1.similarly x is multiplied by A2 partition to
    get Y2 output.
  - now in the second MLP layer ,the compuation is this variant where in we want to compute Z which is dropout
    applied on top of Y *  weight matrix B.
  - here the matrix Y1 and Y2 are the column partitions , here B partition the weight matrix in B1,B2 in row wise fashion,
    where in B1 has half of the row and B2 has next half.
  - next we multiply Y1 partition with B1 (Y1*B1) and then we multiply Y2 with B2(Y2*B2) to get Z1, Z2.
  - for the dropout we need to synchronize the entire output.
  - thas what happen in G function. where in is an "All Reduce Collective Operation" adding Z1 with Z2 (Z1+Z2)
    dropout is applied then we get output matrix Z.
  - in this way we paralleise the computation of these matrix operations or computations across GPU where in
    we reduce the memory requirements by partitioning the weight matrix A and B , at the same time compute
    the things in parallel with only one synchronization point here(G) there by reducing the compuation overhead.

Multi head Attension Paralleism:
================================

![image](https://github.com/user-attachments/assets/627944c8-229a-4c5d-856a-5c59473fc03a)

   - similarly we can parallelise the multi-head attention layer.
   - Multi-head attention layer is much simpler , since they are inherently parallel due to having
     multiple heads.we can see the attention heads for layers of the query (K,V) are already
     having these multiple independent heads such as (Q1,Q2) which are column partitions and we can
     just parallelise on this.
   - As you can see in previous topics, when we want to compute Z which is dropout applied on the
     matrix multiplication with B. we are pattitioning the B in a row wise manner and computing
     Z1 and Z2 and then performing **All reduce Operation**  to add them before applying dropout.
   - in this way we apply tensor paralleism to shard the weights metrices across the accelerators
     i.e across gpu to reduce the memory requirements.   hence memory efficient and try to
     compute things in as much as parallel manner as we can their by reducing the computational overhead.
