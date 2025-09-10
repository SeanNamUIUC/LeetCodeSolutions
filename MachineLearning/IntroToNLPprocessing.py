import torch
import torch.nn as nn
from torchtyping import TensorType

# torch.tensor(python_list) returns a Python list as a tensor
# class Solution:
#     def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        

positive = ["Dogecoin to the moon"]
negative = ["I will short Tesla today"]

Output = [
  [1.0, 7.0, 6.0, 4.0, 0.0],
  [2.0, 9.0, 5.0, 3.0, 8.0]
]

print(positive.extend(negative))