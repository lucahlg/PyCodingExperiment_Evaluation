class Allergies:

    def __init__(self, score):
        self.score = score
        self.allergens_dict = {
            "eggs": 1,
            "peanuts": 2,
            "shellfish": 4,
            "strawberries": 8,
            "tomatoes": 16,
            "chocolate": 32,
            "pollen": 64,
            "cats": 128
        }

    def allergic_to(self, item):
        return self.score & self.allergens_dict[item] != 0

    @property
    def lst(self):
        return [allergen for allergen, value in self.allergens_dict.items() if self.score & value]

allergies = Allergies(34)
print("Allergic to peanuts:", allergies.allergic_to("peanuts"))
print("Allergic to cats:", allergies.allergic_to("cats"))
print("List of allergies:", allergies.lst)