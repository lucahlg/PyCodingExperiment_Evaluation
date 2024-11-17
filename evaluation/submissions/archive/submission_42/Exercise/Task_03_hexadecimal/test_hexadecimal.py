import unittest
from hexadecimal import hexa

class TestHexadecimal(unittest.TestCase):
    def test_valid_hexadecimal(self):
        self.assertEqual(hexa("10af8c"), 109500)
        self.assertEqual(hexa("1"), 1)
        self.assertEqual(hexa("a"), 10)
        self.assertEqual(hexa("f"), 15)
        self.assertEqual(hexa("10"), 16)

    def test_invalid_hexadecimal(self):
        with self.assertRaises(ValueError):
            hexa("1g")
        with self.assertRaises(ValueError):
            hexa("xyz")

if __name__ == '__main__':
    unittest.main()