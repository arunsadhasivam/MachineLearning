import torch

x = torch.randn(3,requires_grad=True)
y = x+2 #computational graphs   y = x+2 (input acting value)
print(y) #tensor([-15.4645, -47.3278, -53.8672], grad_fn=<MulBackward0>)

#32 bit quantizier
v=torch.tensor([0.1,0.2,0.5], dtype=torch.float32)
y.backward(v) #act on y backward since we set gradient = True else throw error.
print(z.grad)
