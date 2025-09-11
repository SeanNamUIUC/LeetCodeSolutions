'''
GPT Dataset
Solved 
Before we can train a transformer like GPT, we need to define the dataset. We take a giant body of text and we can create examples for the model to predict the next token based on different contexts. This is what “ChatGPT was trained on the entire internet” means.

Your task is to write the batch_loader() function which will generate a batch_size * context_length dataset and its labels. Use torch.randint() to pick batch_size different starting words for each sequence.

Inputs:

raw_dataset - a body of text. len(raw_dataset) > 0.
context_length - how many tokens back the model can read. context_length > 0.
batch_size - how many sequences to generate. batch_size > 0.
Return the input dataset X and the labels Y. len(X) = len(Y).
'''



import torch
from typing import List, Tuple

class Solution:
    def batch_loader(self, raw_dataset: str, context_length: int, batch_size: int) -> Tuple[List[List[str]]]:
        # You must start by generating batch_size different random indices in the appropriate range
        # using a single call to torch.randint()
        torch.manual_seed(0)
        # will return input => batch_size  * context_length and output => labels
        
        data = list(raw_dataset.split())
        print(data)
        X = []
        Y = []
        indicies = torch.randint(0, (len(data) - context_length), (batch_size,))
        for i in range(batch_size):
            batch_X = []
            batch_Y = []
            for j in range(context_length):
                batch_X.append(data[indicies[i] + j])
                batch_Y.append(data[indicies[i] + j + 1])
            X.append(batch_X)
            Y.append(batch_Y)
       
        res = (X, Y)
        print(res)
        return res


        
