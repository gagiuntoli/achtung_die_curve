
def is_point_in_rectangle(rect: [float, float, float, float], point):
    [xmin, xmax, ymin, ymax] = rect
    [x, y] = point
    if x >= xmin and x <= xmax and y >= ymin and y <= ymax:
        return True
    return False