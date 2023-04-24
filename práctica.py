import numpy as np
x=np.array([(np.pi/2),(np.pi),(0)])
term = x
sum = x
eps = 1e-8
n = 1

for i in x:
    while np.abs(term/sum)>eps:
        term = -term*x**2/((2*n-1)*(2*n-2))
        sum = sum +term
        n += 1
        imax = n

resultado = abs(sum-np.sin(x))/np.sin(x)


print(x, imax, sum, resultado)