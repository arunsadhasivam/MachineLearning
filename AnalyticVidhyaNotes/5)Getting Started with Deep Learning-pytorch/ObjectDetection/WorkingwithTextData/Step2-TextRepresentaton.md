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
             
   
