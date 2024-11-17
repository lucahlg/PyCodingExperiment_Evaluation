class Cipher:
    def __init__(self, key=None):
        self.key = key if key else self.generate_random_key()
        self.key = self.key.lower()
        if not all(c.islower() for c in self.key):
            raise ValueError('Key must only contain lowercase letters')

    def generate_random_key(self):
        import random
        import string
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(100))

    def encode(self, text):
        return ''.join(self.shift_character(c, i) for i, c in enumerate(text))

    def decode(self, text):
        return ''.join(self.shift_character(c, -i) for i, c in enumerate(text))

    def shift_character(self, char, index):
        if char.isalpha():
            shift = ord(self.key[index % len(self.key)]) - ord('a')
            return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        return char

    def decode(self, text):
        pass
