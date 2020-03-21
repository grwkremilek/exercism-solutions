
def is_isogram(string):
    string_lower = [i.lower() for i in string if i.isalpha()]
    return len(string_lower) == len(set(string_lower))
