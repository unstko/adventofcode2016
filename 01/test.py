from lib.test import Test


class Test01(Test):
    @classmethod
    def setUpClass(cls):
        cls.nr = '01'

    def test_1(self):
        test_input = "R2, L3"
        self.execute_test(test_input)
        self.assertEqual(self.solution.get_solution(1), 5)

    def test_2(self):
        test_input = "R2, R2, R2"
        self.execute_test(test_input)
        self.assertEqual(self.get_solution(1), 2)

    def test_3(self):
        test_input = "R5, L5, R5, R3"
        self.execute_test(test_input)
        self.assertEqual(self.get_solution(1), 12)

    def test_4(self):
        test_input = "R8, R4, R4, R8"
        self.execute_test(test_input)
        self.assertEqual(self.get_solution(2), 4)
