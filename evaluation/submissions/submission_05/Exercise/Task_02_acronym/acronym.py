def abbreviate(words):
    """
    Convert a phrase to its acronym.

    Args:
        text (str): The input phrase to convert to an acronym

    Returns:
        str: The acronym generated from the input phrase

    Examples:
        >>> abbreviate('As Soon As Possible')
        'ASAP'
        >>> abbreviate('Liquid-crystal display')
        'LCD'
        >>> abbreviate("Thank George It's Friday!")
        'TGIF'
    """
    # Replace hyphens with spaces since they're word separators
    text = words.replace('-', ' ')

    # Remove all punctuation except spaces
    cleaned_text = ''.join(char for char in text if char.isalnum() or char.isspace())

    # Split into words and get first letter of each word
    words = cleaned_text.split()
    acronym = ''.join(word[0].upper() for word in words if word)

    return acronym


# Test cases
def run_tests():
    test_cases = [
        ("As Soon As Possible", "ASAP"),
        ("Liquid-crystal display", "LCD"),
        ("Thank George It's Friday!", "TGIF"),
        ("Portable Network Graphics", "PNG"),
        ("GNU Image Manipulation Program", "GIMP"),
        ("Something - I made up from-scratch", "SIMFS"),
        ("Complementary metal-oxide semiconductor", "CMOS"),
        ("Rolling On Floor Laughing", "ROFL"),
    ]

    for phrase, expected in test_cases:
        result = abbreviate(phrase)
        assert result == expected, f"Expected {expected}, but got {result} for input: {phrase}"
        print(f"Input: {phrase}")
        print(f"Output: {result}\n")


if __name__ == "__main__":
    run_tests()