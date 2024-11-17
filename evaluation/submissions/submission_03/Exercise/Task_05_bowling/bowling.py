class BowlingGame:
    def __init__(self):
        pass
    def roll(self, pins):
        self.rolls.append(pins)
    def roll(self, pins):
        self.rolls.append(pins)
    def roll(self, pins):
    def score(self):
        total_score = 0
        frame_index = 0

        for frame in range(10):
            if self.rolls[frame_index] == 10:  # Strike
                total_score += 10 + self.rolls[frame_index + 1] + self.rolls[frame_index + 2]
                frame_index += 1
            elif self.rolls[frame_index] + self.rolls[frame_index + 1] == 10:  # Spare
                total_score += 10 + self.rolls[frame_index + 2]
                frame_index += 2
            else:  # Open frame
                total_score += self.rolls[frame_index] + self.rolls[frame_index + 1]
                frame_index += 2

        return total_score
        self.rolls.append(pins)
    def roll(self, pins):
    def score(self):
        total_score = 0
        frame_index = 0

        for frame in range(10):
            if self.rolls[frame_index] == 10:  # Strike
                total_score += 10 + self.rolls[frame_index + 1] + self.rolls[frame_index + 2]
                frame_index += 1
            elif self.rolls[frame_index] + self.rolls[frame_index + 1] == 10:  # Spare
                total_score += 10 + self.rolls[frame_index + 2]
                frame_index += 2
            else:  # Open frame
                total_score += self.rolls[frame_index] + self.rolls[frame_index + 1]
                frame_index += 2

        return total_score
        self.rolls.append(pins)

    def score(self):
        total_score = 0
        frame_index = 0

        for frame in range(10):
            if self.rolls[frame_index] == 10:  # Strike
                total_score += 10 + self.rolls[frame_index + 1] + self.rolls[frame_index + 2]
                frame_index += 1
            elif self.rolls[frame_index] + self.rolls[frame_index + 1] == 10:  # Spare
                total_score += 10 + self.rolls[frame_index + 2]
                frame_index += 2
            else:  # Open frame
                total_score += self.rolls[frame_index] + self.rolls[frame_index + 1]
                frame_index += 2

        return total_score
    def roll(self, pins):
        pass
    def score(self):
        total_score = 0
        frame_index = 0

        for frame in range(10):
            if self.rolls[frame_index] == 10:  # Strike
                total_score += 10 + self.rolls[frame_index + 1] + self.rolls[frame_index + 2]
                frame_index += 1
            elif self.rolls[frame_index] + self.rolls[frame_index + 1] == 10:  # Spare
                total_score += 10 + self.rolls[frame_index + 2]
                frame_index += 2
            else:  # Open frame
                total_score += self.rolls[frame_index] + self.rolls[frame_index + 1]
                frame_index += 2

        return total_score

    def score(self):
        pass
