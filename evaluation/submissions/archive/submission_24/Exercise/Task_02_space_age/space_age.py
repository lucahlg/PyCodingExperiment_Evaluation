class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth_years = seconds / 31557600
        self.planets = {
            'mercury': 0.2408467,
            'venus': 0.61519726,
            'earth': 1.0,
            'mars': 1.8808158,
            'jupiter': 11.862615,
            'saturn': 29.447498,
            'uranus': 84.016846,
            'neptune': 164.79132
        }
    def age_on(self, planet):
        return round(self.earth_years / self.planets[planet], 2)
