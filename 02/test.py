from lib.test import Test


class Test02(Test):
    @classmethod
    def setUpClass(cls):
        cls.nr = '02'

    def test_1(self):
        test_input = """ULL
RRDDD
LURDL
UUUUD"""
        self.execute_test(test_input)
        self.assertEqual('1985', self.solution.get_solution(1))
        self.assertEqual('5DB3', self.solution.get_solution(2))
