import unittest
from allergies import Allergies

class TestAllergies(unittest.TestCase):
    def test_allergic_to(self):
        allergies = Allergies(34)
        self.assertTrue(allergies.allergic_to('peanuts'))
        self.assertTrue(allergies.allergic_to('chocolate'))
        self.assertFalse(allergies.allergic_to('cats'))

    def test_lst(self):
        allergies = Allergies(34)
        self.assertEqual(allergies.lst, ['peanuts', 'chocolate'])

if __name__ == '__main__':
    unittest.main()