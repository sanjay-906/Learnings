import numpy as np
from collections import Counter

class KNN:
    def __init__(self, k=3):
        self.k= k

    def fit(self, X, y):
        self.X_train= X
        self.y_train= y

    def predict(self, X):
        predictions= [self._predict(x) for x in X]

        return np.array(predictions)

    def _predict(self, sample):
        def euclidean_distance(x1, x2):
            return np.sqrt(np.sum((x1-x2)**2))

        distances= [euclidean_distance(sample, x) for x in self.X_train]
        k_samples= np.argsort(distances)[0:self.k]
        k_labels= self.y_train[k_samples]
        answer_label= Counter(k_labels).most_common(1)

        return answer_label[0][0]

