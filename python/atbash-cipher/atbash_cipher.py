import string
import re

transtab = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[::-1], string.punctuation + string.whitespace)

def encode(string):
    transstring = string.lower().translate(transtab)
    return ' '.join(re.findall(r'.{1,5}', transstring))
    
def decode(string):
    return string.translate(transtab)

