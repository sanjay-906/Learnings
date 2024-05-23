import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

from DecisionTree import DecisionTree

data= datasets.load_breast_cancer()
X= data.data
y= data.target

X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= 0.2, random_state= 42)

model= DecisionTree(max_depth= 10)
model.fit(X_train, y_train)

y_pred= model.predict(X_test)

print(np.sum(y_test==y_pred)/len(y_test))

