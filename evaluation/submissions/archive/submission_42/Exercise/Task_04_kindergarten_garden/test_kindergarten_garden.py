import unittest
from kindergarten_garden import Garden

class TestGarden(unittest.TestCase):
    def test_plants(self):
        garden = Garden("""[window][window][window]
VRCGVVRVCGGCCGVRGCVCGCGV
VRCCCGCRRGVCGCRVVCVGCGCV
""", ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"])
        self.assertEqual(garden.get_plants("Alice"), ["violet", "radish", "violet", "radish"])
        self.assertEqual(garden.get_plants("Bob"), ["clover", "grass", "clover", "clover"])

if __name__ == '__main__':
    unittest.main()