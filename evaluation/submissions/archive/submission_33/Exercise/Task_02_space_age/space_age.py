class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
    def on_earth(self):
        return self.seconds / 31557600
    def on_mercury(self):
        return self.on_earth() / 0.2408467
    def on_venus(self):
        return self.on_earth() / 0.61519726
    def on_mars(self):
        return self.on_earth() / 1.8808158
    def on_jupiter(self):
        return self.on_earth() / 11.862615
    def on_saturn(self):
        return self.on_earth() / 29.447498
    def on_uranus(self):
        return self.on_earth() / 84.016846
    def on_neptune(self):
        return self.on_earth() / 164.79132








