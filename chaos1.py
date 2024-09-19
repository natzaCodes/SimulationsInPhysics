
"""
Author: Natalia Zalewska
Date: 24.01.2022
Description: Way to chaos based on Duffing equations
"""


import numpy as np
import matplotlib.pyplot as plt

from scipy import linspace
from scipy.integrate import solve_ivp

f=0.12
def duffing(t, xv):
    x, v = xv
    a, c, omega, b = 1, 1/5, 0.213*(2*np.pi), 1. # parameters 
    return [v, b*x - a*x**3 - c*v + f*np.cos(omega*t)]

a, b = 0, 40
t = linspace(a, b, 4000)

sol1 = solve_ivp(duffing, [a, b], [0, 0.15], t_eval=t)


plt.subplot(311)
plt.title('f=%f' %f)
plt.plot(sol1.t, sol1.y[0])
plt.xlabel("$t$")
plt.ylabel("$x$")
plt.subplot(312)
plt.plot(sol1.t, sol1.y[1])
plt.ylabel("$v$")
plt.xlabel("$t$")
#plt.subplot(313)
#plt.plot(sol1.y[0], sol1.y[1])
#plt.ylabel("$v$")
#plt.xlabel("$x$")
#plt.savefig("lorenz_x.png")