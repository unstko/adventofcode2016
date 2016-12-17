import collections
import operator


class Dict:
    def __init__(self):
        self.dict = collections.defaultdict(int)

    def reset(self):
        self.dict.clear()

    def add(self, key):
        self.dict[key] -= 1

    def get_sorted_string_by_value_and_key(self, length, reverse=False):
        sorted_list = self.get_sorted_list_by_value_and_key(reverse)
        return "".join(str(x) for x in sorted_list)[:length]

    def get_sorted_list_by_value_and_key(self, reverse=False):
        return collections.OrderedDict(sorted(self.dict.items(), key=operator.itemgetter(1, 0), reverse=reverse))
