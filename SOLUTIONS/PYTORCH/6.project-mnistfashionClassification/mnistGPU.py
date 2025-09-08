#load custom dataset mnist-custom classification.
#load only 6000 dataset out of 60,000 datasets.

# Arch 

# 784 parameters



#                 
# (784inputs)     RELU          RELU         SOFTMAX  
#   -
#   -               -               -            -
#   -               -               -            -
#   -               -               -
#   -               -
#   -
#  input layer  (128 neurons)     64 neurons   10 image output outputlayer

#Note:

#- Hidden layer size should be between the input and output layer sizes
#- Often 2/3 the size of the input layer plus the output layer size
#- Should be less than twice the input layer size to avoid overfitting
#- Powers of 2 (64, 128, 256) are computationally efficient

# Conservative approach - smaller network, less overfitting risk 
#                       - input   = 784
#                       - hidden1 = 128
#                       - hidden2 = 64
#                       - output  = 10
# Aggressive approach - more capacity for complex patterns 
#                       - input   = 784
#                       - hidden1 = 512
#                       - hidden2 = 256
#                       - hidden3 = 128
#                       - output  = 10

# hidden layer calculation - ((inpht_size + ouput_size)* 2.0/3.0)

# E.g calculation
#   int inputSize = 784;
# int outputSize = 10
#  784+10 = (884*2)/3 = 1768/3 = 588
#Dimensionality Reduction: Moving from 784 → 128 → 64 forces the network to learn compressed representations, which can help with:

#####################################################################
# Key Considerations

# Dimensionality Reduction: 
# ==========================
#     Moving from 784 → 128 → 64 forces the network to learn compressed representations, which can help with:

# 1.Feature extraction
# 2.Noise reduction
# 3.Generalization

# Computational Efficiency: Smaller hidden layers mean:
# =====================================================
# 1.Fewer parameters to train
# 2.Faster forward/backward passes
# 3. Less memory usage

# Overfitting Prevention:
# ========================
#     Too many neurons can memorize training data rather than learn generalizable patterns.
# The 784 → 128 → 64 progression is particularly popular for MNIST digit classification because it provides enough capacity to learn the patterns while maintaining efficiency. The exact numbers often come from empirical testing - you might try several architectures and see which performs best on your validation set.


#step 1 - load mnist data
import pandas as pd
from sklearn.model_selection import train_test_split
import torch
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

# Set random seeds for reproducibility
torch.manual_seed(42)


# Check for GPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using device: {device}")


# Create a 4x4 grid of images
fig, axes = plt.subplots(4, 4, figsize=(10, 10))
fig.suptitle("First 16 Images", fontsize=16)
df = pd.read_csv('../data/fmnist_small.csv')

# Create a 4x4 grid of images
fig, axes = plt.subplots(4, 4, figsize=(10, 10))
fig.suptitle("First 16 Images", fontsize=16)

# Plot the first 16 images from the dataset
for i, ax in enumerate(axes.flat):
    img = df.iloc[i, 1:].values.reshape(28, 28)  # Reshape to 28x28
    ax.imshow(img)  # Display in grayscale
    ax.axis('off')  # Remove axis for a cleaner look
    ax.set_title(f"Label: {df.iloc[i, 0]}")  # Show the label

plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout to fit the title
plt.show()

# train test split

X = df.iloc[:, 1:].values
y = df.iloc[:, 0].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# scaling the feautures
X_train = X_train/255.0
X_test = X_test/255.0


class CustomDataset(Dataset):
    def __init__(self, features, labels):
        self.features = torch.tensor(features, dtype=torch.float32)
        self.labels = torch.tensor(labels, dtype=torch.long)

    def __len__(self):
        return len(self.features)

    def __getitem__(self, index):
        return self.features[index], self.labels[index]


#train dataset
train_dataset = CustomDataset(X_train, y_train)
# create test_dataset object
test_dataset = CustomDataset(X_test, y_test)


#create train and test dataloader
train_loader = DataLoader(train_dataset,batch_size=32,shuffle=True)
test_loader = DataLoader(test_dataset,batch_size=32,shuffle=True)


#define neural arch
#                 
# (784inputs)     RELU          RELU         SOFTMAX  
#   -
#   -               -               -            -
#   -               -               -            -
#   -               -               -
#   -               -
#   -
#  input layer  (128 neurons)     64 neurons   10 image output outputlayer

class MyNeuralArch(nn.Module):
    def __init__(self,features):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(features,128),
            nn.ReLU(),
            nn.Linear(128,64),
            nn.ReLU(),
            nn.Linear(64,10)
        )
    def forward(self,x):
        return self.model(x)


#set learning rate and epoch
epochs = 100
learning_rate = 0.1
#instantiate model
model = MyNeuralArch(X_train.shape[1])

#loss function
loss_fn = nn.CrossEntropyLoss()
#optimizer
optimizer = optim.SGD(model.parameters(), lr=learning_rate)

len(train_loader)
#training loop

for epoch in range(epochs):

  total_epoch_loss = 0

  for batch_features, batch_labels in train_loader:

    # move data to gpu
    batch_features, batch_labels = batch_features.to(device), batch_labels.to(device)

    # forward pass
    outputs = model(batch_features)

    # calculate loss
    loss = loss_fn(outputs, batch_labels)

    # back pass
    optimizer.zero_grad()
    loss.backward()

    # update grads
    optimizer.step()

    total_epoch_loss = total_epoch_loss + loss.item()

  avg_loss = total_epoch_loss/len(train_loader)
  print(f'Epoch: {epoch + 1} , Loss: {avg_loss}')

#now evaluate model - because train test, evaluation it behaves different
#now ask to change behaviour to evaluation mode

model.eval()
# evaluation code
total = 0
correct = 0

with torch.no_grad():

  for batch_features, batch_labels in test_loader:

    outputs = model(batch_features)

    _, predicted = torch.max(outputs, 1)

    total = total + batch_labels.shape[0]

    correct = correct + (predicted == batch_labels).sum().item()

print(correct/total)
len(test_loader)
