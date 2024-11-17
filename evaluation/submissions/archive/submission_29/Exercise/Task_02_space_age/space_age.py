class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
    EARTH_YEAR = 31557600
    ORBITAL_PERIODS = {
        'Mercury': 0.2408467,
        'Venus': 0.61519726,
        'Earth': 1.0,
        'Mars': 1.8808158,
        'Jupiter': 11.862615,
        'Saturn': 29.447498,
        'Uranus': 84.016846,
        'Neptune': 164.79132
    }
    def age_on_planet(self, planet):
        return round(self.seconds / (self.EARTH_YEAR * self.ORBITAL_PERIODS[planet]), 2)
