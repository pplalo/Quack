## File with the gradient descendent method for minimization of a function

import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
import math

## Function to be minimized

def f(x1, x2, x3, t):
    return 100*(x3-10*t)**2 + 100*(np.sqrt(x1**2 + x2**2) - 1)**2 + x3**2

## Learning rate
a = 0.001

## Gradient of the function
def grad_f(x1, x2, x3, t):
    grad = np.zeros(3)
    grad[0] = 200*((x1*(np.sqrt(x1**2 + x2**2) - 1))/(np.sqrt(x1**2 + x2**2)))
    grad[1] = 200*((x2*(np.sqrt(x1**2 + x2**2) - 1))/(np.sqrt(x1**2 + x2**2)))
    grad[2] = 200*(x3-10*t)
    return grad

## Iteration 
x = np.zeros((3, 100))
x[:, 0] = np.array([-1, 0, 0])

## t for positive x
def t(x1, x2):
    if x1 > 0:
        return math.atan(x2/x1)/2*math.pi
    else:
        return (math.atan(x2/x1) + math.pi)/2*math.pi


for i in range(0, 99):
    x[:, i+1] = x[:, i] - a*np.array(grad_f(x[0, i], x[1, i], x[2, i], t(x[0, i], x[1, i])))
    
i = 0
while i < 99:
    next_x = x[:, i] - a * np.array(grad_f(x[0, i], x[1, i], x[2, i], t(x[0, i], x[1, i])))
    if f(next_x[0], next_x[1], next_x[2], t(next_x[0], next_x[1])) > f(x[0, i], x[1, i], x[2, i], t(x[0, i], x[1, i])):
        break
    x[:, i + 1] = next_x
    i += 1

print(next_x)
print(f(next_x[0], next_x[1], next_x[2], t(next_x[0], next_x[1])))
print(i)

function = np.zeros(100)

for i in range(0, 100):
    function[i] = f(x[0, i], x[1, i], x[2, i], t(x[0, i], x[1, i]))
    

plt.figure()
plt.plot(np.arange(0, 100), function)
plt.xlabel('Iteration')
plt.ylabel('Function value')
plt.title('Function value vs. iteration')
plt.xticks(np.arange(0, 100, 1))
plt.yticks
plt.show()







