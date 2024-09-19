"""
Author: Natalia Zalewska
Date: 20.01.2022
Description: Gray-Scott 1D model
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
    #dla aktywatora i inhibitira
    u_left = np.roll(u, -1)
    u_right = np.roll(u, 1)
    v_left = np.roll(v, -1)
    v_right = np.roll(v, 1)
    
    Laplaceu = (u_left+u_right - 2*u)/(dx**2)
    Laplacev = (v_left+v_right - 2*v)/(dx**2)
    
    return Laplaceu, Laplacev


''' Warunek początkowy '''
u=np.ones([N])
v=np.zeros([N])
xs = np.arange(N)


for i in range(N//4, 3*N//4):
    u[i] = np.random.rand()*0.2+0.4
    v[i] = np.random.rand()*0.2+0.2
 
    
''' Algorytm Eulera'''
Du = 2*10**(-5)
Dv = 10**(-5)
F = 0.025
k=0.055
dt=1
T=10000

utab = np.zeros([len(u),T+1])
vtab = np.zeros([len(v),T+1])
utab[:,0] = u
vtab[:,0] = v


for t in np.arange(1, T):
    
    d2u, d2v = Laplace_operator(u,v)
    du = (Du*d2u - u*v**2 + F - F*u)*dt
    dv = (Dv*d2v + u*v**2 - (F+k)*v)*dt
    u = u + du
    v = v + dv

    utab[:,t] = u
    vtab[:,t] = v
    

 
#plt.plot(utab[:,5000])
#plt.plot(vtab[:,5000])


'''
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.imshow(vtab, interpolation='nearest', aspect='auto')
cax.set_clim(vmin=0, vmax=1)
cbar = fig.colorbar(cax, ticks=[0,0.3,0.5,1], orientation='vertical')
plt.show()

'''

