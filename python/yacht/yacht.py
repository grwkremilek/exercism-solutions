from itertools import groupby

def multiply_numbers(number, dice):
    occurances = dice.count(number)
    return number * occurances

YACHT           = lambda dice : 50 if len(set(dice)) == 1 else 0
ONES            = lambda dice : multiply_numbers(1, dice)
TWOS            = lambda dice : multiply_numbers(2, dice)
THREES          = lambda dice : multiply_numbers(3, dice)
FOURS           = lambda dice : multiply_numbers(4, dice)
FIVES           = lambda dice : multiply_numbers(5, dice)
SIXES           = lambda dice : multiply_numbers(6, dice)
FULL_HOUSE      = lambda dice : sum(dice) if sorted([len(list(group)) for key, group in groupby(sorted(dice))]) == [2,3]  else 0
FOUR_OF_A_KIND  = lambda dice : 4 * (max(set(dice), key=dice.count)) if sorted([len(list(group)) for key, group in groupby(sorted(dice))]) in [[1,4], [5]] else 0
LITTLE_STRAIGHT = lambda dice : 30 if sum(set(dice)) == 15 else 0
BIG_STRAIGHT    = lambda dice : 30 if sum(set(dice)) == 20 else 0
CHOICE          = lambda dice : sum(dice)

def score(dice, category):
    return category(dice)
