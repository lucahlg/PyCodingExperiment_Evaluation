class Allergies:

    def __init__(self, score):
        self.score = score
        self.allergens = [
        (1, 'eggs'),
    (2, 'peanuts'),
    (4, 'shellfish'),
    (8, 'strawberries'),
    (16, 'tomatoes'),
    (32, 'chocolate'),
    (64, 'pollen'),
    (128, 'cats')
]
            (1, 'eggs'),
            (2, 'peanuts'),
            (4, 'shellfish'),
            (8, 'strawberries'),
            (16, 'tomatoes'),
            (32, 'chocolate'),
            (64, 'pollen'),
            (128, 'cats')
        ]
            (1, 'eggs'),
            (2, 'peanuts'),
            (4, 'shellfish'),
            (8, 'strawberries'),
            (16, 'tomatoes'),
            (32, 'chocolate'),
            (64, 'pollen'),
            (128, 'cats')
        ]

    def allergic_to(self, item):
        item_score = dict(self.allergens).get(item.lower())
        print(f"Score: {self.score}, Item Score: {item_score}")
        return item_score is not None and (self.score & item_score) != 0

    @property
    def lst(self):
        return [allergen for score, allergen in self.allergens if (self.score & score) != 0]
