def encode(plain_text, a, b):
    m = 26  # Length of the alphabet
    if gcd(a, m) != 1:
        raise ValueError(f"{a} and {m} are not coprime.")
    
    encoded_text = []
    for char in plain_text:
        if char.isalpha():  # Only encrypt alphabetic characters
            i = ord(char.lower()) - ord('a')  # Convert char to index
            encoded_char = (a * i + b) % m
            encoded_text.append(chr(encoded_char + ord('a')))
        else:
            encoded_text.append(char)  # Keep non-alphabetic characters unchanged
    
    # Group the encoded text in chunks of 5
    return ' '.join([''.join(encoded_text[i:i+5]) for i in range(0, len(encoded_text), 5)])


def decode(ciphered_text, a, b):
    m = 26  # Length of the alphabet
    if gcd(a, m) != 1:
        raise ValueError(f"{a} and {m} are not coprime.")
    
    # Find the modular multiplicative inverse of a
    a_inv = pow(a, -1, m)
    
    decoded_text = []
    for char in ciphered_text.replace(' ', ''):  # Remove spaces for decoding
        if char.isalpha():  # Only decrypt alphabetic characters
            y = ord(char.lower()) - ord('a')  # Convert char to numeric value
            decoded_char = (a_inv * (y - b)) % m
            decoded_text.append(chr(decoded_char + ord('a')))
        else:
            decoded_text.append(char)  # Keep non-alphabetic characters unchanged
    
    return ''.join(decoded_text)

import math

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Example test
if __name__ == "__main__":
    a, b = 5, 7
    plain_text = "test"
    ciphered_text = encode(plain_text, a, b)
    print(f"Encoded: {ciphered_text}")
    decoded_text = decode(ciphered_text, a, b)
    print(f"Decoded: {decoded_text}")
