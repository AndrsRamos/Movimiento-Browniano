import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
np.random.seed(1234)

def wbridge(N,tau):
    dt=tau/N
    WB= np.empty(N+1)
    w = np.cumsum(np.sqrt(dt) * np.random.randn(1, N))
    w = np.append(0,w)
    for i in range(N+1):
        WB[i]= w[i] -(i*dt/tau)*w[N]
    return WB

def animacion(i):
    y = X[i] 
    xdata.append(i) 
    ydata.append(y) 
    line.set_data(xdata, ydata) 
    return line,

N = 500
X=wbridge(N-1,1)


fig = plt.figure(figsize=(10, 5))
ax = plt.axes(xlim=(0, N), ylim=(np.min(X), np.max(X))) 
line, = ax.plot([], [], lw=2, color='red')
plt.title('Brownian Bridge',fontsize=22)
plt.xlabel('Steps')
plt.ylabel('WB_t')
plt.grid(1)


xdata, ydata = [], []
	 
anim=animation.FuncAnimation(fig, animacion, frames=N, interval=20, blit=True,repeat=False)
plt.show()
#anim.save('wbridge.gif', writer='imagemagick', fps=60)
