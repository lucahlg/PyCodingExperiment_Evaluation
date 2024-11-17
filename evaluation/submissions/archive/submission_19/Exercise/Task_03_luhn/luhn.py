class Luhn:
    def __init__(self, card_num):
        pass

    def valid(self):
        pass

    def check_luhn(self):
        # Implement the Luhn algorithm here
        card_num = ''.join(self.card_num.split())  # Remove spaces
        if len(card_num) <= 1 or not card_num.isdigit():
            return False
        digits = [int(d) for d in card_num]
        # Double every second digit from the right
        for i in range(len(digits) - 2, -1, -2):
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9
        return sum(digits) % 10 == 0
