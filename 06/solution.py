from lib import solution


class Solution(solution.Solution):
    def __init__(self, nr):
        super().__init__(nr)

    def calculate(self, test=False):
        self.read_instructions()

    def read_instructions(self):
        self.read_input(True)
