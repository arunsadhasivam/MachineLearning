wordEmbeddings:
===============


- word Embeeding is a kind of transfer learning
- vector of car ~ vector of jeep  ( angle of difference between car and jeep is small)
- vector of apple ~ vector of orange 
-  king-man + woman = queen


                |  
       (king)*  |    *---------(man)
            |--|----*   
                |   | queen
                | ------------------------>
               /  
             /      
           /

how to obtain word vector
==========================

 pretrained word embeedings

 - word2vec
 - Glove

 Implementation
 ==============

 Steps:
 ======

 1) Get Data - data
 2) Clean tet data - clean punctation, small letters, junk character removal
 3) Tokenization - tokenize by separating by delimiter( space)
 4) prepare vocabulary - create vocabularly (remove duplicate, sort)
 5) download pre-trained embeddings - load pretrained , 13x300
    where 13 - vocabularly
    300      - each vocabulary length.
 6) Get word vectors.
    
  
         
