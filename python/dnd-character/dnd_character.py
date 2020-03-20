import math
import random
from random import randrange


def modifier(num):
    return math.floor((num-10)/ 2)

class Character:

    def __init__(self):
        self.strength = self._get_score(self._roll_dice())
        self.dexterity = self._get_score(self._roll_dice())
        self.constitution = self._get_score(self._roll_dice())
        self.intelligence = self._get_score(self._roll_dice())
        self.wisdom = self._get_score(self._roll_dice())
        self.charisma = self._get_score(self._roll_dice())
        self.hitpoints = 10 + modifier(self.constitution)
        
    def _roll_dice(self):
        dice_rolls = []
        for i in range(5):
            dice_rolls.append(randrange(1, 7))
        return dice_rolls
    
    def _get_score(self, dice_rolls):
        return sum(sorted(dice_rolls[:3]))
        
    def ability(self):
        return random.choice([self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma])
