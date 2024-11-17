import unittest
from simple_cipher import Cipher

class TestCipher(unittest.TestCase):
    def test_encode(self):
        cipher = Cipher("dddd")
        self.assertEqual(cipher.encode("iamapandabear"), "ldpdsdqgdehdu")

    def test_decode(self):
        cipher = Cipher("dddd")
        self.assertEqual(cipher.decode("ldpdsdqgdehdu"), "iamapandabear")

    def test_random_key(self):
        cipher = Cipher()
        self.assertEqual(len(cipher.key), 100)

if __name__ == '__main__':
    unittest.main()