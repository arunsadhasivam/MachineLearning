

Visualize Filter and weights:
==============================


temp = model.get_layer('conv1').get_weights()[0][:,:,:,0]
temp /= temp.min()
plt.imshow(temp)

# plot the filters

flg.ax = plt.subplots(nrows=3, cols=3, figsize=(10,10))

filter_no=1
   for i in range(3):
     for j in range(3):
        temp = model.get_layer('conv').get_weights()[0][:,:,:,filter_no]
        temp -= temp.min()
        temp /= temp.max()
        ax[i][j].inshow(temp)
        ax[i][j].set_title('conv'+'-filter'+str(filter-no))
        ax[i][j].set_xticks()
        ax[i][j].set_yticks()
        fiter_no++

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
   


