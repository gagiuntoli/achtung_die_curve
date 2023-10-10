import math

from geometry import distance, is_point_in_rectangle

def test_distance():
    assert distance([0, 0], [1, 1]) == math.sqrt(2)
    assert distance([0, 0], [0, 0]) == 0.0
    assert distance([2, 0], [0, 0]) == 2.0

def test_is_point_in_rectangle():
    assert is_point_in_rectangle([0.0, 1.0, 0.0, 1.0], [0.5, 0.5]) == True
    assert is_point_in_rectangle([0.0, 1.0, 0.0, 1.0], [1.0, 0.5]) == True
    assert is_point_in_rectangle([0.0, 1.0, 0.0, 1.0], [1.1, 0.5]) == False
    assert is_point_in_rectangle([0.0, 1.0, 0.0, 1.0], [0.5, 1.1]) == False