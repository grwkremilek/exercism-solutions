class Queen(object):
    def __init__(self, row, column):
        if not (0 <= row < 8 and 0 <= column < 8):
            raise ValueError("Input values outside the range")
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Incorrect input values")
        return self.row == another_queen.row or self.column == another_queen.column or abs(self.row - another_queen.row) == abs(self.column - another_queen.column)
