class HighScores:
    def __init__(self, scores):

        self.scores = scores

    def highest_score(self):
        return max(self.scores) if self.scores else None

    def last_score(self):
        return self.scores[-1] if self.scores else None

    def three_highest_scores(self):
        return sorted(self.scores, reverse=True)[:3]
    
