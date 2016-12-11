from lib.test import Test


class Test03(Test):
    @classmethod
    def setUpClass(cls):
        cls.nr = '03'

    def test_1(self):
        test_input = "5 10 25"
        self.execute_test(test_input)
        self.assertEqual(0, self.solution.get_solution(1))
