# fill_arrays_loop.py
# Defines a function h,
# Creates two empty lists and fills them with x values and h values
# Bjorn Gronntun (bgronntu) 30.09.16

from math import sqrt, pi, exp
def h(x):
    return 1.0/sqrt(2*pi)*exp(-0.5*x**2)

lower_bound = -4
upper_bound = 4
n = 41      # number of points

interval_length = (upper_bound - lower_bound)/float(n - 1)
x = []
y = []
for j in range(n):
    x_value = lower_bound + j*interval_length
    x.append(x_value)
    y.append(h(x_value))
