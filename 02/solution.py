from lib import solution
from lib.keypad import Keypad


class Solution(solution.Solution):
    def __init__(self, nr):
        super().__init__(nr)
        self.keypad = Keypad()

    def calculate(self, test=False):
        self.read_instructions()
        self.calc_code()
        self.set_solution(1, self.keypad.get_code())

    def read_instructions(self):
        self.read_input(True)

    def calc_code(self):
        for line in self.input:
            for direction in line:
                self.keypad.move(direction)
            self.keypad.press()
