Hands on - Training BPE Tokenizer
==================================

   - previous lession we learned that how to scrap, create pre-process, de-duplicate domain
     specific dataset.
   - in this lessson we see how to train your  own byte-pair (BP) tokenizer


Tokenizer.py:
==============


  ![image](https://github.com/user-attachments/assets/b3f6accb-c462-45b6-ad92-c78584a0ed83)

  - create blue print base tokenizer -(star coder) blueprint page tokenizer because aim to train our
    own code base llm , our own domain specific dataset.
  - dataset_name  : **hug_stack** this is where folder where we pre_processed dataset from earlier process.
  - tokenizer_name : hug_code : any other name also fine.
  - last step is :  whether to push to hub or not.
  - next we get the base tokenizer and base vocabulary , we do byte level encoding .
  - in this initial vocabulary is **limited to 256 tokens and there is no concept of out of vocabulary tokens** because of it.
  - after that we load the dataset and hugcoder dataset.
  - we get the train split and load in streaming mode and iterate over it which is batch iterator. at a time
    iterate over a batch of size 10 and then it needs those batches and that is then given to tokenizer.train_new_from_iterator()
   - we get new_tokenizer and then save it
   - finally decide whether to push it to hugging face or  not.


  command:
  =========

  ![image](https://github.com/user-attachments/assets/b2e68877-37c8-4e87-988c-faa20dc7e115)


  - doing preprocessing process
  - tokenizing
  - count pairs
  - compute merges
  - final vocabulary size is 49725
 ![image](https://github.com/user-attachments/assets/e5baf726-888d-4ac0-9c8e-209c1409a705)

  - tokenizer.json or config we have this specific special token related to code and vocab size is 5000
  - have merge operations, vocab has also vocabulary.

![image](https://github.com/user-attachments/assets/a9ea2458-a129-4035-a474-d3837060f0c2)
