"""
Author: Natalia Zalewska
Date: 20.01.2022
Description: Gray-Scott 2D model
"""

import numpy as np
import matplotlib.pyplot as plt


L=2
N=100
r = np.linspace(0, L, N)  #odcinek 
dx = 0.02
dt =1

''' Operator Laplace'a '''
''' d2f_dx2 = (f(x-dx) + f(x+dx) - 2f(x))/ (dx)^2  '''

def Laplace_operator(u,v) :

    dx = 0.02
    dy=0.02
    #dla aktywatora i inhibitira
    
    u_right = np.roll(u, 1,axis=0)
    u_left = np.roll(u, -1,axis=0)
    u_down = np.roll(u, 1,axis=1)
    u_up = np.roll(u,-1,axis=1)
    
    v_right = np.roll(v, 1,axis=0)
    v_left = np.roll(v, -1,axis=0)
    v_down = np.roll(v, 1,axis=1)
    v_up = np.roll(v,-1,axis=1)
    
    Laplaceu = (u_left + u_right + u_down + u_up - 4*u)/(dx**2)
    Laplacev = (v_left + v_right + v_down + v_up - 4*v)/(dx**2)
    
    return Laplaceu, Laplacev


''' Warunek początkowy '''
u=np.ones([N, N])
v=np.zeros([N, N])
xs = np.arange(N)

for i in range(N//4, 3*N//4):
    for j in range(N//4, 3*N//4):
        u[i, j] = np.random.rand()*0.2+0.4
        v[i, j] = np.random.rand()*0.2+0.2
 
    
''' Algorytm Eulera'''
Du = 2*10**(-5)
Dv = 10**(-5)
F = 0.03
k=0.062
dt=1
T=10000




for t in np.arange(1, T):
    
    d2u, d2v = Laplace_operator(u,v)
    du = (Du*d2u - u*v**2 + F - F*u)*dt
    dv = (Dv*d2v + u*v**2 - (F+k)*v)*dt
    u = u + du
    v = v + dv
    
    if (t%100==0): 
        plt.imshow(u)
        plt.show()
