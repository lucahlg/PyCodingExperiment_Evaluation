class HighScores:
    def __init__(self, scores):
        self.scores = scores
        pass

        def latest(self):
        return self.scores[-1]
        pass

        def personal_best(self):
        return max(self.scores)
        pass
    
        def personal_top_three(self):
        return sorted(self.scores, reverse=True)[:3]
        pass