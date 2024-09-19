"""
Author: Natalia Zalewska
Date: 24.01.2022
Description: Chaos, Holmes and Moon experiment simulation. Phaze space image
"""

import numpy as np
import matplotlib.pyplot as plt

from scipy import linspace
from scipy.integrate import solve_ivp

f=0.09

def duffing(t, xv):
    x, v = xv
    a, c, omega, b = 1, 0.2, 0.213*2*np.pi, 1. # parameters 
    #graniczna 0.32 // pojedynczy okres 0.2 // podwojny okres 0.31
    return [v, b*x - a*x**3 - c*v + f*np.cos(omega*t)]

a, b = 0, 1000
t = linspace(a, b, 10000)

sol1 = solve_ivp(duffing, [a, b], [0.69, 0.32], t_eval=t)

xsol = sol1.y[0][t>200]
vsol = sol1.y[1][t>200]


plt.plot(xsol, vsol)
plt.xlabel("$x$")
plt.ylabel("$v$")
plt.title('f=%f' %f)
#plt.savefig("pojedynczy_okres.png")

