
import numpy as np
import matplotlib.pyplot as plt

X = np.array([[1, 2, 3, 4]]).T;
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis = 1)
Y = np.array([[2, 3, 4, 5]]).T;

from sklearn import linear_model
# fit the model by Linear Regression
regr_false = linear_model.LinearRegression(fit_intercept=False) # fit_intercept = False for calculating the bias
regr_true = linear_model.LinearRegression(fit_intercept=True) # fit_intercept = False for calculating the bias
regr_false.fit(Xbar, Y)
regr_true.fit(Xbar, Y)

print('Nghiem cua phuong trinh bang scikit-learn : ', regr_false.coef_)
print('Nghiem cua phuong trinh bang scikit-learn : ', regr_true.coef_)
print('Nghiem cua phuong trinh bang scikit-learn : ', regr_)
plt.plot(X.T, Y.T, 'ro')
plt.axis([0, 10, 0, 10])
plt.plot(regr_false.coef_)
plt.show()