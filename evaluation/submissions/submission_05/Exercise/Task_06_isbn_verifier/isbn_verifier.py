def is_valid(isbn):
    # Remove dashes
    isbn = isbn.replace('-', '')

    # Check length
    if len(isbn) != 10:
        return False

    # Calculate the checksum
    total = 0
    for i in range(9):
        total += int(isbn[i]) * (10 - i)

    # Check the last character
    if isbn[9] == 'X':
        total += 10
    else:
        total += int(isbn[9])

    # Validate
    return total % 11 == 0
