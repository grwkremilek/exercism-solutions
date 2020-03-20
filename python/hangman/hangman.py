STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"

class Hangman(object):
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.masked_word = ['_'] * len(self.word)
        self.used_char = []

    def guess(self, char):
        if self.get_status() == STATUS_ONGOING:
            if char in self.word and not char in self.used_char:
                self.used_char.append(char)
                self.update_maked_word(char)
            else:
                self.remaining_guesses -= 1
        else:
            raise ValueError("Game over. You", self.status)
    
    def update_maked_word(self, char):
        for ind, c in enumerate(self.word):
            if c == char:
                self.masked_word[ind] = c

    def get_masked_word(self):
        return "".join(self.masked_word)

    def get_status(self):
        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE
        elif "".join(self.masked_word) == self.word:
            self.status = STATUS_WIN
        return self.status
