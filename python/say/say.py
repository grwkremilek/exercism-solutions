NUMS = [ 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen' ]
DECS = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def say(number):
    if 0 <= number < 20:
        return NUMS[number]
    elif 20 <= number < 100:
        ten, remain = divmod(number, 10)
        return DECS[ten] + ('-' + say(remain) if remain > 0 else '')
    elif 100 <= number < 1e3:
        hundred, remain = divmod(number, 100)
        return NUMS[hundred] + ' hundred' + (' and ' + say(remain) if remain > 0 else '') 
    elif 1e3 <= number < 1e6:
        thousand, remain = divmod(number, 1000)
        return say(thousand) + ' thousand' + (' ' + say(remain) if remain > 0 else '') 
    elif 1e6 <= number < 1e9:
        million, remain = divmod(int(number), 1000000)
        return say(million) + ' million' + (' ' + say(remain) if remain > 0 else '')
    elif 1e9 <= number < 1e12:
        billion, remain = divmod(int(number), 1000000000)
        return say(billion) + ' billion' + (' ' + say(remain) if remain > 0 else '')
    raise ValueError("Incorrect input values")
