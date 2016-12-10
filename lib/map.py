from PIL import Image
from lib.point import Point2D


class Map:
    def __init__(self, mode, size, color, origin):
        """
        Create new map
        :param mode: Image mode
        :param size: Image size
        :param color: Image color
        :param origin: Origin of coordinate system (top left, top right, bottom left, bottom right, center)
        """
        self.origin = origin
        self.image = Image.new(mode, size, color)
        self.map = self.image.load()
        self.min = Point2D(0, 0)
        self.max = Point2D(0, 0)

    # def __getattr__(self, item, *args):
    #     try:
    #         return getattr(self.image, item)(args)
    #     except AttributeError:
    #         return False

    def show(self):
        image = self.image.copy()
        if self.origin == 'center' or self.origin == 'bottom left' or self.origin == 'bottom right':
            image = self.image.transpose(Image.FLIP_TOP_BOTTOM)
        if self.origin == 'bottom right' or self.origin == 'top right':
            image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        image.show('Map')

    def set_point(self, point: Point2D, value):
        x = point.get_x()
        y = point.get_y()
        if self.origin == 'center':
            x += self.image.width / 2
            y += self.image.height / 2
        self.map[x, y] = value
        self.update_min_and_max(point)

    def get_point(self, point: Point2D):
        x = point.get_x()
        y = point.get_y()
        if self.origin == 'center':
            x += self.image.width / 2
            y += self.image.height / 2
        return self.map[x, y]

    def update_min_and_max(self, point: Point2D):
        x = point.get_x()
        y = point.get_y()
        if x > self.max.get_x():
            self.max.set_x(x)
        elif x < self.min.get_x():
            self.min.set_x(x)
        if y > self.max.get_y():
            self.max.set_y(y)
        elif y < self.min.get_y():
            self.min.set_y(y)

    def get_min(self):
        return self.min

    def get_max(self):
        return self.max

    def print_min_and_max(self):
        print("Map minimum: {}".format(self.min))
        print("Map maximum: {}".format(self.max))
