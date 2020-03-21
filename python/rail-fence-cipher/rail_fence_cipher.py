from itertools import cycle

def get_pattern(n):
    r = list(range(n))
    return cycle(r + r[-2:0:-1])
    

def encode(message, rails):
    pttrn = get_pattern(rails)
    return ''.join(sorted(message, key=lambda i: next(pttrn)))



def decode(encoded_message, rails):
    pttrn = get_pattern(rails)
    return ''.join(sorted(encoded_message, key=lambda i: next(pttrn)))


print(decode('TEITELHDVLSNHDTISEIIEA', 3))
