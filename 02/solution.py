from lib import solution
from lib.keypad import Keypad
import os


class Solution(solution.Solution):
    def __init__(self, nr):
        super().__init__(nr)
        self.keypad1 = Keypad()
        self.keypad2 = Keypad()

    def calculate(self, test=False):
        self.read_instructions()
        self.init_keypads()
        self.calc_code()
        self.set_solution(1, self.keypad1.get_code())
        self.set_solution(2, self.keypad2.get_code())

    def read_instructions(self):
        self.read_input(True)

    def init_keypads(self):
        self.keypad2.load_custom(os.path.dirname(__file__)+'/keypad_part2.json')

    def calc_code(self):
        for line in self.input:
            for direction in line:
                self.keypad1.move(direction)
                self.keypad2.move(direction)
            self.keypad1.press()
            self.keypad2.press()
