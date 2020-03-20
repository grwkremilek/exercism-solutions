alpha = list(map(chr, range(65, 91)))

def make_diamond(letter):    
    letters = alpha[:alpha.index(letter)+1]
    width = 2 * len(alpha[:alpha.index(letter)+1])-1
    diamond = []
    for index, letter in enumerate(letters):
        if index:
            diamond.append((letter + " " * (index * 2 - 1) + letter).center(width))
        else:
            diamond.append(letter.center(width))
    return "\n".join(diamond + diamond[:-1][::-1]) + "\n"

