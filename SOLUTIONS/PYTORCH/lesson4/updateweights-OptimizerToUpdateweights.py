import torch
import torch.nn as nn
x = torch.tensor([1,2,3,4], dtype=torch.float32)
y = torch.tensor([2,4,6,8],dtype =torch.float32)
w = torch.tensor(0.0, dtype=torch.float32,requires_grad=True)


def forward(x):
    return w*x

def loss(y,y_pred):
    return ((y_pred-y)**2).mean()

print(f'predicted before training f(5)={forward(5):.3f}')

#training
learning_rate= 0.01
n_iter =10
loss = nn.MSELoss()
optimizer = torch.optim.SGD([w],lr=learning_rate)
for epoch in range(n_iter):
    y_pred = forward(x)
    l= loss(y,y_pred)
    l.backward()

    #optimizer to update weights
    optimizer.step()

    #reset the grad for every iteration
    optimizer.zero_grad()

    if epoch%10==0:
        print(f'epoch {epoch +1}:w ={w:.3f},loss={l:.8f}')

print(f'prediction after training f(5):={forward(5):.3f}')

