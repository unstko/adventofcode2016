from lib import solution
import hashlib


class Solution(solution.Solution):
    def __init__(self, nr):
        super().__init__(nr)
        self.password1 = ""
        self.password2 = list("--------")

    def calculate(self, test=False):
        self.read_instructions()

    def read_instructions(self):
        self.read_input()
        self.calc_passwords()

    def calc_passwords(self):
        pos1 = 0
        calced2 = 0
        index = -1
        m = hashlib.md5()
        m.update(self.input.encode('utf-8'))
        while not self.is_calculated(1) or not self.is_calculated(2):
            while True:
                index += 1
                mc = m.copy()
                mc.update(str(index).encode('utf-8'))
                md5 = mc.hexdigest()
                if md5[:5] == "00000":
                    if not self.is_calculated(1):
                        self.password1 += md5[5]
                        pos1 += 1
                    if pos1 > 7:
                        self.set_solution(1, self.password1)
                    if not self.is_calculated(2):
                        if md5[5].isdigit() and -1 < int(md5[5]) < 8:
                            if self.password2[int(md5[5])] == "-":
                                self.password2[int(md5[5])] = md5[6]
                                calced2 += 1
                    if calced2 > 7:
                        self.set_solution(2, "".join(self.password2))
                    break
