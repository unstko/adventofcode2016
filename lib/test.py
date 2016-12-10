import unittest
from unittest.mock import mock_open, patch
import solution


class Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        self.nr = ""

    def setUp(self):
        self.solution = solution.Solution(self.nr)

    def tearDown(self):
        print(self._testMethodName+":")
        print(self.solution)
        print("")

    def execute_test(self, test_input):
        mocked_open_function = mock_open(read_data=test_input)
        with patch("builtins.open", mocked_open_function):
            self.solution.calculate(True)

    def get_solution(self, nr):
        return self.solution.get_solution(nr)
