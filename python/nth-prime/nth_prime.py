def nth_prime(positive_number):
    if positive_number < 1:
        raise ValueError("Number must be higher than 1")
    primes = [2]; n = 3
    
    while len(primes) < positive_number:
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.append(n)
        n += 2
    return primes[-1]
