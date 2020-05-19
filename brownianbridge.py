##wienner bridge
from math import sqrt
from random import gauss
import matplotlib.pyplot as plt


tau=1
dt=0.01

for j in range(10):
    w=[0]
    for i in range(int(tau/dt)-1):
        w.append(w[i]+gauss(0,sqrt(dt)))
    Wbridge=[0]
    time=[0]
    for i in range(int(tau/dt)-1):
        t=(i+1)*dt
        Wbridge.append(w[i+1]-t/tau*w[int(tau/dt)-1])
        time.append(t)
        
    plt.plot(time,Wbridge)
plt.title('Brownian Bridge', fontsize=22)
plt.xlabel('steps', fontsize=12)
plt.ylabel('WB_t', fontsize=12)
plt.grid(1)
plt.show()
