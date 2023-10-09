import math

def is_point_in_rectangle(rect: [float, float, float, float], point):
    [xmin, xmax, ymin, ymax] = rect
    [x, y] = point
    if x >= xmin and x <= xmax and y >= ymin and y <= ymax:
        return True
    return False

def distance(p1: [float, float], p2: [float, float]) -> float:
    [x1, y1] = p1
    [x2, y2] = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)