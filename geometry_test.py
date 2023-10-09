import math

from geometry import distance

def test_distance():
    assert distance([0, 0], [1, 1]) == math.sqrt(2)
    assert distance([0, 0], [0, 0]) == 0.0
    assert distance([2, 0], [0, 0]) == 2.0