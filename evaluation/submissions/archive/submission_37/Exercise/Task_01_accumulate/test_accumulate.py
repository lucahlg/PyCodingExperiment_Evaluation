import unittest
from accumulate import accumulate

class TestAccumulate(unittest.TestCase):
    def test_accumulate_squares(self):
        self.assertEqual(accumulate([1, 2, 3, 4, 5], lambda x: x * x), [1, 4, 9, 16, 25])
    
    def test_accumulate_doubles(self):
        self.assertEqual(accumulate([1, 2, 3], lambda x: x * 2), [2, 4, 6])

if __name__ == '__main__':
    unittest.main()