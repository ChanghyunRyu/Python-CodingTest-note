from itertools import combinations
import copy


def spread_virus(laboratory):
    for i in range(len(laboratory)):
        for j in range(len(laboratory[i])):
            if laboratory[i][j] == 2:
                dfs(i, j, laboratory)

    result = 0
    for i in range(len(laboratory)):
        for j in range(len(laboratory[i])):
            if laboratory[i][j] == 0:
                result += 1
    return result


def dfs(x, y, laboratory):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        check = 0 <= nx < len(laboratory) and 0 <= ny < len(laboratory[0])
        if not check or laboratory[nx][ny] != 0:
            continue
        laboratory[nx][ny] = 2
        dfs(nx, ny, laboratory)


n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

points = [(i, j) for i in range(n) for j in range(m)]

answer = 0
for com in combinations(points, 3):
    new_board = copy.deepcopy(board)
    flag = True
    for x, y in com:
        if new_board[x][y] == 1 or new_board[x][y] == 2:
            flag = False
            break
        else:
            new_board[x][y] = 1
    if flag:
        answer = max(answer, spread_virus(new_board))
print(answer)
