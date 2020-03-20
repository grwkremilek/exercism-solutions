import re
import math

def remove_punctuation(text):
    text = re.sub("[^a-zA-Z0-9_]+", "", text)
    return text.lower().replace(" ", "")
    
def find_parameters(text):
    sqrt = int(math.sqrt(len(text)))
    if sqrt ** 2 >= len(text):
        row = col = sqrt
    elif sqrt * (sqrt + 1) >= len(text):
        row = sqrt
        col = sqrt + 1
    elif (sqrt + 1) ** 2 >= len(text):
        row = col = sqrt + 1
    return (row, col)
    
def create_rectangle(text, row, col):
    output = []
    for i in range(col):
        output.append([])
    for i in range(len(text)):
        output[i % col].append(text[i])
    for line in output:
        while len(line) < row:
            line.append(' ')
    return ' '.join([''.join(output[i]) for i in range(len(output))])

def encode(plain_text):
    depunctuated_text = remove_punctuation(plain_text)
    if len(depunctuated_text) < 2:
        return depunctuated_text
    row, col = find_parameters(depunctuated_text)
    return create_rectangle(depunctuated_text, row, col)

