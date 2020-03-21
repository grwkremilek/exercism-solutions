import random
from datetime import datetime

ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '1234567890'

class Robot():
    def __init__(self):
        self.name_generator()

    def name_generator(self):
        random.seed(datetime.now())
        self.name = random.choice(ABC) + random.choice(ABC) + random.choice(digits) + random.choice(digits) + random.choice(digits)
        return self.name

    def reset(self):
        return self.name_generator()

