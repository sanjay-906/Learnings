import numpy as np

class Perceptron:
    def __init__(self, lr= 0.03, n_iters= 1000):
        self.lr= lr
        self.n_iters= n_iters
        self.activation_func= self._unit_step_function
        self.weights= None
        self.bias= 0

    def _unit_step_function(self, x):
        return np.where(x>=0, 1, 0)

    def fit(self, X, y):
        n_samples, n_features= X.shape
        self.weights= np.zeros(n_features)

        y_actual= np.array([1 if i>=0 else 0 for i in y])

        for _ in range(self.n_iters):
            for i, x_i in enumerate(X):
                linear_output= np.dot(x_i, self.weights)+ self.bias
                y_pred= self.activation_func(linear_output)

                update= self.lr*(y_actual[i] - y_pred)
                self.weights+= update*x_i
                self.bias+= update

    def predict(self, X):
        return self.activation_func(np.dot(X, self.weights) + self.bias)
