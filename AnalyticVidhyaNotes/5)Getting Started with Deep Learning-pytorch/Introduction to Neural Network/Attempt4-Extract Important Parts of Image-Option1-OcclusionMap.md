Attemp4 - Options to Extract important portion of image:
==========================================================

1) we hide particular section of image and check whether model able to classify image or how
   confident in detecting correct class of image, without that portion of image.
   this is called occlusion Map.


Occlusion Map:
==============

  - Remove upper left corner of image for e.g and check whether model is able to predict the image or classify
    whether image is emergency vehicle or not. we can check how confident the model in predicting or
    classifying the image class.
  - if we hide police logo for e.g , its confident is reduced to 20% which shows it is important portion of image
    to identity that is emergency police vehicle.



CODE-Locate Important part of image:
====================================

here we block part of image and check confidence score.


          def iter_occlusion ( image, size=4):
      
              occlusion = np.full( (size*3 , size*5,1 ),[0.5], np.float32)
              occlusion_center = np.full((size, size,1 [0.5], np.float32)
              occlusion_padding = size*2
              image_padded = np.pad(image,(1,occlusion_padding,occlusion_padding),
                                          (occlusion_padding,occusion_padding),(0,0) ,1,'constant',constant_values=0.0)
              for y in range(occlusion_padding, image.shape[0]+occlusion_padding.size):
                for x in range(occlusion_padding, image.shape[1]+occusion_padding.size):
                  tmp = image_padded.copy()
                  tempy = -occlusion_padding.y + occusion_center.shape[0]+occusion_padding.x-occlusion_padding.x+occluson_center.shape[1]
                                        + occlusion_padding = occlusion
                                        
      
      
          # take example image.
          image = x_train[eg_image_idx]
          correct_class = np.argmax(y_train[eg_image_idx])
          # define variable to use.
          img_size = image.shape[0]
          occlusion_size =8
          heatmap = np.zero((img-size, img-size),np.foat32)
          class_pixels = np.zeroes((img_size,img_size),np.int16)
          from collections import defaultl dict
          counters = defaultdict(int)
      
      
          #print heat map by blocking image
          for n,(x,y,img-float) in enumerate(iter_occlusion, image-size=occluson-size):
              x =  img_float.reshape(1,224,224,3)
              out = model.predict(x)
              heatmap[y:y+ occlusion-size, x:x+occlusion_size] = out[0][correct-class]
              class_pixels[y:y+occlusion-size, x:y+occlusion-size] = np.argsmax(out)
              counter[npargmax[out]]+=1
         plt.imgshow(image)
         plt.show()
      
         # print heat map  alpha means (other than R,G,B) distorted image color
         # it helps to identify where model is focussing in.
         plt.pcolormesh(heatmpa, cmap = plt.cm.jet, alpha=0.50)  
         plt.colorbar().solids.set(alpha=1)
      
         
         
      
         
