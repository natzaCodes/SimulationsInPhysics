"""
Author: Natalia Zalewska
Date: 24.01.2022
Description: Self similar figures -  Sierpniensky Triangle
"""

import matplotlib.pyplot as plt
import numpy as np

d = 4000

xtab = np.empty([d])
ytab = np.empty([d])

x=0
y=0

for i in range(d):
    
    C = np.random.randint(0,3)
    
    if C == 0:
        x = 0.5*x+0.25
        y = 0.5*y + np.sqrt(3.)/4
        
    elif C == 1:
        x = 0.5*x
        y = 0.5*y 
        
    else:
        x = 0.5*x+0.5
        y = 0.5*y 
        
    xtab[i] = x
    ytab[i] = y
    

plt.scatter(xtab, ytab, s=10, c='b', lw=0, marker='o')
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title('trójkat_Sierpinskiego')
plt.savefig("trojkat_s.png")