import torch 
import torch.nn as nn
import pandas as pd


import numpy as np
import pandas as pd
import torch
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv('https://raw.githubusercontent.com/gscdit/Breast-Cancer-Detection/refs/heads/master/data.csv')
df.head()
df.shape
df.drop(columns=['id', 'Unnamed: 32'], inplace= True)
X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, 1:], df.iloc[:, 0], test_size=0.2)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


#label encoding
encoder = LabelEncoder()
y_train = encoder.fit_transform(y_train)
y_test = encoder.transform(y_test)

#pytorch tensor from numpy
X_train_tensor = torch.from_numpy(X_train.astype(np.float32))
X_test_tensor = torch.from_numpy(X_test.astype(np.float32))
y_train_tensor = torch.from_numpy(y_train.astype(np.float32))
y_test_tensor = torch.from_numpy(y_test.astype(np.float32))


class CancerModel(nn.Module):

    def __init__(self,num_features):
        super().__init__()
        self.linear = nn.Linear(num_features,1)
        self.sigmoid = nn.Sigmoid()
    
    def forward(self,features):
        out = self.linear(features)
        out = self.sigmoid(out)
        return out
    
    def loss_function(self,y_pred,y):
        eplison = 1e-7
        y_pred = torch.clamp(y_pred,eplison,1-eplison)
        loss=-(y_train_tensor* torch.log(y_pred)+(1-y_train_tensor)* torch.log(1-y_pred)).mean()
        return loss

if __name__ == "__main__":
    learning_rate=0.1
    epoch=25

    #create model
    model = CancerModel(X_train_tensor.shape[1])

    #define loop
    for epoch in range(epoch):

        #y_pred = model.forward(X_train_tensor)
        #no need to do model.forward 
        y_pred = model(X_train_tensor)
        #loss
        loss = model.loss_function(y_pred,y_train_tensor)

        #backward pass
        loss.backward()
        #parameter upgrade
        with torch.no_grad():
            #update the weight
            model.linear.weight-=learning_rate* model.linear.weight.grad
            model.linear.bias-= learning_rate*model.linear.bias.grad

        #zero gradients
        model.linear.weight.grad.zero_()
        model.linear.bias.grad.zero_()

        print(f'Epoch:{epoch+1}, loss: {loss.item()}')

