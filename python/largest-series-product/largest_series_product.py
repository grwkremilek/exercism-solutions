from functools import reduce

def largest_product(string, size):
    if size < 0:
        raise ValueError("Substring length must be positive.")
    elif size == 0:
        return 1
    l = len(string)//size*size
    return max([product(string[i:i+size]) for i in range(0, l, 1)])

def product(chunk):
    return reduce(lambda x, y: x*y, [int(num) for num in chunk])
