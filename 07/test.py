from lib import test


class Test(test.Test):
    @classmethod
    def setUpClass(cls):
        cls.nr = '07'

    def test_1(self):
        test_input = """abba[mnop]qrst"""
        self.execute_test(test_input)
        self.assertEqual(1, self.solution.get_solution(1))

    def test_2(self):
        test_input = """abcd[bddb]xyyx"""
        self.execute_test(test_input)
        self.assertEqual(0, self.solution.get_solution(1))

    def test_3(self):
        test_input = """aaaa[qwer]tyui"""
        self.execute_test(test_input)
        self.assertEqual(0, self.solution.get_solution(1))

    def test_4(self):
        test_input = """ioxxoj[asdfgh]zxcvbn"""
        self.execute_test(test_input)
        self.assertEqual(1, self.solution.get_solution(1))

    def test_5(self):
        test_input = """aba[bab]xyz"""
        self.execute_test(test_input)
        self.assertEqual(1, self.solution.get_solution(2))

    def test_6(self):
        test_input = """xyx[xyx]xyx"""
        self.execute_test(test_input)
        self.assertEqual(0, self.solution.get_solution(2))

    def test_7(self):
        test_input = """aaa[kek]eke"""
        self.execute_test(test_input)
        self.assertEqual(1, self.solution.get_solution(2))

    def test_8(self):
        test_input = """zazbz[bzb]cdb"""
        self.execute_test(test_input)
        self.assertEqual(1, self.solution.get_solution(2))
