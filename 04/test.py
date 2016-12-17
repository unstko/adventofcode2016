from lib import test


class Test(test.Test):
    @classmethod
    def setUpClass(cls):
        cls.nr = '04'

    def test_1(self):
        test_input = """aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]"""
        self.execute_test(test_input)
        self.assertEqual(1514, self.solution.get_solution(1))

    def test_2(self):
        test_input = """qzmt-zixmtkozy-ivhz-343[zimth]"""
        self.set_param("room name", "very encrypted name")
        self.execute_test(test_input)
        self.assertEqual(343, self.get_solution(2))
