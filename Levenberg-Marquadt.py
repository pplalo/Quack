## In this file, it is presented the Levenberg-Marquadt algorithm

import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from Gradient_descendent_method import f, grad_f

# Set lambda value 
l = 1000

# Hessian matrix
Hessian_f = np.zeros(9,9)

print(Hessian_f)
