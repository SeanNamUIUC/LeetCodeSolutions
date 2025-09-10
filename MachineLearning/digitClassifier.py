
# Digit Classifier
# Solved 
# Your task is to implement a neural network that can recognize black and white images of handwritten digits. This is a simple but powerful application of neural networks. To learn about coding neural networks in PyTorch, watch this 10 minute clip.

# For the model architecture, first use linear layer with 512 neurons follwed by a ReLU activation, as well as a dropout layer with probability p = 0.2 that precedes a final Linear layer with 10 neurons and a sigmoid activation. Each output neuron corresponds to a digit from 0 to 9, where each value is the probability that the input image is the corresponding digit.

# Input:

# images - one or more 
# 28
# ×
# 28
# 28×28 black and white images of handwritten digits. len(images) > 0 and len(images[i]) = 28 * 28 for 0 <= i < len(images).
# Write the artchitecture / constructor and the forward() pass that returns the model's prediction. Do not write the training loop (or gradient descent) to minimize the error.

import torch
import torch.nn as nn
from torchtyping import TensorType

class Solution(nn.Module):
    def __init__(self):
        super().__init__()
        torch.manual_seed(0)
        # Define the architecture here
        self.first_layer = nn.Linear(28 * 28, 512)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(p=0.2)
        self.final_layer = nn.Linear(512, 10)
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, images: TensorType[float]) -> TensorType[float]:
        torch.manual_seed(0)
        
        # Return the model's prediction to 4 decimal places
        first_layer_output = self.first_layer(images)
        activated_relu = self.relu(first_layer_output)
        activated_dropout = self.dropout(activated_relu)
        final_layer_output = self.final_layer(activated_dropout)
        activated_sigmoid = self.sigmoid(final_layer_output)
        return torch.round(activated_sigmoid, decimals = 4)

        


