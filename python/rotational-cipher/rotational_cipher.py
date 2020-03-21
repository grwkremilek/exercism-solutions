import string

def rotate(message, key):
    lower, upper = string.ascii_lowercase, string.ascii_uppercase
    d = dict(zip(lower + upper, lower[key:] + lower[:key] + upper[key:] + upper[:key]))
    return ''.join(d[m] if m in d else m for m in message)
