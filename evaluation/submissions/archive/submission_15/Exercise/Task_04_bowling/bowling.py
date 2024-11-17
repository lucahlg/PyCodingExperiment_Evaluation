class BowlingGame:
    def __init__(self):
        self.frames = []
        self.current_frame = []
        pass

    def roll(self, pins):
        self.current_frame.append(pins)
        if len(self.current_frame) == 2 or pins == 10:
            self.frames.append(self.current_frame)
            self.current_frame = []
        pass

    def score(self):
        total_score = 0
        for i, frame in enumerate(self.frames):
            frame_score = sum(frame)
            if len(frame) == 2 and frame_score == 10:
                frame_score += self.frames[i + 1][0] if i + 1 < len(self.frames) else 0
            elif len(frame) == 1:
                frame_score += sum(self.frames[i + 1]) if i + 1 < len(self.frames) else 0
            total_score += frame_score
        return total_score
        pass
