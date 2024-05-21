import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

from PCA import PCA

data= datasets.load_iris()
X= data.data
y= data.target

pca= PCA(2)
pca.fit(X)

X_projected= pca.transform(X)

