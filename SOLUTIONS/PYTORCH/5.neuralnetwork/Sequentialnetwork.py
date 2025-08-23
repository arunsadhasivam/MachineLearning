import torch
import torch.nn as nn
#create class extend nn for sequential container
class SequentialNeuralNet(nn.Module):
    #no of input features
    def __init__(self,num_features):
        #invoke the super constructor
        super().__init__()
        #Layer 1 - since output has 3 weights
        
        self.network = nn.Sequential(
            nn.Linear(num_features,3),
            nn.ReLU(),
            #Layer 2 - 3 input output 1
            nn.Linear(3,1),
            nn.Sigmoid()
        )

        #architecture - sequential 


    #define forward layer
    def forward(self,features):
        #automatically understand how many layer
        #forward pass which output goes to input
        #sequential automatically understand.
        out = self.network(features)
        return out
    
    

if __name__ == "__main__":
    #create simple dataset
    #get random 5 input
    features = torch.rand(10,5) #10 row, columns
    #create model
    model = SequentialNeuralNet(features.shape[1])
    #call forward
    model.forward(features)
    #above works but pytorch recommend standard way
    #use magic function
    model(features)
    #1.forward output
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

