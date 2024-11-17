class Luhn:
    def __init__(self, card_num):
        # Implement the Luhn algorithm logic here
        total = 0
        reverse_digits = self.card_num[::-1]
        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0

    def valid(self):
        self.card_num = self.card_num.replace(' ', '')
        if len(self.card_num) <= 1:
            return False
        if not self.card_num.isdigit():
            raise ValueError('Invalid characters in card number')
        return self.check_luhn()
