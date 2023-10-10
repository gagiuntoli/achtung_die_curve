from geometry import is_point_in_rectangle, distance

class quad_tree:
    def __init__(self, rectangle: [float, float, float, float], leaf_size: float, radius: float = 0.0):
        self.leaves = []
        self.points = []
        self.rectangle = rectangle

        [xmin, xmax, ymin, ymax] = rectangle

        self.rectangle_extended = [xmin - radius, xmax + radius, ymin - radius, ymax + radius]

        width, height = xmax - xmin, ymax - ymin
        assert width > 0 and height > 0, "Rectangle has invalid sizes"

        if min(width, height) > leaf_size:
            dx = width / 2.0
            dy = height / 2.0
            self.leaves.append(quad_tree([xmin, xmax - dx, ymin, ymax - dy], leaf_size, radius))
            self.leaves.append(quad_tree([xmin, xmax - dx, ymin + dy, ymax], leaf_size, radius))
            self.leaves.append(quad_tree([xmin + dx, xmax, ymin, ymax - dy], leaf_size, radius))
            self.leaves.append(quad_tree([xmin + dx, xmax, ymin + dy, ymax], leaf_size, radius))

    def get_node_for_point(self, point: [float, float]):
        if not is_point_in_rectangle(self.rectangle, point):
            return None

        node = self
        while node.leaves != []:
            for leaf in node.leaves:
                if is_point_in_rectangle(leaf.rectangle, point):
                    node = leaf
        return node

    def get_height(self):
        height = 1
        node = self
        while node.leaves != []:
            height += 1
            node = node.leaves[0]
        return height

    def insert_point(self, point: [float, float]):
        if self.leaves == []:
            if is_point_in_rectangle(self.rectangle_extended, point):
                self.points.append(point)
            else:
                return None
        else:
            for node in self.leaves:
                if is_point_in_rectangle(node.rectangle_extended, point):
                    node.insert_point(point)
                
    def check_collision(self, point: [float, float], radius: float):
        node = self.get_node_for_point(point)
        if node == None:
            return False

        for vpoint in node.points:
            if distance(point, vpoint) < radius:
                return True
        return False
