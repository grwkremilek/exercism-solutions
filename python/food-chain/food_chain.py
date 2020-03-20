animals = [ 'fly','spider', 'bird', 'cat', 'dog', 'goat', 'cow', 'horse' ]

second_lines = [    "It wriggled and jiggled and tickled inside her.",
                    "How absurd to swallow a bird!",
                    "Imagine that, to swallow a cat!",
                    "What a hog, to swallow a dog!",
                    "Just opened her throat and swallowed a goat!",
                    "I don't know how she swallowed a cow!"     ]


def generate_middlelines(x):
    middle_lines = []
    while x > 0:
        if x == 2:
            middle_lines.append(f"She swallowed the {animals[x]} to catch the {animals[x-1]} that wriggled and jiggled and tickled inside her.")
        else:
            middle_lines.append(f"She swallowed the {animals[x]} to catch the {animals[x-1]}.")
        x -= 1
    return middle_lines


def recite(start_verse, end_verse):
    result = []
    while end_verse >= start_verse:
        result.append(f"I know an old lady who swallowed a {animals[start_verse-1]}.")
        if 1 < start_verse < 8:
            result.append(second_lines[start_verse-2])
            result += generate_middlelines(start_verse-1)
        if start_verse < 8:
            result.append("I don't know why she swallowed the fly. Perhaps she'll die.")
        else:
            result.append("She's dead, of course!")
        if start_verse != end_verse:
            result.append("")
        start_verse += 1
        recite(start_verse, end_verse)
    return result
