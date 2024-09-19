"""
Author: Natalia Zalewska
Date: 17.11.2021
Description: Molecular Dynamics Simulation of a Two-Dimensional Noble Gas Under Periodic Boundary Conditions
"""
import numpy as np
from matplotlib.patches import Circle
import matplotlib.pyplot as plt
N=16
boxsize=8.0
eps=1.0
sigma=1.0
promien=0.5
rc = 2.5*sigma
dt=0.01
temp=2.5
𝑘𝐵= 1
k=1
nx = 4
ny = 4
dx = 2.0
m = 0.1
V = boxsize**2/4*1
t = np.arange(0,10,dt)
class particle:
  def __init__(self,promien,pos,vel,his):
    self.promien= promien
    self.r=pos
    self.v=vel
    self.history=[]
particles= []

for i in range(nx):
  for j in range(ny):
    polozenie= np.array([(i+1)*dx+1, (j+1)*dx + 1])
    predkosc=np.array([(np.random.random()-1./2),(np.random.random() -1./2)])
    particles.append(particle(promien,polozenie,predkosc,[]) )
    
    
sumv=0.0
for p in particles:
      sumv=sumv+p.v
sumv=sumv/N   #predkosc srodka masy
for p in particles:
      p.v=(p.v-sumv)    #teraz srodek masy spoczywa


sumv2=0.0
for p in particles:
  sumv2=sumv2+np.dot(p.v,p.v)/2.0
sumv2=sumv2/N    #srednia energia kinetyczna
fs=np.sqrt(temp/sumv2)   #czynnik skalujący
for p in particles:
    p.v=p.v*fs           #sklaowanie
    
    
def closest_image(x1,x2):
  x1 = np.asarray(x1)
  x2 = np.asarray(x2)
  x12=x2-x1
  if x12[0]>boxsize/2:
    x12[0]=x12[0]-boxsize
  elif x12[0]<-boxsize/2:
    x12[0]=x12[0]+boxsize
  if x12[1]>boxsize/2:
    x12[1]=x12[1]-boxsize
  elif x12[1]<-boxsize/2:
    x12[1]=x12[1]+boxsize
  return x12

def Fx(p1,p2):
  r0 = closest_image(p1.r,p2.r)
  r = (r0[0]**2 + r0[1]**2)**(1/2) 
  if r ==0:
      return 0
  if r>rc:
      return 0
  else:
    Fx = -48*eps/(sigma*r)*((sigma/r)**14 - 1/2*(sigma/r)**8)*r0[0]
    return Fx
 
def Fy(p1,p2):
  r0 = closest_image(p1.r,p2.r)
  r = (r0[0]**2 + r0[1]**2)**(1/2) 
  if r ==0:
      return 0
  if r>rc:
      return 0
  else:
    Fy = -48*eps/(sigma**2)*((sigma/r)**14 - 1/2*(sigma/r)**8)*r0[1]
    return Fy

#Żabka start

for p1 in particles:
    rx0 = p1.r[0] - p1.v[0]*dt/2
    ry0 = p1.r[1] - p1.v[1]*dt/2
    p1.v[0] = (p1.r[0] - rx0)/dt 
    p1.v[1] = (p1.r[1] - ry0)/dt
          
for i in range(1,len(t)):
  for p1 in particles:
      Fx_sum = 0
      Fy_sum = 0
      for p2 in particles:
          if not p1==p2:
              Fx_sum += Fx(p1,p2)
              Fy_sum += Fy(p1,p2)
      p1.v[0] = p1.v[0] + Fx_sum/m*dt
      p1.v[1] = p1.v[1] + Fy_sum/m*dt
      p1.r[0] = p1.r[0] + p1.v[0]*dt
      p1.r[1] = p1.r[1] + p1.v[1]*dt
      
      K1 = (p1.v[0]**2 + p1.v[1]**2)*m
      KN = np.sum(K1)
      T = 2/(2*N*kB)*KN
      F=np.sqrt(Fx_sum**2+Fy_sum**2)
      P = N*k*T/V - 1/(2*V)*np.sum(p1.r*F)
      print(T, P) 
      
 #Żabka koniec    
      
      if p1.r[0] > boxsize:
          p1.r[0]-= boxsize
      if p1.r[0] < 0:
            p1.r[0] += boxsize
      if p1.r[1] >boxsize:
            p1.r[1] -= boxsize
      if p1.r[1] < 0:
            p1.r[1] += boxsize
            
  # animacja
         
  if (i%100==0): 
    plt.clf() 
    fig = plt.gcf() 
    for p in particles: 
        a = plt.gca() 
        cir = Circle((p.r[0],p.r[1]), radius=p.promien)  
        a.add_patch(cir) 
        plt.plot() 
    plt.xlim((0,boxsize)) 
    plt.ylim((0,boxsize))    
    fig.set_size_inches((6,6)) 
    plt.title("Symulacja gazu Lennarda-Jonesa, krok  {:03d}".format(i))
    plt.savefig("~/img{:06d}.png".format(i))
       