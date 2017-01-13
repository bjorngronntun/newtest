import numpy as np
import matplotlib.pyplot as plt
import time, glob, os

for name in glob.glob('533/tmp_*.pdf'):
    os.remove(name)

def f(x,t):
    return np.exp(-(x-3*t)**2)*np.sin(3*np.pi*(x-t))

x=np.linspace(-6,6,1001)
tmin=-1;tmax=1
t_values=np.linspace(tmin,tmax,60)
ymax=1


plt.ion()
y = f(x, tmax)
lines = plt.plot(x, y)
plt.axis([-6, 6, -2, 2])
plt.xlabel('x')
plt.ylabel('f')
plt.legend(['s=%4.2f' % tmax])


counter = 0
for t in t_values:
    y = f(x,t)
    lines[0].set_ydata(y)
    plt.legend(['t=%4.2f' % t])
    plt.draw()
    plt.savefig('533/tmp_%04d.png' % counter)
    counter += 1



"""
[fenics@ubuntu64-box] ~ > python plot_wavepacket_movie.py &
[1] 2627

[fenics@ubuntu64-box] ~ > convert -delay 17 533/tmp*.png movie.gif

"""
