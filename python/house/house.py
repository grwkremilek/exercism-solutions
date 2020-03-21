POEM =  {   1 : [ 'house', 'Jack built.' ],
            2 : [ 'malt', 'lay in the'],
            3 : [ 'rat', 'ate the' ],
            4 : [ 'cat', 'killed the'],
            5 : [ 'dog', 'worried the'],
            6 : [ 'cow with the crumpled horn', 'tossed the'],
            7 : [ 'maiden all forlorn', 'milked the'],
            8 : [ 'man all tattered and torn', 'kissed the'],
            9 : [ 'priest all shaven and shorn', 'married the'],
            10 :[ 'rooster that crowed in the morn', 'woke the'],
            11 :[ 'farmer sowing his corn', 'kept the'],
            12 :[ 'horse and the hound and the horn', 'belonged to the'] }

def get_verse(verse_num):
    return POEM[verse_num][0] + ' that ' + POEM[verse_num][1]

def recite(start_verse, end_verse):
    result = []
    for i in range(start_verse, end_verse+1):
        r = ''
        while i >= 1:
            r += ' ' + get_verse(i)
            i -= 1
        result.append('This is the' +  r)
    return result
