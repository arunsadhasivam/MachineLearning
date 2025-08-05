#prediction.
#gradient computation.
#loss function - to know how much predicted accurate 
# MSE - for regression.
# Binary cross entrophy - classification.
#paramater updates - for backward propagation.
#optimizer - to improve the prediction to allow to fine tune 
#            learning parameter which improves the prediction.

import torch

#just change to torch.tensor and quantization.
x = torch.tensor([1,2,3,4],dtype=torch.float32)
y = torch.tensor([2,4,6,8],dtype=torch.float32)

# need to set the requires_grad flag
w = torch.tensor(0.0, dtype=torch.float32 , requires_grad=True)


#forward and loss is same.

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
iter=100

for epoch in range(iter):
    #forward pass prediction.
    y_pred = forward(x) # same
    #calculate loss 
    l = loss(y,y_pred) #same

    #calculate gradient - objective to get closest zero or local minimum and global minimum
    #parameter for which curve take to zero 
    #rate of change i.e check how far move
    #from initial to convergence or local minium
    #dw = gradient(x,y,y_pred)
    l.backward() # it calculate the gradient instead of above, pytorch will do that

    #weight gets updated and can get in w.grad after calling l.backward

    #update the weights.
    with torch.no_grad():
        w-=learning_rate*w.grad

    #l.backward() accumulate the value in w.grad
    #so need to reset.
    w.grad.zero_()
    if epoch % 10 ==0 :
        print (f'epoch {epoch+1}: w = {w: .3f},loss = {l: .3f}')

print(f'Prediction After training forward f(5): {forward(5): .3f}')
     

