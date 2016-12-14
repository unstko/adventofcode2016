from lib import solution
import re
import collections
import operator


class Solution(solution.Solution):
    def __init__(self, nr):
        super().__init__(nr)
        self.sum1 = 0

    def calculate(self, test=False):
        self.read_instructions()
        self.calc_part1()

    def read_instructions(self):
        self.read_input(True)

    def calc_part1(self):
        for line in self.input:
            match = re.match('([a-z\-]+)-(\d+)\[([a-z]{5})\]', line)
            if match:
                name = match.group(1)
                sector_id = match.group(2)
                checksum = match.group(3)
                if self.get_checksum(name) == checksum:
                    self.sum1 += int(sector_id)
        self.set_solution(1, self.sum1)

    @staticmethod
    def get_checksum(name):
        d = collections.defaultdict(int)
        for c in name:
            if c.isalpha():
                d[c] -= 1
        s = collections.OrderedDict(sorted(d.items(), key=operator.itemgetter(1, 0)))
        checksum = "".join(str(x) for x in s)[:5]
        return checksum
