![image](https://github.com/user-attachments/assets/9478e0d5-41dc-478d-856c-89ce4e2d0684)Tokenization
==============


![image](https://github.com/user-attachments/assets/3aad67bb-b21d-44fc-8d88-c2ad16462339)

    - in this lesson we understand tokenization 
    - After data curation ,data pre-processing we need to do tokenization.

  ![image](https://github.com/user-attachments/assets/506f009c-3018-45d0-bb9c-4706eb618993)

  - steps in llm from scratch is 
    1) training data curation.
    2) data preprocessing
    3) tokenization.

<p><details><summary>Tokenization </summary>

  
Tokenization:
==============


 - tokenization is an important step in training llm.
 - it is similar to process we follow while training RNN, LSTM or gru.
 - it breaks down the text in to sequence of tokens i.e "generative ai is fun" is broken down
   in to "generative","ai" ,"is" and "fun". each token is mapped to integer id.

![image](https://github.com/user-attachments/assets/e654cbf5-55c8-4174-a06d-57200eb8da6e)

  - like "generative"-1,"ai"-2 , "is" - 3 and so on 
 - now the list of integer id is passed as a input to llm.
    
    
</details></p>

<p><details><summary>Steps involved in Tokenization </summary>

Steps involed in tokenization:
==============================

 - broadly few steps in tokenization process
 - first steps is to train the tokenizer on training data . this build up the entire vocabularly
   and map each token to the integer id.
 - vocabularly refers to the set of unique tokens present in the trainig corpus, post this we
   apply this we apply this tokenizer on the training data.
 - this step tokenize the text in the training data as per the tokenizer and maps each token to its
   corresponding integer id. this list of integer id is then the data that is ready for us to
   feed us input in our model. that is second step.
 - lets discuss the different types of tokenization steps available out there.

![image](https://github.com/user-attachments/assets/cd95dcd3-1726-47dd-a30f-8889cff76c43)


</details></p>


<p><details><summary>Tokenization Methods </summary>

Tokenization methods:
======================

![image](https://github.com/user-attachments/assets/f03619ac-1117-4530-a158-a3d3321cd559)

1) word -level tokenization
2) sub-word tokenization.
3) character-level tokenization.

pros and cons of each:
======================


<p><details><summary>1)word -level tokenization:</summary>
  
1)word -level tokenization:
============================

![image](https://github.com/user-attachments/assets/b625dd08-45ef-4a01-bdff-132677d3b77e)

  - word level tokenization splits the text in to sequence of words
  - based on individual words like "generative","ai" or "fun" . the break down can be
    puncation based tokenization or based on custom rule based tokenizer or
    space (space based tokenizer).


![image](https://github.com/user-attachments/assets/492c9a55-4345-40f0-ad10-a8e74185e42b)

PROS:
=====
  - relatively simple and efficient
  - as it breaks word to meaning tokens.
    
CONS:
====
  - Massive text vocabularly
  - As we know that language models are trained on massive corpus of data, tokenizing based
    on word level leads to very large vocabularly.
  - dealing with out of vocabularly words - refer to set of words which are not present during
    training phase and occur during inference phase.
  - for e.g consider training e.g above " generative ai is fun"
  - now vocabulary for the corpus will be set of unique words in the training data set.
  - the training data consisting of 2 example with these samples the vocabularly will be
    unique words that represent the training dataset.
   - during the inference phase or test phase, the word **magic** is out of vocabularly word.
   - word level tokenization is inefficient in handling this cruch of words.

![image](https://github.com/user-attachments/assets/e1260af2-69a2-44a1-9408-9b0cd338dd10)

    - let see how to tackle using character level tokenization comes in to play.
   
![image](https://github.com/user-attachments/assets/0ead250f-401a-4536-84da-76c081cd7513)

As you can see in test sentence " Generative ai is magic"

![image](https://github.com/user-attachments/assets/08842a71-5192-4c08-8c5a-c9b1a0aa04b3)

</details></p>


<p><details><summary>2)character-level tokenization:</summary>
  
2)character-level tokenization:
================================

PROS:
=====

  - character level tokenization split the text in to sequence of characters rather than words
  - this enables us to counter challenges with respect to word level tokenization.
  - it reduces the size of vocabularly, as the vocabularly in this case is the unique characters.
    present in training data set , which is very small.

CONS:
====

  - Also handles, out of vocabularly words, since it breaks the text in to sequence of characters
  - however the limiation of the character level tokenization is that break down the text in to
    individual character tokens, as a result learning the meaning representation of the words
    becomes challenging.
  - it also leads to very large sequence of tokens.

    ![image](https://github.com/user-attachments/assets/46ae4b9e-15ea-4b30-a284-8a188a1f1b9c)

let see how to tackle the above cons.    

</details></p>



<p><details><summary>3)Subword tokenization:</summary>
  
3)Sub word tokenization:
========================

  - solves challenges with respect to both character level and word level tokenizer .
  - it breaks the words in to subwords ( individual words or characters) and leverage advantages
    of the both word and character level tokenizer.
  - it works on the priniciple that most frequent words aren't split in to subwords
    rare words are decomposed in to meaning subwords.
![image](https://github.com/user-attachments/assets/d1f8b672-2db7-4f78-af06-0d0e7a60d99c)

      Frequent words     -  NOT split into words
      Rare words         - split in to meaning words

3.1 Different Methods of sub word tokenization Algorithms:
===========================================================

1) Sentence piece
2) Unigram
3) word Piece
4) Byte-pair encoding

![image](https://github.com/user-attachments/assets/a3cacf5d-2447-4605-a050-a50f591b6484)

   1)Byte pair Encoding:
   =====================

     - most commonly used subword tokenization algorithms, while training llm.
     - open llm algorithms like gpt-2 and gpt-3 uses byte level byte pair encoding algorithm.

![image](https://github.com/user-attachments/assets/0d9074af-35db-4ef6-aa91-8c80e189ea53)

   Definition:
   ===========

      - Byte Pair (BP) is a iterative process, where in it starts with individual characters,
        while merging those that are most frequently seen together create a new tokens.
       - Now  lets understand how to create a vocabularly from the training corspus using
         byte pair encoding.

  Working of Byte Pair Encoding:
  ==============================
  - lets consider this e.g where in we have 4 words (low, lowest, newest, widest) in our
    sample training corpus.
  - byte pair encoding works with words and its frequencies. lets compute for our corpus.
![image](https://github.com/user-attachments/assets/226a4a67-9e9c-4563-b477-38b3a1bfc572)

  - for e.g the word low occurs 5 times and so on.
  - now we have the words and frequencies and we can move on next steps.


   Step 1:Add special character: 
   ==============================

      ![image](https://github.com/user-attachments/assets/03069416-66b1-4c98-80ce-839d1bc2fd8e)

    - next we append the special character at the end of each word. this unique symbol
      helps in identifying the word boundaries and distinguishes between subwords situated with in
        words or at the end of the words.

![image](https://github.com/user-attachments/assets/4d828337-a802-49ce-8875-6d900aed60c4)

  Step2: next tokenize the words in to character:
  ===============================================

  ![image](https://github.com/user-attachments/assets/ec050441-55b4-4c38-8607-db4743dc05d8)

  - this will help in initialize the vocabulary
     for the byte pair encoding. as you can see initially the bp consists of 




   step 3: next is initialize the vocabularly:
   ============================================

 ![image](https://github.com/user-attachments/assets/3fbbeb3b-17d9-4506-9885-04e5cb65c858)

  - this will help in initialize the vocabulary
  - for the byte pair encoding. as you can see initially the bp consists of all the individual
   characters present in the corpus as your vocabularly .


  Step 4:Find the most frequent pair:
  ====================================

 ![image](https://github.com/user-attachments/assets/43fd7f81-1cca-42fb-aa91-2491ecec56fc)

 - post that we find the most frequent bi-gram corresponding to the each individual character as token. the most frequent occuring
    pair occurs to be **es**.
   
  Step 5:Merge pair:
  ==================

 ![image](https://github.com/user-attachments/assets/f82f019f-8db3-4de8-803e-d70198489e1a)



  ![image](https://github.com/user-attachments/assets/9e062ee9-161d-41e5-96f4-7ef1506d227b)
      
  - lets merge them in to a single token add to the vocabularly
  -  now that we can see we have added es to our vocabularly.
  -  we have also merged them in our sample training corpus.
  -  this process goes on iteratively  , where in we find the most frequent pair and
     merge it in our token.
  - when we reach the no of merge operation define , i.e vocabulary size that we need to
    have .

Iteration-2:
============

![image](https://github.com/user-attachments/assets/1a13e735-e461-4685-b486-2a7e8a036af4)

  - lets quickly see another iteration. since we have already merged 'e' and 's' in to
    a single token 'es'. in the next iteration we compute the bi-gram by considering the each
    'es' as a single token and we compute frequency.

![image](https://github.com/user-attachments/assets/3f7c80fd-fe22-4f6d-a513-88ac1d44332e)

  - most frequent pair terms to be above screenshot 'es' and 'est'. lets merge them in to
    single token i.e 'es' and 't' are merge to 'est' and add to vocabularly.


Iteration-5:
============

![image](https://github.com/user-attachments/assets/46ae7440-6fab-4d3c-a539-f2e6047dcaec)

    - After 5 iterations, we have 5 newly learned merged operations operations by BP tokenizer and our
      vocabularly is ready.
    - vocabularly size is equal to size of initial vocabularly and plus the no of merge operations learned.
    - this summarizes the entire train process of BP (byte pair encoding tokenizer).
    - now we have successfully trained our tokenizer .
    - next step is to apply tokenizer on training corpus.

Steps involved in tokenization:
=================================

![image](https://github.com/user-attachments/assets/35e95fd3-2d6c-4b5c-b152-cea2e1cbf006)

    - during the tokenization process, BP first split the words in to sequence of characters.
    - lowest - > low, est and then it goes to the vocabularly or the merges and it find the
      first merge operations i.e 'es' is merged  and then 'es' and 't' merged to get 'est'
    - this process continues ,in the end we got 2 subwords   low, est.
    - the word lowest split in to 2 subwords low, 'est'
    
      

</details></p>
