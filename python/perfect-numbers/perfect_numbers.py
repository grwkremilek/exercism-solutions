def classify(number):
    if number > 0:
        if sum(get_factors(number)) == number:
            return "perfect"
        elif sum(get_factors(number)) > number:
            return "abundant"
        return "deficient"
    raise ValueError("Number out of range")

def get_factors(n):
    factors = []; i = 1
    while i * i < n:
        if n % i == 0:
            factors.append(i)
            if n // i != i and n // i != n:
                factors.append(n // i)
        i += 1
    return factors
