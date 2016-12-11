from lib import solution
from lib.triangle import Triangle
import re


class Solution(solution.Solution):
    def __init__(self, nr):
        super().__init__(nr)
        self.triangle_1 = Triangle()
        self.possible_1 = 0

    def calculate(self, test=False):
        self.read_instructions()
        self.check_triangles()

    def read_instructions(self):
        self.read_input(True)

    def check_triangles(self):
        for triangle in self.input:
            sides = re.split(r'\s+', triangle.strip(' '))
            self.triangle_1.set_sides(sides)
            if self.triangle_1.is_possible():
                self.possible_1 += 1
        self.set_solution(1, self.possible_1)
