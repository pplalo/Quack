## This file presents Newton-Raphson method

import numpy as np

# Initialization of parameters
u1 = 0.1
u2 = 0.15
var1 = 0.04
var2 = 0.0625
cov12 = 0.025

# Define the function
def U(x,y,u1,u2,var1,var2,cov12):
    return u1*x + u2*y -(var1*x**2+var2*y**2+2*cov12*x*y)/2

# Define the gradient
def grad_f(x,y,u1,u2,var1,var2,cov12):
    gdf = np.zeros(2)
    gdf[0] = u1 - var1*x -cov12*y
    gdf[1] = u2 - var2*y - cov12*x
    return gdf

# Define the Hessian Matrix
def Hess_f(x,y,u1,u2,var1,var2,cov12):
    Hdf = np.zeros((2,2))
    Hdf[0][0] = -var1
    Hdf[0][1] = -cov12
    Hdf[1][0] = -cov12
    Hdf[1][1] = -var2
    return Hdf

#Inverse of the Hessian Matrix
def inv_Hess_f(x,y,u1,u2,var1,var2,cov12):
    Hdf = Hess_f(x,y,u1,u2,var1,var2,cov12)
    inv_Hdf = np.linalg.inv(Hdf)
    return inv_Hdf

# Iteration to obtain the values of x and y that maximize the function U
x = 0
y = 0
for i in range(100):
    gdf = grad_f(x,y,u1,u2,var1,var2,cov12)
    inv_Hdf = inv_Hess_f(x,y,u1,u2,var1,var2,cov12)
    x = x - np.dot(inv_Hdf,gdf)[0]
    y = y - np.dot(inv_Hdf,gdf)[1]
    if np.linalg.norm(gdf) < 0.001:
        print('The maximum value of U is:',U(x,y,u1,u2,var1,var2,cov12))
        break




    
    