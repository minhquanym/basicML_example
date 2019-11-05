import numpy as np
from sklearn import datasets, neighbors
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

iris = datasets.load_iris()
iris_X = iris.data
iris_Y = iris.target

X_train, X_test, Y_train, Y_test = train_test_split(iris_X, iris_Y, test_size=50)

def my_weight(dist):
    return dist**2
clf = neighbors.KNeighborsClassifier(n_neighbors = 8, p = 2, weights=my_weight)
clf.fit(X_train, Y_train)
y_pred = clf.predict(X_test)

print('Predict: ', y_pred)
print('Answer :', Y_test)

print('Accuracy: ', 100*accuracy_score(Y_test, y_pred))

