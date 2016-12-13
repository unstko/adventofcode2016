import json


class Keypad:
    def __init__(self, start=5):
        self.button = start
        self.code = ''
        self.custom = None

    def load_custom(self, file):
        with open(file) as fp:
            self.custom = json.load(fp)

    def move(self, direction):
        if self.custom is None:
            self.move_std(direction)
        else:
            self.move_custom(direction)

    def move_std(self, direction):
        button = 0
        if direction == 'U':
            button = self.button - 3
        elif direction == 'D':
            button = self.button + 3
        elif direction == 'L':
            if self.button not in (4, 7):
                button = self.button - 1
        elif direction == 'R':
            if self.button not in (3, 6):
                button = self.button + 1
        if 0 < button < 10:
            self.button = button

    def move_custom(self, direction):
        if str(self.button) in self.custom:
            if str(direction) in self.custom[str(self.button)]:
                self.button = self.custom[str(self.button)][str(direction)]

    def press(self):
        self.code += str(self.button)

    def get_code(self):
        return self.code
