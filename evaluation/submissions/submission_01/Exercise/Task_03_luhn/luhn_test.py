from luhn import Luhn

# Test cases
valid_card = "4539 3195 0343 6467"
invalid_card = "8273 1232 7352 0569"
short_card = "123"
non_digit_card = "4539 3195 0343 646A"

# Create instances of Luhn
valid_luhn = Luhn(valid_card)
invalid_luhn = Luhn(invalid_card)
short_luhn = Luhn(short_card)
non_digit_luhn = Luhn(non_digit_card)

# Test validity
assert valid_luhn.valid() == True, "Valid card should return True"
assert invalid_luhn.valid() == False, "Invalid card should return False"
assert short_luhn.valid() == False, "Short card should return False"
assert non_digit_luhn.valid() == False, "Non-digit card should return False"

print("All tests passed!")
