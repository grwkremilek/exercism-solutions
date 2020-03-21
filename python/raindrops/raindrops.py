
def raindrops(number):
    factors = { 3 : 'Pling', 5 : 'Plang', 7 : 'Plong' }
    res = [v for k, v in factors.items() if number % k == 0]
    return ''.join(res) or str(number)
