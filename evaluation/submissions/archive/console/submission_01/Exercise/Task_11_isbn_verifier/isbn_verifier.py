def is_valid(isbn):
    # Remove dashes from the ISBN
    isbn = isbn.replace('-', '')

    # Check if the length is 10
    if len(isbn) != 10:
        return False

    # Calculate the checksum
    total = 0
    for i in range(10):
        if isbn[i] == 'X':
            total += 10 * (10 - i)
        else:
            total += int(isbn[i]) * (10 - i)

    # Validate the checksum
    return total % 11 == 0
