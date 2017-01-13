# fortune_and_inflation.py
# Solves system of difference equation, in order to compute
# future fortune, given initial fortune F, interest p,
# infation rate I, percentage of interest consumed q and
# number of years N
# Bjorn Gronntun (bgronntu) 20.10.16

import numpy as np
import matplotlib.pyplot as plt
def compute_fortune(F, p, q, I, N):
    x = np.zeros(N)
    c = np.zeros(N)
    x[0] = F
    c[0] = p*q/(10**4)*F
    for n in range(1, N):
        x[n] = x[n - 1] + p/100*x[n - 1] - c[n - 1]
        c[n] = c[n - 1] + I/100*c[n - 1]
    return x

F = 10000       # Initial fortune
p = 3.9         # Annual interest
I = 2.8         # Inflation
q = 77.0        # Percentage of interest consumed
N = 20          # Number of years

x = compute_fortune(F, p, q, I, N)

# Make plot of x:
plt.plot(x)
plt.title('Making a living from a fortune')
plt.xlabel('Years')
plt.ylabel('Fortune')
plt.show()
