import unittest
from flatten_array import flatten

class TestFlattenArray(unittest.TestCase):
    def test_flatten_nested_list(self):
        self.assertEqual(flatten([1, [2, 3, None, 4], [None], 5]), [1, 2, 3, 4, 5])

    def test_flatten_empty_list(self):
        self.assertEqual(flatten([]), [])

    def test_flatten_no_nones(self):
        self.assertEqual(flatten([1, 2, 3]), [1, 2, 3])

    def test_flatten_all_nones(self):
        self.assertEqual(flatten([None, [None], None]), [])

    def test_flatten_complex_structure(self):
        self.assertEqual(flatten([1, [2, [3, None], 4], 5]), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()