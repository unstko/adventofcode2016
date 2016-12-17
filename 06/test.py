from lib import test


class Test(test.Test):
    @classmethod
    def setUpClass(cls):
        cls.nr = '06'

    def test_1(self):
        test_input = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"""
        self.execute_test(test_input)
        self.assertEqual("easter", self.solution.get_solution(1))
        self.assertEqual("advent", self.solution.get_solution(2))
