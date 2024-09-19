"""
Author: Natalia Zalewska
Date: 12.01.2022
Description: Sand scattering principle
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


#stworzenie siatki  31x31 plus pustych brzegów; stałe
L = 50  #31
grid = np.zeros((L+2, L+2), int)  #siatka z wolnymi brzegami
grid_zad2 = np.zeros((L+2, L+2), int) #siatka do zad 2
height_crit = 3   #krytyczna iloć ziaren w węźle
za_duzo = height_crit + 1
t = 50000   #krok czasowy

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
       
    return grid, grid_zad2
      
           
''' 3 - czyszczenie brzegów'''
def czyszczenie_brzegow(grid) :
    
    
    return grid


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
   
 # this small if is to illustrate sand scattering principle
 '''
    if (t%100==0): 

        plt.imshow(grid_k)
        plt.show()
      
    #print(grid_zad2)
    
   '''
    
#plt.scatter(t_tab, liczba_ziaren, s=30, c='r', lw=0, marker='o')
'''
plt.figure()
cmap=plt.get_cmap('Set1')
plt.title('Histogram')
opis = []


plt.xlabel('Rozmiary lawin')
plt.ylabel('Częstoć występowania')

#A = [10, 20,30, 40, 60, 10, 30, 40, 70]
plt.hist(liczba_ziaren2, bins=50, density=True, facecolor='g', alpha=0.75)
'''
#Poprawny zapis histogramu

hist, bins = np.histogram(liczba_ziaren2, bins='auto')
plt.xscale('log')
plt.yscale('log')
plt.plot(bins[0:-1], hist, 'r--', marker='o') 

#x=bins[0:-1]
x=bins[0:-1]
y=hist
x = np.array(x, dtype=float) #transform your data in a numpy array of floats 
y = np.array(y, dtype=float) #so the curve_fit can work

def func(x, a):
    return a*x**(-1)

popt, pcov = curve_fit(func, x, y)
plt.plot(x, func(x, *popt), label='Funkcja dopasowana')
plt.legend()
'''
#przetestować generator lawn w tym przypadku
u(x) w klatce i to w x(t)
'''


















