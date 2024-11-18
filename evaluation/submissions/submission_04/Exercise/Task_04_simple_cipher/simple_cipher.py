import random
import string

class Cipher:
    def __init__(self, key=None):
        """
        Initialize the Cipher with a given key.
        If no key is provided, generate a random key of at least 100 characters.
        """
        if key:
            self.key = key
        else:
            self.key = ''.join(random.choices(string.ascii_lowercase, k=100))

    def encode(self, text):
        """
        Encode the given text using the key.
        """
        return self._transform(text, encode=True)

    def decode(self, text):
        """
        Decode the given text using the key.
        """
        return self._transform(text, encode=False)

    def _transform(self, text, encode):
        """
        Transform the text for encoding or decoding.
        """
        result = []
        key_length = len(self.key)

        for i, char in enumerate(text):
            if char.isalpha():  # Ensure we're working with alphabetic characters
                shift = ord(self.key[i % key_length]) - ord('a')
                if not encode:
                    shift = -shift
                new_char = self._shift_char(char, shift)
                result.append(new_char)
            else:
                result.append(char)  # Preserve non-alphabetic characters

        return ''.join(result)

    def _shift_char(self, char, shift):
        """
        Shift a character by the specified amount.
        Handles wrapping for both lowercase and uppercase characters.
        """
        if char.islower():
            base = ord('a')
        elif char.isupper():
            base = ord('A')
        else:
            return char

        # Perform the shift and wrap around the alphabet
        return chr((ord(char) - base + shift) % 26 + base)


# Example with a provided key
key = "dddddddddddddddddd"
cipher = Cipher(key)

text = "iamapandabear"
encoded = cipher.encode(text)
decoded = cipher.decode(encoded)

print(f"Original: {text}")     # Output: "iamapandabear"
print(f"Encoded: {encoded}")   # Output: "ldpdsdqgdehdu"
print(f"Decoded: {decoded}")   # Output: "iamapandabear"

# Example with a random key
random_cipher = Cipher()
random_encoded = random_cipher.encode(text)
random_decoded = random_cipher.decode(random_encoded)

print(f"Random Key: {random_cipher.key}")
print(f"Encoded: {random_encoded}")
print(f"Decoded: {random_decoded}")