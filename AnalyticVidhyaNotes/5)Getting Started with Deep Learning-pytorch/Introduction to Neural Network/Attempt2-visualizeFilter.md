Attempt 2 - visualize filter
============================

1) In CNN **filters** are parameters since in image which part of images to look in case
 of snow leopard or desert leopard. have **filter for Animal** to identity animal ,
 to identify whether it is snow or desert have **filter for background**
3) In case of multilayer perceptron , weights & bias are parameters
4) visualize **print the hidden layer** - to identify the intensity of weights.
5) when print **hidden layers visually** it is in vector of weights. when plot
 using filter of convolution layer. it shows itensity of each.
6) filter shows **specific parts of image to pass or reject remaining** portions.
7) when attempt to visualize hidden layers it is just vector of weights

why visualize the parameters:
=============================

- because it gives intutition of howo one neuron connect to another and how strong the connection
  in neural network.
- it try to visualize hidden layers of neural network. it will be just vector of weights.
  where in each weights can be plotted related to other weights and which will be different shade of grey.
- These weights depict the intensity of that weighted connection from one layer to another.
- This is more intensive , when **we plot a filter** of convolution layer, we can interpret like this , that
  filter shows **specific parts of filter to pass through** and where as **reject or remaining portion**
  like **template matching algorithm**.
  

Visualizing Layer:
===================


  #weights of first filter.
  temp = model.get('conv').get_weights()[0][:,:,:,0]
  temp = temp.min()
  #normalize the image like if we red,blue ,green max is 255 divide all vector by 255 gives the normalized vector.
  temp/=temp.max()


Prof Filters:
=============

To iterate each portion of image and display the image 

    fig.ax = plt.subplots(nrows=3,ncols=3,figsize=(10,10))
    filter_no = 1
    for i in range(3):
      for j in range(3):
          temp = model.get_layer('conv').get_weights()[0][:,:,:,filter_no]
          temp = temp.min()
          temp/=temp.max()
  
          ax[i][j].isshow(temp)
          ax[i][j].set_little('conv1'+'_filter'+str(filter_no))
          ax[i][j].set_xticks([])
          ax[i][j].set_yticks([])
          filter_no++

Neural Network vs Convolution Neural Network
=============================================


N/w Layer N/w                            |     CNN
-----------------------------------------|----------------------------------
 weights,Bias                            |   weights,bias,Filter( images)


NOTE:
=====

- Only visualize first layer of CNN as filter can be represented in RGB Format.
- As we go Deeper harder to visualize since **no color**. hence visualize weights on first layer.

  
  

 






