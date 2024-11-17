class Cipher:
    def __init__(self, key=None):
        if key is None:
            import random
            import string
            self.key = ''.join(random.choices(string.ascii_lowercase, k=100))
        else:
            self.key = key

    def encode(self, text):
        encoded = ''
        for i, char in enumerate(text):
            if char.isalpha():
                shift = ord(self.key[i % len(self.key)]) - ord('a')
                encoded += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encoded += char
        return encoded

    def decode(self, text):
        decoded = ''
        for i, char in enumerate(text):
            if char.isalpha():
                shift = ord(self.key[i % len(self.key)]) - ord('a')
                decoded += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decoded += char
        return decoded
