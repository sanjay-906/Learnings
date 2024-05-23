import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

from KMeans import KMeans
k= 3
X, y = datasets.make_blobs(centers=k, n_samples=500, n_features=2, shuffle=True, random_state=42)
model= KMeans(k=k)
labels= model.predict(X)
