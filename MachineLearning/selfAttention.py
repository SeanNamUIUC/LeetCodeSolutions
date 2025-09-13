# Self Attention
# Solved 
# We're finally ready to code up self-attention. This is the main part of Transformers like ChatGPT. Check out this video for an explanation of the concepts.

# The background video is critical to completely understanding the ML concepts involved in this problem. It is a bit lengthy, but is worth the time investment. This problem teaches you, at the lowest level, how LLMs read like humans and focus on what's important. This is definitely the hardest problem in the series.

# The class which will be used as a layer in the GPT class just like nn.Linear(). Forward() should return a (batch_size, context_length, attention_dim) tensor.

# Inputs:

# embedding_dim - the input dimensionality where embedding_dim > 0.
# attention_dim - the head size where attention_dim > 0.
# embedded - the input to forward(). embedded_shape = (batch_size, context_length, embedding_dim). This tuple format is PyTorch convention for 3-D.


import torch
import torch.nn as nn
from torchtyping import TensorType

# 0. Instantiate the linear layers in the following order: Key, Query, Value.
# 1. Biases are not used in Attention, so for all 3 nn.Linear() instances, pass in bias=False.
# 2. torch.transpose(tensor, 1, 2) returns a B x T x A tensor as a B x A x T tensor.
# 3. This function is useful:
#    https://pytorch.org/docs/stable/generated/torch.nn.functional.softmax.html
# 4. Apply the masking to the TxT scores BEFORE calling softmax() so that the future
#    tokens don't get factored in at all.
#    To do this, set the "future" indices to float('-inf') since e^(-infinity) is 0.
# 5. To implement masking, note that in PyTorch, tensor == 0 returns a same-shape tensor 
#    of booleans. Also look into utilizing torch.ones(), torch.tril(), and tensor.masked_fill(),
#    in that order.
class SingleHeadAttention(nn.Module):
    
    def __init__(self, embedding_dim: int, attention_dim: int):
        super().__init__()
        torch.manual_seed(0)
        # 0. Instantiate the linear layers in the following order: Key, Query, Value.
        # 1. Biases are not used in Attention, so for all 3 nn.Linear() instances, pass in bias=False.
        #d_model, d_k
        self.Key = nn.Linear(embedding_dim, attention_dim , bias = False)
        self.Query = nn.Linear(embedding_dim, attention_dim , bias = False)
        self.Value = nn.Linear(embedding_dim, attention_dim , bias = False)
        self.d_model = embedding_dim
        self.d_k = attention_dim
        self.softmax = nn.Softmax(dim=-1)

        # 2. torch.transpose(tensor, 1, 2) returns a B x T x A tensor as a B x A x T tensor.
        # 3. This function is useful:
        #    https://pytorch.org/docs/stable/generated/torch.nn.functional.softmax.html
        # 4. Apply the masking to the TxT scores BEFORE calling softmax() so that the future
        #    tokens don't get factored in at all.
        #    To do this, set the "future" indices to float('-inf') since e^(-infinity) is 0.


    def forward(self, embedded: TensorType[float]) -> TensorType[float]:
        # Return your answer to 4 decimal places

        #0, 1 embedded = (B , T, d_model)
        k = self.Key(embedded) #-> (B, T, d_k)
        q = self.Query(embedded) #-> (B, T, d_k)
        v = self.Value(embedded) #-> (B, T, d_k)

        #T * T score steps
        kT = torch.transpose(k, 1, 2)
        #1. (Q * KT / sqrt(d_k))
        qkT = (torch.matmul(q , kT) / ((self.d_k) ** 0.5))
        #2. apply masking To implement masking, note that in PyTorch, tensor == 0 returns a same-shape tensor 
        # of booleans. Also look into utilizing torch.ones(), torch.tril(), and tensor.masked_fill(),
        # in that order.
        TT = torch.tril(qkT) # changes 0 into upper trianle part
        print("TT is ", TT)
        mask = (TT == 0)
        print("mask is mask",mask)
        TT_masked = TT.masked_fill(mask, float('-inf'))
        print("TT_masked is ",TT_masked)

        #softmax
        softmax_applied = self.softmax(TT_masked)
        print("softmax applied is ", softmax_applied)
        
        # multiply V
        res = torch.matmul(softmax_applied, v)
        return torch.round(res, decimals=4)
