
def to_decimal(input_base, digits):
    return sum([d * input_base ** ind for ind, d in enumerate(digits[::-1])])
    
    
def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError('invalid input base')
    elif output_base < 2:
        raise ValueError('invalid output base')
    elif any(filter(lambda x: x < 0 or x >= input_base, digits)):
        raise ValueError('invalid digit')
    d = to_decimal(input_base, digits)
    res = []
    while d:
        d, r = divmod(d, output_base)
        res.append(r)
    return list(res[::-1])
