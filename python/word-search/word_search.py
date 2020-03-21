import copy


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({):{}'.format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return Point(self.x == other.x, self.y == other.y)

    def __ne__(self, other):
        return not(self == other)


DIRECTIONS = (Point(1,0), Point(1, -1), Point(1,1), Point(-1, -1),
              Point(0, -1), Point(0, 1), Point(-1,1), Point(-1,0))


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.width = len(self.puzzle[0])
        self.height = len(self.puzzle)

    def find_char(self, coordinate):
        if coordinate.x < 0 or coordinate.x >= self.width:
            return
        if coordinate.y < 0 or coordinate.y >= self.height:
            return
        return self.puzzle[coordinate.y][coordinate.x]

    def find(self, input, position, direction):
        current = copy.copy(position)
        for letter in input:
            if self.find_char(current) != letter:
                return
            current += direction
        return position, current - direction

    def search(self, input):
        position = (Point(x,y) for x in range(self.width) for y in range(self.height))
        for pos in position:
            for d in DIRECTIONS:
                result = self.find(input, pos, d)
                if result:
                    return result
        return None
