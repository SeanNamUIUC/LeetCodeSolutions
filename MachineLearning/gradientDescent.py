
# Gradient Descent
# Solved 
# Your task is to minimize the function via Gradient Descent: 
# �
# (
# �
# )
# =
# �
# 2
# f(x)=x 
# 2
#  .

# Gradient Descent is an optimization technique widely used in machine learning for training models. It is crucial for minimizing the cost or loss function and finding the optimal parameters of a model.

# For the above function the minimizer is clearly x = 0, but you must implement an iterative approximation algorithm, through gradient descent.

# Input:

# iterations - the number of iterations to perform gradient descent. iterations >= 0.
# learning_rate - the learning rate for gradient descent. 1 > learning_rate > 0.
# init - the initial guess for the minimizer. init != 0.
# Given the number of iterations to perform gradient descent, the learning rate, and an initial guess, return the value of x that globally minimizes this function.

# Round your final result to 5 decimal places using Python's round() function.


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