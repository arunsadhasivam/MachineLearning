Data Parallelism
=================


  - in this lesson we understand the data paralleism and see how it accelerate the training process
  - llm are trained on massive scale dataset containing 100 of billions to trillions of token.
  - it would take for ever if we train on single gpu, thats where data paralleism comes in. 


![image](https://github.com/user-attachments/assets/e1cf002d-1f8b-4bd1-8e3b-fd49b0f63fb0)
![image](https://github.com/user-attachments/assets/ce1cc058-7f15-4c10-9c13-a4bd87c0be2e)

![image](https://github.com/user-attachments/assets/f88dcf13-94c6-49a5-8e3b-3cfd689086ed)

  - it solves this challenge by distributing the training data on multiple gpu and running the model
    training on parallel.
  - it first , lists the training data that is given batches to sub-batches and each of which is
    put on a given device, that is on a given gpu.

 ![image](https://github.com/user-attachments/assets/741ba377-fec7-46d8-bedd-d11118e62fe9)
   
  - then the model is also copied on  each of these devices. the given sub-batch is run through
    the model in the forward pass and in backward pass the local gradient are computed corresponding
    to the local sub-batches that each device has.

    ![image](https://github.com/user-attachments/assets/11d65139-5757-40d8-8432-1b86fc856d51)

  - we can see that the local gradients , gradient1,gradient2, ... gradientn corresponds to the
    sub-batch1, subbatch-2, ... subbatchn . once we have this we compute the global gradient
    by aggregating or averaging the local gradients.
  - here all reduced collective operation is performed, post getting the local gradient
    each of these devices has same values of these global gradients. now these global
    gradient is used to update the model weights via the optimizer step.

    ![image](https://github.com/user-attachments/assets/e8d6212c-e954-43a1-a9fe-667bcead60ac)

  - once that is done , each of the model copies will have again same updated weights.
    in this weight you are able to train the model in parallel and to consume larger batch
    sizes.


Pros:
====

![image](https://github.com/user-attachments/assets/c3e2e965-40a2-48ee-8239-e7538aa2b021)


    - it increase computer efficiency , now you are getting the very larger batch size compare
      to what you get using single gpu.
    - relatively easy to implement.


cons:
=====

  - memory inefficient that is it does not reduce the memory foot print per device.
    i.e if model with more than 1 b parameters will run out of memory even in a
    single gpu with 32gpu . thats where model paralleism comes in to picutre.
    
    
