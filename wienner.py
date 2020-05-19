from random import gauss
from math import sqrt
import matplotlib.pyplot as plt

T=1
N=500
dt=T/N

for j in range(10):
    w=[0]*N
    time=[0]
    for i in range(N-1):
        w[i+1]=w[i]+gauss(0,sqrt(dt))
        time.append((i+1)*dt)
        
    plt.plot(time,w)

plt.title('Brownian Motion', fontsize=22)
plt.xlabel('time', fontsize=12)
plt.ylabel('W_t', fontsize=12)
plt.grid(1)
plt.show()
