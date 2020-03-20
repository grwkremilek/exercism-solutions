
def is_armstrong(number):
    return sum(pow(int(i), len(str(number))) for i in str(number)) == number
