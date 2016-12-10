from lib import solution


class Solution(solution.Solution):
    def __init__(self, nr):
        super().__init__(nr)

    def calculate(self, test=False):
        self.read_instructions()
        self.set_solution(1, '0000')

    def read_instructions(self):
        self.read_input(True)
