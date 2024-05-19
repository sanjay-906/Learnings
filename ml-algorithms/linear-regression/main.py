import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

from LinearRegression import LinearRegression
X, y= datasets.make_regression(n_samples= 100, n_features= 1, noise= 20, random_state= 42)

X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= 0.2, random_state= 42)
model= LinearRegression()
model.fit(X_train, y_train)

preds= model.predict(X_test)
accuracy= np.mean((y_test-preds)**2)

print(accuracy)
