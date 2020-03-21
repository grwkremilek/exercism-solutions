import math

def sieve(max_num):
    if max_num == 0 or max_num == 1:
        return []
    candidates = [True] * (max_num)
    candidates[0]  = False
    for i in range(2, int(math.sqrt(max_num)+1)):
        if candidates[i-1] == True:
            for j in range(i*i, max_num+1, i):
                candidates[j-1] = False
    return [i+1 for i, c in enumerate(candidates) if c == True]
