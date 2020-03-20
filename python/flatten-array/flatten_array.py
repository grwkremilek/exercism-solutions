
def flatten(inp):
    lst = []
    if type(inp) is str:
        return list(inp)
    else:
        [lst.append(elem) if type(elem) is int else lst.extend(flatten(elem)) for elem in inp if elem is not None]
        return lst
