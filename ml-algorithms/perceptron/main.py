import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

from Perceptron import Perceptron
X, y= datasets.make_blobs(n_samples= 200, n_features= 10, centers= 2, cluster_std= 2, random_state= 42)


X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= 0.2, random_state= 42)
model= Perceptron()
model.fit(X_train, y_train)

preds= model.predict(X_test)
accuracy= np.sum((y_test==preds))/len(y_test)

print(accuracy)
