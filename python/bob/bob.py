
def hey(inp):
    inp = inp.strip()
    if not inp:
        return "Fine. Be that way!"
    elif inp.isupper():
        if inp.endswith('?'):
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    elif inp.endswith('?'):
            return "Sure."
    return "Whatever."
