import torch
#backward propagation.

#input
x = torch.tensor(1.0)

#actual output
y = torch.tensor(2.0)

#weight
w = torch.tensor(1.0,requires_grad=True)

y_hat = w * x
loss = (y_hat-y)**2
print(loss)
loss.backward()
#first gradient after forward and backward propagation.
print(w.grad)

#update weights and check the forward and backward propagation.
