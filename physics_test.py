from physics import distance2

TOL = 1.0e-10

def test_distance():
    assert(abs(distance2([0, 0], [1, 1]) - 2.0) < TOL)
    assert(abs(distance2([0, 0], [0, 0]) - 0.0) < TOL)
    assert(abs(distance2([2, 0], [0, 0]) - 4.0) < TOL)