def rebase(input_base, digits, output_base):
    if input_base < 2 or output_base < 2:
        raise ValueError('Bases must be >= 2')
    
    # Convert digits from input_base to decimal
    decimal_value = 0
    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError('Digit out of range for input base')
    for digit in digits:
        decimal_value = decimal_value * input_base + digit
    if decimal_value == 0:
        return [0]  # Special case for zero
    # No need for a zero check here, it will be handled later

    # Convert decimal to output_base
    if decimal_value == 0:
        return [0]  # Special case for zero

    output_digits = []
    while decimal_value > 0:
        output_digits.append(decimal_value % output_base)
        decimal_value //= output_base

    output_digits.reverse()  # Reverse to get the correct order
    return output_digits
