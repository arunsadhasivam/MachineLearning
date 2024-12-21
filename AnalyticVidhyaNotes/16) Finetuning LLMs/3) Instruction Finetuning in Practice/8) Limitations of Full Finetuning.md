Limitations of Full Finetuning:
================================



  - pretrain on internet data and
  - FineTune on downstream task.
  - finetune of large model has below issues 1) compute 2) storage - tons of gpu.
  - for e.g as we see for full precision llama 70 billion model on 10 downstream task
    280gbx10 of storage .
  - these 2 limiations limit from performing when large models used.


![image](https://github.com/user-attachments/assets/39d53d53-c193-4270-b472-35ddf8668658)


   What Makes model large?:
   ========================

![image](https://github.com/user-attachments/assets/c2d87884-2115-436c-9c23-2f842fc6a5a0)

   1) Number of parameters
   2) Precision of data

below for 7Billion Parameters
1) in Full precision - 7*4=28gb   ( each parameters take 4 byte)
2) in half precision - 7*2 =14 gb ( each parameters takes 2byte)
3) in 8 precision - 7*1=7gb ( each parameter 1gb)


Why Full Fine Tuning is expensive:
==================================

seeing mistral 7B model.

![image](https://github.com/user-attachments/assets/8d440ac5-355a-45c6-b70f-22111d18a22b)


  
