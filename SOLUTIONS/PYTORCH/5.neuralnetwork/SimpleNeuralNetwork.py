import torch
import torch.nn as nn
#create class extend nn
class SimpleNeuralNet(nn.Module):
    #no of input features
    def __init__(self,num_features):
        #invoke the super constructor
        super().__init__()
        #create layer for nn
        #mention the no of input , output
        # 5 input feature -> generate 1 output


        # (5inputs)  (3x1 weights + bias)
        #   -
        #   -         -
        #   -         -         - (y^pred)
        #   -         -
        #   -      

        #Layer 1 - since output has 3 weights
        self.linear1 = nn.Linear(num_features,3)
        self.relu = nn.ReLU()
        
        #Layer 2 - 3 input output 1
        self.linear2 = nn.Linear(3,1)
        self.sigmoid = nn.Sigmoid()



    #define forward layer
    def forward(self,features):
        #calculate output = wx+b

        #since input is features (5)
        out = self.linear1(features)
        #since output of above feed to layer1
        out = self.relu(out)
        out = self.linear2(out)
        out = self.sigmoid(out)
        return out
    
    

if __name__ == "__main__":
    #create simple dataset
    #get random 5 input
    features = torch.rand(10,5) #10 row, columns
    #create model
    model = SimpleNeuralNet(features.shape[1])
    #call forward
    model.forward(features)
    #above works but pytorch recommend standard way
    #use magic function
    model(features)
    #1.forward output

    print ("=====All Layers output=====")
    print("features=",model(features))
    print("=====Layer1 Weights & Bias =====")
    #shows the model weights(5 weights)
    print("weights = ", model.linear1.weight)
    print("weights = ", model.linear1.bias)
    print("=====Layer1=====\n\n")
    
    #show model bias
    print("=====Layer2 Weights & Bias=====")
    print("bias",model.linear2.weight)        
    print("bias = ", model.linear2.bias)
    print ("=====All Layers output=====\n\n")

    # (5inputs)  (3x1 weights + bias)
    #   -
    #   -         -
    #   -         -         - (y^pred)
    #   -         -
    #   -      

    
    # to visualize the network.
    #3. install torchinfo

    from torchinfo import summary
    summary(model,input_size=(10,5))
    
    #3.create neural network with a hidden layer.
    #hidden layer 3 neuron 

      # (5inputs)  (3hidden + 3 bias)   5*3 = 15 + 3(weights) =18 
    #   -                                        
    #   -         -                                 
    #   -         -         - (y^pred)
    #   -         -
    #   -       (3bias)       (1bias)

    #           RELU(hidden)   sigmoid(in output layer)

    #input layer = (5*3) = 5from input * 3 from hidden layer + 4 bias            
    #(5x3) = 18 weights + 4 bias
    #hidden layer = RELU
    #output layer = Sigmoid

