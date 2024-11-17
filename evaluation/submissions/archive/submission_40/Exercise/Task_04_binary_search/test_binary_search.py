import unittest
from binary_search import find

class TestBinarySearch(unittest.TestCase):
    def test_find(self):
        self.assertEqual(find([4, 8, 12, 16, 23, 28, 32], 23), 4)
        self.assertEqual(find([4, 8, 12, 16, 23, 28, 32], 4), 0)
        self.assertEqual(find([4, 8, 12, 16, 23, 28, 32], 32), 6)
        self.assertEqual(find([4, 8, 12, 16, 23, 28, 32], 100), -1)

if __name__ == '__main__':
    unittest.main()