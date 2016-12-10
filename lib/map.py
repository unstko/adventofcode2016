from PIL import Image
from lib.point import Point2D


class Map:
    def __init__(self, mode, size, color, origin):
        self.origin = origin
        self.image = Image.new(mode, size, color)
        self.map = self.image.load()

    # def __getattr__(self, item, *args):
    #     try:
    #         return getattr(self.image, item)(args)
    #     except AttributeError:
    #         return False

    def show(self):
        self.image.show('Map')

    def set_point(self, point: Point2D, value):
        x = point.get_x()
        y = point.get_y()
        if self.origin == 'center':
            x += self.image.width / 2
            y += self.image.height / 2
        self.map[x, y] = value

    def get_point(self, point: Point2D):
        x = point.get_x()
        y = point.get_y()
        if self.origin == 'center':
            x += self.image.width / 2
            y += self.image.height / 2
        return self.map[x, y]
