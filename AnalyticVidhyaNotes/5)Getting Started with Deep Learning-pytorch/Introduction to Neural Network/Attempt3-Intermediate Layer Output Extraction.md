

Attempt 3 - Intermediate layer : output extraction:
===================================================

we can 

   1) understand model Architecture.
   2) visualize filter/ weights
   3) Extract output of intermediate neural layers.
   4) Locate important parts of image according to model.

What means output of Intermediate Layer:
=========================================

   we get image in forward pass at the last output layer.

CODE to Extract output of intermediate Layer:
==============================================

below code to retrieve image 5

         from keras.model import model
         #  e.g image idx=5 for e.g
         eg_image_idx =5 
         image = x_train[eg_image_idx]
         image = image.reshape(c1, image.shape[0], image.shape[1], image.shape[2])
         # we can do for 'relu', 'pool','conv2' all layers
         intermediate_layer_mode = model(inputs= model.input, outputs = model.get_layer('conv1').output)
         plt.show(intermediate_layer_output,map='gray')
         


