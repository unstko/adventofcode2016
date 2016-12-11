class Triangle:
    def __init__(self):
        self.sides = [0, 0, 0]

    def set_sides(self, lengths: list):
        if len(lengths) > 2:
            for side in range(0, 3):
                self.sides[side] = lengths[side]

    def set_side(self, side, length):
        if 0 <= side < 3:
            self.sides[side] = length

    def get_side(self, side):
        length = 0
        if 0 <= side < 3:
            length = self.sides[side]
        return length

    def is_possible(self):
        possible = True
        side_compares = ([0, 1, 2], [0, 2, 1], [1, 2, 0])
        for compare in side_compares:
            if int(self.sides[compare[0]]) + int(self.sides[compare[1]]) <= int(self.sides[compare[2]]):
                possible = False
                break
        return possible
