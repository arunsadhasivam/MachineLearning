Forward Propagation:
======================

how RNN function 
=================

forward propagation in training.

![image](https://github.com/user-attachments/assets/f5ad0b8a-5b52-4531-8091-dac0374e66fd)


- hidden state(ho,h1) -> is a function of previous function i.e h1 = g(w.ho+uk1)


Back Propagation:
=====================


![image](https://github.com/user-attachments/assets/a634dd92-e49c-4ac2-a36f-bf1f31714f2e)

- loss calculated at final timestamp(y-y^)
-  partial derivative of Loss/Partial derivative of dv
-  weights matrics with respect to w(weigths),u(input),v are updated i.e weights

Note:Not feed forward n/w
==========================

- RNN has memory or feedback, since it needs to recognize the sequence , hence it is not a feed forward n/w.

