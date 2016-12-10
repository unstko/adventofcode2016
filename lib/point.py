import math


class Point2D:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return "{}, {}".format(self.x, self.y)

    def __neg__(self):
        return Point2D(-self.x, -self.y)

    def __add__(self, point):
        return Point2D(self.x+point.x, self.y+point.y)

    def __sub__(self, point):
        return self + -point

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def euclidean_distance(self, point):
        dx = self.x - point.x
        dy = self.y - point.y
        return math.hypot(dx, dy)

    def manhattan_distance(self, point):
        dx_abs = math.fabs(self.x - point.x)
        dy_abs = math.fabs(self.y - point.y)
        return int(dx_abs + dy_abs)
