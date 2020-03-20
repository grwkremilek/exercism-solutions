import itertools

def extract_letters(words):
    letters = []
    for w in words:
        for l in w:
            if l.isalpha() and l not in letters:
                letters.append(l)
    return letters

def solve(puzzle):
    words = puzzle.split(' ')
    letters = extract_letters(words)
    for combo in list(itertools.permutations([0,1,2,3,4,5,6,7,8,9], len(letters))):
        d = dict(zip(letters, combo))
        all_s = ''
        for w in words:
            s = ''
            for l in w:
                s += str(d[l]) if l.isalpha() else str(l)
            if (len(s) > 1 and s == len(s) * '0') or (len(s) > 1 and s[0] == '0'):
                break
            else:
                all_s += s
            if '==' in all_s and all_s[-1].isdigit() and eval(all_s):
                return d
    return {}

