## In this file, it is presented the Levenberg-Marquadt algorithm

import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from Gradient_descendent_method import f, grad_f

# Set lambda value 
l = 1000

# Hessian matrix
def Hessian_f(x1, x2, x3):
    Hessian_f = np.zeros((3, 3))

    # Elements of the Hessian matrix
    Hessian_f[0, 0] = 200*(np.sqrt(x1**2 + x2**2) - 1)/(np.sqrt(x1**2 + x2**2)) + 200*(x1**2/(x1**2 + x2**2)) - 200*(x1**2*(np.sqrt(x1**2 + x2**2) - 1))/(x1**2 + x2**2)**(3/2)
    Hessian_f[0, 1] = -200*(x2*(np.sqrt(x1**2 + x2**2) - 1))/(x1**2 + x2**2)**(3/2) + 600*x2*x1**2*(np.sqrt(x1**2 + x2**2) - 1)/(x1**2 + x2**2)**(5/2) + 200*x2/(x1**2 + x2**2) - 600*x2*x1**2/(x1**2 + x2**2)**2
    Hessian_f[0, 2] = 0
    Hessian_f[1, 0] = -200*(x1*(np.sqrt(x1**2 + x2**2) - 1))/(x1**2 + x2**2)**(3/2) + 600*x1*x2**2*(np.sqrt(x1**2 + x2**2) - 1)/(x1**2 + x2**2)**(5/2) + 200*x1/(x1**2 + x2**2) - 600*x1*x2**2/(x1**2 + x2**2)**2
    Hessian_f[1, 1] = 200*(np.sqrt(x1**2 + x2**2) - 1)/(np.sqrt(x1**2 + x2**2)) + 200*(x2**2/(x1**2 + x2**2)) - 200*(x2**2*(np.sqrt(x1**2 + x2**2) - 1))/(x1**2 + x2**2)**(3/2)
    Hessian_f[1, 2] = 0
    Hessian_f[2, 0] = 0
    Hessian_f[2, 1] = 0
    Hessian_f[2, 2] = 200
    return Hessian_f
