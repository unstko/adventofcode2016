from lib import solution
import re
import collections
import operator


class Solution(solution.Solution):
    def __init__(self, nr):
        super().__init__(nr)
        self.params["room name"] = "northpole object storage"
        self.sum = 0

    def calculate(self, test=False):
        self.read_instructions()
        self.process_room_list()

    def read_instructions(self):
        self.read_input(True)

    def process_room_list(self):
        for line in self.input:
            match = re.match('([a-z\-]+)-(\d+)\[([a-z]{5})\]', line)
            if match:
                name = match.group(1)
                sector_id = int(match.group(2))
                checksum = match.group(3)
                if self.get_checksum(name) == checksum:
                    self.sum += sector_id
                    name_decrypted = self.decrypt_name(name, sector_id)
                    # print(name_decrypt)
                    if name_decrypted == self.params["room name"]:
                        self.set_solution(2, sector_id)
        self.set_solution(1, self.sum)

    @staticmethod
    def get_checksum(string):
        d = collections.defaultdict(int)
        for c in string:
            if c.isalpha():
                d[c] -= 1
        s = collections.OrderedDict(sorted(d.items(), key=operator.itemgetter(1, 0)))
        checksum = "".join(str(x) for x in s)[:5]
        return checksum

    @staticmethod
    def decrypt_name(name, shift):
        decrypted = ""
        for c in name:
            if c.isalpha():
                decrypted += chr((ord(c.lower()) - 97 + shift) % 26 + 97)
            if c == "-":
                decrypted += " "
        return decrypted
