def encode(plain_text, a, b):
    m = 26  # Length of the alphabet
    # Check if a and m are coprime
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    if gcd(a, m) != 1:
        raise ValueError(f"{a} and {m} are not coprime.")

    # Encrypt the plain text
    cipher_text = ''
    for char in plain_text:
        if char.isalpha():  # Only encrypt alphabetic characters
            i = ord(char.lower()) - ord('a')  # Convert char to index
            encrypted_index = (a * i + b) % m
            cipher_char = chr(encrypted_index + ord('a'))
            cipher_text += cipher_char
    return cipher_text


def decode(ciphered_text, a, b):
    m = 26  # Length of the alphabet

    # Function to find modular multiplicative inverse
    def mod_inverse(a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        raise ValueError(f"No modular inverse for {a} under modulo {m}.")

    # Calculate the modular inverse of a
    a_inv = mod_inverse(a, m)

    # Decrypt the ciphered text
    plain_text = ''
    for char in ciphered_text:
        if char.isalpha():  # Only decrypt alphabetic characters
            y = ord(char.lower()) - ord('a')  # Convert char to numeric value
            decrypted_index = (a_inv * (y - b)) % m
            plain_char = chr(decrypted_index + ord('a'))
            plain_text += plain_char
    return plain_text
