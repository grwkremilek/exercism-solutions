from re import sub
from itertools import groupby

def decode(string):
    return sub(r'(\d+)(\D)', lambda x: int(x.group(1)) * x.group(2), string)

def encode(string):
    chunks = [''.join(s) for _, s in groupby(string)]
    res = [c if len(c) == 1 else str(len(c))+c[0] for c in chunks]
    return "".join(res)
