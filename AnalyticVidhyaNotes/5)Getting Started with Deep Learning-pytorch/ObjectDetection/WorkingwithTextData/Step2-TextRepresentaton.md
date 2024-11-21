Step 2- Text Representation:
============================

1.one hot Encoding:
===================

   - convert text data numerically since ML Model almost all dont accept text
   - E.g " I have three dogs"
     encodes to  [           [  
                   1            0
                   0            1
                   1            0
                   0 ]           0 ]

     Vector carrries semantic information.


  Usage:
  ======
  
  1) text cleaning
  2) tokenization
  3) vocabulary preparation
  4) one hot encoder vector

 Raw Text           |      cleaned Text(removePuncation)           | Tokens
 -------------------|----------------------------------------------|--------------
  The ball is pink. |     the ball is pink                         | the,ball,is,pink
  pass the juice.   |     pass the juice                           | pass, the juice
  The Book is good. |  the book is good                            | the , book, is ,good
             
   
one Hot Encoding Limiations:
============================

one hot encoding do not capture any context , it has details of only word.

e.g

1) "the bus is running late"    
2) "the train is running late"

above e.g one hot encoding is

 bus   - [0 , 1, 0 , 0 , 0]
 train - [0,  1, 0,  0 , 0]

 in above no details stored, it has no data or details of context( bus or train) like above 
 difference is wrods in sentence (bus or train). it does not store any context bus and train.
