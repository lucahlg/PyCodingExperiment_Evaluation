class Robot:
    def __init__(self):
import random
import string

class Robot:
    existing_names = set()

    def __init__(self):
        self.name = self.generate_unique_name()

    def generate_unique_name(self):
        while True:
            name = f"{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.randint(100, 999)}"
            if name not in Robot.existing_names:
                Robot.existing_names.add(name)
                return name

    def reset_name(self):
        self.name = self.generate_unique_name()
