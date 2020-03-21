
GIFTS = ['twelve Drummers Drumming',
         'eleven Pipers Piping',
         'ten Lords-a-Leaping',
         'nine Ladies Dancing',
         'eight Maids-a-Milking',
         'seven Swans-a-Swimming',
         'six Geese-a-Laying',
         'five Gold Rings',
         'four Calling Birds',
         'three French Hens',
         'two Turtle Doves',
         'a Partridge in a Pear Tree']

ORDINALS = [None, 'first', 'second', 'third', 'fourth', 'fifth', 'sixth',
           'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']


def verse(day_number):
    gifts = GIFTS[-day_number:]
    if len(gifts) > 1:
        gifts[:-1] = [', '.join(gifts[:-1])]
    gifts = ', and '.join(gifts)
    return f'On the {ORDINALS[day_number]} day of Christmas my true love gave to me: {gifts}.'
    

def recite(start_verse, end_verse):
    return [verse(n) for n in range(start_verse, end_verse + 1)]

