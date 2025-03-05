## This file presents Fletcher_Reeves method for optimization
import numpy as np
import matplotlib.pyplot as plt


# Initialization of parameters
u1 = 0.1
u2 = 0.15
var1 = 0.04
var2 = 0.0625
cov12 = 0.025
x0 = 0
y0 = 0

# Define the function
def U(x,y,u1,u2,var1,var2,cov12):
    return u1*x + u2*y -(var1*x**2+var2*y**2+2*cov12*x*y)/2

# Define the gradient
def grad_f(x,y,u1,u2,var1,var2,cov12):
    gdf = np.zeros(2)
    gdf[0] = u1 - var1*x -cov12*y
    gdf[1] = u2 - var2*y - cov12*x
    return gdf

#Evaluate the gradient at the initial point
d0 = grad_f(x0,y0,u1,u2,var1,var2,cov12)

#Iteration in the direction of the gradient by finding the step size that varies with the iteration
n = 100
a = np.zeros(n)
x = np.zeros(n)
y = np.zeros(n)
dk = np.zeros((2,n))
x[0] = x0
y[0] = y0
a[0] = 0.1
dk[0][0] = d0[0]
dk[0][1] = d0[1]
for i in range(n-1):
    x[i+1] = x[i] + a[i]*dk[0][i]
    y[i+1] = y[i] + a[i]*dk[1][i]
    dk[0][i+1]= grad_f(x[i+1],y[i+1],u1,u2,var1,var2,cov12)[0]+(np.linalg.norm(grad_f(x[i+1],y[i+1],u1,u2,var1,var2,cov12))**2*dk[0][i]/np.linalg.norm(grad_f(x[i],y[i],u1,u2,var1,var2,cov12))**2)
    dk[1][i+1]= grad_f(x[i+1],y[i+1],u1,u2,var1,var2,cov12)[1]+(np.linalg.norm(grad_f(x[i+1],y[i+1],u1,u2,var1,var2,cov12))**2*dk[1][i]/np.linalg.norm(grad_f(x[i],y[i],u1,u2,var1,var2,cov12))**2)
    a[i+1] = np.dot(grad_f(x[i+1],y[i+1],u1,u2,var1,var2,cov12),dk[:,i+1])/np.dot(dk[:,i+1],dk[:,i+1])
    print(U(x[i+1],y[i+1],u1,u2,var1,var2,cov12))
    if np.abs(U(x[i],y[i],u1,u2,var1,var2,cov12)-U(x[i+1],y[i+1],u1,u2,var1,var2,cov12))<0.000001:
       print('The maximum value of U is:',U(x[i+1],y[i+1],u1,u2,var1,var2,cov12), 'at x =', x[i+1], 'and y =', y[i+1])
       break