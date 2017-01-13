# plot_Taylor_sin.py
# Computes Taylor approximations to sine function for n=1,
# n=2, n=3, n=6, n=12.
# Plots approximations together with true sine function on
# 0 < x < 4*pi
# Bjorn Gronntun (bgronntu) 20.10.16

import numpy as np
import matplotlib.pyplot as plt
from math import factorial

# Compute nth Taylor approximation for x
def S(x, n):
    return sum((-1)**j*(x**(2*j + 1))/(factorial(2*j + 1)) for j in range(n + 1))

x = np.linspace(0, 4*np.pi, 1000)

# Make plot
plt.plot(x, S(x, 1), '--', label = 'n=1')
plt.plot(x, S(x, 2), '--', label = 'n=2')
plt.plot(x, S(x, 3), '--', label = 'n=3')
plt.plot(x, S(x, 6), '--', label = 'n=6')
plt.plot(x, S(x, 12), '--', label = 'n=12')
plt.plot(x, np.sin(x), label = 'Sine function')
plt.legend(loc = 2)
plt.title('Taylor approximations to sine function')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
