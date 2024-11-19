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


N/w Layer N/w                            |     CNN
-----------------------------------------|----------------------------------
 weights,Bias                            |   weights,bias,Filter( images)
 
 
