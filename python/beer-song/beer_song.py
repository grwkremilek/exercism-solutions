
def format_line1(start):
    line_1  = { 0 : "No more bottles of beer on the wall, no more bottles of beer.",
                1 : f'{start} bottle of beer on the wall, {start} bottle of beer.' }
    return line_1.get(start, f'{start} bottles of beer on the wall, {start} bottles of beer.')

def format_line2(start):
    line_2 = {  0 : "Go to the store and buy some more, 99 bottles of beer on the wall.",
                1 : "Take it down and pass it around, no more bottles of beer on the wall.",
                2 : f'Take one down and pass it around, {start-1} bottle of beer on the wall.' }
    return line_2.get(start, f'Take one down and pass it around, {start-1} bottles of beer on the wall.')
    
def recite(start, take=1):
    result = []
    for i in range(take):
        if len(result) > 0:
            result.append("")
        result.append(format_line1(start))
        result.append(format_line2(start))
        start -= 1
    return result

