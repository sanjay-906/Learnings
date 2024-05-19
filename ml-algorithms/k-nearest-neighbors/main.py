import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

from KNN import KNN
iris= datasets.load_iris()
X,y= iris.data, iris.target

X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= 0.2, random_state= 42)

model= KNN()
model.fit(X_train, y_train)

preds= model.predict(X_test)

accuracy= np.sum(preds==y_test)/len(y_test)
print(accuracy)
