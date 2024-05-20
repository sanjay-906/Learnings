import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

from NaiveBayes import NaiveBayes
X, y= datasets.make_classification(n_samples= 1000, n_features= 10, n_classes= 2, random_state= 42)


X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= 0.2, random_state= 42)
model= NaiveBayes()
model.fit(X_train, y_train)

preds= model.predict(X_test)
accuracy= np.sum((y_test==preds))/len(y_test)

print(accuracy)
