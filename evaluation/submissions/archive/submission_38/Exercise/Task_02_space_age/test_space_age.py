import unittest
from space_age import SpaceAge

class TestSpaceAge(unittest.TestCase):
    def test_age_on_earth(self):
        age = SpaceAge(1000000000)
        self.assertAlmostEqual(age.on_earth(), 31.68808781402616, places=7)

    def test_age_on_mercury(self):
        age = SpaceAge(1000000000)
        self.assertAlmostEqual(age.on_mercury(), 131.56953287725742, places=7)

    def test_age_on_venus(self):
        age = SpaceAge(1000000000)
        self.assertAlmostEqual(age.on_venus(), 51.50882468824545, places=7)

    def test_age_on_mars(self):
        age = SpaceAge(1000000000)
        self.assertAlmostEqual(age.on_mars(), 16.848054878116695, places=7)

    def test_age_on_jupiter(self):
        age = SpaceAge(1000000000)
        self.assertAlmostEqual(age.on_jupiter(), 2.6712565327315225, places=7)

    def test_age_on_saturn(self):
        age = SpaceAge(1000000000)
        self.assertAlmostEqual(age.on_saturn(), 1.0760876124018737, places=7)

    def test_age_on_uranus(self):
        age = SpaceAge(1000000000)
        self.assertAlmostEqual(age.on_uranus(), 0.37716350140100413, places=7)

    def test_age_on_neptune(self):
        age = SpaceAge(1000000000)
        self.assertAlmostEqual(age.on_neptune(), 0.1922922142624317, places=7)

if __name__ == '__main__':
    unittest.main()