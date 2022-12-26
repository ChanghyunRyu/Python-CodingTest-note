# 착각했던 부분 1: 파이썬 for 문은 c++이나 자바처럼 숫자가 증가하는 것이 아닌 리스트를 하나씩 흩는 것이다 => while문으로 변경
# 착각했던 부분 2: 계속해서 뒤로 돌아가면서, 상태를 초기화하지 않아서 답이 나오지 않는 경우가 더러 생겼다.
import sys

sudoku = []
for i in range(9):
    line = list(map(int, sys.stdin.readline().split()))
    sudoku.append(line)
pn_row = [set([1, 2, 3, 4, 5, 6, 7, 8, 9]) for i in range(9)]
pn_col = [set([1, 2, 3, 4, 5, 6, 7, 8, 9]) for i in range(9)]
pn_box = [set([1, 2, 3, 4, 5, 6, 7, 8, 9]) for i in range(9)]

already_try = {}
for i in range(9):
    for j in range(9):
        if sudoku[i][j] != 0:
            pn_row[i].remove(sudoku[i][j])
            pn_col[j].remove(sudoku[i][j])
            box_num = ((i//3)*3) + (j//3)
            pn_box[box_num].remove(sudoku[i][j])
        else:
            already_try[(i, j)] = set()
i = j = 0
tasks = []
while i < 9 and j < 9:
    if sudoku[i][j] == 0:
        pn = list((pn_row[i] & pn_col[j] & pn_box[((i // 3) * 3) + (j // 3)]) - already_try[(i, j)])
        if len(pn) > 0:
            number = pn[0]
            sudoku[i][j] = number
            pn_row[i].remove(number)
            pn_col[j].remove(number)
            pn_box[((i // 3) * 3) + (j // 3)].remove(number)
            tasks.append((i, j))
        else:
            already_try[(i, j)] = set()
            bt = tasks.pop()
            br = bt[0]
            bc = bt[1]
            bn = sudoku[br][bc]
            already_try[(br, bc)].add(bn)
            pn_row[br].add(bn)
            pn_col[bc].add(bn)
            pn_box[((br // 3) * 3) + (bc // 3)].add(bn)
            sudoku[br][bc] = 0
            i = br
            j = bc
            continue
    j += 1
    if j == 9:
        i += 1
        j = 0

for row in range(9):
    for col in range(9):
        print(sudoku[row][col], end=' ')
    print()

