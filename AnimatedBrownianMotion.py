import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
np.random.seed(1234)

def wienner(N,T):
    dt=T/N
    W = np.cumsum(np.sqrt(dt) * np.random.randn(1,N))    
    return np.append([0],W)


N = 500
X=wienner(N,10)


fig = plt.figure(figsize=(10, 5))
ax = plt.axes(xlim=(0, N), ylim=(np.min(X), np.max(X))) 
line, = ax.plot([], [], lw=2, color='red')
plt.title('Brownian Motion',fontsize=22)
plt.xlabel('Steps')
plt.ylabel('W_t')
plt.grid(1)


xdata, ydata = [], []


def animacion(i):
    y = X[i] 
    xdata.append(i) 
    ydata.append(y) 
    line.set_data(xdata, ydata) 
    return line,

	 
anim=animation.FuncAnimation(fig, animacion, frames=N, interval=20, blit=True,repeat=False)
plt.show()
anim.save('BrownianMotion.gif', writer='imagemagick', fps=60)
