import unittest
from space_age import SpaceAge

class TestSpaceAge(unittest.TestCase):
    def test_age_on_earth(self):
        age = SpaceAge(1000000000)
        self.assertAlmostEqual(age.on_earth(), 31.69, places=2)
    
    def test_age_on_mercury(self):
        age = SpaceAge(1000000000)
        self.assertAlmostEqual(age.on_mercury(), 131.57, places=2)
    
    def test_age_on_venus(self):
        age = SpaceAge(1000000000)
        self.assertAlmostEqual(age.on_venus(), 51.52, places=2)
    
    def test_age_on_mars(self):
        age = SpaceAge(1000000000)
        self.assertAlmostEqual(age.on_mars(), 16.84, places=2)
    
    def test_age_on_jupiter(self):
        age = SpaceAge(1000000000)
        self.assertAlmostEqual(age.on_jupiter(), 2.66, places=2)
    
    def test_age_on_saturn(self):
        age = SpaceAge(1000000000)
        self.assertAlmostEqual(age.on_saturn(), 0.34, places=2)
    
    def test_age_on_uranus(self):
        age = SpaceAge(1000000000)
        self.assertAlmostEqual(age.on_uranus(), 0.12, places=2)
    
    def test_age_on_neptune(self):
        age = SpaceAge(1000000000)
        self.assertAlmostEqual(age.on_neptune(), 0.06, places=2)

if __name__ == '__main__':
    unittest.main()