def rebase(input_base, digits, output_base):
    if input_base < 2 or output_base < 2:
        raise ValueError("Bases must be >= 2")
    
    # Convert input digits to decimal
    decimal_value = 0
    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("Digit out of range for input base")
    decimal_value = 0
    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("Digit out of range for input base")
        decimal_value = decimal_value * input_base + digit

    # Convert decimal to output base
    if decimal_value == 0:
        return [0]
    
    output_digits = []
    while decimal_value > 0:
        output_digits.append(decimal_value % output_base)
        decimal_value //= output_base

    return output_digits[::-1]  # Reverse to get the correct order
