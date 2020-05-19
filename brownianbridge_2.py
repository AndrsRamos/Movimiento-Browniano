#wienner bridge vectorizado
import numpy as np
import matplotlib.pyplot as plt

tau=1 #periodo del puente 
N=300 #numero de intervalos
dt=tau/N #tamaño de los intervalos
tray=5 #numero de realizaciones del WiennerBridge (WB)


WB= np.empty((tray,N+1))  #iniciamos matriz
w = np.cumsum(np.sqrt(dt) * np.random.randn(tray, N), axis=1)
w = np.append([[0]]*tray,w,axis=1)

for i in range(N+1):
    WB[:,i]= w[:,i] -(i*dt/tau)*w[:,N]
plt.plot(WB.T)
plt.title('Brownian Bridge', fontsize=22)
plt.xlabel('steps', fontsize=12)
plt.ylabel('WB_t', fontsize=12)
plt.grid(1)
plt.show()
