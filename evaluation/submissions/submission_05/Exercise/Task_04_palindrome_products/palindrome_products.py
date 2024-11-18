def largest(min_factor=0, max_factor=None):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    largest_palindrome = None
    factors = []

    # Start from highest possible values for optimal performance
    for i in range(max_factor, min_factor - 1, -1):
        # We can start j from i to avoid duplicate factor pairs
        for j in range(i, min_factor - 1, -1):
            product = i * j

            # If we already found a larger palindrome, we can skip
            if largest_palindrome and product < largest_palindrome:
                break

            if is_palindrome(product):
                if largest_palindrome is None or product > largest_palindrome:
                    largest_palindrome = product
                    factors = [(j, i)]
                elif product == largest_palindrome:
                    factors.append((j, i))

    return (largest_palindrome, factors)


def smallest(min_factor=0, max_factor=None):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    smallest_palindrome = None
    factors = []

    # Start from lowest possible values for optimal performance
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j

            # If we already found a smaller palindrome, we can skip
            if smallest_palindrome and product > smallest_palindrome:
                break

            if is_palindrome(product):
                if smallest_palindrome is None or product < smallest_palindrome:
                    smallest_palindrome = product
                    factors = [(i, j)]
                elif product == smallest_palindrome:
                    factors.append((i, j))

    return (smallest_palindrome, factors)


# Example test cases
def test_palindrome_products():
    # Test case 1: Range [1, 9]
    result = smallest(min_factor=1, max_factor=9)
    print(f"Smallest palindrome in range [1, 9]: {result}")
    assert result == (1, [(1, 1)])

    result = largest(min_factor=1, max_factor=9)
    print(f"Largest palindrome in range [1, 9]: {result}")
    assert result == (9, [(1, 9), (3, 3)])

    # Test case 2: Range [10, 99]
    result = smallest(min_factor=10, max_factor=99)
    print(f"\nSmallest palindrome in range [10, 99]: {result}")
    assert result == (121, [(11, 11)])

    result = largest(min_factor=10, max_factor=99)
    print(f"Largest palindrome in range [10, 99]: {result}")
    assert result == (9009, [(91, 99)])

    # Test error case
    try:
        result = largest(min_factor=10, max_factor=9)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        print(f"\nCorrectly caught ValueError: {e}")
        assert str(e) == "min must be <= max"


if __name__ == "__main__":
    test_palindrome_products()