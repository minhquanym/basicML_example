import numpy as np
import math
import matplotlib.pyplot as plt

def grad(x) :
    return 2*x - 3*np.sin(x) + 9
def cost(x) :
    return x**2 + 3*np.cos(x) + 9*x + 5

def myGD1(eta, x0) :
    x = [x0]
    for step in range(100) :
        x_new = x[-1] - eta*grad(x[-1])
        if abs(grad(x_new)) < 1e-3:
            break
        x.append(x_new)
    return (x, step)

print(grad(-5))

(x1, st1) = myGD1(0.1, -5)
(x2, st2) = myGD1(0.1, 5)

print('Solution with learning rate = ', 0.1, ' is: ', x1, ' number of step: ', st1)
print('Solution with learning rate = ', 0.3, ' is: ', x2, ' number of step: ', st2)
