#brownian motion con ARREGLOS de numpy
import numpy as np
import matplotlib.pyplot as plt
N=100
T=1
dt=T/N
trayectorias=10


w=np.empty((trayectorias,N))
w[:,0]=0
for i in range(N-1):
    w[:,i+1]=w[:,i]+np.random.randn(trayectorias)*np.sqrt(dt)


plt.title('Brownian Motion', fontsize=22)
plt.xlabel('time', fontsize=12)
plt.ylabel('W_t', fontsize=12)
plt.grid(1)
plt.plot(w.T)
plt.show()
