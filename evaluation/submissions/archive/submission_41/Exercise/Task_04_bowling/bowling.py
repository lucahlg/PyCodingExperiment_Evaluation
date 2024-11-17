class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        total_score = 0
        frame_index = 0
        for frame in range(10):
            if frame_index >= len(self.rolls):
                break
            if self.rolls[frame_index] == 10:  # Strike
                total_score += 10
                if frame_index + 1 < len(self.rolls):
                    total_score += self.rolls[frame_index + 1]
                if frame_index + 2 < len(self.rolls):
                    total_score += self.rolls[frame_index + 2]
                frame_index += 1
            elif frame_index + 1 < len(self.rolls) and self.rolls[frame_index] + self.rolls[frame_index + 1] == 10:  # Spare
                total_score += 10 + (self.rolls[frame_index + 2] if frame_index + 2 < len(self.rolls) else 0)
            frame_index += 2
                frame_index += 2
                frame_index += 2
            else:
                total_score += (self.rolls[frame_index] + self.rolls[frame_index + 1] if frame_index + 1 < len(self.rolls) else 0)
                frame_index += 2
        return total_score
