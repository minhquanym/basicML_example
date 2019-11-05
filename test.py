# To support both python 2 and python 3
from __future__ import division, print_function, unicode_literals
import numpy as np 
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model

# height (cm)
X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
# weight (kg)
y = (X.T).T
# Visualize data
plt.plot(X, y, 'ro')
plt.axis([140, 190, 100, 500])
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()
