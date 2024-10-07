from math import gcd

def encode(plain_text, a, b):
    m = 26  # Length of the alphabet
    if gcd(a, m) != 1:
        raise ValueError(f"{a} and {m} are not coprime.")
    
    cipher_text = ''
    for char in plain_text:
        if char.isalpha():
            i = ord(char.lower()) - ord('a')
            encrypted_char = (a * i + b) % m
            cipher_text += chr(encrypted_char + ord('a'))
        else:
            cipher_text += char  # Non-alphabetic characters are not encrypted
    
    # Grouping the ciphertext in chunks of 5
    return ' '.join(cipher_text[i:i+5] for i in range(0, len(cipher_text), 5))


def decode(ciphered_text, a, b):
    m = 26  # Length of the alphabet
    if gcd(a, m) != 1:
        raise ValueError(f"{a} and {m} are not coprime.")
    
    # Finding the modular multiplicative inverse of a
    a_inv = pow(a, -1, m)
    plain_text = ''
    ciphered_text = ciphered_text.replace(' ', '')  # Remove spaces for processing
    for char in ciphered_text:
        if char.isalpha():
            y = ord(char.lower()) - ord('a')
            decrypted_char = (a_inv * (y - b)) % m
            plain_text += chr(decrypted_char + ord('a'))
        else:
            plain_text += char  # Non-alphabetic characters are not encrypted
    
    return plain_text
