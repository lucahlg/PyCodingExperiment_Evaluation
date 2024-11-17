def hexa(hex_string):
    decimal_value = 0
    hex_string = hex_string.lower()
    hex_digits = '0123456789abcdef'
    for index, digit in enumerate(reversed(hex_string)):
        if digit not in hex_digits:
            raise ValueError('Invalid hexadecimal string')
        decimal_value += hex_digits.index(digit) * (16 ** index)
    return decimal_value
