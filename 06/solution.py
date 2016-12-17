from lib import solution
from lib.dict import Dict


class Solution(solution.Solution):
    def __init__(self, nr):
        super().__init__(nr)
        self.length = 1
        self.dicts = []
        self.message = ""

    def calculate(self, test=False):
        self.read_instructions()
        self.init_dicts()
        self.calc_message()

    def read_instructions(self):
        self.read_input(True)
        if len(self.input):
            self.length = len(self.input[0])

    def init_dicts(self):
        for i in range(0, self.length):
            self.dicts.append(i)
            self.dicts[i] = Dict()

    def calc_message(self):
        for line in self.input:
            i = 0
            for char in line:
                if i < self.length:
                    self.dicts[i].add(char)
                    i += 1
        for i in range(0, self.length):
            self.message += self.dicts[i].get_sorted_string_by_value_and_key(1)
        self.set_solution(1, self.message)
