def board(board_array):
    if any(len(row) != len(board_array[0]) for row in board_array[1:]):
        raise ValueError("Rows of different lengths!")
    
    for row_index, row in enumerate(board_array):
        for col_index, col in enumerate(row):
            if board_array[row_index][col_index] == ' ':
                count = 0
                if row_index-1 >= 0 and board_array[row_index-1][col_index] == '*':
                    count += 1
                if row_index+1 < len(board_array) and board_array[row_index+1][col_index] == '*':
                    count += 1
                if col_index-1 >= 0 and board_array[row_index][col_index-1] == '*':
                    count += 1
                if col_index+1 < len(row) and board_array[row_index][col_index+1] == '*':
                    count += 1
                if row_index-1 >= 0 and col_index-1 >= 0 and board_array[row_index-1][col_index-1] == '*':
                    count += 1
                if row_index+1 < len(board_array) and col_index+1 < len(row) and board_array[row_index+1][col_index+1] == '*':
                    count += 1
                if row_index-1 >= 0 and col_index+1 < len(row) and board_array[row_index-1][col_index+1] == '*':
                    count += 1
                if row_index+1 < len(board_array) and col_index-1 >= 0 and board_array[row_index+1][col_index-1] == '*':
                    count += 1
                if count > 0:
                    ba_list = list(board_array[row_index])
                    ba_list[col_index] = str(count)
                    board_array[row_index] = ''.join(ba_list)
            elif board_array[row_index][col_index] != '*':
                raise ValueError("Invalid character!")
    return board_array


