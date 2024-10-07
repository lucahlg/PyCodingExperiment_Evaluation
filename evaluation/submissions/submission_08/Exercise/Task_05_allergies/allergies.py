class Allergies:

    def __init__(self, score):
        self.score = score
        self.allergens = {
            'eggs': 1,
            'peanuts': 2,
            'shellfish': 4,
            'strawberries': 8,
            'tomatoes': 16,
            'chocolate': 32,
            'pollen': 64,
            'cats': 128
        }

    def allergic_to(self, item):
        return (self.allergens[item] & self.score) > 0

    @property
    def lst(self):
        return [item for item, value in self.allergens.items() if (value & self.score) > 0]
