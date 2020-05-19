import numpy as np
import matplotlib.pyplot as plt
N=500       #intervalos
T=1        #tiempo de simulacion
dt=T/N      #ancho del intervalo
tray=100     #numero de trayectorias a simular
mu=0.15        #deriva
sigma=.3    #volatilidad
S_0=20       #valor inicial



S=np.empty((tray,N))
S[:,0]=S_0
for i in range(N-1):
    S[:,i+1]=S[:,i]*np.exp((mu-0.5*sigma**2)*dt + np.random.randn(tray)*np.sqrt(dt)*sigma)

plt.title('Geom Brownian Motion', fontsize=22)
plt.xlabel('time', fontsize=12)
plt.ylabel('S_t', fontsize=12)
plt.grid(1)
plt.plot(S.T)
plt.show()
