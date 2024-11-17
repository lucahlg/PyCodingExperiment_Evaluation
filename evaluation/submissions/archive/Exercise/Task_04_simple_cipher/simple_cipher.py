import random
import string

class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key = ''.join(random.choices(string.ascii_lowercase, k=100))
        else:
            self.key = key.lower()

    def encode(self, text):
        def encode(self, text):
    encoded = []
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(self.key[i % len(self.key)]) - ord('a')
            encoded_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
            encoded.append(encoded_char)
        else:
            encoded.append(char)
    return ''.join(encoded)

def decode(self, text):
    decoded = []
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(self.key[i % len(self.key)]) - ord('a')
            decoded_char = chr((ord(char.lower()) - ord('a') - shift) % 26 + ord('a'))
            decoded.append(decoded_char)
        else:
            decoded.append(char)
    return ''.join(decoded)

    def decode(self, text):
        reverse_key = {v: k for k, v in zip(self.key, string.ascii_lowercase)}
        return ''.join(reverse_key[char] if char in reverse_key else char for char in text)
