import unittest
from hexadecimal import hexa

class TestHexadecimal(unittest.TestCase):
    def test_valid_hex(self):
        self.assertEqual(hexa("10af8c"), 109932)
    def test_invalid_hex(self):
        self.assertEqual(hexa("invalid"), 0)
    def test_empty_string(self):
        self.assertEqual(hexa(""), 0)

if __name__ == '__main__':
    unittest.main()