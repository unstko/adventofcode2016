class Keypad:
    def __init__(self, start=5):
        self.button = start
        self.code = ''

    def move(self, direction):
        button = 0
        if direction == 'U':
            button = self.button - 3
        elif direction == 'D':
            button = self.button + 3
        elif direction == 'L':
            button = self.button - 1
        elif direction == 'R':
            button = self.button + 1
        if 0 < button < 10:
            self.button = button

    def press(self):
        self.code += str(self.button)

    def get_code(self):
        return self.code
