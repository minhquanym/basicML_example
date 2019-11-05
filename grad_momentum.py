import numpy as np
import math
import matplotlib.pyplot as plt 


def grad(theta) :
    return 2*x - 3*np.cos(x) + 9
def has_converged(theta) :
    

def GD_momentum(theta_init, eta, gamma) :
    theta = [theta_init]
    v_old = np.zeros_like(theta_init)
    for it in range(100) :
        v_new = gamma*v_old + eta*grad(theta[-1])
        theta_new = theta[-1] - v_new
        if has_converged(theta_new) :
            break
        theta.append(theta_new)
        v_old = v_new
    return (theta, it)

