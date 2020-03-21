LETTER_SCORES = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

def score(word):
    score = 0
    for char in word.lower():
        score += LETTER_SCORES[ord(char)-ord('a')]
    return score
