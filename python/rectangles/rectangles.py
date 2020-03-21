import itertools

def get_indexes(inp, symbol):
    '''Returns indexes of all cases of the symbol given'''
    indexes = []
    for ind_0, sub in enumerate(inp):
        for ind_1, i in enumerate(sub):
            if i == symbol:
                indexes.append([ind_0, ind_1])
    return indexes

def corners(inp):
    '''Returns all possible fours creating corners of the rectangles'''
    corners = []
    indexes = get_indexes(inp, "+")
    combos = list(itertools.combinations(indexes, 4))
    for com in combos:
        r = []; t = []
        for i in com:
            r.append(i[0]); t.append(i[1])
        if len(set(r)) == 2 and len(set(t)) == 2:
            corners.append(com)
    return corners


def bars(inp, rectangle):
    '''Returns if rectangle true'''
    # upper line
    if rectangle[0][0] == rectangle[1][0]:
        for i in range(rectangle[0][1]+1, rectangle[1][1]):
            if inp[rectangle[0][0]][i] == '-' or inp[rectangle[0][0]][i] == '+':
                continue
            else:
                return False
    #bottom line
    if rectangle[2][0] == rectangle[3][0]:
        for i in range(rectangle[2][1]+1, rectangle[3][1]):
            if inp[rectangle[2][0]][i] == '-' or inp[rectangle[2][0]][i] == '+':
                continue
            else:
                return False
    s_rectangle = sorted(rectangle, key=lambda tup: tup[1])
    #left side
    if s_rectangle[0][1] == s_rectangle[1][1]:
        for i in range(s_rectangle[0][0]+1, s_rectangle[1][0]):
            if inp[i][s_rectangle[0][1]] == '|' or inp[i][s_rectangle[0][1]] == '+':
                continue
            else:
                return False
    #right side
    if s_rectangle[2][1] == s_rectangle[3][1]:
        for i in range(s_rectangle[2][0]+1, s_rectangle[3][0]):
            if inp[i][s_rectangle[2][1]] == '|' or inp[i][s_rectangle[2][1]] == '+':
                continue
            else:
                return False
    return True

def count(inp):
    '''Main coordianting function, returns the number of rectangles'''
    rect_count = 0
    ind_corners = corners(inp)
    for rectangle in ind_corners:
        if bars(inp, rectangle) == True:
            rect_count += 1
    return rect_count
