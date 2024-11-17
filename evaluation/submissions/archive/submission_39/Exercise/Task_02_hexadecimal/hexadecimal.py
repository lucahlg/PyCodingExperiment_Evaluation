def hexa(hex_string):
    try:
        
        if not hex_string:
            return 0
        decimal_value = 0
        hex_length = len(hex_string)
        for i, char in enumerate(hex_string):
                decimal_value += int(char, 16) * (16 ** (hex_length - i - 1))
                return decimal_value
    except ValueError:
                return 0
        return 0
