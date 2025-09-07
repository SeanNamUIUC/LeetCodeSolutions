# Linear Regression (Forward)
# Solved 
# Your task is to implement linear regression, a statistical model that ends up being the foundation of neural networks. You can learn more from the Complete Explanation of Linear Regression or by reading the description below.

# Your must implement get_model_prediction() which returns a prediction value for each dataset value, and get_error() which calculates the error for given prediction data.

# Inputs - get_model_prediction:

# X - the dataset to be used by the model to predict the output. len(X) = n, and len(X[i]) = 3 for 0 <= i < n.
# weights - the current 
# �
# 1
# w 
# 1
# ​
#  , 
# �
# 2
# w 
# 2
# ​
#  , and 
# �
# 3
# w 
# 3
# ​
#   weights for the model. len(weights) = 3.
# Inputs - get_error:

# model_prediction - the model's prediction for each training example. len(model_prediction) = n.
# ground_truth - the correct answer for each example. len(ground_truth) = n.


class Solution:
    def get_gradient(self, x: int):
        return 2 * x
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        #res
        res = init
        for i in range(iterations):
            #gradient descent -> res = res - learning_rate *  gradient
            res = res - learning_rate * self.get_gradient(res)
            print(round(res, 5)) # 5의 자리까지 반올림
        return round(res,5)