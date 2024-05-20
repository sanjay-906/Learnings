import numpy as np

class LogisticRegression:
    def __init__(self, n_iters= 1000, lr= 0.01):
        self.weights= None
        self.bias= None
        self.lr= lr
        self.n_iters= n_iters

    def fit(self, X, y):
        n_samples, n_features= X.shape
        self.weights= np.zeros(n_features)
        self.bias= 0

        for _ in range(self.n_iters):
            pred= np.dot(X, self.weights) + self.bias
            y_pred= self._sigmoid(pred)

            dw= (1/n_samples)*2*(np.dot(X.T,(y_pred- y)))
            db= (1/n_samples)*2*(np.sum(y_pred- y))

            self.weights-= self.lr*dw
            self.bias-= self.lr*db

    def predict(self, X):
        pred= np.dot(X, self.weights) + self.bias
        y_pred= self._sigmoid(pred)

        return [1 if x>0.5 else 0 for x in y_pred]


    def _sigmoid(self, x):
        return 1/(1+np.exp(-x))

