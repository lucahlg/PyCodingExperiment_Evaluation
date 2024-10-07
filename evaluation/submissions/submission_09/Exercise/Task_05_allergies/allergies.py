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
        self.allergy_list = [item for item, value in self.allergens.items() if score & value]

    def allergic_to(self, item):
        return item in self.allergy_list

    @property
    def lst(self):
        return self.allergy_list
