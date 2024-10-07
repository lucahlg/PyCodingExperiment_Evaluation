from math import gcd

def encode(plain_text, a, b):
    m = 26  # Length of the alphabet
    if gcd(a, m) != 1:
        raise ValueError(f"{a} and {m} are not coprime.")
    
    encoded_text = ''
    for char in plain_text:
        if char.isalpha():  # Only encrypt alphabetic characters
            i = ord(char.lower()) - ord('a')  # Convert char to index
            encoded_char = (a * i + b) % m
            encoded_text += chr(encoded_char + ord('a'))  # Convert back to char
    return encoded_text


def decode(ciphered_text, a, b):
    m = 26  # Length of the alphabet
    if gcd(a, m) != 1:
        raise ValueError(f"{a} and {m} are not coprime.")
    
    # Find modular multiplicative inverse of a
    a_inv = pow(a, -1, m)
    
    decoded_text = ''
    for char in ciphered_text:
        if char.isalpha():  # Only decrypt alphabetic characters
            y = ord(char.lower()) - ord('a')  # Convert char to index
            decoded_char = (a_inv * (y - b)) % m
            decoded_text += chr(decoded_char + ord('a'))  # Convert back to char
    return decoded_text

# Test the affine cipher implementation
if __name__ == "__main__":
    a = 5
    b = 7
    plain_text = "test"
    ciphered_text = encode(plain_text, a, b)
    print(f"Encoded: {ciphered_text}")
    decoded_text = decode(ciphered_text, a, b)
    print(f"Decoded: {decoded_text}")
