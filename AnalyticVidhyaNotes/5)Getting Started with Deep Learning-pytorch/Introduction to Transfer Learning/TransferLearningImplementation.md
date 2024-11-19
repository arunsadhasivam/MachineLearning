
Modules:
========

VGG16, Imagenet Pretrained Model.


Solving Challenge Using Transfer Learning:
===========================================

- Pretrained VGG16 (Base model) might have 100 neurons.
- we need only 2 neurons.
- Change this for our need in our model (our Model).

CODE:
=====

  original Pretrained Model:
  ===========================
  
      base_model = VGG16(weights='imagenet') 
      x = Dense(100, activation='relu', name='fcl')
      #tailor pretrained LLM to our need choose only 2 output parameters
      y = Dense(2,activation='softmax', name='prediction') (x)  
      my_model=model(base_model,y) 
      my_model.summary()
      

  NOTE:
  ====

  - it has 1000 output neurons need to change to meet our need.
  - our needs is to classify Emergency or non-emergency, only we need 2 output neurons.
  - above **output layers change to 2 layers** instead of imagenet 1000 output neurons.


    
