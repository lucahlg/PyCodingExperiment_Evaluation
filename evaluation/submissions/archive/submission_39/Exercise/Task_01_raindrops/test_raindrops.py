import unittest
from raindrops import convert

class TestRaindrops(unittest.TestCase):
    def test_3(self):
        self.assertEqual(convert(3), "Pling")
    def test_5(self):
        self.assertEqual(convert(5), "Plang")
    def test_7(self):
        self.assertEqual(convert(7), "Plong")
    def test_15(self):
        self.assertEqual(convert(15), "PlingPlang")
    def test_28(self):
        self.assertEqual(convert(28), "Plong")
    def test_34(self):
        self.assertEqual(convert(34), "34")

if __name__ == '__main__':
    unittest.main()