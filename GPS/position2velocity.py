# posititon2velocity.py
# Reads position data from file, computes velocities in x and y
# directions, plots positions and velocities.
# Bjorn Gronntun (bgronntu), 28.10.16
import numpy as np
import matplotlib.pyplot as plt

# Read data from file:
infile = open('src/plot/pos.dat', 'r')
s = float(infile.readline())
x, y = [], []
for line in infile:
    x.append(float(line.split()[0]))
    y.append(float(line.split()[1]))
infile.close()

x = np.array(x)
y = np.array(y)
time = s*np.array(range(len(x) - 1))

# Compute velocities by discrete differentiation:
v_x = np.zeros(len(x) - 1)
v_y = np.zeros(len(y) - 1)
for i in range(len(x) - 1):
    v_x[i] = (x[i + 1] - x[i])/s
    v_y[i] = (y[i + 1] - y[i])/s

# Make plots
plt.subplot(3,1,1)
plt.title('x versus y position')
plt.plot(x, y)
plt.subplot(3,1,2)
plt.title('Time versus x velocity')
plt.plot(time, v_x)
plt.subplot(3,1,3)
plt.title('Time versus y velocity')
plt.plot(time, v_y)
plt.tight_layout()
plt.show()
