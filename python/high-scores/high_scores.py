class HighScores:
    def __init__(self, scores):
        self.scores = scores
    
    def latest(self):
        return self.scores[-1]
    
    def highest(self):
        return max(self.scores)
    
    def top(self):
        sorted_list = sorted(self.scores, reverse = True)
        if len(sorted_list) < 3:
            return sorted_list
        return sorted_list[:3]

    def report(self):
        if self.latest() ==  self.highest():
            return "Your latest score was {}. That's your personal best!".format(self.latest())
        return "Your latest score was {}. That's {} short of your personal best!".format(self.latest(), self.highest() - self.latest())
