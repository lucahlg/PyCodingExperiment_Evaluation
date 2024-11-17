import unittest
from allergies import Allergies

class TestAllergies(unittest.TestCase):
    def test_allergic_to_eggs(self):
        allergies = Allergies(1)
        self.assertTrue(allergies.allergic_to('eggs'))
        self.assertFalse(allergies.allergic_to('peanuts'))

    def test_allergic_to_peanuts(self):
        allergies = Allergies(2)
        self.assertTrue(allergies.allergic_to('peanuts'))

    def test_allergic_to_shellfish(self):
        allergies = Allergies(4)
        self.assertTrue(allergies.allergic_to('shellfish'))

    def test_allergic_to_multiple_items(self):
        allergies = Allergies(34)
        self.assertFalse(allergies.allergic_to('eggs'))
        self.assertTrue(allergies.allergic_to('chocolate'))
        self.assertFalse(allergies.allergic_to('cats'))

    def test_list_allergies(self):
        allergies = Allergies(34)
        self.assertEqual(allergies.lst, ['peanuts', 'chocolate'])

    def test_ignore_unknown_allergens(self):
        allergies = Allergies(257)
        self.assertEqual(allergies.lst, ['eggs'])

if __name__ == '__main__':
    unittest.main()