from lib import test


class Test(test.Test):
    @classmethod
    def setUpClass(cls):
        cls.nr = '05'

    def test_1(self):
        test_input = "abc"
        self.execute_test(test_input)
        self.assertEqual("18f47a30", self.solution.get_solution(1))
        self.assertEqual("05ace8e3", self.solution.get_solution(2))
