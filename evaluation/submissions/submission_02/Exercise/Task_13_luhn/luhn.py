class Luhn:
    def __init__(self, card_num):
        pass

    def valid(self):
        # Strip spaces and check length
        card_num = self.card_num.replace(' ', '')
        if len(card_num) <= 1:
            return False

        # Check for non-digit characters
        if not card_num.isdigit():
            return False

        # Implement Luhn algorithm
        total = 0
        reverse_digits = card_num[::-1]
        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0
