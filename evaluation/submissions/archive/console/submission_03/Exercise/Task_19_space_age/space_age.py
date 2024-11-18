class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth_years = seconds / 31557600
        self.planets = {
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
        return self.earth_years / self.planets[planet]

    def __getattr__(self, planet):
        if planet in self.planets:
            return self.age_on_planet(planet)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{planet}'")