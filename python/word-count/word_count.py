import re

def word_count(inp):
    inp = inp.replace(",", " ").replace("_", " ").replace(":", " ").replace(".", " ").lower()
    inp = ' '.join(w.strip("'") for w in inp.split())
    inp = re.sub("[^a-zA-Z0-9' ]+", ' ', inp)
    counts = dict()
    for i in inp.split():
        counts[i] = counts.get(i, 0) + 1
    return counts
