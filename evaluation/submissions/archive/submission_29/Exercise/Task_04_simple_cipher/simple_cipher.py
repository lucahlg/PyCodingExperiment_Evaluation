class Cipher:
    def __init__(self, key=None):
        import random
        import string
        
        if key is None:
            key = ''.join(random.choices(string.ascii_lowercase, k=100))
        self.key = key

    def encode(self, text):
        pass
    def encode(self, text):
        encoded = ""
        for i in range(len(text)):
            shift = ord(self.key[i % len(self.key)]) - ord('a')
            encoded += chr((ord(text[i]) - ord('a') + shift) % 26 + ord('a'))
        return encoded

    def decode(self, text):
        decoded = ""
        for i in range(len(text)):
            shift = ord(self.key[i % len(self.key)]) - ord('a')
            decoded += chr((ord(text[i]) - ord('a') - shift) % 26 + ord('a'))
        return decoded
