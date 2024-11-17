import unittest
from acronym import abbreviate

class TestAcronym(unittest.TestCase):
    def test_abbreviate(self):
        self.assertEqual(abbreviate("As Soon As Possible"), "ASAP")
        self.assertEqual(abbreviate("Liquid-crystal display"), "LCD")
        self.assertEqual(abbreviate("Thank George It's Friday!"), "TGIF")

if __name__ == '__main__':
    unittest.main()