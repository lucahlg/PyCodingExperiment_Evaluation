class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth_year_in_seconds = 31557600  # One Earth year in seconds

        # Orbital periods of planets relative to Earth years
        self.orbital_periods = {
            'mercury': 0.2408467,
            'venus': 0.61519726,
            'earth': 1.0,
            'mars': 1.8808158,
            'jupiter': 11.862615,
            'saturn': 29.447498,
            'uranus': 84.016846,
            'neptune': 164.79132
        }

    def on_earth(self):
        return self._calculate_age('earth')

    def on_mercury(self):
        return self._calculate_age('mercury')

    def on_venus(self):
        return self._calculate_age('venus')

    def on_mars(self):
        return self._calculate_age('mars')

    def on_jupiter(self):
        return self._calculate_age('jupiter')

    def on_saturn(self):
        return self._calculate_age('saturn')

    def on_uranus(self):
        return self._calculate_age('uranus')

    def on_neptune(self):
        return self._calculate_age('neptune')

    def _calculate_age(self, planet):
        period = self.orbital_periods[planet]
        age = self.seconds / (self.earth_year_in_seconds * period)
        return round(age, 2)


# Creating an instance with one billion seconds
age = SpaceAge(1_000_000_000)

print(age.on_earth())    # Output: 31.69
print(age.on_mercury())  # Output: 131.57
print(age.on_venus())    # Output: 51.51
print(age.on_mars())     # Output: 16.85
print(age.on_jupiter())  # Output: 2.67
print(age.on_saturn())   # Output: 1.08
print(age.on_uranus())   # Output: 0.38
print(age.on_neptune())  # Output: 0.19


#Testing the Calculation for Earth
age_in_seconds = 1_000_000_000
earth_year_in_seconds = 31_557_600
age_on_earth = age_in_seconds / earth_year_in_seconds
rounded_age = round(age_on_earth, 2)
print(rounded_age)  # Output: 31.69
