class Character:
    def __init__(self):
        self.abilities = self.generate_abilities()
        self.hitpoints = 10 + modifier(self.abilities['constitution'])

    def generate_abilities(self):
        import random
        abilities = {}
        for ability in ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']:
            rolls = sorted([random.randint(1, 6) for _ in range(4)])
            abilities[ability] = sum(rolls[1:])  # Sum the largest three dice
        return abilities

def modifier(value):
    if value <= 3:
        return -4
    elif value <= 5:
        return -3
    elif value <= 7:
        return -2
    elif value <= 9:
        return -1
    elif value <= 11:
        return 0
    elif value <= 13:
        return 1
    elif value <= 15:
        return 2
    elif value <= 17:
        return 3
    else:
        return 4
