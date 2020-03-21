class Matrix:
    def __init__(self, matrix):
        self.rows = [[int(i) for i in row.split()] for row in matrix.split("\n")]
        self.columns = [list(j) for j in zip(*self.rows)]

    def row(self, num):
        return self.rows[num-1]
        
    def column(self, num):
        return self.columns[num-1]
