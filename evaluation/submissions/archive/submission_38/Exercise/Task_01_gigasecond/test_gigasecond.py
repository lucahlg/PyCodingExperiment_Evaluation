import unittest
from datetime import datetime
from gigasecond import add

class TestGigasecond(unittest.TestCase):
    def test_gigasecond(self):
        self.assertEqual(
            add(datetime(2015, 1, 24, 22, 0, 0)),
            datetime(2046, 10, 2, 23, 46, 40)
        )

if __name__ == '__main__':
    unittest.main()