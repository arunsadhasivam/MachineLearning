Training:
=========

1)Understand model training happens:
=====================================

![image](https://github.com/user-attachments/assets/a46ed443-a8fb-4a5e-9866-49be414456f4)

 

The things to consider is:
  - hyperparameters
  - saving checkpoints
  - evaluation on an evaluation dataset
  - compute requirements and hardware
  - Tracking Experiments using tracking framework like wonb, tensor board
  
below is the minimal pytorch training loop code

![image](https://github.com/user-attachments/assets/08ed87c1-4fdc-4161-bc72-366162801948)


Training and inference at a scale:
===================================

     - however working directly in pytorch is daunting as it often involves lot of boiler plate code.
     - looks at how hugging face project like Trainer API and accelerate  to alluviate the problems and
       make training breeze.
    


![image](https://github.com/user-attachments/assets/93bdee3c-186f-4ef6-870f-3039364dec29)
![image](https://github.com/user-attachments/assets/4a734f8c-7271-4e0d-b6e0-298ea3bec760)

<p><details><summary>Trainer API</summary>
  
Trainer API:
============

   - Trainer API is very high level abstraction.
   - it does not need any boiler plate code like checkpoints,logging,aswell as considering nuances of different
     distributed strategy.
     
</details></p>

<p><details><summary>Accelerate  API</summary>     
  
Accelerate API:
================

    - Accelerate Trainer another way to have training and inference at scale.
    - use this when you want to have more control over pytorch training loop
      and same time avoid boiler plate code related to 
      1) Different distributed set 
      2) different parallelization strategies
      3) different devices
      4) different data loaders
      5) different tracking frameworks and so on.
      
Summary:
========
      
      These high level frameworks make training simple , scalable and as well as expandable.
</details></p>
