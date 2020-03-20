def collatz_steps(number):
    if number < 1:
        raise ValueError("Number is not valid")
    steps = 0
    while number > 1:
        number = number/2 if number%2==0 else (number*3)+1
        steps +=1
    return steps
