import unittest
from kindergarten_garden import Garden

class TestGarden(unittest.TestCase):
    def test_plants_for_alice(self):
        garden = Garden("VRCCGVRGVCGCCGVRGCVCGCGV", ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"])
        self.assertEqual(garden.plants["Alice"], ["Violets", "Radishes", "Violets", "Radishes"])
    def test_plants_for_bob(self):
        garden = Garden("VRCCGVRGVCGCCGVRGCVCGCGV", ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"])
        self.assertEqual(garden.plants["Bob"], ["Clover", "Grass", "Clover", "Clover"])

if __name__ == '__main__':
    unittest.main()