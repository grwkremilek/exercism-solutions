def prime_factors(natural_number):
    
    prime_numbers = []
    if 1 < natural_number:
        f = 2
        while f < natural_number:
            q, r = divmod(natural_number, f)
            if r == 0:
                prime_numbers.append(f)
                natural_number = q
            else:
                f +=1
        prime_numbers.append(natural_number)
    return prime_numbers


