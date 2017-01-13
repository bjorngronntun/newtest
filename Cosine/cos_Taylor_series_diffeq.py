# cos_Taylor_series_diffeq.py
# Computes some Taylor approximations to cosine function,
# and plots the results
# Bjorn Gronntun (bgronntu), 30.10.16

import numpy as np
import matplotlib.pyplot as plt

# Computes nth Taylor approximation to cosine at x.
# Returns: List containing approximation and error term.
def cos_Taylor(x, n):
    index_set = range(n + 1)
    a = np.zeros(len(index_set))
    s = np.zeros(len(index_set))

    a[0] = 1
    s[0] = a[0]
    for i in index_set[1:]:
        a[i] = -(x**2)/((2*i)*(2*i - 1))*a[i - 1]
        s[i] = s[i - 1] + a[i]

    error = -(x**2)/((2*(n + 1))*(2*(n + 1) - 1))*a[-1]
    return s[-1], error

# Test function
def test_cos_Taylor():
    expected = 0.5
    computed = cos_Taylor(np.pi/3, 2)[0]
    epsilon = 0.01
    success = abs(expected - computed) < epsilon
    msg = 'Excpected: %g. Computed: %g.' %(expected, computed)
    assert success, msg

# Make plots:
x = np.linspace(-np.pi,np.pi,100)
for n in range(1, 4):
    y = np.zeros(len(x))
    for i in range(len(x)):
        y[i] = cos_Taylor( x[i], n)[0]
    new_label = 'n = {}'.format(n)
    plt.plot(x,y, label = new_label)

plt.plot(x, np.cos(x), '.', label='True cosine function')
plt.legend()
plt.title('Taylor approximations to cosine')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
