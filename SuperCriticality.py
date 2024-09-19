"""
Author: Natalia Zalewska
Date: 12.01.2022
Description: Sand scattering principle - with critical starting point
"""

import numpy as np
import matplotlib.pyplot as plt


#stworzenie siatki  31x31 plus pustych brzegów; stałe
L = 100  #31
grid = np.full((L+2, L+2), 7, int)  #siatka z wolnymi brzegami
grid[0,:] = 0
grid[:,0] = 0
grid[-1,:] = 0
grid[:,-1] = 0
grid_zad2 = np.zeros((L+2, L+2), int) #siatka do zad 2
height_crit = 3   #krytyczna iloć ziaren w węźle
za_duzo = height_crit + 1
t = 1000   #krok czasowy


#jeden krok czasowy to dodanie ziarenka, osyp i czyszczenie brzegów;
#krok czasowy dotyczy tylko sytuacji gdy jest osyp

''' 1 - dodawanie ziarenka do losowego miejsca w węźle''' 
def dodanie_ziarna(grid) : 
    
    while np.max(grid) < za_duzo:
        #losuje współrzędne węzła, gdzie będzie dodane ziarno
        a = np.random.randint(1, L+1)
        b = np.random.randint(1, L+1)
        #dodaje ziarno do tego węzła
        grid[a,b] += 1
    
    return grid
    

''' 2 - osypywanie i czyszczenie brzegów''' 
def osypywanie(grid, grid_zad2) :
    while np.max(grid) > height_crit :
        
        ix, iy = np.where( grid > height_crit )
        
        grid[ix,iy] -= 4
        grid[ix+1,iy] += 1
        grid[ix-1,iy] += 1
        grid[ix,iy+1] += 1
        grid[ix,iy-1] += 1
        
        grid_zad2[ix,iy] =1  
        
        grid[0,:] = 0
        grid[:,0] = 0
        grid[-1,:] = 0
        grid[:,-1] = 0
        
        plt.imshow(grid)
        plt.show()
       
    return grid, grid_zad2
      
          

t_tab = np.empty(t)
liczba_ziaren = np.empty(t)
liczba_ziaren2 = np.empty(t)


''' Main code '''

for i in range(t):
    #grid = np.zeros((L+2, L+2), int)
    grid_zad2 = np.zeros((L+2, L+2), int)
    
    grid_k = dodanie_ziarna(grid)   
    osypywanie(grid_k, grid_zad2)
   # czyszczenie_brzegow(grid_k)

    
    liczba_ziaren[i] = np.sum(grid_k)
    liczba_ziaren2[i] = np.sum(grid_zad2)
    t_tab[i] = i+1  
   
'''    
    if (i%100==0): 

        plt.imshow(grid_k)
        plt.show()
'''    
    #plt.imsave("C:/Users/missn/OneDrive/Pulpit/jakieś ważne rzeczy/UW/3 sem/SKwF/Krytycznosc/img{:06d}.png".format(t), image) 
   
  
 
   
    
   
    