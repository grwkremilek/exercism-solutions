TEMPLATE_DIGITS =  [' _     _  _     _  _  _  _  _ ',
                    '| |  | _| _||_||_ |_   ||_||_|',
                    '|_|  ||_  _|  | _||_|  ||_| _|', 
                    '                              ']

def split_digits(digs):
    splits = [[] for i in range(len(digs[0])//3)]
    for row in digs:
        for i, j in enumerate(range(0, len(row), 3)):
            splits[i].append(row[j:j+3])
    return splits    

def convert_digit(digit):
    res = ''
    current = res
    for index, splt in enumerate(split_digits(TEMPLATE_DIGITS)):
        if splt == digit:
            res = res + str(index)
    if current  == res:
        res = '?'
    return res

def convert(input_grid):
    if len(input_grid) % 4 != 0 or any(len(x) % 3 != 0 for x in input_grid):
        raise ValueError("Incorrect grid size")
    lines = [input_grid[x:x+4] for x in range(0, len(input_grid), 4)]
    result = ''
    for line in lines:
        input_splits = split_digits(line)
        for inp_splt in input_splits:
            result = result + convert_digit(inp_splt)
        result += ','
    return result[:-1]
