import math

def norm(vector):
    [a, b] = vector
    return math.sqrt(a**2 + b**2)

def normalize_vector(vector, module):
    [a, b] = vector
    factor = module / norm(vector)
    return [a * factor, b * factor]

def is_point_in_rectangle(rect: [float, float, float, float], point):
    [xmin, xmax, ymin, ymax] = rect
    [x, y] = point
    if x >= xmin and x <= xmax and y >= ymin and y <= ymax:
        return True
    return False

def distance(p1: [float, float], p2: [float, float]) -> float:
    [x1, y1] = p1
    [x2, y2] = p2
    return norm([x2 - x1, y2 - y1])

def rotate_vector(vector, angle):
    [x_old, y_old] = vector
    x = x_old * math.cos(angle) - y_old * math.sin(angle)
    y = x_old * math.sin(angle) + y_old * math.cos(angle)
    return [x, y]
