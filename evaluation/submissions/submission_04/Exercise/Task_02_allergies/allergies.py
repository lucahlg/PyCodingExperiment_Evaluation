class Allergies:
    ALLERGENS = {
        "eggs": 1,
        "peanuts": 2,
        "shellfish": 4,
        "strawberries": 8,
        "tomatoes": 16,
        "chocolate": 32,
        "pollen": 64,
        "cats": 128,
    }


    def __init__(self, score):
        """
        Initialize with a score and determine the allergies.
        """
        self.score = score
        self._calculate_allergies()


    def _calculate_allergies(self):
        """
        Compute the list of allergens the person is allergic to.
        """
        self._allergies = [
            allergen
            for allergen, value in self.ALLERGENS.items()
            if self.score & value
        ]


    def allergic_to(self, item):
        """
        Check if the person is allergic to a specific item.
        """
        return item in self._allergies

    @property
    def lst(self):
        """
        Return the list of all allergens the person is allergic to.
        """
        return self._allergies

allergies = Allergies(34)

# Check specific allergens
print(allergies.allergic_to("peanuts"))  # Output: True
print(allergies.allergic_to("cats"))     # Output: False

# List all allergens
print(allergies.lst)