class Luhn:
    def __init__(self, card_num):
        """Initialize with card number string."""
        self.card_num = card_num

    def valid(self):
        """Check if the number is valid per the Luhn formula."""
        # Remove spaces and store cleaned number
        cleaned = self.card_num.replace(" ", "")

        # Check length
        if len(cleaned) <= 1:
            return False

        # Check if all characters are digits
        if not cleaned.isdigit():
            return False

        # Convert to list of integers and reverse for easier processing
        digits = [int(d) for d in reversed(cleaned)]

        # Double every second digit and subtract 9 if > 9
        for i in range(1, len(digits), 2):
            doubled = digits[i] * 2
            digits[i] = doubled - 9 if doubled > 9 else doubled

        # Return True if sum is divisible by 10
        return sum(digits) % 10 == 0

# Example usage:
# Valid card number
number = Luhn("4539 3195 0343 6467")
print(number.valid())  # True

# Invalid card number
number = Luhn("8273 1232 7352 0569")
print(number.valid())  # False

# Test cases
test_cases = [
    "1",  # False (too short)
    "",  # False (empty)
    "0",  # False (too short)
    " ",  # False (invalid)
    "a",  # False (invalid character)
    "059",  # True
    "59",  # True
    "055 444 285",  # True
    "234 567 891 234",  # False
    "059a",  # False (invalid character)
    "055-444-285",  # False (invalid character)
    "055# 444$ 285"  # False (invalid character)
]

for test in test_cases:
    luhn = Luhn(test)
    print(f"'{test}' is {'valid' if luhn.valid() else 'invalid'}")


