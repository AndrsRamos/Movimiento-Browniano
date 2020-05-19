#brownian motion con ARREGLOS de numpy
#CODE II
"""IMPLEMENTACION
el codigo es una versión vectorizada que grafica tray=10 trayectorias del
 proceso de wiener
Cumsum es la suma acumulativa, la cual va sumando los incrementos normales(0,dt)
Cumsum por si sólo no nos permite la condicion W_0=0,
 entonces [[0]]*tray son los ceros que les hace falta a las trayectorias para
 que inicien en 0 y se los agregamos con el comando append
 axis=1 nos asegura que se agregen por columna
 (axis=0 es por fila)
"""
import numpy as np
import matplotlib.pyplot as plt
N=1000   #intervalos
T=10     #tiempo de simulacion
dt=T/N  #ancho del intervalo
tray=10 #numero de trayectorias a simular
W = np.cumsum(np.sqrt(dt) * np.random.randn(tray,N),axis=1) 
W = np.append([[0]]*tray,W, axis = 1)       #wienner process


plt.title('Brownian Motion', fontsize=22)
plt.xlabel('time', fontsize=12)
plt.ylabel('W_t', fontsize=12)
plt.grid(1)
plt.plot(W.T)
plt.show()
