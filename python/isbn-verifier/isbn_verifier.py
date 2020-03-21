def verify(isbn):
    count = 1; total = 0
    for i in reversed(isbn):
        if i is 'X':
            if count != 1:return False
            i = '10'
        if i.isdigit():
            total += int(i) * count
            count += 1
    return count == 11 and total % 11 == 0
