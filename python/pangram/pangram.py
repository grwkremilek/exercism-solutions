from string import ascii_lowercase

def is_pangram(inp):
    return all(char in inp.lower() for char in ascii_lowercase)
