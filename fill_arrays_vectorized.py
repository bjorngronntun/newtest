# fill_arrays_vectorized.py
# Defines a function h,
# creates an numpy array x and computes associated h values
# Bjorn Gronntun (bgronntu) 30.09.16

import numpy as np
from numpy import sqrt, pi, exp
def h(x):
    return 1.0/sqrt(2*pi)*exp(-0.5*x**2)

lower_bound = -4
upper_bound = 4
n = 41  # Number of points

x = np.linspace(lower_bound, upper_bound, n)
y = h(x)
