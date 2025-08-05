#prediction.
#gradient computation.
#loss function - to know how much predicted accurate 
# MSE - for regression.
# Binary cross entrophy - classification.
#paramater updates - for backward propagation.
#optimizer - to improve the prediction to allow to fine tune 
#            learning parameter which improves the prediction.

import numpy as np

x = np.array([1,2,3,4],dtype=np.float32)
y = np.array([2,4,6,8],dtype=np.float32)

w = 0.0

# apply weight to each input to move forward
# for each input parameter we apply the weight based on 
# weightable the output is predicted
def forward(x):
    return w*x

#calculate loss based on actual to predicted values.
#Mean square root Error(MSE)
# 1/N*(w*x - y)**2

def loss(y,y_predict):
    return ((y_predict-y)**2).mean()

#to allow the input to converge to zero.
#dj/dw = 1/n 2x(w*x - y)
def gradient(x,y,y_predict):
    return np.dot(2*x,y_predict-y).mean()

#how much we increase gradient step 
learning_rate = 0.01
iter=10
print(f'Prediction Bfore training forward f(5): {forward(5): .3f}')

for epoch in range(iter):
    #forward pass prediction.
    y_pred = forward(x)
    #calculate loss 
    l = loss(y,y_pred)

    #calculate gradient - objective to get closest zero or local minimum and global minimum
    #parameter for which curve take to zero 
    #rate of change i.e check how far move
    #from initial to convergence or local minium
    dw = gradient(x,y,y_pred)

    #update the weights.
    w-=learning_rate*dw
    if epoch % 2 ==0 :
        print (f'epoch {epoch+1}: w = {w: .3f},loss = {l: .3f}')

print(f'Prediction After training forward f(5): {forward(5): .3f}')
     

