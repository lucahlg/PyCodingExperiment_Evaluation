import random

class Cipher:
    def __init__(self, key=None):
        if key:
            # Ensure the key contains only lowercase letters
            if not key.islower() or not key.isalpha():
                raise ValueError("Key must consist of lowercase letters only.")
            self.key = key
        else:
            # Manually define ascii_lowercase
            ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
            # Generate a random key of at least 100 lowercase letters
            self.key = ''.join(random.choices(ascii_lowercase, k=100))

    def encode(self, text):
        return self._transform(text, encode=True)

    def decode(self, text):
        return self._transform(text, encode=False)

    def _transform(self, text, encode=True):
        result = []
        key_length = len(self.key)

        for i, char in enumerate(text):
            if char.isalpha() and char.islower():
                shift = ord(self.key[i % key_length]) - ord('a')
                char_code = ord(char) - ord('a')

                if encode:
                    # Shift forward
                    shifted = (char_code + shift) % 26
                else:
                    # Shift backward
                    shifted = (char_code - shift) % 26

                result_char = chr(shifted + ord('a'))
                result.append(result_char)
            else:
                # Non-lowercase alphabetic characters are ignored or could raise an error
                raise ValueError("Text must contain only lowercase alphabetic characters.")

        return ''.join(result)


#Step 1
# Key corresponding to shift of 3 (since 'd' - 'a' = 3)
key = 'd' * 100  # Repeating 'd' to ensure the key is long enough

cipher = Cipher(key)

plaintext = 'iamapandabear'

encoded = cipher.encode(plaintext)
print(f"Encoded: {encoded}")  # Should output: 'ldpdsdqgdehdu'

decoded = cipher.decode(encoded)
print(f"Decoded: {decoded}")  # Should output: 'iamapandabear'


#Step 2

key = 'a' * 20
cipher = Cipher(key)

plaintext = 'iamapandabear'

encoded = cipher.encode(plaintext)
print(f"Encoded with 'a's: {encoded}")  # Should output: 'iamapandabear'

decoded = cipher.decode(encoded)
print(f"Decoded: {decoded}")  # Should output: 'iamapandabear'


#Step 3

cipher = Cipher()

plaintext = 'iamapandabear'

encoded = cipher.encode(plaintext)
print(f"Encoded with random key: {encoded}")

decoded = cipher.decode(encoded)
print(f"Decoded: {decoded}")  # Should output: 'iamapandabear'


#Test

test_keys = [
    'ddddddddddddddddddd',  # Shift of 3
    'aaaaaaaaaaaaaaaaaaa',  # Shift of 0
    None,                   # Random key
    'xyz' * 34,             # Repeating 'xyz' to make a key of length 102
]

plaintext = 'thequickbrownfoxjumpsoverthelazydog'

for key in test_keys:
    cipher = Cipher(key)
    encoded = cipher.encode(plaintext)
    decoded = cipher.decode(encoded)
    print(f"Key: {cipher.key[:10]}...")  # Print the first 10 characters of the key
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")
    print(f"Test Pass: {decoded == plaintext}")
    print('---')
