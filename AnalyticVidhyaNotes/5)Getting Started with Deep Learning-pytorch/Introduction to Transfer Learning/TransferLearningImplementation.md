
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

  Step1: Preprocess - original Pretrained Model trained from VGG16:
  =================================================================
  
      base_model = VGG16(weights='imagenet') 
      
      #functional layer activation function instead of sequential
      x = Dense(100, activation='relu', name='fcl') (base_model.layers[:4].output)
      
      #tailor pretrained LLM to our need choose only 2 output parameters
      y = Dense(2,activation='softmax', name='prediction') (x)  
      my_model=model(input = base_model,output=y) 
      my_model.summary()
      

  NOTE:
  ====

  - it has 1000 output neurons need to change to meet our need.
  - our needs is to classify Emergency or non-emergency, only we need 2 output neurons.
  - above **output layers change to 2 layers** instead of imagenet 1000 output neurons.

   Step2: Freeze 15 layers:
   =========================

       for layers in my_model.layers[ :15]
          layer.trainable = false
       my_model.fit(x_train,y_train,epoch=10, validation_data=(x_valid,y_valid))
       

  NOTE:
  =====
  
   - Now model takes half the second to train then earlier. since we  use **freeze trainable =false**  above.
    
