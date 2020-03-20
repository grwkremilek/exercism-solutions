OPEN = '{[('
CLOSE = '}])'
MATCH_MAP = dict(zip(CLOSE, OPEN))

def is_paired(inp):
    stack = []
    for i in inp:
        if i in OPEN:
            stack.append(i)
        if i in CLOSE and (not stack or stack.pop() != MATCH_MAP[i]):
            return False
    return not stack
