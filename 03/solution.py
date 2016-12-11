from lib import solution
from lib.triangle import Triangle
import re


class Solution(solution.Solution):
    def __init__(self, nr):
        super().__init__(nr)
        self.triangle_1 = Triangle()
        self.possible_1 = 0
        self.triangles_2 = [Triangle(), Triangle(), Triangle()]
        self.possible_2 = 0

    def calculate(self, test=False):
        self.read_instructions()
        self.check_triangles()

    def read_instructions(self):
        self.read_input(True)

    def check_triangles(self):
        group_part = 0
        for triangle in self.input:
            sides = re.split(r'\s+', triangle.strip(' '))
            self.triangle_1.set_sides(sides)
            if self.triangle_1.is_possible():
                self.possible_1 += 1
            for nr in range(0, 3):
                self.triangles_2[nr].set_side(group_part, sides[nr])
            if group_part == 2:
                for nr in range(0, 3):
                    if self.triangles_2[nr].is_possible():
                        self.possible_2 += 1
            group_part = (group_part + 1) % 3
        self.set_solution(1, self.possible_1)
        self.set_solution(2, self.possible_2)
