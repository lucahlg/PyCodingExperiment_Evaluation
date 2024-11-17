def is_valid(isbn):
    if len(isbn.replace('-', '')) != 10 and len(isbn.replace('-', '')) != 13:
        return False
    total = 0
    if len(isbn.replace('-', '')) == 10:
        for i in range(10):
                if isbn[i] != '-':
            total += (10 - i) * int(isbn[i])
        return total % 11 == 0
    else:
        for i in range(12):
                    if isbn[i] != '-':
                        total += (1 + 2 * (i % 2)) * int(isbn[i])
        return total % 10 == 0
