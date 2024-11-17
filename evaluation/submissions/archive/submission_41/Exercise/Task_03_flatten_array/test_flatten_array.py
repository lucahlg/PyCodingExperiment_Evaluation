import unittest
from flatten_array import flatten

class TestFlattenArray(unittest.TestCase):
    def test_flatten_simple(self):
        self.assertEqual(flatten([1, 2, 3]), [1, 2, 3])

    def test_flatten_nested(self):
        self.assertEqual(flatten([1, [2, 3], 4]), [1, 2, 3, 4])

    def test_flatten_with_none(self):
        self.assertEqual(flatten([1, [2, None], 4]), [1, 2, 4])

    def test_flatten_deeply_nested(self):
        self.assertEqual(flatten([1, [2, [3, None], 4], 5]), [1, 2, 3, 4, 5])

    def test_flatten_all_none(self):
        self.assertEqual(flatten([None, [None], None]), [])

if __name__ == '__main__':
    unittest.main()