"""
Author: Natalia Zalewska
Date: 24.11.2021
Description: Percolation - single claster Leath algorithm
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import deque

L= 100
lattice = np.ones( (L+2,L+2) ) * (-1)
#wielkosć klastra

#lattice[1] - zajety
#lattice[0] - niezajety
#lattice[-1] -dziewiczy

i = (L//2, L//2) # wezeł srodkowy czyli x, y początkowe
lattice[i] = 1 # na poczatku jest zajety
#print(np.shape(i))

cluster = deque() # kolejka
cluster.append(i) # dodawanie do kolejki

#i = cluster.popleft() # zdejmownie
#np.sum(lattice == 1)
p=0.59
tossing = np.random.random( (L+2,L+2) ) < p

while not (len(cluster)==0):
   
    i = cluster.popleft()   #zdejmuje z kolejki
    neighbours = ((i[0]+1, i[1]),
                  (i[0], i[1]+1),
                  (i[0]-1, i[1]),
                  (i[0], i[1]-1))  #x+1, y+1, x-1, y-1
   
    
    for j in neighbours:
        
        if(lattice[j]==-1):
            if tossing[j]:
                cluster.append(j)
                lattice[j]=1
            else:
                lattice[j]=0
            
        elif(lattice[j]==-2):
               lattice[j] =0 
            


plt.imshow(lattice, interpolation="nearest",cmap="magma")
plt.grid()
            
        

#print(lattice)