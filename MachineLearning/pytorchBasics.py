

# Pytorch Basics
# Solved 
# PyTorch is the industry standard library for deep learning and was used to train ChatGPT. Checkout the first 9 minutes of this video for a summary of the basic functions.

# You will use built in PyTorch functions to manipulate tensors. These are important to understand before building more interesting & powerful neural networks.

# Your tasks:

# Reshape an 
# �
# ×
# �
# M×N tensor into a 
# (
# �
# ⋅
# �
#  
# /
# /
#  
# 2
# )
# ×
# 2
# (M⋅N//2)×2 tensor.
# Find the average of every column in a tensor.
# Combine an 
# �
# ×
# �
# M×N tensor and a 
# �
# ×
# �
# M×M tensor into a 
# �
# ×
# (
# �
# +
# �
# )
# M×(M+N) tensor.
# Calculate the mean squared error loss between a prediction and target tensor.
# Inputs:

# to_reshape - a tensor to reshape
# to_avg - a tensor to average column wise
# cat_one - the first tensor to concatenate
# cat_two - the second tensor to concatenate
# prediction - the output tensor of a model
# target - the true labels for the model inputs

import torch
import torch.nn
from torchtyping import TensorType

# Helpful functions:
# https://pytorch.org/docs/stable/generated/torch.reshape.html
# https://pytorch.org/docs/stable/generated/torch.mean.html
# https://pytorch.org/docs/stable/generated/torch.cat.html
# https://pytorch.org/docs/stable/generated/torch.nn.functional.mse_loss.html

# Round your answers to 4 decimal places using torch.round(input_tensor, decimals = 4)
class Solution:
    def to_round(self, x):
        return torch.round(x, decimals = 4)
    def reshape(self, to_reshape: TensorType[float]) -> TensorType[float]:
        # torch.reshape() will be useful - check out the documentation
        # (M * N // 2) * 2
        return self.to_round(torch.reshape(to_reshape, (((len(to_reshape) * len(to_reshape[0]) // 2)), 2)))

    def average(self, to_avg: TensorType[float]) -> TensorType[float]:
        # torch.mean() will be useful - check out the documentation
        return self.to_round(torch.mean(to_avg, 0))

    def concatenate(self, cat_one: TensorType[float], cat_two: TensorType[float]) -> TensorType[float]:
        # torch.cat() will be useful - check out the documentation
        return self.to_round(torch.cat((cat_one, cat_two) , 1))# dim=1 -> column 세로방향으로 이어 붙힘

    def get_loss(self, prediction: TensorType[float], target: TensorType[float]) -> TensorType[float]:
        # torch.nn.functional.mse_loss() will be useful - check out the documentation
        res = self.to_round(torch.nn.functional.mse_loss(prediction, target))
        return res
