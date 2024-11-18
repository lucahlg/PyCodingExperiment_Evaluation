class SpaceAge:
    # Earth year in seconds (365.25 Earth days)
    EARTH_YEAR_SECONDS = 31557600

    # Orbital periods in Earth years
    ORBITAL_PERIODS = {
        'mercury': 0.2408467,
        'venus': 0.61519726,
        'earth': 1.0,
        'mars': 1.8808158,
        'jupiter': 11.862615,
        'saturn': 29.447498,
        'uranus': 84.016846,
        'neptune': 164.79132
    }

    def __init__(self, seconds):
        """Initialize with age in seconds."""
        self.seconds = seconds
        self.earth_years = seconds / self.EARTH_YEAR_SECONDS

    def _calc_planet_years(self, planet):
        """Helper method to calculate years on any planet."""
        return round(self.earth_years / self.ORBITAL_PERIODS[planet], 2)

    def on_mercury(self):
        return self._calc_planet_years('mercury')

    def on_venus(self):
        return self._calc_planet_years('venus')

    def on_earth(self):
        return self._calc_planet_years('earth')

    def on_mars(self):
        return self._calc_planet_years('mars')

    def on_jupiter(self):
        return self._calc_planet_years('jupiter')

    def on_saturn(self):
        return self._calc_planet_years('saturn')

    def on_uranus(self):
        return self._calc_planet_years('uranus')

    def on_neptune(self):
        return self._calc_planet_years('neptune')

    # Test cases


def run_tests():
    # Test with 1 billion seconds
    space_age = SpaceAge(1000000000)

    test_cases = [
        ('Earth', space_age.on_earth(), 31.69),
        ('Mercury', space_age.on_mercury(), 131.57),
        ('Venus', space_age.on_venus(), 51.51),
        ('Mars', space_age.on_mars(), 16.85),
        ('Jupiter', space_age.on_jupiter(), 2.67),
        ('Saturn', space_age.on_saturn(), 1.08),
        ('Uranus', space_age.on_uranus(), 0.38),
        ('Neptune', space_age.on_neptune(), 0.19)
    ]

    print("Testing SpaceAge calculations:")
    for planet, calculated, expected in test_cases:
        print(f"{planet}: {calculated} years (Expected: {expected})")
        assert abs(calculated - expected) < 0.01, f"Test failed for {planet}"

    print("\nAll tests passed!")


