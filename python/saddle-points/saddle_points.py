def saddle_points(matrix):
    if any(len(row) != len(matrix[0]) for row in matrix[1:]):
        raise ValueError("Rows of different lengths!")

    rows, columns = matrix, list(zip(*matrix))
    return { (x,y)
            for x, row in enumerate(matrix)
                for y in range(len(row))
                    if max(row) == min(columns[y])
            }
