"""
Author: Natalia Zalewska
Date: 15.12.2021
Description: Ising Model - dynamic domain formation
"""

import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt
from scipy.sparse import spdiags,linalg,eye

nt      = 5        #  number of temperature points
N       = 5         #  size of the lattice, N x N
eqSteps = 1000      #  number of MC sweeps for equilibration
mcSteps = 5000       #  number of MC sweeps for calculation
J=1


T       = np.linspace(1, 5, nt); 
E,M,C,X = np.zeros(nt), np.zeros(nt), np.zeros(nt), np.zeros(nt)
n1, n2  = 1.0/(mcSteps*N*N), 1.0/(mcSteps*mcSteps*N*N) 
state = 2*np.random.randint(2, size=(N,N))-1

Ts = [1., 2., 3., 4., 5.]
Mags = [0.998, 0.912, 0.512, 0.334, 0.275]

def MCS(config, beta):
   
    for i in range(N):
        for j in range(N):
                a = np.random.randint(0, N)
                b = np.random.randint(0, N)
                s =  config[a, b]
                nb = config[(a+1)%N,b] + config[a,(b+1)%N] + config[(a-1)%N,b] + config[a,(b-1)%N]
                delta = 2*J*nb
                dE = 2*J*s*nb
                r = np.random.rand()
                
                if dE<=0 :
                    s *= 1
                elif r < np.exp(-beta*delta):
                    s *= -1
                config[a, b] = s
    return config

def calcEnergy(config):
    energy = 0 
    
    for i in range(len(config)):
        for j in range(len(config)):
            S = config[i,j]
            nb = config[(i+1)%N, j] + config[i,(j+1)%N] + config[(i-1)%N, j] + config[i,(j-1)%N]
            energy += -nb*S
    return energy/2.

def calcMag(config):
    mag = np.sum(config)
    return mag

for tt in range(nt):
    config = state        # initialise
    E1 = M1 = E2 = M2 = 0
    iT=1.0/T[tt]; iT2=iT*iT;
    
    for i in range(eqSteps):         # equilibrate
        MCS(config, iT)           # Monte Carlo moves

    for i in range(mcSteps):
        MCS(config, iT)           
        Ene = calcEnergy(config)     # calculate the energy
        Mag = calcMag(config)        # calculate the magnetisation

        E1 = E1 + Ene
        M1 = M1 + abs(Mag)
        M2 = M2 + Mag*Mag 
        E2 = E2 + Ene*Ene


    # divide by number of sites and iteractions to obtain intensive values    
    E[tt] = n1*E1
    M[tt] = n1*M1
    C[tt] = (n1*E2 - n2*E1*E1)*iT2
    X[tt] = (n1*M2 - n2*M1*M1)*iT
 
print(T, M)    
plt.scatter(T, M, s=50, marker='o', color='RoyalBlue')
plt.scatter(Ts, Mags, s=50, marker='o', color='red')
plt.xlabel("Temperature (T)", fontsize=20); 
plt.ylabel("Magnetization ", fontsize=20);   plt.axis('tight');
    