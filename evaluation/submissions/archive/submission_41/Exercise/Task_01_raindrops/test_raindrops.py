import unittest
from raindrops import convert

class TestRaindrops(unittest.TestCase):
    def test_divisible_by_3(self):
        self.assertEqual(convert(3), "Pling")
        self.assertEqual(convert(6), "Pling")

    def test_divisible_by_5(self):
        self.assertEqual(convert(5), "Plang")
        self.assertEqual(convert(10), "Plang")

    def test_divisible_by_7(self):
        self.assertEqual(convert(7), "Plong")
        self.assertEqual(convert(14), "Plong")

    def test_divisible_by_3_and_5(self):
        self.assertEqual(convert(15), "PlingPlang")

    def test_divisible_by_3_and_7(self):
        self.assertEqual(convert(21), "PlingPlong")

    def test_divisible_by_5_and_7(self):
        self.assertEqual(convert(35), "PlangPlong")

    def test_not_divisible(self):
        self.assertEqual(convert(34), "34")

if __name__ == '__main__':
    unittest.main()