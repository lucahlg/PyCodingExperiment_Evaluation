class Luhn:
    def __init__(self, number):
        self.number = number.replace(' ', '')  # Remove spaces from the input

    def is_valid(self):
        # Input must be more than one character and contain only digits
        if len(self.number) <= 1 or not self.number.isdigit():
            return False

        total = 0
        # Process digits starting from the right
        for idx, digit in enumerate(reversed(self.number)):
            n = int(digit)
            # Double every second digit from the right
            if idx % 2 == 1:
                n *= 2
                # Subtract 9 from numbers over 9
                if n > 9:
                    n -= 9
            total += n

        # Valid if total sum is divisible by 10
        return total % 10 == 0


#example

number = '4539 3195 0343 6467'
luhn = Luhn(number)
print(luhn.is_valid())  # Output: True

#example 2

number = '8273 1232 7352 0569'
luhn = Luhn(number)
print(luhn.is_valid())  # Output: False


#Test Cases

test_numbers = [
    ('4539 3195 0343 6467', True),  # Valid
    ('8273 1232 7352 0569', False), # Invalid
    ('059', True),                  # Valid
    ('055 444 285', True),          # Valid
    ('055-444-285', False),         # Invalid (contains invalid characters)
    ('0', False),                   # Invalid (length <= 1)
    ('091', True),                  # Valid
    (' 0', False),                  # Invalid (after stripping spaces, length <= 1)
]

for num, expected in test_numbers:
    luhn = Luhn(num)
    result = luhn.is_valid()
    print(f"Number: '{num}', Expected: {expected}, Result: {result}, Pass: {expected == result}")
