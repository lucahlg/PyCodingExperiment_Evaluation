def hexa(hex_string):
    decimal_value = 0
    hex_digits = '0123456789abcdef'
    hex_string = hex_string.lower()

    for i, digit in enumerate(reversed(hex_string)):
        if digit not in hex_digits:
            return 'Invalid hexadecimal string'
        decimal_value += hex_digits.index(digit) * (16 ** i)

    return decimal_value
