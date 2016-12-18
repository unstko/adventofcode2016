from lib import solution
import re


class Solution(solution.Solution):
    def __init__(self, nr):
        super().__init__(nr)
        self.match_outside = re.compile(r'([^[\]]+)(?:$|\[)')
        self.match_inside = re.compile(r'\[(.*?)\]')
        self.match_abba = re.compile(r'.*(.)(?!\1)(.)\2\1.*')
        self.count1 = 0

    def calculate(self, test=False):
        self.read_instructions()
        self.check_ips()

    def read_instructions(self):
        self.read_input(True)

    def check_ips(self):
        for line in self.input:
            words_outside = self.match_outside.findall(line)
            words_inside = self.match_inside.findall(line)
            if self.contains_abba(words_outside) and not self.contains_abba(words_inside):
                self.count1 += 1
        self.set_solution(1, self.count1)

    def contains_abba(self, words):
        contains = False
        if words:
            for word in words:
                if self.match_abba.match(word):
                    contains = True
                    break
        return contains
