def hexa(hex_string):
    # Validate input
    if not isinstance(hex_string, str):
        raise ValueError("Input must be a string")

    # Remove '0x' prefix if present
    hex_string = hex_string.lower().strip()
    if hex_string.startswith('0x'):
        hex_string = hex_string[2:]

    # Define valid hex characters and their decimal values
    hex_values = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15
    }

    # Validate all characters are valid hex
    if not all(c in hex_values for c in hex_string):
        raise ValueError("Invalid hexadecimal string")

    # Convert to decimal using positional notation
    decimal = 0
    power = 0

    # Process each character from right to left
    for digit in reversed(hex_string):
        decimal += hex_values[digit] * (16 ** power)
        power += 1

    return decimal


print(hexa("2af"))