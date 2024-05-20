import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

from LogisticRegression import LogisticRegression
data= datasets.load_breast_cancer()
X, y= data.data, data.target


X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= 0.2, random_state= 42)
model= LogisticRegression()
model.fit(X_train, y_train)

preds= model.predict(X_test)
accuracy= np.sum((y_test==preds))/len(y_test)

print(accuracy)
