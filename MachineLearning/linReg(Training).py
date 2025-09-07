# Linear Regression (Training)
# Solved 
# Now that you've implemented get_model_prediction() for a model, it's time to implement the training loop. At every iteration of the training loop, the previous function as well as get_derivative() should be called in order to perform gradient descent.

# Your goal is to implement the train_model() function, which has the following as input:

# X: The dataset for training the model. X.length = n and X[i].length = 3 for 0 <= i < n.
# Y: The correct answers from the dataset. Y.length = n.
# num_iterations: The number of iterations to run gradient descent for. num_iterations > 0.
# initial_weights: The initial weights for the model (
# �
# 1
# ,
# �
# 2
# ,
# �
# 3
# w 
# 1
# ​
#  ,w 
# 2
# ​
#  ,w 
# 3
# ​
#  ). initial_weights.length = 3.
# Return the final weights after training in the form of a NumPy array with dimension 3.







import numpy as np
from numpy.typing import NDArray


class Solution:
    def get_derivative(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64], N: int, X: NDArray[np.float64], desired_weight: int) -> float:
        # note that N is just len(X)
        return -2 * np.dot(ground_truth - model_prediction, X[:, desired_weight]) / N # desired weight is just an index

    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        return np.squeeze(np.matmul(X, weights))

    learning_rate = 0.01

    def train_model(
        self, 
        X: NDArray[np.float64], 
        Y: NDArray[np.float64], 
        num_iterations: int, 
        initial_weights: NDArray[np.float64]
    ) -> NDArray[np.float64]:

        # you will need to call get_derivative() for each weight
        # and update each one separately based on the learning rate!
        # return np.round(your_answer, 5)
        
        updated_weights = initial_weights
        for i in range(num_iterations):
            pred = self.get_model_prediction(X, updated_weights) # shape: (2, )
            for j in range(0, len(X[0])):
                grad = self.get_derivative(pred, Y, len(X), X, j)
                updated_weights[j] = updated_weights[j] - grad * self.learning_rate

        return np.round(updated_weights, 5)

        # for _ in range(num_iterations):
        #     model_prediction = self.get_model_prediction(X, initial_weights)

        #     d1 = self.get_derivative(model_prediction, Y, len(X), X, 0)
        #     d2 = self.get_derivative(model_prediction, Y, len(X), X, 1)
        #     d3 = self.get_derivative(model_prediction, Y, len(X), X, 2)

        #     initial_weights[0] = initial_weights[0] - d1 * self.learning_rate
        #     initial_weights[1] = initial_weights[1] - d2 * self.learning_rate
        #     initial_weights[2] = initial_weights[2] - d3 * self.learning_rate

        # return np.round(initial_weights, 5)
