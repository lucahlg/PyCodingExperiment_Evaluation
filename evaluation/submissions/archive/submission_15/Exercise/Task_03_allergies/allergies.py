class Allergies:

    def __init__(self, score):
        self.score = score
        self.allergens = [
            ('eggs', 1),
            ('peanuts', 2),
            ('shellfish', 4),
            ('strawberries', 8),
            ('tomatoes', 16),
            ('chocolate', 32),
            ('pollen', 64),
            ('cats', 128)
        ]
        pass

    def allergic_to(self, item):
        for allergen, value in self.allergens:
            if allergen == item and (self.score & value) != 0:
                return True
        return False
        pass

    @property
    def lst(self):
        return [allergen for allergen, value in self.allergens if (self.score & value) != 0]
        pass
