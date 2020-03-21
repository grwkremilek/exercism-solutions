def get_palindromes(mx, mn):
    d = dict()
    for i in range(mn, mx+1):
        for j in range(i,mx+1):
            if i*j == int(str(i*j)[::-1]):
                if i*j in d:
                    d[i*j].append((i,j))
                else:
                    d[i*j] = [(i,j)]
    return d

def largest_palindrome(max_factor, min_factor):
    palindromes = get_palindromes(max_factor,min_factor)
    return (max(palindromes), palindromes[max(palindromes)])

def smallest_palindrome(max_factor, min_factor):
    palindromes = get_palindromes(max_factor,min_factor)
    return (min(palindromes), palindromes[min(palindromes)])

