def hexa(hex_string):
    hex_string = hex_string.lower()
    hex_digits = "0123456789abcdef"
    decimal_value = 0
    for index, digit in enumerate(reversed(hex_string)):
        if digit not in hex_digits:
            raise ValueError(f"Invalid hexadecimal digit: {digit}")
        decimal_value += hex_digits.index(digit) * (16 ** index)
    return decimal_value
