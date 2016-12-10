class Solution:
    def __init__(self, nr):
        self.nr = nr
        self.test = False
        self.input = ""
        self.solution = ["(not calculated)", "(not calculated)"]
        self.calculated = [False, False]

    def __str__(self):
        return "Solution 1: {}\nSolution 2: {}".format(self.solution[0], self.solution[1])

    def calculate(self, test=False):
        raise NotImplementedError('users must define calculate to use this base class')

    def get_solution(self, nr):
        if nr in [1, 2]:
            return self.solution[nr-1]

    def set_solution(self, nr, value):
        if nr in [1, 2]:
            self.solution[nr-1] = value
            self.calculated[nr-1] = True

    def is_calculated(self, nr):
        if nr in [1, 2]:
            return self.calculated[nr-1]

    def read_input(self):
        with open(self.nr+"/input.txt", "r") as f:
            self.input = f.read()
