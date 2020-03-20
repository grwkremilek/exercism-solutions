class BowlingGame(object):

    def __init__(self):
        self.frame = []
        self.current_frame = 0
        self.bonus_points = []
        self._score = 0

    def roll(self, pins):
        if pins < 0:
            raise ValueError("Negative input")
        if not self.keep_play():
            raise IndexError("Game is over")

        self.frame.append(pins)
        if sum(self.frame) > 10:
            raise ValueError("Input Too high")

        self._score += len(self.bonus_points) * pins
        self.bonus_points = [1 for i in self.bonus_points if i == 2]

        if self.current_frame < 10:
            self._score += pins
            if sum(self.frame) == 10:
                self.bonus_points.append(3-len(self.frame))             # Number of times bonus points will be added.

        if self.keep_play() and self.frame_over():
            self.current_frame += 1
            self.frame = []

    def score(self):
        if self.keep_play():
            raise IndexError("Game not over")
        return self._score

    def frame_over(self):
        return len(self.frame) == 2 or sum(self.frame) == 10

    def keep_play(self):
        return self.current_frame < 10 or self.bonus_points
