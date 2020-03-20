def test_integer(func):
    def wrapper(integer_number):
        if 0 < integer_number < 65:
            return func(integer_number)
        raise ValueError('Input must be between 0-64.')
    return wrapper

@test_integer
def on_square(integer_number):
    return 1 << (integer_number-1)

@test_integer
def total_after(integer_number):
    return (1 << integer_number)-1
