import unittest
from isbn_verifier import is_valid

class TestISBNVerifier(unittest.TestCase):
    def test_valid_isbn10(self):
        self.assertTrue(is_valid("3-598-21508-8"))
    def test_invalid_isbn10(self):
        self.assertFalse(is_valid("3-598-21507-X"))
    def test_valid_isbn13(self):
        self.assertTrue(is_valid("978-3-16-148410-0"))
    def test_invalid_isbn13(self):
        self.assertFalse(is_valid("978-3-16-148410-1"))
    def test_invalid_length(self):
        self.assertFalse(is_valid("12345"))

if __name__ == '__main__':
    unittest.main()