import numpy as np
from mnist.loader import MNIST
import matplotlib.pyplot as plt
from sklearn import neighbors
from sklearn.metrics import accuracy_score
import time
from display_network import *

mndata = MNIST('/home/minhquanym/PycharmProjects/test/venv/MNISTdata')
mndata.load_testing() 
mndata.load_training()

X_test = mndata.test_images
X_train = mndata.train_images
y_test = np.asarray(mndata.test_labels)
y_train = np.asarray(mndata.train_labels)

start_time = time.time()
clf = neighbors.KNeighborsClassifier(n_neighbors=1, p=2)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
end_time = time.time()

print('Accuracy of 1NN from MNIST: ', (100*accuracy_score(y_pred, y_test)))
print('Running time : ', end_time-start_time)


