def hexa(hex_string):
    # Convert hexadecimal to decimal
    hex_string = hex_string.lower()
    decimal_value = 0
    hex_digits = '0123456789abcdef'
    for i, digit in enumerate(reversed(hex_string)):
        if digit not in hex_digits:
            raise ValueError(f'Invalid hexadecimal digit: {digit}')
        decimal_value += hex_digits.index(digit) * (16 ** i)
    return decimal_value
