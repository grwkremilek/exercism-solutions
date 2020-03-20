alphabet = 'abcdefghijklmnopqrstuvwxyz'
m = len(alphabet)

def encode(plain_text, a, b):
    if are_coprime(a, m):
        result = ''
        for i in plain_text.lower():
            if i.isalpha():
                result += alphabet[(a * alphabet.index(i) + b) % m]
            elif i.isdigit():
                result += i
        return " ".join([result[i:i+5] for i in range(0, len(result), 5)])
    raise ValueError("Error: a and m must be coprime.")


def decode(ciphered_text, a, b):
    if are_coprime(a, m):
        result = ''
        for i in ciphered_text:
            if i.isalpha():
                v = int((mmi(a)*(alphabet.index(i) - b)) % m)
                result += alphabet[v]
            elif i.isdigit():
                result += i
        return result
    raise ValueError("Error: a and m must be coprime.")


def are_coprime(a, b):
    while b != 0:
        a, b = b, a % b
    return a == 1


def mmi(a):
    n = 1
    while (n * a) % m != 1:
        n += 1
    return n
