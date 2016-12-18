from lib import solution
import re


class Solution(solution.Solution):
    def __init__(self, nr):
        super().__init__(nr)
        self.match_outside = re.compile(r'([^[\]]+)(?:$|\[)')
        self.match_inside = re.compile(r'\[(.*?)\]')
        self.match_abba = re.compile(r'.*(.)(?!\1)(.)\2\1.*')
        self.match_aba = re.compile(r'(?=((.)(?!\2)(.)\2))\w')
        self.count1 = 0
        self.count2 = 0

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
            aba_ouside = self.findall_aba(words_outside)
            aba_inside = self.findall_aba(words_inside)
            if self.exists_corresponding_aba(aba_ouside, aba_inside):
                self.count2 += 1
        self.set_solution(1, self.count1)
        self.set_solution(2, self.count2)

    def contains_abba(self, words):
        contains = False
        if words:
            for word in words:
                if self.match_abba.match(word):
                    contains = True
                    break
        return contains

    def findall_aba(self, words):
        list_aba = []
        if words:
            for word in words:
                match = self.match_aba.findall(word)
                if match:
                    for m in match:
                        list_aba.append(m[0])
        return list_aba

    @staticmethod
    def exists_corresponding_aba(words1, words2):
        exists = False
        for word in words1:
            word_correspond = ""+word[1]+word[0]+word[1]
            if word_correspond in words2:
                exists = True
                break
        return exists
