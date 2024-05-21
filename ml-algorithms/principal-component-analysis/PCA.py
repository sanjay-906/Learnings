import numpy as np

class PCA:
    def __init__(self, n_components):
        self.n_componenets= n_components
        self.components= None
        self.mean= None

    def fit(self, X):
        self.mean= np.mean(X, axis= 0)
        X= X- self.mean

        cov= np.cov(X.T)

        eigenvalues, eigenvectors= np.linalg.eig(cov)
        eigenvectors= eigenvectors.T

        i= np.argsort(eigenvalues)[::-1]
        eigenvalues= eigenvalues[i]
        eigenvectors= eigenvectors[i]

        self.components= eigenvectors[:self.n_componenets]

    def transform(self, X):
        X-= self.mean
        return np.dot(X, self.components.T)
