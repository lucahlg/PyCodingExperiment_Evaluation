def is_valid(isbn):
    # Remove dashes
    isbn = isbn.replace('-', '')
    # Check length
    if len(isbn) != 10:
        return False
    # Calculate checksum
    total = 0
    for i in range(10):
        if isbn[i] == 'X':
            total += 10 * (10 - i)
        else:
            total += int(isbn[i]) * (10 - i)
    return total % 11 == 0
