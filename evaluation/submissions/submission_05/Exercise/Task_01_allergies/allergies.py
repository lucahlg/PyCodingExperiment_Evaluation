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
        return item in self.lst

    @property
    def lst(self):
        return [allergen for allergen, value in self.allergens.items() if value & self.score]
