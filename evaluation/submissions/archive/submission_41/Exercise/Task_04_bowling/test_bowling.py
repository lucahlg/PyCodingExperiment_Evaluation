import unittest
from bowling import BowlingGame

class TestBowlingGame(unittest.TestCase):
    def test_open_frame(self):
        game = BowlingGame()
        game.roll(3)
        game.roll(4)
        self.assertEqual(game.score(), 7)

    def test_spare(self):
        game = BowlingGame()
        game.roll(5)
        game.roll(5)  # Spare
        game.roll(3)
        self.assertEqual(game.score(), 16)  # 5 + 5 + 6

    def test_strike(self):
        game = BowlingGame()
        game.roll(10)  # Strike
        game.roll(3)
        game.roll(4)
        self.assertEqual(game.score(), 24)  # 10 + 3 + 4

    def test_perfect_game(self):
        game = BowlingGame()
        for _ in range(12):  # 12 strikes
            game.roll(10)
        self.assertEqual(game.score(), 300)

    def test_tenth_frame_spare(self):
        game = BowlingGame()
        for _ in range(9):
            game.roll(1)
            game.roll(1)
        game.roll(5)
        game.roll(5)  # Spare in the last frame
        game.roll(3)
        self.assertEqual(game.score(), 23)

if __name__ == '__main__':
    unittest.main()