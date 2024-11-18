class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        if len(self.card_num) <= 1 or not self.card_num.isdigit(): 
            return False 
        total_sum = 0 
        num_digits = len(self.card_num) 
        parity = num_digits % 2 
        for i, digit in enumerate(self.card_num): 
            n = int(digit) 
            if i % 2 == parity: 
                n *= 2 
                if n > 9: 
                    n -= 9 
            total_sum += n 
        return total_sum % 10 == 0

number1 = "4539 3195 0343 6467" 
luhn1 = Luhn(number1) 
print(f"Is the number {number1} valid? {luhn1.is_valid()}")

number2 = "8273 1232 7352 0569" 
luhn2 = Luhn(number2) 
print(f"Is the number {number2} valid? {luhn2.is_valid()}")