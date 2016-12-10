from lib import solution
from lib.point import Point2D
from lib.map import Map
import copy


class Solution(solution.Solution):
    def __init__(self, nr):
        super().__init__(nr)
        self.instructions = []
        self.directions = ['N', 'E', 'S', 'W']
        self.face = 0
        self.source = Point2D(0, 0)
        self.destination = Point2D(0, 0)
        self.distance = 0
        self.map = Map('RGB', (350, 350), 0, 'center')

    def calculate(self, test=False):
        self.test = test
        self.map_init()
        self.read_instructions()
        self.calc_destination()
        self.calc_distance()
        self.map_result()

    def map_init(self):
        self.map.set_point(self.source, (0, 255, 0))

    def map_result(self):
        if not self.test:
            self.map.show()
            self.map.print_min_and_max()

    def read_instructions(self):
        self.read_input()
        self.instructions = self.input.split(', ')

    def calc_destination(self):
        for instruction in self.instructions:
            self.calc_face(instruction)
            self.move_destination(instruction)
            self.set_and_check_path()

    def calc_face(self, instruction):
        turn = instruction[0]
        move = 1
        if turn == 'L':
            move = -1
        self.face = (self.face + move) % len(self.directions)

    def move_destination(self, instruction):
        blocks = int(instruction[1:])
        direction = self.get_direction()
        self.source = copy.copy(self.destination)
        if direction == 'N':
            self.destination.move(0, blocks)
        elif direction == 'S':
            self.destination.move(0, -1 * blocks)
        elif direction == 'E':
            self.destination.move(blocks, 0)
        elif direction == 'W':
            self.destination.move(-1 * blocks, 0)

    def get_direction(self):
        return self.directions[self.face]

    def calc_distance(self):
        self.distance = self.destination.manhattan_distance(Point2D(0, 0))
        self.set_solution(1, self.distance)

    def set_and_check_path(self):
        if not self.is_calculated(2):
            x_src = self.source.get_x()
            y_src = self.source.get_y()
            x_dst = self.destination.get_x()
            y_dst = self.destination.get_y()
            direction = self.get_direction()
            step = 1
            if direction == 'S' or direction == 'W':
                step = -1
            range_x = range(x_src, x_dst+step, step)
            range_y = range(y_src, y_dst+step, step)
            for x in range_x:
                if x == x_src:
                    continue
                point = Point2D(x, y_dst)
                check = self.set_and_check_point(point)
                if check:
                    return
            for y in range_y:
                if y == y_src:
                    continue
                point = Point2D(x_dst, y)
                check = self.set_and_check_point(point)
                if check:
                    return

    def set_and_check_point(self, point: Point2D):
        check = False
        if self.map.get_point(point) == (255, 255, 255):
            self.map.set_point(point, (255, 0, 0))
            distance = point.manhattan_distance(Point2D(0, 0))
            self.set_solution(2, distance)
            check = True
        else:
            self.map.set_point(point, (255, 255, 255))
        return check
