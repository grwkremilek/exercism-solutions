from math import sqrt

def score(x, y):
    r = sqrt(x**2 + y**2)
    if r > 10:
        return 0
    elif r > 5:
        return 1
    elif r > 1:
        return 5
    return 10
