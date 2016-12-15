from lib import solution
import hashlib


class Solution(solution.Solution):
    def __init__(self, nr):
        super().__init__(nr)
        self.password = ""

    def calculate(self, test=False):
        self.read_instructions()

    def read_instructions(self):
        self.read_input()
        self.calc_password()
        self.set_solution(1, self.password)

    def calc_password(self):
        index = -1
        m = hashlib.md5()
        m.update(self.input.encode('utf-8'))
        for i in range(0, 8):
            while True:
                index += 1
                mc = m.copy()
                mc.update(str(index).encode('utf-8'))
                md5 = mc.hexdigest()
                if md5[:5] == "00000":
                    self.password += md5[5]
                    break
