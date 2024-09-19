"""
Author: Natalia Zalewska
Date: 24.01.2022
Description: Chaos, Poincare section of the driven Duffing equation
"""

import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import numpy as np
from scipy import linspace

 
omega = 1
f = 0.33
    
def duffing(t, xv):
    x, v = xv
    a, c, b = 1, 0.2, 1. # parameters 
    #graniczna 0.285 // pojedynczy okres 0.12 // podwojny okres 24
    return [v, b*x - a*x**3 - c*v + f*np.cos(omega*t)]
             
T = 2*np.pi/omega
 
a, b = 0, 20000
d = 40000
t = linspace(a, b, d)
sol1 = solve_ivp(duffing, [a, b], [0.69, 0.32], t_eval=t)
#war pocz  [0.69, 0.32]


x0 = sol1.y[:, d-1]
t2 = linspace(1, b, d)
sol1 = solve_ivp(duffing, [1, b], x0, t_eval=t2)

siztmp = np.shape(sol1.y)
siz = siztmp[1]

 
y1= sol1.y[0]
y2 = sol1.y[1]


for i in range(0,3):
 
    faza = np.pi*i/3 #dla pi/3, 2pi/3 i pi
    N = 5000
    
    x1 = np.zeros((2*N,))
    v1 = np.zeros((2*N,))
    krok = -1
    
    # t-f % T - 0.5 T
    testwt = np.mod(t2-faza,T)-0.5*T;
    last = testwt[0]
    
    for j in range(2,siz):
        
        if (last < 0)and(testwt[j] > 0):
            krok = krok+1
            del1 = -testwt[j-1]/(testwt[j] - testwt[j-1])
            v1[krok] = (y2[j]-y2[j-1])*del1 + y2[j-1]
            x1[krok] = (y1[j]-y1[j-1])*del1 + y1[j-1]
            last = testwt[j]
        else:
            last = testwt[j]
  

        plt.figure(3)
        plt.xlabel("$x$")
        plt.ylabel("$v$")
        plt.title('f=%f' %f)
    if i == 0:
 #       lines = plt.plot(x1,v1,'bo',ms=1)
        lines = plt.scatter(x1, v1, s=10, c='b', lw=0, marker='o')
    elif i == 1:
        lines = plt.scatter(x1, v1, s=10, c='b', lw=0, marker='o')
    else:
        lines = plt.scatter(x1, v1, s=10, c='b', lw=0, marker='o')


    plt.show()
 
#plt.savefig('Duffing')