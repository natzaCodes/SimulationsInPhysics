"""
Author: Natalia Zalewska
Date: 24.11.2021
Description: Percolation - probability
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import deque
p = 0.5
L = 50
lista = np.zeros((2,19))
length =  np.zeros((2,19))
for g in range(1,20):
    p +=0.01
    licznik = 0
    sr_dlugosc = 0
    for h in range (0,100):
        def neighbours(k):
            v = [(k[0] ,k[1] + 1),(k[0] ,k[1] - 1),(k[0] - 1,k[1]),(k[0] + 1,k[1])]
            return v
        lattice = np.ones( (L+2,L+2) ) * (-1)
        tossing = np.random.random( (L+2,L+2) ) < p
        lattice[0,:] = -2
        lattice[:,0] = -2
        lattice[:,L+1] = -2
        lattice[L+1,:] = -2
        i = (L//2, L//2) 
        lattice[i] = 1 
        cluster = deque() 
        cluster.append(i)  
        a = 0
        while not( len(cluster) ==0):
            a= a + 1
            i = cluster.popleft()
            for j in neighbours(i):
                if(lattice[j] ==-1):
                    if (tossing[j]):
                        cluster.append(j)
                        lattice[j] = 1
                    else:
                        lattice[j] = 0
                elif(lattice[j] == -2):
                    lattice[j] = 2

        
        if (np.sum(lattice == 2) > 0):
            licznik+=1
        if (np.sum(lattice == 2) == 0):
            dlugosc = np.sum(lattice ==1)
        sr_dlugosc = sr_dlugosc + dlugosc
    czestosc = licznik/100
    lista[0][g-1] = p
    lista[1][g-1] = czestosc*100
    length[0][g-1] = p
    length[1][g-1] = sr_dlugosc/100
plt.scatter(lista[0,:],lista[1,:])
plt.title("Prawdopodobieństwo, L = 50")
plt.show()
plt.scatter(length[0,:],length[1,:])
plt.title("Długosc, L = 50")
plt.show()
        
