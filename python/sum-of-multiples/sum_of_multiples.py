def sum_of_multiples(limit, values=[]):
    return sum(set(v for val in values for v in range(val, limit, val)))
