
Options to check confidence of Image by filter:
===============================================

1.OcclusionMap
===============

- block portion of image and check confidence of image output
   
2.Sailency Map
===============

- check gradient of neural network
- gradient of nearest layers of neural network it shows **how much output category values
  change with respect to input image pixel**.
- Gradient shows sailent image portion which contribute to output.


CODE : sailency Map:
====================


      from vis.visualization import visualize_sailency
      from vis.utils import utils
      from keras import activation

      # utility to search for iayer index by name.
      layer_id = utils.find_layer_idx(model,'preds')
      # swap softmax with layers
      model.layers[layer_idx].activation = activation.linear
      model.utils.apply_modification(model)

      # do back propagation to find which output image attribute to change in  input image with 100% confident
      # one or prediction accuracy closer to 100%
      grads = visualize_sailency(model,layer_idx,filter_indices=0,seed_iinput=x-train(eg_image-idx),back_prop_modifer='guided')
      plt.show(grads,map='jet')
      
