

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
              
