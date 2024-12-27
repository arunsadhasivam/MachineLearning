ShortComings of RNN Solve Autotagging using LSTM:
===================================================


- partial derivative of dl/dw depends on partial derviate of ho and ho depends on h1.
- if gradient < 1 (vanishing gradient) then these gradient will almost zero, since which we
  use update weights, the model wont learn anything. The model **cease to learn** as
  update in parameter are insignificant.
- stop learning  - no use of update weights or parameters.


E.g:
====

  First word is (_)  -> predict next word to be writer.
  it will predict only thing if it stop learning.


Approaches: Gradient Clipping:
=============================



1)vanishing Gradient issues are solved using New Approach:
============================================================

1)LSTM (Long Short Term Memory) -> vanishing gradinet problem.
2)GRU.


1)LSTM:
=======


   ![image](https://github.com/user-attachments/assets/13511d80-fd2a-4ab7-ba2b-64fbc6309822)



  h-1 --->  |   |   |-->ct
  ht-1--->  |   |   |->ht

  * bob - nice person
  * don - evil

           let say 2 sentence 
              "bob is a nice person"   |       "dan on the other hand is evil"
                 <--forgot gate}--->            <--- gate 2  sentence 2-->

  Forgot Gate:
  ============

          ft = a(xt*vf+ ht-1*wt)  //sigmoid o/p


          { ct-1* ft =0, if ft=0, forgot everyting }
          { ct-1*ft =ct-1, if ft=1, forgot nothing current}

 E.g.1:
 =======

         Bob is a nice person . Dan on the otherhand 
         +++
         state1
      
         Bob is a nice person . Dan on other hand evil
         ++++                  +++++
       
         Forget gate =0         Forgot Bob ct-1>0 [if ft=1 forgot gate =1]


Eg.2:
=====


      Bob knows swimming
      He told me over phone that he had served navy for 4 yrs


      Both is about bob.

      Input Gate is Quantify Information that important info. Bob workedin **navy** and used **phone** to convey

      it = q(xt*v1 + ht-1*wi) // he told over (phone) served (navy)

      in long term memory 2 things exists
        1) he told over (phone)
        2) served (navy)


        ![image](https://github.com/user-attachments/assets/97504ab2-7975-47f5-b976-80b162dbb397)


Usually LSTM has

1)  three gates - input or forgot gate ,hidden gate  ,op gate
2)  8 weights -> wf,wi,wo, vf,vi,vo


usually sigmoid commonly used in activation 

    tahn -> (-1,+1) to determine increase or decrease in no. of state, hence tanh used instead of sigma
        
