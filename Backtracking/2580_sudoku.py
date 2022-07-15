sudoku = []
for i in range(9):
    sudoku.append(list(map(int, input().split())))


def check_sudoku(row, col, target):
    global sudoku
    row_num = sudoku[row]
    col_num = []
    for i in range(9):
        col_num.append(sudoku[i][col])
    block_x = (row//3)*3
    block_y = (col//3)*3
    block_num = []
    for i in range(block_x, block_x+3):
        for j in range(block_y, block_y+3):
            block_num.append(sudoku[i][j])
    if target in row_num or target in col_num or target in block_num:
        return False
    else:
        return True


