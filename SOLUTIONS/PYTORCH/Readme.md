https://www.youtube.com/watch?v=3Kb0QS6z7WA&list=PLqnslRFeH2UrcDBWF5mfPGpqQDSta6VK4&index=4


Magic function:
================

https://github.com/arunsadhasivam/MachineLearning/blob/main/SOLUTIONS/PYTORCH/Magicfunction/magicfunction.py

model.forward() or model()

- as you can see model.forward or inside model you have __call__ method which internally call this.forward()

      def __call__(self):  # Makes object callable like a function
        return f"Hello, I'm {self.name}!"


      import torch.nn as nn
      class MyModel(nn.Module):
          def forward(self, x):
              return x * 2
      
      model = MyModel()
      # These are equivalent:
      result1 = model(input_tensor)      # Uses __call__ magic
      result2 = model.forward(input_tensor)  # Direct call

