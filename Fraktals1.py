"""
Author: Natalia Zalewska
Date: 24.01.2022
Description: Self similar figures -  Bransley Fern
"""

import matplotlib.pyplot as plt
import numpy as np

d = 10000

xtab = np.empty([d])
ytab = np.empty([d])

x=0
y=0

for i in range(d):
    n=1/d
     
    C = np.random.randint(1,100)
    
    if C <=2:
        
        x, y = 0.001*x, 0.16*y 
       
        
    elif C <=11:
        
        x, y = -0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44
     
        
    elif C <=21:
      
        x, y = 0.2*x - 0.26*y, 0.26*x + 0.24*y + 0.44
        
        
    else:
        x, y = 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6 
      
        
    xtab[i] = x
    ytab[i] = y
    

plt.scatter(xtab, ytab, s=10, c='green', lw=0, marker='o')
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title('Paproć Bransleya')
plt.savefig("paprotka.png")