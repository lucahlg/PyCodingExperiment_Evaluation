# Game status categories
# Change the values as you see fit
from rx import subject
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.guessed_chars = set()
        self.word_masked = '_' * len(word)
        self.guess_observable = subject.Subject()
        self.guess_observable.subscribe(self.process_guess)

    def guess(self, char):
        self.guess_observable.on_next(char)
        
    def process_guess(self, char):
        if char in self.word and char not in self.guessed_chars:
            self.guessed_chars.add(char)
            self.word_masked = ''.join(
                [c if c in self.guessed_chars else '_' for c in self.word]
            )
            if '_' not in self.word_masked:
                self.status = STATUS_WIN
        else:
            self.remaining_guesses -= 1
            if self.remaining_guesses <= 0:
                self.status = STATUS_LOSE
        

    def get_masked_word(self):
        return self.word_masked

    def get_status(self):
        return self.status

    # Removed duplicate method
