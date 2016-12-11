from lib import solution
import re


class Solution(solution.Solution):
    def __init__(self, nr):
        super().__init__(nr)
        self.compares = ([0, 1, 2], [0, 2, 1], [1, 2, 0])
        self.possible = 0

    def calculate(self, test=False):
        self.read_instructions()
        self.check_triangles()

    def read_instructions(self):
        self.read_input(True)

    def check_triangles(self):
        for triangle in self.input:
            sides = re.split(r'\s+', triangle.strip(' '))
            if self.check_triangle(sides):
                self.possible += 1
        self.set_solution(1, self.possible)

    def check_triangle(self, sides):
        for compare in self.compares:
            if int(sides[compare[0]]) + int(sides[compare[1]]) <= int(sides[compare[2]]):
                return False
        return True
