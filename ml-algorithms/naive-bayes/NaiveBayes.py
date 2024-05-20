import numpy as np

class NaiveBayes:
    def fit(self, X, y):
        n_samples, n_features= X.shape
        self._classes= np.unique(y)
        n_classes= len(self._classes)

        self._mean= np.zeros((n_classes, n_features), dtype= np.float64)
        self._var= np.zeros((n_classes, n_features), dtype= np.float64)
        self._priors= np.zeros(n_classes, dtype= np.float64)

        for _, c in enumerate(self._classes):
            X_c= X[c==y]
            self._mean[c,:] = X_c.mean(axis= 0)
            self._var[c,:] = X_c.var(axis= 0)
            self._priors[c]= X_c.shape[0]/float(n_samples)

    def predict(self, X):
        return [self._predict(x) for x in X]

    def _predict(self, x):
        posteriors= []
        for i, c in enumerate(self._classes):
            prior= np.log(self._priors[i])
            posterior_prob= np.sum(np.log(self._guassian_function(i,x)))
            posteriors.append(posterior_prob)
        return self._classes[np.argmax(posteriors)]

    def _guassian_function(self, class_index, x):
        mean= self._mean[class_index]
        var= self._var[class_index]
        return np.exp(-(x-mean)**2/(2*var))/(np.sqrt(2*np.pi*var))
