import numpy as np

class SVM:
    def __init__(self, lr= 0.001, lambda_= 0.01, n_iters= 1000):
        self.lr= lr
        self.lambda_= lambda_
        self.n_iters= n_iters
        self.w= None
        self.b= 0

    def fit(self, X_train, y_train):
        X= X_train
        y= np.where(y_train<=0, -1, 1)
        n, n_features= X.shape

        self.w= np.zeros(n_features)
        for _ in range(self.n_iters):
            for i, x_i in enumerate(X):
                f_x= np.dot(x_i,self.w) - self.b
                if y[i]*f_x >= 1:
                    dw= 2*self.lambda_*self.w
                    db= 0
                else:
                    dw= 2*self.lambda_*self.w - y[i]*x_i
                    db= y[i]
                self.w-= self.lr*dw
                self.b-= self.lr*db


    def predict(self, X):
        linear_output= np.dot(X,self.w) - self.b
        return np.sign(linear_output)
