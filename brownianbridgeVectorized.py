#wienner bridge vectorizado
import numpy as np
import matplotlib.pyplot as plt

tau=1 #periodo del puente 
N=500 #numero de intervalos
dt=tau/N #tamaño de los intervalos
tray=10 #numero de realizaciones del WiennerBridge (WB)


WB= np.empty((tray,N))  #iniciamos matriz
w = np.cumsum(np.sqrt(dt) * np.random.randn(tray, N), axis=1)
w = np.append([[0]]*tray,w,axis=1)

for i in range(N):
    WB[:,i]= w[:,i] -(i*dt/tau)*w[:,N]
plt.plot(WB.T)
plt.show()
