class Allergies:

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        allergens = ["eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"]
        return [allergens[i] for i in range(8) if (self.score & (1 << i)) > 0]
