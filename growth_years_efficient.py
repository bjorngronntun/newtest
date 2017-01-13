# Test comment...

# growth_years_efficient.py
# Computes how much an initial amount x0 will grow to
# in N years, assuming interest rate p.
# Writes result to file 'data.dat'
# Bjorn Gronntun (bgronntu), 23.10.16

x0 = 100    # initial amount
p = 5       # interest rate
N = 4       # number of years

counter = 0
current = x0
outfile = open('data.dat', 'w')

# Header
outfile.write('%-5s%10s\n' %('Year', 'Amount'))

# Compute interest and write to file
while counter < N + 1:
    outfile.write('%-5d%10.2f\n' %(counter, current))
    current = current + (p/100.0)*current
    counter += 1
outfile.close()
