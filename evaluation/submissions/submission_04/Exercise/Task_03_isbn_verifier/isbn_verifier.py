def is_valid(isbn):
    """
    Check if the provided string is a valid ISBN-10.
    """
    # Remove dashes from the input
    isbn = isbn.replace("-", "")

    # Check if the length is exactly 10 characters
    if len(isbn) != 10:
        return False

    # Initialize total for the checksum calculation
    total = 0

    for i in range(10):
        # Handle the case where the last character is 'X'
        if i == 9 and isbn[i] == 'X':
            value = 10
        elif isbn[i].isdigit():
            value = int(isbn[i])
        else:
            return False  # Invalid character found

        # Compute the weighted sum
        total += value * (10 - i)

    # Check if the total modulo 11 is zero
    return total % 11 == 0


