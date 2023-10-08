from physics import distance2

class quad_tree:
    def __init__(self, width: float, height: float, leaf_size: float):
        self.leaves = []
        self.points = []
        self.width = width
        self.height = height
        if width > leaf_size or height > leaf_size:
            for _ in range(4):
                self.leaves.append(quad_tree(width / 2, height / 2, leaf_size))

    def get_node_for_point(self, point: [float, float]):
        [x, y] = point
        if x < 0 or x > self.width or y < 0 or y > self.height:
            return None

        node = self
        xmin, xmax, dx = 0.0, node.width, node.width / 2.0
        ymin, ymax, dy = 0.0, node.height, node.height / 2.0

        while node.leaves != []:
            if x >= xmin and x <= xmax - dx and y >= ymin and y <= ymax - dy:
                xmax -= dx
                ymax -= dy
                node = node.leaves[0]
            elif x >= xmin and x <= xmax - dx and y >= ymin + dy and y <= ymax:
                xmax -= dx
                ymin += dy
                node = node.leaves[1]
            elif x >= xmin + dx and x <= xmax and y >= ymin and y <= ymax - dy:
                xmin += dx
                ymax -= dy
                node = node.leaves[2]
            elif x >= xmin + dx and x <= xmax and y >= ymin + dy and y <= ymax:
                xmin += dx
                ymin += dy
                node = node.leaves[3]
            
            return node

    def insert_point(self, point: [float, float]):
        node = self.get_node_for_point(point)

        if node != None:
            node.points.append(point)
            return True
        else:
            return None
                
    def check_collision(self, point: [float, float], radius2):
        node = self.get_node_for_point(point)
        if node == None:
            return False

        for vpoint in node.points:
            if distance2(point, vpoint) < radius2:
                return True
        return False
