VOWELS = 'aeiou'

def translate_word(word):
    while word[0] not in VOWELS:
        if word[1] not in VOWELS and word[0] in 'xy' :
            break
        word = reorder_word(word)
    if word.startswith('u') and word.endswith('q'):
        word = reorder_word(word)
    return word + 'ay'

def reorder_word(word):
    return word[1:] + word[0]

def translate(text):
    return ' '.join([translate_word(word) for word in text.split()])
