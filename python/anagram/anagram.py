
def detect_anagrams(word, candidates):
    return [ c
             for c in candidates
             if _sort(c) == _sort(word)
             if c.lower() != word.lower() ]

def _sort(word):
    return sorted(word.lower())
