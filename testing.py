def b(t):
    return 0.01 if t < 6 else 0.002
def test_b():
    tol = 1E-14
    ex = 0.002
    com = b(10)
    success = abs(ex - com) < tol
    msg = 'Expected: %g. Computed: %g' %(ex, com)
    assert success, msg
test_b()
